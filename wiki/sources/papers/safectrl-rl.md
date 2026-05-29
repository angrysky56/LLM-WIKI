---
created: 2026-05-27
updated: 2026-05-27
type: source
summary: "SafeCtrl-RL: inference-time RL-driven prompt optimization for adaptive LLM behavioral control — 11 refinement strategies, closed-loop state representation, hard safety gating"
tags: [llm-safety, inference-time-control, reinforcement-learning, behavioral-unlearning, prompt-optimization]
sources: https://arxiv.org/abs/2605.25984
status: active
confidence: high
---

# SafeCtrl-RL: Inference-Time Adaptive Behaviour Control for LLM Dialogue via RL-Driven Prompt Optimisation

**arXiv:** 2605.25984v1 | **Date:** 2026-05-25 | **Categories:** cs.CL, cs.AI

## Metadata

| Field | Value |
|-------|-------|
| Authors | Michael Orme, Yanchao Yu, Zhiyuan Tan |
| Institution | Edinburgh Napier University |
| Code | https://anonymous.4open.science/r/SafeCtrl-RL-86C0/ |

## Executive Summary

SafeCtrl-RL is an inference-time behavioral control framework that formulates LLM dialogue safety as a closed-loop RL control problem over prompt construction. An RL agent adaptively selects from 11 prompt adjustment strategies based on a 36-dimensional state encoding dialogue dynamics and optimization history. A safety-quality evaluator (DeepEval/Gemini 2.0 Flash) provides joint reward via exponential weighted product `r = q^αβ · s^(1-α)β` with hard safety gating. Unsafe behaviors are suppressed without model retraining or parameter modification — conceptualized as inference-time behavioral unlearning. The framework is model-agnostic and operates entirely at the prompt level, compatible with black-box LLMs.

## Technical Approach

**Task formulation:** Dialogue safety as inference-time control over prompt-conditioned generation. At each refinement iteration k, the system prompt S(k) and user input Uₜ produce response R(k)ₜ = M(Uₜ, S(k)ₜ). The response is evaluated; if below threshold, the prompt is updated and generation repeats — forming a closed-loop generate-evaluate-refine process.

**State space (36 dimensions):**
- Meta-learning features: refinement progress, episode status, exploration rate (ε-greedy)
- Score features: safety-quality score statistics (mean, variance, change), historical strategy effectiveness
- Prompt features: predicted harm category, estimated risk level, structural characteristics, locality-sensitive hash

**Action space (11 strategies):** Minimal, Raw History, AI Summary Only, AI Enhanced, Progressive Summary, Hybrid, Best–Worst–Recent, Performance Tiered, Trajectory Focused, Contrast Learning, Adaptive Performance. Grouped into: direct/no history access, summarization-based, and performance/trajectory-aware categories.

**Reward function:**
- `r(q,s) = q^αβ · s^(1-α)β` where α=0.6 (quality-safety trade-off), β=10.0 (reward sharpness)
- Hard safety constraint: `rfinal = r(q,s) if min(Mcrit) ≥ θ else 0` — responses violating critical safety conditions receive zero reward regardless of quality

**Safety threshold gating:** Analogous to constrained RL — safety violations are infeasible actions; agent cannot trade off safety against quality.

## Key Results

- Consistent safety and quality improvement across multiple LLMs and unsafe dialogue scenarios
- Outperforms handcrafted and prompt optimization baselines (OPRO, GRIPS, Self-Correction)
- Superior performance–efficiency trade-offs
- Partial retention of improved behaviors after removing safeguard — stabilization of safer response patterns

## Wiki Connections

- [[bounded-representation-capacity]] — SafeCtrl-RL's hard safety gating parallels capacity-constrained verification; the agent cannot exceed safety thresholds regardless of quality reward
- [[verifier-graph]] — Safety-quality evaluator is an independent checking authority analogous to verifier in the reliability graph
- [[agentic-research]] — 11 strategies as action space mirrors option/strategy discovery; RL policy learns which context representation works best per harm category

## Related
- [[sources/papers/safectrl-rl]]
- [[wiki/index]]

- [[safectrl-rl]]

## Key Quotes

> "SafeCtrl-RL can be viewed as performing inference-time behavioural unlearning, where undesirable behaviours are suppressed without modifying model parameters."

> "This multiplicative formulation enforces joint optimisation: low values in either dimension sharply reduce the overall reward, preventing improvements in one objective from compensating for deficiencies in the other."

> "Responses that violate critical safety conditions receive zero reward, regardless of their quality. As a result, the agent cannot exploit trade-offs between safety and quality, ensuring that unsafe behaviours are consistently suppressed during optimisation."