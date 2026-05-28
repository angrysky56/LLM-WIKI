---
created: 2026-06-30T00:00:00Z
updated: 2026-06-30T00:00:00Z
type: concept
summary: "[STUB] Applying MOP's path entropy maximization to transformer next-token prediction training from scratch"
tags: [MOP, entropy, path-entropy, next-token-prediction, transformer, training, stubs]
sources: []
status: stub
confidence: 0.3
---

# MOP Next-Token Prediction

*Stub page — needs real content*

## Core Question

Can [[maximum-occupancy-principle|MOP's]] path entropy maximization be applied to transformer next-token prediction training from scratch?

## Key Challenge

- **Absorbing state definition:** What are the meaningful absorbing states for token sequences? EOS token? Context saturation?
- **KL-regularization tension:** MOP Theorem 5 shows absolute vs. relative entropy matters — KL regularization (as in RLHF/DPO) cancels occupancy-maximizing pressure
- **Empirical validation needed:** No papers apply MOP to autoregressive LM training from scratch

## Connections
- [[log]]
- [[index]]
- [[concepts/reinforcement-learning-from-human-feedback]]
- [[concepts/mop-next-token-prediction]]
- [[concepts/group-relative-policy-optimization]]
- [[concepts/maximum-occupancy-principle]]
- [[mop-next-token-prediction]]

- [[maximum-occupancy-principle]] — source theory
- [[wolchover-life-force-2026]] — Boltzmann substrate connection
- [[group-relative-policy-optimization]] — alternative training approach
- [[reinforcement-learning-from-human-feedback]] — KL tension

## Open Questions

1. Can MOP's reward-free exploration be operationalized for language modeling?
2. Would MOP-style training produce more diverse token distributions than cross-entropy NTP?
3. What is the language modeling analogue of an "absorbing state"?
