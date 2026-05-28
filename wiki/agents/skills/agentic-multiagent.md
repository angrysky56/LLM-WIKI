---
created: 2026-01-01
updated: 2026-05-25
type: skill
summary: Multi-agent coordination patterns — supervisor, orchestrator, delegation, hierarchy
tags: [agent-skill, skill, multi-agent, coordination]
sources: 
status: active
confidence: 1.0
---

# Agentic Multi-Agent Patterns

> [!TIP]
> **Use when**: A task requires parallel workstreams, different specializations, or coordination across agents.

## Core Patterns

### 1. Supervisor → Delegate
One supervisor agent breaks down work and assigns to specialist sub-agents. Supervisor merges results.

```
Supervisor
├── Delegate A (research)
├── Delegate B (write)
└── Delegate C (verify)
```

Use for: tasks with distinct phases that can run in parallel or sequence.

### 2. Orchestrator (Dynamic Routing)
Central agent holds the full task state and dynamically routes sub-tasks based on content analysis. No fixed assignment — routes as needed.

```
Orchestrator
├── Route to Researcher (content detected)
├── Route to Coder (logic detected)
└── Route to Reviewer (finished)
```

Use for: heterogeneous tasks where work type isn't known upfront.

### 3. Hierarchical Supervisor
Nested supervisors for complex domains. Each level handles a different abstraction of work.

```
Top Supervisor
├── Supervisor: Research Track
│   ├── Agent: arXiv search
│   └── Agent: Web fetch
└── Supervisor: Write Track
    ├── Agent: First draft
    └── Agent: Review
```

Use for: Large projects with multiple workstreams at different granularities.

## Key Distinctions

| Pattern | Decision | Routing | State |
|---------|----------|---------|-------|
| Supervisor → Delegate | Pre-assigned | Fixed | Shared via carryover |
| Orchestrator | Dynamic | Content-based | Centralized |
| Hierarchical Supervisor | Nested | Layer-based | Layer-isolated |

## When Multi-Agent Overhead Is Not Worth It

- Task is atomic (no separable sub-tasks)
- Sub-tasks are tightly coupled (output of one is input to another — can't parallelize)
- The coordination cost exceeds the time saved by parallelization
- Single ReAct loop can solve it

Rule of thumb: if the task can be expressed as a single well-scoped objective with a clear stopping condition, use single-agent with ReAct.

## Connections
- [[agents/skills/agentic-decision-tree]]
- [[index]]
- [[agents/skills/agentic-multiagent]]
- [[agents/skills/supervisor-orchestrator]]
- [[agents/skills/hierarchical-supervisor]]
- [[agents/skills/supervisor-delegation]]
- [[agentic-multiagent]]

- [[supervisor-delegation]] — supervisor → delegate pattern
- [[supervisor-orchestrator]] — orchestrator pattern
- [[hierarchical-supervisor]] — nested supervisors
- [[single-agent]] — when single is the right choice
- [[agentic-decision-tree]] — routing decision logic