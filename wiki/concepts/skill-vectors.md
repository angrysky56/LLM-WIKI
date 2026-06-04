---
created: 2026-06-04
updated: 2026-06-04
type: concept
summary: "Skill vectors — binary per-question pass/fail vectors serving as behavioral signatures of model capability profiles."
tags: [capability-representation, multi-model-systems, evaluation]
sources: []
status: reference
confidence: 0.85
---

# Skill Vectors

Binary per-question pass/fail vectors that serve as behavioral signatures of model capability profiles in [[wiki/sources/papers/acdc-llm-task-capability-coevolution-sakana|AC/DC]]. A skill vector for model i on question q is 1 if the model's answer is correct, 0 otherwise. Distances between skill vectors measure behavioral diversity in the model population.

Key design choices:
- **No predefined niches** — unlike MAP-Elites' explicit binning, DNS handles the partitioning implicitly
- **Binary format** — simple to compute, aligns with DNS novelty calculation
- **Behavioral, not architectural** — skill vectors describe what a model can do, not how it's built

## Why they matter

Skill vectors provide a formal basis for the "diverse task force" selection in AC/DC. By selecting models whose skill vectors are maximally diverse, the algorithm assembles a collective with high [[concepts/coverage-metric]] even when no single model is best on all questions.

## Connections

- [[wiki/sources/papers/acdc-llm-task-capability-coevolution-sakana]] — source paper
- [[concepts/quality-diversity]] — DNS selection operates on skill-vector space
- [[concepts/coverage-metric]] — the metric computed from skill vectors