---
summary: ClinSeekAgent automates multimodal evidence seeking for agentic clinical reasoning — addressing the gap where evidence is assumed rather than retrieved
tags: [paper, arxiv, llm-agents, clinical-ai, agentic-reasoning, multimodal]
sources: https://arxiv.org/abs/2605.20176
confidence: 0.8
---

# ClinSeekAgent: Automating Multimodal Evidence Seeking for Agentic Clinical Reasoning

## Paper Info
- Authors: Juncheng Wu, Letian Zhang, Yuhan Wang
- arxiv: 2605.20176
- Published: 2026-05-19
- Categories: cs.CL

## Summary

Large language models and agentic systems have shown promise for clinical decision support, but existing systems assume evidence is already available or easily accessible. In real clinical settings, evidence must often be actively sought across multiple modalities — electronic health records, medical literature, imaging databases, and lab results — none of which present a unified interface.

ClinSeekAgent addresses this by constructing a multimodal evidence-seeking pipeline for clinical reasoning. The agent can query disparate evidence sources, evaluate retrieved information for relevance and reliability, and synthesize findings into a clinical reasoning chain. The key challenge tackled is the *evidence gap*: the difference between what the agent assumes it knows and what it can actually verify against source documents.

## Key Findings

- Existing clinical agent systems fail because they assume evidence availability rather than seeking it
- A structured multimodal evidence-seeking pipeline significantly improves clinical reasoning accuracy
- Evidence reliability scoring is critical — not all retrieved content is equally trustworthy
- The agentic loop (seek → evaluate → synthesize → seek again) outperforms single-pass retrieval

## Relevance to Our Work

The [[code-as-agent-harness]] research and [[awesome-code-as-agent-harness]] papers examine how agents search and use external tool outputs. ClinSeekAgent extends this pattern into a high-stakes, multimodal domain where evidence quality is literally life-or-death. The evidence-seeking loop architecture is directly applicable to our agent tool-use research. Also connects to [[Ctx2skill]] work on grounding — clinical evidence grounding is a concrete instance of the broader grounding problem.

## Connections
- [[code-as-agent-harness]]
- [[ctx2skill-on-efhf-rails]]
- [[agentic-reasoning]]