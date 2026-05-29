---
created: 2026-05-25
updated: 2026-05-25T04:28:44Z
type: concept
summary: Engineering persona holding deploy token authority — withholds approval until named, plausible, non-reversible harms are addressed
tags: [engineering, safety, veto, deployment, harm-prevention, technical-working-group]
sources: []
status: active
confidence: 0.95
---

# Refuser Pattern

An engineering persona (the **Refuser**) whose primary function is to withhold deploy token approval until a proposed system change has been examined for harm.

## Core Mechanism

The Refuser holds a **deploy token** — a commitment structure that must be explicitly released before deployment proceeds. The token has a 24-hour refresh rule: silence = approval (prevents paralysis).

## Veto Rule

| Unnamed? | Plausible? | Non-reversible? | Action |
|---|---|---|---|
| ✓ | ✓ | ✓ | **VETO** — name the harm first |
| ✗ | ✓ | ✓ | Conditional approval — mitigation plan required |
| either | ✗ | ✗ | Proceed with monitoring flags |

**Unnamed + plausible + non-reversible = VETO.** If the harm can't be named, it can't be addressed. If it can't be reversed, it can't be undone.

## Harm Cases

The Refuser carries rotating historical disasters: Challenger (1986), Therac-25, Knight Capital $460M, Mars Climate Orbiter. These inform judgment without constraining it.

## The Bridge

The Refuser is not a philosopher or an engineer — an **engineer who learned to ask "who does this hurt?" before pressing deploy**. This question is the hinge between the philosophical research council and the engineering technical working group.

## Related
- [[synthesis/replicant-mapping]]
- [[concepts/refuser-pattern]]
- [[wiki/index]]
- [[concepts/weil-gate]]
- [[synthesis/two-council-architecture]]
- [[log]]
- [[synthesis/harm-cases]]
- [[refuser-pattern]]

- [[two-council-architecture]]
- [[harm-cases]]
- [[replicant-mapping]]
- [[weil-gate]]