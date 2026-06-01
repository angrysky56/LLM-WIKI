---
summary: SHAP (SHapley Additive exPlanations) — game-theory-grounded framework for explaining individual ML predictions via Shapley-value feature attribution
tags: [shap, interpretability, explainability, shapley-values, model-interpretation, feature-attribution, game-theory]
updated: 2026-06-01T14:05:33Z
---

---
created: 2026-06-03
updated: 2026-06-03
type: concept
summary: "SHAP (SHapley Additive exPlanations) — game-theory-grounded framework for explaining individual ML predictions via Shapley-value feature attribution"
tags: [shap, interpretability, explainability, shapley-values, model-interpretation, feature-attribution, game-theory]
sources:
  - https://arxiv.org/abs/1705.07874
  - https://arxiv.org/abs/1802.03888
  - wiki/sources/papers/proxy-based-shapley-banzhaf-2026.md
status: active
confidence: 0.72
---

# SHAP (SHapley Additive exPlanations)

## Definition

**SHAP** is a unified framework for interpreting individual predictions of any machine-learning model by attributing the contribution of each input feature using **Shapley values** from cooperative game theory. The central claim: SHAP is the *unique* additive feature attribution method that satisfies three desirable properties — **local accuracy** (the explanation matches the model's output for that input), **missingness** (a feature that is missing gets zero attribution), and **consistency** (if a feature contributes more in a new model, its SHAP value cannot decrease).

The formal guarantee is what distinguishes SHAP from older heuristic attribution methods (LIME, classical permutation importance). SHAP values are the *only* attribution that satisfies all three axioms simultaneously. That axiomatic grounding is the original contribution of Lundberg & Lee (NeurIPS 2017).

## Core Idea

Treat the prediction task as a **cooperative game** where:

- **Players** = input features
- **Value function** ν(S) = expected model output when only features in coalition S are "known"
- **Payoff** = Shapley value: the marginal contribution of feature *i* averaged over all possible orderings of features joining the coalition

For feature *i* and a specific input *x*:

```
φ_i = Σ_{S ⊆ F\{i}}  [|S|!(|F|-|S|-1)! / |F|!] · [ν(S ∪ {i}) - ν(S)]
```

The weighted sum of marginal contributions across all coalitions gives each feature's "credit" for the prediction. The sum of all SHAP values equals the difference between the model's output for *x* and the expected output over the background dataset — a useful **conservation property** for debugging.

## Why SHAP, Not Just Shapley Values

Classical Shapley values were defined for cooperative games in 1953. SHAP's contribution is making them *computationally tractable* for ML models. Direct computation requires evaluating 2^|F| coalitions, which is infeasible for high-dimensional inputs. SHAP introduced **KernelSHAP** (model-agnostic, kernel-approximated) and connections to existing methods that turned out to be Shapley estimators under specific assumptions (LIME, DeepLIFT, LRP, classic Shapley sampling, TreeSHAP).

The framework unification matters because:

1. **Theoretical grounding** — every previously heuristic method can be classified as approximating a specific variant of Shapley values
2. **Algorithm choice** — practitioners can pick the variant whose assumptions match their model class
3. **Local + global views** — aggregating SHAP values over a dataset yields global feature importance, partial dependence, and interaction effects from the same local explanations

## Algorithm Variants

| Variant | Model class | Tractability | Notes |
|---------|-------------|--------------|-------|
| **KernelSHAP** | Model-agnostic | O(2^M·M) sample complexity; weighted regression approximation | Slow for many features; inspired by LIME |
| **TreeSHAP** | Tree ensembles (XGBoost, LightGBM, RF) | Polynomial in trees and features — exact | Lundberg et al. 2018; orders-of-magnitude faster than KernelSHAP for trees |
| **DeepSHAP** | Neural networks | Backprop-style composition of Shapley values | Efficient for deep nets; equivalent to DeepLIFT under certain assumptions |
| **GradientSHAP** | Differentiable models | Uses gradients w.r.t. inputs | Fast but approximate; sensitive to baseline choice |
| **LinearSHAP** | Linear models | Closed form | Reduces to standard coefficient × (input − baseline) |
| **SamplingSHAP** | Model-agnostic | Monte Carlo over permutations | Permutation-based; unbiased but noisy |
| **ProxySHAP** (2026) | Model-agnostic via tree proxy | Polynomial in features | New polynomial-time SOTA — see [[proxy-based-shapley-banzhaf-2026]] |

The variant choice is consequential. TreeSHAP's polynomial-time exactness for tree models was the practical breakthrough that made SHAP deployable at scale (billions of trees, sub-second explanations). ProxySHAP (2026) extends exactness to non-tree models via a tree-based proxy + residual correction.

## Connections to Adjacent Concepts

### Feature Importance vs Feature Attribution

**Global feature importance** (permutation importance, gain-based) tells you which features matter *on average*. **Feature attribution** (SHAP, LIME, integrated gradients) tells you *why* a specific prediction was made. SHAP bridges both: per-instance SHAP values averaged over a dataset recover a global importance ranking, but you can also drill down to any single row.

### SHAP and Model Trustworthiness

The connection to behavioral credibility ([[behavioral-credibility-trilemma]]) is direct: a model whose reasoning cannot be inspected cannot be calibrated or audited. SHAP provides per-prediction audit trails — for regulated domains (medicine, finance, criminal justice), SHAP values are increasingly required as part of model documentation under EU AI Act provisions on transparency.

### SHAP and Foundation Models

For tabular foundation models like [[tabpfn]], SHAP is a first-class extension — TabPFN ships built-in SHAP-based explanations. For LLMs and VLMs, SHAP has been adapted for **token attribution**: which tokens in a prompt drove the output? The ProxySHAP 2026 paper demonstrates this on SigLIP-2 (vision-language model) for token interaction estimation — opening SHAP to multimodal models where feature attribution was previously computationally prohibitive.

## Practical Considerations

### Baseline / Background Dataset Choice

SHAP values are defined *relative to* a background dataset ν(S) — the expected model output when only features S are present and the rest are drawn from a background distribution. Choice of background matters:

- **Training data mean** — standard, but can mask rare-but-decisive features
- **K-means centroids** — Lundberg's recommended approach for compact representation
- **Single reference point** — fast, but loses the distributional view

A SHAP explanation without a stated background is not reproducible.

### Computational Cost at Production Scale

- **TreeSHAP** scales to millions of trees (XGBoost on credit scoring, fraud detection)
- **KernelSHAP** is slow; budget 1k-10k samples for moderate feature counts
- **SamplingSHAP** is the only tractable option for non-differentiable, non-tree models at high feature count — and even then, variance is the bottleneck
- **ProxySHAP** (2026) targets this last regime with polynomial-time approximations

### Adversarial Robustness

SHAP explanations can be **manipulated**: an adversary who controls a model's gradients can produce models that are accurate but whose SHAP attributions point to spurious features (Slack et al. 2020, "Fooling LIME and SHAP"). The axiom-grounded guarantee is for *unmanipulated* models. SHAP attributions are not a defense against adversarial models — they are a tool for inspecting honest models.

## Connections

- [[shapley-values]] — the theoretical foundation (game theory credit allocation); SHAP is the ML-specific instantiation
- [[maximum-occupancy-principle]] — MOP integration: SHAP-based feature attribution can guide LLM agent memory writes (decide what to commit to long-term memory)
- [[tabpfn]] — repository entity; TabPFN uses SHAP-based explanations as a built-in extension
- [[sources/papers/proxy-based-shapley-banzhaf-2026]] — 2026 paper extending SHAP to polynomial-time interaction estimation
- [[behavioral-credibility-trilemma]] — calibration/autonomy/helpfulness tension; SHAP is a transparency tool
- [[llm-agent-architecture]] — agent-level use of SHAP for tool selection attribution
- [[model-interpretation]] — broader concept: SHAP is the dominant instance

## See Also

- [[shapley-values]] — game-theoretic parent concept
- [[model-interpretation]] — the broader field
- [[explainable-ai]] — XAI as a discipline
- [[tabpfn]] — SHAP-shipped tabular foundation model
- [[feature-importance]] — simpler global alternative

## Open Questions

- **Causal SHAP**: do SHAP attributions recover causal effects? Generally no — SHAP measures *predictive contribution*, not causal contribution. Bridging the two is an active research area.
- **SHAP for retrieval/RAG**: can SHAP attribute a generated answer to specific retrieved documents? Document-level SHAP would be valuable for citation faithfulness, but the combinatorial space of document subsets is a barrier.
- **SHAP faithfulness under distribution shift**: does a SHAP explanation computed on training data remain valid under deployment distribution shift? Likely degrades, but quantification is open.
- **Multimodal SHAP**: ProxySHAP's 2026 demonstration on VLMs is promising but early — token-level attribution for image+text inputs is under-explored.

## Confidence Caveats

- Confidence 0.72 reflects solid axiomatic grounding (Lundberg & Lee 2017 is widely accepted) but active development in tractability variants and adversarial robustness. The 2026 ProxySHAP result is recent and not yet widely replicated.
- Production deployment claims (e.g., "SHAP required by EU AI Act") are accurate at the time of writing but jurisdictional.
