---
summary: Training gating models for adaptive computation: supervised losses, RL, teacher-guidance, and open problems
tags: [adaptive-computation, gating, routing, moe, early-exit, ml-architectures, training]
updated: 2026-05-25T20:22:25Z
created: 2026-05-25T20:22:25Z
---

# Adaptive Budget Learning: Training Gating Models for Adaptive Computation

## Definition

Adaptive budget learning refers to training a gating (or routing) model that dynamically decides how much computation to allocate to each input token or sample at inference time. The gating model is a trainable module that outputs a decision — which expert to activate, when to exit a multi-exit network, or how deep to process a given token — and must be trained jointly with the base model while handling intrinsically non-differentiable compute-allocation decisions.

## Core Problem: The Gating Training Difficulty

The gating model faces a unique optimization challenge: it receives gradients only through the paths it selects. If a token routes to expert A, the router gets no learning signal about expert B's output for that token. This "gradient blocking" problem (TGR-MoE, 2026) causes:

1. **Routing instability** — expert assignments fluctuate wildly during early training
2. **Expert collapse** — a few experts dominate, others never learn
3. **Reward hacking** — the gate learns to route to cheap-but-wrong paths when compute is penalized
4. **RLHF sensitivity** — SafeMoE (Kim 2025) showed that fine-tuning causes severe routing drift across 7B–141B MoE models, as the gating module is disproportionately affected by preference shifts

## Approaches to Training the Gating Model

### 1. Supervised Auxiliary Losses (Most Common)

The gate is trained jointly with the main model using a combined loss:

```
L_total = L_task + λ_entropy * L_entropy + λ_load * L_load_balance
```

- **Task loss** — standard cross-entropy or next-token prediction loss on the selected path
- **Entropy regularization** — prevents collapsing to a single expert; promotes exploration
- **Load-balancing loss** — enforces fair expert utilization (Auxiliary-free load balancing, Switch Transformer)

**Limitation**: Still struggles with non-differentiable decisions (hard routing, early-exit thresholds).

### 2. Reinforcement Learning for Compute Allocation

When the gating decision is discrete (e.g., exit at layer L or activate expert E), RL provides a natural framework:

- **Policy gradient on compute budget** — reward penalizes compute usage, encouraging efficient routing
- **REINFORCE-style estimates** — baseline for variance reduction in routing decisions
- **Applied to early exit** — SPAR-K (2026) uses a fixed depth schedule for speech tokens with periodic full-depth refreshes; DAISY (2024) uses self-supervised loss as confidence signal
- **Key insight** (SPAR-K): confidence-based early exit strategies from text LLMs are suboptimal for speech tokens — the statistical properties differ

### 3. Teacher-Guided Routing (TGR-MoE, 2026)

A pretrained dense teacher model provides routing supervision:
1. Extract intermediate representations from the dense teacher
2. Build a "teacher router" from these representations
3. Use teacher router outputs as pseudo-labels for the student router
4. Suppresses routing fluctuations from early training stages

This addresses the gradient blocking problem by providing gradient signal from outside the selected-path regime.

### 4. Two-Stage Training (LGViT, 2023)

- **Stage 1**: End-to-end training of the full model with early exit heads
- **Stage 2**: Freeze backbone, self-distillation from deep heads to shallow heads

Shallow classifiers receive knowledge from deep classifiers via distillation, compensating for insufficient representation quality in early layers.

### 5. Jointly Trained Confidence Estimation

ADEPT (2026) trains a token-level confidence predictor jointly with the model:
- Confidence threshold determines exit
- Trained via binary cross-entropy against "correct exit depth" labels
- Adaptively adjusts per-token based on token complexity

## Key Findings from Recent Papers

| Paper | Method | Key Insight |
|-------|--------|------------|
| SafeMoE (Kim 2025) | Routing drift monitoring | RLHF causes significant routing collapse; SafeMoE reduces harmfulness 62.0→5.0 |
| TGR-MoE (2026) | Teacher-guided routing | Dense teacher supervision stabilizes sparse MoE training |
| SPAR-K (2026) | Fixed-depth schedule with refresh | Confidence-based exit is suboptimal for speech; speech has different statistical structure |
| ADEPT (2026) | Token-level confidence predictor | Decoupling KV cache dependencies enables early exit in generation phase |
| BEExformer (2024) | Fractional entropy reduction | Soft-routing loss + early exit reduces FLOPs 52% while improving accuracy 3.22% |
| DAISY (2024) | Self-supervised loss as exit signal | HuBERT matches with faster inference; exits early on clean, late on noisy |

## Open Questions

1. **Credit assignment across layers** — when a token exits early and is wrong, how much blame does the gate get vs. the model? Backprop-through-time to the gate is noisy.

2. **Scalability to very large MoE** — existing methods validated on 1B–7B models; 100B+ models may have different routing dynamics.

3. **RLHF interaction** — SafeMoE showed routing collapse under RLHF, but the mechanism (policy injection into routing, or reward shaping changing token complexity estimates) is not fully characterized.

4. **Unified compute budget loss** — no single principled objective combines task performance + compute efficiency + routing stability. Most papers use weighted sum of hand-tuned terms.

5. **Sample-level vs token-level** — should the gate make per-token decisions (as in most MoE) or per-sample decisions (entire sequence exits early)? Task-conditioned routing signatures suggest sample-level may work for classification.

## Connections
- [[log]]
- [[concepts/scaling-laws]]
- [[concepts/adaptive-computation]]
- [[concepts/early-exit-networks]]
- [[concepts/adaptive-budget-learning]]
- [[concepts/mixture-of-experts]]
- [[wiki/index]]
- [[concepts/route-collapse-rlhf]]
- [[adaptive-budget-learning]]

- [[adaptive-computation]] — stub page; this entry substantially fills it
- [[mixture-of-experts]] — gating is the router in MoE
- [[early-exit-networks]] — gating decides when to exit
- [[scaling-laws]] — adaptive compute is one response to compute scaling constraints
- [[route-collapse-rlhf]] — related hazard in MoE training under RLHF (SafeMoE)

## Sources

- ADEPT (2601.03700v1) — Adaptive Dynamic Early-Exit Process for Transformers
- BEExformer (2412.05225v3) — Binarized Early Exit Transformer with soft-routing loss
- TGR-MoE (2604.21330v1) — Teacher-Guided Routing for Sparse Vision MoE
- SPAR-K (2603.09215v1) — Scheduled Periodic Alternating Early Exit for Spoken Language Models
- SafeMoE (Kim 2025) — Routing collapse under RLHF; SafeMoE intervention
- DAISY (2406.05464v2) — Data Adaptive Self-Supervised Early Exit for Speech
- LGViT (2308.00255v1) — Two-stage training for early exit in ViT
- STEM-GNN (2602.09258v1) — Instance-conditional routing for generalization
- MoE-XRAY (2603.11114v1) — Routing signatures for task-conditioned MoE analysis
