---
created: 2026-05-29
updated: 2026-06-09
type: concept
summary: Decoder-only neural network architecture based on stacked self-attention layers — the foundation of modern large language models
tags: [transformers, deep-learning, architecture, llm]
sources: https://arxiv.org/abs/1706.03762
status: active
confidence: 0.9
---

# Transformer Architecture

**Source:** Vaswani et al., *Attention Is All You Need* (NeurIPS 2017)
**Confidence:** 0.9 — foundational architecture for modern LLMs

## What It Is

The transformer is a neural network architecture that processes sequences of tokens using stacked self-attention and feed-forward layers, without any recurrence. It was introduced to address the parallelism limitations of RNNs in sequence-to-sequence tasks.

The key innovation is that all tokens in a sequence attend to all other tokens (via self-attention), enabling direct long-range dependency modeling with O(1) path length between any two positions.

## Architecture Components

### Encoder (original)

The original transformer encoder processes the entire input sequence in parallel:
- **Input embedding + positional encoding** — Convert discrete tokens to continuous vectors, inject position information
- **N× stacked layers** — Each layer: multi-head self-attention → feed-forward network; both with residual connections and layer normalization
- **Output** — Contextualized representations for each position

### Decoder (original)

Autoregressive decoder with two modifications:
1. **Masked self-attention** — Causal masking prevents attending to future positions (preserves autoregressive property)
2. **Cross-attention** — Attend to encoder output for sequence-to-sequence tasks (e.g., translation)

### Decoder-Only (GPT-style)

Modern LLMs use a decoder-only architecture. The key difference:
- No encoder cross-attention — no separate encoder to attend to
- Single stack of layers with masked self-attention
- Directly predicts next token given all prior tokens

The decoder-only variant simplified the architecture and enabled pretraining at massive scale (predict next token) then fine-tuning for diverse downstream tasks.

## Why It Matters

The transformer enabled a qualitative shift in what neural networks can do:

| Property | RNN/LSTM | Transformer |
|----------|----------|-------------|
| Path length | O(n) | O(1) |
| Parallelism | Sequential | Full parallel |
| Max context | Limited by gradient flow | Limited by memory (√d scaling) |
| Content dependence | Position-fixed | Learned similarity |

The O(1) path length means information from the beginning of a sequence can influence the representation at the end without degradation. This enabled effective long-range reasoning in language, code, and biological sequences.

## Scaling as Primary Strategy

The transformer architecture scaled well — bigger models and more data consistently improved performance. This made scaling the primary research strategy from GPT-2 (2019) through GPT-4, Claude, Gemini, and beyond.

The relationship to [[scaling-laws]]: the transformer architecture is what made the scaling laws observable. Kaplan et al. (2020) characterized scaling behavior specifically for transformers.

## Key Variants and Extensions

| Extension | Description | Motivation |
|-----------|------------|------------|
| **RoPE (Rotary Position Embedding)** | Rotary encoding of position in Q/K attention | Better length generalization than absolute positional encoding |
| **ALiBi (Attention with Linear Biases)** | Linear bias instead of positional embeddings | Similar length generalization benefits |
| **Grouped Query Attention** | Shared KV across query groups | Reduce KV cache size for long context |
| **Sliding Window Attention** | Fixed context window per head | Trade long-range for efficiency; some heads still attend globally |
| **Mixture of Experts** | Sparse FFN layers | Scale parameters without scaling compute per token |

## Connections
- [[log]]
- [[scratchpad/jobs/reports/researcher/discovery-2026-06-09]]
- [[concepts/ml-evolution]]
- [[sources/papers/betteti-baggio-bullo-zampieri-idp-hopfield-2025]]
- [[concepts/mixture-of-experts]]
- [[index]]
- [[concepts/attention-monoidal-closure]]
- [[concepts/scaling-laws]]
- [[concepts/kv-cache]]
- [[concepts/in-context-learning]]
- [[concepts/hidden-states]]
- [[concepts/llm-inference]]
- [[concepts/length-generalization]]
- [[concepts/transformer-architecture]]
- [[concepts/attention-mechanism]]
- [[transformer-architecture]]

- [[attention-mechanism]] — the core computational unit
- [[kv-cache]] — inference optimization for decoder-only models
- [[hidden-states]] — intermediate representations at each layer
- [[ml-evolution]] — transformers as paradigm shift that prompted architecture search (NAS)
- [[scaling-laws]] — architecture enabling scaling as primary strategy
- [[length-generalization]] — the key challenge: extending beyond training context
- [[mixture-of-experts]] — sparse extension within transformer FFN layers
- [[in-context-learning]] — emergent capability enabled by large transformer models
- Concept: [[attention-monoidal-closure]]
- Concept: [[betteti-baggio-bullo-zampieri-idp-hopfield-2025]]
- Concept: [[llm-inference]]
