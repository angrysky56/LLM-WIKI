---
created: 2026-05-25
updated: 2026-05-25
type: source
summary: 3-phase roadmap for Hermes Agent observability: EventBus + StateManager, Memory Taxonomy, Self-Healing
tags: [hermes-agent, roadmap, architecture, event-bus, state-machine, memory]
sources: 
status: active
confidence: 0.95
---

# Hermes Agent 3-Phase Integration Plan

## Core Concept

Three-phase integration roadmap to add observable internal state and recovery infrastructure to Hermes Agent. Phase 1 (EventBus + OperationalStateManager) has an open PR (#30634). Phases 2–3 are deferred until Phase 1 merges.

## Key Points

### Phase 1 — EventBus + StateManager ✅ (PR open)
- **PR #30634** on `phase-1-eventbus` branch targeting `NousResearch/hermes-agent`
- Delivers: `agent/event_bus.py` (async pub/sub, singleton, zero deps), `agent/operational_state.py` (STANDBY/ACTIVE/DEGRADED/CRITICAL state machine)
- Transitions driven by: budget fraction (< 20% → DEGRADED, < 5% → CRITICAL) and error streak (≥ 3 → DEGRADED, ≥ 6 → CRITICAL)
- Events: `TASK_STARTED`, `TASK_ENDED`, `BUDGET_UPDATE`, `ITERATION_EXHAUSTED`, `STATE_TRANSITION`
- 21/21 tests passing, Ruff clean
- Upstream overlaps to monitor: #7809 (shutdown EventBus), #17088 (Code Mode EventBus), #7842 (analytics/telemetry)

### Phase 2 — Memory Taxonomy (Deferred)
- Adopt GeNNAiS's SemanticMemory / TemporalMemory / HierarchicalMemory taxonomy over SQLite
- Drops Neo4j and HTTP embedding dependencies
- Episodic: conversation turns with timestamp + outcome; Semantic: accumulated key facts; Hierarchical: goal decomposition trees
- Trigger: Phase 1 merged to upstream `main`

### Phase 3 — Self-Healing闭环 (Deferred)
- Failed delegations trigger verification + retry instead of immediate failure
- `delegate_tool.py` hooks into EventBus for delegation start/success/failure
- `ErrorClassifier` drives retry eligibility (rate_limit → retry, auth → no retry)
- `IterationBudget` allocates retry budget separately from primary budget
- Trigger: Phases 1 + 2 both accepted

### Branch Strategy
```
upstream/main
└── phase-1-eventbus → PR #30634
    └── phase-2 → origin/phase-2 (dev base, not submitted until #30634 clears)
        └── dev/phases-2-3 → origin/dev/phases-2-3 (working branch)
```

## Connections
- [[wiki/index]]
- [[sources/documentation/hermes-path-forward]]
- [[hermes-path-forward]]

- [[codegraph-hermes-phase1-implementation]] — Phase 1 detailed implementation
- [[hermes-agent]] — Target project