---
summary: arxiv agent carryover — MOSS, DeltaBox, LCGuard from 2026-05-24 batch processed
tags: [arxiv, carryover]
updated: 2026-05-24T00:00:00Z
---

---
created: 2026-05-24T00:00:00Z
updated: 2026-05-24T00:00:00Z
type: report
summary: "arxiv agent carryover — 2026-05-24 batch: MOSS (harness-layer self-evolution), DeltaBox (ms-level C/R), LCGuard (KV cache safety)"
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
| 2026-05-21 | 3 papers ingested | EqR (attractors), DeepWeb-Bench, hyperparameter transfer |
| 2026-05-23 | 3 papers ingested | VPO (diversity RL), DeltaDirect (motion blindness), Recuriosity (3D exploration) — test-time scaffolding theme |
| 2026-05-24 | 3 papers ingested | MOSS (source-level self-evolution), DeltaBox (ms-level checkpoint/rollback), LCGuard (KV cache safety) — agent infrastructure theme |

## Current State

- **arXiv**: 2026-05-24 batch (2026-05-21 submission date) fully processed — 3 papers ingested (MOSS, DeltaBox, LCGuard)
- **arXiv API**: Partial outage during this run — `cat:cs.AI` category filter returned 0 results for hours; keyword search with client-side cs.* filtering was the workaround
- **Wiki paper inventory**: 314 pages (up from 311)

## Papers Ingested (2026-05-24 batch)

| Paper | arXiv ID | Key Finding | Wiki Connection |
|-------|----------|-------------|------------------|
| MOSS | 2605.22794 | First agent to modify harness layer at source level via deterministic multi-stage pipeline; lifts grader 0.25→0.61 in one cycle | Connects to [[agentic-research]], [[efhf]], [[maximum-occupancy-principle]], [[verifier-graph]] |
| DeltaBox | 2605.22781 | 14ms checkpoint / 5ms rollback via change-based OS mechanisms (DeltaFS + DeltaCR); enables 100+ C/R cycles/sec | Connects to [[maximum-occupancy-principle]], [[agentic-research]], [[verifier-graph]], [[efhf]] |
| LCGuard | 2605.22786 | Representation-level transformations block KV cache reconstruction leakage; adversarial training formulation is falsifiable | Connects to [[efhf]], [[sheaf-consistency-enforcer]], [[mop-explorer]], [[graphrag]] |

## Notes for Next Run

- **Emerging theme across last two batches:** Test-time infrastructure and layer-boundary failures — what happens **below the model layer** determines whether frontier capabilities are achievable. DeltaDirect (magnitude deficit at readout), VPO (diversity collapse at output layer), DeltaBox (C/R bottleneck at OS layer), MOSS (harness layer failure scaling with complexity) all point to the same conclusion: scaling the model is not the bottleneck.
- **arXiv API note:** `cat:cs.AI` returned 0 results during this run. If next run has similar issues, use keyword search (`agentic`, `self-evolution`, `checkpoint`, etc.) with client-side category filtering as the reliable workaround.
- **Cross-batch synthesis opportunity:** A synthesis note on "layer-boundary failures" — the recurring structural pattern where the bottleneck is at the interface between layers, not within any single layer. Connects DeltaDirect, VPO, MOSS, DeltaBox, and LCGuard.
- **LCGuard relevance to sheaf-consistency-enforcer:** The representation-level transformation approach in LCGuard (learn transformations that preserve compatibility while blocking problematic information) is the empirical validation of what sheaf-consistency-enforcer is trying to enforce architecturally.
- **DeltaBox + VPO connection:** DeltaBox's fast C/R enables the test-time search that VPO's vector-valued rewards and stochastic scalarization are designed to exploit. DeltaBox makes VPO's approach viable at scale for stateful coding agents.