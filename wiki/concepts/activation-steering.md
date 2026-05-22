---
summary: Paradigm for directly manipulating LLM latent activations at inference time to steer behavior without fine-tuning
sources:
status: active
confidence: 0.85
tags: [llm, activation-steering, representation-engineering, interpretability]
updated: 2026-05-29
created: 2026-05-21
---

---
created: 2026-05-21T00:00:00Z
updated: 2026-05-21T00:00:00Z
type: concept
summary: Techniques for directly manipulating LLM internal activations during inference to steer behavior without fine-tuning.
tags: [llm, activation-steering, representation-engineering, interpretability, control-theory]
status: active
confidence: 0.9
---

# Activation Steering

Paradigm for dynamically modulating LLM behavior at inference time by directly manipulating the high-dimensional latent activation space, without expensive fine-tuning or parameter updates.

## Core Mechanism

High-level behaviors (truthfulness, honesty, toxicity, etc.) are encoded as **linear directions** in the model's representation space. Researchers extract a "steering vector" by processing contrastive prompt pairs (positive/negative behavior), computing the mathematical difference vector in activation space, then adding this vector back at runtime scaled by a tuning coefficient.

**Key finding (from RepE research):** behavioral control via activation space is possible because linear directions in transformer representations are genuinely meaningful — not artifacts of the geometry.

## Steering Methods

| Method | Core Mechanism | Distinctive Feature |
|--------|---------------|---------------------|
| **CAA** (Contrastive Activation Addition) | Fixed vector from contrastive pairs | Static, linear behavioral shifts |
| **SADI** (Semantics-Adaptive Dynamic Intervention) | Per-input binary masks on critical neurons/heads | Dynamic, precision-targeted per input |
| **SHARP** | Decomposed steering vectors for Large Vision-Language Models | Targets visual hallucination in LVLMs |
| **ITI** (Inference-Time Intervention) | Shift activations only in high-probing truthfulness heads | Truthfulness autoregressively throughout generation |
| **EAST** (Entropic Activation Steering) | Steering direction that maximizes output-action entropy | Promotes exploratory variance in agentic tasks |
| **Dynamic Activation Composition** | KL-divergence-based adaptive intensity scaling | Multi-property simultaneous control |

## Open-Loop vs Closed-Loop

**Standard ActAdd = open-loop P-controller.** Applies a pre-calculated perturbation but lacks feedback on how that perturbation propagates through non-linear transformer layers. Suffers from non-zero steady-state bias (tracking error accumulates through deep layer stacks).

**PID Steering (STU-PID) = closed-loop.** Three-term feedback: P (immediate correction) + I (accumulated error → zero bias) + D (rate damping → prevents overshoot). Eliminates steady-state error and provides mathematically guaranteed convergence.

## Connection to Internal Awareness

Activation steering is the "modulation" half of the biofeedback loop:
- **Observation** = [[mechanistic-interpretability]] (TransformerLens, caching attention)
- **Modulation** = activation steering (RepE, CAA, PID steering)
- Together they form the complete internal check loop analog to HRV biofeedback

## Connections

- [[mechanistic-interpretability]] — provides the observability layer
- [[metacognitive-architecture-closed-loop-self-regulation]] — full closed-loop self-regulation via PID/LQR steering
- [[chain-of-thought]] — explicit reasoning as complementary verification layer
