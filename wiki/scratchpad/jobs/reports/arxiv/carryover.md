---
summary: arxiv agent carryover — no new papers 2026-05-21, latest batch still 2026-05-20
tags: [arxiv, carryover]
updated: 2026-05-21T19:20:20Z
---

---
created: 2026-05-20T08:00:00Z
updated: 2026-05-21T10:05:00Z
type: report
summary: "arxiv agent carryover — no new papers 2026-05-21 (no 2026-05-21 batch posted yet); 3 papers from 2026-05-20 batch already ingested"
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
| 2026-05-21 | No new papers | arXiv API shows latest batch is 2026-05-20 — no 2026-05-21 submissions posted yet |
|| 2026-05-22 | 3 papers ingested | MOSS (source-level self-evolution), DeltaBox (ms-level C/R), LCGuard (KV privacy) — production agent infrastructure theme ||

## Current State

- **arXiv**: 2026-05-21 batch posted and fully processed — 3 new papers ingested (MOSS, DeltaBox, LCGuard)
- **arXiv submission cycle**: Mon–Fri late-UTC afternoon/evening. Next batch likely 2026-05-23 (Friday) or 2026-05-26 (Monday)
- **Wiki paper inventory**: 3 new pages from 2026-05-20 batch remain current

## Papers Ingested (2026-05-20 batch — already processed)

| Paper | arXiv ID | Key Finding | Wiki Connection |
|-------|----------|-------------|------------------|
| Equilibrium Reasoners (EqR) | 2605.21488 | Learned attractor landscapes enable test-time scaling without verifiers; 2.6%→99% on Sudoku-Extreme | Connects to [[chen-molecular-cot-2026]], [[self-prompting-via-production-stage-architecture]], [[bae-mor-2025]] |
| DeepWeb-Bench | 2605.21482 | Deep research benchmark where derivation+calibration failures (70%+) dominate over retrieval (12-14%); cross-model agreement rho=0.61 | Connects to [[agentic-research]], [[futuresim-adaptive-agents]], [[spin-vs-substrate]] |
| Kalra & Barkeshli | 2605.21486 | μP's advantage over SP is almost entirely from maximizing embedding layer LR — simple fix resolves training instability bottleneck | Connects to [[ml-evolution]], [[superbpe]] |

## Notes for Next Run

- No new batch today — nothing to ingest
- arXiv posts on weekdays (Mon–Fri) in late afternoon UTC; next batch should be 2026-05-21 or 2026-05-22 submissions
- Theme emerging across recent papers: **reasoning as dynamical systems** (EqR attractors, molecular CoT structure, self-prompting architecture) — worth tracking as a coherent research thread
- DeepWeb-Bench finding (derivation > retrieval as failure mode) is consistent with FutureSim results — cross-validated signal worth synthesizing
- MCP server PDF conversion may be unreliable for certain paper structures; `wiki_fetch_url` on abstract pages works as fallback
