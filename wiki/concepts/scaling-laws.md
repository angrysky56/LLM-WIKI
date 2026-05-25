---
created: 2026-05-29
updated: 2026-05-29
type: concept
summary: Empirical power-law relationships between neural network performance and model/data/compute scale — Kaplan/Chinchilla laws, emergent capabilities, and modern inference-time compute scaling
tags: [scaling, neural-networks, empirical, power-law, training-compute, inference-compute]
sources: https://arxiv.org/abs/2001.08361 (Kaplan et al.), https://arxiv.org/abs/2203.15556 (Chinchilla), https://arxiv.org/abs/2202.05006 (emergent capabilities)
status: active
confidence: 0.85
---



# Scaling Laws

## Definition

Scaling laws describe the empirical observation that neural network performance improves as predictably-shaped power-law functions of model size, dataset size, and compute budget. Rather than the smooth improvement intuition might suggest, loss decreases as a power law: `L ∝ N^(-α)` where N is model parameters and α is a task-dependent exponent.

The key empirical findings since 2020:

1. **Kaplan et al. (2020)** — Performance scales as power laws in model parameters, dataset size, and compute — with different exponents. Larger models are more sample-efficient (need fewer training tokens per parameter to reach a given loss).

2. **Chinchilla (Hoffmann et al., 2022)** — The Kaplan findings underinvested in data. For a fixed compute budget, the optimal allocation is roughly 1 token per parameter per epoch — meaning bigger models need proportionally more data. This reframed scaling as "train smaller models on more data" rather than "just make models bigger."

3. **Emergent capabilities (Wei et al., 2022)** — Some abilities appear suddenly at scale thresholds rather than improving gradually. Chain-of-thought reasoning, few-shot learning, and multi-step arithmetic emerge around 10B–100B parameters. This isn't a smooth improvement curve — it's a phase transition.

## Why It Matters

Scaling laws are the closest thing the field has to a "theory of everything" for language models. They let researchers:

- **Predict performance** before training: if you know your compute budget and model size, you can estimate final loss within a narrow band.
- **Allocate compute efficiently**: Chinchilla showed you shouldn't just scale model size — data matters equally.
- **Forecast capability thresholds**: if emergence follows predictable patterns, you can anticipate what the next scale threshold unlocks.

The practical implication: if you want a capability that currently only emerges at 100B parameters, you either need a 100B model or you need to find a way to unlock that capability at smaller scale (e.g., inference-time compute, better architectures, or better training signals).

## The Power-Law Form

For a training run with compute budget C, model parameters N, and training tokens D:

```
L(N, D, C) ≈ L₀ + N^(-α_N) + D^(-α_D) + C^(-α_C)
```

The exponents differ by task:
- **Next-token prediction loss**: α ≈ 0.05–0.1 for N (very slow improvement)
- **Downstream tasks**: α varies — some tasks scale sharply, others plateau early

This means not all capabilities improve equally with scale. Some hit ceilings; others keep improving.

## Emergent Capabilities

The emergence phenomenon complicates the smooth-power-law narrative:

| Capability | Emergence threshold |
|
|
-|
| Few-shot learning | ~1B parameters |
| Chain-of-thought | ~10B parameters |
| Multi-step arithmetic | ~10B–100B |
| Code generation | ~10B+ |
| Multi-hop reasoning | ~100B+ |

Emergence appears sharp because we measure capabilities at discrete thresholds — the underlying distribution of capabilities may be smoother, just with very steep slopes at certain scales.

The key unresolved question: are emergent capabilities genuinely phase transitions in the model behavior, or artifacts of our evaluation metrics (which often use discrete right/wrong thresholds)?

## Compute-Optimal Training vs. Inference-Time Scaling

Scaling laws operate at two distinct axes:

**Axis 1 — Training compute**: How much compute to spend training the model. Kaplan → Chinchilla shifted the recommendation from "bigger models" to "bigger models + proportionally more data."

**Axis 2 — Inference compute**: How much compute to spend per token at inference time. This became the frontier around 2024–2025 with BoN sampling, process reward models, and beam search over reasoning traces.

The interaction between axes matters: a smaller model trained on more compute-efficient data may match a larger model's quality at lower training cost, but might require more inference-time compute to achieve the same output quality on hard tasks.

See [[inference-time-compute-scaling]] for the inference-time axis.

## Connections

- [[inference-time-compute-scaling]] — the second axis of scaling beyond training compute
- [[emergence]] — emergent capabilities at scale thresholds; phase transitions in capability landscapes
- [[power-law-scaling]] — the mathematical form that scaling relationships take
- [[power-law]] — the underlying statistical distribution; why power laws govern these relationships
- [[mixture-of-experts]] — conditional computation as a way to get more effective parameters without proportional compute
- **Chinchilla** (Hoffmann et al. 2022) — the specific paper that reframed optimal compute allocation; see [[scaling-laws]] body for details
- Concept: [[adaptive-budget-learning]]
- Concept: [[adaptive-computation]]
- Concept: [[allometric-scaling]]
- Concept: [[attention-mechanism]]
- Concept: [[benchmark]]
- Concept: [[catastrophic-forgetting]]
- Concept: [[efficient-transformers]]
- Concept: [[evaluation]]
- Concept: [[evolutionary-strategies]]
- Concept: [[in-context-learning]]
- Concept: [[initialization]]
- Concept: [[mathematical-reasoning]]
- Concept: [[mixture-of-depths]]
- Concept: [[taylors-law]]
- Concept: [[transformer-architecture]]


## Open Questions

1. **Predicting emergence**: Can we predict which capabilities will emerge at which scale thresholds, before running the experiments? Currently empirical — no theory.

2. **Abridged scaling**: Can we get emergent capabilities at smaller scale through better training signals (RL, process supervision), better architectures, or inference-time tricks? This is the central practical question behind most scaling research today.

3. **Scaling vs. efficiency**: What is the efficiency frontier — how much compute per capability can we squeeze out? Is there a fundamental limit or can efficiency keep improving?

4. **Inflection points**: Are there scale regimes where scaling *stops* working? Evidence suggests certain capabilities plateau while others continue — suggesting different underlying mechanisms.

## Limitations

- **Task dependency**: Scaling exponents vary enormously across tasks. Loss curves are smooth but downstream capability emergence is not.
- **Data quality ceiling**: Chinchilla showed data scale matters — but data quality (web text vs. curated data) may matter more. Poor quality data saturates the scaling curve.
- **Diminishing returns at frontier**: At GPT-4/Claude-3 level performance on many benchmarks, further training scaling yields marginal gains. This drove the shift to inference-time compute as the next frontier.
