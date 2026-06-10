---
tags: [arxiv, carryover]
updated: 2026-06-10T17:30:00Z
created: 2026-06-10T17:30:00Z
---

# arxiv Agent — Carryover

## Run History

| Date | Result | Notes |
|------|--------|-------|
| 2026-05-18 | 3 papers ingested | EnvFactory, SD-Search, LMAC — credit assignment theme |
| 2026-06-11 | 2 papers ingested (inbox) | PC Layer (2606.06470), RREDCoT (2606.06475) |
| **2026-06-10** | **3 papers ingested (arxiv discovery)** | **Target-SFT, FutureProbes, ReasonAlloc — hierarchy principle theme** |

## Papers Ingested (2026-06-10 — arXiv discovery cycle)

| Paper | arXiv ID | Key Finding | Wiki Page |
|-------|----------|-------------|-----------|
| Target-SFT | 2606.11189v1 | Q-target framework unifies SFT variants; TARGET-SFT consistently outperforms across 10 settings | [[target-sft-unifying-lens]] |
| FutureProbes | 2606.11172v1 | Detection vs prediction features for steering LRMs; FPCG achieves strong steering with minimal quality degradation | [[future-probes-steering]] |
| ReasonAlloc | 2606.11164v1 | Hierarchical KV cache allocation via "Reasoning Wave" pattern; outperforms uniform budgets especially at small cache sizes | [[reasonalloc-kv-cache-allocation]] |

## Papers Ingested (2026-06-11 — inbox batch)

| Paper | arXiv ID | Key Finding | Wiki Page |
|-------|----------|-------------|-----------|
| PC Layer | 2606.06470v1 | Polynomial preconditioning for LLM training — 20-35% faster convergence | Existing |
| RREDCoT | 2606.06475v1 | Segment-level reward redistribution for reasoning models — 30-50% better sample efficiency | Existing |

## Cross-Paper Theme

**"The Hierarchy Principle"** — Three papers independently challenge uniform assumptions across the LLM pipeline (SFT training, KV cache allocation, behavioral steering) and replace them with structured hierarchical allocation. See [[hierarchy-principle-llm-pipeline]].

## Open Items

- [ ] (Optional) Create entity page for Tencent's LLM Agent Memory research
- [ ] (Optional) Check pending PDFs: remaining 2605.26998, 2605.22779 in pool
- [ ] (Optional) Next normal arXiv discovery cycle: check cs.AI/cs.LG/cs.CL for new papers

## Last Run

2026-06-10 17:30 UTC — arXiv discovery cycle. Inbox empty. Queried arXiv API, selected top 3 from 15 results (June 9 submissions). Papers: Target-SFT (2606.11189), FutureProbes (2606.11172), ReasonAlloc (2606.11164). All ingested to wiki/sources/papers/. Cross-paper synthesis at wiki/synthesis/hierarchy-principle-llm-pipeline.md.