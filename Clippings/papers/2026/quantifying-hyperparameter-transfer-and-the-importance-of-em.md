---
title: Quantifying Hyperparameter Transfer and the Importance of Embedding Layer Learning Rate
source: https://arxiv.org/abs/2605.21486
created: 2026-05-21T16:51:29Z
tags: [clippings]
---

## Title:Quantifying Hyperparameter Transfer and the Importance of Embedding Layer Learning Rate

Authors:[Dayal Singh Kalra](https://arxiv.org/search/cs?searchtype=author&query=Kalra,+D+S), [Maissam Barkeshli](https://arxiv.org/search/cs?searchtype=author&query=Barkeshli,+M)

[View PDF](https://arxiv.org/pdf/2605.21486) [HTML (experimental)](https://arxiv.org/html/2605.21486v1)

> Abstract:Hyperparameter transfer allows extrapolating optimal optimization hyperparameters from small to large scales, making it critical for training large language models (LLMs). This is done either by fitting a scaling law to the hyperparameters or by a judicious choice of parameterization, such as Maximal Update ($\mu$ P), that renders optimal hyperparameters approximately scale invariant. In this paper, we first develop a framework to quantify hyperparameter transfer through three metrics: (1) the quality of the scaling law fit, (2) the robustness to extrapolation errors, and (3) the asymptotic loss penalty due to choice of parameterization. Next, we investigate through a comprehensive series of ablations why $\mu$ P appears to offer high-quality learning rate transfer relative to standard parameterization (SP), as existing theory is inadequate. We find that the overwhelming benefit of $\mu$ P relative to SP when training with AdamW arises simply from maximizing the learning rate of the embedding layer. In SP, the embedding layer learning rate acts as a bottleneck that induces training instabilities; increasing it by a factor of width to match $\mu$ P dramatically smooths out training while improving hyperparameter transfer. We also find that weight decay improves the scaling law fits, while, in the fixed token-per-parameter setting, it hurts the robustness of the extrapolation.

| Comments: |
| --- |
| Subjects: | Machine Learning (cs.LG); Disordered Systems and Neural Networks (cond-mat.dis-nn); Artificial Intelligence (cs.AI); Machine Learning (stat.ML) |
| Cite as: | [arXiv:2605.21486](https://arxiv.org/abs/2605.21486) \[cs.LG\] |
|  | (or [arXiv:2605.21486v1](https://arxiv.org/abs/2605.21486v1) \[cs.LG\] for this version) |
|  | [https://doi.org/10.48550/arXiv.2605.21486](https://doi.org/10.48550/arXiv.2605.21486) |

## Submission history

From: Dayal Singh Kalra \[[view email](https://arxiv.org/show-email/ebaeaa36/2605.21486)\]  
**\[v1\]** Wed, 20 May 2026 17:59:40 UTC (5,696 KB)  

[Which authors of this paper are endorsers?](https://arxiv.org/auth/show-endorsers/2605.21486) | Disable MathJax ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))