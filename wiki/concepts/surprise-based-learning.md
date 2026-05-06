---
summary: Concept page for surprise-based learning.
tags: [machine-learning, learning-theory]
updated: 2026-05-06T20:09:39Z
created: 2026-05-06T20:09:39Z
---

---
created: 2026-05-06T20:09:35Z
updated: 2026-05-06T20:09:35Z
type: concept
summary: A learning paradigm where the model prioritizes information storage or weight updates based on the "surprise" value (prediction error or gradient magnitude).
tags: [machine-learning, learning-theory, titans]
sources: [[titans-test-time-memory]]
status: active
confidence: 1.0
---

# Surprise-Based Learning

Surprise-based learning is a cognitive-inspired mechanism where a system's learning rate or memory allocation is modulated by how "surprising" an input is. In neural networks, surprise is often quantified as the magnitude of the gradient $\nabla L$ or the loss of a local prediction task.

## Application in [[titans|Titans]]
The Titans architecture uses surprise to determine which parts of an input sequence should be committed to its **[[neural-long-term-memory]]**. This prevents memory saturation by ignoring predictable, low-information tokens and focusing on novel data.

## Theoretical Basis
- **Entropy**: High-entropy tokens are often more "surprising" and carry more information.
- **Predictive Coding**: The brain updates its internal models primarily when sensory input deviates from expectations.

## Connections
- Concept: [[neural-long-term-memory]]
- Source: [[titans-test-time-memory]]
- Source: [[shorthand-for-thought]] (Entropy-guided)
