---
created: 2026-06-03
updated: 2026-06-09
type: concept
summary: Causal inference and reasoning capabilities in AI systems — structural causal models, do-calculus, causal discovery, and integration with language models
tags: [causal-reasoning, causal-inference, causal-discovery, reasoning, pearl, machine-learning]
sources: https://arxiv.org/abs/2406.04292 (ELHSR hidden-state causal signals)
status: active
confidence: 0.8
---

# Causal Reasoning

**Also known as:** Causal inference, causal discovery, counterfactual reasoning

## What It Is

Causal reasoning is the ability to distinguish correlation from causation, to predict how interventions will change outcomes, and to reason about counterfactuals — what would have happened if circumstances had been different.

This differs from statistical association (which only describes observed correlations) by requiring a structural model of *how* variables are related — not just that they co-occur.

## The Structural Causal Model Framework

Following Pearl, a structural causal model (SCM) consists of:

1. **Directed acyclic graph (DAG)** over variables X₁, ..., Xₙ
2. **Structural equations** specifying how each variable is determined by its parents

Example: X ← Z → Y forms a V-structure (collider). Knowing Z, X and Y are dependent even if not directly connected.

### The Do-Calculus

Standard probability: P(Y | X) — what's the probability of Y given that we observed X?

Causal probability: P(Y | do(X=x)) — what's the probability of Y if we *intervene* to set X = x?

The do-operator represents acting on the system, not just observing it. The distinction matters:
- **Observing** X = x may be confounded by a common cause Z → X, Z → Y
- **Doing** X = x cuts all incoming edges to X, eliminating the confounding path

The do-calculus provides three rules for propagating do-operators through DAGs, enabling identification of causal effects from observational data when direct experimentation isn't possible.

### Counterfactuals

Counterfactual reasoning asks: *If I had done X instead of Y, what would have happened?*

In SCM terms: Given observed outcome Y = y after action X = x, the counterfactual Yₓ=x' is computed by:
1. Abduct: Update the distribution over unobserved variables given the observed evidence
2. Action: Set X = x' in the structural equations
3. Predict: Compute the counterfactual outcome

This requires a full causal model, not just statistical correlations.

## Causal Discovery

Causal discovery algorithms infer the causal structure (DAG) from observational data. Key approaches:

| Method | Principle |
|--------|-----------|
| **PC algorithm** | Constraint-based: conditional independence tests → skeleton → orientation |
| **FCI algorithm** | Handles hidden confounders (extends PC) |
| **NOTEARS** | Continuous optimization for DAG structure via smooth acyclicity constraint |
| **GraN-DAG** | Gradient-based DAG learning with neural networks |
| **Diffanon** | Privacy-preserving causal discovery |

## LLM Integration

Recent work explores whether LLMs can reason causally:

- **Causal inference from text**: Can models distinguish confounded vs causal relationships in scenarios described in text?
- **Causal representation learning**: Learning causal structures from high-dimensional data like text
- **ELHSR (Evidence Location in Hidden States Reward)**: arXiv 2406.04292 showed that LLM hidden states contain causal signals about reasoning correctness — linear probes on concatenated hidden states predict outcome correctness better than the final output alone

The connection to [[world-model]]: A world model is fundamentally causal if it represents how actions change state, not just what states co-occur. Causal reasoning enables the counterfactual planning that distinguishes world models from simple state observation.

## Connections
- [[concepts/formal-methods]]
- [[log]]
- [[scratchpad/jobs/reports/researcher/discovery-2026-06-09]]
- [[wiki/index]]
- [[concepts/world-model]]
- [[concepts/mcts]]
- [[concepts/counterfactual]]
- [[concepts/in-context-learning]]
- [[concepts/wolfram-nks-causal-networks]]
- [[concepts/neural-interpretability]]
- [[synthesis/verifiable-graph-context-protocol]]
- [[concepts/causal-reasoning]]
- [[concepts/maximum-occupancy-principle]]
- [[causal-reasoning]]

- [[world-model]] — causal structure is a key component of internal world representations
- [[concepts/maximum-occupancy-principle]] — MOP's path entropy maximization can be viewed as a causal hypothesis about what drives exploration behavior
- [[neural-interpretability]] — hidden-state causal signals (ELHSR) use the same activation data that neural interpretability studies
- [[formal-methods]] — causal models are a form of structural specification amenable to formal verification
- [[in-context-learning]] — some argue in-context learning itself involves implicit causal inference
- Concept: [[MCTS]]


- [[counterfactual]]
- [[MCTS]]
## Open Questions

- **Do transformers implicitly learn causal structure?** The PC algorithm run on attention patterns produces graphs that resemble true causal structure in some cases — but whether this is genuine causal representation or just statistical association is debated
- **Causal abstract reasoning**: Can LLMs transfer causal reasoning learned in one domain to a novel but structurally similar domain?
- **Causal world models for LLM agents**: How to build a causal model of the environment for a text-based agent operating in a code repository or document corpus