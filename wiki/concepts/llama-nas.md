---
created: 2026-05-23T08:50:00Z
updated: 2026-08-03
type: concept
summary: LLaMA-NAS — one-shot neural architecture search for task-specific sub-networks within the LLaMA model family; achieves compression and throughput gains via inherited pretrained weights
tags: [neural-architecture-search, ml-evolution, architecture-discovery, one-shot-nas, compression, llama]
sources: wiki/sources/articles/ml-evolution-benchmarking-protocol.md
status: active
confidence: 0.7
---

# LLaMA-NAS

## What It Is

LLaMA-NAS applies neural architecture search to the LLaMA model family to discover efficient task-specific sub-networks. Rather than searching the full architecture space from scratch, it starts from a pretrained LLaMA model andprunes or restructures it for a target task — achieving compression and throughput gains simultaneously without full retraining.

The key distinction from other NAS methods in the ml-evolution cluster:
- **CoLLM-NAS**: Uses dual-LLM guidance to explore architecture candidates
- **RZ-NAS**: Uses zero-cost proxies to evaluate candidates without training
- **LLaMA-NAS**: Inherits pretrained weights from the LLaMA family and performs one-shot sub-network search

## Mechanism

LLaMA-NAS operates on the insight that frontier models like LLaMA are heavily over-parameterized for many downstream tasks. Rather than fine-tuning the full model, LLaMA-NAS searches for a sparse sub-network that preserves task-relevant capabilities while removing task-agnostic parameters.

**One-shot search**: The sub-network inherits weights directly from the pretrained parent — no per-candidate training required. This is enabled by the observation that pretraining produces diverse capability representations across the model's parameters, and a carefully chosen sub-network can preserve most of the useful capabilities for a given task.

**Task-specific specialization**: The search is directed at a target task, meaning the discovered sub-network is optimized for that task's performance, not general language modeling. This is what differentiates LLaMA-NAS from generic model compression.

## Relationship to Model Compression

LLaMA-NAS is part of the broader model compression landscape:

| Method | Mechanism | Retraining Required |
|--------|-----------|---------------------|
| Pruning | Remove weights/neurons | Minimal or none |
| Quantization | Reduce weight precision | None post-quantization |
| Knowledge distillation | Train smaller model on larger | Full distillation |
| LLaMA-NAS | Search for task sub-network | One-shot (no training) |

Unlike standard pruning, LLaMA-NAS searches over architecture configurations — which layers to keep, how to route through attention heads, whether to use MoE-style expert selection — rather than simply zeroing weights.

## Connections to ML Evolution Cluster

LLaMA-NAS is one of three NAS methods documented in the ml-evolution benchmarking protocol:

- [[ml-evolution-benchmarking-protocol]] — primary source
- [[neural-architecture-search]] — LLaMA-NAS as a specific NAS method
- [[collm-nas]] — complementary: LLM-guided exploration vs one-shot inheritance
- [[rz-nas]] — complementary: zero-cost proxy evaluation vs weight inheritance
- [[essa]] — analogous philosophy: gradient-free evaluation (ESSA uses singular values; LLaMA-NAS uses one-shot inheritance)
- [[qes]] — analogous philosophy: avoiding full training cost via specialized approximation

- [[bounded-memory-budget-optimization]]
- [[ml-evolution]]
- [[bounded-memory-budget-optimization]]
## Connections Beyond ML Evolution

- [[compression]] — LLaMA-NAS achieves compression as a side effect of architecture search
- [[scaling-laws]] — discovered architectures must be evaluated relative to compute budget; one-shot search respects scaling constraints
- [[catastrophic-forgetting]] — sub-network search can implicitly preserve prior capabilities by selecting architecture paths that retain important representations
- [[lora]] — LoRA and LLaMA-NAS are complementary: LLaMA-NAS finds the right architecture; LoRA adapts the remaining parameters efficiently

## Related
- [[concepts/ml-evolution]]
- [[scratchpad/agent-sheets/researcher/carryover]]
- [[wiki/index]]
- [[concepts/llama-nas]]
- [[concepts/collm-nas]]
- [[log]]
- [[scratchpad/jobs/reports/researcher/discovery-2026-08-03]]
- [[concepts/neural-architecture-search]]
- [[scratchpad/jobs/reports/researcher/discovery-2026-07-15]]
- [[concepts/bounded-memory-budget-optimization]]
- [[sources/articles/ml-evolution-benchmarking-protocol]]

- [[llama-nas]]

## Open Questions

1. **One-shot validity**: How well does a sub-network inherit capabilities from the parent? Does the quality of pretraining affect how well sub-networks generalize?

2. **Architecture vs weight importance**: LLaMA-NAS changes architecture; does this interact differently with continued pretraining than weight-level adaptations like LoRA?

3. **Cross-task sub-networks**: Can a single architecture discovered for task A be efficiently adapted for task B via LoRA? Is the architecture specialization complementary to parameter-efficient fine-tuning?

4. **Scaling to frontier**: LLaMA-NAS was demonstrated on LLaMA-scale models. Do the compression gains hold at GPT-4/Claude scale, or does one-shot evaluation become unreliable at extreme scale?