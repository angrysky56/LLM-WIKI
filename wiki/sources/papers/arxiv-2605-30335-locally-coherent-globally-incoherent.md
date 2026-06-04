---
created: 2026-06-04T00:00:00Z
updated: 2026-06-04T00:00:00Z
type: source
summary: "Locally Coherent, Globally Incoherent — Kotawala (Princeton): formalises the L2 compositional residual ε★ for multi-component LLM agents; shows local coherence does NOT imply global coherence in 33–94% of 1,876 ensemble cliques across Claude-Haiku/GPT-5.4/Llama-3.3, and that retrieval, partition-aware prompting, and aggregator-LLM mitigations all fail or regress."
tags: [arxiv, paper, multi-agent, calibration, bounded-self-model, constraint-satisfaction, agentic-ai, capability-deployment-gap, compositional-incoherence]
sources: https://arxiv.org/abs/2605.30335
status: active
confidence: 0.9
---

# Locally Coherent, Globally Incoherent — Kotawala (2026)

> **One-line:** A system of locally-coherent probabilistic components can be globally incoherent. Kotawala gives a runtime-computable L2 distance ε★ from the joint coherent polytope, a hierarchical Boyle–Dykstra projection to repair it, and an anytime-valid e-process to monitor it. Then shows the standard LLM-side mitigations *do not work*.

**arXiv:** 2605.30335 · 25 pages · Princeton · Anany Kotawala · accepted to ICML 2026 workshops (CTB, AgenticUQ, FAGEN).

## Problem

Foundation-model evaluation reports per-question accuracy, calibration, and proper scoring. But once a system is *composed* of several model calls — each seeing only a slice of the joint problem — there is no instance-wise guarantee on joint coherence. The standard worry is multi-agent LLM systems. Kotawala makes this worry *measurable*.

## Method

1. **Compositional residual ε★.** L2 distance from the composed probabilistic quote to the joint coherent polytope defined by declared cross-component coupling constraints. Computable at runtime from system output + declared constraints. **No access to model internals required.**
2. **Product-structure dichotomy.** Characterises when local coherence *is* sufficient (the polytope is a Cartesian product of per-component half-spaces) and when it is not (coupled constraints like unit-sum partitions).
3. **Rayleigh-quotient prediction.** Closed-form estimator for ε★ from coupling-constraint spectra; matches observed residual within 7% on three of four relation classes (negation, conjunction, disjunction, partition).
4. **Hierarchical Boyle–Dykstra projection.** Deterministic repair — repeatedly project onto the constraint sets in priority order. Reduces mean exposure bound √(m★·ε★) to 1.7×10⁻¹⁴ on the 1,876-clique ensemble.
5. **Anytime-valid e-process.** Sequential coherence monitoring with Type-I error control under optional stopping — deployable on a stream of bets/forecasts.

## Results

**Prevalence.** On 1,876 ensemble cliques across a four-LLM mid-tier panel (Claude-Haiku-4.5, GPT-5.4-mini, GPT-5.4-nano, Llama-3.3-70B):
- ε★ > 0 on **33–94% of cliques** depending on relation class
- 66% on negation, 43% on disjunction, 33% on conjunction
- **Frontier-panel rerun (5.5):** ε★ > 0 on **97.8%** of matched partition bets — upgrading the roster reduces *magnitude* but not *prevalence*. This is a strong empirical claim: **scaling the components does not fix compositional incoherence**.

**Economic impact.** Across 1,770 resolved bets:
- Coherentised bettor (using the projection): **+0.115 nats per bet of regret** under proportional allocation
- "Self-coherentising" bettor (each component applies the fix locally): collapses to +0.006 nats
- Translation: a *system-level* repair is worth ~20× what a per-component repair is worth.

**LLM-side mitigations (all fail):**
- Retrieval-augmented components: fails
- Partition-aware prompting (INFORMED condition, mean paired Δε★ = +0.221, 95% CI [+0.173, +0.270], p=2.6×10⁻¹⁰): **3/20 partitions worsen** when the components are already roughly coherent
- Aggregator-LLM (an LLM resynthesises the joint quote): regresses

**Mechanism.** Per-specialist attribution on the 894 positive-residual cliques: GPT-5.4-mini carries the largest attributed L2 mass per clique (0.120), explaining why upgrading only that model changes magnitude but not prevalence.

## Limitations

- Theoretical contribution is for *probabilistic* composition with declared coupling constraints. Real systems often have implicit couplings (e.g. shared context, shared retriever) that aren't easy to declare up front.
- Hierarchical projection is a *post-hoc* repair, not a *training* or *fine-tuning* solution. The paper does not propose how to make components produce globally-coherent quotes in the first place.
- Per-component error attribution is diagnostic, not causal — knowing GPT-5.4-mini is the worst contributor does not directly tell you how to fix it.
- Evaluation is on a specific class of partition/negation/conjunction bets; whether the same residual pattern holds for open-ended generative composition is unshown.

## Wiki Connections

- **[[bounded-self-model]]** (current theme): the cleanest empirical demonstration yet that *the components' self-models are individually well-formed but jointly inconsistent*. This is the multi-agent analogue of [[faithful-confidence-lrm-2026]]'s "what the model says vs what it does" gap — extended across component boundaries. The failure is not in any one model; it is in the *composition* of bounded self-models.
- [[calibration]]: prior calibration work is per-question. Kotawala is per-*system*. Re-scopes calibration from a model property to a system property.
- [[multi-agent-llm]]: the 4-LLM mid-tier panel is exactly the kind of routing ensemble that's now common in production agentic systems. Result: routing ensembles are *structurally* biased.
- [[capability-vs-deployment-gap]] (theme 2026-06-02): same diagnosis at a different scale. A model can be highly capable per-question and still be a *bad* system component. Frontier upgrades don't fix this.
- [[agentic-ai]]: 33–94% prevalence is a structural finding, not an edge case. Any safety/oversight argument that treats each LLM call in isolation is missing the actual failure mode.
- **Future synthesis candidate:** "System-level coherence" — unifies Kotawala's ε★ with the structural-reuse / bounded-self-model themes. Core claim: coherence is a system property, and a system can be locally-better and globally-worse simultaneously.

## Key Quote

> "Multi-component LLM agents assemble probabilistic claims from components that each see only part of a joint problem; the composition can violate basic probability axioms even when every component is locally coherent." — Kotawala, abstract

> "ε★ > 0 on 33–94% of cliques" — main-text prevalence result (mid-tier panel); 97.8% on the frontier panel.

### Cross-cycle (2026-06-03 batch)
- **Kotawala ↔ [[faithful-confidence-lrm-2026]]:** FC measures a single-model faithfulness gap. Kotawala measures a multi-model compositional gap. Both formalise the same underlying failure ("the *system's* report diverges from the *system's* true state") at different scales. FC uses prefix-conditioned sampling to estimate intrinsic confidence; Kotawala uses the L2 distance to the joint coherent polytope to estimate incoherence. Same meta-problem.
- **Kotawala ↔ [[skill-rm-2026]]:** Skill-RM is a *single-model* procedural evaluator. Kotawala's compositional residual ε★ is what happens when you compose many such evaluators: each is locally coherent, the composition is not. Skill-RM scales to a system; Kotawala measures the system-level failure.
- **Kotawala ↔ [[sleep-self-modify-consolidate-2026]]:** Sleep self-modifies a single component. Kotawala composes many components. Both are *self-management* operations, but at different scopes. Open question: does a sleep-trained component compose better into a multi-agent system?
