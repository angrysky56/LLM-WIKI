---
summary: ITI paper — Li et al. 2023. Linear probe for truthfulness direction, amplified at inference time. Demonstrates causal link between probe-read representations and output behavior.
tags: [papers, activation-probing, representation-engineering, 2023, inference-time-intervention]
updated: 2026-06-09T09:10:03Z
created: 2026-06-09T09:10:03Z
---

# Inference-Time Intervention: Eliciting Truthful Answers

## Summary

Li et al. (2023) propose **Inference-Time Intervention (ITI)**, a method for steering LLMs toward truthfulness by identifying and amplifying "truthfulness directions" in the model's residual stream activations. The key insight is that truth-relevant representation directions can be identified from a small labeled dataset (yes/no question pairs) and then scaled during inference without fine-tuning the model.

### Method

1. **Probe training**: A linear logistic regression probe is trained on activation differences between truthful and untruthful answers at each layer.
2. **Direction identification**: The probe's weight vector at the most discriminative layer defines the "truthfulness direction."
3. **Inference-time intervention**: During generation, the model's activations are shifted along the identified direction (or against it, to reduce truthfulness).

On the TruthfulQA benchmark, ITI improves truthfulness from 38% (baseline) to 65% (ITI) on LLaMA-7B, approaching the performance of much larger models.

### Significance for Probe Adversarial Robustness

ITI demonstrates that activation-space probing can be used for **both** monitoring and intervention — the same representation direction that reveals truthfulness can also be amplified to improve behavior. This dual use creates an interesting adversarial dynamic: if an adversary can compute steering vectors, they may also be able to compute *anti-steering* vectors that bypass probe monitoring.

ITI is a critical source because it makes the causal link between probe-read representations and model outputs explicit: changing the representation along the probe direction changes the output. This means probe robustness and intervention robustness are linked — an attack that evades the probe may also evade the intervention.

### Key Claims
- Truth-relevant representation directions are consistent across inputs for a given model
- A single linear direction per layer suffices for meaningful behavioral shift
- The intervention transfers across related tasks (factuality → helpfulness)

## Connections

- [[wiki/concepts/activation-probe-adversarial-robustness]] — ITI as a canonical example of probe-based intervention
- [[wiki/concepts/representation-engineering]] — broader family of activation steering methods
- [[wiki/synthesis/representation-reading-as-arms-control-verification]] — verification applications of probe reading

## References
- Li, K. et al. (2023). Inference-Time Intervention: Eliciting Truthful Answers from a Language Model. arXiv:2306.03341.
