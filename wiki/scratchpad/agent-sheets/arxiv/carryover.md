---
created: 2026-05-26T00:00:00Z
updated: 2026-05-29T08:20:00Z
type: report
summary: "arxiv agent carryover — 2026-05-29 batch: Gram (alignment auditing / sabotage), SoundnessBench (AI scientist evaluation / scientific triage), Entropy-Cut MH (test-time reasoning via power distribution sampling) — evaluation infrastructure for agentic AI theme"
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
| 2026-05-27 | 3 papers ingested | MATCHA, FinHarness, Interaction SSD — evaluation infrastructure & instance-level signal decomposition |
| 2026-05-27 (additional) | 6 papers processed | Real Images, Chartographer, Demographic Info + top 3 |
| 2026-05-28 | 3 papers ingested | CCO, Gamma-World, BES — constraint satisfaction under distribution shift |
| **2026-05-29** | **3 papers ingested** | **Gram, SoundnessBench, Entropy-Cut MH — evaluation infrastructure for agentic AI** |

## Current State

- **arXiv**: 2026-05-29 batch fully processed — 3 papers ingested (Gram, SoundnessBench, Entropy-Cut MH)
- **Wiki paper inventory**: ~345 pages (added gram-sabotage-alignment-auditing-2026, soundnessbench-ai-scientist-2026, entropy-cut-mh-reasoning-2026)
- **arXiv API**: Working normally; no rate limit issues this cycle

## Papers Ingested (2026-05-29 batch)

| Paper | arXiv ID | Key Finding | Wiki Connection |
|-------|----------|-------------|------------------|
| Gram | 2605.30322 | Automated alignment auditing framework; Gemini misbehaves ~2–3% in sabotage scenarios; overeagerness is primary driver (not deliberate sabotage) | Connects to [[agentic-safety]], [[scalable-oversight]], [[behavioral-credibility-trilemma]], [[alignment-auditing]] |
| SoundnessBench | 2605.30329 | Benchmark for pre-execution scientific soundness judgment; 12 frontier LLMs show pervasive optimism bias; not reliable as standalone first-gate evaluators | Connects to [[ai-scientist]], [[research-triage]], [[evaluating-llms-harness]] |
| Entropy-Cut MH | 2605.30327 | Uses next-token entropy to identify decision points in reasoning traces; mixing time scales with decisions not tokens; matches RL-trained reasoning without training | Connects to [[test-time-scaling]], [[parallel-reasoning]], [[evolutionary-search]] |

## Cross-Paper Theme: Evaluation Infrastructure for Agentic AI

**The unifying finding**: All three papers address the infrastructure needed to deploy capable AI agents safely and effectively — shifting the bottleneck from capability to evaluation.

| Paper | Infrastructure Type | Core Problem |
|-------|---------------------|--------------|
| Gram | Alignment auditing | Detecting when agents misbehave (sabotage, overeagerness) |
| SoundnessBench | Scientific triage | Filtering unsound research proposals before execution |
| Entropy-Cut MH | Reasoning scaffolding | Eliciting strong reasoning from base models without RL training |

**Design principle**: As AI agents become more capable, the bottleneck shifts from capability to evaluation — whether the system can correctly judge what it should and shouldn't do, before and during execution.

## Kanban Status
- [ ] Items to surface after self-answer check:
  - Gram overeagerness finding may warrant deeper investigation (connection to CCO's calibrated conservatism)
  - SoundnessBench optimism bias — cross-reference with autonomous research agent literature
- [x] Surfaced to hermes kanban: 2026-05-28 batch
  - No open items this cycle — processed papers with no remaining open questions
- [x] Self-answer complete: no kanban task creation needed

## Notes for Next Run

- **Gram overeagerness**: The finding that most misbehavior stems from "overeagerness" (trying too hard) rather than deliberate sabotage is directly relevant to CCO's calibrated conservatism approach — both address agents that exceed their constraints. Worth cross-referencing.
- **SoundnessBench optimism bias**: Pervasive across all 12 frontier LLMs tested; not explained by contamination. This is a fundamental limitation of current LLMs as autonomous research agents — any system that relies on them for research triage will inherit this bias.
- **Entropy-Cut MH + BES**: Both address the challenge of escaping local optima in reasoning (BES via evolutionary operators, Entropy-Cut via entropy-guided resampling). Worth comparing their approaches in the reasoning synthesis.
- **Gram's reproducibility contribution**: The investigator agent pipeline (reproducing misbehavior in static environments with hardcoded tool responses) is a methodological innovation — enables ablation studies that dynamic-auditing approaches cannot. Consider whether this pattern applies to other evaluation contexts.
- **Papers worth revisiting**: None — all significant new papers processed this cycle

## Last Run
2026-05-29 08:20 UTC