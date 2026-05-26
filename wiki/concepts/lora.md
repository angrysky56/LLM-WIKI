---
created: 2026-06-17
updated: 2026-07-21
type: concept
summary: LoRA — Low-Rank Adaptation — parameter-efficient fine-tuning method using rank-decomposition matrices to adapt large models with minimal trainable parameters
tags: [fine-tuning, parameter-efficient-fine-tuning, llm-training, low-rank, adapter, peft]
sources: []
status: active
confidence: 0.8
---

# LoRA

## Definition

LoRA (Low-Rank Adaptation), introduced by Hu et al. (2021), is a parameter-efficient fine-tuning method that adapts large language models by learning a pair of small rank-decomposition matrices while keeping the pretrained weights frozen.

The key insight: when a pre-trained model is fine-tuned for a new task, the weight update ΔW is often low-rank — it can be well-approximated by a low-rank product of two smaller matrices. Rather than updating W directly, LoRA learns the decomposition W + BA where B ∈ ℝ^(d×r), A ∈ ℝ^(r×k), and r << min(d, k).

## Mechanism

For a pre-trained frozen weight matrix W₀ ∈ ℝ^(d×k), LoRA represents the weight update as:

```
W = W₀ + BA
```

Where:
- B ∈ ℝ^(d×r) — trainable
- A ∈ ℝ^(r×k) — trainable  
- r = rank, typically 4–64 (vs d×k for full matrix)

During forward pass, both W₀ and BA are computed, but gradients only flow through BA. Only the low-rank matrices are trained — W₀ remains frozen.

The trainable parameter count is (d + k) × r, vs d × k for full fine-tuning. For a 7B parameter model with hidden dimension 4096:
- Full fine-tune: ~16B trainable parameters
- LoRA (r=8): ~4M trainable parameters (~4000× reduction)

## Rank Selection

The rank r is the primary hyperparameter controlling the capacity of adaptation:

| Rank | Approx. params (7B model) | Typical use |
|------|---------------------------|-------------|
| 2–4 | ~1–2M | Minimal change, fast adaptation |
| 8–16 | ~4–8M | Balanced; most common choice |
| 32–64 | ~16–32M | High-capacity adaptation |
| 128+ | ~65M+ | Approaches full fine-tune |

Lower ranks are more parameter-efficient but may underfit complex tasks. Higher ranks approach full fine-tuning behavior but lose parameter efficiency benefits.

## Variants

- **LoRA+** (Hayou et al., 2024): Different learning rates for A and B matrices; stabilizes training
- **QLoRA** (Dettmers et al., 2023): Quantized base model (4-bit) + LoRA fine-tuning — enables fine-tuning on consumer GPUs
- **AdaLoRA** (Zhang et al., 2023): Adaptive rank allocation — redistribute rank budget based on importance scores
- **DoRA** (Liu et al., 2024): Weight-decomposed LoRA — separates magnitude and direction updates
- **LoRA-FA** (LoRA with Factorized attention): Apply LoRA to attention and MLP layers separately

## Relationship to Other PEFT Methods

LoRA is the most widely used PEFT method, but it's one approach in a larger family:

- **Adapter-based**: Add small bottleneck layers within the transformer (different from LoRA's additive approach)
- **Prefix tuning**: Prepend trainable token embeddings to each layer ( LoRA modifies weight matrices; prefix modifies embeddings)
- **Prompt tuning**: Train soft prompts at the input level (even fewer parameters than LoRA)

LoRA occupies a middle ground: more parameter-efficient than full fine-tuning while being more expressive than prompt-based approaches.

## Connection to MoE Fine-Tuning

LoRA combines naturally with Mixture of Experts architectures. The MoE router already selects which experts to activate — applying LoRA to MoE models allows task-specific adaptation without modifying the shared expert weights. This is particularly valuable for multi-task or multi-domain scenarios where different tasks benefit from different adaptation patterns.

## Open Questions

1. **Rank selection principles**: How should rank be chosen for a given task? Current practice is empirical — theoretical guidance is limited.

2. **What does LoRA actually learn?**: Empirical studies show LoRA often learns similar representations to full fine-tuning, but the mechanism isn't fully understood. Why does low-rank capture task-relevant directions so effectively?

3. **LoRA vs. full fine-tuning ceiling**: For very large models, does LoRA eventually hit a ceiling that full fine-tuning doesn't? Evidence suggests at extreme scale, even LoRA-adapter approaches may need selective full fine-tuning.

4. **Combining multiple LoRA adapters**: How should multiple task-specific LoRA adapters be composed at inference time? Weighting schemes, routing, or merging strategies?

## Connections

- [[parameter-efficient-fine-tuning]]: the broader category LoRA belongs to
- [[fine-tuning]]: LoRA is a fine-tuning method; fine-tuning.md covers the general fine-tuning landscape
- [[qora|QLoRA]]: the quantized variant that enables 4-bit base model fine-tuning
- [[mixture-of-experts]]: MoE + LoRA is a natural combination for multi-task adaptation
- [[catastrophic-forgetting]]: LoRA's parameter efficiency reduces the risk of forgetting by keeping most weights frozen
- [[llm-training]]: LoRA is primarily used during the LLM training/fine-tuning phase
- [[control-llm]]: architectural alternative to LoRA for task adaptation — Control LLM uses structural separation vs LoRA's low-rank decomposition
- [[continual-learning]]: LoRA can be used as a continual learning tool — one LoRA adapter per task, combined via meta-learning or routing