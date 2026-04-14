---
summary: First-order logic MCP server (Prover9/Mace4) — EFHF Layer 3; structural verification, absorbing state detection, hypothesis validation for MOP agents
tags: [MCP, EFHF, logic, Prover9, Mace4, verification, FOL, absorbing-states]
updated: 2026-04-14T04:17:05Z
created: 2026-04-14T04:17:05Z
---

# mcp-logic

**Type:** Tool — MCP server
**Repository:** [MCP-Logic](https://github.com/angrysky56/MCP-Logic)
**EFHF Layer:** 3 — Structural verification
**Backend:** Prover9 (theorem proving), Mace4 (model finding), HCC (propositional logic)

---

## What It Does

First-order logic verification server. Proves theorems, finds counterexamples, checks consistency, performs abductive reasoning, and verifies category-theoretic diagram commutativity.

Key tools: `prove`, `find_counterexample`, `find_model`, `abductive_explain`, `check_well_formed`, `verify_commutativity`, `get_category_axioms`

## Role in EFHF

Layer 3 — checks whether the macro-level world model (Layer 2, [[hipai-montague]]) commutes with micro-level evidence. This is the lumpability check: does the coarse-grained description preserve the Markov property?

## Role in MOP Architecture

**Absorbing state detection:** `find_model(premises)` — if no model exists for the agent's current beliefs, they are inconsistent → absorbing state (Kernel 2 transition). The reasoning chain must be terminated or rolled back.

**Hypothesis validation (β-filter):** `find_counterexample(premises, conclusion)` — when the MOP agent proposes a novel connection (high Δ), check for counterexamples before committing.

**Abductive reasoning:** `abductive_explain(observation, candidates)` — find the VFE-minimizing explanation for surprising observations. Bridges MOP's exploration drive with formal grounding.

## Verified Results

- AbsorbingState(x) → Kernel2Transition(x) — proved in 0.00s
- SubjectiveIntegration(x) → Kernel1(x) ∧ ComputationalClosure(x) ∧ CausalClosure(x) — proved
- SubjectiveIntegration(x) ∧ CoherenceTimeout(x) → ⊥ — proved (logically incompatible)

## Connections

- [[efhf]] — Layer 3 of the five-layer architecture
- [[hipai-montague]] — Layer 2; beliefs verified here
- [[mop-explorer]] — VERIFY action uses prove/find_counterexample
- [[maximum-occupancy-principle]] — absorbing state detection via find_model
- [[mop-edm-cognitive-architecture]] — formal verification backbone
