---
created: 2026-05-27
updated: 2026-05-27
type: source
summary: "Fixed orthonormal bottlenecks preserve RL expressivity and stabilize representations — once bottleneck dim exceeds task intrinsic rank, performance recovers; orthogonal projections yield higher effective rank"
tags: [reinforcement-learning, representation-learning, orthogonal-bottleneck, low-dimensional-structure, manifold-hypothesis]
sources: https://arxiv.org/abs/2605.26012
status: active
confidence: high
---

# Learning in Low-Dimensional Subspaces: Orthogonal Bottlenecks for Reinforcement Learning

**arXiv:** 2605.26012v1 | **Date:** 2026-05-25 | **Categories:** cs.LG, cs.AI

## Metadata

| Field | Value |
|-------|-------|
| Authors | Aleksandar Todorov, Matthia Sabatelli |
| Institution | University of Groningen |
| Contact | a.todorov.4@student.rug.nl, m.sabatelli@rug.nl |

## Executive Summary

The paper studies a simple architectural prior for deep RL: inserting a fixed orthonormal projection (B^T ∈ ℝ^{D×k}, B^T B = I_k) between the encoder and downstream policy/value heads, constraining representations to a low-dimensional orthogonal subspace without auxiliary objectives, pretraining, or changes to the underlying RL algorithm. Under a linear realizability assumption, the authors prove that when the bottleneck dimension k meets or exceeds the intrinsic rank r of the optimal value function in feature space, the bottleneck preserves expressivity and leaves induced gradient dynamics unchanged. Empirically, across Classic Control, Atari, Brax MuJoCo, and Meta-World benchmarks, baseline performance is either matched or improved once k exceeds a small task-dependent threshold; value representations can often be compressed to extremely low dimensions without loss. Fixed orthogonal bottlenecks stabilize feature norms and yield higher effective rank compared to trainable projections, which can be unstable and cause representation collapse.

## Technical Approach

**Architecture:** After encoding state to features z ∈ ℝ^D, a fixed orthonormal projection constrains to h = B^T z ∈ ℝ^k, fed to all downstream heads. No changes to RL algorithm or training objective.

**Theoretical result (linear realizability):** If the optimal value function V* is linearly realizable in feature space with intrinsic rank r, then:
1. A fixed orthogonal bottleneck of dimension k ≥ r preserves full expressivity
2. The induced gradient dynamics are equivalent to an explicit low-dimensional parameterization

**Key property:** Orthogonal projections are non-expansive (Johnson-Lindenstrauss lemma) — approximately preserve distances with high probability; orthogonal weight matrices improve conditioning and gradient propagation through non-expansiveness.

**Diagnostic metrics:**
- Feature norm stability
- Effective rank of representations
- Performance recovery curves as bottleneck dimension increases

## Key Results

- Baseline performance recovered once bottleneck dimension exceeds task-dependent threshold (often very low k)
- Minimal sufficient dimension depends far more on environment complexity than encoder width
- Fixed orthogonal bottlenecks stabilize feature norms and are associated with higher effective rank
- Learned/trainable projections can be unstable — representation collapse observed in some regimes
- In small domains: visualized low-dimensional value manifolds
- In larger benchmarks: sharp performance recovery as bottleneck dimension increases

## Wiki Connections

- [[bounded-representation-capacity]] — Orthogonal bottleneck as explicit capacity constraint; once k ≥ r (intrinsic rank), capacity is sufficient; beyond that, additional dimension is wasteful
- [[maximum-occupancy-principle]] — Value manifold compression mirrors MOP occupancy planning; both exploit low-dimensional structure in high-dimensional representations
- [[mop-explorer]] — The paper's insight that minimal sufficient dimension depends on environment complexity parallels capacity planning for bounded representations

## Related
- [[index]]
- [[sources/papers/orthogonal-bottlenecks-rl]]

- [[orthogonal-bottlenecks-rl]]

## Key Quotes

> "Deep reinforcement learning representations can often be faithfully compressed into low-dimensional orthogonal subspaces, and that fixed orthogonal bottlenecks offer a simple mechanism for shaping representation geometry."

> "Under a linear realizability assumption, we prove that when the optimal value function is realizable by a linear map in feature space, inserting a fixed orthonormal bottleneck whose dimension meets or exceeds the intrinsic rank does not reduce representational capacity and yields learning dynamics equivalent to an explicit low-dimensional parameterization."

> "Fixed orthogonal bottlenecks stabilize feature norms and are associated with higher effective rank, while learned projections can be unstable in some regimes."