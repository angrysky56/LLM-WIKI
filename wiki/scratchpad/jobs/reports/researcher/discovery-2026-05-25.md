# Researcher Discovery Report — 2026-05-25

## Discovery Cycle

- Topics researched: 1 (adaptive budget learning / gating model training)
- New pages created: 2 (adaptive-budget-learning.md, early-exit-networks.md)
- Pages updated: 2 (adaptive-computation.md, mixture-of-experts.md)
- Cross-links added: 5

## New Entries

### wiki/concepts/adaptive-budget-learning.md
Created comprehensive concept page covering:
- Core problem: gradient blocking in gating models (receiving gradients only through selected paths)
- 5 training approaches: supervised auxiliary losses, RL for compute allocation, teacher-guided routing (TGR-MoE 2026), two-stage training (LGViT 2023), jointly trained confidence estimation (ADEPT 2026)
- Key findings from 8 papers: SafeMoE routing collapse under RLHF, TGR-MoE teacher guidance, SPAR-K fixed-depth schedule for speech, ADEPT token-level confidence, BEExformer soft-routing loss, DAISY self-supervised exit signal
- 5 open questions: credit assignment, scalability to 100B+, RLHF interaction, unified budget loss, sample-level vs token-level decisions

### wiki/concepts/early-exit-networks.md
New concept page derived from adaptive budget research:
- Confidence-based, entropy-based, and fixed-depth exit strategies
- Training strategies: deep supervision, two-stage (LGViT), joint confidence estimation
- Key tradeoff: shallow classifiers get weaker representations
- Connection to adaptive budget learning via shared gating problem

## Updated Entries

### wiki/concepts/adaptive-computation.md
Upgraded from stub to linked hub:
- Added links to adaptive-budget-learning (which substantially fills it), mixture-of-experts, early-exit-networks

### wiki/concepts/mixture-of-experts.md
Added bidirectional link to adaptive-budget-learning:
- New connection: gradient blocking problem in gating/training section points to adaptive-budget-learning
- adaptive-budget-learning connects back to MoE

## Gap Analysis

- [[route-collapse-rlhf]] — mentioned in adaptive-budget-learning but not a full page; SafeMoE paper exists (Kim 2025) that should be synthesized
- [[inference-time-compute-scaling]] — appears in MoE connections but not a concrete page yet
- [[mixture-of-recursions]] — mentioned in knowledge graph; related to dynamic recursive depth

## Open Questions

1. **No established "unified compute budget loss"** — all existing approaches use hand-tuned weighted combinations of task loss + entropy + load-balancing. A principled approach is a real research gap.

2. **RLHF + routing interaction mechanism** — SafeMoE empirically confirmed routing collapse under RLHF but the mechanism (policy injection vs reward shaping) is not characterized. Requires deeper analysis of SafeMoE paper.

3. **Per-sample vs per-token gating** — current MoE is per-token; for classification tasks, task-conditioned routing signatures (MoE-XRAY) suggest per-sample might work. Open question whether this generalizes to generative tasks.

4. **Test-time compute + MoE integration** — MoE already provides sparse per-token compute; combining with BoN/PRM search would multiply cost by N candidates. Unclear if any work has addressed this.