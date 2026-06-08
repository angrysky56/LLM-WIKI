---
summary: Steering vectors — directional activation vectors that bias model behavior; mathematical foundation for activation engineering; extraction via CAA, properties, and open questions
tags: [ml, activation-steering, interpretability, representation-engineering, inference-time]
updated: 2026-06-05T21:07:00Z
---

---
created: 2026-05-25
updated: 2026-06-07
type: concept
summary: Steering vectors — directional vectors in neural network activation space that bias model behavior toward or away from specific cognitive phenomena; the mathematical foundation for activation engineering
tags: [ml, activation-steering, interpretability, representation-engineering, inference-time]
sources: https://arxiv.org/abs/2310.01405 (RepE)
status: active
confidence: 0.72
---

# Steering Vectors

## Definition

A **steering vector** is a direction in a neural network's activation space that, when added to (or subtracted from) activations at a target layer during inference, biases the model's subsequent output toward or away from a specific high-level behavior or cognitive phenomenon.

The core premise is the **Linear Representation Hypothesis**: high-level concepts — honesty, harmlessness, power-seeking, a specific writing style — are encoded as *directions* in the model's internal representation space, not as patterns distributed across individual neurons. A steering vector is an approximation of that direction, extracted from the model's own representations and used to modulate inference.

Steering vectors are distinct from the broader concept of [[activation-steering]] (the paradigm of modulating behavior via activations) and [[activation-engineering]] (the practical methods for computing and applying them). Steering vectors are the *mathematical object* that the entire paradigm rests on.

## How Steering Vectors Are Extracted

### Contrastive Activation Addition (CAA / ActAdd)

The canonical method, introduced by the RepE paper (Zou et al., 2023):

1. **Construct contrastive prompt pairs**: Generate pairs of inputs designed to elicit opposite behaviors (e.g., "Tell the truth" vs "Lie")
2. **Run both through the model**: Cache the hidden state activations at each layer for both positive and negative prompts
3. **Compute the difference vector**: `v = mean(activations_positive) - mean(activations_negative)` at the chosen layer
4. **Normalize and scale**: The resulting vector is unit-normalized and multiplied by a scalar coefficient `α`

The resulting vector `v` points in the direction of the target behavior in activation space. Adding it during inference pushes the model toward that behavior; subtracting it pushes the model away.

### Alternative Extraction Methods

- **PCA on activation datasets**: Collect activations from many prompts, run PCA, identify the principal component that best separates the target behaviors
- **Probe-based extraction**: Train a linear probe to classify behavior from activations, then take the probe's weight vector as the steering direction
- **Difference-in-means on attention heads**: Some work extracts steering vectors from specific attention heads rather than hidden states

## Mathematical Properties

### Are steering vectors orthogonal?

The evidence is mixed. Some steering vectors for unrelated concepts appear approximately orthogonal, while semantically related concepts (e.g., "honest" and "helpful") can be correlated. This matters for **compositional steering** — if steering vectors are non-orthogonal, combining them causes interference. The [[bounded-representation-capacity]] concept formalizes this limit: activation space is finite-dimensional, and each steering direction consumes some of that capacity.

### Do they superpose?

Yes — this is the **superposition hypothesis** applied to steering. A model's activations superpose many behavioral directions simultaneously. Steering toward "honesty" may inadvertently suppress "creativity" if those directions share components in the same activation subspace. This is not a bug in the steering vector but a fundamental property of distributed representations.

### Stability across runs and model versions

Initial evidence suggests steering vectors computed from one model checkpoint don't transfer reliably to a fine-tuned version of the same model, even with identical architecture. This is an open question with practical implications: steering vectors may need to be recomputed for each model version.

## The RepE Framework: Reading vs Controlling

The RepE paper makes a critical distinction:

- **Representation Reading**: Using steering vectors as *probes* — measure how strongly a model's activations align with the steering direction on a given input, without modifying the activations. This enables behavioral monitoring at inference time.
- **Representation Control**: Actually adding the steering vector to activations to *shift* behavior. This is what most people mean by "steering."

Reading is easier, more reliable, and has fewer tradeoffs than controlling. A linear probe trained on the steering direction achieves high accuracy for monitoring, while the same steering vector used for control may degrade fluency or over-correct.

See [[../synthesis/representation-reading-for-inference-safety-monitoring|Representation Reading for Inference-Time Safety Monitoring]] for a full synthesis of reading-as-monitoring across the activation-engineering and AI safety domains.

## Key Distinction From Activation Engineering

| Property | Steering Vectors | Activation Engineering |
|----------|----------------|----------------------|
| **What** | The mathematical object (the direction vector) | The practical methods (how to apply it) |
| **Focus** | Extraction, linearity, orthogonality, superposition | Layer selection, PID tuning, multi-vector composition |
| **Core question** | Is this the right direction? | How do we apply it effectively? |

The connection: activation engineering *uses* steering vectors. The vector itself is the output of the extraction step; activation engineering takes that vector and figures out where in the network to inject it, at what scale, with what feedback.

## Connections

- [[activation-engineering]] — the practice that uses steering vectors as its primary tool
- [[activation-steering]] — the broader paradigm of behavioral control via activations
- [[mechanistic-interpretability]] — provides observability into what the steering vector captures
- [[bounded-representation-capacity]] — formalizes why steering vectors interfere when composed
- [[model-editing]] — parametric editing (weight changes) vs activation-level intervention (steering)
- [[concepts/steering-vectors]]
- [[sources/papers/repe-representation-engineering]] — the canonical RepE paper
- [[sources/articles/emotion-concepts-llm]] — Anthropic's functional emotion research, which identifies emotion-related steering directions

## Source Anchors

- [[sources/papers/repe-representation-engineering]] (0.95) — defines contrastive activation addition, the primary extraction method for steering vectors
- [[sources/articles/emotion-concepts-llm]] (0.80) — demonstrates that even complex, abstract behaviors (functional emotions) correspond to detectable steering directions
- [[synthesis/representation-reading-safety-monitoring]] — bridge page connecting representation reading to safety monitoring via the reading/controlling duality

## See Also

- [[activation-engineering]] — the practice layer built on steering vectors
- [[ai-safety]] — downstream application of steering vectors for behavioral control
- [[inference-time-compute-scaling]] — steering vectors are an inference-time technique alongside CoT and adaptive compute

## Open Questions

1. **Transferability**: Do steering vectors computed for one model architecture transfer to another? Initial evidence suggests they do not — even between model versions — but the boundary of transfer is not well characterized.
1. **Arms control verification**: Can steering vector probes serve as a verification mechanism for AI arms control treaties? The question connects to read-later [[synthesis/representation-reading-as-arms-control-verification]] — it requires answering whether probes are adversarially robust enough to survive deliberate evasion by a non-compliant signatory.
2. **Optimal extraction**: Is CAA the optimal extraction method, or can alternatives (PCA, ICA, contrastive learning) produce better steering vectors? No systematic comparison exists.
3. **Orthogonal decomposition**: Can a set of steering vectors be orthogonalized to enable clean compositional steering, or is non-orthogonality inherent to distributed representations?
4. **Minimal data requirements**: CAA requires dozens of contrastive prompt pairs per behavior. Can effective steering vectors be extracted from fewer examples — or zero-shot from the model's existing representations?
