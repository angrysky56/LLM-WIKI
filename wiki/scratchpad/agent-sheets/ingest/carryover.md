---
created: 2026-05-26
updated: 2026-05-26
type: carryover
summary: Ingest pipeline healthy — 2 files processed, raw/ empty, no issues
tags: [ingest, carryover]
---

# Ingest Agent Carryover

## Established
- **Pipeline healthy**: raw/ emptied after every run
- **Ingest approach**: Copy source to Clippings/ then write summary page to wiki/sources/
- **MCP unavailable**: synapse MCP server doesn't expose `wiki_ingest_raw` — running CLI/manual approach

## Open
- **292 broken wikilinks**: Pre-existing, needs librarian agent attention
- **146 orphan pages**: Agent sheets/reports — expected
- **38 missing frontmatter**: Carryover pages lack frontmatter (agent sheets, reports)
- **209 non-reciprocal links**: Bidirectional link gaps

## Heading
- **Next run**: Monitor for new raw/ files from news and arxiv cron jobs
- **Backlog**: Empty — raw/ is clean

## Notes
- **2026-05-26 run**: 2 files processed (colab-mcp repository, Menin/D-serine article)
  - colab-mcp → archived to Clippings/repositories/2026/ + summary at wiki/sources/repositories/googlecolab-colab-mcp.md
  - Menin article → archived to Clippings/articles/2026/ + summary at wiki/sources/articles/menin-d-serine-hypothalamus-anti-aging.md
  - raw/ is now empty

## Kanban Status
- [x] Surfaced to hermes kanban: 2026-05-26
  - No new open items from this run