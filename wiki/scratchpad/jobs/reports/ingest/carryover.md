---
created: 2026-06-27
updated: 2026-06-27
type: carryover
summary: Ingest agent carryover — pipeline healthy, MCP unavailable, 38 missing frontmatter flagged
tags: [ingest, carryover]
---

# Ingest Agent Carryover

## Established
- **Pipeline healthy**: raw/ emptied after every run, all files archived to Clippings/
- **MCP unavailable**: synapse MCP server doesn't expose `wiki_ingest_raw` directly — running raw CLI instead
- **Ingest approach**: Manual file processing (MCP not available for direct ingest), copy to Clippings then write summary page to wiki/sources/
- **3 files ingested**: kanban-multi-agent-board, profiles-running-multiple-agents, scheduled-tasks-cron (all documentation type)
- **3 more files ingested (this run, 2026-06-27)**: codegraph-hermes-phase1-implementation, codegraph-readme, hermes-path-forward (all documentation)

## Open
- **292 broken wikilinks**: Pre-existing, needs librarian agent attention
- **146 orphan pages**: Agent sheets/reports — expected
- **38 missing frontmatter**: Carryover pages lack frontmatter (agent sheets, reports)
- **209 non-reciprocal links**: Bidirectional link gaps

## Heading
- **Next run**: Monitor for new raw/ files from news and arxiv cron jobs
- **Backlog**: Empty — raw/ is clean

## Notes
- MCP server test succeeds (`InsightEngine` loads OK) but tools aren't exposed via `wiki_ingest_raw` pattern — need to verify actual MCP tool names available
- Three Hermes Agent docs ingested: Kanban board, Profiles, Scheduled Tasks (all documentation type, confidence 0.95)
- Source files archived to `Clippings/documentation/2026/`
- **2026-05-25 run**: 1 file processed (Kanban Wikipedia article), archived to Clippings/articles/2026/, summary written to wiki/sources/articles/kanban-development.md
- **2026-06-27 run**: 3 files processed (codegraph-hermes-phase1-implementation, codegraph-readme, hermes-path-forward), archived to Clippings/documentation/2026/, summaries written to wiki/sources/documentation/

## Kanban Status
- [x] Surfaced to hermes kanban: 2026-06-27
  - 3 open items → t_0c7ec52de58b56b7 (broken wikilinks), t_c1d9d10d15cd07cc (orphans), t_1354d9bfe9598069 (frontmatter)