---
created: 2026-06-04
updated: 2026-06-04
type: concept
summary: "Coverage — 'at least one model gets it right' rate measuring complementary capability of a model population."
tags: [evaluation-metrics, multi-model-systems, llm]
sources: []
status: reference
confidence: 0.9
---

# Coverage Metric

The central evaluation metric in [[wiki/sources/papers/acdc-llm-task-capability-coevolution-sakana|AC/DC]]. For Q questions and N models:

$$\\text{Coverage} = \\frac{1}{Q} \\sum_{q=1}^{Q} \\left( \\bigvee_{i=1}^{N}(x_{q,i}=y_q) \\right)$$

The "at least one model gets it right" rate across the population — captures *complementary* capability better than per-model accuracy. A model collective covering a diverse range of questions has high coverage even if no individual model is best on every question.

## Why it matters

Standard evaluation (per-model accuracy) rewards jack-of-all-trades models. Coverage rewards collectives where different models excel on different questions — the core insight of collective intelligence applied to model selection.

## Connections

- [[wiki/sources/papers/acdc-llm-task-capability-coevolution-sakana]] — source paper
- [[concepts/quality-diversity]] — Coverage is the fitness function in DNS selection