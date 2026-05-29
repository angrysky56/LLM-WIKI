---
created: 2026-01-01
updated: 2026-05-25
type: skill
summary: Supervisor Orchestrator pattern — central agent dynamically routes sub-tasks based on content analysis
tags: [agent-skill, skill, orchestrator, dynamic-routing]
sources: 
status: active
confidence: 1.0
---

# Supervisor Orchestrator Pattern

> [!TIP]
> **Use when**: The type of work is unknown until you inspect the content — a central orchestrator must analyze and route dynamically.

## Pattern

```
Orchestrator (central state holder)
├── Receives task
├── Analyzes content
├── Routes to Specialist A (type: research)
├── Routes to Specialist B (type: code)
├── Routes to Specialist C (type: review)
├── Gathers all results
└── Delivers final output
```

## Key Properties

- **Dynamic routing**: The orchestrator decides which specialist to use based on content analysis — not predetermined
- **Centralized state**: Orchestrator holds the full task state; sub-agents are stateless workers
- **Content-awareness**: Routing decision is based on inspecting the actual input
- **Flexible delegation**: Different runs may route differently based on content

## Orchestrator vs Supervisor-Delegation

| Property | Supervisor-Delegation | Supervisor-Orchestrator |
|----------|---------------------|------------------------|
| Routing | Fixed at start | Dynamic per content |
| Sub-agent role | Semi-autonomous | Stateless worker |
| State | Distributed via carryover | Centralized in orchestrator |
| Complexity | Lower | Higher |

**Use orchestrator when**: The routing can't be predetermined. Example: an ingest pipeline that sees different document types and routes to different processing agents.

**Use supervisor-delegation when**: You know the task structure upfront. Example: research → write → review is known before agents start.

## When NOT to Use

- Routing is predetermined → use supervisor-delegation
- Sub-agents need stateful context → use supervisor-delegation with carryover
- Single agent can handle it → use single-agent

## Connections
- [[wiki/scratchpad/agent-sheets/skills/hierarchical-supervisor]]
- [[supervisor-delegation]]
- [[single-agent]]
- [[agentic-decision-tree]]
- [[wiki/scratchpad/agent-sheets/skills/index]]
- [[agentic-multiagent]]
- [[supervisor-orchestrator]]
- [[supervisor-orchestrator]]

- [[supervisor-delegation]] — fixed routing variant
- [[wiki/scratchpad/agent-sheets/skills/hierarchical-supervisor]] — nested orchestrators
- [[single-agent]] — when orchestrator overhead isn't worth it
- [[agentic-multiagent]] — multi-agent coordination patterns