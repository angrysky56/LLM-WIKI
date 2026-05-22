# Researcher Discovery Report — 2026-05-27

## Discovery Cycle
- Topics researched: 2 (GRPO, MOP+RLHF interaction)
- New pages created: 1 (group-relative-policy-optimization)
- Pages updated: 0
- Cross-links added: 3 (to reward-modeling, inference-time-compute-scaling, constitutional-ai)

## New Entries

### [[group-relative-policy-optimization]]
**Group Relative Policy Optimization** — a simplified RL algorithm for LLM training that uses within-group advantage estimation instead of a separate reference model.

Key coverage:
- Definition: advantages computed relative to group mean, not against a learned critic
- Comparison table: GRPO vs PPO across baseline, reference model, critic network, variance reduction
- SD-Search context: GRPO used as outer RL loop with G=8 rollouts per group
- The key tension it addresses: GRPO removes the reference model overhead that PPO requires, but has no explicit KL constraint

Why it matters: GRPO is the workhorse algorithm behind SD-Search and EnvFactory — both researched in recent cycles. Creating a dedicated concept page clarifies the algorithm that these methods share. It also sets up the MOP+RLHF interaction question: MOP challenges RLHF's KL structure, and GRPO is part of that landscape.

## Gap Analysis

### Still thin or missing
1. **Verifier-graph theory** — entity page exists but no concept explaining the theory. Open since May 21 — still needs Ty input on concept vs synthesis classification.
2. **MOP + RLHF interaction** — addressed below as an open question.
3. **Adaptive budget learning** — how to train the gating model that estimates problem difficulty. No clear paper yet — worth monitoring.
4. **Hybrid reward models** — combining ELHSR (hidden-state) with SD-Search (process-level). Emerging direction, not yet actionable.

## Open Questions

### Resolved this cycle

**GRPO → new concept page created.** The algorithm appears in SD-Search and EnvFactory but had no dedicated page. Created `group-relative-policy-optimization.md` with the key mechanics and connections.

### Still open

**1. Verifier-graph classification**: Should the theory be a `concept` or `synthesis`? Ty's original work. Flagged May 21, still unresolved — needs decision.

**2. MOP + RLHF interaction**: MOP's stochastic policy principle challenges RLHF's KL-regularization structure. Can they be combined?

The structural tension:
- MOP: optimal policy is always stochastic; KL-regularization cancels the preference for states with many actions — self-defeating for occupancy maximization
- RLHF (PPO/DPO): KL constraint against reference model pushes toward deterministic policy

Potential resolution paths:
1. **Replace KL withoccupancy-relative regularization**: Instead of `KL(π || π_ref)`, use `KL(π(·|s) || π_group(·|s))` — push policy toward group-averaged stochasticity rather than a fixed reference. Analogous to GRPO's group-relative advantage but at the policy level.
2. **MOP as auxiliary intrinsic reward**: Keep RLHF's KL structure for alignment, add MOP's entropy bonus for behavioral diversity. This is the approach used in some toy examples but hasn't been tested at scale.
3. **Structural incompatibility**: MOP's path entropy objective and RLHF's trajectory-level reward optimization may be fundamentally incompatible — they optimize for different things.

**Status**: No published work addressing this combination specifically. Worth flagging as an open research direction.

**3. Self-correction depth**: How many self-correction passes before the model starts to over-correct? The SD-Search result (3B matches 72B with self-distillation) suggests implicit self-correction is more capable than assumed.

**4. Adaptive budget learning**: How to train the gating model that estimates problem difficulty. ELHSR has a lightweight gating mechanism but no training signal for it — it's fixed, not learned.

## Carryover Status

All established items from previous cycles remain valid:
- Constitutional AI: standalone concept ✓
- Length generalization: page exists ✓
- Self-correction: page exists ✓
- Process reward model: page exists ✓
- Inference-time compute scaling: updated with economics section ✓
- GRPO: new concept page created ✓

---

*Next run scheduled: Wednesday 2026-05-28 8:30AM*