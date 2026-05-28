---
summary: Multi-exit networks with early termination based on confidence thresholds; training strategies and connection to adaptive budget learning
tags: [early-exit, adaptive-computation, confidence, gating, deep-supervision, ml-architectures]
updated: 2026-05-25T20:22:52Z
created: 2026-05-25T20:22:52Z
---

# Early Exit Networks

*Concept page — derived from adaptive budget learning research*

## Definition

Early exit networks (also called multi-exit or adaptive depth networks) attach auxiliary classifiers to intermediate layers of a deep neural network, allowing inference to terminate before reaching the final layer. The decision to exit at a given depth is made by a confidence estimator or gating mechanism, enabling adaptive computation based on input difficulty.

Unlike standard deep networks where every input traverses all layers, early exit networks allow "easy" inputs to exit at shallow layers while "hard" inputs proceed to deeper layers. This is analogous to how humans allocate cognitive effort — simple tasks are resolved quickly, complex ones warrant deeper analysis.

## How the Exit Decision is Made

### Confidence-Based Exit

Each intermediate classifier outputs a probability distribution over classes. Exit is triggered when the maximum confidence exceeds a threshold:

```
if max(p_shallow) > τ: exit_at_shallow
else: continue_to_next_layer
```

ADEPT (2026) uses this approach with a token-level confidence predictor that is jointly trained with the backbone. DAISY (2024) uses the self-supervised loss (HuBERT) as a confidence proxy — lower reconstruction error indicates easier tokens that can exit early.

### Entropy-Based Exit

BEExformer (2024) uses fractional reduction in entropy among intermediate transformer blocks:
- Compute entropy of the classifier output at layer L
- If entropy reduction from L-1 to L is small enough, exit
- This captures "diminishing returns" of additional layers

### Fixed Depth Schedule

SPAR-K (2026) for spoken language models uses a modality-aware schedule — speech tokens exit at a fixed intermediate layer with periodic full-depth refreshes. This works because speech tokens have different statistical properties than text; confidence-based methods from text LLMs are suboptimal for speech.

## Training Strategies

### Deep Supervision

All intermediate classifiers are trained jointly with the backbone using the same task loss. Each exit head receives gradient signal from both its own output and from deeper layers via the main network — this is "deep supervision."

**Problem**: Shallow classifiers receive weaker representations because they haven't been refined by as many layers. This creates a quality-compute tradeoff.

### Two-Stage Training (LGViT, 2023)

1. **End-to-end training**: Train full model with all exit heads
2. **Self-distillation**: Freeze backbone; train shallow heads to mimic deep heads

This compensates for the representation quality gap in early layers by transferring knowledge from deep classifiers to shallow ones.

### Joint Confidence Estimation

ADEPT (2026) trains a separate confidence predictor using binary cross-entropy against "correct exit depth" labels — a form of meta-learning for compute allocation.

## Key Tradeoffs

| Factor | Early Exit Favors | Full Forward Favors |
|--------|-------------------|---------------------|
| Easy samples | Fast, low compute | No benefit |
| Hard samples | May exit too early, wrong answer | Accurate but expensive |
| Model architecture | Works best with residual connections | Depth is essential for quality |
| Hardware | Reduces FLOPs but may hurt GPU utilization | Better compute density |

## Connection to Adaptive Budget Learning

The exit decision is fundamentally a gating problem — the network must decide how much computation to allocate. In adaptive budget learning, this gating is trained explicitly (via RL, supervised loss, or distillation). In early exit networks, the gating emerges from confidence thresholds.

The gradient blocking problem also applies: when a token exits early, the early classifier receives no gradient from deeper layers' representations. This motivates the two-stage training approach and teacher-guided methods.

## Open Questions

1. **Label quality for confidence training**: Who decides what the "correct" exit depth is for each sample? Using final output as ground truth creates bias toward always-exiting; using oracle depth requires additional annotation.

2. **KV cache efficiency**: For autoregressive decoding, early exit in intermediate layers still requires computing all layers for the KV cache. ADEPT addresses this by decoupling sequential dependencies for skipped layers.

3. **Generalization of exit thresholds**: A threshold tuned on one distribution may not transfer to another. Harder test sets may have more tokens requiring full depth.

## Connections
- [[log]]
- [[concepts/mixture-of-experts]]
- [[concepts/early-exit-networks]]
- [[index]]
- [[concepts/adaptive-budget-learning]]
- [[early-exit-networks]]

- [[adaptive-budget-learning]] — gating model training; the early exit decision is a specific gating problem
- [[mixture-of-experts]] — related via shared theme of conditional computation; MoE routes across experts, early exit routes across depth
- [[adaptive-computation]] — umbrella concept

## Sources

- ADEPT (2601.03700v1) — Adaptive Dynamic Early-Exit Process for Transformers
- BEExformer (2412.05225v3) — Binarized Early Exit Transformer
- SPAR-K (2603.09215v1) — Scheduled Periodic Alternating Early Exit for Spoken Language Models
- DAISY (2406.05464v2) — Data Adaptive Self-Supervised Early Exit for Speech
- LGViT (2308.00255v1) — Dynamic Early Exiting for Vision Transformer
