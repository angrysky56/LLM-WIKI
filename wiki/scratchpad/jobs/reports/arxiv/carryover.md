---
summary: arxiv agent carryover — Shannon Scaling Law, SkillOpt, SkillLens — bounded representation capacity theme
updated: 2026-05-26T00:00:00Z
---

---
created: 2026-05-26T00:00:00Z
updated: 2026-05-26T00:00:00Z
type: report
summary: "arxiv agent carryover — 2026-05-26 batch: Shannon Scaling Law (finite LLM capacity via SNR), SkillOpt (trainable skill docs), SkillLens (negative transfer is common, meta-skill reduces it)"
tags: [arxiv, carryover]
status: active
confidence: high
---

# arxiv Agent — Carryover

## Run History

||| Date | Result | Notes |
|||------|--------|-------|
||| 2026-05-18 | 3 papers ingested | EnvFactory, SD-Search, LMAC — credit assignment theme |
||| 2026-05-20 | No new papers | arXiv late-UTC batch not yet posted |
||| 2026-05-21 | 3 papers ingested | EqR (attractors), DeepWeb-Bench, hyperparameter transfer |
||| 2026-05-23 | 3 papers ingested | VPO (diversity RL), DeltaDirect (motion blindness), Recuriosity (3D exploration) — test-time scaffolding theme |
||| 2026-05-24 | 3 papers ingested | ProxySHAP (Shapley/Banzhaf), Boiling the Frog (agentic safety), CUSP (scientific forecasting) — verification/trust theme |
||| 2026-05-26 | 3 papers ingested | Shannon Scaling Law (finite LLM capacity), SkillOpt (trainable skill docs), SkillLens (skill lifecycle, negative transfer) — **bounded representation capacity theme** |

## Current State

- **arXiv**: 2026-05-26 batch fully processed — 3 papers ingested
- **arXiv API**: No rate limiting; behaved normally throughout
- **Wiki paper inventory**: ~323 pages

## Papers Ingested (2026-05-26 batch)

||| Paper | arXiv ID | Key Finding | Wiki Connection |
|||-------|----------|-------------|------------------|
||| Shannon Scaling Law | 2605.23901 | LLM capacity bounded by SNR; U-shaped degradation emerges past critical model-data ratio; extrapolates with R²=0.847 | Connects to [[efhf]], [[verifier-graph]], [[maximum-occupancy-principle]], [[mop-explorer]] |
||| SkillOpt | 2605.23904 | First systematic text-space optimizer for agent skills — skill documents are trainable external state with validation gating, edit budgets, and epoch-wise meta updates; best on 52/52 cells | Connects to [[efhf]], [[agentic-research]], [[mop-explorer]], [[maximum-occupancy-principle]] |
||| SkillLens | 2605.23899 | Full skill lifecycle study — negative transfer is common and non-trivial; skill utility is independent of model scale; meta-skill that guides extraction toward utility-features reduces negative transfer | Connects to [[efhf]], [[agentic-research]], [[mop-explorer]], [[verifier-graph]] |

## Cross-Paper Theme: Bounded Representation Capacity

**The unifying finding**: The failure mode of bounded representations is **saturation-induced degradation**, not mere sub-optimality.

| System | Representation | Saturation Failure |
|--------|---------------|-------------------|
| LLM (Shannon Law) | Model weights | U-shaped loss — scaling past SNR threshold degrades performance |
| Skill document (SkillOpt) | External text state | Harmful rewrites accumulate when validation gate is absent |
| Skill transfer (SkillLens) | Transferred skill | Negative transfer when skill exceeds target's semantic capacity |

**Design principle**: Every bounded adaptation step must be verification-gated with a capacity-constrained step size.

## Notes for Next Run

- **World-model improvement as next theme continues**: Given the bounded representation theme, next cycle should search for papers on: model editing, knowledge unlearning, skill compaction/compression, uncertainty-aware planning, or adaptive world model improvement via environment interaction.
- **The SNR ↔ reliability mapping**: The Shannon Scaling Law's SNR-to-capacity mapping (C = B log₂(1+S/N)) is structurally identical to the reliability ratio in [[verifier-graph]] — both track signal quality relative to noise. Papers on calibrated confidence scores or uncertainty-aware verification would deepen this thread.
- **Capacity-aware skill construction**: SkillOpt's bounded edits and SkillLens's meta-skill both point to a general principle: skill documents should be constructed with explicit capacity budgets relative to target model scale. A "skill capacity planning" thread would bridge these papers.
- **Papers worth revisiting**: LCGuard (2605.22786, multi-agent KV sharing safety), HarnessAPI (2605.22733, MCP+HTTP unified endpoints), ProxySHAP (2605.22738 — the SNR/exact-Shapley structure exploit pattern appears in both ProxySHAP and the Shannon Scaling Law)