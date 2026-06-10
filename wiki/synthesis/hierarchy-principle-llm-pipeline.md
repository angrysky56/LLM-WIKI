---
summary: Cross-paper synthesis: three June 2026 papers independently challenge uniform assumptions in the LLM pipeline (SFT training, KV cache allocation, behavioral steering) and replace them with hierarchical allocation.
tags: [synthesis, arxiv, cross-paper, hierarchy, uniform-assumptions, LLM-pipeline, reasoning-models]
updated: 2026-06-10T17:29:56Z
created: 2026-06-10T17:29:56Z
---

# The Hierarchy Principle: Replacing Uniform Assumptions in the LLM Pipeline

A cross-paper synthesis connecting three papers from the June 9, 2026 arXiv submission batch.

## The Pattern

All three papers challenge a **uniform/one-size-fits-all assumption** at different stages of the LLM pipeline and replace it with a **structured, hierarchical allocation** approach:

| Pipeline Stage | Uniform Assumption | Hierarchical Replacement | Paper |
|---------------|-------------------|------------------------|-------|
| **Training (SFT)** | Every token equally valid as a one-hot target | Per-token allocation of confidence (γt) and alternative probability mass (˜πt) | [[target-sft-unifying-lens]] |
| **Inference (KV Cache)** | Equal KV budget across all layers and heads | Layer-wise "Reasoning Wave" preallocation + head-wise real-time reallocation | [[reasonalloc-kv-cache-allocation]] |
| **Control (Steering)** | Detection features (for past text) also work for future behavior | Separate prediction features for future behavior steerability + sentence-level selection | [[future-probes-steering]] |

## The Meta-Insight

The LLM pipeline — from training data design to inference serving to behavioral control — has been built on convenience assumptions: treat everything uniformly, allocate resources equally, and let optimization or scale handle the rest. These three papers independently converge on the same corrective insight: **optimal performance requires non-uniform, hierarchical allocation that respects the structure of the problem**:

1. **Training**: Not all tokens deserve equal weight — the model's confidence and the token's information content should determine how strongly we imitate it
2. **Inference**: Not all layers and heads have equal KV demands — architecture-specific "waves" and real-time head importance should drive allocation
3. **Control**: Not all internal features are equally useful for steering — detection and prediction features serve different purposes, and using the right one for the right job avoids quality degradation

This "hierarchy principle" may generalize beyond these three papers: any stage of the LLM pipeline that currently assumes uniformity is a candidate for structured allocation.

## Connections

- This synthesis lives at [[wiki/synthesis/hierarchy-principle-llm-pipeline]]
- Connects to [[RREDCoT]] which also questions per-token optimization in reward settings
- Related to [[PC-Layer]] on non-uniform training optimization
