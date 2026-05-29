---
created: 2026-05-26
updated: 2026-05-26
type: source
summary: "Shannon Scaling Law: LLM capacity follows noisy-channel dynamics — U-shaped degradation emerges when SNR collapses, with a finite Shannon capacity ceiling."
tags: [paper, scaling-laws, information-theory, uncertainty, model-capacity, shannon, efhf]
sources: https://arxiv.org/abs/2605.23901
status: active
confidence: high
---

# Shannon Scaling Law: A Noisy Channel Perspective on LLM Capacity

**Paper:** [LLMs as Noisy Channels: A Shannon Perspective on Model Capacity and Scaling Laws](https://arxiv.org/abs/2605.23901)  
**arXiv:** `2605.23901` | **Published:** 2026-05-22 | **Authors:** Xu Ouyang, Deyi Liu, Yuhang Cai (ByteDance Seed, University of Virginia, UC Berkeley)

---

## Executive Summary

Existing monotonic power-law scaling laws fail to explain U-shaped performance degradation — catastrophic overtraining and quantization-induced degradation (QiD) — where performance deteriorates despite increased compute. This paper proposes the **Shannon Scaling Law**, which models LLM training as information transmission over a noisy channel using the Shannon-Hartley theorem. Model parameters map to channel bandwidth, training tokens to signal power, and noise arises from data, model architecture, and perturbations. The key insight is a **finite Shannon capacity** for LLMs: beyond a critical model-data combination, scaling without maintaining sufficient SNR amplifies noise and induces U-shaped degradation. The law accurately predicts loss basins, extrapolates to unseen model sizes (R²=0.847 on 12B/307B tokens from ≤6.9B/≤180B fits), and outperforms all baseline monotonic and perturbation-aware laws.

---

## Technical Approach

### Core Framework: Shannon-Hartley → LLM Capacity

The Shannon Scaling Law maps the Shannon-Hartley theorem (C = B log₂(1 + S/N)) to LLM training dynamics:

```
C_LLM = a·N^α · log₂(1 + b·D^β / (c·(DN)^γ + d·D^δ + e))
        bandwidth   signal         noise terms
```

Where:
- **N** (model parameters) → channel **bandwidth** (wider channel = more throughput)
- **D** (training tokens) → **signal power** (more data = stronger learning signal)  
- **Noise** has three components:
  - **Data-induced noise** (d·D^δ): typos, ambiguities, contradictions accumulate with data scale
  - **Model-interaction noise** (c·(DN)^γ): intrinsic model noise evolving over training trajectory
  - **Irreducible noise** (e): constant architectural limitations

The loss-capacity relationship is reciprocal: L = 1/C_LLM, satisfying:
1. As capacity → ∞, loss → 0
2. At high loss (early training), small capacity gains → large loss reductions
3. Near convergence, marginal loss reduction requires large capacity increases

### Critical Insight: The SNR Threshold

The U-shaped curve emerges when SNR collapses:
- **High-SNR regime**: Pretraining — perturbation factor negligible → monotonic improvement
- **Low-SNR regime**: Overtraining / quantization — noise term dominates → U-shaped degradation

This reconciles the apparent contradiction: monotonic pretraining curves are a **special case** of the U-shaped phenomenon (high SNR where perturbation is negligible).

### Experiments

- **Pythia suite** (160M–12B, ≤307B tokens) and **OLMo2** under Gaussian noise, quantization (3-bit, 4-bit, 8-bit), and SFT on math/QA/code
- Shannon law **outperforms all baselines** in all perturbation scenarios
- **Extrapolation test**: Fit on ≤6.9B / ≤180B tokens → predict unseen 12B / 307B tokens at **pooled R²=0.847**; monotonic baselines (OpenAI, Chinchilla) collapse to negative R²

---

## Key Results

| Setting | Shannon Law | Chinchilla | OpenAI |
|---------|-------------|------------|--------|
| Fit R² (Pythia, all perturbations) | **Best** | Poor | Poor |
| Extrapolation R² (12B, 307B tokens) | **0.847** | negative | negative |
| QiD prediction | ✅ U-shaped | ❌ monotonic | ❌ monotonic |

---

## Relevance to EFHF/Wiki Research Threads

**[[efhf]]**: The Shannon capacity ceiling directly maps to EFHF's boundedness concern. Just as the Shannon-Hartley theorem sets a hard capacity limit for any communication channel, the Shannon Scaling Law reveals that LLMs have a finite representational capacity that cannot be exceeded by naive scaling — only by improving SNR. This provides a theoretical foundation for EFHF's claim that agentic systems need structured representation layers rather than unbounded weight expansion.

**[[verifier-graph]]**: Verification at inference time is analogous to receiver-side error correction in a noisy channel. The verifier-graph must operate within the SNR budget established by the Shannon capacity — if the verifier's confidence scores don't track actual reliability, the system is operating below the capacity bound and will produce overconfident failures. The paper's SNR analysis (signal / noise) maps to the verifier's reliability ratio.

**[[maximum-occupancy-principle]]**: MOP's "maximum occupancy" of semantic space has an analog in information theory: channel capacity is maximized at optimal SNR. Beyond the optimal operating point, increasing bandwidth (model size) without improving SNR decreases effective capacity — a precise formalization of MOP's saturation intuition.

**[[mop-explorer]]**: The MOP explorer's bounded exploration strategy parallels the paper's finding that effective capacity is noise-limited. Agents that don't account for capacity collapse (SNR degradation) will exploration-explode their state space without corresponding gains.

> *"We posit that the strictly monotonic loss curves observed in standard pretraining represent a special case of the U-shaped phenomenon — specifically, a high-SNR regime where the perturbation factor is negligible."*

---

## Key Quotes

> *"The Shannon Scaling Law consistently outperforms classical scaling laws and recent perturbation-aware laws, achieving strong R² scores and accurately capturing loss basins missed by prior approaches."*

> *"Scaling model size or data without preserving a sufficient signal-to-noise ratio (SNR) inevitably amplifies noise, inducing a transition from monotonic improvement to U-shaped performance degradation."*

> *"By mapping model parameters to channel bandwidth and training tokens to signal power, our formulation explicitly captures the interaction between learning signal and intrinsic noise."*

---

## Related
- [[sources/papers/shannon-scaling-law-2026]]
- [[wiki/index]]

- [[shannon-scaling-law-2026]]

## Structural Insights

1. **The "structure → tractable exact solution" pattern is general**: ProxySHAP used tree structure to get polynomial-time exact Shapley values; this paper uses channel structure (bandwidth/signal/noise decomposition) to get a unified scaling law that subsumes both monotonic and U-shaped regimes. Both papers exploit structure that prior approaches ignored.

2. **The reciprocity principle (L = 1/C_LLM) is a design constraint**: For agentic systems, this suggests the loss function should be formulated in terms of inverse capacity — not just raw perplexity. Verifiers that don't track this reciprocal relationship will have miscalibrated confidence at high-entropy boundaries.

3. **SNR as the fundamental variable, not compute or parameters**: The paper shows that SNR, not parameter count or token count in isolation, determines capacity. This reframes the scaling debate: the question isn't "how big?" but "how high-SNR?"