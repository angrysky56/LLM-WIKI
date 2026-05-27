---
summary: Techniques for modifying trained neural network weights or representations directly — locate-edit frameworks, Knowledge Neurons, ROME
tags: [model-editing, knowledge-updates, fine-tuning, interpretability, llm]
updated: 2026-05-27T14:05:05Z
---

---
created: 2026-05-25
updated: 2026-08-08
type: concept
summary: Techniques for modifying specific knowledge or behaviors in trained neural networks — locate-edit frameworks, Knowledge Neurons, ROME, and gradient-based approaches
tags: [model-editing, knowledge-updates, fine-tuning, interpretability, llm]
sources: https://arxiv.org/abs/2105.04361 (ROME), https://arxiv.org/abs/2106.01751 (Knowledge Neurons), https://arxiv.org/abs/2312.14125 (TransformerPatch)
status: active
confidence: 0.75
---

# Model Editing

## Definition

Model editing refers to techniques for modifying specific knowledge, behaviors, or capabilities in a trained neural network — updating individual facts or patterns without affecting unrelated performance. The goal is surgical precision: change exactly what needs to change, leave everything else intact.

This is distinct from fine-tuning (which updates many parameters broadly) and prompt-based methods (which only affect the current context window). Model editing targets the model's parametric memory directly.

## The Core Problem

LLMs store factual associations across their parameters in distributed, superposed representations. When a fact changes in the world, or when the model has an error that needs correcting, you can't simply open a file and edit a line. Model editing researchers ask: can we identify *where* a piece of knowledge lives in the network and update it directly?

Three failure modes make this hard:
- **Locality**: An edit affects only the target fact, not other facts
- **Generalization**: The edited knowledge generalizes correctly across paraphrases and contexts
- **Fluency preservation**: Editing doesn't hurt unrelated capabilities

## Primary Methods

### ROME (Rank-One Model Editing)

ROME (Meng et al., 2022) identifies that factual associations in MLPs are approximately rank-one transforms. The technique:
1. Use causally-motivated intervention to identify the layer and MLP component responsible for a specific factual association
2. Compute a rank-one weight update that replaces the old association with the new one
3. Maintain a causal tracing consistency constraint to ensure locality

The key insight: factual knowledge in MLPs has a simple structure that can be decomposed and edited with low-rank updates.

### Knowledge Neurons

Dai et al. (2022) identified that certain neurons in transformers activate specifically for factual associations. The approach:
1. Use knock-out studies to identify fact-specific neurons
2. Ablate or modify those neurons to update the associated fact
3. Problem: Knowledge neurons are rarely monosemantic — ablation has collateral damage

### TransformerPatch (EE-Kpt)

TransformerPatch (2023) uses ek明天
1. Locate: identify the MLP layers most relevant to the target fact via causal tracing
2. Compute key: derive the key phrase that should maximally activate the target subject
3. Patch: apply a low-rank update to redirect associations

More general than ROME but with similar locality guarantees.

### Gradient-Based Methods (FT-δ, KE, KN)

- **FT-δ**: Fine-tune on the new fact, then compute the difference (δ) between old and new weights. Apply only the δ to target layers.
- **KE (Knowledge Editor)**: Meta-learning approach — train a small editor network that learns to apply edits to the target model
- **KN+**: Upgraded Knowledge Neurons with better generalization via targeted ablation

## Connections

- [[fine-tuning]] — broader parameter update; model editing is surgical fine-tuning
- [[steering-vectors]] — activation steering as an alternative to weight editing
- [[activation-steering]] — inference-time intervention vs. parametric editing
- [[neural-interpretability]] — causal tracing and probing provide the localization mechanisms
- [[bounded-representation-capacity]] — editing works because knowledge is superposed; capacity constraints determine edit density limits
- [[catastrophic-forgetting]] — the anti-pattern; editing aims to avoid the generalization failures that forgetting causes

## Open Questions

1. **Compositionality**: Can we edit composed facts (A is X, B is Y, A+B is Z) without editing each independently?
2. **Temporal binding**: How do we handle facts about time-specific knowledge (laws, prices, facts) that change? The model must represent temporal validity, not just current-state facts.
3. **Unlearning vs. editing**: Knowledge unlearning (remove a capability) is the inverse problem. Can we formulate unlearning as negative editing?
4. **Scalability**: ROME requires a full forward-backward pass per edit. At 100K edits in a production system, the compute cost is prohibitive.

## Limitations

- **Causal tracing overhead**: ROME's localization step requires multiple forward passes with interventions — expensive at scale
- **Distributed representations**: Most facts aren't stored in a single location — editing one site may leave shadow associations elsewhere
- **Generalization brittleness**: Simple edits often fail to generalize beyond the exact phrasing used during localization
- **Readiness gap**: Most published methods (2021-2023) haven't been demonstrated at production scale — deployment risk is high
