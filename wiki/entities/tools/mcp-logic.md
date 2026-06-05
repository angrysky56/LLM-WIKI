---
created: 2026-05-20
updated: 2026-05-20
type: entity
summary: First-order logic verification server — Prover9, Mace4, HCC for theorem proving, model finding, and abductive reasoning
tags: [logic, theorem-proving, mcp, verification]
sources: ['https://github.com/angrysky56/MCP-Logic']
status: active
confidence: 0.9
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
- [[sources/repositories/mcp-logic]]
- [[entities/projects/tys-repos/conscience-servitor]]
- [[entities/tools/mcp-logic]]
- [[entities/projects/tys-repos/advanced-reasoning-mcp]]
- [[synthesis/seg-scientist-agent-design]]
- [[concepts/mcp-model-context-protocol]]
- [[spikes/spike-campaign-001-004-summary]]
- [[entities/projects/efhf]]
- [[entities/projects/tys-repos/sheaf-consistency-enforcer]]
- [[entities/projects/tys-repos/efhf]]
- [[entities/people/tyler-hall]]
- [[sources/papers/bae-lmac-2026]]
- [[concepts/symbolic-regression]]
- [[wiki/index]]
- [[spikes/spike-001-spacy-owlready2]]
- [[sources/documentation/hermes-mcp-integration]]
- [[entities/tools/hipai-montague]]
- [[concepts/eml-operator]]
- [[sources/papers/odrzywolek-eml-2026]]
- [[entities/projects/tys-repos]]
- [[log]]
- [[sources/papers/vector-policy-optimization-vpo-2026]]
- [[entities/projects/meta-harness]]
- [[concepts/sheffer-stroke]]
- [[mcp-logic]]

- [[entities/projects/efhf]] — Layer 3 of the five-layer architecture
- [[hipai-montague]] — Layer 2; beliefs verified here
- [[mop-explorer]] — VERIFY action uses prove/find_counterexample
- [[concepts/maximum-occupancy-principle]] — absorbing state detection via find_model
- [[mop-edm-cognitive-architecture]] — formal verification backbone
- [[advanced-reasoning-mcp]]
- [[mcp-model-context-protocol]]
- [[symbolic-regression]]
- [[entities/projects/efhf]]
- [[spike-campaign-001-004-summary]]
- [[meta-harness]]
- [[eml-operator]]
- [[spike-001-spacy-owlready2]]
- [[conscience-servitor]]
- [[hipai-montague]]
- [[sheaf-consistency-enforcer]]
- [[odrzywolek-eml-2026]]
- [[tys-repos]]
- [[sheffer-stroke]]