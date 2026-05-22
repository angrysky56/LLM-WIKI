# Researcher Discovery Report — 2026-05-26

## Discovery Cycle
- Topics researched: 1 (inference-time compute economics)
- New pages created: 0
- Pages updated: 1 (inference-time-compute-scaling)
- Cross-links added: 1 (Hermes deployment implications)

## Updated Entries

### [[inference-time-compute-scaling]]
**Updated with Economics Section** — Added a dedicated economics analysis section addressing the carryover gap.

Key additions:
- **Four-variable trade-off framework**: Error cost × accuracy gain vs compute cost, with domain-specific guidance
- **Decision rule**: `error_cost × accuracy_gain > compute_cost` — when this holds, inference-time scaling pays
- **Domain-specific recommendations**:
  - High error cost + verifiable (code/math/legal): BoN-64 with PRM-guidance, almost always justified
  - Low error cost + subjective (chat/creative): Single-pass dominates
  - Medium error cost + verifiable (fact QA): ELHSR-style adaptive gating
- **Compute-optimal budget analysis**: Marginal accuracy gain formula `ΔA = (1-p)ⁿ⁻¹ × p`; diminishing returns flatten around N=16–64
- **Hermes deployment implications**: Four-tier guidance by task type — tool calls, research synthesis, casual conversation, long-context reasoning

Removed Open Question #4 ("Inference cost vs accuracy tradeoff") and folded its content into the new economics section since it now has a proper answer.

## Gap Analysis

### Still thin or missing
1. **Verifier-graph theory** — entity page exists but no concept explaining the theory. Needs Ty input on concept vs synthesis classification. Still open since May 21.
2. **MOP fine-tuning** — MoE fine-tuning complexity. Left as a note; not a priority gap.
3. **Hybrid reward models** — combining ELHSR (hidden-state) with SD-Search (process-level). Emerging direction, not yet actionable.
4. **Adaptive budget learning** — how to train the gating model that estimates problem difficulty. No clear paper yet; worth monitoring.

## Open Questions

1. **Verifier-graph classification**: Should it be a `concept` or `synthesis`? Ty's original work. Flagged May 21, still unresolved — needs decision.
2. **MOP + RLHF interaction**: MOP's stochastic policy principle challenges RLHF's KL-regularization structure. Is there a way to combine them that preserves both properties?
3. **Self-correction depth**: How many self-correction passes before the model starts to over-correct? The SD-Search result (3B matches 72B with self-distillation) suggests implicit self-correction is more capable than assumed.

## Carryover Status

All established items from previous cycle remain valid:
- Constitutional AI: standalone concept ✓
- Length generalization: page exists ✓
- Self-correction: page exists ✓
- Test-time compute economics: resolved this cycle ✓

---

*Next run scheduled: Tuesday 2026-05-27 8:30AM*