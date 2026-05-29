---
created: 2026-05-27 08:30:00+00:00
updated: 2026-05-27 08:30:00+00:00
type: concept
summary: GRPO — a group-relative policy optimization algorithm for LLM training that uses within-group advantage estimation instead of a reference model
tags: [reinforcement-learning, llm-training, policy-gradient, group-relative, grpo, rlhf-alternative]
sources: ['arXiv:2410.06906', 'arXiv:2605.18299']
status: active
confidence: 0.9
---




# Group Relative Policy Optimization (GRPO)

GRPO is a policy gradient algorithm for training LLMs that computes advantages by comparing within a group of samples from the same prompt — without requiring a separate reference model or critic network.

## Definition

Standard policy gradient algorithms (like PPO) require a learned value function as a baseline to reduce variance. GRPO replaces this by sampling G responses to the same prompt and using the group mean as the baseline:

```
A_i = r_i - μ(r_group)
```

Where `r_i` is the reward for sample i, and `μ(r_group)` is the mean reward across the group. This is the "group-relative" part — advantages are computed relative to the group, not against a separate baseline network.

## Why It Matters

GRPO simplifies the RLHF pipeline by eliminating:
- **Reference model overhead**: PPO requires maintaining a reference model for KL regularization against the current policy. GRPO uses the group mean as the implicit baseline, eliminating the reference model entirely.
- **Critic network**: The value function baseline in PPO is itself a learned network. GRPO's group-relative estimate requires no learned critic.

This makes GRPO significantly more computationally efficient than PPO, especially as model scales increase. The SD-Search paper (arXiv:2605.18299) uses GRPO as its outer RL loop with ~8 rollouts per group.

## Relationship to PPO

| Aspect | PPO | GRPO |
|
--|
--|
|
| Baseline | Learned value function V(s) | Group mean μ(r_group) |
| Reference model | Required (KL penalty) | Not required |
| Critic network | Required | Not required |
| Variance reduction | Via learned baseline | Via group comparison |
| Sample efficiency | Lower (needs both actor and critic) | Higher (simplified) |

PPO's KL constraint against a reference model prevents the policy from drifting too far from the initial model. GRPO's group-relative advantage doesn't have an explicit constraint — the group mean naturally constrains the update direction.

## GRPO in SD-Search

SD-Search uses GRPO as its outer loop:
- Sample G=8 rollouts per question
- Compute binary outcome reward (CORRECT/INCORRECT) from gold-answer F1
- Each token in every rollout receives the same group-relative advantage
- Add the self-distillation loss on top (SD-Search's modification)

The key insight from SD-Search: GRPO's trajectory-level advantage averages over within-trajectory variance in query quality — individual search decisions receive no step-specific credit. SD-Search's hindsight self-distillation addresses this gap without modifying the GRPO outer loop.

## Open Questions

1. **KL regularization absent in GRPO**: Without a reference model, GRPO has no explicit KL constraint against the initial policy. Does this lead to reward hacking or policy collapse in longer training runs? SD-Search's 200-step training doesn't show it, but longer horizon behavior is unexplored.

2. **Group size sensitivity**: The variance reduction from group-relative baselines improves with larger group size G, but so does computational cost per step. Optimal G appears to be task-dependent — SD-Search uses G=8, but whether this generalizes is unknown.

3. **Credit assignment within groups**: GRPO distributes uniform advantage within a trajectory but doesn't differentiate between steps. SD-Search's token-level JSD distillation addresses this for search-augmented reasoning — but for general tasks, how should within-group credit be assigned?

## Connections
- [[concepts/constitutional-ai]]
- [[concepts/maximum-occupancy-principle]]
- [[concepts/llm-training]]
- [[log]]
- [[concepts/mop-and-rlhf-interaction]]
- [[concepts/inference-time-compute-scaling]]
- [[wiki/index]]
- [[concepts/evolutionary-strategies]]
- [[concepts/reward-modeling]]
- [[concepts/reinforcement-learning-from-human-feedback]]
- [[concepts/mop-next-token-prediction]]
- [[concepts/reward-hacking]]
- [[concepts/group-relative-policy-optimization]]
- [[concepts/essa]]

- [[reward-modeling]] — GRPO is the RL algorithm used to optimize reward models in LLM training
- [[inference-time-compute-scaling]] — SD-Search uses GRPO + self-distillation for step-level credit assignment
- [[maximum-occupancy-principle]] — MOP's stochastic optimal policy principle has structural parallels to GRPO's group-relative advantage computation
- [[constitutional-ai]] — CAI uses RLHF (PPO/DPO) while GRPO is an alternative approach to policy optimization
- Concept: [[evolutionary-strategies]]
- Concept: [[group-relative-policy-optimization]]
- Concept: [[llm-training]]
- Concept: [[mop-and-rlhf-interaction]]
- Concept: [[mop-next-token-prediction]]
- Concept: [[reinforcement-learning-from-human-feedback]]
- Concept: [[reward-hacking]]

- [[essa]]