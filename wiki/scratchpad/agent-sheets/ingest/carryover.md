---
created: 2026-05-26
updated: 2026-05-27
type: carryover
summary: Ingest pipeline healthy — 1 file processed, raw/ empty, no issues
tags: [ingest, carryover]
---

# Ingest Agent Carryover

## Established
- **Pipeline healthy**: raw/ emptied after every run
- **Ingest approach**: Copy source to Clippings/ then write summary page to wiki/sources/
- **MCP unavailable**: synapse MCP server doesn't expose `wiki_ingest_raw` — using wiki_write_page directly

## Open
- **292 broken wikilinks**: Pre-existing, needs librarian agent attention
- **146 orphan pages**: Agent sheets/reports — expected
- **38 missing frontmatter**: Carryover pages lack frontmatter (agent sheets, reports)
- **209 non-reciprocal links**: Bidirectional link gaps

## Heading
- **Next run**: Monitor for new raw/ files from news and arxiv cron jobs
- **Backlog**: Empty — raw/ is clean

## Notes
- **2026-05-27 run**: 1 file processed (Ebola Bundibugyo Yahoo search results)
  - ebola-bundibugyo-drc-may-2026 → archived to Clippings/articles/2026/ + summary at wiki/sources/articles/ebola-bundibugyo-drc-uganda-may-2026.md
  - raw/ is now empty
  - No new open items from this run

## Kanban Status
- [x] Surfaced to hermes kanban: 2026-05-26
  - No new open items from this run