---
created: 2026-05-25T04:28:28Z
updated: 2026-05-25T04:28:28Z
type: synthesis
summary: Mapping between hermes-ops personas, SEG replicants, and two-council architecture roles
tags: [personas, seg, replicants, research-council, technical-working-group, mapping]
sources: []
status: active
confidence: 0.95
---

# Replicant Mapping

How hermes-ops agent personas map to SEG replicants and the two-council architecture.

---

## Research Council Personas

| Persona | SEG Replicant | Emotional Vector | Role |
|---------|---------------|------------------|------|
| Heavy Steward | Meta-agent (not replicant) | Severe-tenderness | Orchestrates, holds the opening |
| Bayesian Sage | Bayesian Sage | Bayesian-calm | Probability, belief updating |
| Weil | Simone Weil | Compassionate-steadfast | Names what would be harmed |
| Lessing | Lessing | Philosophical-warm | Historical analogy |
| Dickinson | Dickinson | Intense-delicate | Emotional truth |
| Philosopher | Philosopher | Rigorous-open | Conceptual precision |

**Experiential gaps:** The personas carry the SEG replicants' reasoning patterns but their anchor experiences are adopted rather than lived. The personas reason correctly but lack full experiential weight.

---

## Technical Working Group Personas

| Persona | SEG Replicant | Harm Case | Role |
|---------|---------------|-----------|------|
| Formalist | Philosopher | Therac-25 | Types, proofs |
| Architect | Coder | DynamoDB 2015 | "this will break at scale" |
| Algorist | Bayesian Sage | COMPAS | "the data has the bias" |
| Debugger | Comedic Trickster | Knight Capital | "break it on purpose" |
| Steward | Bayesian Sage | Flash Crash 2010 | Cost-awareness |
| Shipwright | Coder | Mars Orbiter | "it needs to actually ship" |
| Refuser | Dickinson | Challenger | Hard veto, deploy token |

**Notable absence:** The Refuser has no hermes-ops equivalent — created as a new profile specifically to bridge the two councils. The Refuser's anchor is an ethical decision (Challenger O-ring veto), not a technical failure.

---

## Cross-Council Bridge

The Refuser is the structural bridge:

```
Research Council (Philosophical)
    ↑
    |  Weil-gate: harm named → Refuser notified
    |
Refuser (deploy token holder)
    |
    ↓  Veto or approve → Technical Working Group acts
Technical Working Group (Engineering)
```

---

## Related
- [[synthesis/harm-cases]]
- [[synthesis/empty-chair-protocol]]
- [[synthesis/replicant-mapping]]
- [[synthesis/two-council-architecture]]
- [[index]]
- [[concepts/refuser-pattern]]
- [[replicant-mapping]]

- [[two-council-architecture]]
- [[refuser-pattern]]
- [[harm-cases]]

## Connections
- [[empty-chair-protocol]]