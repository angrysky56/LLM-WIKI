---
created: 2026-06-27
updated: 2026-06-27
type: report
summary: Researcher discovery report
tags: [researcher, report]
---

# Researcher Discovery Report — 2026-06-27

## Discovery Cycle
- Topics researched: 3 (MoE routing collapse under fine-tuning/RLHF)
- New pages created: 3 source summaries
- Pages updated: 1 (mop-and-rlhf-interaction.md)
- Cross-links added: 3 (internal wiki links in updated pages)

## New Entries

### Source Summaries Created
1. **`wiki/sources/on-the-representation-collapse-of-sparse-mixture-of-experts.md`** — Chi et al. (Microsoft, 2022). Core finding: MoE routing mechanism structurally encourages token clustering around expert centroids (representation collapse), not just a fine-tuning artifact. Proposed hypersphere routing on low-dimensional sphere as fix. Cross-lingual pre-training experiments. Pre-training-level evidence for routing degeneracy.

2. **`wiki/sources/defending-moe-llms-against-harmful-fine-tuning-via-safety-routing-alignment.md`** — Kim et al. (2025). **Direct empirical confirmation of routing drift under fine-tuning**. OLMoE harmfulness score: 62.0 post-fine-tuning (vs. aligned baseline). Routing weights for harmful inputs change substantially after fine-tuning — safety-critical experts no longer handle harmful tokens. Confirmed across 7B to 141B architectures (OLMoE, gpt-oss, Llama 4). SafeMoE proposes routing-space penalty to preserve pre-fine-tuning routing distribution.

3. **`wiki/sources/moe-sieve-routing-guided-lora-for-efficient-moe-fine-tuning.md`** — Manzoni (2026). Per-layer expert routing is **already highly skewed pre-fine-tuning**: top-25% of experts handle most tokens, bottom-75% are "cold". Only adapting top-25% via LoRA is competitive (±1pp). Cold expert adaptation introduces gradient noise without accuracy gains. Confirms skewed utilization is structural, not purely RLHF-induced.

### Updated Entries
1. **`wiki/concepts/mop-and-rlhf-interaction.md`** — Open question #2 (MoE routing collapse under RLHF) marked as **EMPIRICALLY CONFIRMED**. Updated with three empirical papers. Added two new open questions (pre-existing skew, pre-training collapse). Updated Limitations section with nuance about SafeMoE not being standard RLHF.

## Key Findings

### Q: Is MoE routing collapse under RLHF happening in practice?
**A: Yes — but the picture is more nuanced than expected.**

1. **Routing drift is real**: SafeMoE (Kim 2025) empirically shows fine-tuning changes routing weights significantly. Safety-critical routing for harmful inputs collapses post-fine-tuning. This is direct evidence of routing instability.

2. **Routing skew pre-exists fine-tuning**: MoE-Sieve (Manzoni 2026) shows per-layer utilization is already highly skewed pre-fine-tuning (top-25% handles most tokens). Fine-tuning compounds this skew rather than creating it from a uniform baseline.

3. **Pre-training collapse is structural**: Chi et al. (2022) shows the token-clustering-around-experts tendency is inherent to MoE routing mechanisms — not just an artifact of RLHF or fine-tuning.

4. **Scale**: Routing drift observed at 7B–141B parameters — not frontier-only.

### The Nuance
The original question assumed RLHF causes collapse from a healthy diverse baseline. The evidence suggests the problem is:
- Pre-existing skew (the baseline was already not uniform)
- Compounded by fine-tuning (especially safety-critical routing drifts)
- Structural to the MoE routing mechanism itself (starts in pre-training)

This changes the resolution paths: it's not just about preventing fine-tuning collapse, but about preserving whatever expert diversity survives pre-training.

## Gap Analysis
- Still no direct study of standard RLHF (PPO/GRPO/DPO) routing collapse in MoE LLMs — SafeMoE is alignment-specific, not general RLHF
- No published comparison of resolution paths (Path 1/2/3) for the MOP+RLHF tension
- GRPO for MoE remains empirically untested
- The "MOP training for transformers" question still needs exploration

## Related
- [[scratchpad/jobs/reports/researcher/discovery-2026-06-27]]
- [[index]]

- [[discovery-2026-06-27]]

## Open Questions Remaining
- Adaptive budget learning (how to train the gating model)
- Hybrid reward models (ELHSR + SD-Search)
- Reward hacking detectability
- Category theory for attention verification
- Cognitive world models for LLM agents
- MOP training for transformers
