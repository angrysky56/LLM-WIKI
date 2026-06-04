---
created: 2026-05-29
updated: 2026-05-29
type: concept
summary: Organizational structures where AI agents operate at different levels of abstraction and authority — supervisor-worker, manager-specialist, orchestrator-delegator patterns
tags: [multi-agent, hierarchy, delegation, architecture, agentic-ai]
sources:
status: active
confidence: 0.8
---

# Agentic Hierarchy

## Definition

Agentic hierarchy refers to organizational structures where AI agents operate at different levels of abstraction and authority. Rather than a single agent handling all tasks, a hierarchy decomposes complex goals across levels — each level has a distinct role: planning at high abstraction, executing at low abstraction, reporting back up.

The key insight is that not all cognitive work requires the same model or approach. A 72B planner doesn't need to micromanage a 1B tool-use agent. Hierarchy exploits this by matching model capacity to task complexity.

## Why It Matters

Without hierarchy, every agent attempt handles the full stack: goal decomposition, execution planning, tool selection, error recovery, and validation — all at the same abstraction level. This creates two failure modes:

1. **Underthinking**: Simple models make poor high-level plans but good low-level executors. Forcing them to plan at high abstraction leads to brittle, underdecomposed strategies.
2. **Overthinking**: Frontier models waste capacity on tasks that smaller models handle adequately — expensive compute on simple tool calls.

Hierarchy solves this by separating concerns across levels, allowing each level to use appropriately-sized models for their specific cognitive workload.

## Architectural Patterns

### Supervisor-Worker

A single supervisor decomposes a task into subtasks, assigns them to workers, monitors progress, and handles failures. Workers are interchangeable and stateless.

```
Supervisor (72B)
  ├─ Worker A (7B): fetch data
  ├─ Worker B (7B): process data
  └─ Worker C (7B): format output
```

**典型 use case**: Parallelizable pipelines where subtasks are independent. Works well when task decomposition is straightforward and failure modes are predictable.

### Manager-Specialist

A manager coordinates specialists with domain expertise. Unlike supervisor-worker (where workers are interchangeable), specialists have persistent capabilities and state.

```
Manager (72B)
  ├─ Code Specialist (13B): code generation, debugging
  ├─ Research Specialist (13B): web search, citation
  └─ Math Specialist (13B): formal verification, calculation
```

**Typical use case**: Tasks requiring diverse expertise. The manager knows when to call which specialist; specialists have deep domain knowledge.

### Orchestrator-Delegator

An orchestrator decides _what_ to delegate and to whom, without being involved in execution. Delegators manage execution in their domain and report results up.

```
Orchestrator (reasoning model)
  └─ Delegator A (execution model) → subtask execution
  └─ Delegator B (execution model) → subtask execution
```

**Typical use case**: Complex, open-ended tasks where the right decomposition isn't known upfront. The orchestrator can dynamically decide how to structure work based on what it discovers.

### Recursive Decomposition

Agents can decompose their own tasks into sub-tasks, then further decompose sub-tasks they receive — without a fixed hierarchy depth. The hierarchy emerges dynamically from the problem structure.

```
Level 0: Goal
  └─ Level 1: Subgoal A, Subgoal B
       └─ Level 2: Task A1, Task A2 (from Subgoal A)
            └─ Level 3: Micro-tasks...
```

This is the pattern behind "Chain of Thought" extended to multi-agent systems — reasoning traces become task hierarchies.

## Key Challenges

### Coherence Across Levels

Information loss at each level transition. A high-level plan is a compression of the full solution space; by the time results bubble up, important details may have been dropped. Mitigation: structured reporting formats, mandatory check-ins at critical decision points.

### Credit Assignment

When a high-level plan fails, was it bad planning or bad execution? Without clear attribution, it's hard to improve either level. Approaches:

- **Hierarchical RL**: Train levels jointly with reward signals at each level
- **Replay and attribution**: Log decomposition decisions and execution outcomes separately

### Information Flow

Top-down: Goals and context must reach the right level without being over- or under-specified. Bottom-up: Results must convey both what was done and what was learned that might affect higher-level strategy.

The bounded-structured-memory pattern addresses this via layered memory — each level maintains its own context, with selective upward summarization.

## Hermes Implementation

[[hermes-agent]] implements agentic hierarchy via:

- **`delegate_task`**: Spawns child agents at a designated level (default flat, max 3 concurrent). Children get isolated tool sets and sessions.
- **Cron jobs**: Durable background agents that survive session boundaries — appropriate for monitoring or long-horizon tasks that need persistent identity.
- **Markovian carryover**: Bounded forward-state so each level can resume with appropriate context after context reset.

The [[bounded-structured-memory]] architecture formalizes this with per-agent vaults under `LLM-WIKI/wiki/agents/`, where each agent maintains its own working context.

## Connections

- [[log]]
- [[concepts/agentic-design-picker]]
- [[concepts/llm-agent-architecture]]
- [[concepts/multi-agent-coordination]]
- [[concepts/agent-native-design]]
- [[concepts/agentic-hierarchy]]
- [[concepts/agent-onboarding]]
- [[concepts/agentic-planner]]
- [[concepts/markovian-carryover]]
- [[concepts/multi-agent-llm-systems]]
- [[concepts/agentic-oversight]]
- [[concepts/subagent-delegation]]
- [[wiki/index]]
- [[concepts/delegation]]
- [[concepts/mcts]]
- [[concepts/onboarding-standards]]
- [[concepts/agentic-hierarchy]]

- [[multi-agent-llm-systems]] — systems built with agentic hierarchies; five architectural patterns include hierarchical ones
- [[delegation]] — the mechanism for assigning tasks down the hierarchy; act of moving authority across levels
- [[hermes-agent]] — framework supporting hierarchical agent patterns via delegate_task and cron
- [[bounded-structured-memory]] — layered memory architecture that supports multi-level information flow
- [[markovian-carryover]] — forward-state mechanism for continuity across context resets
- [[subagent-delegation]] — mechanics of delegate_task spawning
- Concept: [[MCTS]]
- Concept: [[agent-native-design]]
- Concept: [[agent-onboarding]]
- Concept: [[agentic-oversight]]
- Concept: [[llm-agent-architecture]]
- Concept: [[multi-agent-coordination]]
- Concept: [[onboarding-standards]]

- [[MCTS]]
- [[agentic-design-picker]]

## Open Questions

1. **Optimal depth**: How many levels of hierarchy are useful? Does the answer depend on task complexity or model capacity at each level?

2. **Level-specialized training**: Should each level be a different model, or the same model with different prompts/contexts? Different training objectives?

3. **Dynamic re-hierarchization**: Can a system dynamically add or remove hierarchy levels based on task demands? What signals trigger restructuring?

## Limitations

- **Coordination overhead**: Every level transition adds latency and potential information loss. For simple tasks, flat is faster.
- **Single points of failure**: If the top level fails, the whole system fails. Redundancy at each level adds complexity.
- **Debugging difficulty**: When something goes wrong across multiple levels, diagnosing which level is responsible is non-trivial.
- [[agentic-planner]]
