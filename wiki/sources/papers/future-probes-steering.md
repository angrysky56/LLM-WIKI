---
summary: Introduces Future Probe Controlled Generation (FPCG) for steering reasoning models by distinguishing detection features from prediction features, enabling effective control with minimal output degradation.
tags: [arxiv, paper, steering, LLM-control, probing, reasoning-models, LRM, interpretability]
updated: 2026-06-10T17:29:26Z
created: 2026-06-10T17:29:26Z
---

# Predicting Future Behaviors in Reasoning Models Enables Better Steering

**Authors:** Evgenii Kortukov, Piotr Komorowski, Florian Klein, Paula Engl, Gabriele Sarti, Seong Joon Oh, Sebastian Lapuschkin, Wojciech Samek (Fraunhofer HHI, Northeastern University, KAIST)

**arXiv:** 2606.11172v1, 9 Jun 2026

## Problem

Large reasoning models (LRMs) often behave unexpectedly in deployment. Test-time steering controls LRM outputs by intervening on hidden representations (activation steering), but this degrades output quality. The paper identifies a conceptual flaw: prior steering work implicitly relies on **detection features** — internal features that detect behavior in *already generated text* — but these are poor predictors of *future* behavioral outcomes, making them a weak intervention target.

## Method

The paper introduces **Future Probe Controlled Generation (FPCG)**, a text-level steering method built on a key theoretical distinction:

1. **Detection features** — internal representations that detect properties of already-completed text (used by prior activation steering)
2. **Prediction features** — a separate type of internal feature that predicts *future* behavior likelihood from intermediate reasoning steps

The authors train linear probes on intermediate reasoning activations to predict future behavior probabilities (refusal, sycophancy, reward-seeking, etc.). These probes achieve 64–91% accuracy in predicting which behavior the model will ultimately exhibit.

**FPCG algorithm**: During generation, the model samples M candidate sentences at each step. The probe evaluates each candidate's predicted future behavior likelihood, and the system selects the candidate with the highest probability of the desired behavior. This selection process repeats sentence-by-sentence throughout the response.

## Key Findings

1. **Detection vs. prediction features are distinct**: Internal features used for detecting past behavior are measurably different from features that predict future behavior — the latter are found earlier in the reasoning process

2. **FPCG achieves strong steering with minimal output degradation**: On DeepSeek-R1-Distill-Llama-8B, negative steering reduces refusal rate from 46.2% to 5.1% (-41.1pp) and positive steering increases it to 88.9% (+42.7pp), with a filtered rate (output quality proxy) of only 0-8%

3. **FPCG succeeds where activation steering fails**: In several evaluations, activation-based steering methods produce no measurable effect while FPCG achieves significant steering

4. **Perplexity is preserved**: FPCG maintains near-baseline perplexity, while activation steering causes measurable degradation (Figure 8 in paper)

## Limitations

- Requires probes trained on each behavior of interest — not a zero-shot steering method
- Sampling overhead: generating M candidates per sentence increases inference cost
- Probes are linear (logistic regression) — may miss more complex behavioral patterns
- Evaluation focuses on six specific behaviors (refusal, sycophancy, myopic reward, wealth seeking, survival instinct, prompt injection)

## Connections

- Directly relevant to [[ReasonAlloc]] (2606.11164v1) — both papers address challenges specific to reasoning models (LRMs) from different angles (steering vs. inference efficiency)
- Related to [[PPO-vs-DPO]] and activation steering literature (DiffMeans, CAA)
- Connects to mechanistic interpretability work on understanding how LRMs plan vs. verbalize decisions
- Provides a practical interpretability-to-control pipeline aligned with [[RREDCoT]]'s emphasis on reasoning-time behavior analysis

## Key Quote

> "We argue that to successfully steer LRMs without quality loss, we need to understand their decision making processes — specifically how internal representations reflect the evolution from planning and considering possible future behaviors, towards converging on a decision."

## References

- Kortukov et al. (2026). Predicting Future Behaviors in Reasoning Models Enables Better Steering. arXiv:2606.11172v1. Code: https://github.com/kortukov/future_probes
