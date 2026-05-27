---
name: wiki-overseer
description: "Wiki overseer — single authoritative system for agent coordination and tasking via meta-advancement tracking. Reads all agent carryovers and meta-advancement files, updates the central sheet, creates kanban cards, assigns tasks."
triggers:
  - cron: "0 9 * * *"
  - manual: delegate_task
updated: 2026-05-27
created_by: agent
---

# Wiki Overseer

Single authoritative system for agent coordination and tasking via meta-advancement tracking.

## Core Responsibility

The overseer is the **only agent that writes to the central sheet**. It:
1. Reads all agent carryovers and meta-advancement tracking files
2. Computes advancement scores per agent
3. Updates the central sheet with open items for kanban routing
4. Creates kanban triage cards for new open items
5. Logs cycle completion to `reports/overseer/`

## Tool Protocol

**Use `terminal()` with `cat` for all file reads in cron context.** `read_file` is not whitelisted for background/cron agent execution. Never call `read_file` directly.

```bash
# Correct (in terminal() calls):
cat /home/ty/Documents/LLM-WIKI/wiki/scratchpad/jobs/sheet.md
cat /home/ty/Documents/LLM-WIKI/wiki/scratchpad/agent-sheets/{agent}/carryover.md

# Wrong — will fail in cron:
read_file(path="...")
```

## Agent Registry

|| Agent | Job ID | Schedule | Carryover | Notes ||
|-------|--------|----------|-----------|--------||
|| `arxiv` | `72599f850df2` | `10 8 * * *` | [[arxiv/carryover]] | ||
|| `researcher` | `8ea33cfa560a` | `0 8 * * *` | [[researcher/carryover]] | ||
|| `ingest` | `c838e81a1496` | `30 6 * * *` | [[ingest/carryover]] | ||
|| `librarian` | `48a3a009a820` | `20 8 * * *` | [[librarian/carryover]] | ||
|| `librarians-assistant` | `385aa0819a57` | `40 8 * * *` | [[librarians-assistant/carryover]] | ||
|| `insights` | `723e76246970` | `0 6 * * *` | [[insights/carryover]] | ||
|| `news` | `eaaa6bdc8503` | `30 7 * * *` | [[news/carryover]] | ||
|| `orcaid` | `297092f3b347` | PAUSED | [[orcaid/carryover]] | ||

## Overseer Own Files

|| File | Path | Purpose ||
|------|------|--------||
| Carryover | `overseer/carryover.md` | Overseer's own open items, state, last run ||
| Meta-Advancement Framework | `overseer/meta-advancement/SKILL.md` | Advancement formula and tracking structure ||
| References | `overseer/references/Meta-Meta Process for Structured Exploration.md` | Conceptual grounding for meta-meta process ||

## Monitoring Cycle

```
# Overseer's own carryover
terminal(cat overseer/carryover.md) → update own state and advancement score

FOR each agent in registry:
  a. terminal(cat {agent}/carryover.md) → extract open items, last run, state
  b. COMPUTE advancement score from carryover state
  c. UPDATE {agent}/carryover.md with new state and score
UPDATE overseer/carryover.md with own state and advancement score
REFRESH central sheet with open items from carryovers

FOR each open item in carryovers:
  a. CHECK if item already has a kanban ID in sheet.md
  b. IF no kanban ID → CREATE kanban card using terminal(hermes kanban create):
     hermes kanban create "<title>" --triage --priority P<1|2|5> --body "<description>"
  c. The triage system handles decomposition and routing automatically
LOG cycle completion to reports/overseer/overseer-YYYY-MM-DD.md
```

## Creating Triage Cards

When an open item is found in an agent's carryover, the overseer must:

1. **Check the agent's reports folder** (`reports/{agent}/`) for relevant context on the open item
2. **Read the detailed findings** to understand the full problem space
3. **Write a complete triage card** with full context — not just the carryover snippet

```bash
# Step 1: List agent reports for relevant files
ls /home/ty/Documents/LLM-WIKI/wiki/scratchpad/jobs/reports/{agent}/

# Step 2: Read relevant report(s) for context
cat /home/ty/Documents/LLM-WIKI/wiki/scratchpad/jobs/reports/{agent}/<relevant-report.md>

# Step 3: Write triage card with full context via terminal(hermes kanban create)
hermes kanban create "<specific title>" --triage --priority P<1|2|5> --body "<full description from reports + what needs to be decided>"
```

**Example triage formulation:**

```
Carryover snippet: "NAMM upgrade — needs Ty decision"
Report context: "NAMM adds KV cache retention vs Control LLM — complementary? Dettmers et al. 2023"

→ Triage card body: "NAMM (Neural Additive Memory Module) adds learned KV cache retention 
as an inductive bias. Control LLM uses separate routing. The question is whether these 
are complementary or redundant. Dettmers et al. 2023 is the primary source. 
Decision needed: should NAMM and Control LLM be separate wiki pages, merged, or 
one as a subsection of the other? Researcher agent owns this."
```

**Priority mapping:** high=P1, med=P2, low=P5 (hermes uses P1-P5, higher = more urgent).

**Only create ONE card per open item.** If the item already has a Kanban ID in sheet.md (format: `t_<hex>`), skip it — it's already tracked.

## Kanban Card Pattern (Actionable via Triage)

**Wiki-agent open items are actionable tasks routed through the triage system.** Create cards with `status=triage` — the triage skill handles decomposition, state transitions, and routing to the appropriate agent or human. Do NOT set `status=done`; informational done-cards were a mistake.

For items needing Ty input: set `status=blocked` and note what input is needed in the card body.

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

The central sheet is at `wiki/scratchpad/jobs/sheet.md`. Per-agent carryovers are at `wiki/scratchpad/agent-sheets/{agent}/carryover.md`.

## Logs

```
2026-05-25 — Overseer initialized, central sheet redesigned for meta-advancement tracking
2026-05-27 — Tool protocol: replaced read_file with terminal() cat calls (cron compatibility)
```