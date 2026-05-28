---
created: 2026-05-26
updated: 2026-05-26
type: source
summary: "EM framework with O(nK) E-step for multi-intention IRL using a recurrent gating network; recovers discrete nameable intentions with closed-form per-intention reward recovery"
tags: [inverse-reinforcement-learning, intention-switching, multi-task-learning, recurrent-network, robotics]
sources: https://arxiv.org/abs/2605.26998
status: active
confidence: high
---

# Probabilistic Recurrent Intention Switching Model

## Executive Summary

PRISM addresses the assumption in standard IRL that a single stationary reward drives all behavior — ignoring goal switches within an episode. It replaces memoryless Markov chain models (HIQL) and fixed-window history augmentation (SWIRL) with a lightweight recurrent network mapping observation history to per-step intention distributions. The key result: a provably exact EM decomposition yielding independent per-intention reward subproblems solvable in closed form, with an O(nK) E-step and ~50K trainable parameters. PRISM recovers nameable, temporally coherent intentions from unlabeled demonstrations across mouse labyrinth, frustration gridworld, and BridgeData V2 robotic manipulation.

## Technical Approach

**Core problem**: Real agents switch between discrete intentions within a single episode (seeking water vs. returning home; reaching vs. grasping vs. placing). Standard IRL conflates all objectives into one stationary reward. Prior multi-intention IRL approaches (HIQL, SWIRL, DIRL) either assume memoryless transitions or use fixed history windows that don't scale.

**PRISM framework**:
- A recurrent gating network fθ maps observation history to a per-step soft assignment over K intentions
- Each intention k has an associated reward function rk recovered via closed-form IAVI (inverse action-value iteration)
- E-step: per-step posterior factorization P(zi=k | ξ, ψ, Θ) = fθ(φi)k πrk(ai|si) / Σj fθ(φi)j πrj(ai|si) → O(nK) complexity
- M-step: independent per-intention reward recovery via weighted IAVI (closed form); recurrent network update via gradient descent

**Theorem 1 (exact EM decomposition)**: The auxiliary function Q(Θ+ | Θ) decomposes exactly into independent subproblems — one for θ+ (maximizing per-step responsibility weighted by fθ) and one per reward r+k (solvable in closed form via IAVI). No variational approximation needed. The posterior factorizes across time steps: P(η | ξ, ψ, Θ) = Πi P(zi | ξ, ψ, Θ), making the E-step O(nK).

**Training objective**: LNLL + λℓ1 Lℓ1 + λkl Lkl, combining negative log-likelihood of per-step intention assignments with temporal smoothness penalties (ℓ1 on fθ changes, KL divergence on consecutive fθ outputs).

## Key Results

| Domain | PRISM | DIRL | SWIRL | HIQL |
|--------|-------|------|-------|------|
| Mouse labyrinth (log-likelihood) | highest | — | — | — |
| Mouse labyrinth intentions | 3 (water-seeking, homing, exploration) | 3 | 3 | — |
| Frustration gridworld | captures non-Markovian switching | fails | fails | fails |
| BridgeData V2 robotic | 4 phases (approach, grasp, carry, idle) | — | — | — |

PRISM achieves highest held-out log-likelihood across all domains while recovering nameable intentions without supervision.

## Wiki Connections

- [[agentic-research]] — BridgeData V2 robotic manipulation as first large-scale application of multi-intention IRL; PRISM operates offline on demonstration data
- [[bounded-representation-capacity]] — hidden MDP with latent intention space Z; the gating network routes observations to intentions, acting as a compression mechanism for behavioral state
- [[credit-assignment]] — PRISM performs "inverse option discovery": instead of recovering skills/policies (which are temporally extended), it recovers the reward structure that generates behavioral options
- [[mop-explorer]] — intention switching as a form of behavioral exploration/exploitation trade-off; PRISM's latent intention variable provides a representational substrate for this

## Related
- [[sources/papers/prism]]
- [[index]]

- [[prism]]

## Key Quotes

> "Recovering the reward functions that drive each goal, the moments at which the agent switches between them, and the aspects of the history that trigger these switches is essential for understanding complex sequential behavior."

> "PRISM trains in minutes on a laptop GPU and produces human-interpretable reward maps without manual specification of the temporal horizon."

> "These experiments suggest that discrete intention switching is present in both biological and artificial agents, and that the reward maps PRISM recovers provide a useful lens for interpreting the latent goals behind complex sequential behavior."
