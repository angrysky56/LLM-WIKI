---
created: 2026-05-29
updated: 2026-05-29
type: concept
summary: Sudden appearance ofCapabilities at scale thresholds — phase transitions in LLM capability landscapes, distinct from smooth power-law improvement
tags: [emergence, scaling, capability, phase-transition, llm]
sources: https://arxiv.org/abs/2202.05006 (Wei et al. emergent capabilities)
status: active
confidence: 0.8
---




# Emergence

## Definition

Emergence, in the context of large language models, refers to the sudden appearance of capabilities at certain scale thresholds — abilities that are absent or weak in smaller models and then become measurably present at larger scales, without having been explicitly trained for them.

The canonical definition from Wei et al. (2022): a capability is emergent if "models trained with a small number of parameters do not show the capability, but models trained with a larger number of parameters do show it." The key property is non-linearity: the capability doesn't improve gradually as you scale — it appears discontinuously when you cross a threshold.

This is distinct from smooth power-law improvement, where capability improves predictably with scale in a continuous way.

## Why It Matters

Emergence matters because it means capability forecasting isn't just an extrapolation problem — there are genuine surprises at scale. If a capability emerges at 100B parameters, you can't discover it by studying 1B or 10B models. This has several practical implications:

1. **Surprise detection**: Researchers didn't predict that chain-of-thought reasoning would emerge around 10B parameters — it was discovered empirically. This suggests many capabilities may be lurking undiscovered at frontier scales.

2. **Capability gap remediation**: If a capability only exists at 100B but you need it at 10B, you need a different approach (better training signals, architectures, inference-time tricks). Emergence tells you that scale alone won't close certain gaps.

3. **Safety implications**: Emergent capabilities could include things we didn't design for — including deceptive behavior, hidden reasoning patterns, or goal-directed behavior at certain scales.

4. **Evaluation challenge**: If capabilities appear suddenly, evaluating only at certain scale points misses the emergence threshold. You need fine-grained scale sampling to detect when capabilities turn on.

## The Emergence-vs.-Smooth-Improvement Debate

There's genuine scientific dispute about whether emergence is real or an artifact of evaluation methods:

**The "real emergence" view** (Wei et al., 2022):
- Capabilities appear discontinuously at scale thresholds
- The sharp right/wrong evaluation metrics reveal phase transitions that continuous metrics miss
- The underlying mechanism is a genuine regime shift in what the model can represent

**The "smooth but steep" view** (Schaeffer et al., 2023):
- Many apparent emergent capabilities are artifacts of discontinuous evaluation metrics
- When you use continuous metrics (e.g., per-token accuracy instead of exact-match), the apparent phase transitions become smooth (though still steep) curves
- The underlying improvement is continuous; our metrics make it look discontinuous

The actual answer is likely: some capabilities genuinely emerge (phase transitions in representation capacity), while others appear to emerge due to metric choice. Distinguishing which is which is an open research question.

## Known Emergence Thresholds

| Capability | Approximate threshold | Evidence quality |
|
|
-|
--|
| Few-shot learning | ~1B parameters | Strong |
| Chain-of-thought reasoning | ~10B parameters | Strong |
| Multi-step arithmetic | ~10B–100B | Moderate |
| Code generation | ~10B+ | Strong |
| Multi-hop reasoning | ~100B+ | Moderate |
| Self-correction | ~50B+ | Weak/emerging |

Note: these thresholds are model-dependent. The same capability might emerge at 7B in one architecture and 50B in another. Architecture, training data quality, and training objectives all shift emergence thresholds.

## Relationship to Scaling Laws

Emergence lives in tension with the smooth power-law predictions of scaling laws:

- **Scaling laws** describe aggregate performance on continuous metrics (loss, perplexity) — these are smooth.
- **Emergence** describes capability appearance on discrete metrics — these can be sharp.

This apparent contradiction resolves when you consider that:
1. Underlying loss improvements may be smooth, but capability thresholds (exact-match accuracy) depend on crossing a loss threshold, which can be sharp.
2. The same smooth loss curve can produce very different emergence behavior depending on task structure.

See [[scaling-laws]] for the power-law framework that governs the smooth aspects of scale-dependent performance.

## Connections
- [[concepts/in-context-learning]]
- [[concepts/wolfram-nks-causal-networks]]
- [[concepts/dynamical-systems]]
- [[concepts/chain-of-thought]]
- [[concepts/computational-irreducibility]]
- [[agents/skills/researcher-agent/references/gap-discovery-patterns]]
- [[concepts/attractor-dynamics]]
- [[agents/skills/researcher-agent/skill]]
- [[log]]
- [[concepts/emergence]]
- [[concepts/complexity]]
- [[concepts/power-law-scaling]]
- [[index]]
- [[concepts/imagination]]
- [[concepts/open-ended-evolution]]
- [[sources/papers/critical-initialization-biological-neural-networks]]
- [[concepts/scaling-laws]]
- [[concepts/openpraparat]]
- [[concepts/creativity]]
- [[emergence]]

- [[scaling-laws]] — the power-law framework; smooth scale-performance relationships that underlie emergent capability thresholds
- [[computational-irreducibility]] — why some systems can't be predicted without explicit simulation; related to why emergence surprises us
- [[open-ended-evolution]] — emergence in biological/computational systems; related but different domain
- [[chain-of-thought]] — an emergent capability that appears at ~10B parameters; the reasoning trace is what emerges
- [[in-context-learning]] — few-shot learning emerges at small scales (~1B); a well-studied emergence case
- Concept: [[complexity]]
- Concept: [[critical-initialization-biological-neural-networks]]
- Concept: [[openpraparat]]
- Concept: [[power-law-scaling]]


- [[imagination]]
- [[dynamical-systems]]
- [[attractor-dynamics]]
- [[creativity]]
## Open Questions

1. **Which emergence is real?**: Distinguishing genuine phase transitions from metric artifacts requires continuous-metric evaluations across scale — expensive and rarely done systematically.

2. **Can we predict emergence thresholds?**: Without a theory of which capabilities will emerge at which scales, we're stuck with empirical scaling runs. Is there a structural predictor?

3. **Abridging emergence**: If we know a capability's emergence threshold, can we abridge it — get the capability at smaller scale through better architecture, training signals, or inference-time methods? Self-correction techniques suggest yes for some capabilities.

4. **Negative emergence**: Are there capabilities that degrade at scale, or emerge as failure modes rather than success modes? Early evidence suggests some capabilities (e.g., certain biases) strengthen with scale while others weaken.

## Limitations

- **Metric dependency**: How you measure matters enormously. Discontinuous metrics create the appearance of emergence even when underlying capability changes smoothly.
- **Model specificity**: Emergence thresholds are not universal — they're specific to architecture, training data, and training objectives.
- **Limited sample**: We only have a few documented emergence cases because running across scales is expensive. The true prevalence of emergence vs. smooth improvement is unknown.