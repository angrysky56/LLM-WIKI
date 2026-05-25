# Phase 1 Implementation: EventBus + Operational State
**Status:** Ready to Implement
**Based on:** AGEM EventBus (agent-group-evolving-molecular-system-AGEM/src/orchestrator/) + Hermes conversation_loop.py analysis
**Target file:** `hermes_agent/agent/event_bus.py` and `hermes_agent/agent/operational_state.py`

---

## What Exists vs. What Needs to Be Built

### Hermes Current Plumbing (callback-based, one-way)

```python
# run_agent.py — already has these:
self._emit_status(message)    → status_callback("lifecycle", message)
self._emit_warning(message)   → status_callback("warn", message)
self._emit_auxiliary_failure  → status_callback("auxiliary_failure", ...)
```

This is a **callback funnel** — one emitter, multiple consumers via one callback registration. Not a pub/sub bus.

### Gap: No State Machine

```python
# conversation_loop.py — stateless retry tracking:
retry_count = 0
primary_recovery_attempted = False
# ...retry loop...
if agent._try_activate_fallback():
    retry_count = 0
    primary_recovery_attempted = False
    continue
```

This is **ad-hoc recovery**, not a state machine. No visible operational state, no state-transition events, no handlers that react to state changes.

---

## Files to Create

### 1. `hermes_agent/agent/event_bus.py` (~90 lines)

Port of AGEM EventBus to Python. Zero external dependencies.

```python
"""EventBus — async pub/sub for Hermes agent lifecycle events."""

from __future__ import annotations

import asyncio
import logging
from typing import Any, Callable, Dict, List

logger = logging.getLogger(__name__)

# Type alias for event handlers
EventHandler = Callable[[dict], Any]
# Unsubscribe function returned to caller
UnsubscribeFn = Callable[[], None]


class EventBus:
    """Async pub/sub event bus for Hermes agent events.

    Hermes events flow through this bus instead of the old callback-funnel
    pattern in run_agent.py (_emit_status, _emit_warning, status_callback).

    Not multi-process safe — all events stay in-process. For multi-agent
    coordination, route through gateway hooks.

    Example:
        bus = EventBus()
        bus.subscribe("hermes:turn-complete", on_turn_complete)
        bus.subscribe("hermes:state-transition", on_state_change)
        await bus.emit({"type": "hermes:turn-complete", "turn": 5, "ok": True})
    """

    def __init__(self) -> None:
        self._subscribers: Dict[str, List[EventHandler]] = {}

    def subscribe(self, event_type: str, handler: EventHandler) -> UnsubscribeFn:
        """Register a handler for an event type.

        Returns an unsubscribe function — call it to remove the handler.
        """
        if event_type not in self._subscribers:
            self._subscribers[event_type] = []
        self._subscribers[event_type].append(handler)

        def unsubscribe() -> None:
            handlers = self._subscribers.get(event_type, [])
            if handler in handlers:
                handlers.remove(handler)

        return unsubscribe

    async def emit(self, event: dict) -> None:
        """Dispatch event to all registered handlers concurrently."""
        event_type = event.get("type", "")
        handlers = self._subscribers.get(event_type, [])
        if not handlers:
            return
        await asyncio.gather(
            *(asyncio.create_task(asyncio.to_thread(handler, event)) for handler in handlers),
            return_exceptions=True,
        )

    def emit_sync(self, event: dict) -> None:
        """Synchronous emit for use in non-async code."""
        event_type = event.get("type", "")
        handlers = self._subscribers.get(event_type, [])
        for handler in handlers:
            try:
                result = handler(event)
                if asyncio.iscoroutine(result):
                    logger.warning("emit_sync called with async handler for %s", event_type)
            except Exception:
                logger.exception("Event handler error for %s", event_type)

    def subscriber_count(self, event_type: str) -> int:
        """Return number of handlers registered for an event type."""
        return len(self._subscribers.get(event_type, []))


# ── Singleton bus instance ──────────────────────────────────────────────────
# Module-level singleton. Import this in run_agent.py and wire it into AIAgent.
# Subagents get their own bus instance (no shared state between parent/child).

_bus: EventBus | None = None


def get_bus() -> EventBus:
    """Get or create the global EventBus singleton."""
    global _bus
    if _bus is None:
        _bus = EventBus()
    return _bus


def reset_bus() -> None:
    """Reset the global bus (for testing only)."""
    global _bus
    _bus = None
```

---

### 2. `hermes_agent/agent/operational_state.py` (~120 lines)

Hermes-specific state machine, adapted from AGEM's `OrchestratorStateManager`.
Thresholds are Hermes-specific (iteration budget, error rate).

```python
"""Operational state machine for Hermes agent.

Defines the visible operational state of the agent: STANDBY / ACTIVE /
DEGRADED / CRITICAL. Transitions are driven by Hermes metrics (iteration
budget, error rate, task completion).

Replaces the old ad-hoc retry-count tracking in conversation_loop.py with
a proper state machine that emits events on every transition.
"""

from __future__ import annotations

import logging
import time
from enum import Enum

from agent.event_bus import EventBus, get_bus

logger = logging.getLogger(__name__)


class HermesOperationalState(str, Enum):
    """Visible operational state of the Hermes agent.

    Transitions:
      STANDBY  → ACTIVE   : task begins
      ACTIVE   → DEGRADED: error rate exceeds threshold OR budget < 20%
      DEGRADED → ACTIVE  : successful turn completion
      DEGRADED → CRITICAL: budget exhaustion or cascading failures
      CRITICAL → STANDBY : task terminated, ready for new task
      ACTIVE   → STANDBY : task completed normally
    """

    STANDBY = "STANDBY"    # No active task, ready for new work
    ACTIVE = "ACTIVE"      # Task in progress, normal operation
    DEGRADED = "DEGRADED"  # Recoverable errors, increased monitoring
    CRITICAL = "CRITICAL"  # Unrecoverable or budget exhausted


# ── State transition events ─────────────────────────────────────────────────

StateTransitionEvent = dict  # {
#     "type": "hermes:state-transition",
#     "old_state": HermesOperationalState,
#     "new_state": HermesOperationalState,
#     "reason": str,
#     "timestamp": float,
# }


class OperationalStateManager:
    """State machine for Hermes operational state.

    Tracks STANDBY / ACTIVE / DEGRADED / CRITICAL transitions driven by:
      - Iteration budget remaining (fraction of max)
      - Consecutive error count
      - Task lifecycle events

    Emits ``hermes:state-transition`` events via the EventBus on every
    transition. No-op if new_state == current_state (idempotent guard).

    Example:
        mgr = OperationalStateManager(get_bus())
        mgr.on_task_started()         # STANDBY → ACTIVE
        mgr.on_error()                # ACTIVE → DEGRADED if threshold crossed
        mgr.on_turn_complete(ok=True) # DEGRADED → ACTIVE if recovering
    """

    def __init__(
        self,
        bus: EventBus | None = None,
        *,
        budget_warning_threshold: float = 0.20,  # < 20% budget → DEGRADED
        error_burst_threshold: int = 3,           # 3+ consecutive errors → DEGRADED
        critical_budget_threshold: float = 0.05,  # < 5% budget → CRITICAL
        critical_error_threshold: int = 6,        # 6+ consecutive errors → CRITICAL
    ) -> None:
        self._bus = bus or get_bus()
        self._state = HermesOperationalState.STANDBY
        self._last_transition_time = time.time()
        self._consecutive_errors = 0
        self._budget_warning_threshold = budget_warning_threshold
        self._error_burst_threshold = error_burst_threshold
        self._critical_budget_threshold = critical_budget_threshold
        self._critical_error_threshold = critical_error_threshold

    @property
    def state(self) -> HermesOperationalState:
        return self._state

    @property
    def last_transition_time(self) -> float:
        return self._last_transition_time

    def on_task_started(self) -> None:
        """Task begins — transition to ACTIVE from STANDBY."""
        self._transition(
            HermesOperationalState.ACTIVE,
            "Task started",
        )

    def on_task_completed(self) -> None:
        """Task completed normally — return to STANDBY."""
        self._consecutive_errors = 0
        self._transition(
            HermesOperationalState.STANDBY,
            "Task completed",
        )

    def on_task_terminated(self, reason: str = "terminated") -> None:
        """Task ended abnormally — return to STANDBY."""
        self._transition(
            HermesOperationalState.STANDBY,
            f"Task terminated: {reason}",
        )

    def on_turn_complete(self, ok: bool) -> None:
        """Process turn completion — update error streak, attempt recovery."""
        if ok:
            self._consecutive_errors = 0
            if self._state == HermesOperationalState.DEGRADED:
                # Successful turn while degraded → recover to ACTIVE
                self._transition(
                    HermesOperationalState.ACTIVE,
                    "Recovered: successful turn after degraded state",
                )
        else:
            self._consecutive_errors += 1
            self._maybe_transition_from_error()

    def on_budget_update(self, remaining_fraction: float) -> None:
        """Check if budget level warrants a state transition."""
        if remaining_fraction <= self._critical_budget_threshold:
            if self._state != HermesOperationalState.CRITICAL:
                self._transition(
                    HermesOperationalState.CRITICAL,
                    f"Budget critical: {remaining_fraction:.0%} remaining",
                )
        elif remaining_fraction <= self._budget_warning_threshold:
            if self._state == HermesOperationalState.ACTIVE:
                self._transition(
                    HermesOperationalState.DEGRADED,
                    f"Budget warning: {remaining_fraction:.0%} remaining",
                )

    def _maybe_transition_from_error(self) -> None:
        """Evaluate error count and transition if thresholds crossed."""
        errors = self._consecutive_errors
        state = self._state

        if state == HermesOperationalState.CRITICAL:
            # Already critical — only recover through explicit task end
            return

        if errors >= self._critical_error_threshold:
            self._transition(
                HermesOperationalState.CRITICAL,
                f"Critical error burst: {errors} consecutive failures",
            )
        elif errors >= self._error_burst_threshold:
            if state == HermesOperationalState.ACTIVE:
                self._transition(
                    HermesOperationalState.DEGRADED,
                    f"Error burst: {errors} consecutive failures",
                )

    def _transition(
        self,
        new_state: HermesOperationalState,
        reason: str,
    ) -> None:
        """Execute state transition. Idempotent if new_state == current."""
        if new_state == self._state:
            return

        old_state = self._state
        self._state = new_state
        self._last_transition_time = time.time()

        logger.info("[OP-STATE] %s → %s: %s", old_state.value, new_state.value, reason)

        event: StateTransitionEvent = {
            "type": "hermes:state-transition",
            "old_state": old_state.value,
            "new_state": new_state.value,
            "reason": reason,
            "timestamp": self._last_transition_time,
        }
        self._bus.emit_sync(event)
```

---

## Wiring Into AIAgent

### Changes to `run_agent.py`

1. Import:
```python
from agent.event_bus import get_bus
from agent.operational_state import OperationalStateManager
```

2. In `AIAgent.__init__`:
```python
self._event_bus = get_bus()
self._op_state = OperationalStateManager(self._event_bus)
```

3. In `AIAgent._emit_status` (existing), re-route through bus:
```python
def _emit_status(self, message: str) -> None:
    self._event_bus.emit_sync({"type": "hermes:status", "message": message})
    # Keep status_callback for backward compat
    if self.status_callback:
        try:
            self.status_callback("lifecycle", message)
        except Exception:
            pass
```

### Changes to `conversation_loop.py`

4. In `run_conversation()`, wire state transitions around the retry loop:

```python
# At task start
agent._op_state.on_task_started()

# Around the main retry loop (replace the ad-hoc primary_recovery_attempted tracking):
while retry_count < max_retries:
    # ...existing API call logic...
    if api_success:
        agent._op_state.on_turn_complete(ok=True)
        break
    else:
        agent._op_state.on_turn_complete(ok=False)
        # ...existing retry logic...

# At task end (in the finally or completion path):
agent._op_state.on_task_completed()
```

5. Also wire budget monitoring in the loop header:
```python
budget_remaining = agent.iteration_budget.remaining / agent.iteration_budget.max_total
agent._op_state.on_budget_update(budget_remaining)
```

---

## Events Emitted

| Event | When | Payload |
|-------|------|---------|
| `hermes:state-transition` | Any state change | old_state, new_state, reason, timestamp |
| `hermes:status` | `_emit_status` called | message |
| `hermes:error` | Classified error | reason, retryable, recovery_hint |
| `hermes:budget-update` | Budget crossing threshold | remaining_fraction, state |
| `hermes:turn-complete` | Each turn ends | ok, turn_number |
| `hermes:task-started` | Task begins | session_id |
| `hermes:task-completed` | Task ends normally | session_id |
| `hermes:task-terminated` | Task ends abnormally | session_id, reason |

---

## Handler Examples (what subscribers can do)

```python
# Log state transitions
bus.subscribe("hermes:state-transition", lambda e: logger.info(
    "State %s → %s: %s", e["old_state"], e["new_state"], e["reason"]
))

# Alert when critical
bus.subscribe("hermes:state-transition", lambda e: (
    alert_user(f"Hermes entered CRITICAL state: {e['reason']}")
    if e["new_state"] == "CRITICAL" else None
))

# Track degradation for metrics
bus.subscribe("hermes:state-transition", lambda e: metrics.record(
    "state_transition", {"from": e["old_state"], "to": e["new_state"]}
))

# Auto-recover from degraded (on successful turn)
# → handled internally by OperationalStateManager via on_turn_complete(ok=True)
```

---

## What This Does NOT Include (Phase 1 scope)

- **Self-healing 闭环** — verification hooks after delegation (Phase 3)
- **Memory taxonomy** — episodic/semantic/temporal layers (Phase 2)
- **Multi-agent event routing** — the bus is in-process only
- **ObstructionHandler** — AGEM's gap-detection pipeline (too AGEM-specific)

---

## Testing

```python
# agent/test_operational_state.py
import pytest
from agent.event_bus import EventBus, reset_bus
from agent.operational_state import (
    HermesOperationalState,
    OperationalStateManager,
)

def test_standby_to_active():
    bus = EventBus()
    mgr = OperationalStateManager(bus)
    mgr.on_task_started()
    assert mgr.state == HermesOperationalState.ACTIVE

def test_error_burst_transitions():
    bus = EventBus()
    mgr = OperationalStateManager(bus, error_burst_threshold=2)
    mgr.on_task_started()
    mgr.on_turn_complete(ok=False)
    assert mgr.state == HermesOperationalState.ACTIVE  # 1 error, below threshold
    mgr.on_turn_complete(ok=False)
    assert mgr.state == HermesOperationalState.DEGRADED  # 2 errors → degraded

def test_recovery_from_degraded():
    bus = EventBus()
    mgr = OperationalStateManager(bus, error_burst_threshold=1)
    mgr.on_task_started()
    mgr.on_turn_complete(ok=False)  # DEGRADED
    assert mgr.state == HermesOperationalState.DEGRADED
    mgr.on_turn_complete(ok=True)  # Recovered
    assert mgr.state == HermesOperationalState.ACTIVE

def test_event_bus_fires():
    bus = EventBus()
    received = []
    bus.subscribe("hermes:state-transition", lambda e: received.append(e))
    mgr = OperationalStateManager(bus)
    mgr.on_task_started()
    assert len(received) == 1
    assert received[0]["old_state"] == "STANDBY"
    assert received[0]["new_state"] == "ACTIVE"
```

---

## Files Summary

| File | Action | Lines |
|------|--------|-------|
| `hermes_agent/agent/event_bus.py` | CREATE | ~90 |
| `hermes_agent/agent/operational_state.py` | CREATE | ~120 |
| `hermes_agent/run_agent.py` | MODIFY | ~15 (import + wiring) |
| `hermes_agent/agent/conversation_loop.py` | MODIFY | ~20 (state callbacks) |
| `hermes_agent/tests/test_operational_state.py` | CREATE | ~60 |