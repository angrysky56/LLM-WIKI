---
summary: Comprehensive PEFT survey — taxonomy of 50+ methods, experimental comparison at 11B scale, and practical deployment recommendations
tags: [fine-tuning, peft, lora, adapters, parameter-efficient]
updated: 2026-06-05T21:06:44Z
created: 2026-06-05T21:06:44Z
---

---
created: 2026-06-05
updated: 2026-06-05
type: source
summary: Lialin et al. — comprehensive survey of 50+ PEFT methods, taxonomy, experimental comparison at 11B scale, and practical recommendations
tags: [fine-tuning, peft, lora, adapters, parameter-efficient]
sources: https://arxiv.org/abs/2303.15647
status: active
confidence: 0.95
---

# Scaling Down to Scale Up: A Guide to Parameter-Efficient Fine-Tuning

**Authors:** Vladislav Lialin, Namrata Shivagunde, Sherin Muckatira, Anna Rumshisky

**Published:** March 2023 (arXiv:2303.15647), updated November 2024

## Summary

A systematic survey of parameter-efficient fine-tuning (PEFT) methods covering over 50 papers from early 2019 to mid-2024. The paper provides:

1. **Taxonomy** of PEFT methods organized by approach
2. **Head-to-head experimental comparison** of 15 diverse PEFT methods on models up to 11B parameters
3. **Practical recommendations** for real-world PEFT deployment

## Key Findings

- **LoRA remains the strongest practical baseline**: Methods that claimed to surpass LoRA in prior work often fail under resource-constrained settings (limited hyperparameter optimization, few training epochs)
- **The gap between LoRA and full fine-tuning is architecture-dependent**: For some tasks, LoRA matches full fine-tuning; for others, the gap is substantial
- **Hyperparameter sensitivity**: PEFT methods are highly sensitive to rank, target modules, and learning rate — fair comparison requires extensive tuning
- **Efficiency ≠ effectiveness**: The most compute-efficient methods (e.g., prompt tuning) are often the least effective on complex tasks

## Taxonomy

The survey organizes PEFT into:

- **Adapter-based methods**: Small bottleneck layers inserted between transformer layers
- **Low-rank methods**: LoRA, its variants (DoRA, rsLoRA, PiSSA), and Kronecker-based approaches
- **Prompt-based methods**: Prompt tuning, prefix tuning, p-tuning
- **Sparse fine-tuning**: Diff pruning, lottery ticket, fish mask
- **Reparameterization methods**: Intrinsic SAID, Compacter

## Evidence Quality

The paper's head-to-head comparison is a significant contribution — most PEFT papers evaluate only a few methods on limited benchmarks. The 11B-scale comparison with controlled hyperparameters provides reliable relative rankings. However, findings are limited to English-language text tasks; multimodal and code tasks not covered.

## Wiki Connections

- [[fine-tuning]] — the broader concept this source feeds into
- [[parameter-efficient-fine-tuning]] — the sub-concept this survey directly addresses
- [[lora]] — the dominant PEFT method
- [[instruction-tuning]] — a specific PEFT application (archived into fine-tuning)
- [[transfer-learning]] — the theoretical foundation
