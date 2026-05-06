---
summary: Entity page for Prover9.
tags: [logic, theorem-proving]
updated: 2026-05-06T20:09:43Z
created: 2026-05-06T20:09:43Z
---

---
created: 2026-05-06T20:09:39Z
updated: 2026-05-06T20:09:39Z
type: entity
summary: An automated theorem prover for first-order and equational logic. Successor to the OTTER prover.
tags: [logic, theorem-proving, formal-methods]
sources: https://www.cs.unm.edu/~mccune/prover9/
status: active
confidence: 1.0
---

# Prover9

Prover9 is an automated theorem prover (ATP) for first-order logic and equational logic. It is part of the LADR (Logic/Automated Deduction/Resolution) suite and is often used alongside **Mace4** (a model finder).

## Usage
- **Resolution**: Uses resolution and paramodulation to find proofs.
- **Isabelle Integration**: Often utilized as an external "Sledgehammer" prover in [[isabelle]] to automate proof discovery.

## CI Considerations
Legacy Makefiles for Prover9 may require specific linker flag ordering (e.g., placing `-lm` at the end) to avoid "undefined reference" errors in modern CI environments.

## Connections
- Entity: [[isabelle]]
- Source: [[github-actions-troubleshooting]]
- Concept: [[formal-verification]]
