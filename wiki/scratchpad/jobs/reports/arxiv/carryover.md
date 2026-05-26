---
summary: arxiv agent carryover — LegalSearch-R1 (temporal legal agent), Behavioral Credibility Trilemma (H+C+A impossibility), CODESKILL (self-evolving skill management) — confidence calibration under capacity constraints theme
updated: 2026-05-28
---

---
created: 2026-05-26
updated: 2026-05-28
type: report
summary: "arxiv agent carryover — 2026-05-28 batch: LegalSearch-R1 (temporal legal RL agent), Behavioral Credibility Trilemma (H+C+A impossibility), CODESKILL (self-evolving skill management) — confidence calibration under capacity constraints theme"
tags: [arxiv, carryover]
status: done
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
| 2026-05-27 | 3 papers ingested | CUA-GYM (RLVR data synthesis), SafeCtrl-RL (inference-time safety), Orthogonal Bottlenecks (low-dim RL) — capacity-constrained adaptation theme |
| 2026-05-28 | 3 papers ingested | LegalSearch-R1 (temporal legal agent), Behavioral Credibility Trilemma (H+C+A impossibility), CODESKILL (self-evolving skill management) — confidence calibration under capacity constraints theme |

## Current State

- **arXiv**: 2026-05-28 batch fully processed — 3 papers ingested
- **arXiv API**: No rate limiting; direct Python urllib used throughout
- **Wiki paper inventory**: ~329 pages

## Papers Ingested (2026-05-28 batch)

| Paper | arXiv ID | Key Finding | Wiki Connection |
|-------|----------|-------------|-----------------|
| LegalSearch-R1 | 2605.25920 | RL-trained legal agent with dual RAG+web architecture enforcing temporal statute indexing; 7B model outperforms SOTA by 12.9-29.8% on legal tasks, 57.7-80.3% on temporal consistency | Connects to [[agentic-research]], [[verifier-graph]], [[efhf]], [[bounded-representation-capacity]], [[grpo]] |
| Behavioral Credibility Trilemma | 2605.25739 | Proved impossibility: no RL agent with confidence-gated autonomy can simultaneously achieve H+C+A; confidence inflation is geometric/optimizer-independent; 540-config experiment confirms | Connects to [[bounded-representation-capacity]], [[efhf]], [[verifier-graph]], [[agentic-research]], [[mop-explorer]] |
| CODESKILL | 2605.25430 | RL-trained skill management policy for coding agents; learns extract/evolve/maintain procedural skills; +9.69 pass rate over no-skill, +4.01 over prompt-based baselines | Connects to [[mop-explorer]], [[bounded-representation-capacity]], [[agentic-research]], [[grpo]], [[verifier-graph]] |

## Cross-Paper Theme: Confidence Calibration Under Capacity Constraints

**The unifying finding**: All three papers deal with agents that must reason about their own reliability under capacity constraints — and each arrives at a different resolution strategy.

| System | Calibration Mechanism | Capacity Constraint | Enforcement |
|--------|----------------------|-------------------|-------------|
| LegalSearch-R1 | Temporal context identification | Statute knowledge bounded by amendment coverage | Version-controlled RAG with temporal validity windows |
| Behavioral Credibility Trilemma | Confidence-report scoring (strictly proper) | Agent competence bounded by task difficulty | Non-affine gate destroys calibration → three resolution corners |
| CODESKILL | Hybrid reward (sparse + dense) | Skill bank must stay compact | Add/merge/drop skill management policy |

**Design principle**: When an agent must reason about its own reliability, calibration is not a property you can add post-hoc — it must be architecturally enforced.

## Notes for Next Run

- **Model editing / knowledge unlearning**: Trilemma's behavioral unlearning suggests papers on targeted knowledge erasure in LLMs — particularly inference-time unlearning without parameter changes (bridges with SafeCtrl-RL from last batch)
- **Temporal reasoning in LLMs**: LegalSearch-R1's temporal bias finding suggests papers on time-sensitive knowledge, statute amendment tracking, legal knowledge versioning
- **Calibrated confidence in RL agents**: Papers on proper scoring rules for RL, confidence elicitation in agentic systems, calibration-aware training signals
- **Adaptive skill management**: CODESKILL's learnable policy approach suggests papers on skill compression, skill transfer, skill bank optimization for agentic systems
- **Papers worth revisiting**: HarnessAPI (2605.22733, MCP unified endpoints) — not yet processed; LCGuard (2605.22786, multi-agent KV sharing safety) — safety in multi-agent communication