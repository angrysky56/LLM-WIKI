---
created: 2026-06-03
updated: 2026-07-15
type: concept
summary: QES (Quality-Evolutionary Search) — accumulated error feedback for high-precision fine-tuning of quantized models at inference-level memory
tags: [quantization, fine-tuning, error-feedback, ml-evolution, memory-efficiency]
sources: wiki/sources/articles/ml-evolution-benchmarking-protocol.md
status: active
confidence: 0.7
---

# QES (Quality-Evolutionary Search)

**Also known as:** QES, Quality-Evolutionary Search, Error-Feedback Fine-Tuning

## What It Is

QES is a fine-tuning method for quantized LLMs that uses accumulated error feedback to recover precision lost through quantization. When a model is quantized to 4-bit or lower, the quantization error (difference between original float weights and quantized approximations) accumulates across layers and compounds — leading to degraded output quality. QES tracks this error and applies corrective evolutionary mutations to compensate.

The key insight: quantization error is structured and predictable, not random noise. QES leverages this structure by:
1. Running forward passes in quantized precision (saving memory)
2. Accumulating per-layer quantization residuals across the forward pass
3. Applying evolutionary search over the residual space to find precision-correcting weight updates

This enables "inference-level memory" fine-tuning — the model being updated lives in quantized form, so GPU memory requirements approach inference levels rather than full fine-tuning levels.

## Why Accumulated Error Feedback?

Standard quantized fine-tuning has a fundamental problem: gradient updates computed in quantized space are noisy (quantization rounds weights to discrete values before gradient accumulation). The resulting update direction is correct in expectation but high-variance.

QES sidesteps this by separating the **error tracking** from the **error correction**:
- **Error tracking**: Forward pass in quantized precision records quantization residuals per layer
- **Error correction**: Evolutionary search in the residual space — mutations are applied to accumulated residuals rather than the quantized weights directly

The residuals encode what the quantized model "lost" relative to the full-precision reference. As the evolutionary algorithm selects for fitness (downstream task performance), it implicitly discovers corrective residual patterns that offset quantization degradation.

## The Algorithm

1. **Quantize**: Load base model in quantized form (e.g., 4-bit GPTQ/GGUF)
2. **Forward tracking**: Run calibration data; record per-layer quantization residuals
3. **Residual population**: Initialize population of residual correction vectors from accumulated error
4. **Evolutionary mutation**: Perturb residual vectors; apply to quantized weights
5. **Fitness evaluation**: Run downstream benchmark (downstream task, not just perplexity)
6. **Selection**: Retain residual corrections that most improve task performance
7. **Repeat**: Covariance adaptation over residual correction space

## Why "Quality-Evolutionary"?

"Quality" refers to recovering output quality (reducing quantization artifacts). "Evolutionary" references the search mechanism — CMA-ES over the residual space. The method is not merely a quantification algorithm; it's an evolutionary optimization that operates at the interface between quantized representation and task loss.

## Trade-offs

| Approach | Memory | Quality | Speed |
|----------|---------|---------|-------|
| Full fine-tuning (float16) | High | Best | Slow |
| QLoRA | Medium | Good | Medium |
| **QES** | **Low (inference-level)** | **Good with error feedback** | **Medium** |

QES occupies a middle ground: memory efficiency approaching pure quantization, with evolutionary search recovering much of the quality gap. The main cost is evolutionary search overhead (multiple forward/backward passes per generation), which partially offsets the memory gains.

## Connection to ML Evolution Framework

In the ML Evolution Benchmarking Protocol framework, QES represents the "tactical generation" complement to the "strategic exploration" role of methods like CoLLM-NAS. Where:
- **CoLLM-NAS**: Navigator LLM explores architecture space; Generator LLM evaluates
- **QES**: Evolutionary search explores residual correction space; accumulated error feedback evaluates

Both are guided evolution methods where LLMs (or their derived representations) guide the search.

## Connections
- [[concepts/bounded-memory-budget-optimization]]
- [[sources/articles/ml-evolution-benchmarking-protocol]]
- [[concepts/qes]]
- [[scratchpad/agent-sheets/researcher/carryover]]
- [[index]]
- [[concepts/maximum-occupancy-principle]]
- [[concepts/llama-nas]]
- [[log]]
- [[scratchpad/jobs/reports/researcher/discovery-2026-08-03]]
- [[concepts/neural-architecture-search]]
- [[concepts/qora]]
- [[scratchpad/jobs/reports/researcher/discovery-2026-07-15]]
- [[qes]]

- [[ml-evolution-benchmarking-protocol]] — source reference for QES
- [[ml-evolution]] — QES as guided evolution of quantized representations
- [[llm-training]] — QES compensates for quantization error; relates to GPTQ, GGUF, AWQ
- [[lora]] — both reduce trainable parameters; QES works on residuals, LoRA on weight updates
- [[parameter-efficient-fine-tuning]] — QES is a PEFT method for the quantized setting
- [[evolutionary-strategies]] — QES uses CMA-ES-style adaptation over residual space
- [[namm]] — NAMM evolves KV cache representations; QES evolves quantization residuals; different memory modalities, similar evolutionary philosophy

- [[llama-nas]]
- [[qora]]
- [[neural-architecture-search]]
- [[bounded-memory-budget-optimization]]
- [[maximum-occupancy-principle]]
## Open Questions

1. Does QES residual correction transfer across different token sequences, or only for the calibration distribution?
2. Can QES be combined with LoRA adapters for doubly-efficient fine-tuning (quantized base + residual-space adaptation)?
3. At what quantization level (bit-width) does QES stop providing meaningful quality recovery?
4. How does QES compare to on-the-fly dequantization for inference-time compute-heavy workloads?
