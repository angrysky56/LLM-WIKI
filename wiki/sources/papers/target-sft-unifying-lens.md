---
summary: Reinterprets supervised fine-tuning as target distribution design via the Q-target framework, unifying many SFT variants and proposing TARGET-SFT.
tags: [arxiv, paper, SFT, supervised-fine-tuning, target-distribution, Q-target, LLM-training, reasoning]
updated: 2026-06-10T17:29:15Z
created: 2026-06-10T17:29:15Z
---

# A Unifying Lens on Supervised Fine-Tuning Through Target Distribution Design

**Authors:** Tong Xie, Yuanhao Ban, Yunqi Hong, Sohyun An, Yihang Chen, Cho-Jui Hsieh (UCLA)

**arXiv:** 2606.11189v1, 9 Jun 2026

## Problem

Standard supervised fine-tuning (SFT) maximizes the likelihood of every token in a demonstrated trajectory — a one-hot target distribution where the observed token gets probability 1 and every other token gets 0. This is fundamentally brittle: an observed token can be non-unique, noisy, or misaligned with the model's pretrained prior. Strictly fitting toward this one-hot target can amplify noise, induce overconfidence, interfere with what the model already knows, and hurt generalization — especially for reasoning tasks where multiple valid reasoning paths exist.

Existing SFT variants (token reweighting, KL regularization, label smoothing, distillation) each address aspects of this rigidity, but they are presented as separate algorithmic choices with no unifying framework connecting them.

## Method

The paper introduces the **Q-target framework**, which decomposes SFT supervision into two explicit design choices:

1. **γt** — How strongly to rely on the observed token yt (imitation strength)
2. **˜πt** — How to allocate the remaining probability mass (1−γt) over alternatives

Formally: **Qt = γt δyt + (1−γt) ˜πt**

Where Qt is the target distribution at token position t, δyt is the one-hot distribution at the observed token, and ˜πt specifies the plausible alternative distribution.

The key insight: rather than studying the loss objective in isolation, the paper asks *what target distribution should SFT drive the model to learn?* The loss is merely an optimization surrogate — the target distribution directly specifies the desired allocation of probability mass.

The paper shows that many existing SFT variants can be understood as implicit choices of (γt, ˜πt):

| Method | γt (imitation) | ˜πt (alternatives) |
|--------|----------------|-------------------|
| Standard SFT | 1.0 | — (none) |
| Token Reweighting (DFT, ProFit) | Model-confidence-weighted | — (residual undefined) |
| Label Smoothing | (1−ε) | Uniform |
| KL-regularized (ASFT, Proximal SFT) | 1.0 (implicit) | Reference model distribution |
| GEM (reverse KL) | 1.0 (implicit) | Entropy-regularized |
| Direct Distillation | Teacher logits | Teacher distribution |

Building on this view, they propose **TARGET-SFT**, which constructs the training objective directly from the desired target distribution. TARGET-SFT uses model confidence to determine γt (softening supervision on uncertain tokens) and the model's pretrained prior as ˜πt (allocating residual mass to plausible alternatives).

## Key Findings

1. **Q-target framework unifies SFT variants**: Seemingly different losses correspond to implicit target distribution choices through varying (γt, ˜πt)
2. **TARGET-SFT consistently outperforms** standard SFT, token-reweighting, distillation, and KL-regularized variants across all 10 dataset-model settings evaluated
3. **Mathematical reasoning**: On NuminaMath-CoT and OpenR1-15k, TARGET-SFT achieves the highest Average@16 accuracy. Standard SFT can even hurt performance (Qwen3-1.7B: 14.26→12.99)
4. **Choosing γt alone is incomplete**: Probability-weighted SFT improves over standard SFT, but TARGET-SFT improves further by explicitly designing ˜πt — the allocation of residual probability mass matters

## Limitations

- The Q-target framework is demonstrated for token-level SFT losses only
- TARGET-SFT's specific instantiation (model confidence for γt, model prior for ˜πt) is one choice among many
- Evaluation is on reasoning benchmarks only (math, medical)
- Frame work assumes access to well-calibrated model confidence scores

## Connections

- Directly relevant to [[RREDCoT]] (2606.06475v1) on reward redistribution — both argue naive per-token optimization is insufficient
- Extends the line of work on SFT limitations (DFT, beyond-log, ProFit, GEM, ASFT) by providing a theoretical unification

## Key Quote

> "We argue that the fundamental object in SFT is not the loss function itself, but the target distribution induced by the loss."

## References

- Xie et al. (2026). A Unifying Lens on Supervised Fine-Tuning Through Target Distribution Design. arXiv:2606.11189v1.
