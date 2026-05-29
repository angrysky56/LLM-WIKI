---
summary: Training-free inference-time reasoning via MCMC power sampling, matches RL without training
tags: [inference-time-compute, MCMC, power-sampling, reasoning, base-model, reinforcement-learning-alternative]
updated: 2026-05-29T17:57:15Z
created: 2026-05-29T17:57:15Z
---

---
created: 2026-05-29
updated: 2026-05-29
type: source
summary: "Training-free inference-time reasoning via Metropolis-Hasticks MCMC sampling from power distributions — matches RL performance without training, verifier, or curated data."
tags: [inference-time-compute, MCMC, power-sampling, reasoning, base-model, reinforcement-learning-alternative]
sources: https://aakaran.github.io/reasoning_with_sampling/
status: active
confidence: 0.95
---

# Reasoning with Sampling: Your Base Model is Smarter Than You Think

**Authors**: Aayush Karan, Yilun Du  
**Year**: 2025  
**Source**: [arXiv / Project Page](https://aakaran.github.io/reasoning_with_sampling/)

## Core Finding

Base models already contain reasoning capabilities comparable to RL-posttraining — but standard sampling methods (greedy, temperature sampling) fail to elicit them. **Power sampling** — an MCMC-based iterative sampling algorithm — boosts base model reasoning to near-RL levels without any training, verifier, or curated dataset.

## Key Ideas

### Power Distributions

RL post-training shifts model outputs toward high-likelihood, high-confidence regions of the base model distribution — effectively "sharpening" the distribution. Rather than training to achieve this, power sampling directly samples from the **power distribution** $p^\alpha$ (exponentiated base model probabilities), which naturally upweights high-likelihood sequences.

Unlike simple temperature scaling, power distributions account for **future path likelihoods** — tokens with fewer but higher-probability completions are preferred. This avoids "critical windows" or "pivotal tokens" that trap outputs in low-likelihood futures.

### Autoregressive MCMC Sampling

Directly sampling from $p^\alpha$ is intractable (requires normalizing over exponential sequence space). The paper uses **Metropolis-Hastings MCMC** to approximately sample from $p^\alpha$ block-by-block:

1. Start with a draft output from the base model
2. Iteratively propose modifications and accept based on $p^\alpha$ weights
3. Build output block-by-block to avoid dimensionality explosion

The number of MCMC iterations ($N_{\text{MCMC}}$) serves as a **test-time compute scaling** knob — more iterations push output closer to true $p^\alpha$ sample and improve reasoning performance.

### Results

| Benchmark | Base Model | GRPO (RL) | Power Sampling |
|-----------|-----------|-----------|----------------|
| MATH500 (in-domain) | baseline | GRPO | close to GRPO |
| HumanEval (OOD) | baseline | GRPO | outperforms GRPO |
| AlpacaEval 2.0 (non-verifiable) | baseline | GRPO | outperforms GRPO |

**Key advantage**: Unlike GRPO, power sampling **maintains diversity** on pass@k — GRPO collapses diversity (deteriorated multi-sample performance), while power sampling universally outperforms both GRPO and the base model for $k > 1$.

### Inference Cost

On MATH500 with experimental parameters: ~**8.84×** token multiplier vs standard inference (roughly equivalent to 1 epoch of GRPO with 8 rollouts on identically-sized dataset).

## Connections

- [[inference-time-compute-scaling]] — test-time compute as scaling axis; power sampling provides a training-free approach
- [[entropy-cut-mh-reasoning-2026]] — related MCMC-based reasoning approach (entropy-based decision point cutting vs. full power sampling)
- [[parallel-reasoning]] — inference-time reasoning strategies; power sampling is a training-free alternative to parallel sampling
- [[llm-reasoning]] — power sampling demonstrates base models have latent reasoning capabilities not revealed by standard sampling
- [[group-relative-policy-optimization]] — GRPO as the RL baseline power sampling compares against; shows training-free can match trained

## Caveats

- $\alpha$ (power exponent) is a hyperparameter requiring tuning
- $N_{\text{MCMC}}$ iterations add inference cost — practical but not free
- MCMC acceptance ratios depend on proposal distribution quality
