---
summary: Locally Coherent, Globally Incoherent — compositional residual ε⋆ for multi-component LLM agent coherence failures
tags: [paper, arxiv, multi-agent, probabilistic, coherence, calibration]
updated: 2026-05-30T01:35:44Z
created: 2026-05-30T01:35:44Z
---

---
created: 2026-05-30T00:00:00Z
updated: 2026-05-30T00:00:00Z
type: source
summary: "Locally Coherent, Globally Incoherent — compositional residual ε⋆ certifies when multi-component LLM agents fail under composition despite locally calibrated components."
tags: [paper, arxiv, multi-agent, probabilistic, coherence, calibration, agentic-ai]
sources: https://arxiv.org/abs/2605.30335
status: active
confidence: high
---

# Locally Coherent, Globally Incoherent: Bounding Compositional Incoherence in Multi-Component LLM Agents

**Paper**: Bounding Compositional Incoherence in Multi-Component LLM Agents  
**arXiv**: [2605.30335](https://arxiv.org/abs/2605.30335)  
**Author**: Anany Kotawala — Princeton University  
**Published**: 2026-05-28 (to appear at ICML 2026 workshops: CTB, AgenticUQ, FAGEN)  
**Categories**: cs.AI, cs.CL

## Executive Summary

Multi-component LLM agents assemble probabilistic claims from components that each see only part of a joint problem. The paper shows that composition can violate basic probability axioms even when every component is locally coherent and calibrated. The **compositional residual ε⋆** (L2 distance from composed quote to the joint coherent polytope) serves as a runtime, distribution-free certificate of system-level coherence failure. A hierarchical Boyle–Dykstra projection deterministically repairs compositions; an anytime-valid e-process enables sequential coherence monitoring.

## Core Problem

When a research component emits P(Republican)=0.6 and a forecasting component emits P(Democrat)=0.6, the agent assembles a 1.2-mass quote that no probability measure can assign — creating Dutch-book exposure arising strictly between components. Per-component calibration, self-consistency, and conformal prediction all preserve only per-output coherence properties; cross-component logical constraints are invisible to all three.

## Key Concepts

### Compositional Residual ε⋆

Given m Bernoulli questions Q₁...Qₘ with logical relations R, the set M_C = {r ∈ [0,1]ᵐ : ∃ µ ∈ Δ({0,1}ᵐ) consistent with R} is a closed convex polytope (de Finetti, 1937). The L2 projection onto this polytope gives the residual: εC(p̂) = ∥p̂ − ΠC(p̂)∥₂

### Product-Structure Dichotomy

Local coherence guarantees system coherence (under owner-selected aggregation) **if and only if** the joint polytope factorises as a Cartesian product of local polytopes. Under any tighter coupling, locally coherent component forecasts exist whose composition is globally incoherent.

### Rayleigh Quotient Prediction

The observed residual is predicted within 7% on three of four relation classes.

### Repair: Hierarchical Boyle–Dykstra Projection

Deterministic repair of composition that preserves specialist routing.

## Key Results

- Across 1,876 ensemble cliques on a four-LLM mid-tier panel: ε⋆ > 0 on 33–94% of cliques
- Translates to +0.115 nats per bet of regret on 1,770 resolved bets under proportional allocation rule
- Gain collapses to +0.006 under bettors that themselves coherentise
- Three intuitive LLM-side mitigations (retrieval, partition-aware prompting, aggregator-LLM) each fail or regress

## Connections

- [[multi-agent-systems]] — primary concept for composition failures
- [[calibration]] — per-component calibration insufficient for system-level coherence
- [[constraint-satisfaction]] — connects to CCO's approach to constraint satisfaction under distribution shift
- [[agentic-ai]] — multi-component agent architecture
- [[belief-updates]] — probabilistic belief composition

## Key Quote

> "Per-component coherence does not, in general, repair the composed system."

## Relevance to Agentic AI

Multi-component agents are the architecture du jour for deployed AI systems — planners route retrieval, arithmetic, and probability assessment to specialist subagents. This paper shows that even if every specialist is individually well-calibrated, the composed belief state can be incoherent. This is a fundamental architectural limitation, not a training bug.

## Notes

- Preliminary versions to appear at ICML 2026 workshops (CTB, AgenticUQ, FAGEN)
- Princeton University affiliation
