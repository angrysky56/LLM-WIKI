---
name: ingest
description: "Daily raw file ingestion pipeline — process files from raw/ into structured wiki knowledge, verify frontmatter and links, archive to Clippings/. Schedule: 08:30 AM."
tags: [ingest, pipeline, wiki-operations, daily]
triggers:
  - cron: "30 8 * * *"
  - manual: delegate_task
updated: 2026-05-25
created_by: agent
---

# ingest — Raw File Ingestion Pipeline

Process raw files from the `raw/` inbox into structured wiki knowledge. Every file should either be ingested and archived, or skipped with explicit reason.

## See Also

- `references/workflow.md` — 7-step ingest pipeline
- `templates/ingest-report.md` — daily report format

## Quick Start

1. Load the `ingest` skill
2. Read jobs sheet for priority files
3. List `raw/` — prioritize flagged → new → backlog
4. Process each file via `wiki_ingest_raw`
5. Verify frontmatter and wikilinks
6. Archive to Clippings/ subfolder
7. Deliver ingest report (silent if nothing to process)

## FINAL STEP — Update Carryover (REQUIRED)

After all ingest operations complete, write updated carryover to `wiki/scratchpad/agent-sheets/ingest/carryover.md`. Include:
- Files ingested this cycle (source + count)
- Ingest errors or stalled items
- Open items for next cycle
- Last run timestamp

## Wiki Operations
- **Tools:** `synapse_recall` (check for existing content before ingesting), `wiki_write_page` (create/update pages), `wiki_update_index` (after changes)
- **Constraint:** Verify no duplicate before writing — `synapse_recall` first, then `wiki_write_page`.

## Critical Rule

**`raw/` must be EMPTY after every run.** Every file either:
- Ingested → archived in Clippings/
- Skipped → explicit reason in report

## Quality Standards

- Ingest completely — no half-processed files
- Verify frontmatter on every page
- Check wikilink integrity on every new page
- Archive source immediately after successful ingest