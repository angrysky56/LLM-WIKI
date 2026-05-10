---
title: From Context to Skills: Can Language Models Learn from Context Skillfully?
source: https://arxiv.org/abs/2604.27660
created: 2026-05-08T19:18:52Z
tags: [clippings]
---

## Title:From Context to Skills: Can Language Models Learn from Context Skillfully?

[View PDF](https://arxiv.org/pdf/2604.27660) [HTML (experimental)](https://arxiv.org/html/2604.27660v2)

> Abstract:Many real-world tasks require language models (LMs) to reason over complex contexts that exceed their parametric knowledge. This calls for context learning, where LMs directly learn relevant knowledge from the given context. An intuitive solution is inference-time skill augmentation: extracting the rules and procedures from context into natural-language skills. However, constructing such skills for context learning scenarios faces two challenges: the prohibitive cost of manual skill annotation for long, technically dense contexts, and the lack of external feedback for automated skill construction. In this paper, we propose Ctx2Skill, a self-evolving framework that autonomously discovers, refines, and selects context-specific skills without human supervision or external feedback. At its core, a multi-agent self-play loop has a Challenger that generates probing tasks and rubrics, a Reasoner that attempts to solve them guided by an evolving skill set, and a neutral Judge that provides binary feedback. Crucially, both the Challenger and the Reasoner evolve through accumulated skills: dedicated Proposer and Generator agents analyze failure cases and synthesize them into targeted skill updates for both sides, enabling automated skill discovery and refinement. To prevent adversarial collapse caused by increasingly extreme task generation and over-specialized skill accumulation, we further introduce a Cross-time Replay mechanism that identifies the skill set achieving the best balance across representative cases for the Reasoner side, ensuring robust and generalizable skill evolution. The resulting skills can be plugged into any language model to obtain better context learning capability. Evaluated on four context learning tasks from CL-bench, Ctx2Skill consistently improves solving rates across backbone models.

| Subjects: | Artificial Intelligence (cs.AI) |
| --- | --- |
| Cite as: | [arXiv:2604.27660](https://arxiv.org/abs/2604.27660) \[cs.AI\] |
|  | (or [arXiv:2604.27660v2](https://arxiv.org/abs/2604.27660v2) \[cs.AI\] for this version) |
|  | [https://doi.org/10.48550/arXiv.2604.27660](https://doi.org/10.48550/arXiv.2604.27660) |

## Submission history

From: Shuzheng Si \[[view email](https://arxiv.org/show-email/bbaa15ba/2604.27660)\]  
**[\[v1\]](https://arxiv.org/abs/2604.27660v1)** Thu, 30 Apr 2026 09:53:15 UTC (8,023 KB)  
**\[v2\]** Sun, 3 May 2026 14:10:15 UTC (8,023 KB)  

[Which authors of this paper are endorsers?](https://arxiv.org/auth/show-endorsers/2604.27660) | Disable MathJax ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))