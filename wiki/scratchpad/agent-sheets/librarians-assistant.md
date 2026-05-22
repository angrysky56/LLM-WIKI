---
summary: Agent instructions for Librarians-assistant cron job
tags: [agent-instructions, librarians-assistant, wiki-remediation]
updated: 2026-05-21
---

# Librarians Assistant — Agent Sheet

**Job ID**: `librarians-assistant`  
**Schedule**: Daily 08:50 AM (cron) + manual trigger any time  
**Delivery**: origin (Discord thread)  
**Preceded by**: Wiki Librarian (48a3a009a820) at 08:40 AM

---

## Your Task

Fix the open wiki health issues identified by the Wiki Librarian audit. Work in batches, report progress, and carry open items to the next cycle. **Your priorities come from the librarian's carryover and batch-progress — not from hardcoded instructions below.**

**synapse** mcp tools:

1. `wiki_lint()` — detect broken links, orphans, missing frontmatter
2. `wiki_read_page` — read a page to fix it
3. `wiki_write_page` — fix frontmatter, add wikilinks, normalize tags
4. `wiki_search` — find related pages for orphan linking
5. `wiki_cluster_pages()` — find same-cluster pages for cross-linking
6. `wiki_update_index()` — rebuild index after fixes

---

## Workflow

### STEP 1 — Read librarian carryover
Read: `wiki/scratchpad/jobs/reports/librarian/carryover.md`  
This tells you what the librarian found and what's open. The carryover's "What Remains" section is your task list — work through it in the priority order specified there.

### STEP 2 — Read batch progress
Read: `wiki/scratchpad/jobs/reports/librarian/batch-progress.md` (if it exists)  
知道你已经做到哪里了. Start where the last run stopped — don't redo work already done.

### STEP 3 — Run fixes
Read the carryover's open items. Execute them in priority order. Stop at 50+ fixes or when you hit a hard blocker (needs judgment or content creation beyond scope).

### STEP 4 — Update batch-progress
After every 15-20 fixes, write a progress note to:
`wiki/scratchpad/jobs/reports/librarian/batch-progress.md`

Format:
```markdown
# Batch Progress — YYYY-MM-DD HH:MM

## Fixes Applied This Batch
- [list of what you fixed]

## Remaining Open Items
- [list, priority order]

## Next Batch Starts With
- [first task]
```

### STEP 5 — Update assistant carryover
Write state to: `wiki/scratchpad/jobs/reports/librarians-assistant/carryover.md`

```markdown
# Librarians-Assistant Carryover — YYYY-MM-DD

## What Was Fixed
- [list]

## What Remains
- [list, priority order]

## Hard Blockers
- [anything that needs judgment or content creation beyond scope]
```

### STEP 6 — Report
Deliver to origin (Discord thread):

**Librarians-Assistant — YYYY-MM-DD**

**Fixed:**
- N alias stubs created
- N reciprocal wikilinks added
- N orphan pages connected
- N frontmatter completions
- N tags normalized

**Still open:** [brief list of what couldn't be fixed and why]

---

## Quality Bar

- Fix incrementally — don't try to fix everything in one run
- Stop at 50+ fixes or hard blocker (needs judgment)
- Never delete content — move or archive instead
- If a link target genuinely doesn't exist: create a stub, don't remove the wikilink
- Log everything in batch-progress.md

## Questions?
If the task is unclear, write your question and deliver to origin.