---
created: 2026-05-06T20:08:04Z
updated: 2026-05-06T21:51:04Z
type: concept
summary: A fundamental representation of spacetime in Wolfram Physics, where nodes are updating events and edges are causal dependencies in a multiway rewrite system.
tags: [wolfram-physics, spacetime, nks, computation]
sources: [[wolfram-nks-causal-networks]]
status: reference
confidence: 1.0
---

# Causal Networks (NKS)

In the context of the **[[wolfram-physics-project|Wolfram Physics Project]]** and **A New Kind of Science**, causal networks are directed graphs that represent the fundamental structure of the universe.

## Mechanics
- **Events as Nodes**: Each node represents a discrete "updating event" in a multiway rewrite system (e.g., hypergraph substitution).
- **Causal Edges**: A directed edge from Event A to Event B exists **if and only if** Event A produces an output that is consumed by Event B.
- **Emergent Spacetime**: Spacetime is not a pre-existing container but is emergent from the topology of this network.

## Distinction from Reasoning
While "causal network" is sometimes used metaphorically to describe LLM reasoning traces, the NKS definition is strictly defined by rewrite system semantics. For analysis of LLM intent and logical dependencies, see **[[load-bearing-reasoning]]**.

## Connections
- Entity: [[stephen-wolfram]]
- Project: [[wolfram-physics-project]]
- Source: [[wolfram-nks-causal-networks]]
