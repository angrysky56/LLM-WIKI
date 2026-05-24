---
created: 2026-05-28
updated: 2026-06-09
type: concept
summary: Inference optimization technique that caches key-value tensors from previous tokens to avoid recomputation during autoregressive generation
tags: [transformers, inference, optimization, ml-infrastructure]
sources: https://arxiv.org/abs/2309.05653 (Efficient Long Sequence Modeling)
status: active
confidence: 0.85
---

# KV-Cache

**Also known as:** Key-value cache, attention cache, past cache

## What It Is

KV-cache is an inference optimization technique for autoregressive transformers. During generation, each new token attends to all previous tokens. Without caching, you'd recompute attention over the entire context from scratch for every generated token — O(n²) compute per token.

KV-cache stores the key and value tensors from all previous positions in a persistent cache. When generating token *t+1*, you:
1. Compute Q for position *t+1*
2. Look up cached K and V for positions 0...t
3. Attend only over the cached K/V (single forward pass for the new token)

The memory cost grows linearly with context length, but the compute per token becomes constant (not quadratic).

## Why It Matters

Autoregressive generation involves iterating the same model on its own outputs. Without KV-cache:
- Each token requires recomputing attention over the full history
- Generation is O(n²) in context length
- Practically unusable beyond a few hundred tokens

With KV-cache:
- Each token's computation is constant time (dominated by the new token's Q projection and attention over cached KV)
- Generation can scale to thousands of tokens

The tradeoff: memory usage grows linearly with context length, requiring careful management in production systems.

## PagedAttention

The main production challenge is memory fragmentation when cache doesn't fit in GPU memory. **PagedAttention** (vLLM) handles this by managing KV cache in fixed-size blocks (like OS memory pages), allowing non-contiguous storage and efficient batching across requests with different context lengths.

This enabled significant throughput improvements — vLLM reports 2-4× higher throughput than naive attention implementations for LLM serving.

## Multi-Query Attention and Grouped Query Attention

MQA and GQA significantly reduce KV cache size:
- **MQA:** Single KV head shared across all query heads → 1/h the KV cache
- **GQA:** g KV heads (g << h) shared by groups of queries → intermediate between MHA and MQA

These reduce memory proportionally, enabling longer contexts within the same memory budget.

## Connections

- [[transformer-architecture]] — applies to decoder-only transformers
- [[attention-mechanism]] — the mechanism being optimized
- [[hidden-states]] — K/V are projections of hidden states
- [[inference-time-compute-scaling]] — KV-cache is a prerequisite for many inference-time compute strategies (prefix caching, speculative decoding)
- [[mixture-of-experts]] — MoE models benefit especially from KV-cache since active expert count is small per token but memory for all experts is still present

## Open Questions

- **Prefix caching:** When multiple requests share a common prefix (system prompt), can the KV-cache be shared across requests? State-of-the-art serving systems handle this but it's not yet standardized.
- **Cache eviction:** For very long contexts, which tokens should be evicted? LRU is common but optimal eviction strategy is an open research question.