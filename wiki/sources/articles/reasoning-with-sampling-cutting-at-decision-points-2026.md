---
summary: LLM inference-time reasoning paper on selectively branching/sampling only at high-entropy decision points
tags: [sampling, reasoning, inference-time-compute, LLM, decision-points, chain-of-thought, papers-2026]
updated: 2026-05-29T17:21:43Z
created: 2026-05-29T17:21:43Z
---

---
created: 2026-05-29T11:18:00Z
updated: 2026-05-29T11:18:00Z
type: source
summary: "LLM inference-time reasoning paper on selectively branching/sampling only at high-entropy decision points, reducing compute overhead vs. full-trajectory MCMC."
tags: [sampling, reasoning, inference-time-compute, LLM, decision-points, chain-of-thought, papers-2026]
sources: https://arxiv.org/abs/2605.30327
status: active
confidence: 0.9
---

# Reasoning with Sampling: Cutting at Decision Points (2026)

**Paper**: [arXiv:2605.30327](https://arxiv.org/abs/2605.30327)  
**Authors**: Anay Mehrotra (Stanford), Felix Zhou, Quanquan C. Liu  
**Venue**: arXiv preprint (2026)

## Core Problem

Traditional test-time compute scaling for LLM reasoning faces a tradeoff between **overthinking** (wasting compute on trivial sub-steps) and **underthinking** (committing to an early wrong path before exploring alternatives).

Standard approaches like full-trajectory MCMC sampling explore complete reasoning chains from each branching point — computationally expensive. The paper identifies that most tokens in a CoT trace are deterministic; only **decision points** (high conditional entropy junctures) genuinely benefit from exploration.

## Key Framework

**Decision Points**: Token/step-level locations where the model faces multiple competing, equally plausible logical paths. Monitored via entropy signals to isolate exactly where exploration matters.

**Cutting Strategies**: Rather than generating full redundant trajectories, the method:
1. Identifies high-entropy decision points
2. Truncates/backs-off exploration to those points only
3. Branches or prunes based on outcome relevance, not uniform sampling

**Compute Efficiency**: Focused compute on pruning bad branches at critical steps → lower inference latency and token overhead vs. full-trajectory MCMC.

## Relationship to Prior Work

Extends the foundational paper *"Reasoning with Sampling: Your Base Model is Smarter Than You Think"* (2025/2026) by refining how models navigate search trajectories.

Related to [[entropy-cut-mh-reasoning-2026]] — both address sampling efficiency in reasoning traces. The Entropy-Cut approach applies Metropolis-Hastings to reasoning traces; this paper focuses on identifying and cutting at decision points rather than sampling full trajectories.

## Connections

- [[inference-time-compute-scaling]] — same problem domain (test-time compute allocation)
- [[chain-of-thought]] — CoT is the substrate this operates on
- [[parallel-reasoning]] — alternative approach to reasoning efficiency
- [[entropy-cut-mh-reasoning-2026]] — related sampling-based reasoning approach
- [[adaptive-computation]] — shares the theme of dynamic compute allocation
- [[process-reward-model]] — decision point identification may relate to process reward signals

## Notes

- Paper is a 2026 preprint; still being evaluated by the community
- The decision point identification mechanism is key — the paper monitors token-level or step-level entropy to isolate these junctures
