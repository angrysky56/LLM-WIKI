---
summary: Ramírez-Ruiz et al. (Nature Communications 2024) — Maximum Occupancy Principle: agents maximize future action-state path entropy instead of extrinsic reward, producing complex goal-directed behavior from intrinsic motivation alone
tags: [MOP, intrinsic-motivation, entropy, reinforcement-learning, reward-free, behavioral-variability, Bellman-equation, empowerment, free-energy-principle]
updated: 2026-04-14T00:34:32Z
created: 2026-04-14T00:34:32Z
---

# Complex Behavior from Intrinsic Motivation to Occupy Future Action-State Path Space

**Type:** Source — peer-reviewed paper
**Authors:** Jorge Ramírez-Ruiz, Dmytro Grytskyy, Chiara Mastrogiuseppe, Yamen Habib, Rubén Moreno-Bote
**Published:** Nature Communications 15, 6368 (2024)
**DOI:** https://doi.org/10.1038/s41467-024-49711-1
**Code:** https://zenodo.org/records/11401402
**Confidence:** 0.95 — peer-reviewed, mathematically proven, empirically demonstrated

---

## Core Insight

Reward maximization is not necessary for complex, goal-directed behavior. An agent that simply maximizes future action-state path entropy — the variety of paths it can take through state space — spontaneously generates curiosity, goal-directedness, survival instincts, hide-and-seek, dancing, and basic altruism. Rewards become *means* to continued exploration, not goals in themselves.

---

## The Maximum Occupancy Principle

A MOP agent maximizes the state-value:

$$V^\pi(s) = \mathbb{E}\left[\sum_{t=0}^{\infty} \gamma^t \left(\alpha \mathcal{H}(A|s_t) + \beta \mathcal{H}(S'|s_t, a_t)\right) \bigg| s_0 = s\right]$$

where $\alpha$ weights action entropy (diversity of strategies), $\beta$ weights successor-state entropy (novelty of outcomes), and $\gamma$ is the discount factor (time horizon).

**Key result (Theorem 1):** Action-state path entropy is the *only* measure of path occupancy consistent with additivity per time step, monotonicity (rare paths contribute more), and smoothness. This uniqueness is analogous to Shannon's derivation of information entropy but uses different axioms.

## Optimal Policy

The optimal policy is a softmax/Boltzmann distribution (Eq. 6):

$$\pi^*(a|s) = \frac{1}{Z(s)} \exp\left(\alpha^{-1}\beta \mathcal{H}(S'|s,a) + \alpha^{-1}\gamma \sum_{s'} p(s'|s,a) V^*(s')\right)$$

**Critical property:** Optimal MOP policies are *always stochastic* — behavioral variability persists even after learning. This contrasts with all reward-maximizing frameworks where the optimal policy is deterministic.

## Key Properties

| Property | Mechanism |
|---|---|
| Survival instinct | Absorbing states (death) have zero future entropy → naturally avoided |
| Goal-directedness | Emerges near constraints (low energy → deterministic food-seeking) |
| Exploration | Intrinsic — agents seek unoccupied path space, no exploration bonus needed |
| Risk sensitivity | β controls preference for stochastic vs. deterministic environments |
| Altruism | When other agents' states are included in state space, β drives freedom-giving behavior |
| No exploration-exploitation tradeoff | Agents care about rewards only as means to continue exploring |

## Empirical Results

- **Gridworld:** MOP agents visit entire arena; reward agents park at food; random walkers die
- **Prey-predator:** MOP mouse teases cat, uses both clockwise and counterclockwise escape routes; reward mouse uses one route 90% of the time
- **Cartpole:** MOP agent "dances" with wide angle variety; reward agent maintains minimal-movement balance
- **Agent-pet altruism:** Higher β → agent sacrifices own action freedom to give pet more state freedom
- **Quadruped (MuJoCo):** MOP agent walks, jumps, spins without any locomotion reward; becomes goal-directed toward food when energy is low

## Comparison with Other Reward-Free Approaches

| Framework | Behavior | Problem |
|---|---|---|
| Empowerment (MPOW) | Finds highest-empowerment state, parks there | Collapses to deterministic; not additive over paths |
| Free Energy Principle (FEP/EFE) | Minimizes surprise; proven equivalent to reward maximization in deterministic environments | Optimal policy is deterministic; no behavioral variability |
| MOP | Variable, curiosity-driven, goal-directed when constrained | None identified in paper (see limitations below) |

## Limitations

1. Discrete state spaces require full transition model (model-free extension via SAC demonstrated but not fully developed)
2. Learning the transition matrix in unknown environments is an open problem
3. α/β/γ are hyperparameters — no principled method for setting them (though only β/α ratio matters)
4. Computational cost scales with state space size for exact solutions

## Connections

- [[maximum-occupancy-principle]] — the concept page distilling the principle itself
- [[edm-framework]] — EDM's disruption metric as a possible measurement analog in concept space
- [[causal-state-edm-ood-isomorphism]] — epsilon machine framing connects to MOP's entropy formalism
- [[zettelkasten-engine]] — MOP-guided insight exploration as a curation strategy
- [[mop-edm-cognitive-architecture]] — synthesis applying MOP to AI cognitive architecture
