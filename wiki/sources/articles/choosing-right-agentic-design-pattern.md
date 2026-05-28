---
updated: 2026-05-17T17:55:39Z
created: 2026-05-17T17:55:39Z
---

---
created: 2026-05-17T11:00:00Z
updated: 2026-05-17T11:00:00Z
type: source
summary: Decision-tree guide for choosing among five agentic design patterns — single agent, sequential pipeline, parallel batch, orchestration, and multi-agent council — based on task topology, context needs, and error tolerance.
tags: [agentic-design, multi-agent, orchestration, decision-tree, workflow]
sources: (unknown — file from raw/)
status: reference
confidence: 0.8
---

## Core Insight

Agentic design patterns form a decision topology: single-agent for simple tasks; sequential when outputs chain; parallel when independent sub-tasks exist; orchestration when a coordinator delegates and aggregates; and council when diverse perspectives need to deliberate. The choice is driven by task coupling, context window pressure, and error recovery requirements.

## Key Claims

| Pattern | When to Use | Error Handling |
|---------|-------------|----------------|
| **Single Agent** | One model, straightforward task | Retry with same model |
| **Sequential Pipeline** | A→B→C dependency chain | Checkpoint between stages |
| **Parallel Batch** | Independent tasks that can run simultaneously | Map-reduce aggregation |
| **Orchestration** | Coordinator delegates to specialized workers | Worker retry, fallback, timeout |
| **Multi-Agent Council** | Multiple perspectives deliberate on a decision | Consensus or majority vote |

## Connections
- [[sources/articles/designing-agentic-design-picker]]
- [[sources/articles/choosing-right-agentic-design-pattern]]
- [[index]]
- [[choosing-right-agentic-design-pattern]]

- [[delegation]] — related to orchestration pattern
- [[hermes-agent]] — supports orchestrator subagent mode
- [[agentic-design-picker]] — tool referenced in designing-agentic-design-picker.txt
