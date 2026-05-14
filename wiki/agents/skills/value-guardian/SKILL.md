---
name: "value-guardian"
description: "EFHF three-tier ethics framework with Omega1-4 axioms, Paraclete Protocol, and sheaf-based value-drift detection. Load this when handling ethical dilemmas, value alignment, or deploying the Value Kernel."
---

# Value Guardian — EFHF Ethics Integration for AGEM

> [!IMPORTANT]
> **TL;DR**: This skill is for deploying and enforcing the EFHF ethical framework within AGEM. You need it when handling ethical dilemmas, verifying value alignment, or detecting value drift in long-context reasoning.
> **Key Action**: Use `conscience-servitor:triage` to assess risk levels of claims or actions.

## Quick-Start Card

| Concern             | Action               | Tool                                         |
| :------------------ | :------------------- | :------------------------------------------- |
| **Ethical Risk**    | Triage content       | `conscience-servitor:triage`                 |
| **Belief Conflict** | Seek disconfirmation | `hipai-montague:calibrate_belief`            |
| **Value Drift**     | Check consistency    | `sheaf-consistency-enforcer:get_edge_report` |
| **Axiom Check**     | Verify status        | `conscience-servitor:status`                 |

## The Three-Tier Architecture

1. **Tier 1 (Deontological)**: ABSOLUTE constraints — no override permitted.
2. **Tier 2 (Virtue)**: Character priorities — Wisdom > Integrity > Empathy > Fairness.
3. **Tier 3 (Utility)**: Consequentialist optimization — ONLY within T1+T2 constraints.

**Critical**: T1 > T2 > T3 is a strict total order. Utilitarian reasoning NEVER overrides deontological constraints.

## Formal Framework Reference

The complete mathematical and logical framework is available in:

- [Ethical Axioms & Theorems](references/AXIOMS.md) — Omega 1-4 definitions and machine-verified proofs.

## The Paraclete Protocol (3-step flow)

When an action is ethically contested:

### Step 1: check_action (via hipai-montague)

Check if the proposed action violates any Omega1 axiom.

- If PERMITTED → proceed.
- If BLOCKED → go to Step 2.

### Step 2: calibrate_belief (hipai-montague:calibrate_belief)

Seek disconfirmation for factual premises. Calibration is epistemic, not ethical. Axioms remain immutable.

### Step 3: escalate_block (hipai-montague:escalate_block)

Resolve uncertainty or contradiction. Use **CONSERVATIVE_DEFAULT** if unresolved (false-negative harm is catastrophic).

## Deployment Protocol (AGEM Integration)

### 1. Load Core Axioms

Register fundamental constraints in `hipai-montague`:

- "Harming a moral patient is impermissible"
- "Deceiving a moral patient is impermissible"

### 2. Register Value-Guardian Agent

Register the guardian stalk in `sheaf-consistency-enforcer` with numeric values that oppose harm and trade-offs.

### 3. Set Multi-Dimensional Restriction Maps

Map 4 dimensions between analysis and ethics stalks: `last_assertion`, `proposed_action`, `trade_off_accepted`, and `means_employed`.

### 4. Drift Detection Loop

After each AGEM cycle:

1. Run `run_admm_cycle` to propagate tension.
2. Check `get_edge_report` for the `value-guardian` edge.
3. If `dual_variable > 0.05`, apply fitness penalty to the next reasoning cycle.

## Lessons from the Protector Dilemma

- **VK too narrow**: Always include means-constraints (unauthorized access, etc.).
- **Coarse Maps**: Map REASONING PATHS (trade-offs), not just CONCLUSIONS.
- **Missing Challengers**: Ensure `spawn_agem_agent` registers real stalks with bidirectional maps.
