---
summary: Introduces ReasonAlloc, a training-free hierarchical KV cache budget allocator for reasoning models that combines offline layer-wise preallocation (capturing the "Reasoning Wave" pattern) with online head-wise reallocation.
tags: [arxiv, paper, KV-cache, inference, reasoning-models, LRM, attention, compression]
updated: 2026-06-10T17:29:37Z
created: 2026-06-10T17:29:37Z
---

# ReasonAlloc: Hierarchical Decoding-Time KV Cache Budget Allocation for Reasoning Models

**Authors:** Wenhao Liu, Hao Shi, Yunhe Li, Weizhi Fei, Xiangyuan Wang, Mengzhe Ruan, Hanxu Hou, Peisong Wang, Linqi Song, Shuang Qiu (Tsinghua University, City University of Hong Kong, Peking University)

**arXiv:** 2606.11164v1, 9 Jun 2026

## Problem

Long chain-of-thought (CoT) trajectories in large reasoning models (LRMs) cause severe inference bottlenecks due to rapid KV cache growth. Current decoding-time compression methods (token eviction) assume a **uniform budget distribution** across all layers and heads. Non-uniform budget allocation methods exist but are designed for the static prompt prefill phase — they do not capture the stepwise context demands of autoregressive reasoning. The fundamental mismatch: reasoning models generate long, variable-length CoT sequences where different layers and heads have dramatically different KV cache demands.

## Method

ReasonAlloc is a **training-free** framework that recasts decoding-time KV compression as a **hierarchical budget allocation problem** operating at two complementary levels:

### Level I: Offline Layer-wise Preallocation
The paper discovers a **"Reasoning Wave"** pattern — a stable, architecture-driven non-linear KV demand curve across layers. Each model architecture exhibits a characteristic demand pattern:
- **R1-Llama-8B**: Overwhelming initial spike in early layers
- **R1-Qwen-14B**: Bimodal distribution with dips and peaks
These patterns are highly stable across tasks for the same model but diverge substantially across architectures. ReasonAlloc uses a lightweight offline calibration run to establish preallocated per-layer budgets.

### Level II: Online Head-wise Reallocation
During decoding, head-level utility fluctuates even within a fixed layer budget. ReasonAlloc dynamically routes KV budgets to information-rich heads based on real-time importance and redundancy scoring (based on accumulated attention patterns). A normalization technique handles the instability of raw importance scores.

## Key Findings

1. **Consistent outperformance**: ReasonAlloc outperforms uniform-budget R-KV (the current SOTA decoding-time eviction method) and Pyramid-RKV (a static non-uniform baseline) across all cache budgets on MATH-500 and AIME 2024
2. **Largest gains at small budgets**: 128-512 token budgets show the biggest improvements — precisely where reasoning model inference is most bottlenecked
3. **The "Reasoning Wave" is real**: Layer-wise KV demand follows a stable, architecture-specific pattern that can be pre-calibrated offline — no online layer profiling needed
4. **Plug-and-play**: ReasonAlloc is compatible with existing token-eviction policies (R-KV, SnapKV) and introduces negligible inference overhead
5. **Ablation validates both levels**: Decomposing ReasonAlloc shows that both the layer-wise preallocation and head-wise reallocation contribute independently to performance

## Limitations

- The "Reasoning Wave" pattern is characterized only for mathematical reasoning — it's unclear if it holds for other reasoning domains
- Evaluation uses three specific reasoning model families (DeepSeek-R1 variants, AceReason-14B)
- Offline calibration requires one forward pass per architecture, which may be impractical for rapidly evolving model families
- The approach targets decoding-time eviction only — doesn't address prompt-phase compression or KV cache quantization

## Connections

- Directly complements [[future-probes-steering]] (2606.11172v1) — both tackle reasoning model inference from different angles (efficiency vs. control)
- Extends the KV cache compression literature (R-KV, SnapKV, Pyramid-RKV, H2O, StreamingLLM) by introducing hierarchical allocation
- Related to [[PC-Layer]] (2606.06470v1) on training efficiency — both question uniform resource allocation assumptions in LLM pipelines
- Relevant to practical deployment of reasoning models — addresses the specific bottleneck that makes LRMs expensive to serve

## Key Quote

> "Current decoding-time compression methods treat the KV cache budget uniformly across all layers and heads — but reasoning models exhibit a stable, architecture-driven 'Reasoning Wave' pattern that demands non-uniform allocation."

## References

- Liu et al. (2026). ReasonAlloc: Hierarchical Decoding-Time KV Cache Budget Allocation for Reasoning Models. arXiv:2606.11164v1.
