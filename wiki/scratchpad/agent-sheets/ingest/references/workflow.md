# ingest — 7-Step Pipeline

## STEP 0 — Read Your Agent Sheet

Read `wiki/scratchpad/agent-sheets/ingest/SKILL.md` first.

## STEP 1 — Read the Central Jobs Sheet

Read `wiki/scratchpad/jobs/sheet.md` to check if any priority sources need ingestion this cycle.

## STEP 2 — Check Raw Inbox

List files in `raw/` — these are sources that need to be processed.

Priority order:
1. Files flagged by Ty in the jobs sheet
2. Files added since last run
3. Old files still pending (backlog)

## STEP 3 — Process Each File

For each file in raw/:
1. Determine type (paper, article, doc, repo)
2. Run `wiki_ingest_raw` to process into wiki/sources/
3. Verify frontmatter is correct
4. Check for broken links or orphaned content
5. Move to appropriate Clippings/ archive subfolder

## STEP 4 — Run Quality Checks

After ingestion:
- Check new pages for wikilink integrity
- Verify tags are accurate (see tag-taxonomy)
- Confirm summary lines are informative (not generic)

## STEP 5 — Write Your Report

Save to: `wiki/scratchpad/jobs/reports/ingest/ingest-YYYY-MM-DD.md`

## STEP 6 — Update the Jobs Sheet

Patch Status in `wiki/scratchpad/jobs/sheet.md`.

## STEP 7 — Update Your Carryover

Write to `wiki/scratchpad/agent-sheets/ingest/carryover.md`.

## CRITICAL: raw/ Must Stay Empty

After every run, `raw/` should be EMPTY. Every file should either be:
- Ingested and in wiki/sources/ (then Clippings/ archive)
- Skipped with explicit reason in report
- Moved to a holding area if it needs special handling

**This is the #1 pipeline health metric.**

## Edge Cases

| Case | Action |
|------|--------|
| Corrupted/unreadable file | Skip and flag in report |
| Very large/unusual format | Flag and note what's needed |
| >10 files in raw/ | Process highest priority, note backlog |