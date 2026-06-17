---
title: "ReasonAlloc: Hierarchical Decoding-Time KV Cache Budget Allocation for Reasoning Models"
source: "https://www.alphaxiv.org/abs/2606.11164"
author:
  - "[[Wenhao Liu]]"
  - "[[Hao Shi]]"
  - "[[Yunhe Li]]"
  - "[[Weizhi Fei]]"
  - "[[Xiangyuan Wang]]"
  - "[[Mengzhe Ruan]]"
  - "[[Hanxu Hou]]"
  - "[[Peisong Wang]]"
  - "[[Linqi Song]]"
  - "[[Shuang Qiu]]"
published: 2026-06-09
created: 2026-06-12
description:
tags:
  - "clippings"
---
[TH](https://www.alphaxiv.org/@tyler-hall)

[Paper](https://www.alphaxiv.org/abs/2606.11164) [Blog](https://www.alphaxiv.org/overview/2606.11164) [Audio](https://www.alphaxiv.org/audio/2606.11164)

/ 23

ReasonAlloc: Hierarchical Decoding-Time KV  
Cache Budget Allocation for Reasoning Models  
Wenhao Liu 1,†, Hao Shi 1,†, Yunhe Li 2,†, Weizhi Fei 1, Xiangyuan Wang 3, Mengzhe Ruan 2, Hanxu  
Hou 4, Peisong Wang 5, Linqi Song 2, Shuang Qiu 2,B  
1 Tsinghua University 2 City University of Hong Kong 3 Peking University 4 Shenzhen University of  
Advanced Technology 5 Institute of Automation, Chinese Academy of Sciences  
Long chain-of-thought (CoT) trajectories in large language model (LLM) reasoning cause severe inference  
bottlenecks due to rapid key-value (KV) cache growth. Current decoding-time compression methods  
mitigate this issue via token eviction, but typically assume a uniform budget distribution across all  
layers and heads.In contrast, existing non-uniform budget allocation methods are predominantly  
designed for the static prompt prefill phase, and they do not capture the stepwise context demands of  
autoregressive reasoning. To bridge this gap, we propose ReasonAlloc, a training-free framework that  
recasts decoding-time KV compression as a hierarchical budget allocation problem.ReasonAlloc operates  
at two complementary levels: an offline layer-wise preallocation strategy captures an architecture-driven  
demand pattern which we call “ Reasoning Wave ”, while an online head-wise strategy reallocates resources  
during decoding to information-rich heads based on real-time utility. Evaluations on mathematical  
reasoning benchmarks (MATH-500, AIME 2024) using DeepSeek-R1-Distill-Llama-8B, DeepSeek-R1-  
Distill-Qwen-14B, and AceReason-14B show that ReasonAlloc outperforms uniform-budget R-KV, SnapKV,  
and Pyramid-RKV (a baseline enforcing a static, monotonically decreasing layer budget), with the largest  
gains at small budgets (128-512 tokens).ReasonAlloc is plug-and-play with existing token-eviction  
policies and introduces negligible inference-time overhead.  
Figure 1 | An overview of the proposed ReasonAlloc framework.Left (I):Layer-wise allocation  
strategy based on offline architecture calibration, demonstrating the non-linear “Reasoning Wave” KV  
demand across layers.Right (II):Head-wise allocation strategy that dynamically routes KV budgets  
to distinct attention heads based on real-time importance and redundancy scoring during decoding.  
† These authors contributed equally to this work.  
B Corresponding Author. Email:shuanqiu@cityu.edu.hk  
arXiv:2606.11164v1 \[cs.AI\] 9 Jun 2026

1\. Introduction  
Large reasoning models, particularly those leveraging reinforcement learning (RL) and chain-of-  
thought (CoT) prompting (Guo et al., 2025; Wei et al., 2022), perform well on complex inference  
tasks but often generate very long reasoning trajectories. The continuous accumulation of the key-  
value (KV) cache during decoding becomes a major memory bottleneck and reduces batch size and  
inference throughput (Fatemi et al., 2025). Decoding-time KV cache compression has therefore  
become an active research direction.  
Despite recent progress, existing decoding-time compression strategies (Cai et al., 2025; Zhang  
et al., 2025) share a common structural assumption: they treat the KV cache budget as uniformly  
distributed across layers and heads. These frameworks focus on which tokens to evict, but our empirical  
analysis (Section 4) shows that the effective KV demand is heterogeneous across layers and heads in  
reasoning models. To preserve a fraction 𝜌 of the attention mass, some layers and some attention  
heads require substantially more cache retention than others.  
While a separate line of work (Cai et al., 2024; Zhou et al., 2024) has explored non-uniform  
budget allocation, these methods are predominantly designed for the prompt prefilling stage. They  
rely on static mathematical heuristics (e.g., monotonic decay) and do not adapt to the step-by-step  
utility fluctuations of individual attention heads during autoregressive generation. When these static  
prefill-centric allocation rules are applied to the decoding phase, they can starve reasoning-critical  
pathways and lead to accuracy loss, as we show with our Pyramid-RKV baseline.  
We therefore frame decoding-time KV compression as a hierarchical resource allocation problem:  
before an underlying policy evicts tokens, the system first determines per-layer budgets (layer-  
wise allocation) and then routes the budgets across heads (head-wise allocation) based on online  
decoding-time utility.  
Motivated by this, we propose ReasonAlloc, a plug-and-play framework that is orthogonal to the  
underlying token-scoring mechanism and can wrap most decoding-time eviction policies. Our main  
contributions are:  
• We characterize the heterogeneity of KV cache demand in distilled reasoning LLMs and show that  
uniform or naively static allocations create a bottleneck for long-context decoding.  
• We propose ReasonAlloc (Figure 1), a training-free hierarchical allocator that combines offline  
calibration of a model’s approximately task-invariant layer-wise demand (the “Reasoning Wave”)  
with an online head-wise router that captures decoding-time utility fluctuations.  
• On MATH-500 and AIME 2024, using DeepSeek-R1-Distill-Llama-8B and DeepSeek-R1-Distill-  
Qwen-14B (hereafter R1-Llama-8B and R1-Qwen-14B), along with AceReason-14B,ReasonAlloc  
surpasses both uniform-budget and fixed non-uniform allocation baselines at the same compression  
ratios, with the largest gains at small budgets, while adding negligible inference-time overhead.  
2\. Related Work  
KV Cache Compression.Existing KV cache optimization methods include token eviction, quan-  
tization, token merging, and low-rank compression (Chang et al., 2024; Fei et al., 2024, 2026;  
Hooper et al., 2024; Li et al., 2024; Liu et al., 2024; Zhang et al., 2023). Among eviction-based  
methods, SnapKV (Li et al., 2024) ranks tokens using attention-derived importance, while methods  
like H 2 O (Zhang et al., 2023) and StreamingLLM (Xiao et al., 2023) focus on decoding-time retention  
patterns. R-KV (Cai et al., 2025) further proposes joint importance-redundancy scoring to improve  
selection for reasoning-heavy generation.  
2

Highlight & Ask

Select any part of the paper to ask specific questions

Add Context

Type @ to reference other papers and expand the discussion

Additional

•

• See how others cite this work

• Literature reviews

• Community context

Try asking "What's the intuition behind section 3.2?"