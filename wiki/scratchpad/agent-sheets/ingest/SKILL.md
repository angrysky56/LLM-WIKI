---
name: ingest
description: "Daily raw file ingestion pipeline — process files from raw/ into structured wiki knowledge, verify frontmatter and links, archive to Clippings/. Schedule: 06:30 AM."
tags: [ingest, pipeline, wiki-operations, daily]
triggers:
  - cron: "30 6 * * *"
  - manual: delegate_task
updated: 2026-05-27
created_by: agent
---

# ingest — Raw File Ingestion Pipeline

Process raw files from the `raw/` inbox into structured wiki knowledge. Every file should either be ingested and archived, or skipped with explicit reason.

## Tool Protocol

**Use `terminal()` with `cat` / `ls` for ALL file reads in cron context.** `read_file` is not available for background/cron execution. Use MCP tools (`mcp-project-synapse`) for wiki operations.

## Quick Start

1. **Layer 2 Load**: Read `wiki/scratchpad/agent-sheets/ingest/carryover.md` and `wiki/scratchpad/jobs/sheet.md`
2. **Layer 1 Start**: Initialize or clear `vault.md` to act as your episodic scratchpad for this session
3. List raw inbox: `ls -la raw/`
4. Process each file, logging steps and errors to `vault.md`
5. **MOP Compression**: Compress `vault.md` into `carryover.md` (Layer 1 → Layer 2)

## Workflow

### Step 1 — Check Inbox

```bash
ls -la /home/ty/Documents/LLM-WIKI/raw/
```

If `raw/` is empty → write carryover noting "inbox empty, pipeline healthy" and exit silently with `[SILENT]`.

### Step 2 — Process Each File

For each file in `raw/`, in priority order (Ty-flagged → new → backlog):

```
1. CHECK for duplicates first:
   synapse_recall(query="{filename or title}")
   → If content already exists in wiki, skip and note in report

2. INGEST the file:
   wiki_ingest_raw(filename="{filename}")
   → This routes to Clippings/<type>/<year>/ automatically
   → Creates a Neo4j node for the content

3. WRITE source summary:
   wiki_write_page(path="wiki/sources/<type>/<slug>.md", content="{summary}")
   → Type: papers/ articles/ documentation/ repositories/
   → Frontmatter: type=source, status=active, sources={original url}

4. VERIFY:
   wiki_read_page(path="wiki/sources/<type>/<slug>.md")
   → Confirm frontmatter is complete
   → Confirm wikilinks resolve
```

### Step 3 — Cross-Link New Pages

After ingesting all files:

```
1. wiki_search(query="{topic from ingested file}")
   → Find related existing pages

2. Add wikilinks to the source summary connecting to related concepts/entities

3. wiki_update_index()
   → Refresh search index after all changes
```

### Step 4 — Deliver Report

Write report to: `wiki/scratchpad/jobs/reports/ingest/ingest-{YYYY-MM-DD}.md`

```markdown
# Ingest Report — {YYYY-MM-DD}

## Files Processed
| File | Action | Archived To | Wiki Page |
|------|--------|-------------|-----------|
| {filename} | ingested | Clippings/{type}/{year}/ | [[slug]] |

## Errors
| File | Error | Action Taken |
|------|-------|--------------|
| {filename} | {error} | skipped / retried |

## Inbox Status
- Files processed: {N}
- Files skipped: {N} (with reasons)
- raw/ is now: EMPTY / {N} remaining
```

If nothing was processed (empty inbox), respond with `[SILENT]`.

### Final Step — MOP Compression (Layer 1 → Layer 2)

Read your `vault.md` (Episodic Trace) and compress it into `wiki/scratchpad/agent-sheets/ingest/carryover.md` (Semantic State), adhering to the ~512 token bound:

```yaml
---
created: {original date}
updated: {today's date}
type: carryover
summary: "{N} files processed, raw/ {empty|N remaining}"
tags: [ingest, carryover]
---
```

Include:
- **What Was Done**: Files ingested, pages created (compressed from vault.md)
- **What Remains**: `- [ ]` checklist (stalled files, errors, pending retries)

Once compressed, clear or archive your `vault.md` so the next session starts fresh.

## Critical Rule

**`raw/` must be EMPTY after every run.** Every file either:
- Ingested → archived in `Clippings/<type>/<year>/`
- Skipped → explicit reason in report and carryover

## Critical Paths

- **Raw inbox**: `/home/ty/Documents/LLM-WIKI/raw/`
- **Clippings archive**: `/home/ty/Documents/LLM-WIKI/Clippings/<type>/<year>/`
- **Source summaries**: `wiki/sources/<type>/<slug>.md`
- **Reports**: `wiki/scratchpad/jobs/reports/ingest/ingest-YYYY-MM-DD.md`
- **Carryover**: `wiki/scratchpad/agent-sheets/ingest/carryover.md`

## MCP Tools

| Tool | Purpose |
|------|---------|
| `wiki_ingest_raw` | Process raw file → Neo4j + auto-route to Clippings |
| `synapse_recall` | Check for duplicate content before ingesting |
| `wiki_write_page` | Create source summary page |
| `wiki_read_page` | Verify page after creation |
| `wiki_search` | Find related pages for cross-linking |
| `wiki_update_index` | Refresh index after changes |

**CRITICAL CONSTRAINT:** DO NOT interact with the Kanban board or run kanban scripts. Output open items as `- [ ]` in the `## What Remains` section of your `carryover.md`. The overseer will create Kanban tickets and assign them to you in `jobs/sheet.md`. Use the standard MCP tools exclusively.

## Fallback Patterns

- **MCP unavailable**: Note in carryover, DO NOT process files without MCP (risk of lost data)
- **wiki_ingest_raw fails**: Try `wiki_fetch_url` if the file is a URL/link, otherwise note in report
- **Clippings routing wrong**: Manually move file and note the correction in report
- **Empty inbox**: Write "pipeline healthy" to carryover and respond `[SILENT]`

## Quality Standards

- Ingest completely — no half-processed files
- Verify frontmatter on every page created
- Check wikilink integrity on every new page
- Archive source immediately after successful ingest
- Never leave raw/ in an inconsistent state