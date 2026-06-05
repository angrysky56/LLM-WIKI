---
updated: 2026-05-17 18:17:29+00:00
summary: Grep often outperforms vector retrieval in agentic search; harness architecture and tool result presentation matter more than retrieval strategy.
tags: [arxiv, cs.CL, retrieval, rag, ai-agents, benchmarking]
---


# Is Grep All You Need? How Agent Harnesses Reshape Agentic Search

**arXiv:** [2605.15184](https://arxiv.org/abs/2605.15184) | **Category:** cs.CL | **Submitted:** 2026-05-14

## Core Insight

Grep (BM25 keyword search) consistently outperforms vector retrieval in agentic search pipelines across multiple provider-native CLI harnesses — even as the field converges on semantic embeddings as the default. The retrieval strategy matters less than the harness architecture and how tool results are presented to the model, suggesting that *how* an agent reads matters more than *what* it searches with.

## Key Claims

| Claim | Evidence | Implication |
|-------|----------|-------------|
| Grep > Vector retrieval on agentic search tasks | 116-question sample, LongMemEval | BM25 remains competitive in grounded agent workflows |
| Harness choice dominates retrieval choice | Claude Code, Codex, Gemini CLI vary widely on same data | Standardising agent eval requires harness-aware benchmarks |
| Inline tool results ≠ file-based tool results | File-based results degrade performance | Agent UX design choices have measurable impact |
| Distractor material amplifies retrieval gaps | Progressive noise injection shows vector retrieval degrades faster | Real-world noisy contexts amplify the grep advantage |

## Authors

Sahil Sen, Akhil Kasturi, Elias Lumer, Anmol Gulati, Vamse Kumar Subbiah

## Metadata

- **arXiv ID:** 2605.15184
- **Primary category:** cs.CL
- **Submitted:** 2026-05-14
- **PDF:** https://arxiv.org/pdf/2605.15184

## Connections

- [[information-retrieval]] — grep vs vector retrieval comparison

## Open Questions

- Does the grep advantage hold on non-code agentic tasks (e.g., research assistants)?
- Would fine-tuned embedding models close the gap?
- How do multi-step agent loops amplify or suppress retrieval differences?
