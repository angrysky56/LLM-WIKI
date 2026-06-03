---
created: 2026-05-22T20:57:14Z
updated: 2026-05-22T20:57:14Z
type: synthesis
summary: "CodeGraph-driven integration plan: GeNNAiS memory architecture + AGEM EventBus/StateManager for Hermes"
tags: [hermes, integration, plan, memory, state-machine, codegraph, agem, gennaiis]
sources: []
status: active
confidence: 0.8
---

# CodeGraph Hermes Integration Plan
**Status:** Assessment Complete — Integration Recommended (Partial)
**Created:** 2026-05-22
**Sources:** CodeGraph analysis of 62K-file / 1M-node / 1.67M-edge workspace index



## Executive Summary

CodeGraph scan of the user's 62K-file personal workspace revealed two mature systems with direct applicability to Hermes:

1. **GeNNAiS UnifiedMemoryInterface** — 3-layer memory (semantic + temporal + hierarchical) with Neo4j storage
2. **AGEM OrchestratorStateManager + EventBus** — 3-state operational machine with H^1 obstruction detection

Both systems are production-quality code (not sketches), with significant test coverage. Neither can run standalone — each requires its full deployment environment. Integration must be architectural porting, not import-and-run.



## System 1: GeNNAiS Memory Architecture

### What It Is

`Nexus-Prime/MetaTransformers-Fractal-Workflow-System/MetaTransformer-Scripts/GeNNAiS/src/core/`

Three specialized memory systems coordinated by `UnifiedMemoryInterface`:

| Layer | Class | Role |
|-------|-------|------|
| Semantic | `SemanticMemory` | Content storage + embedding similarity search |
| Temporal | `TemporalMemory` | Time-ordered sequences + pattern detection + `predict_next_memory()` |
| Hierarchical | `HierarchicalMemory` | Agglomerative clustering + cluster summarization |
| Coordinator | `UnifiedMemoryInterface` | `store_thought()`, `retrieve_context()`, `predict_next_thought()` |

### Data Flow

**store_thought():**
```
content → EmbeddingConnector (HTTP:1234) → Neo4j (Memory node with embedding JSON)
       → SemanticMemory.find_similar_memories() → top-5 similar
       → TemporalMemory.create_temporal_sequence() → TEMPORAL_SEQUENCE edges
       → HierarchicalMemory.create_memory_hierarchy() → Cluster nodes + BELONGS_TO edges
```

**retrieve_context():**
```
query → EmbeddingConnector → cosine similarity against ALL stored memories (N+1 problem)
      → TemporalMemory.get_memory_timeline() → time-windowed memories
      → HierarchicalMemory.find_cluster_path() + get_cluster_summary() → cluster context
```

### Critical Flaws

1. **N+1 in find_similar_memories**: Fetches ALL memories from Neo4j, computes similarity in-memory per query. No vector index. Will not scale.
2. **Embedding service dependency**: `EmbeddingConnector` calls `http://127.0.0.1:1234` (text-embedding-granite-embedding-278m-multilingual). No embedding = no memory operations.
3. **Neo4j dependency**: All data in Neo4j. No Neo4j = no memory.
4. **memory_id collision risk**: `f"mem_{hash(content)}"` uses Python's `hash()` which is not stable across processes for strings.
5. **Granite LLM** (`192.168.1.82:1234`) only used for cluster summaries — not in hot path.

### Hermes Fit Assessment

| GeNNAiS Component | Hermes Current State | Gap |
|-------------------|---------------------|-----|
| SemanticMemory (embedding + similarity) | **NONE** — no episodic/semantic/temporal taxonomy in agent core | Full gap |
| TemporalMemory (sequences + predict_next) | **NONE** — no temporal reasoning in agent core | Full gap |
| HierarchicalMemory (clustering) | **NONE** — no concept hierarchy in agent core | Full gap |
| UnifiedMemoryInterface | **NONE** — no coordinator for multi-layer memory | Full gap |
| Neo4j dependency | **NONE** — no Neo4j in hermes-agent | N/A |

**Verdict: PARTIAL — Architecture is sound, implementation is not portable.**

The 3-layer taxonomy (semantic + temporal + hierarchical) is exactly what Hermes needs. But the implementation is tied to:
- Neo4j (would need to be SQLite or in-memory for Hermes)
- External HTTP embedding service (would need local embeddings or different approach)
- Specific LLM for summarization (not needed for core functionality)

### Recommended Integration Path

1. **Port the taxonomy, not the implementation**: Adopt SemanticMemory / TemporalMemory / HierarchicalMemory as named layers
2. **Replace storage**: Use SQLite (like Hermes already has `hermes_state.py`) instead of Neo4j
3. **Simplify embeddings**: Use lightweight local embeddings (e.g., ONNX runtime or skip embeddings for MVP) or integrate with existing memory providers (Hindsight, Honcho)
4. **Drop the N+1**: Add proper vector indexing (SQLite FTS5 can handle this) or use a simpler hash-based similarity
5. **Keep predict_next_memory()**: This is the most novel feature — worth preserving



## System 2: AGEM Orchestrator

### What It Is

`agent-group-evolving-molecular-system-AGEM/src/orchestrator/`

A sheaf-theoretic agent orchestration system with H^1 obstruction detection and regime-gated agent spawning.

### Core Components

**EventBus** (fully functional):
- Async pub/sub with `subscribe()`, `emit()`, `unsubscribe()`
- Zero external dependencies — only imports `EventEmitter` from `node:events`
- Parallel handler dispatch via `Promise.all`
- **Extractable: YES** — clean, generic, AGEM-independent

**OrchestratorStateManager** (fully functional + well-tested):
- 3-state machine: NORMAL → OBSTRUCTED → CRITICAL
- Thresholds: `h1ObstructionThreshold=2`, `h1CriticalThreshold=5`
- State transitions driven by H^1 dimension from CohomologyAnalyzer
- Emits `orch:state-changed` events via EventBus
- **Extractable: YES** — only depends on EventBus, no AGEM coupling

**ObstructionHandler** (mostly complete):
- Subscribes to `sheaf:h1-obstruction-detected` on EventBus
- FIFO queue with `#isProcessing` lock
- Spawns `GapDetectorAgent` from pool (max 4)
- Integrates results into TNA `CooccurrenceGraph`
- **Verdict: Complete as a pattern, stub implementation for Phase 6 agents**

**VdWAgentSpawner** (spawner complete, agents are stubs):
- Regime-gated: `stable` suppresses, `nascent` limits, `transitioning`/`critical` enables
- Hysteresis: H^1 must stay ≥ threshold for `h1HysteresisCount` consecutive iterations
- Token budget: `max(500, 5000 / h1Dimension)` — inverse scaling
- **Agents themselves**: Phase 6 stubs that generate synthetic bridging queries (no real LLM calls yet)

**Test Coverage**: 2,508 lines across 5 test files — substantial.

### Hermes Fit Assessment

| AGEM Component | Hermes Current State | Gap |
|---------------|---------------------|-----|
| EventBus | **NONE** — no central event system in agent core | Full gap |
| OrchestratorStateManager | **NONE** — no NORMAL/OBSTRUCTED/CRITICAL state machine | Full gap |
| ObstructionHandler | **NONE** — no obstruction detection / self-healing | Full gap |
| VdWAgentSpawner | **Delegation exists** — `delegate_task` tool, but no regime-gating or H^1 parameterization | Partial |
| H^1 Cohomology Analysis | **NONE** — no sheaf theory in Hermes | N/A (too specialized) |

**Verdict: RECOMMENDED (EventBus + StateManager only).**

EventBus and OrchestratorStateManager are clean, extractable, AGEM-independent. They solve a real need — Hermes has no operational state machine and no central event system.

### Recommended Integration Path

1. **Extract EventBus + OrchestratorStateManager** from AGEM into Hermes as reusable components
2. **Adapt state thresholds** to Hermes domain (operational thresholds, not H^1 obstruction)
3. **Keep EventBus generic** — don't bake in AGEM event types
4. **Drop ObstructionHandler + VdWAgentSpawner** — these are too AGEM-specific (sheaf theory, gap detection)
5. **Replace with Hermes-native handlers**: Tie state transitions to Hermes metrics (iteration budget, error rates, task completion)



## Hermes Current State (Baseline)

| Dimension | Current Implementation |
|-----------|------------------------|
| Memory | Plugin-based (`MemoryProvider` + `MemoryManager`). No built-in episodic/semantic/temporal taxonomy. External providers (Honcho, Hindsight, mem0) supply memory if configured. |
| State Management | `IterationBudget` (consume/refund counter). `conversation_loop.py` tracks retry flags. **No NORMAL/OBSTRUCTED/CRITICAL state machine.** |
| Delegation | `delegate_task` tool — flat hierarchy (parent → child → blocked grandchild). Max depth 1. Max concurrent children 3. |
| Error Recovery | `ErrorClassifier` (14 error types + recovery hints). Recovery strategies: credential rotation, model fallback, compression, image shrink. |
| Self-Healing | **NONE** — no `闭环` (closed-loop verification). No post-verification loops. |
| Context Management | `ContextCompressor` pluggable via plugin system. LCM can replace default. |



## Integration Plan

### Phase 1: EventBus + StateManager (Low Risk, High Value)

**Extract and adapt** the AGEM EventBus + OrchestratorStateManager into Hermes.

```
New file: hermes_agent/agent/event_bus.py
New file: hermes_agent/agent/operational_state.py

HermesOperationalState:
  - STANDBY (starting up, no active task)
  - ACTIVE (task in progress, normal operation)
  - DEGRADED (recoverable errors detected, increased monitoring)
  - CRITICAL (unrecoverable errors or budget exhaustion)
```

**Transitions:**
- STANDBY → ACTIVE: task begins
- ACTIVE → DEGRADED: error rate exceeds threshold OR iteration budget < 20%
- DEGRADED → ACTIVE: successful turn completion
- DEGRADED → CRITICAL: budget exhaustion or cascading failures
- CRITICAL → STANDBY: task terminated, ready for new task

**Event bus events** (Hermes-native):
- `hermes:turn-complete` — turn finished successfully
- `hermes:error-detected` — classified error with recovery hint
- `hermes:budget-update` — iteration budget changed
- `hermes:state-transition` — operational state changed
- `hermes:delegation-started` / `hermes:delegation-complete`

### Phase 2: Memory Taxonomy (Medium Risk, Medium Value)

**Adopt the GeNNAiS 3-layer taxonomy** without the implementation.

```
New layer concepts in hermes_agent/agent/memory/
  - episodic/     (what happened in this session — SQLite backed)
  - semantic/     (what we know — facts extracted and stored)
  - temporal/     (when things happened — timestamps + sequences)
```

**MVP approach:**
- Use existing SQLite schema (`hermes_state.py` FTS5) as the episodic layer
- Add semantic layer as structured fact storage (e.g., `syapse_remember` already does this)
- Add temporal layer as event log with timestamps
- **Do NOT add Neo4j** — keep it SQLite-native

### Phase 3: Self-Healing闭环 (Higher Risk, Requires Design)

**Pattern from AGEM ObstructionHandler** adapted to Hermes:

```
task_submitted → delegate executes → verify_output → 
  if failure detected → classify → recover → re-verify →闭环
```

**This is what the user actually wants**: verification after delegation, not obstruction detection.

- Phase 1 (this plan): Add verification hooks in `delegate_task` result handling
- Phase 2: Add automatic retry with exponential backoff for recoverable failures
- Phase 3: Add output validation before returning to caller

### Not Recommended

- **GeNNAiS embeddings**: Require external HTTP service. Not portable.
- **GeNNAiS Neo4j**: Full replacement of Hermes SQLite. Not worth the migration.
- **AGEM CohomologyAnalyzer**: Sheaf theory too specialized. H^1 obstruction is not applicable to Hermes.
- **AGEM VdWAgentSpawner**: Regime-gating is interesting but too coupled to AGEM's agent model.
- **AGEM ObstructionHandler**: Too AGEM-specific (gap detection in TNA graphs). Hermes needs different self-healing logic.



## Verification闭环

From user memory: *"self-healing verification 闭环"* — closed loop where:
1. A task is delegated
2. Output is verified
3. If verification fails → classify → recover → re-verify
4. Loop until success or budget exhaustion

**Current state**: `delegate_task` returns results, caller receives them. No verification step.

**Target state**:
```
delegate_task(task) → execute → verify(output) →
  if fail: classify_error() → recover() → re-verify →
  if pass: return result
```

**Implementation** (in `delegate_tool.py`):
- Add `verify_output` hook after task execution
- Hook calls user-defined or model-defined verification function
- On failure: feed back to `ErrorClassifier`, apply recovery strategy, retry
- Max retries bounded by iteration budget



## Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| EventBus adds complexity without enough events to justify it | Medium | Low | Start with a minimal set (state transitions + delegation events only) |
| Memory taxonomy becomes over-engineered | Medium | Medium | MVP: use existing SQLite schema, add layers only when needed |
| Neo4j dependency creep from GeNNAiS concepts | Low | High | Explicitly ban Neo4j in new memory code — SQLite only |
| Self-healing闭环 becomes infinite retry loop | Medium | High | Budget-bounded retries with explicit abort conditions |
| External embedding service required | High (for GeNNAiS-style) | High | Skip embeddings for MVP, use keyword/pattern matching instead |



## Dependencies

- EventBus + StateManager: Zero new dependencies (pure Python)
- Memory taxonomy: Zero new dependencies (SQLite already in use)
- Self-healing闭环: Zero new dependencies (uses existing ErrorClassifier)



## Success Criteria

1. Hermes gains operational state machine visible in logs
2. Delegation emits lifecycle events (start/complete/error)
3. Memory operations can be described in terms of episodic/semantic/temporal
4. Failed delegation triggers recovery flow, not immediate failure
5. No new external services required (no Neo4j, no embedding HTTP service)



## Related
- [[synthesis/codegraph-hermes-integration-plan]]
- [[wiki/index]]

- [[codegraph-hermes-integration-plan]]

## Related Pages

- `wiki/synthesis/nairobi-protocol-gde.md` — related local-first knowledge graph work
- `wiki/agents/skills/agem-expert/` — AGEM skill documentation
- `wiki/synthesis/essan-internal-representation.md` — Essan R&D notes
