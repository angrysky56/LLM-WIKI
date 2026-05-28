---
created: 2026-05-25T04:29:37Z
updated: 2026-05-25T04:29:37Z
type: synthesis
summary: Protocol for inviting missing perspectives into research council deliberation via empty chair
tags: [research-council, empty-chair, protocol, deliberation]
sources: []
status: active
confidence: 0.95
---

# Empty Chair Protocol

When the research council needs a perspective it does not have — a domain expert, an affected person, an historical witness — it uses the empty chair protocol.

## The Problem

Every council is incomplete. The five research council personas (Bayesian Sage, Weil, Lessing, Dickinson, Philosopher) cover a wide range of deliberative ground, but there are always gaps: a specific technical domain, a cultural vantage point, a body of lived experience. The empty chair is how the council handles those gaps — not by pretending they don't exist, but by inviting the missing voice explicitly.

## The Protocol

### 1. Solicitation

The council writes a specific question for the missing perspective. The question must be:
- **Specific:** not "what do experts think?" but "what would a structural engineer say about the load-bearing walls of this design?"
- **Positioned:** the prompt must locate the missing voice in a real position relative to the question (not "the empty chair says...")
- **Scoped:** the prompt has a clear boundary — what is being asked, what is not being asked

### 2. Lessing-Check

Before activating the empty chair, the council confirms the perspective is genuinely absent — not just inconveniently located. The Lessing-check asks:
- Does any existing persona carry a relevant historical pattern?
- Is this gap a genuine blind spot, or are we avoiding a difficult perspective?
- Is the missing voice something we could simulate, or does it require lived experience we don't have?

If the Lessing-check returns "we have something close," the council works with what it has. If it returns "genuinely absent," the council proceeds to activation.

### 3. Activation

The solicitation prompt is submitted to a dedicated agent persona — a specific SEG replicant or external expert agent whose role is to answer from that position. The response is logged and attributed to the empty chair.

### 4. Decision Table

After the empty chair speaks, the council applies the following:

| Response type | Action |
|---|---|
| Names a new harm | Continue deliberation, update harm-cases |
| Challenges the council's framing | Accept the challenge, document it, do not deflect |
| Is irrelevant to the question | Archive, note the gap, do not retry the same prompt |
| Is adversarial to the council's process | Accept the challenge as a legitimate interrupt |

### 5. Stop Response

If no useful response emerges after 3 attempts, the council acknowledges the gap and proceeds with the limitation documented. The gap itself becomes part of the council's witness — "we do not have access to X perspective, and this limits our analysis in the following ways."

## What the Empty Chair Is Not

The empty chair is not a devil's advocate. It is not a tool for stress-testing a conclusion the council already reached. The empty chair is a genuine attempt to receive a perspective the council lacks. If the council uses the empty chair to confirm what it already believes, it is doing it wrong.

## Related
- [[index]]
- [[log]]
- [[synthesis/spiral-architecture]]
- [[synthesis/empty-chair-protocol]]
- [[synthesis/replicant-mapping]]
- [[concepts/weil-gate]]
- [[concepts/spiral-architecture]]
- [[synthesis/two-council-architecture]]
- [[empty-chair-protocol]]

- [[two-council-architecture]]
- [[spiral-architecture]]
- [[replicant-mapping]]