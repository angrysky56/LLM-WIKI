---
created: 2026-05-27
updated: 2026-05-27
type: report
summary: arxiv papers researched — CUA-GYM (RLVR data synthesis), SafeCtrl-RL (inference-time safety control), Orthogonal Bottlenecks (low-dimensional RL representations) — capacity-constrained adaptation theme
tags: [arxiv, report]
---

# arxiv Research Report — 2026-05-27

## Papers Processed

### 2605.25624 — CUA-GYM
RLVR (Reinforcement Learning with Verifiable Rewards) data synthesis pipeline for computer-use agents. Three adversarially coupled agents (Generator, Discriminator, Orchestrator) co-generate task instructions, environment states, and reward functions from a shared topic specification. Information barrier prevents reward hacking. Produces 32,112 verified tuples across 110 environments. GSPO-trained Qwen3.5-A3B reaches 62.1% OSWorld-Verified; A17B reaches 72.6%. Key finding: environment diversity is an independent scaling axis — expanding from 10→80 environments yields gains that data volume alone cannot recover.

### 2605.25984 — SafeCtrl-RL
Inference-time behavioral control via RL-driven prompt optimization. 11 discrete prompt adjustment strategies selected by RL agent based on 36-D state encoding dialogue dynamics. Joint reward via `r = q^αβ · s^(1-α)β` with hard safety gating (zero reward for critical safety violations regardless of quality). Model-agnostic, black-box compatible. Key finding: inference-time behavioral unlearning without parameter modification; safety threshold enforcement analogous to constrained RL where safety violations are infeasible actions.

### 2605.26012 — Orthogonal Bottlenecks for RL
Fixed orthonormal projection constrains RL encoder representations to low-dimensional subspace. Under linear realizability assumption, k ≥ r (bottleneck dim ≥ intrinsic rank of optimal value function) preserves expressivity and gradient dynamics. Across Classic Control, Atari, MuJoCo, Meta-World: baseline performance recovered once k exceeds small task-dependent threshold; value representations often compress to extremely low dimensions. Fixed > learned projections — learned can cause representation collapse. Key finding: deep RL representations can be faithfully compressed into orthogonal subspaces; minimal sufficient dimension depends on environment complexity, not encoder width.

## Cross-Paper Theme: Capacity-Constrained Adaptation

All three papers share a structural pattern: **bounded adaptation with capacity-constrained enforcement**.

| System | Adaptation Target | Capacity Constraint | Enforcement |
|--------|------------------|---------------------|--------------|
| CUA RLVR (CUA-GYM) | Environment state + reward function | Information barrier + adversarial synthesis | Isolated Discriminator cannot see Generator |
| LLM behavior (SafeCtrl-RL) | System prompt | Hard safety threshold | Zero reward on critical violations |
| RL representation (Orthogonal Bottlenecks) | Encoder features | Bottleneck dimension k ≥ r | Fixed orthonormal projection |

The common principle: **when adapting a bounded system, enforce capacity constraints at the adaptation point, not just the output.** CUA-GYM enforces at the reward writer (Discriminator isolated from setup). SafeCtrl-RL enforces at the reward evaluation (hard floor on safety regardless of quality). Orthogonal Bottlenecks enforces at the representation level (k ≥ r threshold on intrinsic rank).

**Next cycle search direction:** papers on model editing, knowledge unlearning, skill compaction, or uncertainty-aware verification — all extend the capacity-constrained adaptation theme. Also: CUA-GYM's environment diversity as independent scaling axis suggests papers on environment design principles for RL.

## Wiki Pages Written

- `wiki/sources/papers/cua-gym.md`
- `wiki/sources/papers/safectrl-rl.md`
- `wiki/sources/papers/orthogonal-bottlenecks-rl.md