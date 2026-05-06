---
summary: Tool page for Mamba (SSM).
tags: [llm, ssm, architecture]
updated: 2026-05-06T20:09:35Z
created: 2026-05-06T20:09:35Z
---

---
created: 2026-05-06T20:09:30Z
updated: 2026-05-06T20:09:30Z
type: entity
summary: A state-space model (SSM) architecture for sequence modeling that offers linear scaling with sequence length.
tags: [llm, ssm, architecture, machine-learning]
sources: [Gu & Dao 2023]
status: active
confidence: 1.0
---

# Mamba

Mamba is a structured state-space model (SSM) designed to compete with Transformers. It utilizes selective scan mechanisms to achieve linear scaling, making it highly efficient for processing long sequences.

## Features
- **Linear Scaling**: Unlike the quadratic complexity of standard self-attention.
- **Selective State Update**: Allows the model to filter irrelevant information.
- **Performance**: Comparable to Transformers on many benchmarks while being significantly faster for long contexts.

## Comparisons
- **[[titans]]**: Titans builds on the efficiency of models like Mamba but adds a neural long-term memory module to improve performance on million-token contexts.

## Connections
- Concept: [[neural-long-term-memory]]
- Source: [[titans-test-time-memory]]
