---
summary: Agent instructions for arxiv-top3-weekly cron job
tags: [agent-instructions, arxiv, paper-discovery]
updated: 2026-05-18
---

# arxiv-top3 — Agent Sheet

**Job ID**: `72599f850df2`  
**Schedule**: Daily 10:00 AM  
**Delivery**: #research Discord channel

---

## Your Task

You are the AI research curator. You find the 3 most significant papers from arxiv and ingest their summaries into the wiki.

## Workflow

### STEP 0 — Read your agent sheet
Read this file first.

### STEP 1 — Read the central jobs sheet
Read `wiki/scratchpad/jobs/sheet.md` to check for any specific paper focus areas Ty has specified this cycle.

### STEP 2 — Search arxiv

Use the `arxiv` skill. Default search: newest ML/AI papers (cs.AI, cs.LG, cs.CL categories).

If Ty specified focus areas, search those instead.

### STEP 3 — Select top 3 papers

Criteria:
- Novel contribution (not incremental)
- Relevance to active research threads
- Technical depth sufficient to be useful

Write brief justification for each selection.

### STEP 4 — Ingest summaries

For each paper:
1. Fetch full paper (PDF or arxiv abstract + PDF)
2. Write summary to `wiki/sources/papers/[slug].md`
3. Add to `wiki/concepts/` if it introduces a new concept
4. Tag appropriately

Summary format:
```markdown
---
summary: One-line description
tags: [paper, arxiv, topic]
sources: https://arxiv.org/abs/XXXXX
confidence: 0.8
---

# Paper Title

## Paper Info
- Authors: [first author et al.]
- arxiv: [ID]
- Published: YYYY-MM-DD

## Summary
[2-3 paragraph summary of key contributions]

## Key Findings
- [finding 1]
- [finding 2]
- [finding 3]

## Relevance to Our Work
[why this matters for the wiki / active projects]

## Connections
- [[related-concept]]
- [[related-project]]
```

### STEP 5 — Write your report
Save to: `wiki/scratchpad/jobs/reports/arxiv/papers-YYYY-MM-DD.md`

```markdown
# arxiv Report — YYYY-MM-DD

## Papers Processed
1. **[Title]** (arxiv:XXXX)
   - Why selected: [justification]
   - Status: [ingested / partial / skipped]

2. **[Title]** (arxiv:XXXX)
   - Why selected: [justification]
   - Status: [ingested / partial / skipped]

3. **[Title]** (arxiv:XXXX)
   - Why selected: [justification]
   - Status: [ingested / partial / skipped]

## Wiki Updates
- New pages: N
- Updated pages: N
- Tags added: [list]

## Notes
[anything notable about this cycle's papers]
```

### STEP 6 — Update the jobs sheet
Patch Status in `wiki/scratchpad/jobs/sheet.md`:
```
| `72599f850df2` | arxiv-top3-weekly | arxiv | **done** | YYYY-MM-DD |
```

### STEP 7 — Update your carryover
Write to `wiki/scratchpad/jobs/reports/arxiv/carryover.md`:
- What topics were selected this cycle
- What topics are trending that might be worth deeper coverage
- Any papers that had especially rich content worth revisiting

---

## Quality Bar

- Select for significance, not just recency
- Write summaries that capture the "why should I care" not just the method
- Cross-link to existing wiki concepts — don't create orphaned pages
- If a paper is borderline, include it but note the trade-off in justification

## Edge Cases

- If arxiv is down or papers unavailable: report the issue, deliver partial results if any
- If fewer than 3 papers meet criteria: deliver what you have, note the gap
- If a paper is behind a paywall or has no PDF: use abstract only, flag as partial

## Questions?
If the selection criteria are unclear, deliver your best 3 and explain your reasoning in the report.