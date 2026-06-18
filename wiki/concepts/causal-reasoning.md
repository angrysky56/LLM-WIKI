---
created: 2026-06-03
updated: 2026-07-14
type: concept
summary: Causal inference and reasoning capabilities in AI systems — structural causal models, do-calculus, causal discovery, Graph of Thoughts as causal reasoning scaffold, and integration with language models
tags: [causal-reasoning, causal-inference, causal-discovery, reasoning, pearl, machine-learning, graph-of-thoughts]
sources: https://arxiv.org/abs/2406.04292 (ELHSR hidden-state causal signals)
status: active
confidence: 0.85
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

## Graph of Thoughts as Structural Causal Model

Graph of Thoughts (GoT) doesn't just *use* causal reasoning — it **is** a structural causal model of reasoning. This is not an analogy; it's a formal isomorphism:

1. **DAG as SCM**: Each GoT node is a variable governed by structural equations encoding dependencies on parent nodes. Unlike static SCMs, GoT is *dynamic* — the graph can be modified (split, merge, loop) during reasoning, adapting structure to the problem.

2. **Operations as causal inference**:
   - `generate` (split) ≈ **do-operator**: Intervene on a thought to create alternative reasoning branches
   - `aggregate` (merge) ≈ **causal effect computation**: Synthesize multiple branches, mirroring how conditional independence tests combine evidence
   - `score` / `keep_best_n` ≈ **conditioning**: Select thoughts by quality, analogous to conditioning on specific variables
   - `improve` ≈ **counterfactual**: Ask "what if this thought were different?" and compute the improvement

3. **Graph metrics as causal diagnostics** (`got_graph_metrics`):
   | GoT metric | Causal discovery analog | Interpretation |
   |------------|------------------------|----------------|
   | Density | Faithfulness check | Too dense → confounding; too sparse → missing edges |
   | Path length | Mediation depth | Long paths = mediated causal chains; too long = error propagation |
   | Clustering | Latent common cause detection | High clustering → shared premises or confounders (V-structures) |
   | Hub reliance | Confounder fragility | Concentrated betweenness = single-point-of-failure reasoning |

   A well-conditioned reasoning DAG has moderate density, bounded path length, and distributed betweenness — the same criteria a causal discovery algorithm uses to score candidate graphs.

4. **Explicit vs implicit causal structure**: The open question "do transformers learn causal structure?" reveals a deeper distinction. Attention patterns may recover graphs resembling causal structure, but this is *descriptive causal discovery* — inferring structure from co-occurrence. GoT's DAG is *prescriptive causal reasoning* — specifying how reasoning should flow. This parallels the SCM argument: structural models over statistical ones because explicit structure supports do-calculus queries (interventions) that observational patterns alone cannot answer. Attention cannot distinguish "A causes B" from "A and B share a cause." GoT's labeled edges can.

## Connections
- [[concepts/formal-methods]] — causal models are structural specifications amenable to formal verification
- [[concepts/world-model]] — causal structure is a key component of internal world representations
- [[concepts/mcts]] — tree search with causal backpropagation
- [[concepts/counterfactual]] — counterfactual reasoning is the third rung of Pearl's ladder
- [[concepts/in-context-learning]] — some argue ICL involves implicit causal inference
- [[concepts/neural-interpretability]] — ELHSR hidden-state causal signals use activation-level probing
- [[concepts/maximum-occupancy-principle]] — path entropy maximization as causal exploration hypothesis
- [[synthesis/verifiable-graph-context-protocol]] — VGCP's DAG is a causal reasoning scaffold
- [[entities/tools/graph-of-thoughts]] — GoT is a structural causal model of reasoning; its DAG enables do-calculus on thought sequences
- [[log]]
- [[scratchpad/jobs/reports/researcher/discovery-2026-06-09]]
## Open Questions

- **Do transformers implicitly learn causal structure?** The PC algorithm run on attention patterns produces graphs that resemble true causal structure in some cases — but whether this is genuine causal representation or just statistical association is debated. GoT suggests a complementary answer: even if transformers learn implicit causal structure, making it explicit through a formal DAG provides verifiability, auditability, and intervention capability (do-calculus) that implicit structure lacks.
- **Causal abstract reasoning**: Can LLMs transfer causal reasoning learned in one domain to a novel but structurally similar domain?
- **Causal world models for LLM agents**: How to build a causal model of the environment for a text-based agent operating in a code repository or document corpus
- **GoT as causal reasoning testbed**: Can GoT's explicit causal graph be used to *evaluate* whether a reasoning chain is genuinely causal (each step produces the next) rather than merely sequential (steps follow each other)? This would operationalize the distinction between correlation and causation at the reasoning level.