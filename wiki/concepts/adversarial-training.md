---
created: 2026-06-03
updated: 2026-06-09
type: concept
summary: Training methodology that exposes models to adversarial examples to improve robustness against adversarial attacks
tags: [adversarial-machine-learning, robustness, security, training-methodology]
sources: https://arxiv.org/abs/1312.6199 (Basic Iterative Method)
status: active
confidence: 0.85
---

# Adversarial Training

**Also known as:** Adversarial perturbation training, robust training

## What It Is

Adversarial training is a training methodology where a model is exposed to adversarial examples — inputs that have been specially crafted to cause misprediction — during training. The goal is to improve robustness: the model learns to resist adversarial perturbations that would otherwise fool it.

### The Adversarial Attack Setting

Given a clean example (x, y), an adversarial attack finds a perturbation δ such that:
- ||δ|| < ε (small enough to be imperceptible)
- The model predicts incorrectly: f(x + δ) ≠ y

The most common constraint is the L∞ norm: each pixel changes by at most ε.

### Basic Iterative Method (BIM)

Iterative gradient-based attack:
```
x_{t+1} = Clip_{x,ε}(x_t + α · sign(∇_x L(x_t, y)))
```
Where α is the step size and Clip constrains the perturbation to be within the ε-ball around x.

### Projected Gradient Descent (PGD) Attack

PGD is BIM with random initialization — considered the strongest first-order adversarial attack:

```
x_{t+1} = Clip_{x,ε}(x_t + α · sign(∇_x L(x_t, y)))
```

Random init allows the attack to find the strongest local perturbation within the ε-ball, making PGD-trained models provably more robust.

## Why It Matters

Adversarial vulnerability is a fundamental property of neural networks — even state-of-the-art models can be fooled by imperceptibly small perturbations. This has practical security implications:

- **Autonomous vehicles**: Road sign perturbations could cause misclassification
- **Security systems**: Adversarial inputs could bypass malware detectors
- **LLM agents**: Adversarial prompts that bypass safety guardrails (jailbreaks)
- **Multi-agent systems**: LCGuard uses adversarial training to find reconstruction vulnerabilities

## Adversarial Training for LLMs

Adversarial training for LLMs takes a different form:

| Setting | Attack | Defense |
|---------|--------|---------|
| **Safety/alignment** | Adversarial prompts (jailbreaks) | RLHF + adversarial training against red-team prompts |
| **Prompt injection** | Hidden instructions in context | Adversarial training on prompt injection examples |
| **Latent communication** | Reconstruction decoder (LCGuard) | Adversarial training of the communication transformation |

The LCGuard framework (see [[lcguard]]) uses adversarial training to simultaneously:
- Optimize the communication transformation g_ij for task utility
- Adversarially train the reconstruction decoder to find the worst-case leakage
- Iterate until equilibrium (minimax optimization)

## Connections
- [[concepts/multi-agent-llm-systems]]
- [[scratchpad/jobs/reports/researcher/discovery-2026-06-09]]
- [[concepts/adversarial-training]]
- [[wiki/index]]
- [[defending-moe-llms-against-harmful-fine-tuning-via-safety-routing-alignment]]
- [[log]]
- [[sources/papers/lcguard-kv-communication-guard-2026]]
- [[concepts/agent-leak-benchmark]]
- [[concepts/lcguard]]
- [[concepts/agent-onboarding]]
- [[adversarial-training]]

- [[agent-leak-benchmark]] — the benchmark for measuring adversarial reconstruction attacks
- [[latent-communication]] — the communication paradigm being protected
- [[agent-onboarding]] — agents should be evaluated for adversarial robustness before deployment
- [[multi-agent-llm-systems]] — the domain where adversarial KV-cache attacks occur