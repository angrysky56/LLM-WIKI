---
title: Defending MoE LLMs against Harmful Fine-Tuning via Safety Routing Alignment
source: https://arxiv.org/abs/2509.22745
created: 2026-05-25T17:36:36Z
tags: [clippings]
---

## Title:Defending MoE LLMs against Harmful Fine-Tuning via Safety Routing Alignment

Authors:[Jaehan Kim](https://arxiv.org/search/cs?searchtype=author&query=Kim,+J), [Minkyoo Song](https://arxiv.org/search/cs?searchtype=author&query=Song,+M), [Seungwon Shin](https://arxiv.org/search/cs?searchtype=author&query=Shin,+S), [Sooel Son](https://arxiv.org/search/cs?searchtype=author&query=Son,+S)

[View PDF](https://arxiv.org/pdf/2509.22745) [HTML (experimental)](https://arxiv.org/html/2509.22745v2)

> Abstract:Recent large language models (LLMs) have increasingly adopted the Mixture-of-Experts (MoE) architecture for efficiency. MoE-based LLMs heavily depend on a superficial safety mechanism in which harmful inputs are routed safety-critical experts. However, our analysis reveals that routing decisions for harmful inputs drift significantly after fine-tuning, exposing a critical vulnerability to harmful fine-tuning (HFT) attacks. Existing defenses, primarily designed for monolithic LLMs, are less effective for MoE LLMs as they fail to prevent drift in harmful input routing. To address this limitation, we propose SafeMoE, a safe fine-tuning method tailored to MoE LLMs. SafeMoE directly mitigates routing drift by penalizing the gap between the routing weights of a fine-tuned model and those of the initial safety-aligned model, thereby preserving the safety-aligned routing of harmful inputs to safety-critical experts. Experiments on open-source MoE LLMs ranging from 7B to 141B parameters demonstrate that SafeMoE effectively mitigates HFT attacks, reducing the harmfulness score of OLMoE from 62.0 to 5.0, for example, while maintaining task utility within 1% degradation and incurring only 2% overhead. It significantly outperforms state-of-the-art defense methods for safeguarding LLM fine-tuning and remains effective in recent large-scale MoE LLMs such as gpt-oss and Llama 4. Our implementation is available at [this https URL](https://anonymous.4open.science/r/SafeMoE).

| Comments: |
| --- |
| Subjects: | Cryptography and Security (cs.CR); Artificial Intelligence (cs.AI) |
| Cite as: | [arXiv:2509.22745](https://arxiv.org/abs/2509.22745) \[cs.CR\] |
|  | (or [arXiv:2509.22745v2](https://arxiv.org/abs/2509.22745v2) \[cs.CR\] for this version) |
|  | [https://doi.org/10.48550/arXiv.2509.22745](https://doi.org/10.48550/arXiv.2509.22745) |

## Submission history

From: Jaehan Kim \[[view email](https://arxiv.org/show-email/c20983f8/2509.22745)\]  
**[\[v1\]](https://arxiv.org/abs/2509.22745v1)** Fri, 26 Sep 2025 04:10:32 UTC (433 KB)  
**\[v2\]** Thu, 9 Oct 2025 13:00:18 UTC (437 KB)  

[Which authors of this paper are endorsers?](https://arxiv.org/auth/show-endorsers/2509.22745) | Disable MathJax ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))