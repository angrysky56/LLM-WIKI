---
created: 2026-05-29
updated: 2026-06-09
type: concept
summary: Key-value lookup mechanism at the core of transformer architectures — enables content-dependent, long-range dependency modeling
tags: [transformers, deep-learning, architecture, attention, self-attention]
sources: https://arxiv.org/abs/1706.03762 (Attention is All You Need)
status: active
confidence: 0.9
---

# Attention Mechanism

**Source:** Vaswani et al., *Attention Is All You Need* (NeurIPS 2017)
**Confidence:** 0.9 — well-established mechanism with extensive subsequent work

## What It Is

The attention mechanism allows a model to weigh the importance of different parts of the input when producing each output. Unlike recurrent architectures that process sequences step-by-step, attention enables direct connections between any two positions — regardless of their distance in the sequence.

The core formulation is **scaled dot-product attention**:

```
Attention(Q, K, V) = softmax(QKᵀ / √d) · V
```

Where:
- **Q (Query):** What am I looking for?
- **K (Keys):** What do I contain?
- **V (Values):** What information do I carry?

The output is a weighted sum of values, where weights are determined by the similarity between query and keys. The √d scaling prevents the dot products from growing too large in high-dimensional spaces, which would push softmax into saturated regimes.

## Why It Matters

Attention solves the long-range dependency problem that plagued RNNs. In recurrence, information must traverse each intermediate step to travel from position *i* to position *j*. Attention creates a direct edge — every position attends to every other position in a single operation.

This has three practical consequences:
1. **Parallelism** — All attention heads compute simultaneously, unlike RNN step-by-step unrolling
2. **Path length** — O(1) path length between any two positions (vs O(n) for RNNs)
3. **Content dependence** — Relationships are determined by learned similarity, not fixed position

The ability to model arbitrary content-dependent relationships is what makes transformers effective at tasks where distant context matters: language modeling, protein structure, code comprehension.

## Variants

| Variant | Description | Use Case |
|---------|-------------|----------|
| **Multi-head attention** | Parallel attention layers with different Q/K/V projections | Captures multiple relationship types simultaneously |
| **Cross-attention** | Queries from one sequence, keys/values from another | Sequence-to-sequence tasks, cross-modal alignment |
| **Flash Attention** | IO-aware exact attention with tiling; reduces memory from O(n²) to O(n) | Long context training/inference |
| **Grouped Query Attention (GQA)** | Keys/values shared across multiple query groups | Reduced KV cache size with minimal quality loss |
| **Multi-Query Attention (MQA)** | Single key/value head for all query heads | Aggressive memory reduction (e.g., inference serving) |

### Multi-Head Attention (MHA)

Instead of a single attention function, multi-head attention runs *h* attention heads in parallel, each with their own Q/K/V projections. The outputs are concatenated and projected:

```
MultiHead(Q, K, V) = Concat(head₁, ..., headₕ) · Wᴼ
where headᵢ = Attention(QWᵢQ, KWᵢK, VWᵢV)
```

This allows each head to attend to different aspects of the relationship. In practice, different heads specialize: some capture syntactic dependencies, others capture semantic roles, others track coreference.

### Flash Attention

Standard attention has O(n²) memory in sequence length — the attention matrix must be materialized. Flash Attention exploits the linear associativity of matrix multiplication to compute attention in tiles that fit in SRAM, reading/writing from HBM only once per block. This reduces memory from O(n²) to O(n) while maintaining bit-exact results.

The practical impact: Enables attention over sequences of length 65K+ on a single GPU, where standard attention would OOM at 4K-8K.

## Connections

- [[transformer-architecture]] — built on attention mechanisms as the core component
- [[kv-cache]] — inference optimization for autoregressive attention
- [[hidden-states]] — intermediate Q/K/V representations at each layer
- [[ml-evolution]] — transformers as a paradigm shift that prompted architecture search
- [[scaling-laws]] — the transformer architecture enabled scaling as a primary research strategy
- [[length-generalization]] — challenge of extending context beyond training distribution
- [[mixture-of-experts]] — often applied inside the FFN layer of transformer blocks