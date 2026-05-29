---
summary: Weight decay induces Solomonoff universal prior in fixed precision — weight norm = Kolmogorov complexity
tags: [kolmogorov-complexity, weight-decay, solomonoff, fixed-precision, theory, inductive-bias]
updated: 2026-05-28T20:01:18Z
created: 2026-05-28T20:01:18Z
---

# Neural Weight Norm = Kolmogorov Complexity

**Paper**: [2605.10878](https://arxiv.org/pdf/2605.10878)  
**Author**: Tiberiu Musat (ETH Zürich)  
**Date**: 2026-05-28

## Core Claim

In any fixed-precision regime, the minimum weight norm of a looped neural network outputting a binary string `s` equals the Kolmogorov complexity `K(s)` up to a logarithmic factor:

```
N(s) ≤ K(s) ≤ N(s) · log N(s)
```

where `N(s)` = minimum non-zero parameter count for a fixed-precision looped network outputting `s`. Both bounds are **tight** — the log factor is realized by permutation encodings.

## Why Fixed Precision Is Essential

- **Real-valued weights are super-Turing**: Siegelmann-Sontag showed bounded-magnitude real-weight RNNs decide non-recursively-enumerable languages. For such networks `K(s) = ∞` while `||θ||` is finite → bound is vacuous.
- **Rational/computable reals still break it**: a single `p/q` with `|p/q| ≤ B` carries unbounded information in its numerator/denominator → `K(w)` is unbounded over the ball.
- **Only fixed precision works**: Each weight becomes a `O(1)`-bit object. Magnitude and description length lock together. This is the regime where the question even has content — and it's the regime all real hardware uses (fp16, bf16, int8, int4).

## The Lp Collapse

In fixed precision, every Lp norm collapses to non-zero parameter count up to constants:

```
δ^p · ||θ||₀ ≤ ||θ||_p^p ≤ M^p · ||θ||₀
```

So L1, L2, and any other Lp regularizer all control the same underlying quantity: **sparsity (non-zero parameter count)**. The penalty's behaviour during training depends on `p`; the resulting Kolmogorov-complexity profile does not.

## Two-Sided Bound (Proof Sketch)

**Upper bound** (`K(s) ≤ N(s) log N(s)`): Encode any fixed-precision network `θ` with `W = ||θ||₀` non-zero parameters. Each parameter needs `≤ 3 log W + O(1)` bits: layer index + source neuron + target neuron + value. A constant-size simulator program reconstructs and runs the network. Total: `cd · W · log W + cd`. Tightness witness: permutation matrices, where `N(s_π) = Θ(N)` but `K(s_π) = Θ(N log N)` for typical `π`.

**Lower bound** (`N(s) ≤ K(s)`): Take a shortest program `p` for `s` on a universal Turing machine `U`. Load `p` into a universal looped network `TU` via `|p|` routing weights (one per program bit). Total: `K(s) + cU` non-zero parameters.

## Solomonoff Corollary

The L2 weight-decay penalty term `−log π(θ) ∝ λ||θ||₂²` induces a prior on network outputs:

```
Q(s) := ∫_{θ: outputs s} π(θ)
```

**Corollary**: For every computable `s`:

```
2^{−K(s)−α} ≤ Q(s) ≤ 2^{−K(s) / (β log K(s))}
```

Equivalently: `−log Q(s) ∈ [K(s)/(β log K(s)), K(s)+α]` — the induced output prior matches Solomonoff's universal prior in the exponent up to a logarithmic factor. **Weight decay is asymptotically the optimal Bayesian prior over computable functions.**

## Empirical Predictions

1. **Low-K tasks benefit more from weight decay**: algorithmic reasoning, regular languages, structured prediction — as opposed to essentially random data.
2. **Quantisation strengthens the bias**: int4/int8 makes `||θ||_2²` track non-zero count exactly, making quantisation-aware sparse training a more direct implementation of the induced output prior.
3. **Effective complexity is log-augmented**: the right effective complexity for predicting generalisation is `||θ||₂² · log||θ||₂²`, not raw parameter count.
4. **Looped depth helps on low-K targets**: chain-of-thought, deep equilibrium models outperform fixed-depth on bounded-but-variable Kolmogorov complexity.
5. **All sparsity priors converge**: L1 decay, magnitude pruning, variational dropout all target `||θ||₀` in fixed precision → equivalent output priors up to constants.

## Limitations

- Constants are large; result is conceptual rather than predictive at small scale
- Restricted to looped networks from `x₀ = 0`; feedforward needs adaptation
- Corollary concerns the induced prior, not what gradient descent finds
- Not experimentally validated in the paper
- Spectral/operator norms (Lipschitz) are not captured

## Conjectures Posed

1. Weight norm tracks data complexity: `||θ||₂²` at convergence tracks `K(S)` in expectation for networks trained with L2 decay.
2. Flat minima are downstream: minima of low description length are locally flat in MDL coordinates.
3. Effective complexity is log-augmented: `||θ||₂² · log||θ||₂²` not raw norm.

## Relevance to Meta-Harness / Essan

The induction/regularization layer that explains weight decay's effectiveness may be the key to understanding the Essan symbol training idea: train Essan symbols as internal representation markers via fine-tuning with contrastive loss — using activation geometry as the training signal for hallucination detection. The paper provides the theoretical grounding: **weight norm = description length = complexity measure of what the network "knows"**. If Essan symbols are trained to mark activation geometry regions corresponding to low-K (well-described, generalizable) vs high-K (overfitted, hallucinatable) representations, the geometric separation is the complexity signal.

## References

- Li & Wang (2025): Constant bit-size transformers are Turing complete
- Giannou et al. (2023): Looped transformers as programmable computers
- Siegelmann & Sontag (1995): Super-Turing power of real-valued RNNs
- Solomonoff (1964): Universal prior
- Shaw et al. (2026): Bridging Kolmogorov complexity and deep learning (MDL-optimal transformers)

## Tags

#regularization #kolmogorov-complexity #solomonoff #weight-decay #fixed-precision #looped-networks #MDL #theory #inductive-bias
