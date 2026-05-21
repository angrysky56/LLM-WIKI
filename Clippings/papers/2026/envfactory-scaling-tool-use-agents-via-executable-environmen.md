---
title: EnvFactory: Scaling Tool-Use Agents via Executable Environments Synthesis and Robust RL
source: https://arxiv.org/abs/2605.18703
created: 2026-05-19T16:24:28Z
tags: [clippings]
---

## Title:EnvFactory: Scaling Tool-Use Agents via Executable Environments Synthesis and Robust RL

[View PDF](https://arxiv.org/pdf/2605.18703) [HTML (experimental)](https://arxiv.org/html/2605.18703v1)

> Abstract:Equipping LLMs with tool-use capabilities via Agentic Reinforcement Learning (Agentic RL) is bottlenecked by two challenges: the lack of scalable, robust execution environments and the scarcity of realistic training data that captures implicit human reasoning. Existing approaches depend on costly real-world APIs, hallucination-prone LLM simulators, or synthetic environments that are often single-turn or depend on pre-collected documents. Moreover, synthetic trajectories are frequently over-specified, resembling instruction sequences rather than natural human intents, reducing their effectiveness for RL training. We introduce EnvFactory, a fully automated framework that addresses both challenges. EnvFactory autonomously explores and verifies stateful, executable tool environments from authentic resources, and synthesizes natural multi-turn trajectories through topology-aware sampling and calibrated refinement, producing grounded queries with implicit intents. Using only 85 verified environments across 7 domains, EnvFactory generates 2,575 SFT and RL trajectories. Despite using significantly fewer environments than prior work, which are often 5 times more, EnvFactory achieves superior training efficiency and downstream performance, improving Qwen3-series models by up to +15% on BFCLv3, +8.6% on MCP-Atlas, and +6% on conversational benchmarks including $\tau^2$ -Bench and VitaBench. By fully automating both environment construction and trajectory synthesis, EnvFactory provides a scalable, extensible, and robust foundation for Agentic RL.

| Comments: |
| --- |
| Subjects: | Computation and Language (cs.CL); Machine Learning (cs.LG) |
| Cite as: | [arXiv:2605.18703](https://arxiv.org/abs/2605.18703) \[cs.CL\] |
|  | (or [arXiv:2605.18703v1](https://arxiv.org/abs/2605.18703v1) \[cs.CL\] for this version) |
|  | [https://doi.org/10.48550/arXiv.2605.18703](https://doi.org/10.48550/arXiv.2605.18703) |

## Submission history

From: Minrui Xu \[[view email](https://arxiv.org/show-email/96b6c0aa/2605.18703)\]  
**\[v1\]** Mon, 18 May 2026 17:37:40 UTC (12,599 KB)  

[Which authors of this paper are endorsers?](https://arxiv.org/auth/show-endorsers/2605.18703) | Disable MathJax ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))