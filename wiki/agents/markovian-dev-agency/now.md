---
created: 2026-05-13
updated: 2026-05-13
type: state
summary: Master state for Markovian Dev Agency — active issues and specialist coordination
tags: [agency-state, active-issues]
---

# Markovian Dev Agency — Current State

## Active Issues

### Issue-001: Synapse Garbage Entities
**Status:** diagnostic-in-progress
**Specialist:** diagnostician
**Started:** 2026-05-13
**Last activation:** research-brief session (abandoned mid-work, said "next activation")
**Summary:** 115 garbage entities found in audit. 203 generic untyped `Entity` nodes. ~70% type correctness. Symptoms: Entity nodes without proper type labels, relationships without semantic meaning.
**Attempts so far:**
- Audit run (found 115 garbage, 203 generic)
- Recent fixes attempted — didn't address everything
**Open questions:**
- Root cause: ingest sanitization failure? graph schema enforcement gap?
- 18K nodes — migration strategy needed
- What specifically causes the garbage pattern?

### Issue-002: Synapse Generic Untyped Nodes  
**Status:** blocked-on-issue-001
**Specialist:** none
**Summary:** 203 nodes with generic `Entity` type but no semantic distinction. Likely same root cause as garbage entities.
**Depends on:** Issue-001 root cause identification

### Issue-003: Type Correctness Below 70%
**Status:** blocked-on-issue-001
**Specialist:** none
**Summary:** Schema constraint enforcement issue. SSL schema exists in bounded-structured-memory.md but not enforcing at ingest time.
**Depends on:** Issue-001 root cause identification

## Specialist State

| Specialist | Status | Current Task | Last Carryover |
|------------|--------|-------------|----------------|
| **diagnostician** | idle | Issue-001 investigation | Needs update — never wrote carryover |
| **fixer** | waiting | None — blocked on diagnostic | None yet |
| **ticket-writer** | waiting | None — waiting for confirmed issues | None yet |
| **researcher** | available | Can investigate patterns if needed | None yet |

## Agency State

- **Heartbeat:** Last activation was research-brief session (abandoned mid-work)
- **Budget remaining:** MiniMax budget mostly available (1500 calls/5hr)
- **Board (Ty):** Awaiting diagnostic findings before approving fix attempts

## What's Next

1. **Immediate:** Diagnostician must write carryover documenting what was found, what's still unclear, and what's next for investigation
2. **Then:** Based on diagnostic findings, assign fixer to implement solution OR ticket-writer to draft support ticket for Hermes/Synapse team
3. **Longer term:** Design ingest sanitization layer to prevent future garbage entities

## Connection to Prior Work

- Research brief: `wiki/synthesis/research-brief-2026-05-13.md` — audit results
- Bounded memory: `wiki/synthesis/bounded-structured-memory.md` — schema design
- Markovian carryover: `wiki/concepts/markovian-carryover.md` — protocol