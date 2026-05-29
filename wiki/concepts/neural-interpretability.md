---
created: 2026-06-03
updated: 2026-06-08
type: concept
summary: Techniques for understanding what neural networks represent internally — probing, feature visualization, representation geometry, superposition, and the relationship between activation patterns and model behavior
tags: [interpretability, neural-networks, probing, representation-geometry, superposition, feature-analysis]
sources: https://transformerlens.org/, https://arxiv.org/abs/2406.04292 (ELHSR)
status: active
confidence: 0.8
---

# Neural Interpretability

Neural interpretability is the study of understanding what neural networks represent internally and how representations give rise to behavior. It spans a broad toolkit: probing studies that train classifiers on hidden states, feature visualization that renders what neurons respond to, representation geometry that maps how concepts are arranged in activation space, and the discovery of phenomena like superposition and polysemanticity that reveal how networks pack information into limited dimensions.

## The Core Problem

Neural networks are black boxes by default — you see the input and output, but the internal processing is opaque. Neural interpretability asks: what's actually happening inside? What does the model believe? What does it represent? Where does it fail?

The practical importance: if you can't interpret a model's internal state, you can't:
- Detect when the model is uncertain or mistaken
- Understand why it makes specific errors
- Verify that safety constraints are enforced internally
- Identify when reward hacking is occurring

## Key Techniques

### Probing Studies (Linear Probes)

Train a classifier on the model's hidden states to predict some property of the input. If the classifier works well, the hidden state contains information about that property.

Example: train a linear probe on GPT-2's hidden states to predict whether the current token is a verb. High accuracy → verb information is linearly encoded in those states.

The key finding from probing: information is often linearly represented, even when the underlying computation is non-linear. This is surprising — it means you can often decode complex information with a simple linear transformation of the activations.

The [[reward-inside-model-elhsr]] (ELHSR) paper uses exactly this: a lightweight linear probe on hidden states predicts reward without processing the full text output. The model "knows" whether it got the answer right, stored in its hidden states.

### Feature Visualization

Render what a specific neuron, attention head, or direction in activation space responds to. For image models, this produces the classic "deep dream" images — what the neuron "wants to see." For language models, it produces texts that maximally activate the target unit.

Feature visualization reveals polysemanticity: individual neurons often respond to multiple unrelated concepts. This is not a bug — it's a consequence of superposition.

### Superposition

Networks have more features to represent than they have neurons. A neuron can only be in one activation state at a time, but it needs to track many independent features. The solution: represent multiple features as directions in activation space, using different linear combinations of the same neurons.

This creates superposition: a single neuron participates in representing many different features. The cost: features interfere with each other, and the geometry of the representation space matters enormously.

Sparse autoencoders (SAEs) are the primary tool for decomposing superposed features. Training an SAE on a model's activations finds a set of sparse, monosemantic features that the original representations are superposing over. Anthropic's work on SAEs (e.g., Grokking) found millions of features in small models — far more than the neuron count.

### Representation Geometry

The arrangement of concepts in activation space reveals structure:
- Similar concepts cluster together (geometry reflects semantics)
- Analogies are often represented as parallel vectors (`king - man + woman ≈ queen`)
- Different layers encode different levels of abstraction (syntax → semantics → behavior)

This connects to [[supertokens]] — high-frequency structural patterns in reasoning might be "compressed" as geometrically close directions in activation space, enabling efficient inference.

## The Superposition Problem and Sparse Autoencoders

The key insight from Anthropic's superposition research:

**Neurons ≠ features.** A single neuron participates in representing many features. Features are not "in" neurons; they are directions in the activation space.

The problem: if you want to understand what a network knows, you can't just look at individual neurons. You need to find the actual features — the directions that correspond to independent, interpretable concepts.

Sparse autoencoders solve this by learning a decomposition:

```
input activations → sparse features (interpretable) → reconstructed activations
```

The sparsity constraint forces the autoencoder to find a minimal set of features that reconstruct the original activations. These features are typically more monosemantic than the raw neurons — each feature has a clearer interpretation.

## Neural Interpretability and the MOP-EDM Framework

In the [[mop-edm-cognitive-architecture]], neural interpretability provides the measurement layer:

- **EDM's Δ signal** (disruption) is ultimately measured via activation patterns — the divergence between past and future vectors is visible in the model's hidden states
- **MOP's epistemic energy** might be measurable via hidden state properties (perplexity on known facts, context utilization, activation entropy)
- **Load-bearing reasoning analysis** uses causal mediation to identify which activation patterns are essential to conclusions

The sheaf-consistency-enforcer detects coboundary norm violations via differential activation patterns across layers — if layer L and layer L+1 have inconsistent activations, the closure status degrades.

## Connections
- [[concepts/wolfram-nks-causal-networks]]
- [[concepts/neural-interpretability]]
- [[concepts/hidden-states]]
- [[concepts/dynamical-systems]]
- [[concepts/model-editing]]
- [[concepts/activation-steering]]
- [[concepts/causal-reasoning]]
- [[wiki/index]]
- [[concepts/taylors-law]]
- [[concepts/attractor-dynamics]]
- [[concepts/latent-reasoning]]
- [[concepts/supertokens]]
- [[log]]
- [[concepts/load-bearing-reasoning]]
- [[scratchpad/jobs/reports/researcher/discovery-2026-06-08]]
- [[concepts/allometric-scaling]]
- [[concepts/power-law-scaling]]
- [[sources/articles/emotion-concepts-llm]]
- [[concepts/initialization]]
- [[scratchpad/jobs/reports/researcher/discovery-2026-08-08]]
- [[concepts/mechanistic-interpretability]]
- [[neural-interpretability]]

- [[mechanistic-interpretability]] — circuit-level analysis and reverse-engineering; neural interpretability is the broader field
- [[hidden-states]] — the raw material for neural interpretability
- [[activation-steering]] — modulation using discovered features; closed-loop biofeedback requires interpretability as the sensor
- [[load-bearing-reasoning]] — causal mediation analysis on which activations are load-bearing vs scaffolding
- [[reward-inside-model-elhsr]] — linear probe on hidden states as reward signal
- [[supertokens]] — structural patterns in reasoning that might be geometrically compressed in activation space
- Superposition — the phenomenon that motivates sparse autoencoders (see neural-interpretability.md lines 42–63 for full treatment)
- Concept: [[allometric-scaling]]
- Concept: [[causal-reasoning]]
- Concept: [[initialization]]
- Concept: [[power-law-scaling]]
- Concept: [[taylors-law]]


- [[dynamical-systems]]
- [[attractor-dynamics]]
- [[latent-reasoning]]
- [[model-editing]]
## Open Questions

1. **Scale of features**: How many features does a frontier model (GPT-4, Claude) have? Current SAEs have found millions of features in small models — frontier models likely have billions. Can we find them efficiently?

2. **Feature stability**: Do the same features exist across model runs, fine-tuning stages, or different architectures? If features are instable, interpretability tools built on one model checkpoint may not transfer.

3. **Causal vs correlational features**: Probing finds correlational features — things that are predictably present together. Are there causal features — directions that actually drive behavior, not just correlate with it?

4. **Compositional features**: High-level concepts (justice, causality, recursion) are likely composed from lower-level features. Can we map the composition structure? This connects to categorical reasoning about neural representations.