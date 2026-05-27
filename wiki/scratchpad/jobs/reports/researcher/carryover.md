# Researcher Carryover

## Open Items

1. **Schema competition** (low priority) — open from prior cycles. librarian flagged 10 merge candidates from similarity analysis.
2. **Bounded memory budget optimization** (med priority) — capacity/saturation theme. Connects QES/ESSA/LLaMA-NAS.

## Completed This Run

### MOP vs Fine-Tuning Boundary (t_b1e3b062cbc54e42)

Full synthesis achieved across three existing pages that had the core content but weren't well-connected:

**1. `mop-and-rlhf-interaction.md` (substantial expansion):**
- Added the KL formal critique from MOP paper Supplemental Sec. F: KL(π||π_ref) with uniform default penalizes states with many actions — self-defeating for occupancy maximization
- Formal distinction: absolute entropy (MOP's path entropy, unique measure per Theorem 1) ≠ relative entropy (KL, divergence from reference)
- Added new section: "Relationship to Fine-Tuning" — pre-training (MOP-compatible, no reference), fine-tuning (MOP-incompatible by default, KL tether added), MoE routing collapse data from SafeMoE
- "When Fine-Tuning Can Be Made MOP-Compatible" — three conditions: remove reference, replace regularization target, use absorbing states instead of KL
- Connections updated — added `[[ramirez-ruiz-mop-2024]]`, `[[route-collapse-rlhf]]`, `[[mop-edm-cognitive-architecture]]`

**2. `mop-architecture.md` (added major section):**
- Added "MOP vs Fine-Tuning: When Memory, When Weights?" — full decision matrix covering mechanism, strengths, weaknesses for each path
- Factor table: experience type, update frequency, forgetting tolerance, interpretability need, budget, pattern stability, generalization
- Key insight: MOP memory for novel/episodic/revocable experience; fine-tuning for stable patterns confirmed across many sessions
- Architectural implication: MOP-as-Layer-0 + fine-tuning for stable knowledge must be kept operationally separated

**3. KL Regularization Critique (from mop-edm-cognitive-architecture synthesis):**
- Confirmed per above — MOP paper Supplemental Sec. F proves KL-self-defeating structure

## Sources Read
- maximum-occupancy-principle.md (concept — full detail on MOP parameters and properties)
- ramirez-ruiz-mop-2024.md (source — paper summary with empirical results)
- reinforcement-learning-from-human-feedback.md (concept — RLHF pipeline, algorithms, MOP tension)
- mop-and-rlhf-interaction.md (concept — three resolution paths, prior version)
- mop-edm-cognitive-architecture.md (synthesis — KL regularization critique, three implementation levels)
- group-relative-policy-optimization.md (concept — GRPO structure, MoE relevance)
- mop-architecture.md (concept — four-layer memory schema, MOP-as-L0 integration)
- mop-explorer.md (entity — project using MOP as EFHF Layer 0)

## Status
All MOP vs fine-tuning boundary content now coherent across: MOP theory, RLHF methods, fine-tuning mechanics, decision framework, and architecture integration. The structural tension is articulated with the mathematical proof from the MOP paper as grounding.
