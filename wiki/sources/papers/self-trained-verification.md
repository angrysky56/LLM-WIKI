---
created: 2026-05-30T09:30:00Z
updated: 2026-05-30T09:30:00Z
type: source
summary: "Self-trained verification (STV): trains verifiers via reference-conditioned teacher; doubles hard math accuracy, 14× on scientific reasoning; breaks RLVR convergence plateau with ViL training."
tags: [arxiv, paper, verification, self-improvement, reasoning, training, test-time-scaling]
sources: https://arxiv.org/abs/2605.30290
status: active
confidence: high
---

# Self-Trained Verification for Training- and Test-Time Self-Improvement

**arXiv**: 2605.30290v1 | **Date**: 2026-05-28 | **Authors**: Chen Henry Wu, Aditi Raghunathan (CMU)

## Core Contribution

Self-trained verification (STV) addresses the verifier bottleneck that gates both test-time refinement and training-time self-improvement in reasoning models. The key observation: a model cannot reliably find errors in its own output from scratch, but can when shown the reference solution. This asymmetry — **diagnosis is easier given a reference** — becomes the supervision signal for training an unconditioned verifier.

The pipeline:
1. A reference-conditioned teacher `V★(· | x, y_{r-1}, y★(x))` identifies errors in generated solutions
2. On-policy distillation trains an unconditioned student `Vθ(· | x, y_{r-1})` to match the teacher's feedback distribution
3. At test time the student runs without references

## Key Results

| Setting | Task | Improvement |
|---------|------|-------------|
| Test-time refinement | DAPO Hard math (Qwen3-8B zero-shot) | ~2× pass@1 vs untrained verifier |
| Test-time refinement | SciKnowEval (hardest problems) | 1.5% → 21.0% (14×) |
| Training-time (ViL) | After RLVR convergence | +33% relative final-round pass@1 |
| Training-time (ViL) | Standalone pass@1 (no verifier at inference) | +30% past RLVR ceiling |

STV verifier enables Qwen3-8B + STV to outperform the much larger Qwen3-32B generator on hard reasoning tasks — **trained verification can substitute for generator scale**.

## Method Details

**Verifier training objective:**
```
L_STV(θ) = L_OPD(θ) + λ · L_RL(θ)
```
OPD = on-policy distillation matching student to teacher distribution (α-divergence, α=0.5, Jensen-Shannon). SFT on teacher outputs fails because the student encounters prefixes never seen during training (off-policy collapse). RL verdict component improves verdict accuracy.

**ViL (Verifier-in-the-Loop) training:** Generator trains inside V-R loop with frozen STV verifier providing feedback. Standard RL on verifiable reward. Only generator updated; verifier frozen.

## Design Principle

> "The next frontier in reasoning on hard problems may lie in how we train for and with verification."

This suggests an iterative self-improvement loop: better verifiers → more reliable test-time refinement + richer generator training → harder attempts for future verifier training.

## Connections

- [[test-time-scaling]] — STV enables verification to scale test-time compute effectively
- [[reasoning-scaffolding]] — verification-refinement loop as scaffolding mechanism
- [[self-improvement]] — STV as training recipe for both training-time and test-time self-improvement
- [[llm-training]] — ViL breaks RLVR ceiling, new training paradigm
- [[llm-verification]] — core contribution: training verifiers without human-graded feedback

## Kanban Status

- [x] Paper ingested 2026-05-30
- [ ] **Open**: RiM vs STV comparison — both address latent reasoning via different mechanisms (memory blocks vs verifier-refinement); RiM decouples internal computation, STV trains the verifier that drives refinement