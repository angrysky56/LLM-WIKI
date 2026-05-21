---
summary: Equilibrium Reasoners: test-time scaling via learned attractor landscapes, 2.6%→99% on Sudoku-Extreme
tags: [paper, reasoning, test-time-compute, attractors, latent-dynamics]
updated: 2026-05-21T16:53:06Z
created: 2026-05-21T16:53:06Z
---

---
created: 2026-05-21T16:50:00Z
updated: 2026-05-21T16:50:00Z
type: source
summary: "Equilibrium Reasoners (EqR): iterative latent reasoning via learned attractor landscapes — test-time compute scaling without verifiers, 2.6%→99% on Sudoku-Extreme"
tags: [paper, reasoning, test-time-compute, attractors, latent-dynamics, cs-LG]
sources: https://arxiv.org/abs/2605.21488
status: active
confidence: high
---

# Equilibrium Reasoners: Learning Attractors Enables Scalable Reasoning

**Authors**: Benhao Huang, Zhengyang Geng, Zico Kolter (CMU / Meta AI)

## Core Insight

Generalizable reasoning in iterative latent models arises from **learned task-conditioned attractors** — latent dynamical systems whose stable fixed points correspond to valid solutions. The paper formalizes this as **Equilibrium Reasoners (EqR)**, enabling test-time compute scaling without external verifiers or task-specific priors.

## Key Claims

| Claim | Evidence |
|-------|----------|
| Generalizable reasoning = convergence to solution-aligned attractors | Ablations show gains tightly coupled with attractor convergence |
| Test-time scaling via two axes: depth (more iterations) + breadth (stochastic aggregation) | Both axes improve accuracy independently |
| Adaptive compute: simple cases converge in 1–5 steps; hard cases benefit from massive scaling | Up to 40,000 equivalent layers tested |
| Sudoku-Extreme: 2.6% (feedforward) → 99%+ (EqR with 40K layers) | Dramatic lift on extreme reasoning task |
| Attractor perspective explains why iterative models generalize beyond memorization | Mechanistic lens rather than engineering hack |

## Mechanism

EqR treats the neural network as a **latent dynamical system**. At each iteration step, the state moves toward the nearest attractor basin. Solution quality depends on whether the converged attractor is aligned with a valid solution — learned during training, generalized at test time.

Two scaling axes:
- **Depth**: more iterative updates (equivalent to more "layers" in a single unroll)
- **Breadth**: aggregate stochastic trajectories from multiple random initializations

## Why This Matters

1. **No verifier needed** — unlike o1-style reasoning which requires a trained verifier, EqR relies purely on learned attractor geometry
2. **Connects to molecular CoT** — the three-bond structure (Deep-Reasoning backbone, Self-Reflection fold-back, Self-Exploration basin) in Chen et al. 2026 maps naturally onto attractor dynamics: reasoning steps as gradient descent toward fixed points
3. **Self-prompting connection** — if attractor landscapes are learned and structured, then self-directed compute allocation (the core of self-prompting) can be understood as navigation in that landscape, not arbitrary meta-learning
4. **Interpretability angle** — attractor basins are empirically observable; the paper provides a framework for mechanistic study of what "thinking longer" actually does

## Connections

- [[chen-molecular-cot-2026]] — molecular CoT three-bond structure maps onto attractor basin topology
- [[self-prompting-via-production-stage-architecture]] — self-directed compute = attractor navigation
- [[bae-mor-2025]] — MoR's dynamic recursion depth routing may implement multi-scale attractor traversal
- [[load-bearing-reasoning]] — attractor fixed points are the load-bearing reasoning outcomes; scaffolding tokens maintain basin structure

## Caveats

- Sudoku-Extreme is a synthetic task; generalization to open-ended reasoning unclear
- No external verifier means attractor quality is entirely learned — brittle if training distribution doesn't cover target reasoning patterns
