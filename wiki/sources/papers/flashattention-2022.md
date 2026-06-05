---
summary: FlashAttention: IO-aware exact attention algorithm using tiling to reduce HBM reads/writes; foundational LLM kernel optimization
tags: [attention, transformer, kernel-optimization, inference-efficiency, gpu]
updated: 2026-06-05T20:09:39Z
created: 2026-06-05T20:09:39Z
---

---
created: 2026-06-06
updated: 2026-06-06
type: source
summary: "FlashAttention: IO-aware exact attention algorithm using tiling to reduce HBM reads/writes; 2-3× speedup on GPT-2, enables Path-X/Path-256 with 16K-64K context; foundational kernel optimization for all LLM training and inference"
tags: [attention, transformer, kernel-optimization, inference-efficiency, gpu]
sources: https://arxiv.org/abs/2205.14135
status: active
confidence: 0.95
---

# FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness

**Authors:** Tri Dao, Daniel Y. Fu, Stefano Ermon, Atri Rudra, Christopher Ré (Stanford)
**Published:** 2022-05-27 (arXiv:2205.14135)
**Venue:** NeurIPS 2022

## Core Idea

Standard attention implementations are bottlenecked by memory bandwidth, not compute. The quadratic FLOP count is dwarfed by the O(N²) reads/writes between GPU HBM and on-chip SRAM. FlashAttention makes attention **IO-aware** — it tiles the attention computation so that each pass through the SRAM does useful work on a block, dramatically reducing HBM round-trips.

## Key Technical Contribution

FlashAttention computes **exact** self-attention (not approximate) using:

- **Tiling**: Split Q, K, V into blocks that fit in on-chip SRAM. Compute attention scores block-by-block, accumulating results.
- **Online softmax**: Standard softmax requires two passes over the full row. FlashAttention uses a running rescaling trick to compute the softmax correctly in a single pass.
- **No materialization of the full N×N attention matrix**: The attention scores are computed, applied, and discarded before leaving SRAM — O(N²) HBM reads become O(N²) SRAM operations.

## Performance Results

| Model | Sequence Length | Speedup vs. Standard Attention |
|-------|----------------|-------------------------------|
| BERT-large | 512 | 15% end-to-end wall-clock (vs. MLPerf 1.1 record) |
| GPT-2 | 1K | 3× |
| Long-Range Arena | 1K–4K | 2.4× |
| Path-X | 16K | 61.4% accuracy (first transformer > chance) |
| Path-256 | 64K | 63.1% accuracy (first transformer > chance) |

## Impact

FlashAttention is arguably **the most influential single kernel optimization** in the LLM era. It:

- Made long-context transformers practical (GPT-4's 32K/128K context depends on FlashAttention variants)
- Sparked a family of IO-aware attention kernels: FlashAttention-2 (2023), FlashAttention-3 with FP8 (2024)
- Proved that **memory bandwidth is the bottleneck, not compute** — a principle that now guides all LLM serving infrastructure
- Enabled block-sparse attention extensions, combining sparsity with IO-awareness

## Connections

- [[concepts/llm-kernel-optimization]] — this page anchors the broader kernel optimization concept
- [[concepts/attention-mechanism]] — the operation being optimized
- [[concepts/transformers]] — flash attention makes transformers practical at long context
- [[concepts/inference-efficiency]] — downstream beneficiary of kernel-level optimization
- [[concepts/llm-inference]] — inference serving benefits directly
- [[concepts/mixture-of-depths]] — orthogonal optimization (adaptive depth) that combines with flash attention
- [[concepts/linear-attention]] — alternative approach to O(N) attention (Mamba, DeltaNet, Gated DeltaNet-2)

## Open Questions

- Can IO-awareness extend beyond attention to the full transformer compute graph (MLP fusion, residual streaming)?
- Is the optimal tile size fundamentally bounded by SRAM capacity, or can multi-level memory hierarchy (L1/L2/L3 awareness) yield further gains?
- How do flash-attention-style kernels compose with other GPU bottlenecks — e.g., warp divergence in sparse attention patterns?
