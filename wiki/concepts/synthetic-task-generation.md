---
created: 2026-06-04
updated: 2026-06-04
type: concept
summary: "Synthetic task generation — using LLMs (scientist-LLM pattern) to generate evaluation tasks from parent tasks + reference tasks + adaptation hints."
tags: [llm-generated-benchmarks, task-generation, evaluation]
sources: []
status: reference
confidence: 0.85
---

# Synthetic Task Generation

Using LLMs to generate evaluation tasks as an alternative to human-annotated datasets. In the AC/DC setting, a *scientist LLM* takes a parent task + 3 reference tasks + an adaptation hint (harder / easier / novel) and generates a candidate task. The task then goes through novelty filtering (cosine similarity + judge LLM) and reflection (scientist LLM attempts its own task, fixes errors).

## Key properties

- **Correctness**: 97.8% of synthetic tasks are correct (human evaluated, n=47)
- **OOD rate**: 68.9% of synthetic tasks are out-of-distribution vs. standard benchmarks
- **Creativity**: 37.8% of synthetic tasks are judged creative

## Applications

- FunSearch (prior work) — evolved mathematical programs via LLM-generated tasks
- AC/DC — coevolution of synthetic task population with model population
- General benchmark construction for domains with scarce labeled data

## Connections

- [[wiki/sources/papers/acdc-llm-task-capability-coevolution-sakana]] — the reference application
- [[concepts/open-endedness]] — continuous synthetic task discovery is an OE mechanism