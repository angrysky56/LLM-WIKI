---
summary: Quantization — reducing model weight precision (FP32→INT8/INT4) for memory/compute efficiency; calibration methods, NF4/GPTQ/AWQ formats, KV-cache quantization, and quantization-accuracy tradeoff
tags: [quantization, model-compression, llm-training, inference-efficiency, llm-inference]
updated: 2026-06-01T04:02:52Z
---

---
created: 2026-07-28
updated: 2026-09-13T08:10:00Z
type: concept
summary: Quantization — reducing model weight precision (FP32→INT8/INT4) to decrease memory and compute costs; PTQ, QAT, AWQ, GPTQ, KV-cache quantization, and the quantization-accuracy tradeoff
tags: [quantization, model-compression, llm-training, inference-efficiency, llm-inference]
sources: https://arxiv.org/abs/2309.05653 (EfficientMAM), https://arxiv.org/abs/2212.11288 (QLoRA)
status: active
confidence: 0.72
---

# Quantization

Quantization reduces the precision of neural network weights and activations from high-precision formats (typically FP32 or BF16) to lower-precision integer formats (INT8 or INT4). The goal is to reduce memory footprint and increase inference throughput, at the cost of some accuracy degradation. In LLM serving contexts, quantization is often the difference between a model fitting in GPU memory and not.

## The Quantization Pipeline

### Step 1: Choose Bit-Width

| Format | Memory vs FP16 | Typical Quality Loss | Use Case |
|--------|---------------|---------------------|----------|
| **FP16** | 1× (baseline) | None | Full precision training/evaluation |
| **INT8** | 2× reduction | 1-3% on benchmarks | Production inference, acceptable quality |
| **INT4** | 4× reduction | 5-15% on benchmarks | Memory-constrained serving, 4-bit inference |
| **NF4** | 4× reduction | 3-8% on benchmarks | Optimal for normally-distributed weights (QLoRA) |

### Step 2: Choose Calibration Method

Quantization requires determining the mapping from floating-point values to integer bins. Three main approaches:

**Post-Training Quantization (PTQ)**: Quantize a trained model without any retraining. Fast and simple — just需要一个calibration dataset (typically 1024 samples) to determine quantization boundaries. Quality depends on the calibration data being representative.

**Dynamic Quantization**: Quantization boundaries computed at runtime based on actual activation ranges. No calibration needed but more overhead during inference.

**Quantization-Aware Training (QAT)**: Training with quantization constraints built in from the start. The model learns to be robust to quantization noise during training. Higher quality than PTQ but requires full retraining — expensive for large models.

### Step 3: Handle Activation Quantization

Weight quantization alone provides significant memory savings. But activations (the outputs of each layer, which feed into the next layer) also consume memory during inference. The challenge: activation ranges vary dramatically across inputs, unlike weights which have fixed ranges.

**Static activation quantization**: Use calibration data to determine fixed quantization boundaries for activations. Simple but can overflow on out-of-distribution inputs.

**Dynamic activation quantization**: Compute quantization boundaries per-token during inference. More accurate but introduces compute overhead.

## Key Quantization Formats

### INT8 / INT4 — Uniform Quantization

Standard uniform quantization maps floating-point values to integer bins of equal width:

```
quantized = round(fp_value / scale)
scale = max_abs / (2^(bits-1) - 1)
```

**Limitation**: Uniform bins work poorly when weight distributions are non-uniform (e.g., bimodal). Most neural network weights are approximately Gaussian — uniform quantization wastes precision on values near zero where most weights cluster, while insufficient precision for the tails where outlier weights live.

### NF4 — Normal Float 4

NF4 (Normal Float 4) is designed specifically for normally-distributed weights. It uses non-uniform quantization bins optimized for Gaussian distributions:

- Quantization boundaries are data-dependent (computed per-tensor on calibration data)
- More bins near zero (where weights concentrate), fewer bins in the tails
- Optimal for weights that follow a normal distribution

NF4 is the format used by QLoRA and the `bitsandbytes` library. It achieves better quality than INT4 on LLM benchmarks because the bin distribution matches the weight distribution.

**Key property**: NF4 requires a calibration set (typically 1024 samples from the training distribution) to determine optimal quantization boundaries. The quality of the calibration set directly affects the quality of the quantized model.

### FP8 — 8-bit Floating Point

FP8 is a middle ground between INT8 and FP16: 8 bits but floating-point format with an exponent and mantissa. Two variants:
- **E4M3**: 4-bit exponent, 3-bit mantissa — better for activations (need dynamic range)
- **E5M2**: 5-bit exponent, 2-bit mantissa — better for weights (dominated by small values)

FP8 is emerging as the standard for inference acceleration on NVIDIA H100/H200 GPUs, which have native FP8 matmul support.

## Weight-Only vs Full Quantization

**Weight-only quantization**: Only model weights are quantized; activations computed in FP16/BF16. This gives memory savings (weights are the dominant storage cost) without the accuracy complications of activation quantization.

**Full quantization**: Both weights and activations quantized. More complex (requires careful handling of activation outliers) but enables further memory and compute savings.

For LLM serving, weight-only INT8 quantization is the most common approach — significant memory savings with minimal quality impact.

## KV Cache Quantization

The KV cache is a dominant memory bottleneck at long contexts. With 50K context and a 70B model in FP16, just the KV cache requires ~160GB — larger than the model weights for smaller models.

**KV cache quantization** quantizes the stored key and value tensors:
- FP16 KV cache → FP8 KV cache: 2× memory reduction, minimal quality loss
- FP16 KV cache → INT8 KV cache: 2× reduction, some quality degradation on long-context tasks
- INT4 KV cache: 4× reduction but significant quality loss unless using special formats (e.g., kvquant)

Key challenge: unlike model weights (static), KV cache values depend on the input — the quantization boundaries must be either dynamic or calibrated for the expected input distribution.

## AWQ vs GPTQ

Two dominant post-training quantization methods for LLMs:

| Property | AWQ (Activation-aware Weight Quantization) | GPTQ (Post-Training Quantization) |
|----------|---------------------------------------------|-------------------------------------|
| **What it protects** | Salient weights (high activation impact) | Weights with large magnitude |
| **Key insight** | Not all weights matter equally for output quality | Large weights dominate reconstruction error |
| **Calibration** | Uses activation statistics, not just weight distribution | Uses weight distribution only |
| **Quality on INT4** | Better on complex tasks (code, math) | Good on general language tasks |
| **Speed** | Similar inference speed | Similar inference speed |
| **Origin** | Lin et al., arXiv:2306.10778 | Frantar et al., arXiv:2210.17323 |

AWQ generally performs better on tasks where activation patterns are important (reasoning, code generation). GPTQ is simpler and faster to apply. Both can achieve comparable quality with proper calibration.

## Quantization-Accuracy Tradeoff

The fundamental tension: aggressive quantization saves memory and increases throughput but degrades model quality. The acceptable tradeoff depends on the use case:

| Task | Tolerable Degradation | Recommended Format |
|------|----------------------|-------------------|
| High-stakes (code, math, legal) | < 2% accuracy loss | INT8 or FP8 |
| General language generation | < 5% loss | INT8 or mild INT4 |
| Chat / creative writing | < 10% loss | INT4 (NF4) acceptable |
| Low-stakes (summarization) | < 15% loss | INT4 with AWQ |

## Quantization and Fine-Tuning

The relationship between quantization and fine-tuning has become central to modern LLM adaptation:

**QLoRA (Quantized Low-Rank Adaptation)**: The base model stays frozen in 4-bit NF4; only the LoRA adapters train in full precision. This is the dominant method for fine-tuning large models on consumer GPUs. The key insight: gradients flow through dequantized weights during training — the 4-bit storage is a memory optimization that doesn't compromise gradient quality.

**QA-LoRA**: Quantization-aware LoRA that jointly quantizes the base model and adapts the LoRA ranks to minimize accuracy loss.

**AWQ + LoRA**: Apply AWQ to the base model, then train LoRA adapters. The LoRA adapters can partially compensate for quantization errors.

## Connections

- [[llm-inference]] — quantization is a key optimization layer in the inference stack
- [[kv-cache]] — KV cache quantization is a distinct sub-problem (quantizing activations, not just weights)
- [[qora]] — QLoRA is the dominant use case connecting quantization and PEFT
- [[parameter-efficient-fine-tuning]] — QLoRA is a PEFT variant combining quantization and LoRA
- [[transformer-architecture]] — quantization modifies how transformer computations are performed
- [[model-serving]] — quantization strategy is a key decision in model serving architecture

## Open Questions

1. **Optimal KV cache quantization**: What is the accuracy tradeoff for aggressive KV cache quantization (INT4)? Can learned quantization boundaries outperform static calibration?

2. **Joint weight + activation quantization at INT4**: Weight-only INT4 is well-understood; full INT4 (including activations) remains challenging due to activation outliers.

3. **Calibration dataset quality**: How much does calibration set quality matter for NF4 quantization? Is there a systematic way to select calibration data that covers the full output distribution?

4. **Quantization-aware fine-tuning vs PTQ**: When is QAT worth the compute cost vs PTQ with better calibration? This tradeoff is poorly understood for models > 30B parameters.

## Limitations

- **Accuracy cliff**: Some models exhibit sharp accuracy degradation below a certain bit-width threshold, not smooth degradation. This makes it hard to predict acceptable quantization levels without empirical testing.
- **Task-dependent sensitivity**: Some tasks (math, code) are more sensitive to quantization than others (chat). The same quantization level can be acceptable for one task but not another.
- **Calibration data dependency**: PTQ quality depends on calibration data being representative. For specialized applications, default calibration sets may not be adequate.
- **Hardware support**: Not all quantization formats are supported on all hardware. INT4 support is limited — most production inference uses INT8 or FP8.
