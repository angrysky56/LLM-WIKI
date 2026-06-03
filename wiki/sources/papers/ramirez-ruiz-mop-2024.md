
---
created: 2026-05-22
updated: 2026-05-22
type: source
title: "Complex Behavior from Intrinsic Motivation to Occupy Future Action-State Path Space"
authors: ["Jorge Ramírez-Ruiz", "Dmytro Grytskyy", "Chiara Mastrogiuseppe", "Yamen Habib", "Rubén Moreno-Bote"]
summary: "Maximum Occupancy Principle (MOP) — replaces reward maximization with action-state path entropy maximization. Rewards become means to continued exploration, not goals. Proves path entropy is the only measure consistent with additivity, monotonicity, and smoothness. Layer 0 of the EFHF architecture (absorbing states → Kernel 2 transitions)."
tags: [mop, entropy, intrinsic-motivation, behavioral-variability, reward-free, reinforcement-learning, absorbing-states, stochastic-policy, efhf, kernel-2, lumpability]
sources: [https://doi.org/10.1038/s41467-024-49711-1, https://zenodo.org/records/11401402]
status: active
confidence: 0.95
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
