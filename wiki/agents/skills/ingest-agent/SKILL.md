---
created: 2026-05-24T00:00:00Z
updated: 2026-05-24T00:00:00Z
type: skill
summary: Ingest pipeline operator — processes raw/ inbox into wiki knowledge, handles arXiv papers, enforces quality standards
tags: [agent-skill, ingest, pipeline, wiki-ops]
sources: []
status: reference
confidence: 1.0
---

# Ingest Agent

**Agent ID:** `ingest-agent`  
**Job ID:** `c838e81a1496`  
**Schedule:** Daily 08:30 AM (cron) + manual trigger  
**Delivery:** local (verbose internal job)  
**Trigger:** `/ingest-agent`

---

## Bootstrap

1. Read this skill file
2. Read agent sheet: `wiki/scratchpad/agent-sheets/ingest.md`
3. Read jobs sheet: `wiki/scratchpad/jobs/sheet.md`
4. Execute per agent sheet directives

---

## Key Paths

```
Wiki root:       /home/ty/Documents/LLM-WIKI/
Raw inbox:       /home/ty/Documents/LLM-WIKI/raw/         ← NOT wiki/raw/
Clippings:       /home/ty/Documents/LLM-WIKI/Clippings/
Agent sheet:     wiki/scratchpad/agent-sheets/ingest.md
Jobs sheet:      wiki/scratchpad/jobs/sheet.md
Reports:         wiki/scratchpad/jobs/reports/ingest/
Carryover:       wiki/scratchpad/jobs/reports/ingest/carryover.md
```

**Path correction:** `raw/` lives at `/home/ty/Documents/LLM-WIKI/raw` (parent of `wiki/`), NOT `wiki/raw/`. All `find`/`ls` operations must use the correct absolute path.

---

## Core Tools

**MCP availability probe** (run first if using MCP tools):
```bash
/home/ty/Repositories/ai_workspace/project-synapse-mcp/.venv/bin/python3 \
  -c "from synapse_mcp.zettelkasten.insight_engine import InsightEngine; print('OK')" \
  2>/dev/null && echo "MCP OK" || echo "MCP UNAVAILABLE"
```
If MCP unavailable: skip `wiki_ingest_raw` and `wiki_lint`, log to carryover and retry next cycle.

| Tool | Purpose |
|------|---------|
| `wiki_ingest_raw` | Ingest file from raw/ into Neo4j + wiki/sources/; auto-archives to Clippings/ |
| `wiki_write_page` | Write or update a wiki page with frontmatter |
| `wiki_fetch_url` | Fetch URL with defuddle → save to raw/ and optionally ingest |
| `wiki_lint()` | Health check: orphan pages, broken wikilinks, missing frontmatter |
| `wiki_update_index(deep=True)` | Rebuild wiki index after ingestion |
| `terminal` + `find` | Discover files in raw/ paths |

---

## raw/ Scanning

**Process in priority order:**
1. Files flagged by Ty in jobs sheet
2. New files added since last run
3. Old files still pending (backlog)

**File discovery:**
```bash
# Find all files in raw/ (non-recursive)
find /home/ty/Documents/LLM-WIKI/raw -maxdepth 1 -type f

# Find files newer than last run (compare mtime)
find /home/ty/Documents/LLM-WIKI/raw -maxdepth 1 -type f -newer /home/ty/Documents/LLM-WIKI/wiki/scratchpad/jobs/reports/ingest/carryover.md
```

**Supported file types:** papers (PDF, LaTeX), articles (HTML, markdown), documentation, repositories

**Critical rule: raw/ Must Stay Empty**
After every run, `raw/` should be EMPTY. Every file must be:
- Ingested → `wiki/sources/` → auto-moved to `Clippings/`
- Skipped with explicit reason in report
- Flagged for special handling

This is the #1 pipeline health metric.

---

## arXiv Paper Pipeline

For academic papers (arXiv or similar):

### Step 1 — Fetch paper metadata/content

Use the `wiki_fetch_url` + `wiki_write_page` combo:

```
1. wiki_fetch_url(url="https://arxiv.org/abs/XXXX.XXXX")  → saves defuddled page to raw/
2. wiki_ingest_raw(filename="arxiv-abs-XXXX-XXXX.md")     → ingest into Neo4j + wiki/sources/
3. wiki_write_page(...)                                  → create/update summary page in wiki/sources/papers/
```

### Step 2 — Write summary page

Create or update `wiki/sources/papers/<paper-id>.md`:

```markdown
---
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: source
summary: <one-line paper summary>
tags: [paper, arxiv, <primary-domain>]
sources: [arxiv:<id>]
status: reference
confidence: 0.8
---

# <Paper Title>

**arXiv:** [XXXX.XXXX](https://arxiv.org/abs/XXXX.XXXX)  
**Authors:** <author list>  
**Published:** YYYY-MM-DD

## Summary

<2-4 sentence summary of the paper's contribution>

## Key Claims

- <claim 1>
- <claim 2>

## Methodology

<brief description of approach/method>

## Relevance

<why this matters for the wiki/our work>
```

### Step 3 — Quality checks

After ingestion:
- Run `wiki_lint()` to check for broken wikilinks
- Verify frontmatter has `type: source` and a non-generic summary
- Confirm tags are accurate (see [[tag-taxonomy]])
- Archive check: verify file moved to `Clippings/papers/YYYY/`

---

## Quality Standards

### Ingest Completeness
- Never leave half-processed files in raw/
- Every ingested file must have frontmatter with `type`, `summary`, `tags`
- After successful ingest, `wiki_ingest_raw` auto-archives to Clippings/ — do NOT manually `rm`

### Frontmatter Requirements
```yaml
---
created: YYYY-MM-DDTHH:MM:SSZ
updated: YYYY-MM-DDTHH:MM:SSZ
type: source | entity | concept | synthesis  # must be correct type
summary: <one-line, non-generic description>
tags: [<relevant tags>]
sources: [<source reference>]
status: reference | draft | archived
confidence: 0.0-1.0
---
```

### Wikilink Integrity
- Every page should link to related concepts/entities using `[[wikilink]]` syntax
- Run `wiki_lint()` after bulk ingestion to catch broken links
- Orphan pages (no incoming links) should be flagged and linked from relevant concept pages

### Summary Quality
- Summaries must be specific: `"Implements retrieval-augmented generation using bipartite graph attention"` NOT `"This paper discusses AI"`
- If a summary would be identical for multiple files, the frontmatter needs refinement

### Tag Accuracy
- See `wiki/scratchpad/tag-taxonomy.md` before tagging
- Primary domain tag required (e.g., `ml`, `nlp`, `agents`, `infrastructure`)
- Type tag required (`paper`, `article`, `doc`, `repo`)

---

## Report Format

Save to: `wiki/scratchpad/jobs/reports/ingest/ingest-YYYY-MM-DD.md`

```markdown
# Ingest Report — YYYY-MM-DD

## Processing Summary
- Files in raw/: N
- Files processed: N
- Files skipped: N (with reasons)
- Files archived: N

## Ingested Files
1. **[filename]** → `wiki/sources/<path>`
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

---

## Carryover

Write to: `wiki/scratchpad/jobs/reports/ingest/carryover.md`

Track:
- Current backlog size
- Recurring issues with file types
- Pipeline improvements needed
- Files that need special handling

---

## Edge Cases

| Situation | Action |
|-----------|--------|
| Corrupted/unreadable file | Skip and flag in report |
| Very large or unusual format | Flag and note what's needed in report |
| File already ingested | Expected — file moved to Clippings/, skip |
| `raw/` has >10 files | Process highest priority, note backlog |
| MCP unavailable | Skip `wiki_ingest_raw`/`wiki_lint`, log to carryover |
| Unsure about file type | Err on the side of ingestion |

---

## Jobs Sheet Update

After each run, patch status in `wiki/scratchpad/jobs/sheet.md`:

```
| `c838e81a1496` | llm-wiki-raw-ingest | ingest | **done** | YYYY-MM-DD |
```