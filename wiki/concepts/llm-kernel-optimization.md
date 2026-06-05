---
summary: LLM kernel optimization — FlashAttention, FlashDecoding, kernel fusion, and IO-aware GPU techniques that drive most LLM throughput improvements since 2022
tags: [llm, kernel-optimization, inference-efficiency, gpu, transformer]
updated: 2026-06-05T20:10:17Z
---

---
created: 2026-05-25
updated: 2026-06-06
type: concept
summary: LLM kernel optimization — GPU kernel-level techniques for efficient LLM training and inference; FlashAttention, FlashDecoding, kernel fusion, quantization kernels, and IO-aware algorithms
sources: https://arxiv.org/abs/2205.14135
tags: [llm, kernel-optimization, inference-efficiency, gpu, transformer]
status: active
confidence: 0.72
---

# LLM Kernel Optimization

## Definition

**LLM kernel optimization** refers to techniques that optimize the GPU kernel implementations of LLM operations — attention, feedforward, normalization, and activation functions — to maximize throughput and minimize memory usage at the hardware level. Unlike architectural innovations (new attention variants, different layer counts), kernel optimizations preserve the exact mathematical computation while improving how it maps to GPU hardware (SRAM, HBM, tensor cores, warp scheduling).

## The Core Principle: IO-Awareness

The most significant insight in modern LLM kernel optimization is that **memory bandwidth is the bottleneck, not FLOPs**. Standard implementations of attention require O(N²) reads/writes to GPU high-bandwidth memory (HBM), even though the actual compute (matrix multiply) only requires O(N²) FLOPs. GPU HBM bandwidth (~1-2 TB/s on A100/H100) is orders of magnitude slower than on-chip SRAM bandwidth (~20 TB/s shared memory).

**FlashAttention** (Dao et al., 2022) is the canonical example: by tiling the attention computation so it fits entirely in GPU SRAM and using online softmax to avoid materializing the full attention matrix, FlashAttention achieves 2-3× wall-clock speedup while computing the exact same mathematical result.

## Major Kernel Optimization Categories

### 1. IO-Aware Attention Kernels
- **FlashAttention** — tiled, exact attention with online softmax ([[sources/papers/flashattention-2022]])
- **FlashAttention-2** — reduced non-matrix-multiply overhead, better warp partitioning
- **FlashAttention-3** — FP8 quantization in the attention kernel, leveraging H100 Hopper tensor cores
- **FlashDecoding** — optimized kernel for the autoregressive decoding phase (batch-size-1 attention)
- **Block-sparse FlashAttention** — FlashAttention extended with block-level sparsity masking

### 2. Quantization Kernels
- **GPTQ** — post-training quantization kernel for weight compression (4-bit, 3-bit)
- **AWQ** — activation-aware weight quantization (better perplexity retention than GPTQ at low bitwidths)
- **FP8 kernels** — native FP8 matmul on H100 with lower memory footprint

### 3. Kernel Fusion
- **Fused MLP + GELU** — avoids writing the intermediate activation to HBM
- **Fused layer norm + residual add** — single kernel for normalization and skip connection
- **FlashAttention-based MHA fusion** — single kernel for the entire multi-head attention block

### 4. Serving Optimizations
- **PagedAttention (vLLM)** — KV-cache management at page granularity, eliminating fragmentation
- **Prefix caching** — reuse KV-cache for shared prompt prefixes across requests
- **Continuous batching** — add/remove sequences from the batch at each iteration

## Why This Matters

Kernel optimization is responsible for as much LLM performance improvement as architectural advances since 2022:

- GPT-4's 32K/128K context windows depend on FlashAttention-family kernels
- vLLM's throughput would be impossible without PagedAttention kernel
- The practical speed of all open-weight models (Llama 3, Mixtral, DeepSeek) is determined more by kernel availability than model architecture
- The cost of serving LLMs has dropped by ~10× since 2023, primarily through kernel optimization

## Connections

- [[sources/papers/flashattention-2022]] — foundational source, the most influential kernel optimization
- [[concepts/attention-mechanism]] — the operation being kernel-optimized
- [[concepts/transformers]] — the model architecture that requires optimized kernels
- [[concepts/inference-efficiency]] — broad topic; kernel optimization is the primary driver
- [[concepts/quantization]] — weight compression kernels (GPTQ, AWQ)
- [[concepts/llm-inference]] — serving infrastructure dependently on kernel efficiency
- [[concepts/vllm]] — PagedAttention kernel for KV-cache management
- [[concepts/memory-mechanisms]] — the memory hierarchy (SRAM/HBM) that IO-aware kernels exploit
- [[concepts/linear-attention]] — alternative approach that avoids the quadratic attention kernel entirely

## Open Questions

1. **Is IO-aware kernel optimization hitting diminishing returns?** FlashAttention-3's FP8 gains are narrower than FlashAttention-2's — the low-hanging fruit (tiling, online softmax) is taken.
2. **Can kernel optimization extend beyond attention to the entire compute graph?** Full-layer fusion (attention + MLP + norm in one kernel) would eliminate all intermediate HBM traffic.
3. **How do kernel optimizations compose with sparsity?** Sparse attention kernels (block-sparse FlashAttention, MoE kernel optimizations) add complexity to tiling strategies.
