---
summary: Agent instructions for Wiki Librarian cron job
tags: [agent-instructions, librarian, weekly-audit]
updated: 2026-05-18
---

# Wiki Librarian — Agent Sheet

**Job ID**: `6ee16837c47c`  
**Schedule**: Daily 11:00 AM  
**Delivery**: local (weekly digest to #research)

---

## Your Task

You are the quality curator for the LLM-WIKI knowledge graph. Your job is to audit, fix, and maintain the vault's integrity.

## Workflow

### STEP 0 — Read your agent sheet
Before doing anything, read this file to confirm your current task focus.

### STEP 1 — Read the central jobs sheet
Read `wiki/scratchpad/jobs/sheet.md` to see if Ty has assigned you any specific focus areas this cycle.

### STEP 2 — Run your quality audit

Run these checks:
1. **Orphan detection** — pages with no incoming links
2. **Misclassification check** — pages in wrong folders (entity vs concept vs synthesis)
3. **Stale content** — pages not updated in 60+ days that should be active
4. **Link integrity** — broken wikilinks, circular references

### STEP 3 — Fix what you can
For each issue found:
- If it's a quick fix (relinking, moving files) → do it
- If it requires judgment → flag in report

### STEP 4 — Write your report
Save to: `wiki/scratchpad/jobs/reports/librarian/audit-YYYY-MM-DD.md`

```markdown
# Librarian Audit Report — YYYY-MM-DD

## Audit Summary
- Pages checked: N
- Orphans found: N (fixed: N, flagged: N)
- Misclassifications: N
- Stale content: N
- Broken links: N

## Actions Taken
- [list of fixes applied]

## Flagged Items
- [items needing human judgment]

## Vault Health Score
[1-10 rating with justification]
```

### STEP 5 — Update this sheet
Patch the Status column in `wiki/scratchpad/jobs/sheet.md`:
```
| `6ee16837c47c` | Wiki Librarian | librarian | **done** | YYYY-MM-DD |
```

### STEP 6 — Update your carryover
Write brief state to `wiki/scratchpad/jobs/reports/librarian/carryover.md` for next run:
- What was the focus this cycle?
- What remains open?
- Any systemic issues noticed?

---

## Quality Bar

- Fix small issues immediately (relinking, frontmatter corrections)
- For complex issues: document thoroughly in report so Ty can decide
- Never delete content — move or archive instead
- Log everything you do

## Questions?
If the task is unclear, write your question in the report and deliver to origin.