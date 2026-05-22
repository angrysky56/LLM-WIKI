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

Fix the open wiki health issues identified by the Wiki Librarian audit. Work in batches, report progress, and carry open items to the next cycle.

**synapse** mcp tools:

1. `wiki_lint()` — detect broken links, orphans, missing frontmatter
2. `wiki_read_page` — read a page to fix it
3. `wiki_write_page` — fix frontmatter, add wikilinks, normalize tags
4. `wiki_search` — find related pages for orphan linking
5. `wiki_cluster_pages()` — find same-cluster pages for cross-linking
6. `wiki_update_index()` — rebuild index after fixes

---

## Priority Fix Order

### P0 — Alias Stubs (high impact, easy wins)

Create stub pages for concept aliases that have no target:

1. **`[[reasoning]]`** → Create `wiki/concepts/reasoning.md` as a redirect/stub to `[[load-bearing-reasoning]]`
2. **`[[rz-nas]]`** → Create `wiki/concepts/rz-nas.md` stub (it's a neural architecture search method)
3. **`[[llama-nas]]`** → Create `wiki/concepts/llama-nas.md` stub (LLaMA NAS approach)
4. **`[[wolfram-physics-project]]`** → Create `wiki/concepts/wolfram-physics-project.md` stub

A stub page should have minimal frontmatter + a one-line description noting the concept is documented elsewhere or needs development.

### P1 — Non-Reciprocal Wikilinks

A→B without B→A. Add return links. Priority pairs from last audit:
- `efhf` ↔ `maximum-occupancy-principle` (both missing)
- `hermes-agent` ↔ `markovian-dev-agency` (missing both directions)
- `meta-harness` ↔ `agem` (missing both)
- `load-bearing-reasoning` ↔ `chain-of-thought` (missing both)
- `maximum-occupancy-principle` ↔ `efhf` (already listed above)

For each reciprocal pair: read both pages, add the missing wikilink to each.

### P2 — Orphan Pages

Pages with zero inbound links that are load-bearing concepts (not self-contained daily reports).  
From last audit: `hermes-agent`, `librarian`, `researcher`, `orcaid`, `ingest`, `arxiv`, `meta-harness`, `agem`.

Find related pages and add wikilink context from those pages.

### P3 — Frontmatter Completeness

Pages missing required frontmatter fields. Priority: concept pages over daily reports.

Required fields: `created`, `updated`, `type`, `summary`, `tags`.

### P4 — Tag Normalization

Use `tag-taxonomy.md` as canonical. Normalize:
- `concept` vs `concepts` → canonical is `concept`
- Mixed-case variants → lowercase
- Missing tags on concept pages

---

## Workflow

### STEP 1 — Read carryover
Read: `wiki/scratchpad/jobs/reports/librarian/carryover.md`  
This tells you what the librarian found and what's already been fixed.

### STEP 2 — Read batch progress
Read: `wiki/scratchpad/jobs/reports/librarian/batch-progress.md` (if it exists)  
知道你已经做到哪里了.

### STEP 3 — Run fixes
Work through P0 → P1 → P2 → P3 → P4 in order.

After every 15-20 fixes, write a progress note to:
`wiki/scratchpad/jobs/reports/librarian/batch-progress.md`

Format:
```markdown
# Batch Progress — YYYY-MM-DD HH:MM

## Fixes Applied This Batch
- Fixed [[reasoning]] alias → created stub page
- Added 5 reciprocal links
- Resolved 3 orphans

## Remaining Open Items
- [[llama-nas]] stub not yet created
- 98 non-reciprocal links remain
- etc.

## Next Batch Starts With
- [first task]
```

### STEP 4 — Update assistant carryover
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

### STEP 5 — Report
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