# Researcher Discovery Report — 2026-05-26

## Discovery Cycle
- Topics researched: 8 pages across MOP theory, RLHF methods, GRPO, and cognitive architecture
- New pages created: 0 (all content already existed, work was synthesis and expansion)
- Pages updated: 2 (**mop-and-rlhf-interaction.md**, **mop-architecture.md**)
- Cross-links added: 3 (ramirez-ruiz-mop-2024, route-collapse-rlhf, mop-edm-cognitive-architecture)

## New/Updated Entries

### mop-and-rlhf-interaction.md — substantial expansion
**What changed:** The page existed with three resolution paths but lacked the mathematical grounding for why KL is structurally incompatible with MOP. Added:

1. **The KL Formal Critique** (from MOP paper Supplemental Sec. F): Proved that `KL(π||π_ref)` with uniform default policy penalizes states with many available actions — self-defeating for occupancy maximization. The immediate return becomes `H(A|s) - ln|A(s)|` where the `-ln|A(s)|` term actively suppresses the states MOP most wants to maximize.

2. **Absolute vs. Relative Entropy** as the core theoretical distinction: Path entropy (MOP's measure, unique per Theorem 1) is not merely different from KL divergence — it's a different measurement primitive entirely. MOP counts actual paths; KL measures divergence from reference.

3. **Relationship to Fine-Tuning** section: Pre-training (no reference, MOP-compatible) vs fine-tuning (KL tether added, MOP-incompatible by default). Three ways to make fine-tuning MOP-compatible: remove reference (GRPO path), replace regularization target (group-relative), use absorbing states instead of KL.

4. **Expanded connections**: Added `[[ramirez-ruiz-mop-2024]]`, `[[route-collapse-rlhf]]`, `[[mop-edm-cognitive-architecture]]`

### mop-architecture.md — new section added
**What changed:** Added "MOP vs Fine-Tuning: When Memory, When Weights?" — a full decision matrix addressing the open question. Includes:
- Path 1 (MOP memory compression): mechanism, 5 strengths, 3 weaknesses
- Path 2 (fine-tuning): mechanism, 3 strengths, 4 weaknesses  
- Factor table: experience type, update frequency, forgetting tolerance, interpretability need, budget, pattern stability, generalization
- Key insight: MOP memory for novel/episodic/revocable experience; fine-tuning for stable patterns confirmed across many sessions
- Architectural implication: MOP-as-Layer-0 + fine-tuning must be kept operationally separated because fine-tuning risks destroying the stochasticity MOP depends on

## Gap Analysis
- **mop-next-token-prediction.md** (stub) — applying MOP to transformer training from scratch. Very thin. Could be expanded with the Level 2 implementation insights from mop-edm-cognitive-inarchitecture.
- **route-collapse-rlhf.md** — empirics of MoE routing collapse under RLHF. SafeMoE citation confirmed. Page may exist but not yet connected.
- **eviction policy for MoE routing** — no existing page. The pre-training skew in MoE-Sieve (top-25% experts handle most tokens pre fine-tuning) is a distinct topic from RLHF-induced collapse.

## Open Questions
1. **Which resolution path is correct?** All three are theoretically coherent but empirically untested in a systematic comparison.
2. **GRPO for MoE diversity** — can GRPO naturally preserve expert diversity? Open empirical question.
3. **Level 2 MOP training** — absolute entropy + absorbing states replacing KL as the regularization mechanism — remains theoretical, no LLM-scale implementation exists.
4. **Pre-training skew compounding** — MoE-Sieve shows skewed routing pre-exists fine-tuning. Is the RLHF effect compounding a pre-existing skew, or creating a new one?
