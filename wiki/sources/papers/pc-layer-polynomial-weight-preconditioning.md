---
summary: A polynomial preconditioning layer that stabilizes weight singular values during LLM pre-training, yielding 20-35% faster convergence and 0.3-0.8 perplexity improvement.
tags: [paper, llm, pretraining, optimization, preconditioning, training-stability]
updated: 2026-06-06T16:58:46Z
created: 2026-06-06T16:58:46Z
---

---
created: 2026-06-06T08:00:00Z
updated: 2026-06-06T08:00:00Z
type: source
summary: "A preconditioning layer (PC Layer) that reshapes weight singular values via polynomial preconditioner to maintain healthy conditioning throughout LLM pre-training."
tags: [paper, llm, pretraining, optimization, preconditioning, training-stability]
arxiv_id: "2606.06470v1"
status: active
confidence: 0.85
---

# PC Layer: Polynomial Weight Preconditioning for Improving LLM Pre-Training

**Authors:** Senmiao Wang, Tiantian Fang, Haoran Zhang, Yushun Zhang, Kunxiang Zhao, Alex Schwing, Ruoyu Sun

**arXiv:** [2606.06470v1](https://arxiv.org/abs/2606.06470v1) | June 2026

## Problem

Large language model pre-training suffers from unstable weight conditioning as training progresses. The singular value distribution of weight matrices tends to degrade over time — some singular values grow dominant while others shrink — which slows convergence and can lead to training collapse. Existing approaches include normalization layers (LayerNorm, RMSNorm), learning rate schedules, and weight decay, but none directly address the *conditioning of the weight matrices themselves* during training.

## Method: Preconditioning (PC) Layer

The PC Layer is a lightweight weight parameterization module inserted at each weight matrix:

1. **Polynomial Preconditioner**: Each weight matrix W is reparameterized as W = P(A) where P is a learnable low-degree polynomial applied to A's singular values. The PC layer learns polynomial coefficients that dynamically reshape the singular value spectrum.

2. **Forward pass**: Instead of computing Wx directly, the PC layer computes P(A)x via iterative application, using Chebyshev polynomial expansions for numerical stability.

3. **Backward pass**: Gradients flow through the preconditioner, which stabilizes the gradient conditioning — preventing the ill-conditioning that causes training to stall.

4. **Integration**: PC layers replace standard linear layers. The polynomial degree (typically 3-5) adds minimal computational overhead.

**Theoretical contribution**: For deep *linear* networks, the authors prove that uniformly bounding each layer's condition number via PC layers ensures the overall network condition number remains bounded, directly linking layer-level preconditioning to global training stability.

## Key Results

- PC Layer improves **pre-training perplexity by 0.3-0.8** across GPT-2 scale models (125M-1.5B parameters) compared to standard training.
- Training converges **20-35% faster** to the same loss target.
- Singular value spectrum remains stable throughout training — the condition number of weight matrices stays within a tight band, unlike baseline training where it diverges.
- Compatible with AdamW optimizer — PC + AdamW outperforms AdamW alone.
- Memory overhead: ~5% additional parameters (the polynomial coefficients). Compute overhead: ~3-8% per forward pass.

## Limitations

- Only validated up to 1.5B parameters — scaling behavior to 10B+ models is unknown.
- Polynomial degree introduces a hyperparameter that needs tuning per model scale.
- Theoretical guarantees only hold for linear networks; the nonlinear case relies on empirical evidence.
- The 3-8% compute overhead per forward pass may compound at very large scales.
- Interaction with other training stabilizers (gradient clipping, warmup schedules) not fully explored.

## Connections

- [[optimization]] — Directly addresses the optimization landscape of LLM pre-training.
- [[layer-normalization]] — PC Layer is complementary to normalization; they address different sources of training instability.
- [[adaptive-optimizers]] — Works with AdamW, suggesting the conditioning issue is orthogonal to adaptive gradient methods.
- [[pretraining]] — A practical improvement to the pre-training pipeline applicable to any transformer-based LLM.
- [[weight-decay]] — The paper could inform how weight decay interacts with singular value conditioning.

## Key Quote

> "We propose a preconditioning (PC) layer — a weight parameterization via polynomial preconditioner that ensures stable weight conditioning throughout LLM training."

## Significance

This paper takes a principled approach to a practical problem. Rather than another architectural trick or learning rate heuristic, the PC Layer provides mathematical grounding for stable LLM training. If it scales to frontier models, it could become a standard component of the pre-training recipe — conceptually similar to how LayerNorm became universal.
