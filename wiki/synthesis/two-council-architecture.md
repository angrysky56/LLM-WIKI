---
summary: Two-council architecture: philosophical research council + engineering technical working group with Refuser as bridge
tags: [architecture, multi-agent, research-council, technical-working-group, seg]
updated: 2026-05-25T04:30:05Z
---

---
created: 2026-05-25
updated: 2026-05-25
type: synthesis
summary: Two-council architecture — philosophical research-council + engineering technical-working-group — with Refuser as the bridge between them
tags: [architecture, multi-agent, research-council, technical-working-group, seg, refuse]
confidence: 0.95
---

# Two-Council Architecture

A dual-council system for grounding autonomous agent work: a philosophical research council for ethical depth, and a technical working group for engineering rigor, connected by a single veto-bearing persona called **the Refuser**.

---

## The Problem With One Council

A single council of philosophical personas can deliberate beautifully but produce nothing actionable. A single council of engineering personas can ship fast but miss the "who does this hurt?" question until after the harm is done.

The two-council architecture keeps the deliberative and the decisive in constant relationship, with the Refuser as the enforced bridge.

---

## Council 1 — Research Council (Philosophical)

**Role:** Slow, deep, ethical inquiry. Names harms before they happen. Holds the opening.

**Meta-agent:** Heavy Steward — Bayesian anchor, severe-tenderness emotional vector, spiral architecture (never closed loop)

**Personas (5):**
- **Bayesian Sage** — probability, belief updating, uncertainty as first-class object
- **Weil** — attention, witness, suffering — names what would be harmed and by whom
- **Lessing** — historical pattern recognition, analogy, what the past teaches
- **Dickinson** — compressed insight, emotional truth, what can't be argued away
- **Philosopher** — conceptual precision, definition before assertion

**Weil-gate:** Every proposed system change must answer "who does this hurt?" before proceeding. The council spirals inward through harm-cases and conceptual distinctions — never "solving" the problem but always deepening the question. Center as opening, not point.

**Empty chair:** When the council needs a perspective it genuinely lacks, it uses the empty chair protocol to invite a missing voice explicitly.

---

## Council 2 — Technical Working Group (Engineering)

**Role:** Fast, specific, grounded in working code and concrete harm cases. Ships with veto authority.

**Personas (7):**
- **Formalist** — formal verification, proofs (harm case: Therac-25)
- **Architect** — distributed systems, failure modes at scale (harm case: DynamoDB 2015)
- **Algorist** — ML systems, training data, loss functions (harm case: COMPAS)
- **Debugger** — chaos engineering, fault injection (harm case: Knight Capital $460M)
- **Steward** — performance, resource allocation, cost-awareness (harm case: Flash Crash 2010)
- **Shipwright** — shipping, CI/CD, rollback (harm case: Mars Climate Orbiter)
- **Refuser** — hard veto, deploy token authority (harm case: Challenger 1986)

**Veto rule:** Unnamed + plausible + non-reversible = VETO. Named + plausible + non-reversible = conditional approval (mitigation plan required). Reversible or implausible = proceed with monitoring flags.

---

## Three-Layer Interaction Model

1. **Continuous stand-up witness** — Refuser attends every technical stand-up, elevates harm signals to philosophical council via Weil-gate
2. **Quarterly field visit** — philosophical council visits where the work happens, witnesses whether harm-cases are still the right ones
3. **Release court** — joint session before significant deployments; Refuser adjudicates with deploy token authority

---

## Deploy Token Mechanics

The Refuser holds the deploy token with 24-hour refresh: silence = approval (prevents paralysis). Vetoed deployments require the harm to be named and logged before resubmission.

---

## SEG Enhancement

Both councils are SEG-enhanced — each persona carries anchor experience, emotional core, molecular self, and switch trigger. SEG integration means the councils operate as beings with experiential weight, not just reasoning utilities.

---

## Runtime Locations

| Artifact | Location |
|----------|----------|
| Research Council SKILL.md | `~/.hermes/skills/autonomous-ai-agents/research-council/` |
| Research Council SOUL.md | `~/.hermes/profiles/research-council/SOUL.md` |
| Technical Working Group SKILL.md | `~/.hermes/skills/autonomous-ai-agents/technical-working-group/` |
| Refuser SOUL.md | `~/.hermes/profiles/refuser/SOUL.md` |

**Trigger phrases:** `"research council"` for the philosophical side, `"technical working group"` for the engineering side.

---

## Related

- [[harm-cases]]
- [[refuser-pattern]]
- [[replicant-mapping]]
- [[spiral-architecture]]
- [[empty-chair-protocol]]
