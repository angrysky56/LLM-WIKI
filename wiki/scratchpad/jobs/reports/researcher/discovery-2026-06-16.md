---
summary: Jun 16 cycle: shapley-values concept promoted from stub (0.3→0.75), cross-domain verification for steering-vectors and fine-tuning, 1145 pages in index
tags: [researcher, report, concept-advancement]
updated: 2026-06-05T22:57:08Z
created: 2026-06-05T22:57:08Z
---

# Researcher Discovery Report — 2026-06-16

## Discovery Cycle

- Topics researched: 1 (shapley-values), plus cross-domain verification for steering-vectors and fine-tuning
- New pages created: 0
- Pages updated: 1
- Cross-links added: 2 (shapley-values ↔ shap, proxy-based-shapley-banzhaf-2026)

## Focus: Concept Advancement

**Primary**: shapley-values promotion (carryover priority — pre-existing source anchor)

### shapley-values: Stub → Full Concept Page (0.3 → 0.75)

**What changed**: Promoted the game-theoretic foundation stub into a full concept page covering:
- Formal definition and Shapley's 1953 axiomatization (4 axioms)
- Uniqueness theorem (Shapley proved it's the unique function satisfying efficiency, symmetry, dummy player, and additivity)
- Relationship to the Banzhaf value — key trade-off (efficiency vs raw influence)
- Computational complexity (#P-complete in general; polynomial-time via ProxySHAP's tree proxy approach)
- Applications: cost allocation, voting power (Shapley-Shubik index), data valuation (Ghorbani & Zou 2019)
- SHAP as the ML instantiation — correctly distinct from the game theory foundation
- 4 genuine open questions (causal Shapley, sequential games, ν selection criterion, large-scale data Shapley)

**Source anchors**:
- [[sources/papers/proxy-based-shapley-banzhaf-2026]] (0.85) — provides the game-theoretic framing, Banzhaf comparison, and polynomial-time estimation result
- Lundberg & Lee 2017 (referenced externally) — axiomatic connection to SHAP

## Cross-Domain Verification

As requested by carryover: verified cross-domain connections for Jun 5's promotions.

### steering-vectors
- **Connections**: All ML — activation-engineering, mechanistic-interpretability, bounded-representation-capacity, model-editing
- **Non-ML bridges**: Potential through [[behavioral-credibility-trilemma]] (if activation-level intervention resolves the calibration/autonomy trade-off) — but no explicit link yet
- **Genuine gap**: No governance, alignment-theory, or cognitive-science cluster connections

### fine-tuning
- **Connections**: All ML — PEFT, LoRA, instruction-tuning, transfer-learning
- **Non-ML bridges**: Potential through AI diagnostics (fine-tuning as diagnostic probe) or safety routing alignment (AI safety) — but no explicit links
- **Genuine gap**: No cross-domain bridges exist yet; fine-tuning remains entirely within ML domain

**Assessment**: Neither page has natural cross-domain bridges that aren't forced. The behavioral-credibility-trilemma connection for steering-vectors is the most plausible, but it remains within the same cluster (Cluster 7: reasoning/evaluation). Genuine cross-domain bridges would need a different abstraction layer.

## Gap Analysis

### Remaining high-priority stubs (from ~73 ML concept stubs):
1. **mechanism-design** (confidence 0.3) — has reciprocal link to shapley-values; both are game theory stubs. shapley-values is now promoted; mechanism-design should follow.
2. **model-interpretation** (confidence 0.3) — the broader concept that subsumes SHAP. Stub; SHAP is a sub-concept.
3. **causal-reasoning** (confidence 0.3) — connects to shapley-open-questions about causal vs predictive attribution
4. Entity stubs: anthropic, huggingface, sakana-ai, priorlabs, google-deepmind (all confidence 0.3) — deferred from previous cycle

### Cross-domain synthesis opportunities
- steering-vectors ↔ behavioral-credibility-trilemma — activation-level intervention as trilemma resolution
- shapley-values ↔ verifier-graph — both involve verification of distributed contributions
- ProxySHAP pattern (tree proxy + residual correction) ↔ EFHF's layer verification (both use tractable surrogates for intractable verification)

## Open Questions

1. **shapley-values**: Should a concept page for "data Shapley" (data valuation) be written? Currently covered inline in shapley-values; may need separate page if the topic grows.
2. **mechanism-design**: Is it worth promoting next cycle? It has a reciprocal link to shapley-values, so the connection is already live. But it lacks a source anchor — would need source fetching.
3. **Cross-domain bridge for steering-vectors**: The behavioral-credibility-trilemma link is tempting but would synthesis — is activation-level intervention truly a trilemma resolution mechanism, or is it orthogonal? Needs deeper investigation.

## Wiki State

- Total pages: 1145 (up from ~1141 last cycle)
- Concept stubs remaining: ~72 (shapley-values removed from stub count)
- Entity stubs remaining: ~12
