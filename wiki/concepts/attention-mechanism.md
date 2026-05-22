---
created: 2026-05-29
updated: 2026-05-29
type: concept
summary: Attention mechanism — key-value lookup pattern at the core of transformer architectures
tags: [transformers, deep-learning, architecture]
sources: 
status: stub
confidence: 0.3
---

# Attention Mechanism

The attention mechanism allows models to weigh the importance of different parts of the input when producing output. The core formulation (scaled dot-product attention):

```
Attention(Q, K, V) = softmax(QK^T / √d) · V
```

Where Q (query), K (keys), and V (values) are projections of the input.

Variants include:
- **Multi-head attention** — parallel attention layers with different projections
- **Cross-attention** — attention from one sequence to another
- **Flash attention** — memory-efficient exact attention

## Connections

- [[transformer-architecture]] — built on attention mechanisms
- [[kv-cache]] — cache of key-value vectors for efficient inference
- [[hidden-states]] — intermediate representations in attention
- [[ml-evolution]] — transformers as a major milestone
