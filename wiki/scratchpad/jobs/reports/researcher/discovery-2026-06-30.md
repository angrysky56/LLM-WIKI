---
summary: Discovery on MOP training for transformers: path entropy maximization vs standard NTP entropy
tags: [research, entropy, MOP, transformer, training]
updated: 2026-05-25T17:38:22Z
created: 2026-05-25T17:38:22Z
---

# Researcher Discovery Report — 2026-06-30

## Discovery Cycle
- Topics researched: 3 (path entropy maximization, softmax temperature theory, next-token prediction training dynamics)
- New pages created: 0
- Pages updated: 1 (carryover.md)
- Cross-links added: 0

## Task: t_0eae0cb4306c1f26 — MOP Training for Transformers

**Question:** Can path entropy maximization be applied to next-token prediction training from scratch?

### What the Literature Shows

**Standard NTP already maximizes a form of entropy.** Cross-entropy loss for next-token prediction is equivalent to minimizing the negative log-likelihood of the data — which is the same as maximizing the entropy of the model's token-level predictive distribution, conditioned on the context. The model is trained to match the data distribution, not to spread probability mass uniformly.

**MOP's path entropy is a different quantity.** MOP ( Ramírez-Ruiz et al., Nature Communications 2024) maximizes:

```
V^π(s) = E[Σ γ^t (α·H(A|s_t) + β·H(S'|s_t, a_t))]
```

This is the **entropy of action sequences and state-transition paths**, not the entropy of individual token emissions. Under standard NTP, the "state" is the context prefix and the "action" is the next token. MOP would add a bonus for exploring diverse state-transition trajectories — different from maximizing token-level predictive accuracy.

**Key papers found:**

| Paper | Relevance |
|-------|-----------|
| 2409.17335 — Non-asymptotic convergence of NTP transformers | Theoretical analysis of transformer training dynamics for NTP; shows sub-linear convergence to max-margin solutions |
| 2403.06963 — Pitfalls of next-token prediction | Shows teacher-forcing can fail to learn accurate NTP; multi-token prediction as fix |
| 2405.13718 — Next-token prediction capacity bounds | Upper/lower bounds on how many distinct NTP distributions a transformer can represent |
| 2010.07344 — Temperature theory for softmax cross-entropy | Shows β (inverse temperature) is a key tunable hyperparameter; optimal β is architecture-sensitive |
| 2402.13991 — Sequence composition for LM pre-training | Intra-document causal masking outperforms cross-document masking; shows context matters for what gets predicted |

### Key Challenge

**MOP training from scratch requires defining absorbing states in token space.** In reinforcement learning, absorbing states are states from which no further action is possible (failure/death states). For NTP training, what are the absorbing states? Possible candidates:

- End-of-sequence token (EOS) — natural absorbing state for individual sequences
- Padding tokens — absorbing in the batch sense
- Context windows that have saturated attention — structurally absorbing in a different sense

The challenge is that MOP's power comes from defining *what not to do* (absorbing states) and letting diverse path exploration emerge. For NTP, the analogous move would be defining what sequences are "dead" — but most sequences are potentially useful, not failures. This is fundamentally different from RL environments where death is a clear absorbing state.

**KL-regularization tension.** MOP's Theorem 5 notes that absolute vs. relative entropy matters: KL regularization (as used in RLHF/DPO) cancels the preference for states with many actions — self-defeating for occupancy maximization. This directly challenges the standard RLHF structure, suggesting that MOP-guided training would need a different regularization form than what's commonly used.

### Gap Assessment

No papers directly address MOP-style path entropy maximization applied to transformer NTP training from scratch. This remains an **open research direction** with a strong theoretical motivation (MOP's reward-free exploration) but no empirical validation in the autoregressive language modeling setting.

### Open Questions
- **[Question]** Absorbing state definition: What are the meaningful absorbing states for token sequences? Is EOS sufficient, or does MOP-NTP require a richer failure state definition?
- **[Question]** KL-regularization compatibility: Can MOP's path entropy objective be combined with standard RLHF without the KL term canceling the occupancy-maximizing pressure?
- **[Question]** Empirical validation: Would MOP-style training produce more diverse, less collapsed token distributions than standard cross-entropy NTP? No experimental evidence exists yet.
- **[Question]** Connection to temperature: The softmax temperature β is already known to affect entropy during training (2010.07344). Is MOP training just a principled way to set the temperature/sampling distribution, or does it add something structurally different?

## Updated Carryover

The carryover.md will be updated to reflect:
- MOP-NTP gap confirmed: no existing papers apply MOP to transformer training from scratch
- Key challenge identified: absorbing state definition in token space
- New candidate page to create: `mop-next-token-prediction.md` (stub — pending empirical evidence)
