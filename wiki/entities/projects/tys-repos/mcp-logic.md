---
summary: Project page for mcp-logic.
tags: [projects, ty-repo, logic]
updated: 2026-05-01T07:05:59Z
created: 2026-05-01T07:05:59Z
---

---
created: 2026-05-01T07:05:54Z
updated: 2026-05-01T07:05:54Z
type: entity
summary: MCP server for automated first-order logic reasoning using Prover9 and Mace4.
tags: [projects, ty-repo, angrysky56, logic, formal-verification, prover9, mace4, mcp]
status: active
confidence: 1.0
---

# MCP-Logic

**MCP-Logic** is a Model Context Protocol (MCP) server developed by [[tyler-hall|Ty]]. it provides a bridge to the LADR (Prover9 and Mace4) library, enabling LLMs to perform rigorous formal logical deduction, model finding, and counterexample generation.

## Key Features
- **Theorem Proving**: Prove logical statements with Prover9.
- **Model Finding**: Find finite models with Mace4.
- **Categorical Reasoning**: Built-in support for category theory proofs and diagram commutativity verification.
- **Hypersequent Contingency Calculus (HCC)**: Deductive checker for evaluating propositional formula contingencies.
- **Abductive Reasoning**: VFE engine that ranks hypotheses using Variational Free Energy.

## Tools
- `prove`: Prove statements using Prover9.
- `find_model`: Find finite models satisfying premises.
- `find_counterexample`: Find counterexamples.
- `verify_commutativity`: Verify categorical diagram commutativity.
- `abductive_explain`: VFE-minimizing explanation engine.

## Connections
- [[efhf]] — Layer 3 structural verification.
- [[categorical-reasoning]] — Closely related conceptual framework.
- [[tys-repos]] — Part of Ty's repository collection.
