---
summary: Theory of behavior replacing reward maximization with action-state path entropy maximization — complex goal-directed behavior emerges from intrinsic motivation to occupy future possibility space
tags: [MOP, entropy, intrinsic-motivation, behavioral-variability, reward-free, reinforcement-learning, absorbing-states, stochastic-policy]
updated: 2026-04-14T00:35:09Z
created: 2026-04-14T00:35:09Z
---

# Maximum Occupancy Principle

**Source:** [[ramirez-ruiz-mop-2024]] — Ramírez-Ruiz et al., *Nature Communications* (2024)
**Status:** Active research area with follow-up work (NeuroMOP, PIMBAA workshop 2025)

---

## What It Is

A theory of behavior that replaces reward maximization with action-state path entropy maximization. The agent's goal is to visit as many different action-state paths as possible over the long term. Extrinsic rewards (food, energy) are treated as means to sustain continued exploration — not as objectives.

The principle is formalized as maximizing:

$$V^\pi(s) = \mathbb{E}\left[\sum_{t=0}^{\infty} \gamma^t \left(\alpha \mathcal{H}(A|s_t) + \beta \mathcal{H}(S'|s_t, a_t)\right)\right]$$

## Why It Matters

MOP resolves several persistent problems in theories of behavior:

**The reward definition problem.** Reward-maximizing agents need a reward function specified by design. What reward should a vacuum robot maximize? Dust weight? Energy efficiency? Volume? MOP sidesteps this entirely — define only what kills the agent (absorbing states), and complex behavior emerges.

**The exploration-exploitation tradeoff.** Under MOP this tradeoff disappears. Agents explore intrinsically and exploit (seek resources) only when their survival requires it. The "exploitation" behavior emerges naturally near constraint boundaries.

**Behavioral variability after learning.** All reward-maximizing frameworks predict behavior should collapse to a deterministic optimal policy once learning is complete. MOP predicts — and biological evidence supports — that behavioral stochasticity persists indefinitely. Optimal MOP policies are always stochastic.

## The Three Parameters

Only the ratio β/α and γ matter:

| Parameter | Controls | Effect |
|---|---|---|
| α | Action entropy weight | Higher → more diverse action strategies |
| β | State-transition entropy weight | Higher → preference for surprising/novel outcomes; also controls risk sensitivity |
| γ | Discount factor | Higher → longer planning horizon; avoids myopic traps (noisy TV problem) |

## Absorbing States Are the Only Design Choice

Instead of designing rewards, a MOP system designer only needs to define absorbing states — states from which no further action-state paths are possible. These have zero value by construction. The agent's entire behavioral repertoire emerges from avoiding absorbing states while maximizing path entropy.

This has a deep connection to ethical frameworks where harm is defined deontologically (certain states are unconditionally to be avoided) while behavior within the non-absorbing space is guided by entropy maximization (freedom, diversity, possibility).

## Key Mathematical Properties

1. **Uniqueness (Theorem 1):** Path entropy is the *only* occupancy measure satisfying additivity, monotonicity, and smoothness
2. **Bellman equation exists:** The value function can be computed recursively, enabling efficient algorithms
3. **Convergent value iteration:** The iterative map (Eq. 7) converges to the unique optimal solution from any positive initial condition
4. **Optimal policy is always stochastic:** Unlike reward maximization, there is no deterministic optimal policy under MOP
5. **Absolute vs. relative entropy matters:** KL-regularization (relative entropy) cancels the preference for states with many actions — self-defeating for occupancy maximization

## Connections

- [[ramirez-ruiz-mop-2024]] — the source paper with full mathematical detail
- [[edm-framework]] — EDM disruption as a measurement analog: high Δ = high state entropy = novel conceptual territory
- [[causal-state-edm-ood-isomorphism]] — epsilon machines provide the theoretical bridge; MOP agents seek to *create* new causal states
- [[zettelkasten-engine]] — MOP-guided exploration prioritizes high-disruption insight regions
- [[mop-edm-cognitive-architecture]] — synthesis applying MOP to AI model architecture and cognitive agents

## Open Questions

1. How do α/β map onto cognitive agent parameters? (explored in [[mop-edm-cognitive-architecture]])
2. Can MOP be applied to attention mechanisms — making models explore diverse attention patterns rather than collapsing to dominant ones?
3. What is the relationship between MOP's path entropy and computational mechanics' excess entropy?
4. Can MOP value iteration be adapted for online learning in unknown environments without model-based transition estimation?
5. Does the persistent stochasticity prediction hold for LLMs — do models with entropy-regularized training maintain more diverse outputs after convergence?
