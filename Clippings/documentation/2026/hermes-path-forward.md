# Hermes Agent — 3-Phase Integration Plan

> **Status:** Phase 1 PR open (#30634). Phases 2–3 deferred until Phase 1 is accepted.

## The Problem

Hermes has no observable internal state and no recovery infrastructure for delegated subagents. When a tool fails or a model call errors, the system reacts ad-hoc — no state machine, no event bus, no taxonomy for episodic/semantic/temporal memory.

## The 3-Phase Roadmap

| Phase | Focus                                                             | Status         | Risk   |
| ----- | ----------------------------------------------------------------- | -------------- | ------ |
| **1** | EventBus + OperationalStateManager                                | PR #30634 open | Low    |
| **2** | Memory taxonomy: Semantic/Temporal/Hierarchical over SQLite       | Not started    | Medium |
| **3** | Self-healing: delegation verification + recoverable-failure retry | Not started    | Medium |

---

## Phase 1 — EventBus + StateManager ✅

**PR:** [#30634](https://github.com/NousResearch/hermes-agent/pull/30634) (`phase-1-eventbus` branch)

**What it delivers:**
- `agent/event_bus.py` — thread-safe async-capable pub/sub, singleton `get_event_bus()`, zero external deps
- `agent/operational_state.py` — 4-state machine: STANDBY / ACTIVE / DEGRADED / CRITICAL
- Events: `TASK_STARTED`, `TASK_ENDED`, `BUDGET_UPDATE`, `ITERATION_EXHAUSTED`, `STATE_TRANSITION`
- State driven by: budget fraction (< 20% → DEGRADED, < 5% → CRITICAL) and error streak (≥ 3 → DEGRADED, ≥ 6 → CRITICAL)
- All calls wrapped in try/except — handler crashes cannot affect agent turns

**Files touched:**
- `agent/event_bus.py` (new, 194 lines)
- `agent/operational_state.py` (new, 195 lines)
- `agent/agent_init.py` (wires `_event_bus` + `_op_state`)
- `agent/conversation_loop.py` (emits lifecycle events)
- `tests/agent/test_event_bus.py` (new, 288 lines, 21 tests)

**Upstream overlap to watch:**
- #7809 — `agent/hermes/shutdown.py` + streaming EventBus (different path, same layer)
- #17088 — `hermes_cli/code/event_bus.py` (Code Mode only, different layer)
- #7842 — `agent/hermes/analytics.py` / `telemetry.py` (infra bundle, 11 new files)

Phase 1 uses `agent/event_bus.py` — does not collide with any of the above paths.

**Tests:** 21/21 passed. Ruff PLW1514 clean.

---

## Phase 2 — Memory Taxonomy (Deferred)

**Concept:** Adopt GeNNAiS's SemanticMemory / TemporalMemory / HierarchicalMemory taxonomy over SQLite, dropping Neo4j and HTTP embedding dependencies.

**What changes:**
- Episodic memory: conversation turns tagged with timestamp + outcome
- Semantic memory: accumulated key facts per topic
- Hierarchical memory: goal decomposition trees for multi-turn tasks

**Constraint:** No new external dependencies. All storage via Hermes's existing SQLite session layer.

**Trigger:** Phase 1 accepted and merged to upstream `main`.

---

## Phase 3 — Self-Healing 闭环 (Deferred)

**Concept:** Failed delegations trigger verification + retry instead of immediate failure.

**What changes:**
- `delegate_tool.py` hooks into EventBus for delegation start/success/failure
- `ErrorClassifier` drives retry eligibility (rate_limit → retry, auth → no retry)
- `IterationBudget` allocates retry budget separately from primary budget

**Trigger:** Phases 1 + 2 both accepted.

---

## Branch Strategy

```
upstream/main
└── phase-1-eventbus → PR #30634
    └── phase-2 → origin/phase-2 (dev base, not submitted until #30634 clears)
        └── dev/phases-2-3 → origin/dev/phases-2-3 (working branch)
```

If #30634 is accepted: rebase `phase-2` onto `upstream/main` and start Phase 2.
If #30634 is closed for overlap: reassess — upstream's decision indicates which layer they want to own.

---

## Key Decisions (Phase 1)

- **Global singleton EventBus** — single instance via `get_event_bus()`, shared across all subsystems
- **Async via daemon thread loop** — no running event loop? async handlers get a lazy daemon thread with their own asyncio event loop. `emit()` never blocks.
- **STANDBY as default** — state machine resets between conversation sessions
- **Fork-first workflow** — fork at `angrysky56/hermes-agent`, PR targets `NousResearch/hermes-agent`
- **GitHub noreply email** — `113643118+angrysky56@users.noreply.github.com` auto-resolves in AUTHOR_MAP