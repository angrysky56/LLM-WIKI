---
summary: arxiv agent carryover — CUA-GYM, SafeCtrl-RL, Orthogonal Bottlenecks — capacity-constrained adaptation theme
updated: 2026-05-27
---

---
created: 2026-05-26
updated: 2026-05-27
type: report
summary: "arxiv agent carryover — 2026-05-27 batch: CUA-GYM (agentic RLVR data synthesis), SafeCtrl-RL (inference-time safety), Orthogonal Bottlenecks (low-dim RL) — capacity-constrained adaptation theme"
tags: [arxiv, carryover]
status: done
confidence: high
---

# arxiv Agent — Carryover

## Run History

||| Date | Result | Notes |
|||------|--------|-------|
||| 2026-05-18 | 3 papers ingested | EnvFactory, SD-Search, LMAC — credit assignment theme |
||| 2026-05-20 | No new papers | arXiv late-UTC batch not yet posted |
||| 2026-05-21 | 3 papers ingested | EqR (attractors), DeepWeb-Bench, hyperparameter transfer |
||| 2026-05-23 | 3 papers ingested | VPO (diversity RL), DeltaDirect (motion blindness), Recuriosity (3D exploration) — test-time scaffolding theme |
||| 2026-05-24 | 3 papers ingested | ProxySHAP (Shapley/Banzhaf), Boiling the Frog (agentic safety), CUSP (scientific forecasting) — verification/trust theme |
||| 2026-05-27 | 3 papers ingested | CUA-GYM (RLVR data synthesis), SafeCtrl-RL (inference-time safety), Orthogonal Bottlenecks (low-dim RL) — capacity-constrained adaptation theme |

## Current State

- **arXiv**: 2026-05-27 batch fully processed — 3 papers ingested
- **arXiv API**: No rate limiting; direct Python urllib used throughout
- **Wiki paper inventory**: ~326 pages

## Papers Ingested (2026-05-27 batch)

| Paper | arXiv ID | Key Finding | Wiki Connection |
|-------|----------|-------------|-----------------|
| CUA-GYM | 2605.25624 | Agentic co-generation pipeline for CUA RLVR data — 32K verified tuples, 110 envs; environment diversity is independent scaling axis; Qwen3.5-A3B→62.1% OSWorld-Verified | Connects to [[efhf]], [[agentic-research]], [[mop-explorer]], [[verifier-graph]], [[bounded-representation-capacity]] |
| SafeCtrl-RL | 2605.25984 | Inference-time RL-driven prompt optimization — 11 strategies, 36-D state, hard safety gating with zero reward on critical violations; behavioral unlearning without parameter change | Connects to [[bounded-representation-capacity]], [[verifier-graph]], [[agentic-research]] |
| Orthogonal Bottlenecks | 2605.26012 | Fixed orthonormal projection constrains RL encoder to low-dim subspace; k ≥ r preserves expressivity; minimal sufficient dim depends on env complexity not encoder width | Connects to [[bounded-representation-capacity]], [[maximum-occupancy-principle]], [[mop-explorer]] |

## Cross-Paper Theme: Capacity-Constrained Adaptation

**The unifying finding**: All three papers implement adaptation with capacity constraints enforced at the adaptation point, not the output.

| System | Adaptation Target | Capacity Constraint | Enforcement |
|--------|------------------|---------------------|--------------|
| CUA RLVR (CUA-GYM) | Environment state + reward function | Information barrier + adversarial synthesis | Isolated Discriminator cannot see Generator |
| LLM behavior (SafeCtrl-RL) | System prompt | Hard safety threshold | Zero reward on critical violations regardless of quality |
| RL representation (Orthogonal Bottlenecks) | Encoder features | Bottleneck dimension k ≥ r (intrinsic rank) | Fixed orthonormal projection |

**Design principle**: When adapting a bounded system, enforce capacity constraints at the adaptation point, not just the output.

## Notes for Next Run

- **Model editing / knowledge unlearning**: SafeCtrl-RL's inference-time behavioral unlearning suggests papers on targeted knowledge erasure or unlearning in LLMs; bridges capacity-constrained adaptation with the bounded representation theme
- **Skill compaction / compression**: CUA-GYM's environment diversity as independent scaling axis suggests papers on compact skill representations or skill compression for transfer; connects to SkillOpt/SkillLens from prior batch
- **Uncertainty-aware verification**: SafeCtrl-RL's hard safety gating parallels SNR-based capacity thinking from Shannon Scaling Law; papers on calibrated confidence or uncertainty-aware verification would deepen the capacity thread
- **Papers worth revisiting**: HarnessAPI (2605.22733, MCP unified endpoints) — was in prior notes but not yet processed; LCGuard (2605.22786, multi-agent KV sharing safety) — safety in multi-agent communication