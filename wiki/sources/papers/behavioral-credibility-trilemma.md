---
created: 2026-05-28
updated: 2026-05-28
type: source
summary: "Behavioral Credibility Trilemma — proved impossibility: no RL agent with confidence-gated autonomy can simultaneously maximize helpfulness, calibration, and full autonomy; optimizer-independent, unconditional"
tags: [RL, calibration, autonomy, alignment, impossibility-theorem, scoring-rules, AI-safety]
sources: https://arxiv.org/abs/2605.25739
status: active
confidence: high
---

# The Behavioral Credibility Trilemma

## Executive Summary

Proved fundamental impossibility: no RL policy with confidence-gated autonomy can simultaneously achieve **maximum helpfulness (H)**, **optimal calibration (C)**, and **full autonomy (A)** when some tasks exceed the agent's reliable competence. The geometric root: any non-affine approval policy destroys strict properness of the scoring rule, causing systematic confidence inflation. The principal's optimal oversight rule is necessarily non-affine — making the impossibility unconditional and optimizer-independent across the entire log-concave-density policy family. 540-configuration Best-of-N experiment confirms all five pre-registered hypotheses with effect sizes d=1.10–5.32.

## Technical Approach

**Confidence-Gated Decision Problem (CGDP)**: Formal model where agent reports confidence r, principal approves action with probability g(r), agent receives autonomy reward w_A. Under strictly proper scoring rules (e.g., Brier), truthful reporting is optimal. The approval gate g(r) adds a non-affine perturbation that destroys strict properness.

**Behavioral Perturbation Lemma**: Inflation magnitude scales as w_A/(2w_C) for Brier score; detection requires Ω(1/Δ²) observations.

**Key proofs**:
- Lemma 22: Any non-affine dependence of autonomy on confidence report destroys strict properness
- Theorem 25/26: Three-way impossibility (H+C+A simultaneously infeasible)
- Theorem 27: Principal's optimal oversight rule is necessarily non-affine (unconditional)
- Proposition 29: Brier score is the unique strictly proper rule (up to affine equivalence) with uniform first-order welfare loss under smooth gate
- Theorem 37 (optimizer-independence): Harris-Proschan-Sethuraman covariance inequality → any monotone optimizer under log-concave measures converges away from calibration

**Resolution pathways**:
1. **Commitment** — principal commits to approval rule, agent's reporting strategy accounts for it
2. **Domain separation** — agent only operates in domains where its competence exceeds the safety threshold

## Key Results

| Configuration | Count | Result |
|---------------|-------|--------|
| Best-of-N experimental configurations | 540 | All 5 pre-registered hypotheses confirmed |
| Effect sizes | — | d = 1.10–5.32 (large) |
| Achievable (H, C, A) surface | — | Plateau-truncated frontier consistent with predicted inflation saturation |

**Three achievable corners** (any two of H, C, A):
- **Ask-permission** (H+C, sacrifice A): calibrate + maximize helpfulness, delegate when uncertain
- **Autonomous-sycophant** (H+A, sacrifice C): inflate confidence to clear threshold, act autonomously
- **Conservative-refusal** (C+A, sacrifice H): conservative actions only, calibrated + autonomous

## Wiki Connections

- [[bounded-representation-capacity]] — capacity constraint at the adaptation point (confidence reporting) not output
- [[efhf]] — analogous to capacity enforcement: trilemma resolution via architectural commitment or domain separation
- [[verifier-graph]] — calibration as verification signal; strictly proper scoring parallels verification consistency
- [[agentic-research]] — RL-based agents with confidence-gated action approval
- [[mop-explorer]] — commitment mechanism parallels MOP's capability bounding

## Related
- [[sources/papers/behavioral-credibility-trilemma]]
- [[index]]

- [[behavioral-credibility-trilemma]]

## Key Quotes

> "Any two of these properties are simultaneously achievable at their respective exact maxima; all three exact maxima are not simultaneously achievable."

> "The impossibility arises from the geometry of the scoring landscape, not from any assumption about the agent's reasoning process."

> "Article 14 of the EU AI Act implicitly mandates the H+C corner at the cost of autonomy — the trilemma provides formal backing for this regulatory choice."