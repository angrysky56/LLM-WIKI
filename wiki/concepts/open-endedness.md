---
created: 2026-06-04
updated: 2026-06-04
type: concept
summary: "Open-endedness (OE) — property of a system that continuously generates novel, increasingly complex capabilities without a fixed termination condition."
tags: [open-endedness, evolutionary-algorithms, complexity, longhorizon]
sources: []
status: reference
confidence: 0.9
---

# Open-Endedness (OE)

The property of a system that continuously generates novel, increasingly complex capabilities without a fixed termination condition. OE was first formalized in artificial life / evolutionary computation (Stanley & Lehman 2015); AC/DC instantiates it in the LLM setting.

## Key mechanisms in AC/DC

- **Minimal criteria** — coarse filters that weed out degenerate solutions without constraining the search space
- **Coevolution** — model population and task population mutually drive each other's improvement
- **Quality-Diversity selection** — DNS maintains a diverse archive, not convergence to a single optimum

## Connection to synthesis

AC/DC's OE framework maps onto the agent carryover architecture: agents and tasks coevolve in the vault, with no fixed endpoint. The [[wiki/synthesis/insights/oee-knowledge-cluster-insight]] synthesis explores this connection more deeply.

## Connections

- [[wiki/sources/papers/acdc-llm-task-capability-coevolution-sakana]] — the LLM instantiation of OE
- [[wiki/synthesis/insights/oee-knowledge-cluster-insight]] — related synthesis on OE
- [[concepts/coevolution]] — the specific OE mechanism used in AC/DC
- [[concepts/quality-diversity]] — DNS is the selection mechanism