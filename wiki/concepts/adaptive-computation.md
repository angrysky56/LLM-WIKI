---
created: 2026-06-16
updated: 2026-06-30
type: concept
summary: Adaptive computation time in neural networks — dynamically adjusting computation per input rather than applying fixed-depth processing; includes early exit, mixture-of-depths, and learned stopping criteria
tags: [adaptive-computation, neural-architecture, inference-efficiency, routing, early-exit, mixture-of-depths]
sources: https://arxiv.org/abs/1601.00353 (ACT, Graves 2016), https://arxiv.org/abs/2305.02144 (Depth-adaptive RNN), https://arxiv.org/abs/2406.12743 (SPAD, 2024), https://arxiv.org/abs/2502.03380 (adaptive budget learning survey)
status: active
confidence: 0.78
---

# Adaptive Computation

## Definition

Adaptive computation refers to neural network architectures that dynamically adjust the amount of computation applied to each input, rather than applying a fixed computational budget uniformly. The core idea: not all inputs require the same depth of processing. Simple inputs can be handled with shallow computation; hard inputs that require more reasoning get deeper processing.

This is distinct from conditional computation (which expert to activate) and includes three main mechanisms:
- **Early exit**: Process through fewer layers; exit when confident
- **Mixture of depths**: Skip layers or apply variable-depth processing per token
- **Adaptive computation time (ACT)**: Learn a stopping criterion that varies per position

## Why It Matters

Fixed-depth processing is inefficient: a simple arithmetic query and a complex mathematical proof require the same number of forward passes. This inefficiency compounds at scale. Adaptive computation addresses:

1. **Inference cost reduction**: Cheap inputs don't need full model depth — early exit can reduce latency and FLOPs by 40-60% on average with minimal quality degradation
2. **Test-time compute scaling**: Reasoning models (o1/o3 class) use more inference-time compute on hard problems. Adaptive computation formalizes this — allocate more compute where it helps
3. **Bounded rationality alignment**: From the [[bounded-rationality]] perspective, fixed-depth processing wastes reasoning resources on problems that don't need them. Adaptive computation is the architectural realization of efficient resource allocation

## Mechanisms

### Early Exit Networks

Early exit adds classification/embedding heads at intermediate layers. The network can exit at layer L if the intermediate prediction is confident enough, skipping the remaining layers.

Key challenge: shallow layers have weaker representations than deep layers. This is addressed via:
- **Self-distillation**: Deep heads teach shallow heads (LGViT two-stage training)
- **Confidence calibration**: Exit only when a calibrated confidence threshold is exceeded
- **Ensemble of exits**: Combine predictions from multiple exit depths

### Mixture of Depths

Rather than exiting, the model skips entire residual blocks for some tokens — effectively variable depth per token. Proposed in MoD (Dehghani et al., 2019) and refined in subsequent work.

The router decides: for this token, should I apply this layer's computation or skip it?

### Adaptive Computation Time (ACT)

Graves (2016) introduced ACT: a scalar halting unit at each step decides whether to emit an output or continue processing. The network learns when to stop — effectively a learned early stopping criterion.

Limitations: ACT introduces significant overhead (the halting unit must be evaluated at each step) and the halting decisions are not fully differentiable.

## Connections
- [[mixture-of-recursions 1]]
- [[concepts/agentic-reasoning]]
- [[concepts/adaptive-budget-learning]]
- [[log]]
- [[concepts/mixture-of-experts]]
- [[wiki/index]]
- [[concepts/scaling-laws]]
- [[concepts/llm-reasoning]]
- [[concepts/adaptive-computation]]
- [[concepts/early-exit-networks]]
- [[concepts/adaptive-computation]]

- [[mixture-of-experts]] — gating is the router in MoE; both MoE and adaptive computation address conditional computation
- [[adaptive-budget-learning]] — the specific problem of training gating models; includes early exit and RL approaches
- [[scaling-laws]] — adaptive computation is one response to the diminishing returns of uniform depth scaling
- [[mixture-of-depths]] — stub; this concept is the parent topic
- [[llm-reasoning]] — reasoning models are a form of adaptive computation: more tokens for harder problems
- [[epistemic-energy]] — adaptive computation is the architectural substrate; epistemic energy depletion is the principled stopping criterion
- [[bounded-rationality]] — the theoretical motivation: don't spend more reasoning resources than the problem requires

- [[agentic-reasoning]]
- [[early-exit-networks]]
## Limitations

- **Confidence calibration**: Early exit requires calibrated confidence estimates. Neural networks are notoriously overconfident on incorrect predictions.
- **Skip connection conflicts**: Skipping layers can break residual connections — gradients from early exits must still propagate correctly.
- **Hardware efficiency**: Variable-length computation is harder to batch efficiently than fixed-depth. GPU kernels for early exit are less optimized than dense matmuls.
- **Representation quality**: Shallow layers have demonstrably weaker representations for abstract reasoning tasks. Early exit works well for classification; less clear for generation.

## Open Questions

1. **Optimal exit criteria**: What is the best confidence measure for early exit in transformer language models? Attention entropy? Prediction confidence? Perplexity on a held-out calibration set?

2. **Training stability**: How do you train early-exit models without the shallow heads becoming undertrained compared to deep heads?

3. **Interaction with RLHF**: Does adaptive computation interact badly with RLHF? If the exit policy was trained with fixed-depth models, the distribution shift under RLHF may break exit confidence calibration.
