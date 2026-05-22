---
created: 2026-05-29
updated: 2026-05-29
type: concept
summary: Transformer architecture — dominant neural network architecture based on self-attention
tags: [transformers, deep-learning, architecture]
sources: 
status: stub
confidence: 0.3
---

# Transformer Architecture

The transformer architecture, introduced in "Attention Is All You Need" (2017), uses self-attention mechanisms instead of recurrence. Key components:

- **Self-attention layers** — relate positions within the same sequence
- **Feed-forward layers** — position-wise MLPs between attention layers
- **Positional encodings** — inject position information since no recurrence
- **Layer normalization** — stabilize training
- **Residual connections** — enable deep networks

The decoder-only variant (GPT-style) is the basis for modern LLMs.

## Connections

- [[attention-mechanism]] — core component of transformers
- [[kv-cache]] — inference optimization for decoder-only transformers
- [[ml-evolution]] — transformers as a paradigm shift in deep learning
- [[hidden-states]] — intermediate representations
