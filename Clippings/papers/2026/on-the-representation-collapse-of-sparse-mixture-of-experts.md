---
title: On the Representation Collapse of Sparse Mixture of Experts
source: https://arxiv.org/abs/2204.09179
created: 2026-05-25T17:35:36Z
tags: [clippings]
---

## Title:On the Representation Collapse of Sparse Mixture of Experts

[View PDF](https://arxiv.org/pdf/2204.09179)

> Abstract:Sparse mixture of experts provides larger model capacity while requiring a constant computational overhead. It employs the routing mechanism to distribute input tokens to the best-matched experts according to their hidden representations. However, learning such a routing mechanism encourages token clustering around expert centroids, implying a trend toward representation collapse. In this work, we propose to estimate the routing scores between tokens and experts on a low-dimensional hypersphere. We conduct extensive experiments on cross-lingual language model pre-training and fine-tuning on downstream tasks. Experimental results across seven multilingual benchmarks show that our method achieves consistent gains. We also present a comprehensive analysis on the representation and routing behaviors of our models. Our method alleviates the representation collapse issue and achieves more consistent routing than the baseline mixture-of-experts methods.

| Comments: |
| --- |
| Subjects: | Computation and Language (cs.CL); Machine Learning (cs.LG) |
| Cite as: | [arXiv:2204.09179](https://arxiv.org/abs/2204.09179) \[cs.CL\] |
|  | (or [arXiv:2204.09179v3](https://arxiv.org/abs/2204.09179v3) \[cs.CL\] for this version) |
|  | [https://doi.org/10.48550/arXiv.2204.09179](https://doi.org/10.48550/arXiv.2204.09179) |

## Submission history

From: Li Dong \[[view email](https://arxiv.org/show-email/4464d2b3/2204.09179)\]  
**[\[v1\]](https://arxiv.org/abs/2204.09179v1)** Wed, 20 Apr 2022 01:40:19 UTC (762 KB)  
**[\[v2\]](https://arxiv.org/abs/2204.09179v2)** Fri, 20 May 2022 13:35:05 UTC (916 KB)  
**\[v3\]** Wed, 12 Oct 2022 10:17:55 UTC (767 KB)  

[Which authors of this paper are endorsers?](https://arxiv.org/auth/show-endorsers/2204.09179) | Disable MathJax ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))