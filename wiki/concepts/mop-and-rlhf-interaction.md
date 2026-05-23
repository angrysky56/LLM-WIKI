---
created: 2026-05-28
updated: 2026-05-28
type: concept
summary: Structural tension between Maximum Occupancy Policy (MOP) entropy maximization and RLHF's KL-regularization — three potential resolution paths identified
tags: [reinforcement-learning, policy-optimization, llm-training, mixture-of-experts, open-research]
sources: https://arxiv.org/abs/2410.10700, https://arxiv.org/abs/2409.16140, https://arxiv.org/abs/2310.02793
status: active
confidence: 0.75
---



# MOP and RLHF Interaction

The structural tension between the **Maximum Occupancy Principle (MOP)** and **Reinforcement Learning from Human Feedback (RLHF)** — specifically how their differing objectives for stochasticity and policy conservatism produce conflicting training signals.

## The Core Tension

MOP (Maximum Occupancy Principle) and RLHF optimize for different things:

| Property | MOP | RLHF (PPO/DPO) |
|
-|
--|
-|
| **Objective** | Path entropy maximization — visiting all high-reward states | Maximize trajectory-level reward against reference |
| **Policy** | Always stochastic | Tends toward deterministic via KL penalty |
| **Reference** | None — no reference model | KL penalty against reference model |
| **Behavior** | Behavioral diversity across states | Convergence toward a single best action |

The fundamental conflict: **MOP's path entropy objective pushes toward stochastic policies that visit all rewarding states, while RLHF's KL-regularization pushes toward deterministic policies that pick the single best action per state**.

This is most acute in **mixture-of-experts (MoE)** architectures, where:
- MOP's occupancy objective could guide expert routing toward diverse, equitable utilization
- RLHF fine-tuning tends to collapse routing to a small set of "favorite" experts

## Why This Matters

In MoE-based LLMs (Mixtral, Grok, DBRX), the routing policy determines which expert handles each token. If RLHF causes routing collapse — tokens consistently routing to the same 1-2 experts in an N-expert system — then the MoE architecture degrades toward a dense model.

The compute efficiency of MoE (sparse conditional computation) depends on high expert diversity. If RLHF destroys that diversity, you lose the architectural advantage you paid for.

## Three Resolution Paths

### Path 1: Occupancy-Relative Regularization

**Replace** `KL(π || π_ref)` **with** `KL(π(·|s) || π_group(·|s))` — pushing the policy toward group-averaged stochasticity rather than a fixed reference.

This is analogous to GRPO's group-relative advantage, but at the policy level:
- Instead of measuring advantage relative to a reference model, measure it relative to the group's average stochasticity
- Rewards policies that maintain diverse action distributions across the expert group
- Keeps the RLHF structure (reward + regularization) but changes what the regularization targets

**Challenge**: Requires defining "group" — is it other rollouts in the same batch? Historical policies? The mathematical structure is less clean than standard KL.

### Path 2: MOP as Auxiliary Intrinsic Reward

Keep RLHF's KL structure for alignment (this is where you get your behavioral safety guarantees). **Add MOP's entropy bonus as an intrinsic reward term** for behavioral diversity:

`R_total(s, a) = R_RLHF(s, a) + β × H(π(·|s))`

Where `H(π(·|s))` is the entropy of the policy at state `s`, scaled by `β`.

This approach:
- Preserves the alignment properties of RLHF
- Adds exploration incentives via the entropy bonus
- Has been tested in toy settings but not at scale in MoE systems

**Challenge**: Entropy bonuses are notoriously unstable — they can cause the policy to wander if not carefully tuned. The entropy scale `β` is critical and task-dependent.

### Path 3: Structural Incompatibility

MOP's path entropy objective and RLHF's trajectory-level reward optimization are **fundamentally incompatible** — they optimize for different things and cannot be combined without one dominating the other.

Under this view: MOP is a pre-training/architecture design principle, not a fine-tuning objective. Use MOP to design the architecture (expert routing that maximizes coverage), then use standard RLHF for alignment.

This is the "don't mix" resolution — cleaner architecturally, but potentially loses the benefit of MOP-informed fine-tuning.

## Connection to GRPO

GRPO (Group Relative Policy Optimization) provides an interesting middle ground:

- GRPO removes the reference model (no KL against `π_ref`)
- GRPO uses within-group advantage estimation instead
- This means GRPO naturally produces less deterministic policies than PPO

For MoE systems, GRPO's group-relative structure is potentially more compatible with MOP than PPO is, because:
- No reference model means no anchoring toward deterministic behavior
- Within-group advantage naturally handles the stochasticity of expert routing

However, GRPO has not been specifically studied in the MoE fine-tuning context — this is an open empirical question.

## Connections

- [[maximum-occupancy-principle]] — MOP's entropy maximization principle
- [[group-relative-policy-optimization]] — GRPO, the most compatible existing algorithm
- [[mixture-of-experts]] — where this tension is most acute
- [[reward-modeling]] — RLHF's reward model is what gets optimized
- [[inference-time-compute-scaling]] — BoN search is a form of stochasticity exploitation

## Open Questions

1. **Which resolution path is correct?** No published work has tested all three systematically.

2. **MoE routing collapse under RLHF**: Is routing collapse actually happening in practice? What's the empirical degradation in expert utilization after RLHF fine-tuning?

3. **GRPO for MoE**: Can GRPO naturally preserve MoE expert diversity without additional regularization? This is empirically testable.

4. **Scale of the conflict**: Does the MOP+RLHF tension matter at small scale (7B MoE), or only emerge at frontier scale (400B+ MoE)?

## Limitations

- **No empirical validation**: All three paths are theoretical — no published experiments comparing them.
- **Algorithm-specific**: The tension depends on which RLHF algorithm is used. DPO and PPO have different KL structures and different compatibility with MOP.
- **Domain-specific**: The severity of the conflict depends on the domain. Code generation (high reward variance across states) may benefit more from MOP-style diversity than factual Q&A.