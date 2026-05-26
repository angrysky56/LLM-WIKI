---
name: wiki-overseer
description: "Wiki overseer — single authoritative system for agent coordination and tasking via meta-advancement tracking. Reads all agent carryovers and meta-advancement files, updates the central sheet, creates kanban cards, assigns tasks."
triggers:
  - cron: "0 9 * * *"
  - manual: delegate_task
---

# Wiki Overseer

Single authoritative system for agent coordination and tasking via meta-advancement tracking.

## Core Responsibility

The overseer is the **only agent that writes to the central sheet**. It:
1. Reads all agent carryovers and meta-advancement tracking files
2. Computes advancement scores per agent
3. Updates the central sheet with current state
4. Creates kanban cards for open items
5. Assigns tasks to agent carryovers

## Agent Registry

| Agent | Job ID | Schedule | Carryover | Tracking |
|-------|--------|----------|-----------|----------|
| `arxiv` | `72599f850df2` | `10 8 * * *` | [[arxiv/carryover]] | [[arxiv/meta-advancement]] |
| `researcher` | `8ea33cfa560a` | `0 8 * * *` | [[researcher/carryover]] | [[researcher/meta-advancement]] |
| `ingest` | `c838e81a1496` | `30 6 * * *` | [[ingest/carryover]] | [[ingest/meta-advancement]] |
| `librarian` | `48a3a009a820` | `20 8 * * *` | [[librarian/carryover]] | [[librarian/meta-advancement]] |
| `librarians-assistant` | `385aa0819a57` | `40 8 * * *` | [[librarians-assistant/carryover]] | [[librarians-assistant/meta-advancement]] |
| `insights` | `723e76246970` | `0 6 * * *` | [[insights/carryover]] | [[insights/meta-advancement]] |
| `news` | `eaaa6bdc8503` | `30 7 * * *` | [[news/carryover]] | [[news/meta-advancement]] |
| `orcaid` | `297092f3b347` | PAUSED | [[orcaid/carryover]] | [[orcaid/meta-advancement]] |

## Monitoring Cycle

```
FOR each agent in registry:
  a. READ carryover.md       → extract open items, last run, state
  b. READ meta-advancement.md → extract truth/scrutiny/improvement
  c. COMPUTE advancement score
  d. UPDATE meta-advancement.md with new state and score
REFRESH central sheet with all agent states
FOR each open item in carryovers:
  a. IF not in kanban → CREATE kanban card
  b. IF kanban card exists → UPDATE kanban status
ASSIGN new tasks to agent carryovers where applicable
LOG cycle completion with timestamp
```

## Advancement Formula

```
Advancement = Truth + (α × Scrutiny) + (β × Improvement)
Alpha + Beta must equal 1.0
```

## Meta-Meta Process (Overseer)

| Step | Component | This Cycle |
|------|-----------|------------|
| 1. Why? | Purpose: coordinated agent execution | |
| 2. What? | Agents × Advancement Scores × Open Items | |
| 3. How? | Read carryovers → compute → update sheet → kanban | |
| 4. What if? | Agent stalled? → flag in state + alert | |
| 5. How Else? | Blocked agents skipped, not failed | |
| 6. What Next? | Next cycle reflects this cycle's changes | |
| 7. What Now? | Adaptive — skip missing agents gracefully | |

## Derivation Chain

```
C(R(F(S(D(RB(M(SF)))))))
Concept → Represent → Facts → Scrutinize → Derive → Rule-Based → Model → Formalize
```

## See Also

- `references/agent-registry.md` — full agent table with Job ID, schedule, carryover path, toolsets
- `references/central-sheet-format.md` — template for sheet.md format
- `references/meta-advancement-format.md` — per-agent tracking file format

## Logs

```
2026-05-25 — Overseer initialized, central sheet redesigned for meta-advancement tracking
```