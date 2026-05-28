---
created: 2026-05-19
updated: 2026-06-27
type: report
summary: arxiv daily report — EnvFactory paper and Claude Code skills article
tags: [arxiv, report]
---

# arxiv Report — 2026-05-19

## Papers Processed

### 1. **EnvFactory: Scaling Tool-Use Agents via Executable Environments Synthesis and Robust RL** (arxiv:2605.18703)
- **Why selected**: Tackles a fundamental bottleneck in agentic RL — environment scarcity. The paper's approach to auto-synthesizing executable tool environments from authenticated APIs directly addresses the training data problem for tool-use agents. Novel contribution: fully automated environment synthesis with robust RL handling of stochastic environment models.
- **Status**: ingested → `wiki/sources/papers/xu-envfactory-2026.md`
- **Wiki connections**: agentic-research, verifier-graph, mcp-logic, graphrag, efhf

### 2. **SD-Search: On-Policy Hindsight Self-Distillation for Search-Augmented Reasoning** (arxiv:2605.18299)
- **Why selected**: Solves a core credit assignment problem in search-augmented reasoning — every query in a rollout previously received the same trajectory-level reward. SD-Search derives step-level credit from the policy's own successful rollouts via hindsight self-distillation, requiring no external teacher. Novel and architecturally clean.
- **Status**: ingested → `wiki/sources/papers/ma-sd-search-2026.md`
- **Wiki connections**: graphrag, rag, reward-modeling, chain-of-thought, mcp-logic

### 3. **LMAC: LLM-Guided Communication for Cooperative Multi-Agent RL** (arxiv:2605.18077)
- **Why selected**: Uses LLM reasoning to design communication protocols for multi-agent systems, addressing the partial observability problem via an explicit state-awareness criterion. The LLM-as-protocol-designer pattern is architecturally significant — connects to EFHF multi-agent coordination and sheaf consistency.
- **Status**: ingested → `wiki/sources/papers/bae-lmac-2026.md`
- **Wiki connections**: efhf, mop-explorer, reward-modeling, sheaf-consistency-enforcer, maximum-occupancy-principle

## Wiki Updates

- **New pages**: 3 (`xu-envfactory-2026.md`, `ma-sd-search-2026.md`, `bae-lmac-2026.md`)
- **Updated pages**: 0
- **Tags added**: paper, arxiv, agentic-rl, tool-use, search-augmented-rag, multi-agent-rl, communication-protocols, cooperative-learning

## Related
- [[index]]
- [[scratchpad/jobs/reports/arxiv/arxiv-2026-05-19-top-papers]]

- [[arxiv-2026-05-19-top-papers]]

## Notes

- Semantic Scholar returned 429 (rate limited) for all 5 papers checked — skipped citation enrichment this cycle
- arXiv search returned 8 papers across three query categories; selected top 3 by novelty and relevance to active research threads
- All 3 selected papers share a theme: **credit assignment in distributed/agentic systems** — EnvFactory (environment model credit), SD-Search (query-level credit), LMAC (communication protocol credit). This is a coherent research thread worth tracking.
- All papers published 2026-05-18 (yesterday) — fresh contributions in active areas