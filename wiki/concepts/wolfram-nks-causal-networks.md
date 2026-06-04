---
created: 2026-05-25
updated: 2026-07-03
type: concept
summary: Stephen Wolfram's causal network interpretation of spacetime and computation — hypergraph rewriting, multiway branching, causal disruption as physical/computational irreducibility
tags: [wolfram-physics, nks, causal-networks, spacetime, computation, multiway]
sources: https://www.stephenwolfram.com/publications/a-new-kind-science/
status: active
confidence: 0.75
---

# Wolfram NKS Causal Networks

## Definition

Stephen Wolfram's causal networks are directed graphs where **nodes represent updating events** (discrete computation steps in a rewrite system) and **directed edges represent causal dependencies** — event A causally influences event B if A's output is consumed by B.

This is the representational framework underlying both [[wolfram-physics-project]] (physical) and [[computational-irreducibility]] (computational). The causal network is what you get when you trace the actual execution of a computationally irreducible system — a record of which events caused which.

## Why It Matters

The key claim: spacetime and matter are not pre-existing containers — they **emerge from the topology of causal networks**. The structure of the network (how events connect, what the long-range topology looks like) determines physical properties like dimension, locality, and conservation laws.

In Wolfram's framework:
- **Time** = the traversal of the causal network from past to future
- **Space** = the slice of the network at a given instant (the set of nodes whose causal past includes the current node)
- **Matter** = persistent structures in the network (cycles, stable subgraphs)
- **Causality** = the directed edges; what can influence what

## Multiway Rewrite Systems

The underlying computation model is a **multiway rewrite system**: multiple rules can apply simultaneously, producing branching histories. At each step, many possible rewrites may apply to many locations in the hypergraph. All branches exist in the multiway system — the network represents all possible computations simultaneously.

This is the source of [[computational-irreducibility]] in the physical context: you cannot know which branch the physical universe "actually" takes because there is no selection — all paths are taken. Observing which path we experience is itself a computation that must be simulated to determine.

## Causal Disruption and Physical Irreducibility

In the Wolfram Physics framework, **causal disruption** is the key phenomenon: when a multiway branch creates divergent causal histories, the causal network may have multiple incompatible paths from past to future. This is physically realized as quantum indeterminacy.

The connection to computational irreducibility: if the only way to determine which branch structure leads to our observed physical state is to simulate the entire multiway system, then the physics is computationally irreducible. There is no shortcut to knowing which outcome will be ours.

## Connection to Causal Reasoning (LLM Context)

Note: there is a separate use of "causal network" in the context of causal reasoning in LLMs — see [[causal-reasoning]]. The NKS causal network is a different concept: a structural representation of computation, not a model of how one event causes another in a semantic sense.

The **distinction** matters: NKS causal networks represent the causal structure of a computational process (what computes what). Causal reasoning in LLMs infers causal relationships from observational data (what predicts what). The former is about actual causal dependence in a rewrite system; the latter is about statistical correlations that can be interpreted causally.

## Connections
- [[concepts/causal-networks]]
- [[entities/people/stephen-wolfram]]
- [[log]]
- [[concepts/wolfram-physics-project]]
- [[concepts/wolfram-nks-causal-networks]]
- [[wiki/index]]
- [[concepts/wolfram-nks-causal-networks]]

- [[wolfram-physics-project]] — the broader research program; causal networks are the representational framework
- [[computational-irreducibility]] — causal networks are the empirical trace of computationally irreducible processes; the network must be simulated to know its structure
- [[causal-networks]] — the reference page distinguishes NKS causal networks from causal reasoning in LLMs
- [[stephen-wolfram]] — the originator; see entity page
- [[emergence]] — the topological properties of causal networks (dimension, connectivity) emerge from local rewrite rules

## Open Questions

1. **Correspondence to physics**: Does the Wolfram causal network framework reproduce known physics (relativity, quantum mechanics)? The claim is yes, but the derivation of standard model physics from rewrite rules is still incomplete.

2. **Multiway observer problem**: If all branches exist in the multiway system, why do we experience a single history? The framework needs an account of how observation selects (or contextualizes) a branch history.

3. **Irreducibility across scales**: At which scales does the causal network become reducible? Macroscopic physics has effective theories — does this mean the underlying causal network is partially reducible at certain scales?

4. **Connection to neural networks**: Could transformer attention be viewed as a causal network where tokens are events and attention edges are causal dependencies? This would link the Wolfram framework to [[neural-interpretability]].

## Limitations

- The Wolfram Physics framework is not empirically verified against standard physics — it is a candidate theory
- Causal networks in the NKS sense are defined at the level of the underlying hypergraph rewrite rules, not at the level of observable physical quantities
- The computational complexity of simulating full multiway systems is prohibitive — reducing the framework to testable predictions is non-trivial