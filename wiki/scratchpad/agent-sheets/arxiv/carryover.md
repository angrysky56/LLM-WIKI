---
tags: [arxiv, carryover]
updated: 2026-06-11T08:30:00Z
created: 2026-06-10T17:30:00Z
---

# arxiv Agent — Carryover

## Run History

| Date | Result | Notes |
|------|--------|-------|
| 2026-05-18 | 3 papers ingested | EnvFactory, SD-Search, LMAC — credit assignment theme |
| 2026-06-11 | 2 papers ingested (inbox) | PC Layer (2606.06470), RREDCoT (2606.06475) |
| 2026-06-10 | 3 papers ingested (arxiv discovery) | Target-SFT, FutureProbes, ReasonAlloc — hierarchy principle theme |
| 2026-06-11 | 3 papers ingested (arxiv discovery) | MoE MPI, APPO, VToken Routing — structured inductive biases theme |

## Papers Ingested (2026-06-11 — arxiv discovery cycle)

| Paper | arXiv ID | Key Finding | Wiki Page |
|-------|----------|-------------|-----------|
| Redesign MoE Routers w/ MPI | 2606.12397 | "Power-then-Retract" aligns router rows with expert singular directions | [[moe-manifold-power-iteration]] |
| APPO: Agentic Procedural Policy Optimization | 2606.12384 | Procedure-level credit assignment beats action-level for multi-turn tool use | [[appo-agentic-procedural-policy-optimization]] |
| Recoverable Visual Token Routing | 2606.12412 | Active/standby routing with recovery preserves quality while cutting KV-cache | [[recoverable-visual-token-routing]] |

## Cross-Cycle Theme — Structured Inductive Biases

All three papers impose structured information flow pathways on LLM subsystems:
- **Geometric**: MPI aligns router/expert representations
- **Procedural**: APPO segments trajectories into procedures for credit
- **Attentional**: VToken Routing manages token flow with recovery

Meta-principle: reversible + structurally aligned > irreversible + unstructured.

## Last Run

- Date: 2026-06-11T08:30:00Z
- Inbox: Empty
- Discovered: 10 papers from cs.AI, cs.LG, cs.CL
- Selected: 3 (by significance)
- Status: Complete

## What Remains

- [ ] Explore MPI applicability to vision MoEs
- [ ] Investigate APTO procedure-to-function mapping
- [ ] Track VToken routing generalization to video
- [ ] Next cycle suggestion: evaluation methodology papers