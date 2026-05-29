---
created: 2026-01-01
updated: 2026-05-25
type: skill
summary: Hierarchical Supervisor pattern — nested supervisors for complex domains with multiple abstraction layers
tags: [agent-skill, skill, hierarchical, nested-supervisor]
sources: 
status: active
confidence: 1.0
---

# Hierarchical Supervisor Pattern

> [!TIP]
> **Use when**: A domain is large enough that one supervisor managing 10 sub-agents creates coordination overhead — use nested layers instead.

## Pattern

```
Top Supervisor
├── Research Track Supervisor
│   ├── Agent: arXiv search
│   └── Agent: Web fetch
└── Write Track Supervisor
    ├── Agent: First draft
    └── Agent: Review / Edit
```

## Why Nested Layers

A flat supervisor with 8+ sub-agents becomes a coordination bottleneck:
- The supervisor must track all 8 workstreams simultaneously
- Result merge is complex with many heterogeneous outputs
- Adding new sub-types requires modifying the supervisor

Nested layers solve this by grouping related sub-tasks under intermediate supervisors:
- Top supervisor manages tracks (Research, Write, Verify)
- Track supervisors manage individual agents within that track
- Each layer only needs to track 2-5 children

## When to Use

✅ Good for:
- Complex projects with distinct phases (research → architect → implement → verify)
- Multi-track workstreams (parallel tracks that merge at the end)
- Domains with broad scope (meta-harness, wiki curator, research synthesis)

❌ Bad for:
- Simple tasks with 2-3 sub-tasks (over-engineered)
- Tasks where all sub-tasks are the same type (use flat supervisor + parallel-execution)
- Single-layer coordination suffices

## Layer Sizing

| Layer | Typical children |
|-------|-----------------|
| Top supervisor | 2-4 track supervisors |
| Track supervisor | 2-5 specialist agents |
| Specialist agent | Atomic task |

## Connections

- [[supervisor-delegation]] — flat supervisor variant
- [[supervisor-orchestrator]] — dynamic routing with centralized state
- [[agentic-multiagent]] — multi-agent coordination patterns
- [[agentic-decision-tree]] — routing to hierarchical when domain warrants