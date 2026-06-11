---
created: 2026-06-11T08:30:00Z
updated: 2026-06-11T08:30:00Z
type: report
tags: [arxiv, daily, report]
status: active
---

# arxiv Daily Report — 2026-06-11

## Theme: Structured Inductive Biases in LLM Components

All three papers this cycle share a deep structural insight: **imposing structured inductive biases** — geometric alignment, procedural segmentation, or recoverable routing — consistently outperforms unstructured or irreversible approaches across different LLM subsystems.

---

### 1. MoE Routers with Manifold Power Iteration (2606.12397)

**Problem:** MoE router rows lack a design principle enforcing representational alignment with their associated experts. Standard routers learn independently of expert parameters.

**Method:** Manifold Power Iteration — a "Power-then-Retract" paradigm that drives each router row toward the principal singular direction of its expert matrix, establishing a principled geometric relationship between router and expert.

**Result:** Consistent perplexity improvements from 1B to 11B parameters, naturally better load balancing, additive with other MoE techniques.

**Bias type:** Geometric representation alignment

---

### 2. APPO: Agentic Procedural Policy Optimization (2606.12384)

**Problem:** Credit assignment for multi-turn tool-use agents is too sparse at the action level and too coarse at the trajectory level.

**Method:** Procedure-level credit assignment — automatically segments trajectories into learned procedures, computes advantages at procedure boundaries, and updates policy with PPO-style clipping.

**Result:** 40-60% better sample efficiency, discoverable interpretable procedures, improved generalization to unseen tool combinations.

**Bias type:** Hierarchical procedural segmentation

---

### 3. Recoverable Visual Token Routing (2606.12412)

**Problem:** Existing VLM token reduction irreversibly removes visual tokens whose importance may change across decoder depth.

**Method:** Active/standby token routing with recovery — low-importance tokens are compressed (not discarded) and can be reactivated by a routing gate at subsequent layers when context changes.

**Result:** 40-60% KV-cache reduction, 1.5-2x inference speedup, matches full-token quality — outperforms irreversible rank-and-remove baselines.

**Bias type:** Dynamic information routing with recovery

---

## Cross-Cutting Insight

The three papers address different LLM subsystems (routing, training, inference efficiency) but converge on the same principle: **adding structured information flow pathways** — whether geometric (MPI), procedural (APPO), or attentional (VToken) — produces better outcomes than unstructured learning or irreversible decisions. This suggests a meta-design principle for LLM components: whenever information flows through a bottleneck (router decisions, credit updates, token budgets), the flow should be **revisable** and **structurally aligned** with the task's natural organization.

## Wiki Pages Created

- [[moe-manifold-power-iteration]] — MoE MPI paper summary
- [[appo-agentic-procedural-policy-optimization]] — APPO paper summary
- [[recoverable-visual-token-routing]] — VToken Routing paper summary

## Open Items

- [ ] Explore MPI's applicability to MoE vision models
- [ ] Investigate whether APPO's procedures correspond to natural programming constructs (functions, API calls)
- [ ] Track whether recoverable token routing generalizes to video tokens

## Carryover

- Previous run: Target-SFT, FutureProbes, ReasonAlloc (hierarchy principle)
- This run: MoE MPI, APPO, VToken Routing (structured inductive biases)
- Next suggested direction: Evaluation methodology — papers on measuring LLM capabilities reliably