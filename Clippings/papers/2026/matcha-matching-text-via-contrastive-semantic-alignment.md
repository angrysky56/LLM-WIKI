---
title: MATCHA: Matching Text via Contrastive Semantic Alignment
source: https://arxiv.org/abs/2605.27345
created: 2026-05-27T14:17:03Z
tags: [clippings]
---

## Title:MATCHA: Matching Text via Contrastive Semantic Alignment

[View PDF](https://arxiv.org/pdf/2605.27345) [HTML (experimental)](https://arxiv.org/html/2605.27345v1)

> Abstract:Reliable evaluation is essential for understanding large language model (LLM) performance, yet today's go-to metrics, namely token-overlap scores (e.g., ROUGE) and embedding-based measures (e.g., BERTScore), often misjudge semantic similarity of documents. Our study shows that both token-overlap metrics and embedding-based metrics routinely assign nearly identical scores to texts that directly contradict each other, thereby potentially masking fundamental errors. We introduce MATCHA, an automatic metric that jointly rewards semantic agreement with a reference and penalizes contradictions. MATCHA employs a dual-view perspective that measures (i) proximity to the gold text and (ii) distance from an adversarially generated counterfactual contradiction. In eight public benchmarks, MATCHA outperforms popular metrics, compared with human annotations on question-answering, image caption generation, natural language inference, summarization, and semantic textual similarity tasks. On the TruthfulQA dataset (i.e., a dataset without a training set, where no embedding-based metrics could locally train on), this improvement in terms of matching texts with a reference reaches 18.38% over ROUGE-L and 20.82% over BERTScore. Both quantitative comparison and qualitative human assessments confirm the efficacy and validity of MATCHA and uncover fundamental weaknesses in pre-existing metrics. Compared with 23 embedding models, including top state-of-the-art ones, used as a metric similar to BERTScore, MATCHA remains the most accurate in distinguishing correct from incorrect statements solely based on a reference. Our code and metric are publicly available ([this https URL](https://github.com/Siran-Li/MATCHA)).

| Subjects: | Computation and Language (cs.CL) |
| --- | --- |
| Cite as: | [arXiv:2605.27345](https://arxiv.org/abs/2605.27345) \[cs.CL\] |
|  | (or [arXiv:2605.27345v1](https://arxiv.org/abs/2605.27345v1) \[cs.CL\] for this version) |
|  | [https://doi.org/10.48550/arXiv.2605.27345](https://doi.org/10.48550/arXiv.2605.27345) |

## Submission history

From: Siran Li \[[view email](https://arxiv.org/show-email/30c42ad3/2605.27345)\]  
**\[v1\]** Tue, 26 May 2026 17:47:14 UTC (7,587 KB)  

[Which authors of this paper are endorsers?](https://arxiv.org/auth/show-endorsers/2605.27345) | Disable MathJax ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))