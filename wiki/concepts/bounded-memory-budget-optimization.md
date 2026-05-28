---
summary: Bounded memory budget optimization theme covering QES saturation, ESSA spectral alignment, and LLaMA-NAS compression
tags: [memory-efficiency, quantization, neural-architecture-search, evolutionary-strategies, ml-evolution, compression]
updated: 2026-05-27T05:45:20Z
created: 2026-05-27T05:45:20Z
---

# Bounded Memory Budget Optimization

## What It Is

A design principle and research theme in LLM optimization where memory capacity is treated as a fixed, non-expandable budget — not a problem to be solved with more hardware, but a constraint to design around. Methods in this cluster accept the budget as given and discover how to get the most utility within it, rather than trying to exceed the budget or make it larger.

The theme connects three otherwise distinct methods — QES, ESSA, and LLaMA-NAS — which all navigate the same fundamental tension: model capability expectations keep rising while the memory available for inference and training remains bounded by hardware and deployment constraints.

## Memory Capacity as a Bounded Resource

Modern LLMs are expected to perform complex reasoning, follow instructions, and maintain long context — all within GPU memory that may be fixed by the deployment hardware. This isn't a limitation unique to edge deployment; even datacenter budgets are bounded by GPU count, bandwidth, and interconnect topology.

The bounded-memory framing reframes the problem: instead of asking "how do we fit more model into memory?" (scaling up), it asks "how do we get more capability out of the memory we already have?" (optimizing down). This shift has productive consequences:

- **Saturation effects**: Adding more parameters stops helping when memory is saturated; efficiency matters more than raw size
- **Architecture awareness**: Memory constraints shape which architectural choices are viable
- **Search over training**: When memory is fixed, searching over model variants (architecture, quantization level, residual corrections) can outperform training the same model longer

Three methods in the wiki illustrate distinct strategies within this bounded regime.

## QES: Saturation Effects in Quantized Fine-Tuning

[[qes|QES (Quality-Evolutionary Search)]] operates directly in the quantized weight space, where memory is already saturated relative to full-precision training. The method encounters saturation in a specific form: at low bit-widths (4-bit and below), quantization error accumulates and saturates the residual correction space, such that further quantization produces diminishing returns for the error-feedback search.

The saturation effect manifests as follows: when a model is quantized to 2-bit or lower, the quantization residuals become so large and unstructured that evolutionary search over the residual space cannot reliably find corrective mutations — the "signal" (structured residual) is overwhelmed by "noise" (random quantization error). QES works well in the 4-bit regime where residuals still carry predictable structure; below that threshold, quality recovery diminishes rapidly.

This means QES occupies a bounded region of the quality-memory tradeoff curve — not the lowest memory point, but the point where memory savings are maximal while saturation effects remain manageable. The method is explicitly designed for inference-level memory budgets, meaning the fine-tuning process lives entirely in quantized form and never lifts back to float16.

## ESSA: Evolutionary Score Alignment Under Memory Constraints

[[essa|ESSA (Evolutionary Score-based Singular-value Alignment)]] approaches memory constraints differently: it constrains the search space itself to be memory-efficient, rather than operating in a memory-constrained representation.

ESSA's singular value decomposition targets the spectral structure of weight matrices, which has a natural connection to memory efficiency: low-rank approximations of weight matrices (keeping only the largest singular values) are both memory-efficient and information-efficient. By mutating the spectrum rather than individual weights, ESSA implicitly searches in a compressed representation — the mutation operates on O(r) parameters where r is the rank of the approximation, not O(n²) for the full weight matrix.

Under memory constraints, ESSA's spectral mutations are more sample-efficient than unstructured weight mutations because they concentrate evolutionary search on the directions that actually matter for model behavior. This makes ESSA particularly well-suited to memory-budget-constrained settings where each fitness evaluation must be informative — you can't afford to waste evaluations on parameter directions that don't affect the outcome.

The method scales 6x faster than gradient-based alignment on 128 GPUs because the population evaluations are independent and memory-efficient: each candidate is a weight snapshot, not a gradient computation, and the SVD operations are memory-bound rather than compute-bound at scale.

## LLaMA-NAS: Memory-Aware Architecture Search

[[llama-nas|LLaMA-NAS]] treats memory constraints as an architectural design criterion from the start. Rather than taking a fixed model architecture and optimizing within it, LLaMA-NAS searches over architectures specifically to find sub-networks that fit a target memory budget while preserving task-relevant capability.

The one-shot search mechanism is itself a memory-efficiency strategy: by inheriting pretrained weights rather than training candidate architectures from scratch, LLaMA-NAS avoids the memory cost of training many candidates. This is critical when memory is the limiting factor — you can't afford to train 100 architecture variants when each training run requires GPU memory for the full model.

LLaMA-NAS discovers that for many tasks, the memory budget is saturated not because the model is too small, but because the architecture is wrong for the task. A sub-network sized at 40% of the parent model's memory footprint can match or exceed the parent on a specific task if the architecture is tailored to that task's computational pattern.

The compression achieved is a side effect of architecture search constrained by memory budget — not a primary goal. The memory constraint is the search boundary, not the optimization target.

## Shared Themes Across the Three Methods

| Property | QES | ESSA | LLaMA-NAS |
|----------|-----|------|-----------|
| Memory constraint handled via | Quantized representation | Low-rank spectral mutations | Architecture search |
| Saturation mechanism | Residual noise at extreme quantization | Spectral collapse from over-focused mutations | Sub-network underfitting for general capability |
| Search strategy | Evolutionary (CMA-ES over residuals) | Evolutionary (CMA-ES over spectrum) | One-shot inheritance |
| What saturates | Error feedback signal | Singular value diversity | Task-relevant parameter coverage |
| Memory efficiency achieved by | Never lifting to full precision | Compressing the search space | Compressing the architecture |

All three share the core insight: when memory is fixed, the search over model variants (residual corrections, spectral perturbations, sub-network architectures) can outperform continued training of a single model. The bounded budget transforms from limitation to inductive bias — it forces the method to discover what actually matters for the task, rather than just training longer on everything.

## Connections
- [[concepts/bounded-memory-budget-optimization]]
- [[scratchpad/agent-sheets/researcher/carryover]]
- [[index]]
- [[log]]
- [[bounded-memory-budget-optimization]]

- [[qes]] — quantized fine-tuning with error feedback; saturation at extreme bit-widths
- [[essa]] — gradient-free alignment via spectral mutations; memory-efficient search
- [[llama-nas]] — one-shot architecture search within a memory budget
- [[neural-architecture-search]] — LLaMA-NAS as memory-constrained NAS; ESSA's spectral approach as analogy
- [[ml-evolution]] — all three are guided evolution methods operating under bounded resources
- [[parameter-efficient-fine-tuning]] — all three reduce the memory footprint of model adaptation
- [[compression]] — LLaMA-NAS achieves compression via architecture; QES enables compression-friendly fine-tuning
- [[lora]] — complementary: LoRA adapts weights within a fixed architecture; the bounded-memory methods search over architecture and representation

## Open Questions

1. **Optimal budget allocation**: Is there a principled way to allocate a fixed memory budget across architecture (LLaMA-NAS), representation (QES), and alignment (ESSA) — or do these compose sequentially?

2. **Saturation thresholds**: Each method has a saturation point (QES at ~2-bit, ESSA on spectrum collapse, LLaMA-NAS on sub-network size). Can these thresholds be predicted from the underlying model properties, and can the methods be adapted to push the threshold lower?

3. **Composability**: Could LLaMA-NAS find a memory-efficient architecture, which is then fine-tuned with QES under continued memory constraint? Does the order of application matter?

4. **Memory vs compute tradeoff**: All three optimize for memory efficiency, but compute efficiency is also bounded. Are there regimes where the memory-bounded methods actually increase compute (e.g., QES's multiple evolutionary passes) — and if so, when is the tradeoff worth it?

5. **Beyond saturation as failure**: The theme treats saturation as a limitation, but could saturation effects be harnessed as a signal? If a method saturates quickly, does that indicate the memory budget is well-matched to the task?
