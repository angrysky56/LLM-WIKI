---
created: 2026-06-16
updated: 2026-06-26
type: concept
summary: RLHF — training AI systems using human preference feedback via reward modeling and policy optimization (PPO/DPO); core tension with MOP's entropy maximization objective
tags: [RLHF, reinforcement-learning, alignment, human-feedback, policy-optimization, training]
sources: https://arxiv.org/abs/1909.08593 (RLHF intro), https://arxiv.org/abs/2203.02155 (InstructGPT)
status: active
confidence: 0.85
---

# Reinforcement Learning from Human Feedback

RLHF is a training methodology for aligning AI systems to human preferences by using human feedback to build a reward model, then optimizing policy against that reward model. The dominant pipeline: collect preference data (human ranks comparisons of model outputs), train a reward model, then use reinforcement learning (typically PPO) to fine-tune the policy to maximize reward while staying close to a reference model.

## The Standard Pipeline

1. **Collect comparison data**: Humans rank multiple model outputs (typically 4–9) for a given prompt. Labelers indicate which they prefer and by how much.
2. **Train a reward model**: A neural network learns to predict human preference scores from (prompt, response) pairs.
3. **Fine-tune with RL**: The base language model is fine-tuned to maximize reward from the reward model, with a KL penalty against the original model to prevent collapse.

The KL penalty `KL(π || π_ref)` is central — it constrains how far the adapted policy can drift from the original, which provides a conservatism mechanism.

## Why It Matters

RLHF is the dominant approach for aligning large language models:

- GPT-3.5, GPT-4, Claude, Gemini all use RLHF in their training pipelines
- It converts implicit human values into an explicit reward signal
- It allows models to exhibit complex behaviors that are hard to specify directly (helpfulness, harmlessness, honesty)

Without RLHF, language models optimize next-token prediction — which correlates imperfectly with human preference.

## Key Algorithms

**PPO (Proximal Policy Optimization)** — the original RLHF algorithm (Ouyang et al. 2022, InstructGPT):
- On-policy: requires fresh samples from the current policy at each update step
- KL penalty against reference model: `L = E[r] - β KL(π || π_ref)`
- Requires a reward model and a reference model simultaneously

**DPO (Direct Preference Optimization)** — simplifies to a classification objective (Rafailov et al. 2023):
- No explicit reward model needed
- No KL penalty against reference model — preference objective alone implicitly handles this
- `L = -E_{(x,y_w,y_l) ~ D}[log σ(r(x,y_w) - r(x,y_l))]`
- where `r` is derived implicitly from the policy

**GRPO (Group Relative Policy Optimization)** — removes reference model, uses within-group advantage (DeepSeek):
- No reference model needed
- Within-group advantage: compare each output to the group average rather than to a fixed reference
- Less deterministic than PPO (more stochastic policies)
- Potentially more compatible with MOP's entropy objective

## The MOP Tension

RLHF's KL-regularized structure is in fundamental tension with [[maximum-occupancy-principle]]'s entropy maximization objective:

| Property | MOP | RLHF (PPO) |
|----------|-----|------------|
| Objective | Path entropy maximization | Reward maximization |
| Policy | Always stochastic | KL → deterministic |
| Reference | None | KL against `π_ref` |
| Behavioral diversity | High (by design) | Degrades over training |

The core issue: KL-regularization pushes toward a deterministic policy (single best action per state), while MOP requires stochastic policies for occupancy diversity. This is most acute in MoE architectures where RLHF can collapse expert routing.

See [[mop-and-rlhf-interaction]] for the three resolution paths identified.

## Connection to [[group-relative-policy-optimization]]

GRPO is notable because:
- Removes the reference model entirely
- Uses within-group advantage estimation
- Produces less deterministic policies than PPO
- Structurally more compatible with MOP's entropy objective

For MoE systems specifically, GRPO may naturally preserve expert diversity better than PPO — but this is empirically untested.

## Connections

- [[group-relative-policy-optimization]] — alternative to PPO/DPO, structurally closer to MOP
- [[mop-and-rlhf-interaction]] — tension between MOP entropy and KL-regularization
- [[maximum-occupancy-principle]] — MOP's incompatible entropy objective
- [[reward-modeling]] — the reward model is the alignment bottleneck
- [[mixture-of-experts]] — where RLHF causes routing collapse

## Limitations

- **Reward hacking**: Human preferences are imperfectly specified. Reward models learn proxies, not actual values — leading to Goodhart's Law failures and [[reward-hacking]].
- **Human feedback quality**: Expensive, slow, inconsistent. Cultural biases, annotator fatigue, preference reversals.
- **Distribution shift**: Reward models overfit to the distribution they were trained on; they degrade when evaluated on significantly different prompts.
- **KL collapse**: Aggressive KL penalties prevent useful adaptation; conservative KL penalties leave the model insufficiently aligned.
