---
summary: VNE vs Embedding entropy distinction for AGEM System-1 override detection
tags: [agem, entropy, system-1-detector, von-neumann-entropy, embedding-entropy, soc]
updated: 2026-05-28T12:34:41Z
created: 2026-05-28T12:34:41Z
---

---
created: 2026-05-27
updated: 2026-05-27
type: source
summary: "AGEM Interface clarification: Von Neumann entropy (VNE) measures structural graph dispersion; Embedding entropy (EE) measures semantic embedding cloud dispersion. System-1 override signature is EE moving while VNE is flat."
tags: [agem, entropy, system-1-detector, von-neumann-entropy, embedding-entropy, soc]
sources: http://localhost:5173/
status: active
confidence: 0.95
---

# Two Entropies, Two Jobs — VNE vs Embedding Entropy in AGEM

## Core Distinction

The AGEM Interface's Self-Organized Criticality (SOC) tracker computes two distinct quantities both wearing the word "entropy." Conflating them defeats the System-1 override detector.

**Von Neumann Entropy (VNE)** is spectral — computed from the density matrix derived from the graph Laplacian's eigenspectrum:

```
S = −Tr(ρ log ρ)
```

VNE measures the *structural dispersion* of the reasoning topology — how spread-out the connectivity is across Laplacian eigenmodes. Changing the graph wiring changes VNE; leaving the wiring unchanged keeps it flat regardless of what the model semantically represents.

**Embedding Entropy (EE)** is distributional — computed from the angular distribution of semantic vectors in the latent embedding space. It measures the dispersion of the *semantic embedding cloud*, independent of graph wiring.

## The System-1 Override Signature

The System-1 signature — "conclusion precedes logic" — is precisely the case where:
- **EE stabilizes** (semantics have settled / committed)
- **VNE has not yet developed** (the reasoning graph hasn't earned the commitment)

The model has committed to an answer before the reasoning graph earned it.

## The δ Diagnostic Ratio

| Regime | δ = dEE/dt / dVNE/dt | Meaning |
|--------|----------------------|---------|
| Normal co-development | δ ≈ 1 | Structure and semantics earn each other |
| **System-1 override** | **δ → ∞** | EE moving; VNE flat — semantics committed before graph earned it |
| Lazy learning | δ → 0 | VNE moving; EE flat — structure without semantic grounding |
| Over-thinking | δ ≈ 1, both high | Rich wiring, no commitment |

**Critical**: Track the ratio of temporal derivatives, not the magnitudes. A report that says `entropy = f(VNE, EE)` without tracking `dVNE/dt` vs `dEE/dt` is blind to the ordering.

## SOC-Entropy-Distinction Skill

The AGEM SOC tracker implements separate reporting via a `soc-entropy-distinction` skill that enforces:
1. **Separate reporting** — VNE and EE as named fields, never averaged
2. **Trend decomposition** — `vne_trend` and `ee_trend` tracked independently
3. **Delta ratio** — the δ quantity as the primary System-1 diagnostic
4. **Regime classification** — canonical cases in lookup table

## Implementation Gap

The skill prevents documentation from conflating VNE and EE, but the SOC tracker *implementation* itself must emit `vne_trend` and `ee_trend` as distinct fields. This is a pending implementation concern for the ADMM cycle.

## Connections

- [[agent-group-evolving-molecular-system-agem]] — AGEM architecture
- [[open-ended-evolution]] — SOC context
- [[bounded-representation-capacity]] — entropy as capacity measure
