---
summary: Theory of behavior replacing reward maximization with action-state path entropy maximization — Layer 0 of EFHF architecture; absorbing states → Kernel 2 (Prover9-verified)
tags: [MOP, entropy, intrinsic-motivation, behavioral-variability, reward-free, reinforcement-learning, absorbing-states, stochastic-policy, EFHF, Kernel-2, lumpability]
updated: 2026-04-14T04:12:42Z
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

**The reward definition problem.** Reward-maximizing agents need a reward function specified by design. MOP sidesteps this — define only what kills the agent (absorbing states), and complex behavior emerges.

**The exploration-exploitation tradeoff.** Under MOP this tradeoff disappears. Agents explore intrinsically and exploit only when survival requires it.

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
2. **Bellman equation exists:** The value function can be computed recursively
3. **Convergent value iteration:** The iterative map (Eq. 7) converges from any positive initial condition
4. **Optimal policy is always stochastic:** No deterministic optimal policy under MOP
5. **Absolute vs. relative entropy matters:** KL-regularization cancels the preference for states with many actions — self-defeating for occupancy maximization. This directly challenges RLHF's standard structure.

## EFHF Integration: Layer 0

MOP serves as Layer 0 (Intrinsic Motivation) of the [[efhf]] architecture. The existing EFHF pipeline (L1-L5+) is reactive — it waits for user prompts. MOP makes it proactive by generating exploration targets autonomously.

**Formally verified (Prover9):** MOP absorbing states → EFHF Kernel 2 transitions. Zero future entropy ↔ zero future computation ↔ Kernel 2. The structural equivalence is a logical theorem, not an analogy.

| MOP Concept | EFHF Concept | Relationship |
|---|---|---|
| Absorbing state | Kernel 2 transition | Proved equivalent |
| Energy reservoir | Buffering capacity T | Operational mapping |
| Discount factor γ | Coherence window τ | Both control planning horizon |
| Controlled high-Δ | Strong lumpability | Coherent exploration |
| Uncontrolled high-Δ | Weak lumpability failure | Hallucination |

## Connections

- [[ramirez-ruiz-mop-2024]] — source paper with full mathematical detail
- [[efhf]] — the five-layer architecture MOP integrates with as Layer 0
- [[edm-framework]] — disruption as measurement analog: high Δ = high state entropy = novel conceptual territory
- [[causal-state-edm-ood-isomorphism]] — epsilon machines provide the theoretical bridge; MOP agents seek to *create* new causal states
- [[zettelkasten-engine]] — MOP-guided exploration prioritizes high-disruption insight regions
- [[mop-edm-cognitive-architecture]] — full synthesis: MOP + EDM + EFHF cognitive architecture

## Open Questions

1. How do α/β map onto cognitive agent parameters? (explored in [[mop-edm-cognitive-architecture]])
2. Can MOP be applied to attention mechanisms?
3. What is the relationship between MOP's path entropy and computational mechanics' excess entropy? (partially answered — see [[mop-edm-cognitive-architecture]])
4. Can MOP value iteration be adapted for online learning in unknown environments?
5. Does the persistent stochasticity prediction hold for LLMs?
