---
title: OpenDeepThink: Parallel Reasoning via Bradley--Terry Aggregation
source: https://arxiv.org/abs/2605.15177
created: 2026-05-17T18:06:10Z
tags: [clippings]
---

## Title:OpenDeepThink: Parallel Reasoning via Bradley--Terry Aggregation

Authors:[Shang Zhou](https://arxiv.org/search/cs?searchtype=author&query=Zhou,+S), [Wenhao Chai](https://arxiv.org/search/cs?searchtype=author&query=Chai,+W), [Kaiyuan Liu](https://arxiv.org/search/cs?searchtype=author&query=Liu,+K), [Huanzhi Mao](https://arxiv.org/search/cs?searchtype=author&query=Mao,+H), [Qiuyang Mang](https://arxiv.org/search/cs?searchtype=author&query=Mang,+Q), [Jingbo Shang](https://arxiv.org/search/cs?searchtype=author&query=Shang,+J)

[View PDF](https://arxiv.org/pdf/2605.15177) [HTML (experimental)](https://arxiv.org/html/2605.15177v1)

> Abstract:Test-time compute scaling is a primary axis for improving LLM reasoning. Existing methods primarily scale depth by extending a single reasoning trace. Scaling breadth by sampling multiple candidates in parallel is straightforward, but introduces a selection bottleneck: choosing the best candidate without a ground-truth verifier, since pointwise LLM judging is noisy and biased. To address this, we introduce OpenDeepThink, a population-based test-time compute framework that selects via pairwise Bradley-Terry comparison. Each generation, the LLM judges random pairs of candidates and aggregates votes via Bradley-Terry into a global ranking; top-ranked candidates are preserved and the top three quarters are mutated using the natural-language critiques produced during comparison; the bottom quarter is discarded. OpenDeepThink raises Gemini 3.1 Pro's effective Codeforces Elo by +405 points in eight sequential LLM-call rounds (~27 minutes wall-clock). The pipeline transfers across weaker and stronger models without retuning, and on the multi-domain HLE benchmark, gains appear concentrated in objectively verifiable domains and reverse in subjective ones. We release CF-73, a curated set of 73 expert-rated Codeforces problems with International Grandmaster annotation and 99% local-evaluation agreement against the official verdict.

| Comments: |
| --- |
| Subjects: | Artificial Intelligence (cs.AI) |
| Cite as: | [arXiv:2605.15177](https://arxiv.org/abs/2605.15177) \[cs.AI\] |
|  | (or [arXiv:2605.15177v1](https://arxiv.org/abs/2605.15177v1) \[cs.AI\] for this version) |
|  | [https://doi.org/10.48550/arXiv.2605.15177](https://doi.org/10.48550/arXiv.2605.15177) |

## Submission history

From: Shang Zhou \[[view email](https://arxiv.org/show-email/2547ec3d/2605.15177)\]  
**\[v1\]** Thu, 14 May 2026 17:57:40 UTC (186 KB)  

[Which authors of this paper are endorsers?](https://arxiv.org/auth/show-endorsers/2605.15177) | Disable MathJax ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))