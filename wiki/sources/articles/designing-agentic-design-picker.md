---
updated: 2026-05-17T17:56:50Z
created: 2026-05-17T17:56:50Z
---

---
created: 2026-05-17T11:00:00Z
updated: 2026-05-17T11:00:00Z
type: source
summary: Design for an "agentic design picker" meta-orchestrator — evaluates task topology and outputs a structured JSON/YAML manifest that provisions the right execution environment (Sequential, ReAct, Planning+ReAct, Multi-Agent) with explicit complexity penalties for over-engineering.
tags: [agentic-design, meta-orchestrator, design-picker, workflow, decision-tree]
sources: (unknown — file from raw/)
status: reference
confidence: 0.75
---

## Core Insight

The agentic design picker is a meta-orchestrator that evaluates five decision points (path predictability, structural articulability, validation tradeoff, domain span, scale) and outputs a structured topological manifest (JSON/YAML) rather than a plain string recommendation. Key constraint: strict complexity penalty — must explicitly justify stepping up from Sequential Workflow to ReAct, or ReAct to Multi-Agent.

## Key Claims

| Evaluation Point | Routing Logic |
|-----------------|--------------|
| **Path predictability** | Fixed DAG → sequential bypass; emergent → ReAct |
| **Structural articulability** | Clear upfront deps → Planning+ReAct; emergent → standard ReAct |
| **Validation tradeoff** | High-fidelity required → append Reflection loop |
| **Domain span & scale** | Cognitive bottleneck or contradictory reasoning → Multi-Agent |
| **Complexity penalty** | Default to simplest; must justify upgrades |

Output is a manifest with `topology_type`, `required_tools`, `reflection_enabled`, `max_iterations`.

## Connections

- [[choosing-right-agentic-design-pattern]] — the decision tree this design picker formalizes
- [[agentic-design-picker]] — Hermes skill that implements this pattern
