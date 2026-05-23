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
|| 2026-05-23 | 3 papers ingested | VPO (diversity RL), DeltaDirect (motion blindness), Recuriosity (3D exploration) — test-time scaffolding theme |

## Current State

- **arXiv**: 2026-05-23 batch (dated 2026-05-21) fully processed — 3 papers ingested (VPO, DeltaDirect, Recuriosity)
- **arXiv submission cycle**: Mon–Fri late-UTC afternoon/evening. Next batch likely 2026-05-26 (Monday). Weekend gap expected.
- **Wiki paper inventory**: 3 new pages from 2026-05-23 batch are current

## Papers Ingested (2026-05-23 batch — just processed)

| Paper | arXiv ID | Key Finding | Wiki Connection |
|-------|----------|-------------|------------------|
| Vector Policy Optimization (VPO) | 2605.22817 | Replaces GRPO scalar collapse with vector-valued rewards + stochastic scalarization; unlocks evolutionary search that GRPO cannot solve at any budget | Connects to [[agentic-research]], [[maximum-occupancy-principle]], [[verifier-graph]] |
| DeltaDirect | 2605.22823 | Direction binding gap in Video-LLMs is a readout failure (99.8% decodable, ~25% QA); projector-level aux objective fixes magnitude deficit; +59.5pp accuracy | Connects to [[efhf]], [[sheaf-consistency-enforcer]], [[verifier-graph]] |
| Recuriosity | 2605.22814 | Online 3DGS persistent world model + episodic RGB transformer; fixes amnesiac curiosity failure; zero-shot generalization to Gibson/AI worlds | Connects to [[mop-explorer]], [[maximum-occupancy-principle]], [[agentic-research]] |

## Notes for Next Run

- **Next batch**: Likely 2026-05-26 (Monday) — weekend gap; no papers on Saturday/Sunday
- **Emerging theme across recent papers**: **test-time computation as bottleneck** (VPO: diversity at output layer; DeltaDirect: readout binding; Recuriosity: world model persistence) — these all point to internal scaffolding that scaling alone doesn't fix
- **Thematic thread**: binding/magnitude failures recur across modalities (DeltaDirect: direction binding; VPO: reward collapse is a similar binding failure to scalarized optimization); worth a cross-paper synthesis note
- **Carryover note**: DeltaDirect's "magnitude deficit not geometry loss" finding is directly relevant to [[maximum-occupancy-principle]] — readout layer failures where representation is correct but not correctly bound to output are a recurring structural pattern
