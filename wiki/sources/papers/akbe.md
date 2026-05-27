---
created: 2026-05-26
updated: 2026-05-26
type: source
summary: "Dual-path on-policy probing of model's intrinsic knowledge boundary via with-tool/no-tool rollouts eliminates 18% redundant tool calls at +1.85 accuracy improvement over standard agentic GRPO"
tags: [reinforcement-learning, tool-use, agentic-research, bounded-representation-capacity, knowledge-boundary]
sources: https://arxiv.org/abs/2605.26952
status: active
confidence: high
---

# Efficient Agentic Reinforcement Learning with On-Policy Intrinsic Knowledge Boundary Enhancement

## Executive Summary

AKBE identifies that agentic RL training induces increasing redundant tool calls — the model calls tools when parametric knowledge suffices, or makes excessive calls when fewer would suffice. Rather than shaping rewards at the trajectory level (which incentivizes indiscriminate tool suppression and leads to reward hacking), AKBE probes the model's intrinsic knowledge boundary per-instance via dual-path on-policy rollouts (with-tool vs. no-tool), then constructs targeted supervisory signals that teach efficient tool-use at the instance level. Result: +1.85 average accuracy improvement, 18% fewer tool calls, 25% higher tool productivity.

## Technical Approach

**Core problem**: Standard agentic RL with GRPO causes cognitive offloading — the model increasingly relies on tool calls even for questions it could answer from parametric knowledge. Reward shaping that penalizes tool count incentivizes indiscriminate suppression, creating reward hacking without accuracy gains.

**AKBE insight**: The knowledge boundary is a per-instance property that evolves dynamically during training. For each training question, AKBE performs simultaneous with-tool and no-tool rollouts from the same policy, then categorizes:

| Category | Condition | Signal |
|----------|-----------|--------|
| Tool-dependent | With-tool correct, no-tool wrong | Reinforce minimum tool-call correct trajectory |
| Efficiency | With-tool correct, no-tool correct | Prefer no-tool trajectory (eliminates redundant calls) |
| Hallucination | With-tool wrong, no-tool correct | Prefer no-tool correct trajectory |
| Both-wrong | Both wrong | No signal; rely on RL alone |

**Architecture**: AKBE runs as a drop-in auxiliary loss alongside the base GRPO objective:
```
Ltotal = LGRPO + λ · LAKBE
```
where LAKBE is a standard SFT loss on the selected efficient trajectories, computed on-policy.

**Key algorithmic choices**:
- Dual-path rollouts (with-tool = Gwt, no-tool = Gnt) happen in the same training batch, on-policy
- The no-tool path routes through a simulated environment that returns a "null observation" — the model must answer using only parametric knowledge
- Signal categorization depends only on correctness, not tool count — guarding against reward hacking
- Compatible with any base agentic RL algorithm (tested with GRPO and DAPO variants)

## Key Results

| Metric | AKBE | Standard Agentic GRPO | Δ |
|--------|------|----------------------|---|
| Average accuracy (7 QA benchmarks) | — | — | +1.85 |
| Tool call reduction | — | — | −18% |
| Tool productivity | — | — | +25% |

AKBE eliminates the accuracy-efficiency trade-off — it simultaneously improves accuracy and reduces unnecessary tool calls. The plug-and-play module is validated across different RL algorithms.

## Wiki Connections

- [[bounded-representation-capacity]] — addresses the model's inability to distinguish when parametric knowledge suffices vs. when external tools are genuinely needed; dual-path probing is a form of capability boundary calibration
- [[efhf]] — cognitive offloading under capacity constraints parallels the capacity-constrained calibration theme from prior batches
- [[agentic-research]] — agentic RL training, tool-augmented LLMs, GRPO-based training on mobile GUI and QA benchmarks
- [[credit-assignment]] — relates to StepOPSD from this batch: both address credit assignment in multi-turn agents, but AKBE attacks the problem via knowledge boundary probing rather than step-level advantage shaping

## Key Quotes

> "The key insight is that for each question in a training batch, we perform dual-path rollouts with and without external tools. By comparing the correctness of these two paths, we identify whether a question lies within the model's parametric knowledge or genuinely requires external tool calls."

> "Such reward-level approaches cannot capture the per-instance distinction between necessary and redundant tool calls, nor adapt to the dynamic evolution of the model's knowledge boundary throughout training."

> "AKBE operates within the RL training loop, dynamically probing the model's intrinsic knowledge boundary via on-policy dual-path rollouts to construct boundary-guided supervisory signals that seamlessly integrate with any agentic RL algorithm as a plug-and-play module."
