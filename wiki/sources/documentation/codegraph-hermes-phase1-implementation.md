---
created: 2026-05-22
updated: 2026-05-22
type: source
summary: Phase 1 implementation plan for EventBus + OperationalStateManager in Hermes Agent
tags: [hermes-agent, event-bus, state-machine, architecture, codegraph]
sources: 
status: active
confidence: 0.95
---

# CodeGraph Hermes Phase 1 Implementation

## Core Concept

Implementation plan for adding observable internal state and recovery infrastructure to Hermes Agent via two new Python modules: `agent/event_bus.py` (async pub/sub) and `agent/operational_state.py` (4-state machine). Replaces the ad-hoc retry tracking in `conversation_loop.py` with a proper state machine that emits events on every transition.

## Key Points

- **EventBus** (`agent/event_bus.py`): Thread-safe async-capable pub/sub, singleton `get_event_bus()`, zero external dependencies. Replaces the old callback-funnel pattern (`_emit_status`, `_emit_warning`, `status_callback`).
- **OperationalStateManager** (`agent/operational_state.py`): 4-state machine (STANDBY / ACTIVE / DEGRADED / CRITICAL). Transitions driven by budget fraction (< 20% → DEGRADED, < 5% → CRITICAL) and error streak (≥ 3 → DEGRADED, ≥ 6 → CRITICAL).
- **Events emitted**: `TASK_STARTED`, `TASK_ENDED`, `BUDGET_UPDATE`, `ITERATION_EXHAUSTED`, `STATE_TRANSITION`, `TURN_COMPLETE`, `ERROR`.
- **Wiring**: `run_agent.py` imports the bus and wires `_emit_status` through it. `conversation_loop.py` calls `on_task_started()`, `on_turn_complete(ok=True/False)`, `on_task_completed()` around the retry loop.
- **PR #30634** open on `phase-1-eventbus` branch, targeting `NousResearch/hermes-agent`.
- **Test coverage**: 21/21 passed, Ruff PLW1514 clean.
- **Phase 2** (Memory taxonomy: Semantic/Temporal/Hierarchical over SQLite) deferred until Phase 1 merges.
- **Phase 3** (Self-healing: delegation verification + recoverable-failure retry) deferred until Phase 2 merges.

## Connections
- [[sources/documentation/codegraph-readme]]
- [[wiki/index]]
- [[sources/documentation/hermes-path-forward]]
- [[sources/documentation/codegraph-hermes-phase1-implementation]]
- [[codegraph-hermes-phase1-implementation]]

- [[codegraph]] — CodeGraph tool used for Hermes codebase indexing
- [[hermes-agent]] — Target project for this implementation