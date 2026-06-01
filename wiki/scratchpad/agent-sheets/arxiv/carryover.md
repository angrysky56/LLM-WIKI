---
created: 2026-05-26T00:00:00Z
updated: 2026-06-01T14:30:00Z
type: report
summary: "arxiv agent carryover — 2026-06-01 batch: ReuseRL (MDL-grounded skill reuse), AutoSci (memory-centric research lifecycle), Stateful Monitoring (catches distributed agent attacks). Agent architecture + oversight theme — structural reuse as the unit of trustworthiness."
tags: [arxiv, carryover]
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
| 2026-05-24 | 3 papers ingested | ProxySHAP (Shapley/Banzhaf), Boiling the Frog (agentic safety), CUSP (scientific forecasting) — verification/trust theme |
| 2026-05-26 | 3 papers ingested | Shannon Scaling Law, SkillOpt, SkillLens — bounded representation capacity |
| 2026-05-26 (new) | 3 papers ingested | StepOPSD, AKBE, PRISM — instance-level behavioral decomposition |
| 2026-05-27 | 3 papers ingested | MATCHA, FinHarness, Interaction SSD — evaluation infrastructure |
| 2026-05-27 (additional) | 6 papers processed | Real Images, Chartographer, Demographic Info + top 3 |
| 2026-05-28 | 3 papers ingested | CCO, Gamma-World, BES — constraint satisfaction under distribution shift |
| 2026-05-29 | 3 papers ingested | Gram, SoundnessBench, Entropy-Cut MH — evaluation infrastructure |
| 2026-05-31 | No new batch | No new arXiv submissions today — API returned only 2026-05-28 papers already processed. |
| **2026-06-01** | **3 papers ingested** | **ReuseRL, AutoSci, Stateful Monitoring — agent architecture + oversight** |

## Current State

- **arXiv**: 2026-06-01 batch fully processed — 3 papers ingested
- **Wiki paper inventory**: ~94 pages in `wiki/sources/papers/` (added reuserl-skill-reuse-compression, autosci-memory-centric-research-lifecycle, stateful-monitoring-distributed-agent-attacks)
- **arXiv API**: Still aggressive rate limiting; required sleep+backoff to merge cs.AI+cs.LG+cs.CL queries

## Papers Ingested (2026-06-01 batch)

| Paper | arXiv ID | Key Finding | Wiki Connection |
|-------|----------|-------------|------------------|
| ReuseRL | 2605.31509 | MDL penalty via skill-dictionary extraction from successful trajectories; PAC-Bayes bound; pure round-length penalty collapses (74% burned) | Connects to [[skillopt-self-evolving-2026]], [[skill-consumption-2026]], [[codeskill]], [[muse-autoskill]], [[stepopsd]], [[akbe]] — theoretical anchor for skill theme |
| AutoSci | 2605.31468 | 4-module system (SciMem + SciFlow + SciDAG + SciEvolve) for full scientific research lifecycle; ICLR scores 6.3/10 (GPU kernels) and 5.8/10 (drug discovery) | Connects to [[physics-is-all-you-need]], [[why-llms-arent-scientists-yet]], [[soundnessbench-ai-scientist-2026]], [[deepweb-bench-2026]], [[xu-envfactory-2026]] — system-level culmination of trustworthy-scientific-AI theme |
| Stateful Monitoring | 2605.31593 | First distributed agent attack; gpt-oss-120b 0%→36.7-40% via scaffold; online stateful monitor catches 30% earlier with stream clustering; also catches standard jailbreaks | Connects to [[boiling-frog-agentic-safety-2026]], [[gram-sabotage-alignment-auditing-2026]], [[calibrating-conservatism-scalable-oversight-2026]], [[finharness]], [[alignment-tampering]] — architectural level of oversight theme |

## Cross-Paper Theme: Agentic Systems in Three Layers — Structural Reuse as the Unit of Trustworthiness

| Layer | Paper | Architectural Lever |
|-------|-------|---------------------|
| **Training** (how the agent learns) | ReuseRL | MDL-grounded skill-dictionary penalty; PAC-Bayes generalisation |
| **Runtime** (how the agent executes) | AutoSci | Schema-governed persistent memory + lifecycle harness + DAG augmentation + self-evolution |
| **Oversight** (how the agent is monitored) | Stateful Monitoring | Stream clustering across user accounts; new class of safety monitor |

**Design principle:** All three layers converge on the same idea — **structural reuse is the unit of trustworthiness**:
- ReuseRL uses structural reuse as a training regulariser
- AutoSci uses it as a memory substrate (skill entities, DAG templates, lifecycle stages)
- Stateful Monitoring uses it as a detection signal (attackers reuse patterns across accounts → monitor catches it)

## Kanban Status

### Prior Cycle Open Items (from 2026-05-29 carryover)

1. **Gram overeagerness finding — connection to CCO's calibrated conservatism** — **Resolved** (see last carryover)
2. **SoundnessBench optimism bias — cross-reference with autonomous research agent literature** — **Resolved** (see last carryover)

### This Cycle

- [x] Prior cycle items remain resolved
- [x] New theme emerging: Structural Reuse as the Unit of Trustworthiness — three papers converge on this
- [x] Wiki pages cross-linked to existing concept/sources pages only (no broken wikilinks)

## Notes for Next Run

- **arXiv rate limiting**: Still aggressive this cycle — multiple 429s and timeouts. Used single-category queries with sleep+backoff. Consider adding API key or larger backoff windows.
- **New theme**: Agentic systems in three layers (training / runtime / oversight) with structural reuse as the unifying concept. Worth a synthesis page if not already covered.
- **PDF storage**: `/home/ty/Documents/paper-research/processed/` for the three 2026-06-01 PDFs
- **Inbox**: Empty — no manual processing needed

## What Remains

- [ ] (Optional) Create synthesis page on "Structural Reuse as Unit of Trustworthiness" if not yet covered in synthesis/
- [ ] (Optional) Add incoming wikilinks from related wiki pages to the three new source pages (currently orphans — only have outgoing links)
- [ ] (Pending) Researcher tasks from 2026-05-30 carryover: STV vs RiM comparison, Physics vs LLMSurgeon comparison, Predictive adequacy vs explanatory correctness

## Last Run

2026-06-01 14:30 UTC — 3 papers processed from 2026-05-29 batch: ReuseRL (MDL-grounded skill reuse), AutoSci (memory-centric research lifecycle), Stateful Monitoring (catches distributed agent attacks).