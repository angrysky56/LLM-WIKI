---
created: 2026-05-25
updated: 2026-06-30
type: concept
summary: RLHF fine-tuning causes routing instability in MoE models — experts that were safety-critical pre-fine-tuning route incorrectly post-fine-tuning, confirmed across 7B–141B parameter scales
tags: [mixture-of-experts, rlhf, fine-tuning, routing, safety, safe-moe, moe]
sources: https://arxiv.org/abs/2505.05634 (SafeMoE, Kim 2025), https://arxiv.org/abs/2409.17270 (MoE-Sieve, Manzoni 2024)
status: active
confidence: 0.88
---

# Route Collapse under RLHF

## Definition

Route collapse (also called routing collapse or routing drift) is the phenomenon where Mixture-of-Experts models that were trained with stable expert routing behavior become unstable under RLHF fine-tuning — experts that were functionally specialized pre-fine-tuning route incorrectly or cease to be selected after RLHF training, even when the fine-tuned behavior is not explicitly reward-hacked.

SafeMoE (Kim et al., 2025) documents this empirically across models from 7B to 141B parameters: after standard RLHF fine-tuning, routing distributions shift significantly away from pre-RLHF baselines. The effect is not driven by reward hacking per se — it occurs even when reward is maximized correctly — but it creates safety risks because expert specialization often correlates with safety-critical capabilities.

## Why It Matters

MoE models are increasingly standard in frontier deployments (Grok-1, DBRX, Mixtral). Route collapse under RLHF creates a specific deployment risk:

1. **Safety expert degradation**: In many MoE architectures, specific experts develop implicit specialization during pre-training (e.g., a refusal expert, a coding expert, a math expert). RLHF fine-tuning can disrupt this specialization even when the reward signal is benign, because RL updates change the router's confidence thresholds in ways that don't preserve expert boundaries.

2. **Unpredictable post-fine-tune behavior**: A model that was thoroughly tested pre-RLHF may exhibit qualitatively different routing behavior post-RLHF. Safety evaluations conducted on the pre-RLHF checkpoint may not transfer.

3. **Scale amplifies the problem**: Larger MoE models (141B+) show more severe routing drift than smaller ones, consistent with the general pattern that capability and optimization co-evolve.

4. **Monitoring is the current mitigation**: SafeMoE proposes routing audit mechanisms — tracking routing distributions before and after fine-tuning to detect drift. No architectural fix fully prevents it.

## Mechanism

The root cause is that the router is a learned linear layer optimized for pre-training objectives (next-token prediction). RLHF introduces a new optimization target (human preference) that changes the token-level statistics the router sees. The router's decision boundary was set by pre-training distributions; RLHF changes those distributions in ways the router wasn't designed to handle.

Specifically:
- RLHF changes the distribution of token types (the model produces different tokens post-RLHF)
- The router's confidence scores shift accordingly
- Experts that were selected for specific token patterns pre-RLHF may receive no signal for those patterns post-RLHF
- The auxiliary load-balancing loss (which was tuned for pre-training) may be inappropriate for the new distribution

## Key Evidence

| Paper | Finding | Model Scale |
|-------|---------|-------------|
| SafeMoE (Kim 2025) | RLHF causes routing distribution shift; safety experts route incorrectly post-fine-tuning | 7B–141B |
| MoE-Sieve (Manzoni 2024) | Pre-training routing skew exists and interacts with fine-tuning; routing heterogeneity is a structural property | Various |
| Chi et al. (2022) | Expert collapse during pre-training identified as a failure mode; routing instability pre-exists fine-tuning | Foundational |

## Connections
- [[concepts/mop-and-rlhf-interaction]]
- [[index]]
- [[concepts/route-collapse-rlhf]]
- [[log]]
- [[concepts/mixture-of-experts]]
- [[scratchpad/jobs/reports/researcher/discovery-2026-05-26]]
- [[concepts/adaptive-budget-learning]]
- [[route-collapse-rlhf]]

- [[mixture-of-experts]] — the architecture; token-choice routing is the vulnerable component
- [[mop-and-rlhf-interaction]] — the broader interaction space; MoE+RLHF routing problems are part of a larger set of MoE training instabilities
- [[reward-hacking]] — a related failure mode where RLHF causes capability regressions, but route collapse occurs even without explicit reward hacking
- [[adaptive-budget-learning]] — the training problem: how to update routers without destabilizing learned routing

## Limitations

- Routing collapse is detected via post-hoc audits; no real-time prevention exists
- The interaction between load-balancing loss and RLHF reward is not fully characterized
- It is unclear whether models can relearn stable routing after collapse without full retraining
