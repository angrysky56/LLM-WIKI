---
created: 2026-06-04
updated: 2026-06-04
type: concept
summary: "Coevolution — evolutionary dynamics where two or more populations mutually influence each other's fitness landscape, applied to LLM-task coevolution in AC/DC."
tags: [coevolution, evolutionary-algorithms, open-endedness]
sources: []
status: reference
confidence: 0.85
---

# Coevolution

An evolutionary dynamics where two or more populations mutually influence each other's fitness landscape. In the AC/DC setting: model population ↔ task population. As models improve, tasks must become harder to remain informative; as tasks improve, models must become more capable to solve them — creating an arms race that drives open-ended improvement.

AC/DC uses *minimal criteria* (MC) for both populations: coarse filters that weed out gibberish and impossible tasks without constraining the search space too tightly. This is the minimal-criteria open-ended variant described by Brant & Stanley and Soros & Stanley.

## Connection to synthesis

AC/DC's coevolution model has a conceptual link to the agent carryover architecture: agents (models) and tasks (research questions) coevolve in the vault — as agents improve, the questions they can address shift, and vice versa.

## Connections

- [[wiki/sources/papers/acdc-llm-task-capability-coevolution-sakana]] — reference application
- [[concepts/open-endedness]] — coevolution is a core OE mechanism
- [[wiki/synthesis/insights/oee-knowledge-cluster-insight]] — related synthesis on open-ended evolution