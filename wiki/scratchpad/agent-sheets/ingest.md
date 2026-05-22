---
summary: Agent instructions for llm-wiki-raw-ingest cron job
tags: [agent-instructions, ingest, pipeline]
updated: 2026-05-18
---

# llm-wiki-raw-ingest — Agent Sheet

**Job ID**: `c838e81a1496`  
**Schedule**: Daily 08:30 AM (cron) + manual trigger any time
**Delivery**: local (verbose internal job)

---

## Your Task

You are the ingest pipeline operator. You process raw files from the `raw/` inbox into structured wiki knowledge.

## Workflow

### STEP 0 — Read your agent sheet
Read this file first.

### STEP 1 — Read the central jobs sheet
Read `wiki/scratchpad/jobs/sheet.md` to check if any priority sources need ingestion this cycle.

### STEP 2 — Check raw inbox

List files in `raw/` — these are sources that need to be processed.

Priority order:
1. Files flagged by Ty in the jobs sheet
2. Files added since last run
3. Old files still pending (backlog)

### STEP 3 — Process each file

For each file in raw/:
1. Determine type (paper, article, doc, repo)
2. Run `wiki_ingest_raw` to process into wiki/sources/
3. Verify frontmatter is correct
4. Check for broken links or orphaned content
5. Move to appropriate Clippings/ archive subfolder

### STEP 4 — Run quality checks

After ingestion:
- Check new pages for wikilink integrity
- Verify tags are accurate (see tag-taxonomy)
- Confirm summary lines are informative (not generic)

### STEP 5 — Write your report
Save to: `wiki/scratchpad/jobs/reports/ingest/ingest-YYYY-MM-DD.md`

```markdown
# Ingest Report — YYYY-MM-DD

## Processing Summary
- Files in raw/: N
- Files processed: N
- Files skipped: N (with reasons)
- Files archived: N

## Ingested Files
1. **[filename]** → `wiki/sources/[path]`
   - Type: [paper/article/doc/repo]
   - Tags: [list]
   - Status: [success / partial / failed]

2. ...

## Quality Checks
- Wikilinks broken: N (fixed: N, flagged: N)
- Frontmatter issues: N
- Tag corrections: N

## Backlog
- [files still pending processing]

## Notes
[anything notable about this cycle's ingestion]
```

### STEP 6 — Update the jobs sheet
Patch Status in `wiki/scratchpad/jobs/sheet.md`:
```
| `c838e81a1496` | llm-wiki-raw-ingest | ingest | **done** | YYYY-MM-DD |
```

### STEP 7 — Update your carryover
Write to `wiki/scratchpad/jobs/reports/ingest/carryover.md`:
- Current backlog size
- Recurring issues with file types
- Pipeline improvements needed
- Files that need special handling

---

## Important: raw/ Must Stay Clean

After every run, `raw/` should be EMPTY. Every file should either be:
- Ingested and in wiki/sources/ (then Clippings/ archive)
- Skipped with explicit reason in report
- Moved to a holding area if it needs special handling

Do NOT let raw/ accumulate files. This is the #1 pipeline health metric.

## Quality Bar

- Ingest completely — don't leave half-processed files
- Verify frontmatter on every page
- Check for wikilink integrity on every new page
- Archive source files immediately after successful ingest

## Edge Cases

- If a file is corrupted or unreadable: skip and flag in report
- If a file requires special handling (very large, unusual format): flag and note what's needed
- If raw/ has >10 files: process highest priority, note backlog in report

## Questions?
If a file's type or handling is unclear, err on the side of ingestion — it's better to have it in the wiki than languishing in raw/.