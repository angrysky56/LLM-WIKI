---
summary: Shows skill rewriting is not prompt compression — shorter skills can make agents more expensive by removing sparse operational anchors that prevent exploration, debugging, and recovery. Economic lens on skill optimisation.
tags: [agent-skills, skill-rewriting, prompt-compression, cost-analysis, arxiv-2026-06-09]
updated: 2026-06-09T15:06:39Z
created: 2026-06-09T15:06:39Z
---

# What Should a Skill Remember? Quality-Cost Trade-offs in Cost-Aware Skill Rewriting

**arXiv:** 2606.09421 | **Authors:** Qinghua Xing, Yinda Chen, Yaping Jin, Zhenhe Wu, Bohan Lin

## Problem

Large language model agents increasingly rely on **skills** — reusable procedural documents encoding workflows, tool-use patterns, implementation patterns, validation checks, and domain rules. As skill libraries grow, there is natural pressure to rewrite skills for compression, maintenance, and quality. The conventional approach treats skill rewriting as **prompt compression**: reduce token count while preserving task accuracy. But this paper identifies a counter-intuitive failure mode: **shorter skills can make agents more expensive** by removing sparse operational anchors that prevent costly exploration, debugging, and recovery.

## Method — Economic Lens on Skill Rewriting

The paper reframes skill rewriting as an **economic optimisation problem** with three cost components:

1. **Upfront cost** (C_u): tokens used per invocation — the standard compression target
2. **Exploration cost** (C_e): additional tokens and API calls the agent spends when a skill lacks sufficient guidance — the agent wanders, tries irrelevant approaches, or generates incorrect outputs that must be discarded
3. **Debugging cost** (C_d): recovery actions when an under-specified skill leads to errors — re-planning, backtracking, error correction loops

The total cost C_total = C_u + C_e + C_d. The key insight: **compression reduces C_u but can increase C_e and C_d** — sometimes enough that C_total rises.

**Operational anchors** are the elements in a skill that prevent these costs: validation checks that catch errors early, recovery procedures that handle edge cases, domain rules that constrain the agent's action space, and examples that demonstrate the desired output format. These are the first things removed during naive compression, but they are also the most economically valuable parts of the skill.

The paper proposes **cost-aware rewriting** that models this trade-off:

- Identify operational anchors via ablation — measuring C_e+C_d impact when each anchor is removed
- Rewrite decisions based on the marginal cost impact, not just token reduction
- A skill rewrite is economically beneficial iff ΔC_total < 0

## Results

Evaluated on a suite of agent tasks with skills of varying complexity (web navigation, API orchestration, data processing, tool chaining):

| Metric | Naive Compression | Length-Only Optimisation | Cost-Aware Rewriting |
|--------|-------------------|-------------------------|---------------------|
| Token reduction | **55%** | **40%** | 25% |
| ΔC_total | **+18%** (more expensive!) | +5% | **−12%** |
| Error rate | +14pp | +6pp | −2pp |
| Debugging loops/run | +0.7 | +0.3 | −0.1 |

Key findings:
- **Naive compression consistently increases total cost** — token savings dwarfed by additional exploration and debugging
- **~20% of skill content accounts for ~80% of C_e+C_d prevention value** (Pareto distribution of operational anchors)
- **The optimal rewrite is not the shortest valid skill** — it is the skill that minimises C_total
- **Anchors are domain-specific** — validation checks matter more for data-processing; recovery procedures matter more for tool-chaining

## Limitations

- Evaluated on scripted agent environments; real-world deployments have additional cost dimensions (latency SLAs, user satisfaction, error propagation)
- Operational anchor identification via ablation is expensive (requires n+1 runs per skill)
- The cost model assumes independent skills; compound costs from interacting skill rewrites are not modelled
- Does not address the **security angle** — removing anchors could create gaps exploitable by poisoned skills

## Connections

- [[reuserl-skill-reuse-compression-2026]] — ReuseRL uses MDL-grounded compression for skill extraction from trajectories. This paper studies compression at the *skill-documentation* level. Both converge on: compression must account for the cost of decompression errors.
- [[skillopt-self-evolving-2026]] — Self-evolving skills that update based on experience. Cost-aware rewriting provides the economic objective for those updates.
- [[skillharm-lifecycle-skill-attacks-2026]] — Security counterpoint: if operational anchors are removed for cost reasons, the resulting thinner skills have higher attack surface for poisoning.
- [[skill-rm-2026]] — Skill-RM reformulates reward evaluation as an agent skill; its operational anchors (mandatory evidence fields) are exactly the kind this paper would protect.
- [[codeskill]] — Code-oriented skills where operational anchors (test cases, error handling) are most critical.
- [[muse-autoskill]] — Automatic skill generation; this paper provides the economic criteria for deciding whether a generated skill is worth its token cost.
- [[bounded-representation-capacity]] — The skill-rewriting trade-off is a manifestation of bounded capacity: the agent cannot afford to keep all anchors, and the cost of removing the wrong ones is disproportionately high.

## Key Quote

> "The economic value of skill rewriting is not captured by skill-token compression alone. A rewrite is useful only when it preserves or strengthens the sparse operational anchors that prevent exploration, debugging, and recovery."

## Discussion

This paper is the **economic counterpart** to the wiki's existing skill coverage. The current theme arc runs: skill generation (SkillOpt, CodeSkill, MUSE-Autoskill) → skill compression (ReuseRL) → skill attacks (SkillHarm) → skill evaluation (Skill-RM) → **skill economics** (this paper).

The economic lens is a **methodological upgrade** over the pure compression framing: it makes explicit that skill optimisation is a multi-objective problem where token-efficiency and operational robustness trade off. This connects to the **bounded-self-model** theme — the skill is an externalised representation of the agent's capability, and rewriting it changes the boundary of what the agent can (and cannot) recover from autonomously.

For the **capability-vs-deployment gap**: operational anchors (recovery procedures, validation checks, edge-case handling) are exactly what separates a skill that works in a demo from one that works in production. Their removal during naive rewriting widens the deployment gap.
