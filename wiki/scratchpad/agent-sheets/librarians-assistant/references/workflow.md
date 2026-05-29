# librarians-assistant — 6-Step Fix Workflow

## STEP 1 — Read Librarian Carryover

Read: `wiki/scratchpad/agent-sheets/librarian/carryover.md`
This tells you what the librarian found and what's open. The carryover's "What Remains" section is your task list — work through it in the priority order specified there.

## STEP 2 — Read Batch Progress

Read: `wiki/scratchpad/jobs/reports/librarian/batch-progress.md` (if it exists)
知道你已经做到哪里了. Start where the last run stopped — don't redo work already done.

## STEP 3 — Run Fixes

Read the carryover's open items. Execute them in priority order. Stop at 50+ fixes or when you hit a hard blocker (needs judgment or content creation beyond scope).

## Fix Priority Order

1. **Broken wikilink aliases** → create stub pages at target path
2. **Orphan pages** → connect to cluster via `wiki_search`
3. **Non-reciprocal links** → add reverse wikilinks
4. **Frontmatter completions** → add summary/tags/status
5. **Tag normalization** → standardize per taxonomy

## STEP 4 — Update Batch-Progress

After every 15-20 fixes, write a progress note to:
`wiki/scratchpad/jobs/reports/librarian/batch-progress.md`

## STEP 5 — Update Assistant Carryover

Write state to: `wiki/scratchpad/agent-sheets/librarians-assistant/carryover.md`

## Related
- [[wiki/index]]
- [[scratchpad/agent-sheets/librarians-assistant/references/workflow]]

- [[workflow]]

## STEP 6 — Report

Deliver to origin (Discord thread).

**Librarians-Assistant — YYYY-MM-DD**

**Fixed:**
- N alias stubs created
- N reciprocal wikilinks added
- N orphan pages connected
- N frontmatter completions
- N tags normalized

**Still open:** [brief list of what couldn't be fixed and why]