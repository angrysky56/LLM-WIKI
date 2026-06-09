---
title: Inference-Time Intervention: Eliciting Truthful Answers from a Language Model
source: https://arxiv.org/abs/2306.03341
created: 2026-06-09T09:08:48Z
tags: [clippings]
---

## Title:Inference-Time Intervention: Eliciting Truthful Answers from a Language Model

[View PDF](https://arxiv.org/pdf/2306.03341) [HTML (experimental)](https://arxiv.org/html/2306.03341v6)

> Abstract:We introduce Inference-Time Intervention (ITI), a technique designed to enhance the "truthfulness" of large language models (LLMs). ITI operates by shifting model activations during inference, following a set of directions across a limited number of attention heads. This intervention significantly improves the performance of LLaMA models on the TruthfulQA benchmark. On an instruction-finetuned LLaMA called Alpaca, ITI improves its truthfulness from 32.5% to 65.1%. We identify a tradeoff between truthfulness and helpfulness and demonstrate how to balance it by tuning the intervention strength. ITI is minimally invasive and computationally inexpensive. Moreover, the technique is data efficient: while approaches like RLHF require extensive annotations, ITI locates truthful directions using only few hundred examples. Our findings suggest that LLMs may have an internal representation of the likelihood of something being true, even as they produce falsehoods on the surface.

| Comments: |
| --- |
| Subjects: | Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Computation and Language (cs.CL) |
| Cite as: | [arXiv:2306.03341](https://arxiv.org/abs/2306.03341) \[cs.LG\] |
|  | (or [arXiv:2306.03341v6](https://arxiv.org/abs/2306.03341v6) \[cs.LG\] for this version) |
|  | [https://doi.org/10.48550/arXiv.2306.03341](https://doi.org/10.48550/arXiv.2306.03341) |

## Submission history

From: Kenneth Li \[[view email](https://arxiv.org/show-email/38a47004/2306.03341)\]  
**[\[v1\]](https://arxiv.org/abs/2306.03341v1)** Tue, 6 Jun 2023 01:26:53 UTC (1,677 KB)  
**[\[v2\]](https://arxiv.org/abs/2306.03341v2)** Wed, 7 Jun 2023 00:27:45 UTC (1,677 KB)  
**[\[v3\]](https://arxiv.org/abs/2306.03341v3)** Fri, 21 Jul 2023 19:11:58 UTC (1,676 KB)  
**[\[v4\]](https://arxiv.org/abs/2306.03341v4)** Thu, 21 Sep 2023 23:38:08 UTC (1,678 KB)  
**[\[v5\]](https://arxiv.org/abs/2306.03341v5)** Fri, 20 Oct 2023 01:37:21 UTC (1,677 KB)  
**\[v6\]** Wed, 26 Jun 2024 14:11:53 UTC (1,991 KB)  

[Which authors of this paper are endorsers?](https://arxiv.org/auth/show-endorsers/2306.03341) | Disable MathJax ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))