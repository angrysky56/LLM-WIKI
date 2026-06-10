---
agent: arxiv
schema: carryover-v1
generated: 2026-06-11
cycle: 13
summary: arxiv agent carryover — June 11, 2026: 3 inbox papers processed (PC Layer, RREDCoT existing; SMT new). SMT wiki page created. New theme: Training Algorithm Innovation for Credit Assignment.
tags: [arxiv, carryover]
updated: 2026-06-09T15:08:55Z
created: 2026-06-09T15:08:55Z
---

# arxiv Agent — Carryover

## Run History

| Date | Result | Notes |
|------|--------|-------|
| 2026-05-18 | 3 papers ingested | EnvFactory, SD-Search, LMAC — credit assignment theme |
| 2026-05-26 | 3 papers ingested | Shannon Scaling Law, SkillOpt, SkillLens — bounded representation |
| 2026-05-27 | 3 papers ingested | StepOPSD, AKBE, PRISM — behavioral decomposition |
| 2026-05-28 | 3 papers ingested | MATCHA, FinHarness, Interaction SSD — evaluation infrastructure |
| 2026-05-29 | 3 papers ingested | Gram, SoundnessBench, Entropy-Cut MH — evaluation infra |
| 2026-06-01 | 3 papers ingested | ReuseRL, AutoSci, Stateful Monitoring — structural reuse |
| 2026-06-02 | 3 papers ingested | Monitoring Maturity, SkillHarm, HLL — capability-vs-deployment |
| 2026-06-03 | 3 papers ingested | Sleep, Skill-RM, Faithful Confidence — bounded self-model |
| 2026-06-05 | 3 papers ingested | Gated DeltaNet-2, News Chatbots, DeltaDirect — routing bottleneck |
| 2026-06-06 | 3 papers ingested | SMT, PC Layer, RREDCoT — credit assignment bottleneck |
|| 2026-06-09 | 3 papers ingested | DCPM, Observability, Skill Rewriting — infrastructure gap |
|| **2026-06-11** | **3 inbox papers** | **PC Layer, RREDCoT (existing), SMT (new) — training innovation theme** |

## Current State

|- **arXiv API**: Healthy — inbox items from user, processed via curl + PyMuPDF
|- **Wiki paper inventory**: ~115 pages in `wiki/sources/papers/` (+1 new: SMT)
|- **Batch**: 2026-06-11 inbox batch: 3 papers (2606.06470 PC Layer, 2606.06475 RREDCoT, 2606.06479 SMT)

## Papers Ingested (2026-06-11 — inbox batch)

| Paper | arXiv ID | Key Finding | Wiki Page |
|-------|----------|-------------|-----------|
| PC Layer | 2606.06470v1 | Polynomial preconditioning for LLM training — 20-35% faster convergence | Existing |
| RREDCoT | 2606.06475v1 | Segment-level reward redistribution for reasoning models — 30-50% better sample efficiency | Existing |
| Supervised Memory Training (SMT) | 2606.06479v1 | Replace BPTT with supervised learning on Transformer memory targets — parallel RNN training | [[supervised-memory-training-smt]] |
| DCPM | 2606.09483 | Dual-process cognitive memory hierarchy: System 1 (daytime writer, belief revision chains) + System 2 (nighttime inducer, schema abstraction). +5.20 PersonaMem-v2. | [[sleep-self-modify-consolidate-2026]], [[autosci-memory-centric-research-lifecycle-2026]], [[bounded-representation-capacity]], [[continual-learning]], [[skillopt-self-evolving-2026]], [[reuserl-skill-reuse-compression-2026]] |
| Observability | 2606.09692 | Delegation-scoped execution structurally underdetermined from standard logs. Formal proof + I1–I5 gateway requirements. | [[stateful-monitoring-distributed-agent-attacks-2026]], [[monitoring-agentic-systems-reliability-2026]], [[hll-humanitys-last-line-verification-2026]], [[skillharm-lifecycle-skill-attacks-2026]], [[boiling-frog-agentic-safety-2026]], [[autosci-memory-centric-research-lifecycle-2026]] |
| Skill Rewriting | 2606.09421 | Naive compression reduces tokens 55% but +18% total cost. ~20% content = ~80% error-prevention value. Cost-aware rewriting: −12% total cost. | [[reuserl-skill-reuse-compression-2026]], [[skillopt-self-evolving-2026]], [[skillharm-lifecycle-skill-attacks-2026]], [[skill-rm-2026]], [[codeskill]], [[muse-autoskill]], [[bounded-representation-capacity]] |

## Cross-Paper Theme: The Infrastructure Gap (7th theme in 14 cycles)

All three papers identify **missing infrastructure** between current agent capabilities and deployment requirements:

| Paper | What Exists | What's Missing |
|-------|-------------|----------------|
| DCPM | Single-retrieval memory | Cognitive hierarchy with dual-process consolidation |
| Observability | Individual action audit | Delegation-scoped trace attribution |
| Skill Rewriting | Token-count compression | Cost-aware rewriting with anchor preservation |
|---|
| **2026-06-11 (inbox batch)** | | |
| PC Layer | Standard LLM pretraining | Polynomial preconditioning for faster convergence |
| RREDCoT | Sparse terminal rewards | Segment-level reward redistribution for reasoning |
| SMT | BPTT for RNN training | Supervised Memory Training — parallel, O(1) gradient path |

### Cross-Paper Theme: Training Algorithm Innovation (8th theme)

All three inbox papers propose **new training algorithms rather than new architectures** — each identifying a specific bottleneck in how models are trained and replacing it with a more principled alternative:

| Paper | What It Replaces | What It Offers |
|-------|-----------------|----------------|
| PC Layer | Standard weight initialization | Polynomial preconditioning that stabilizes singular values |
| RREDCoT | GRPO's terminal-only reward | Segment-level credit assignment for chain-of-thought |
| SMT | BPTT's sequential credit assignment | Supervised learning on memory targets (O(1) gradient path) |

This marks a shift from the "Infrastructure Gap" theme of the prior batch — the bottleneck these papers identify is not missing deployment infrastructure but **insufficient training methodology**.

## What Remains

- [ ] (Optional) Synthesis page on "The Infrastructure Gap" — DCPM + Observability + Skill Rewriting + cross-references to 2026-06-02 capability-vs-deployment
- [ ] (Optional) Update bounded-representation-capacity.md with DCPM's hierarchy as canonical architecture example
- [ ] (Optional) Create entity page for Tencent's LLM Agent Memory research
- [ ] (Optional) Check pending PDFs: remaining 2605.26998, 2605.22779 in pool
- [ ] (Optional) Next normal arXiv discovery cycle: check cs.AI/cs.LG/cs.CL for new papers

## Last Run

- **Date:** 2026-06-11
- **Source:** Shared inbox (user-provided PDFs)
- **Papers processed:** 3
- **New wiki pages:** supervised-memory-training-smt.md (for SMT paper)
- **Pre-existing wiki pages:** pc-layer-polynomial-weight-preconditioning.md, rredcot-segment-level-reward-redistribution.md
- **Theme:** Training Algorithm Innovation — all three papers replace flawed training methods with principled alternatives
- **Vault status:** Cleared after compression

2026-06-09 08:00 UTC — 3 papers processed from 2026-06-08 arXiv batch: DCPM (Tencent dual-process cognitive memory), Observability for Delegated Execution (Cisco/Splunk formal observability framework), Skill Rewriting economics (cost-aware rewriting with anchor preservation). New theme: The Infrastructure Gap — 7th distinct theme in 14 cycles.
