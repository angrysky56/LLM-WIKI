---
summary: LMAC leverages LLM reasoning to design communication protocols that enable multi-agent RL systems to reconstruct underlying states accurately and uniformly
tags: [paper, arxiv, multi-agent-rl, communication-protocols, llm, cooperative-learning]
sources: https://arxiv.org/abs/2605.18077
confidence: 0.8
---

# LLM-Guided Communication for Cooperative Multi-Agent Reinforcement Learning

## Paper Info
- Authors: Sangjun Bae, Yisak Park, Sanghyeon Lee, Seungyul Han
- arXiv: 2605.18077
- Published: 2026-05-18
- Categories: cs.AI, cs.LG, cs.MA

## Summary

Communication in multi-agent RL (MARL) is critical for mitigating partial observability — each agent sees only a fragment of the world state. Prior approaches suffer from either inefficient information exchange (agents communicate too much or too little) or failure to transmit sufficient state information (protocols are too lossy). LMAC (LLM-driven Multi-Agent Communication) uses an LLM's reasoning capability to design a communication protocol enabling all agents to reconstruct the underlying state as accurately and uniformly as possible. The protocol is iteratively refined using an explicit state-awareness criterion, improving state reconstruction while narrowing differences in agents' knowledge. Experiments across diverse MARL benchmarks show substantial performance gains.

## Key Findings
- **LLM-as-protocol-designer**: Using the LLM's inherent reasoning to design communication protocols rather than having agents learn protocols from scratch — the LLM's world model provides the structural scaffolding for the communication schema
- **State-awareness criterion**: Protocol refinement is driven by how well all agents can reconstruct the underlying state from received messages — explicitly optimizing for state uniformity across agents
- **Iterative refinement**: The protocol improves over multiple rounds by identifying which messages lead to state reconstruction errors and adjusting accordingly
- **Handles partial observability**: The core challenge in MARL — each agent has incomplete information — is addressed by treating communication as a state reconstruction problem rather than an information routing problem

## Relevance to Our Work

Relevant to [[efhf]] architecture (multi-agent coordination, Layer 0-2), [[mop-explorer]] (multi-agent exploration), and the broader agentic research agenda. The state-uniformity criterion in LMAC is structurally similar to the consistency requirements in [[sheaf-consistency-enforcer]] — both deal with ensuring that distributed agents maintain consistent world models. The LLM-as-protocol-designer pattern also connects to the idea in [[supertokens]] where high-level structural units (communication protocols as "supertokens") guide lower-level behavior.

Also relevant to [[reward-modeling]] — the state-awareness criterion serves as an intrinsic reward signal for protocol optimization, analogous to how reward models provide training signal for alignment.

## Connections
- [[efhf]]
- [[mop-explorer]]
- [[reward-modeling]]
- [[supertokens]]
- [[sheaf-consistency-enforcer]]
- [[maximum-occupancy-principle]]