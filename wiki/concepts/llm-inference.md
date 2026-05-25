---
created: 2026-06-17
updated: 2026-06-28
type: concept
summary: LLM inference — serving, KV cache management, batching, and efficiency optimizations for large language models at scale
tags: [llm, inference, serving, kv-cache, optimization, ml-infrastructure]
sources: https://arxiv.org/abs/2309.05653 (EfficientMAM), https://arxiv.org/abs/2309.08141 (PagedAttention)
status: active
confidence: 0.8
---

# LLM Inference

## Definition

LLM inference refers to the process of running a trained large language model to generate outputs — the complement to training. Unlike training (which happens once and produces the model), inference happens every time the model is used, creating different optimization pressures: latency, throughput, memory, and cost per token generated.

The key challenge: autoregressive generation means each token depends on all previous tokens, creating a sequential bottleneck where the computation for token `t+1` cannot start until token `t` completes.

## The Inference Stack

Modern LLM serving systems have several layers:

### Layer 1: Autoregressive Generation

During generation, each new token attends to all previous tokens. Without optimization:
- Each token requires recomputing attention over the full history
- Generation is O(n²) in context length — unusable beyond ~500 tokens

### Layer 2: KV Cache

The key optimization. KV cache stores key-value tensors from previous positions:
- Each new token only needs to attend over cached K/V (constant compute per token)
- Memory grows linearly with context length, not compute
- See [[kv-cache]] for full treatment

### Layer 3: Batching and调度

Production inference must handle multiple concurrent requests with different:
- Input lengths
- Output lengths (unknown at start)
- Priority/urgency

**Continuous batching** (而非 static batching) dynamically adds and removes requests from GPU batches as they complete — critical for throughput since requests finish at different times.

### Layer 4: Model Serving

Key systems:
- **vLLM**: PagedAttention + continuous batching; 2-4× throughput improvement over naive attention
- **TensorRT-LLM**: NVIDIA's optimized inference engine; best latency for fixed batch sizes
- **SGLang**: Structured generation language; RadixAttention for efficient prefix caching

## Key Research Areas

### 1. KV Cache Management

The dominant memory bottleneck. With 50K context and 70B parameters (fp16), the KV cache alone requires ~160GB — larger than the model weights for smaller models.

**Key techniques:**
- **PagedAttention** (vLLM): Non-contiguous KV cache storage via fixed-size blocks; eliminates fragmentation
- **Prefix caching**: When multiple requests share a system prompt, cache the KV of the shared prefix; reuse across requests
- **Streaming cache eviction**: For very long contexts, which tokens to evict? LRU is common but optimal strategy is open

### 2. NAMM: Neural Attention Memory Models

NAMM (Neural Attention Memory Models) replace heuristic KV cache management with **learned retention strategies**. Rather than fixed eviction rules (e.g., "always keep last 4096 tokens"), NAMM models learn which past tokens are worth keeping.

The key insight: not all tokens are equally important for future attention. A retrieval-augmented generation system that fetches relevant context needs different retention behavior than a chain-of-thought reasoner that relies on earlier reasoning steps.

**Key paper:** EfficientMAM (arXiv:2309.05653) — learns to compress and retrieve relevant past content using a small auxiliary model.

### 3. Speculative Decoding

Use a small draft model to generate candidate tokens, then verify them with the large model in a single forward pass:
- If draft model is 10× smaller, generate 10 tokens in roughly the time of 1
- Large model accepts/rejects each token in parallel (no sequential decoding needed for the draft)
- Speedup: 2-4× on typical workloads; limited by the correlation between draft and target model

### 4. Batching Strategies

**Static batching**: Wait for N requests, process together, return together. Simple but wastes GPU on incomplete batches.

**Continuous batching** (dynamic batching): Add requests to an in-progress batch as slots open. Maximizes GPU utilization but requires careful scheduling.

**Chunked prefill**: Split long input sequences into chunks to avoid GPU memory spikes when a very long request blocks the batch.

### 5. Quantization at Inference

Reducing precision (fp16 → int8 → int4) dramatically reduces memory and increases throughput:
- **AWQ**: Activation-aware weight quantization; protects salient weights
- **GPTQ**: Post-training quantization; faster but quality degradation on complex tasks
- **KV cache quantization**: Even the attention cache can be quantized (FP8 KV cache) for additional memory savings

## Economics of Inference

The decision of how much inference compute to spend depends on the error cost vs compute cost tradeoff (see [[inference-time-compute-scaling]] for full treatment):

| Error Cost | Compute Strategy |
|-------------|------------------|
| High (code, math, legal) | BoN-16 to BoN-64 with PRM guidance |
| Medium (fact QA, classification) | Adaptive budget with hidden-state gating (ELHSR-style) |
| Low (chat, creative) | Single-pass generation |

## Connections

- [[kv-cache]] — the dominant memory optimization; prerequisite for efficient long-context generation
- [[namm]] — learned KV cache management; replacing heuristic rules with trained models
- [[inference-time-compute-scaling]] — the economic and technical framework for deciding how much compute to spend per token
- [[transformer-architecture]] — the underlying architecture that makes LLM inference distinct from classical inference
- [[mixture-of-experts]] — conditional computation at inference; only active experts consume compute per token
- [[model-serving]] — systems engineering layer; vLLM, TensorRT-LLM, SGLang

## Open Questions

1. **Optimal cache eviction**: For very long contexts, which tokens should be evicted? LRU is the default but is it optimal? Learned eviction strategies (NAMM) show promise but aren't standard.

2. **Cross-request KV sharing**: When a system prompt is shared across many requests (e.g., 1000 users with the same template), can the shared prefix KV cache be deduplicated? Practical implementations exist but no standardized solution.

3. **Speculative decoding with divergent models**: Current speculative decoding assumes draft and target model share architecture. Can we do speculative decoding between fundamentally different architectures (e.g., small transformer draft, large MoE target)?

4. **Energy efficiency**: Inference now consumes a significant fraction of global AI compute. What are the fundamental limits of inference efficiency, and can we approach them?

## Limitations

- **Memory wall**: For large models at long contexts, KV cache memory dominates — without compression or eviction, contexts cannot exceed GPU memory
- **Autoregressive bottleneck**: Sequential token generation is fundamentally latency-limited — batching helps throughput but not latency per token
- **Cold-start problem**: Every new request pays the full attention cost for its prefix — no reuse across requests unless the prefix is shared (which requires careful system design)
- **Quantization artifacts**: Aggressive quantization (int4) can produce qualitatively different errors than the full-precision model — not just worse, but sometimes bizarre