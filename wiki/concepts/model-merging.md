---
created: 2026-06-04
updated: 2026-06-04
type: concept
summary: "Model merging — techniques for combining two or more LLM checkpoints into a single model, including weight averaging, task-vector interpolation, and evolutionary approaches."
tags: [model-merging, llm, weight-merging, ensemble]
sources: []
status: stub
confidence: 0.8
---

# Model Merging

Techniques for combining two or more LLM checkpoints into a single model. Forms include:
- **Weight averaging** — simple interpolation of model weights (e.g., model soup)
- **Task-vector interpolation** — τ = θ_model − θ_base; merging models via τ-space operations
- **Evolutionary model merging** — crossover and mutation in weight space (EvoMerge, AC/DC)

## Evolutionary vs. naive merging

Naive averaging produces a model that may be worse than both parents on all tasks (the "mode collapse" problem). Evolutionary approaches use selection pressure to maintain diversity and quality across the merged population.

## Connections

- [[concepts/evolutionary-model-merging]] — evolutionary approach to model merging
- [[wiki/sources/papers/acdc-llm-task-capability-coevolution-sakana]] — uses evolutionary merging