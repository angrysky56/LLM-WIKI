---
summary: Entropy-based decision point identification for power distribution sampling; matches RL-trained reasoning without training, dataset, or verifier
tags: [reasoning, sampling, test-time-scaling, MCMC, entropy]
updated: 2026-05-29T14:13:14Z
created: 2026-05-29T14:13:14Z
---

# Reasoning with Sampling: Cutting at Decision Points

## Metadata

| Field | Value |
|-------|-------|
| arXiv ID | 2605.30327 |
| Published | 2026-05-28 |
| Authors | Felix Zhou, Anay Mehrotra, Quanquan C. Liu (Yale/Stanford) |
| Categories | cs.LG, cs.AI, cs.CL |
| PDF | /home/ty/Documents/paper-research/2605.30327v1.pdf |
| Wiki path | wiki/sources/papers/entropy-cut-mh-reasoning-2026.md |

## Summary

Entropy-Cut Metropolis–Hastings is an algorithm for efficient sampling from the power distribution (a sharpened version of the base model) to elicit strong reasoning without RL training. The key innovation is using next-token entropy as a proxy to identify consequential decision points in reasoning traces, then resampling from those positions — achieving better mixing between modes than uniform-cut MH. Across MATH500, HumanEval, GPQA Diamond, and AIME26, Entropy-Cut MH consistently improves over RL-trained models and uniform-cut baselines.

## Key Findings

1. **Entropy as decision-point proxy**: High-entropy tokens indicate consequential branching decisions (e.g., proof strategy choice). Cutting at these positions and resampling the suffix enables mode-switching that uniform cuts cannot achieve.
2. **Mixing time scales with decisions, not tokens**: In a stylized reasoning model, Entropy-Cut MH's mixing time is proportional to the number of decision points in a trace, not the total token count — critical because reasoning traces often have few consequential decisions among many local tokens.
3. **Training-free, dataset-free, verifier-free**: Unlike RL-trained reasoning models (OpenThink, etc.), this approach requires no additional training, curated datasets, or verification signals — pure test-time scaling on the base model.
4. **Outperforms RL-trained models**: Across MATH500, HumanEval, GPQA Diamond, AIME26, consistently improves over RL-trained models and sampling baselines.

## The Problem with Uniform Cuts

Uniform-cut MH tends to resample inside a local calculation (e.g., rewriting intermediate arithmetic) rather than at strategic branching points. This is because reasoning traces have a few consequential decisions (proof strategy, algorithm choice) embedded in many local tokens. Uniform cuts miss the decisions.

## How Entropy-Cut Works

1. For each position in the current reasoning trace, compute the base model's next-token entropy
2. Select cut positions proportional to entropy (high entropy = likely decision point)
3. Keep the prefix, resample the suffix from the base model
4. Accept/reject via Metropolis-Hastings correction

## Why This Matters

The paper provides theoretical and empirical evidence that test-time scaling via power distribution sampling can match RL-trained reasoning without any training overhead. The entropy-cut insight — that decision points are identifiable via entropy — is both computationally elegant and practically effective. This extends the "reasoning is in the base model" thread from prior work (Karan & Du) by making the sampling process itself smarter.

## Connections

- [[test-time-scaling]] — test-time compute strategies for reasoning
- [[parallel-reasoning]] — best-of-N and sampling-based reasoning approaches
- [[evolutionary-search]] — also addresses escaping local optima; BES's backward decomposition vs. Entropy-Cut's forward sampling
- [[entropy-cut-mh-reasoning-2026]] — self-reference
