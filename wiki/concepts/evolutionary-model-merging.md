---
created: 2026-06-04
updated: 2026-06-04
type: concept
summary: "Evolutionary model merging — evolutionary algorithms applied to LLM weight merging, combining task vectors via crossover and SVD-based mutation."
tags: [model-merging, evolutionary-algorithms, llm, weight-merging]
sources: []
status: reference
confidence: 0.9
---

# Evolutionary Model Merging

Applying evolutionary algorithms to the problem of merging LLM weights. Given a population of models, evolutionary model merging uses crossover (interpolating task vectors τ = θ_model − θ_base) and mutation (SVD-based perturbations of weight matrices) to produce diverse model variants, then selects on a fitness function.

Key lineage:
- **EvoMerge** (Akiba et al.) — evolutionary merging with CMA-ES
- **CycleQD (CQD)** — task-vector crossover in QD setting; predecessor to AC/DC
- **AC/DC** — Sakana AI's application to LLM populations with DNS selection

## Mutation operator

For a weight matrix W = UΣV^T, mutation perturbs the top k singular values of Σ — modifying representational structure while preserving geometric relationships. This is the mutation used in AC/DC's model evolution phase.

## Connections

- [[wiki/sources/papers/acdc-llm-task-capability-coevolution-sakana]] — the reference application
- [[concepts/model-merging]] — broader category; evolutionary merging is one approach
- [[concepts/quality-diversity]] — DNS selection is used alongside evolutionary merging