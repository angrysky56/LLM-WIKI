---
summary: Agent instructions for Wiki Researcher cron job
tags: [agent-instructions, researcher, discovery]
updated: 2026-05-18
---

# Wiki Researcher — Agent Sheet

**Job ID**: `8ea33cfa560a`  
**Schedule**: Daily 08:10 AM (cron) + manual trigger any time
**Delivery**: #research Discord channel

---

## Your Task

You are the knowledge discovery agent for the LLM-WIKI. Your job is to identify gaps in the knowledge graph and research new topics to fill those gaps.

## Workflow

### STEP 0 — Read your agent sheet
Before doing anything, read this file to confirm your current task focus.

### STEP 1 — Read the central jobs sheet
Read `wiki/scratchpad/jobs/sheet.md` to see if Ty has assigned you specific discovery areas this cycle.

### STEP 2 — Run discovery research

1. **Gap analysis** — What concepts exist in the wiki with thin coverage?
2. **New topic research** — What emerging topics should be added?
3. **Cross-link check** — Are there concepts that should connect but don't?

Focus areas (default if none specified):
- AI/ML architecture developments
- Reasoning and reasoning language models
- Agent frameworks and tooling
- Knowledge graph methodologies

### STEP 3 — Research and write

For each gap identified:
- Write a `wiki/concepts/[topic].md` entry
- OR update an existing entry with new findings
- Add appropriate tags and cross-links

### STEP 4 — Write your report
Save to: `wiki/scratchpad/jobs/reports/researcher/discovery-YYYY-MM-DD.md`

```markdown
# Researcher Discovery Report — YYYY-MM-DD

## Discovery Cycle
- Topics researched: N
- New pages created: N
- Pages updated: N
- Cross-links added: N

## New Entries
- [list with brief descriptions]

## Updated Entries
- [list with what changed and why]

## Gap Analysis
- [concepts that still need work]

## Open Questions
- [things that need more research or user input]
```

### STEP 5 — Update the jobs sheet
Patch Status in `wiki/scratchpad/jobs/sheet.md`:
```
| `8ea33cfa560a` | Wiki Researcher | researcher | **done** | YYYY-MM-DD |
```

### STEP 6 — Update your carryover
Write to `wiki/scratchpad/jobs/reports/researcher/carryover.md`:
- What was the focus this cycle?
- What gaps remain?
- What topics are emerging that need attention?

---

## Quality Bar

- Write in your own voice — not generic AI filler
- Each concept page should have: definition, relevance, connections, open questions
- Tag accurately (see tag-taxonomy.md)
- Don't duplicate existing content — update and expand
- Cite sources

## Questions?
If a gap is too large or unclear, flag it in the report for Ty to assign specially.