# Ingest Agent Carryover

## Established
- **Pipeline healthy**: raw/ emptied after every run, all files archived to Clippings/
- **MCP unavailable**: synapse MCP server doesn't expose `wiki_ingest_raw` directly — running raw CLI instead
- **Ingest approach**: Manual file processing (MCP not available for direct ingest), copy to Clippings then write summary page to wiki/sources/
- **3 files ingested**: kanban-multi-agent-board, profiles-running-multiple-agents, scheduled-tasks-cron (all documentation type)

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