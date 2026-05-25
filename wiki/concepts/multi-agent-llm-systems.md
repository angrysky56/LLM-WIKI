---
created: 2026-05-28
updated: 2026-05-29
type: concept
summary: Frameworks and coordination patterns for using multiple LLM agents together to solve complex tasks beyond the capability of any single agent
tags: [multi-agent, llms, coordination, agentic-ai, frameworks]
sources: https://arxiv.org/abs/2308.03688, https://arxiv.org/abs/2401.03428, https://arxiv.org/abs/2403.30016
status: active
confidence: 0.85
---

# Multi-Agent LLM Systems

**Multi-Agent LLM Systems** refer to frameworks that deploy multiple language model agents to work together on tasks that no single agent could solve alone. Each agent may have specialized capabilities, different access to tools, or distinct responsibilities. The key challenge is *coordination* — ensuring agents don't conflict, duplicate work, or deadlock.

Unlike single-agent systems (one LLM with tools), multi-agent systems introduce emergent complexity from agent-to-agent interaction: communication protocols, shared state, role assignment, and collective decision-making.

## Definition

A multi-agent LLM system has:
- **Two or more agents**, each powered by one or more language models
- **Coordination mechanism**: how agents share information, assign tasks, and resolve conflicts
- **Shared or private state**: memory, knowledge, or context that may be accessible to some or all agents
- **Emergent collective behavior**: the system as a whole can solve tasks that exceed any individual agent's capability

## Why It Matters

Single-agent systems hit a ceiling on complex, multi-step problems. A single agent handling a research project needs to simultaneously browse the web, write code, evaluate results, and write a report — but the same model can't be optimal at browser-level爬虫, deep code analysis, and high-level synthesis simultaneously.

Multi-agent systems sidestep this by giving each sub-task to a specialized agent. The *whole* is smarter than any part because the specialization is real, not just a prompt engineering trick.

Real-world applications:
- **Research automation**: ideation agent + search agent + implementation agent + reviewer agent
- **Code generation**: architect agent + coder agent + test agent + reviewer agent
- **Long-horizon planning**: manager agent decomposes tasks, worker agents execute, manager synthesizes results
- **Knowledge synthesis**: multiple research agents reading different papers, a synthesis agent integrates

## Architectural Patterns

### 1. Supervisor-Worker (Hierarchical)

```
Supervisor (manager LLM)
  ├── Worker A (specialist LLM)
  ├── Worker B (specialist LLM)
  └── Worker C (specialist LLM)
```

The supervisor decomposes tasks and assigns to workers. Workers execute and report back. Supervisor synthesizes final output. Simple, stable, but the supervisor is a bottleneck.

**Example**: LangChain's `ReactDocstoreAgent` — supervisor reads Wikipedia and assigns lookups to a worker.

### 2. Peer-to-Peer (Debate /协商)

```
Agent A ←→ Agent B ←→ Agent C
```

Agents communicate directly, exchanging arguments or partial results. No central supervisor. Emergent from local interactions.

**Example**: Multi-agent debate (Lanchester et al., 2023) — agents argue positions, final answer is the consensus view.

### 3. Blackboard / Shared State

```
Agent A → Shared Memory/Borad
Agent B → Shared Memory/Borad
Agent C → Shared Memory/Borad
```

All agents write to and read from a shared information pool. Agents have partial observability — they see the board but not each other's internal reasoning.

**Example**: IBM's ABS; Heuristic Search (Shoham & Tenenholtz).

### 4. Pipeline / Sequential

```
Input → Agent A → Agent B → Agent C → Output
```

Each agent processes the previous agent's output. Strictly sequential, like an assembly line. No branching or backtracking.

**Example**: Chain-of-thought pipeline where each step is handled by a different agent.

### 5. Hierarchical with Memory

```
Manager (top-level)
  ├── Sub-manager 1 (handles subtask cluster A)
  │     ├── Worker 1a
  │     └── Worker 1b
  └── Sub-manager 2 (handles subtask cluster B)
        ├── Worker 2a
        └── Worker 2b
```

Nested hierarchy with shared cross-level memory. Allows parallel workstreams that are coordinated at higher levels.

## Coordination Challenges

Multi-agent systems introduce failure modes that don't exist in single-agent setups:

| Failure Mode | Description | Mitigation |
|---|---|---|
| **Contention** | Multiple agents competing for the same resource ortool | Priority queues, mutex locks, request scheduling |
| **Deadlock** | Circular wait between agents | Timeouts, dependency ordering, deadlock detection |
| **Conflicting goals** | Agents optimize for incompatible objectives | Explicit goal alignment at system design time |
| **Context fragmentation** | No agent has the full picture | Shared memory/bboard; periodic synchronization |
| **Free-riding** | One agent benefits from others' work without contributing | Reputation systems; verification of contributions |
| **Semantic conflicts** | Agents interpret shared data differently | Structured communication protocols; schema for shared state |

## Connections

- [[multi-agent-coordination]] — the sub-field concerned with coordination mechanisms (blackboard, message passing, market-based, swarm)
- [[agentic-hierarchy]] — hierarchical organizational structure for multi-agent systems
- [[agentic-research]] — research automation uses multi-agent pipelines
- [[project-synapse]] — knowledge graph as shared state / coordination substrate
- [[hermes-agent]] — framework supporting hierarchical agent patterns
- [[delegation]] — how one agent assigns work to another
- Concept: [[adversarial-training]]
- Concept: [[agent-leak-benchmark]]
- Concept: [[agentic-design-picker]]
- Concept: [[agentic-planner]]
- Concept: [[categorical-reasoning]]
- Concept: [[cognitive-world-models-for-llm-agents]]
- Concept: [[hierarchical-supervisor]]


## Open Questions

1. **Scalable coordination**: How do you coordinate 100+ agents without the communication overhead destroying the efficiency gain?

2. **Shared mental models**: How do agents ensure they have consistent assumptions about the task, the world, and each other's capabilities?

3. **Emergent vs. designed coordination**: Is the best multi-agent system one where coordination *emerges* from simple rules, or one where it's explicitly programmed?

4. **Trust and verification**: How does a supervisor verify that a worker's output is correct when the worker is a black box?

## Limitations

- **Coordination overhead**: Every coordination message is compute overhead. For simple tasks, multi-agent is slower than single-agent.
- **Debugging difficulty**: When the system fails, is it one agent's fault or an emergent failure from interaction? Hard to diagnose.
- **Resource cost**: Running multiple LLM agents simultaneously costs more than one. Need clear gain to justify.
- **Context window pressure**: Shared state (via messages or blackboard) consumes the context window. Long-running tasks hit length limits.