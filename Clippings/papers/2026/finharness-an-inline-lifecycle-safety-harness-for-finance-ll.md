---
title: FinHarness: An Inline Lifecycle Safety Harness for Finance LLM Agents
source: https://arxiv.org/abs/2605.27333
created: 2026-05-27T14:17:04Z
tags: [clippings]
---

## Title:FinHarness: An Inline Lifecycle Safety Harness for Finance LLM Agents

[View PDF](https://arxiv.org/pdf/2605.27333) [HTML (experimental)](https://arxiv.org/html/2605.27333v1)

> Abstract:Finance LLM agents must simultaneously block prompt-induced unauthorized actions and approve legitimate multi-step business workflows. However, boundary filters often miss irreversible mid-trajectory tool calls, while post-hoc LLM judges perform auditing only after termination -- too late for intervention and at a computational cost that scales linearly with trace length. We present FinHarness, an inline safety harness that wraps a finance agent end-to-end with three components: a Query Monitor that fuses single-turn intent with cross-turn drift, a Tool Monitor that evaluates each prospective tool call, and a Cascade module that integrates per-step risk and adaptively routes verification between a lightweight and an advanced-tier LLM judge. Fired risk factors are re-injected into the agent input as ex-ante evidence, enabling the agent to refuse, re-plan, or approve on its own. On FinVault, routed FinHarness cuts ASR from 38.3% to 15.0% while largely preserving benign approval ($41.1\% \to 39.3\%$), and uses $4.7\times$ fewer advanced-judge calls than an always-advanced ablation.

| Subjects: | Computation and Language (cs.CL) |
| --- | --- |
| Cite as: | [arXiv:2605.27333](https://arxiv.org/abs/2605.27333) \[cs.CL\] |
|  | (or [arXiv:2605.27333v1](https://arxiv.org/abs/2605.27333v1) \[cs.CL\] for this version) |
|  | [https://doi.org/10.48550/arXiv.2605.27333](https://doi.org/10.48550/arXiv.2605.27333) |

## Submission history

From: Haoxuan Jia \[[view email](https://arxiv.org/show-email/d7ac540c/2605.27333)\]  
**\[v1\]** Tue, 26 May 2026 17:41:01 UTC (1,135 KB)  

[Which authors of this paper are endorsers?](https://arxiv.org/auth/show-endorsers/2605.27333) | Disable MathJax ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))