---
summary: Memory estimates for A-LQR Jacobian caching: 2GB for A_k cache on 7B models, calibration cost ~1000 GPU-hours one-time, per-token inference is 64MB reads with no recomputation
type: concept
tags: [a-lqr, memory-estimates, jacobian-caching, implementation, closed-loop]
updated: 2026-05-21T08:28:21Z
created: 2026-05-21T08:28:21Z
sources: []
status: active
confidence: 0.8
---



# A-LQR Implementation: Memory Estimates and Jacobian Caching

## Background

The paper establishes that Activation-LQR (A-LQR) avoids the intractable O(d²) per-layer cost of computing layer-wise Jacobians at runtime by exploiting local linearity — Jacobians at different reachable activations within the same transformer layer are highly correlated. This justifies offline computation and caching of both A_k (layer-wise Jacobians) and K_k (feedback gain matrices derived via the discrete Riccati equation).

This note provides concrete memory estimates for the caching strategy.

## Notation

- d: hidden dimension (state space dimension)
- m: steering vector dimension (control input dimension)  
- T: number of transformer layers
- B: batch size (number of prompts in calibration dataset)
- N: sequence length (max tokens in calibration prompts)

## Layer-wise Jacobian Cache (A_k)

Each A_k is a d×d matrix (square Jacobian of the layer's forward pass).

**Storage per layer:** d² float32 values = d² × 4 bytes

| Model Scale | d (hidden dim) | A_k per layer | T layers (total) |
|
-|
|
|
|
| 125M (GPT-2 small) | 768 | 2.3 MB | ~75 MB |
| 1.5B (Distill) | 1600 | 10 MB | ~320 MB |
| 7B (Qwen/Llama) | 4096 | 64 MB | ~2 GB |
| 70B (Llama 3) | 8192 | 256 MB | ~8 GB |

The 7B class is the primary experimental target. 2GB for A_k cache is manageable on a 24GB GPU during offline calibration. The cost is paid once, not per-token during inference.

## Feedback Gain Matrix Cache (K_k)

LQR pre-computes K_k = -R^{-1}B_k^T P_k where P_k is the solution of the discrete Riccati equation. K_k is d×m.

**Storage per layer:** d × m float32 values = d × m × 4 bytes

Typical m values:
- Sparse steering: m = 16-64 (only a few steering directions active)
- Dense steering: m = d (full activation perturbation)

| m | d=4096 | d=8192 |
|
|
--|
--|
| 16 | 256 KB | 1 MB |
| 64 | 1 MB | 4 MB |
| 256 | 4 MB | 16 MB |
| d (4096/8192) | 64 MB | 256 MB |

For sparse steering (m=64), K_k cache for 32 layers ≈ 32 MB — negligible compared to A_k cache.

## Calibration Dataset Requirements

Local linearity assumes A_k computed from a calibration dataset is representative of all reachable activations during inference. The calibration set must:

1. Cover diverse semantic regions (not just one domain)
2. Include adversarial/edge cases (hallucination-triggering prompts)
3. Use sufficiently long sequences (N ≥ 512) to capture deep layer dynamics

A practical calibration run: B=1000 prompts, N=512, T=32 layers, d=4096. Total activations: B × N × T × d ≈ 6.5B float values = 26 GB. This is the working set for computing A_k via empirical Jacobian estimation (finite difference or backward-pass sampling).

## Computational Cost of Offline Calibration

Computing A_k via empirical estimation requires:
- Multiple forward passes per calibration prompt (to estimate directional derivatives)
- Backprop through each layer (or forward-backward gradient sampling)

For B=1000, N=512, T=32 on a 7B model: ~1000 GPU-hours on A100 (estimated, varies by implementation efficiency). This is a one-time offline cost.

Once calibrated, the A_k cache is fixed until model weights change.

## Memory Bandwidth During Inference

With A_k cached, inference adds:
- Read A_k for current layer: 64 MB (7B case)
- Matrix multiply: δh_{k+1} = A_k · δh_k + B_k · u_k (dominated by d×d and d×m ops)
- No Jacobian recomputation

This is the key efficiency gain: O(d²) compute per layer becomes O(d²) memory read + O(d²) matmul — no gradient computation, no automatic differentiation.

## Cross-Model Portability

A_k and K_k are geometry-specific. Caches computed for one model cannot be used on a different model, even from the same family, without recalibration. The local linearity property (Jacobians within same layer are highly correlated across activations) means the calibration is robust to some distribution shift, but there is no theoretical guarantee — only empirical validation.

For production systems, this means:
- Model upgrade → recalibrate
- Architecture change → recalibrate  
- Significant tokenizer change → recalibrate

The practical cost of recalibration (1000 GPU-hours) argues for selecting model families with stable architecture across versions.

## Summary

| Component | Storage (7B, d=4096, T=32) | Notes |
|
--|
--|
-|
| A_k cache (Jacobians) | 2 GB | One-time offline computation |
| K_k cache (gain matrices) | 32 MB (m=64 sparse) to 2 GB (dense) | Depends on steering strategy |
| Calibration working set | ~26 GB | B=1000, N=512, temporary during calibration |
| **Total offline** | ~2-4 GB | Excluding calibration working set |
| **Per-token inference** | 64 MB reads (A_k only) | No recomputation |

The tractable regime is clearly defined: 7B models, sparse steering (m ≤ 64), offline Jacobian calibration. Dense steering (m = d) pushes K_k cache to 64 MB per layer × 32 = 2 GB, still tractable but on the edge for memory-constrained deployment.
