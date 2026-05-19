---
summary: SD-Search uses on-policy hindsight self-distillation to provide step-level credit to individual search queries in search-augmented reasoning, without external teachers
tags: [paper, arxiv, search-augmented-rag, reinforcement-learning, reasoning]
sources: https://arxiv.org/abs/2605.18299
confidence: 0.8
---

# SD-Search: On-Policy Hindsight Self-Distillation for Search-Augmented Reasoning

## Paper Info
- Authors: Yufei Ma, Zihan Liang, Ben Chen, Zhipeng Qian, Huangyu Dai, Lingtao Mao, Xuxin Zhang, Chenyi Lei, Wenwu Ou
- arXiv: 2605.18299
- Published: 2026-05-18
- Categories: cs.AI, cs.CL, cs.IR

## Summary

Search-augmented reasoning agents alternate between internal reasoning and external retriever calls. The key bottleneck: under outcome-reward RL, every search decision in a rollout receives the same trajectory-level reward, leaving individual queries without step-specific credit. Existing process-supervision approaches address this with external teachers (larger models) or sub-question annotations from a stronger external system. SD-Search derives step-level supervision from the policy itself through on-policy hindsight self-distillation — requiring neither an external teacher nor additional annotations. The method identifies which search queries contributed to successful reasoning outcomes and uses that to credit individual search decisions within the same rollout.

## Key Findings
- **Hindsight self-distillation**: Step-level credit is derived from the policy's own experience — successful trajectories are decomposed into their constituent successful queries, then used to train the policy on failed trajectories that shared queries with successful ones
- **No external teacher required**: Unlike prior process-supervision approaches, SD-Search doesn't require a larger teacher model or additional annotation pipelines
- **On-policy consistency**: By using on-policy data, the step-level signals stay consistent with the current policy state, avoiding the distribution mismatch of off-policy distillation approaches
- **Improves search quality**: Better query selection leads to more relevant retrieved context, which improves overall reasoning quality in a virtuous cycle

## Relevance to Our Work

Relevant to [[graphrag]] and the [[rag]] concept page — both deal with retrieval-augmented generation and the problem of when and how to query external knowledge. SD-Search addresses a fundamental credit assignment problem in iterative retrieval: without step-level signals, the agent can't learn to make better retrieval decisions. This is the same class of problem as [[reward-modeling]] for RLHF — how to assign credit to intermediate decisions that contribute to a final outcome.

Also connects to [[chain-of-thought]] — the step-level credit assignment in SD-Search is essentially applying CoT-style decomposition to the search process itself.

## Connections
- [[graphrag]]
- [[rag]]
- [[reward-modeling]]
- [[chain-of-thought]]
- [[supertokens]]
- [[mcp-logic]]