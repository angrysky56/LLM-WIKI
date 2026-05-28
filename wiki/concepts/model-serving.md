---
created: 2026-07-01
updated: 2026-07-01
type: concept
summary: Production ML model serving — deployment architectures, orchestration, latency/throughput tradeoffs, and the software engineering layer that connects models to users in production
tags: [mlops, serving, deployment, infrastructure, vllm, sglang, tensorrt]
sources: https://arxiv.org/abs/2309.08141, https://github.com/vllm-project/vllm
status: active
confidence: 0.85
---

# Model Serving

## Definition

Model serving is the software engineering discipline of deploying trained ML models to production — managing latency, throughput, availability, and resource utilization. For LLMs, model serving includes the inference engine, batching logic, scheduling, and the API layer that connects the model to user requests.

Model serving is distinct from model training: training produces the weights, serving keeps the model running and responding to real requests at scale. The two have very different optimization targets (training: GPU utilization and convergence; serving: latency and throughput under variable load).

## Why It Matters

A model that performs well in evaluation but is slow, expensive, or unavailable in production is not fully useful. Model serving determines:
- **Latency**: How fast does the model respond? Critical for interactive applications.
- **Throughput**: How many concurrent requests can be handled?
- **Cost**: GPU-hours per token generated. The economics of deployed AI.
- **Reliability**: Uptime, graceful degradation under load spikes.

The ML community's focus on benchmark leaderboards understates how much model-serving infrastructure determines real-world impact. vLLM's 2-4× throughput improvement over naive serving had a larger practical impact than most new model releases in 2024–2025.

## Key Systems

### vLLM

The dominant open-source LLM serving engine. Core innovation: **PagedAttention** — non-contiguous KV cache storage via fixed-size blocks that eliminates memory fragmentation. Enables:

- **2-4× throughput** vs naive attention implementations
- **Continuous batching** for dynamic request schedules
- **FP8 inference** for reduced memory footprint
- Open architecture: can be used as a drop-in inference backend for downstream frameworks

vLLM is the reference implementation for production LLM serving. Most benchmarks and comparisons use vLLM as the baseline.

### TensorRT-LLM

NVIDIA's proprietary inference engine, optimized for NVIDIA hardware. Best-in-class latency for fixed-batch production workloads. Tradeoff: less flexible than vLLM, vendor-locked to NVIDIA GPUs, harder to tune for novel architectures.

### SGLang

Structured generation language built on top of vLLM. Adds **RadixAttention** for efficient prefix caching across requests — when many users share system prompts, SGLang caches the shared KV and reuses it without recomputation. Key advantage for multi-tenant deployments.

### Ray Serve

General-purpose model serving built on Ray. Useful for multi-model serving pipelines and complex deployment topologies where models need to be composed dynamically. More general than vLLM (which is purpose-built for single-model autoregressive generation).

## Architecture Patterns

### Single-Model Single-Endpoint

Simplest pattern: one model, one endpoint, direct requests. Used for high-traffic production models that justify dedicated GPU resources (e.g., GPT-4 class models).

### Multi-Model Endpoint

Multiple models behind one endpoint with routing logic. Different models handle different request types (classification vs. generation vs. embedding). Tradeoff: resource sharing vs. interference between models.

### Ensemble Pipeline

Multiple models in a pipeline (e.g., embedding model → retrieval → generation model). Requires careful orchestration of intermediate results and failure handling. LangChain and LlamaIndex use this pattern.

### Speculative Decoding Targets

A model serving setup where a small draft model generates candidates that a large target model verifies in parallel. The serving system must coordinate the draft-target handoff and manage the verification pass efficiently.

## Latency vs. Throughput Tradeoff

| Priority | Technique | Tradeoff |
|----------|----------|----------|
| **Minimize latency** | Static batching with small batch size | Lower throughput, faster per-request response |
| **Maximize throughput** | Continuous batching, large batch sizes | Higher throughput, higher queue latency for short requests |
| **Minimize cost** | Quantization (int8/int4) + aggressive batching | Quality degradation, longer sequences may fail |

The optimal operating point depends on the application. A code autocomplete tool prioritizes latency. An async document processing job prioritizes throughput. A customer service chatbot needs a balance.

## Connections
- [[concepts/inference-efficiency]]
- [[concepts/llm-inference]]
- [[index]]
- [[concepts/model-serving]]
- [[log]]
- [[model-serving]]

- [[llm-inference]] — The technical layer below serving; KV cache, batching strategies, and inference optimization
- [[inference-efficiency]] — Broader treatment of efficiency mechanisms; model serving is the systems engineering instantiation
- [[kv-cache]] — The core memory optimization that makes long-context serving tractable; prerequisite for efficient serving
- [[inference-time-compute-scaling]] — Test-time compute choices (BoN, speculative decoding) that interact with serving architecture
- [[mixture-of-experts]] — MoE models have different serving characteristics; only active experts consume compute, complicating resource allocation
- [[mlops]] — Model serving is a subset of MLOps; the discipline of managing the full ML lifecycle in production

## Open Questions

1. **Cross-request prefix deduplication at scale**: When 1000 requests share the same system prompt, the KV cache for that prefix could be shared to avoid redundant memory and compute. Practical implementations exist (SGLang's RadixAttention) but there is no standard. At what scale does prefix sharing break even?

2. **Serving heterogeneous model families**: A serving system that must run models with different architectures (MoE, transformers, state-space models) cannot share a common engine. Can a unified serving layer abstract across architectures without losing the per-architecture optimizations that make vLLM fast?

3. **Serving cost vs. capability scaling**: The trend toward larger models with longer context has made serving more expensive per token. At what point does investing in serving infrastructure (custom silicon, aggressive quantization) become more cost-effective than spending on training a more efficient architecture?

4. **Distributed serving for very large models**: Models that exceed single-GPU memory require tensor parallelism across multiple GPUs. Current solutions (TensorPilot, Alpa) are complex to operate. Is there a path to transparent tensor parallelism that doesn't require application-level sharding?

## Limitations

- **GPU dependency**: All major serving frameworks are GPU-bound. CPU inference is possible but 10-100× slower for large models. This creates infrastructure lock-in.
- **Auto-regressive bottleneck**: Sequential token generation is latency-limited by design. Batching helps throughput but not the latency of the first token.
- **Memory wall**: KV cache dominates memory usage at long contexts. Without compression or eviction, serving context length is capped by GPU memory.
- **Vendor fragmentation**: vLLM, TensorRT-LLM, and SGLang are actively developed but have different optimization targets. Switching between them requires code changes and re-benchmarking.
