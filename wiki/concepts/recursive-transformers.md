---
summary: Transformer variants with recursive hidden state passing across layers — combining parallel attention efficiency with sequential inductive bias
tags: [transformers, recursion, neural-architecture, llm-architecture, memory]
updated: 2026-05-28T14:05:04Z
---

---
created: 2026-05-25
updated: 2026-08-19
type: concept
summary: Transformer variants that add recursive hidden state passing across layers — combining the parallel efficiency of attention with the sequential inductive bias of recurrence
tags: [transformers, recursion, neural-architecture, llm-architecture, memory]
sources: []
status: active
confidence: 0.65
---

# Recursive Transformers

Recursive transformers augment the standard transformer architecture with a **recurrent hidden state** that passes across layers, combining parallel attention computation with sequential information flow. Where a standard transformer processes all layers independently on the full input, a recursive transformer passes its computed state forward — the output of layer N becomes part of the input to layer N+1.

## Motivation

Standard transformers have no memory between layers — each layer sees the same initial input plus positional encodings. This makes it difficult to:
- Maintain a coherent working memory that accumulates across processing steps
- Incorporate feedback connections (bottom-up, top-down processing)
- Model sequences where state must be refined iteratively

Recurrence adds an inductive bias toward sequential computation that mirrors classical RNNs, but within each layer the attention computation remains parallel.

## Approaches

### RWKV (Receptive Weighted Key Value)
The RWKV architecture (Peng et al.) replaces attention with a linearized form that supports recurrence:

```
output_t = Σ_{i=1}^{t} (o_i · w_{i,t})
```
where w_{i,t} is a time-mixing weight decaying exponentially with distance. This achieves O(T) instead of O(T²) attention cost while maintaining recurrence. RWKV-4 and later versions add token-level and channel-level recurrence mechanisms.

### RNN-Transformer Hybrids
Various hybrid approaches pass cached hidden states across transformer layers during inference:
- **LSTM-augmented attention**: LSTM gates modulate how new information updates the recurrent state
- **Gemma-style continuous batching with KV-cache**: Not architectural recurrence, but inference-time state propagation via cached key-value pairs

### Recursive Neural Networks (General)
The broader class of [[recursive-neural-networks]] (not transformer-specific) includes:
- Tree-structured neural networks for parse trees
- Graph neural networks with message passing
- Neural GPUs and differentiable neural computers

The transformer-specific recursion variants share the goal of adding sequential state but differ in how they implement recurrence relative to attention.

## Connections

- [[transformers]]: The base architecture recursive transformers build on
- [[mixture-of-experts]]: Can be combined with recursion for sparse recurrent layers
- [[mixture-of-recursions 1]]: Synthesis-level concept exploring iterative refinement loops (no dedicated page yet — this is the conceptual parent)
- [[recursive-neural-networks]]: Broader class of recursive neural architectures
- [[state-space-models]]: Alternative approach to long-range dependencies via recurrence (Mamba)
- [[titans]]: Adds explicit memory layers — related goal, different mechanism
- [[working-memory]]: What recursive state effectively implements within the model

## Open Questions

- Can recursive transformers match pure attention on very long contexts, or does the recurrence create a bottleneck?
- How does gradient flow through recursive connections compare to residual connections in deep attention stacks?
- RWKV's linearized attention — does it lose the full-attention expressivity, and if so, where?
