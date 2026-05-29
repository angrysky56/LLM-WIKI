---
created: 2026-06-03
updated: 2026-07-15
type: concept
summary: Parameter-Efficient Fine-Tuning (PEFT) — methods for adapting large models by updating only a small fraction of parameters; LoRA, QLoRA, AdaLoRA, DoRA, and related techniques
tags: [fine-tuning, parameter-efficiency, lora, quantization, adapter-methods, llm-training]
status: active
confidence: 0.85
---

# Parameter-Efficient Fine-Tuning (PEFT)

**Also known as:** PEFT, Parameter-Efficient Fine-Tuning, Adapter Methods, LoRA-style methods

## What It Is

PEFT methods reduce the computational cost of fine-tuning large models by updating only a small, structured subset of parameters while keeping most weights frozen. Rather than full fine-tuning (which updates all parameters per task), PEFT methods inject or update a small number of additional parameters — achieving comparable adaptation quality at a fraction of the compute and memory cost.

## Core Methods

### LoRA (Low-Rank Adaptation)

LoRA (Hu et al., 2021) is the foundational PEFT method. It exploits the low-rank structure of weight updates during fine-tuning:

```
ΔW = BA where B ∈ R^(d×r), A ∈ R^(r×k), rank r << min(d,k)
```

Instead of updating W directly, LoRA trains A and B while freezing W₀. The output becomes:
```
h = W₀x + BAx
```

Key properties:
- **Rank selection**: r ∈ [4, 128+] — controls the expressiveness of adaptation
- **Weight combination**: W = W₀ + BA allows merging adapters post-training (no inference overhead)
- **Multiple adapters**: Different tasks get different (A,B) pairs; merged via meta-learning or routing

### QLoRA (Quantized LoRA)

QLoRA (Dettmers et al., 2023) combines quantization with LoRA:
- Base model stored in 4-bit quantized form (GPTQ/GGUF)
- LoRA adapters trained in full precision (or higher precision than base)
- Enables fine-tuning frontier models on consumer GPUs (24GB VRAM)

QLoRA does not quantize the LoRA gradients — quantization is applied only to the frozen base model's forward pass. This preserves most of the quality gains from 4-bit quantization while maintaining training stability from full-precision adapter updates.

### AdaLoRA (Adaptive LoRA)

AdaLoRA (Zhang et al., 2023) dynamically allocates rank budget based on importance scores:
- Not all layers need the same rank — some are more adaptable than others
- AdaLoRA measures the singular value importance of each (A,B) pair and redistributes rank budget
- Early stopping for low-importance layers saves parameters without sacrificing performance

### DoRA (Weight-Decomposed LoRA)

DoRA (Liu et al., 2024) separates magnitude and direction updates:
```
W = W₀ + m·(VA)/||VA||_F
```
Where m is a scalar magnitude and VA is the LoRA update decomposed into magnitude and direction. DoRA views fine-tuning as decomposition into magnitude + directional change, which aligns better with full fine-tuning's update geometry than standard LoRA's additive update.

### LoRA+ and LoRA-FA

- **LoRA+** (Hayou et al., 2024): Different learning rates for A and B matrices (α/r for A, α/(β·r) for B) — stabilizes training and improves convergence
- **LoRA-FA**: Apply LoRA to attention and MLP layers separately with different rank budgets

## The Category Landscape

PEFT is broader than just LoRA variants. Other adapter paradigms:

| Method | Adaptation Mechanism | Trainable Parameters |
|--------|---------------------|---------------------|
| **LoRA** | Low-rank weight decomposition | ~0.1-1% of W |
| **Adapter** | Bottleneck MLP + residual | ~1-5% of W |
| **Prefix Tuning** | Learnable prefix tokens | ~0.1% of parameters |
| **Prompt Tuning** | Soft prompt embeddings | ~0.01% of parameters |
| **IA³** | Learned element-wise rescaling | ~0.01% of parameters |

LoRA is the most widely used because it merges cleanly (no inference overhead), is simple to implement, and composes well with quantization.

## Connections to Broader Architecture

PEFT methods are central to several clusters in this wiki:

### LLM Training Cluster
- [[llm-training]] — PEFT is the primary practical technique for customizing pretrained models
- [[continual-learning]] — LoRA's parameter efficiency makes it ideal for sequential task adaptation without forgetting
- [[catastrophic-forgetting]] — frozen backbone + adapter preserves prior knowledge

### MoE Cluster
- [[mixture-of-experts]] — MoE + LoRA combines sparse computation with parameter-efficient adaptation; per-expert adapters are a natural fit
- [[wiki/sources/papers/moe-sieve-routing-guided-lora-for-efficient-moe-fine-tuning]] — recent research on routing-aware LoRA for MoE

### Optimization Cluster
- [[evolutionary-strategies]] — ES applied to PEFT rank allocation (EVOLORA family)
- [[essa]] — gradient-free alignment as alternative to PEFT's gradient-based adaptation

- [[qes]]
- [[bounded-memory-budget-optimization]]
- [[bounded-memory-budget-optimization]]
- [[qes]]
## LoRA Variants on the Frontier

Beyond the core methods, several research directions extend LoRA:

- **VeRA** (2024): Random projection matrices for further parameter reduction
- **LoRA-Quant**: Different rank for different weight bit-widths
- **SLoRA** (2024): Unified LoRA for multi-task serving via batched adapter execution
- **MoE LoRA**: Per-expert LoRA adapters for sparse MoE fine-tuning

## Strengths and Limitations

**Strengths:**
- Parameter efficient (0.1-1% trainable vs full fine-tune)
- Memory efficient (gradients only for adapters)
- Task-composable (multiple LoRA adapters per task)
- Mergable (no inference overhead after training)

**Limitations:**
- Low-rank bottleneck may not capture all task complexity
- Adapter interference in multi-adapter regimes
- Not all tasks benefit equally from PEFT vs full fine-tuning

## Connections
- [[scratchpad/jobs/reports/researcher/discovery-2026-07-15]]
- [[concepts/quantization]]
- [[concepts/bounded-memory-budget-optimization]]
- [[concepts/qes]]
- [[concepts/continual-learning]]
- [[scratchpad/agent-sheets/researcher/carryover]]
- [[wiki/index]]
- [[wiki/sources/papers/moe-sieve-routing-guided-lora-for-efficient-moe-fine-tuning]]
- [[scratchpad/jobs/reports/researcher/discovery-2026-07-20]]
- [[concepts/parameter-efficient-fine-tuning]]
- [[log]]
- [[concepts/fine-tuning]]
- [[concepts/qora]]
- [[concepts/lora]]
- [[parameter-efficient-fine-tuning]]

- [[lora]] — the foundational PEFT method
- [[fine-tuning]] — PEFT is a subset of fine-tuning (parameter-efficient variant)
- [[mixture-of-experts]] — MoE + LoRA is a natural combination
- [[wiki/sources/papers/moe-sieve-routing-guided-lora-for-efficient-moe-fine-tuning]] — routing-aware LoRA for MoE
- [[continual-learning]] — LoRA's parameter isolation is ideal for multi-task continual learning
- [[catastrophic-forgetting]] — frozen backbone preserves prior weights
- [[ml-evolution]] — ESSA and QES are alternative adaptation paradigms for the ml-evolution framework
- [[quantization]] — QLoRA combines 4-bit quantization with LoRA fine-tuning
- [[qora]] — dedicated QLoRA concept page: NF4 format, two-stage design, memory footprint comparison

## Open Questions

1. Does LoRA's low-rank constraint ultimately limit adaptation expressiveness at frontier model scales?
2. Can we learn adapter composition across tasks without expert-level meta-learning?
3. Optimal rank selection (r) remains ad hoc — is there a theoretical framework for choosing r given task complexity?
4. How does adapter interference manifest in simultaneous multi-task training, and what prevents it?
