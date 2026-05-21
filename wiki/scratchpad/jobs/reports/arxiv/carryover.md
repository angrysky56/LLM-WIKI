---
summary: arxiv agent carryover — 3 papers ingested 2026-05-21 (EqR, DeepWeb-Bench, hyperparameter transfer)
tags: [arxiv, carryover]
updated: 2026-05-21T16:53:32Z
---

---
created: 2026-05-20T08:00:00Z
updated: 2026-05-21T16:55:00Z
type: report
summary: "arxiv agent carryover — 3 papers ingested 2026-05-21 (EqR, DeepWeb-Bench, hyperparameter transfer); MCP server conversion errors bypassed via wiki_fetch_url"
tags: [arxiv, carryover]
sources: []
status: active
confidence: high
---

# arxiv Agent — Carryover

## Run History

| Date | Result | Notes |
|------|--------|-------|
| 2026-05-18 | 3 papers ingested | EnvFactory, SD-Search, LMAC — credit assignment theme |
| 2026-05-20 | No new papers | arXiv late-UTC batch not yet posted |
| 2026-05-21 | 3 papers ingested | EqR (attractors), DeepWeb-Bench (benchmark), hyperparameter transfer (embedding LR) |
| 2026-05-22 | — | — |

## Current State

- **arXiv**: 3 new papers successfully ingested from 2026-05-20 batch
- **MCP conversion issue**: arxiv-mcp-server PDF conversion failed for 2 papers (2605.21488, 2605.21482) with `'NoneType' object has no attribute 'tables'` — bypassed by using wiki_fetch_url directly on arXiv abstract pages, which succeeded and ingested to Neo4j
- **Wiki paper timeline**: populated — 3 new source pages created in wiki/sources/papers/

## Papers Ingested (2026-05-21)

| Paper | arXiv ID | Key Finding | Wiki Connection |
|-------|----------|-------------|------------------|
| Equilibrium Reasoners (EqR) | 2605.21488 | Learned attractor landscapes enable test-time scaling without verifiers; 2.6%→99% on Sudoku-Extreme | Connects to [[chen-molecular-cot-2026]], [[self-prompting-via-production-stage-architecture]], [[bae-mor-2025]] |
| DeepWeb-Bench | 2605.21482 | Deep research benchmark where derivation+calibration failures (70%+) dominate over retrieval (12-14%); cross-model agreement rho=0.61 | Connects to [[agentic-research]], [[futuresim-adaptive-agents]], [[spin-vs-substrate]] |
| Kalra & Barkeshli | 2605.21486 | μP's advantage over SP is almost entirely from maximizing embedding layer LR — simple fix resolves training instability bottleneck | Connects to [[ml-evolution]], [[superbpe]] |

## Notes for Next Run

- MCP server PDF conversion may be unreliable for certain paper structures; wiki_fetch_url on abstract pages works as fallback
- Theme emerging across recent papers: **reasoning as dynamical systems** (EqR attractors, molecular CoT structure, self-prompting architecture) — worth tracking as a coherent research thread
- DeepWeb-Bench finding (derivation > retrieval as failure mode) is consistent with FutureSim results — cross-validated signal worth synthesizing
