---
created: 2026-01-01
updated: 2026-05-25
type: skill
summary: Decision tree for choosing agent patterns — single, sequential, parallel, hierarchical
tags: [agent-skill, skill, agentic, decision]
sources: 
status: active
confidence: 1.0
---

# Agentic Decision Tree

> [!TIP]
> **Use when**: Starting a new task and unsure which agent pattern to use. Walk the tree.

## Decision Tree

```
Is the task atomic — one clear objective, clear stopping condition?
├── YES → Use [[single-agent]] (with ReAct if path is uncertain)
└── NO
    ├── Does the task have separable sub-tasks that need different specializations?
    │   ├── YES → Use [[supervisor-delegation]] or [[agentic-multiagent]]
    │   └── NO
    │       ├── Is the task's work type unknown until you see the content?
    │       │   ├── YES → Use [[supervisor-orchestrator]] (dynamic routing)
    │       │   └── NO
    │       │       ├── Is the domain large enough to warrant nested layers?
    │       │       │   ├── YES → Use [[hierarchical-supervisor]]
    │       │       │   └── NO → Use [[supervisor-delegation]]
    │       │       └── Sequential — use [[agentic-sequential]]
    │       └── Parallel sub-tasks?
    │           └── YES → Use [[parallel-execution]]
    └── Is the solution path unknown (exploratory)?
        └── YES → Use [[agentic-react]]
```

## Pattern Selection Matrix

| Condition | Pattern |
|-----------|---------|
| Atomic, linear | single-agent |
| Atomic, unknown path | single-agent + ReAct |
| Sequential phases, separable | sequential or supervisor-delegation |
| Parallel independent workstreams | parallel-execution |
| Heterogeneous content (route by type) | supervisor-orchestrator |
| Deep/complex domain, layered | hierarchical-supervisor |
| Multiple specialists needed | multi-agent |

## Common Mistakes

1. **Reaching for multi-agent on atomic tasks** — adds coordination overhead with no benefit
2. **Using sequential when parallel is possible** — blocks on independent phases
3. **Orchestrator when supervisor-delegation suffices** — dynamic routing is complex; use it only when routing can't be predetermined
4. **Flat supervisor on complex domains** — nested layers beat one supervisor managing 10 sub-agents

## Connections

- [[single-agent]] — atomic tasks
- [[agentic-react]] — exploratory unknown-path tasks
- [[agentic-sequential]] — sequential phases
- [[parallel-execution]] — parallel independent workstreams
- [[supervisor-delegation]] — supervisor → fixed delegates
- [[supervisor-orchestrator]] — dynamic routing orchestrator
- [[hierarchical-supervisor]] — nested layers