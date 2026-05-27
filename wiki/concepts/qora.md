---
created: 2026-08-08
updated: 2026-08-08
type: concept
summary: QLoRA — Quantized LoRA — fine-tuning large models in 4-bit quantization with LoRA adapters; enables frontier model training on consumer GPUs
tags: [quantization, lora, parameter-efficient-fine-tuning, 4-bit, gptq, gguf, llm-training]
sources: []
status: active
confidence: 0.8
---

# QLoRA (Quantized LoRA)

**Also known as:** QLoRA, Quantized Low-Rank Adaptation, 4-bit LoRA fine-tuning

## What It Is

QLoRA (Dettmers et al., 2023) combines low-precision quantization of the base model with full-precision LoRA adapter training. The base model is stored in 4-bit (typically NF4 — Normal Float 4), dramatically reducing memory footprint, while the LoRA adapters are trained in full precision (or bf16). This enables fine-tuning models up to 65B parameters on a single 24GB GPU.

The key design constraint: **quantization is applied only to the frozen base model's forward pass** — gradients flow through dequantized weights for the adapter update. This is the critical difference from naive quantized fine-tuning, where gradient noise from quantized rounding would destabilize training.

## The Two-Stage Design

```
Base model (frozen, 4-bit NF4)
    ↓ forward pass (dequantized on-the-fly)
LoRA adapters (trainable, full precision bf16)
    ↓ gradient update
```

1. **Quantize base model to 4-bit NF4** — Normal Float 4 is optimal for normally-distributed weights (which is what transformer weights approximate). This achieves ~4x memory reduction vs float16.

2. **Load LoRA adapters in full precision** — only (A,B) matrices per layer, rank r, so the adapter portion remains in bf16/float32.

3. **Forward pass through dequantized base** — weights are dequantized on-the-fly during forward pass (not stored in full precision). The 4-bit storage saves memory; the on-the-fly dequantization preserves numerical accuracy where it matters for gradients.

4. **Backward propagates through dequantized weights** — gradients computed against the full-precision representation, not the quantized approximation.

## Why Not Quantize the LoRA Gradients?

The original QLoRA paper (Dettmers et al., 2023) explicitly does NOT quantize the gradient computation. The reason: quantization rounding error is not Gaussian noise — it has structure that correlates with the weight magnitude. When you quantize before gradient accumulation, the rounding introduces systematic bias in the gradient direction. Over thousands of gradient steps, this bias compounds and training diverges.

QLoRA sidesteps this by keeping the base model in 4-bit (forward only) and the adapter training in full precision (forward + backward). The memory savings come entirely from the frozen base model's 4-bit storage — not from quantized gradient computation.

## NF4: The 4-bit Format

QLoRA uses **NF4 (Normal Float 4)**, a 4-bit quantization format designed for normally-distributed weights. Standard INT4 uses uniform quantization bins — NF4 uses bins optimized for the quantile distribution of Gaussian-distributed data.

Key properties:
- Optimal for weights that follow a normal distribution (most neural network weights)
- Quantization boundaries are data-dependent (computed per layer/tensor)
- Requires a calibration set (typically 1024 samples) to determine quantization boundaries

NF4 is the format used by GPTQ and the `bitsandbytes` library that powers QLoRA implementations.

## Memory Footprint Comparison

| Configuration | Memory (7B params) | Memory (13B params) | Memory (65B params) |
|--------------|---------------------|---------------------|----------------------|
| Full fine-tune (bf16) | ~14GB | ~26GB | ~130GB |
| LoRA (bf16 base, rank 8) | ~15GB | ~27GB | ~131GB |
| QLoRA (4-bit base, bf16 adapter) | ~5GB | ~10GB | ~50GB |

QLoRA brings 65B parameter models within reach of a single A100 (80GB) or even 24GB consumer GPU for fine-tuning.

## Relationship to Standard LoRA

| Property | LoRA | QLoRA |
|----------|------|-------|
| Base model precision | bf16/fp16 | 4-bit NF4 |
| Adapter precision | bf16 | bf16 |
| Memory (7B) | ~15GB | ~5GB |
| GPU requirement | High-end consumer | Mid-range consumer |
| Training stability | High | High (no quantized gradients) |
| Quality vs full fine-tune | ~95% | ~90-95% |

QLoRA trades ~5-10% quality for a 3x memory reduction. The gap is task-dependent: reasoning-heavy tasks show larger degradation; knowledge distillation tasks show smaller degradation.

## Connections to PEFT Cluster

QLoRA sits at the intersection of two major wiki clusters:

### PEFT Cluster
- [[parameter-efficient-fine-tuning]] — QLoRA is the quantized variant of LoRA; the dominant practical PEFT method for large models
- [[lora]] — QLoRA builds on LoRA's rank-decomposition mechanism; same (A,B) adapter structure
- [[qes]] — QES explores an alternative path: evolutionary search over quantization residuals rather than gradient-based LoRA updates. Both address memory efficiency but QES preserves full-precision base

### Quantization Cluster
- [[quantization]] — QLoRA's 4-bit base model relies on PTQ (post-training quantization); NF4 format is the preferred 4-bit scheme
- [[ml-evolution-benchmarking-protocol]] — QLoRA appears in the ml-evolution framework as a memory-efficient fine-tuning baseline

## Open Questions

1. At what model scale does QLoRA's quality degradation become unacceptable vs full fine-tune?
2. Can the LoRA adapter be further quantized post-training (e.g., QLoRA → QLoRA)? What precision floor maintains quality?
3. How does QLoRA interact with MoE architectures — does per-expert quantization provide compounding memory gains?
4. Does the NF4 calibration set matter significantly? Does a task-specific calibration set improve downstream performance?

## See Also

- [[parameter-efficient-fine-tuning]] — QLoRA as a PEFT method
- [[lora]] — the rank-decomposition base that QLoRA builds on
- [[quantization]] — 4-bit NF4 and PTQ as the underlying mechanism
- [[qes]] — alternative approach to quantized model adaptation via evolutionary search
- [[ml-evolution]] — QLoRA as a baseline method in the ml-evolution framework