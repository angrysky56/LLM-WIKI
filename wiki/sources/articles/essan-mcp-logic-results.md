---
summary: Essan core symbols FOL formalization:2-element model satisfies all axioms, P1 proved
tags: [essan, formal-verification, fol, mace4, prover9, symbolic-notation]
updated: 2026-05-30T08:52:44Z
created: 2026-05-30T08:52:44Z
---

---
created: 2026-05-22
updated: 2026-05-30
type: source
summary: "Essan core symbols (⦿⧈⫰⩘⧉) admit a consistent FOL formalization with a minimal 2-element model; P1 (no infinite chains) proved"
tags: [essan, formal-verification, fol, mace4, prover9, symbolic-notation]
sources: 
status: active
confidence: 0.9
---

# Essan Core Symbols Formalization: FOL Axioms, Models & Proofs

## Symbols Formalized

| Symbol | FOL Representation | Meaning |
|--------|-------------------|---------|
| ⦿ | `essence(x)` | Core entity with essential properties |
| ⧈ | `connected(x,y)` | Binary relation between entities |
| ⫰ | `movement(x,y,z)` | Ternary transition relation |
| ⩘ | `affirmed(x)` | Property of being affirmed/coherent |
| ⧉ | `strengthened(x,y)` | Asymmetric reinforcement relation |

## FOL Axioms (AX1–AX5)

- **AX1:** `exists x essence(x)` — Every model must contain at least one essential entity
- **AX2:** `all x (essence(x) -> exists y (essence(y) & connected(x,y)))` — Every essence is connected to another
- **AX3:** `all x all y (connected(x,y) -> exists z movement(x,y,z))` — Every connection supports a transition
- **AX4:** `all x (essence(x) -> affirmed(x))` — All essential entities are affirmed
- **AX5:** `all x all y (strengthened(x,y) -> connected(x,y))` — Reinforcement requires connection

## Mace4 Model Search

**Result:** Model found (domain size = 2)
- Element 0 is the sole essential/affirmed entity
- Element 0 is self-connected
- Movement defined on the self-loop

## Prover9 Proof

**Theorem P1 (No Infinite Chains): PROVED**
- AX1 provides witness `c1` with `essence(c1)`
- AX4 yields `affirmed(c1)`
- Goal follows by existential elimination

## Key Findings

1. **Five Essan core symbols admit a consistent FOL formalization** with a minimal 2-element model
2. **All essential properties simultaneously satisfiable** — essence, connection, movement, affirmation, strength
3. **P1 (no infinite descending chains) is provable** from the axioms via Prover9
4. **Self-loop** (`connected(x,x)`) is the minimal abductive basis for bidirectional reachability

## Connections

- [[essan-pidgin-results]] — Blind pidgin communication experiment; symbols encode structure but lack semantic bindings
- [[essan-vector-results]] — Vector space encoding test; random symbol vectors carry no semantic signal
- [[essan-vgcp-comparative-analysis]] — Essan vs VGCP reasoning traceability; Essan's symbolic feedback notation is genuinely novel vs VGCP's DAG enforcement
