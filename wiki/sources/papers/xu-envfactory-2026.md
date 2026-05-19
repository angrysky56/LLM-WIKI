---
summary: EnvFactory automates generation of scalable executable tool-use environments for training tool-use agents via agentic RL
tags: [paper, arxiv, agentic-rl, tool-use, llm, reinforcement-learning]
sources: https://arxiv.org/abs/2605.18703
confidence: 0.8
---

# EnvFactory: Scaling Tool-Use Agents via Executable Environments Synthesis and Robust RL

## Paper Info
- Authors: Minrui Xu, Zilin Wang, Mengyi DENG, Zhiwei Li, Zhicheng Yang, Xiao Zhu, Yinhong Liu, Boyu Zhu, Baiyu Huang, Chao Chen, Heyuan Deng, Fei Mi, Lifeng Shang, Xingshan Zeng, Zhijiang Guo
- arXiv: 2605.18703
- Published: 2026-05-18
- Categories: cs.CL, cs.LG

## Summary

EnvFactory tackles two fundamental bottlenecks in training LLMs to use tools via Agentic Reinforcement Learning: (1) the lack of scalable, robust execution environments, and (2) the scarcity of realistic training data that captures implicit human reasoning. Existing approaches rely on costly real-world APIs, hallucination-prone LLM simulators, or synthetic single-turn environments dependent on pre-collected documents. EnvFactory autonomously explores and verifies stateful, executable tool environments from authenticated APIs, generating realistic multi-turn interaction data without hand-crafted annotations. The framework uses robust RL to handle the noisy, stochastic environments that arise from this automated synthesis.

## Key Findings
- **Automated environment synthesis**: EnvFactory can generate executable tool environments at scale from authenticated APIs without human annotation, addressing the data scarcity problem directly
- **Robust RL training**: The noisy, stochastic nature of auto-synthesized environments requires robust RL techniques to handle environment model errors and hallucinations
- **Multi-turn realism**: Unlike prior single-turn or document-dependent synthetic environments, EnvFactory produces stateful, multi-turn trajectories that resemble natural human intent
- **Stateful execution**: Environments maintain state across interactions, enabling realistic tool-use chains that depend on prior actions

## Relevance to Our Work

Directly relevant to [[agentic-research]] and the tool-use patterns being explored in the EFHF architecture. The robust RL approach for handling noisy environments parallels concerns in the [[verifier-graph]] and [[mcp-logic]] verification substrates. Also connects to [[ctx2skill]] — both address the problem of generating training signal for agentic behaviors without human annotation.

The problem framing (agentic RL bottlenecked by environment scarcity) mirrors the same structural problem as [[graphrag]] — both are cases where the bottleneck is environmental/contextual scaffolding, not the core learning algorithm.

## Connections
- [[agentic-research]]
- [[chain-of-thought]]
- [[verifier-graph]]
- [[mcp-logic]]
- [[graphrag]]
- [[efhf]]