---
title: MoE-Sieve: Routing-Guided LoRA for Efficient MoE Fine-Tuning
source: https://arxiv.org/abs/2603.24044
created: 2026-05-25T17:37:22Z
tags: [clippings]
---

## Title:MoE-Sieve: Routing-Guided LoRA for Efficient MoE Fine-Tuning

Authors:[Andrea Manzoni](https://arxiv.org/search/cs?searchtype=author&query=Manzoni,+A)

[View PDF](https://arxiv.org/pdf/2603.24044) [HTML (experimental)](https://arxiv.org/html/2603.24044v1)

> Abstract:Standard LoRA fine-tuning of Mixture-of-Experts (MoE) models applies adapters to every expert, yet our profiling shows that per-layer expert routing is highly skewed: a small subset of experts handles most tokens in each layer, while many others are rarely activated ("cold"). We propose MoE-Sieve, a simple routing-guided framework for LoRA fine-tuning, and pair it with a systematic profiling study of expert routing across architectures and tasks. The method is simple: profile routing counts on a small calibration set, select the top-k most-routed experts per layer, and apply LoRA only to those experts. Across two architecturally distinct MoE models and three diverse tasks, tuning only the top 25% routed experts per layer remains competitive with full LoRA, with mean differences within +/-1 percentage point across all conditions. This reduces LoRA trainable parameters by 70-73%, adapter checkpoint size by 71-73%, and wall-clock training time by up to 50%. We also observe a non-monotonic relationship between expert count and seed-to-seed variance, consistent with the hypothesis that adapting cold experts can introduce gradient noise without improving accuracy. Further ablations show that random expert selection at matched budget is about 2.5 percentage points worse, indicating that the routing signal matters, while greedy per-layer budget optimization does not improve over uniform top-k.

| Comments: |
| --- |
| Subjects: | Machine Learning (cs.LG); Computation and Language (cs.CL) |
| Cite as: | [arXiv:2603.24044](https://arxiv.org/abs/2603.24044) \[cs.LG\] |
|  | (or [arXiv:2603.24044v1](https://arxiv.org/abs/2603.24044v1) \[cs.LG\] for this version) |
|  | [https://doi.org/10.48550/arXiv.2603.24044](https://doi.org/10.48550/arXiv.2603.24044) |

## Submission history

From: Andrea Manzoni \[[view email](https://arxiv.org/show-email/46912ae7/2603.24044)\]  
**\[v1\]** Wed, 25 Mar 2026 07:53:09 UTC (143 KB)  

[Which authors of this paper are endorsers?](https://arxiv.org/auth/show-endorsers/2603.24044) | Disable MathJax ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))