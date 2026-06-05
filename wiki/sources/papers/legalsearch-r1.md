---
created: 2026-05-28
updated: 2026-05-28
type: source
summary: "LegalSearch-R1 — RL-trained legal agent with temporal statute indexing; 7B model outperforms SOTA by 12.9-29.8% via dual RAG+web architecture enforcing lex retro non agit"
tags: [legal-ai, agentic-search, temporal-consistency, RL, RAG, grpo, law]
sources: https://arxiv.org/abs/2605.25920
status: active
confidence: high
---

# LegalSearch-R1 — Temporal Consistency in Legal Agentic Search

## Executive Summary

LegalSearch-R1 addresses a fundamental failure mode in legal LLMs: **temporal inconsistency** where the same legal query yields opposite answers depending on which version of a statute is applied. The framework trains a 7B RL agent (GRPO) to identify temporal context before searching, pairing local statute RAG (article-level precision) with online web search (broader judicial interpretation). Outperforms SOTA deep research agents and specialized legal LLMs by 12.9-29.8%, with 57.7-80.3% gains on temporal consistency. The core principle: **applicable law must match the temporal context of each case** — retroactive application of statutes violates core legal norms (lex retro non agit).

## Technical Approach

**Problem**: Legal LLMs suffer parametric temporal bias anchored to training cutoff; search agents rarely incorporate temporal constraints; web search cannot provide precise article-level statute citations.

**Framework**: End-to-end RL (GRPO) with dual-tool architecture:
1. **Local statute RAG** — curated corpus with version-controlled statute indexing; BM25 + dense (FAISS+text2vec) retrieval; temporal validity windows per amendment period
2. **Online web search** — broader judicial interpretations and precedent analyses
3. **Entropy-based advantage shaping** — accelerates learning of temporal query formulation (planning-stage decision)
4. **Temporally-indexed training data** — spanning multiple amendment periods

**Architecture**: ReAct-style multi-turn reasoning interleaving:
- Time-aware planning → temporal query formulation
- Dual retrieval (RAG + web) → reasoning → answer

## Key Results

| Metric | Result |
|--------|--------|
| In-domain legal tasks (7 tasks) | +12.9-29.8% vs SOTA deep research agents |
| Temporal consistency | +57.7-80.3% vs baselines |
| Out-of-domain generalization | Robust across 6 OOD tasks |
| Model size | 7B parameter agent |

## Wiki Connections

- [[agentic-research]] — RL-based agentic search with reasoning (ReAct framework)
- [[verifier-graph]] — entropy-based advantage shaping; calibration signal in RL
- [[entities/projects/efhf]] — dual-tool architecture parallels EFHF's environment + auxiliary channel design
- [[bounded-representation-capacity]] — temporal indexing as explicit capacity constraint on legal knowledge retrieval
- [[grpo]] — GRPO training for reasoning agents (was in prior batch)

## Related
- [[wiki/index]]
- [[sources/papers/legalsearch-r1]]

- [[legalsearch-r1]]

## Key Quotes

> "A retroactive law is truly a monstrosity. (Lex retro non agit)" — Lon L. Fuller, The Morality of Law (1969)

> "All evaluated models peak on provisions near their training cutoff (2021–2022) while degrading on both earlier and post-cutoff versions."

> "The principal of lex retro non agit holds that applicable law should align with the temporal context of each case."