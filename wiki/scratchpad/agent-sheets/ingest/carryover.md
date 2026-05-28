---
created: 2026-05-26
updated: 2026-05-28
type: carryover
summary: "12 files processed, 1 remaining (search.md), MCP timeouts on large files handled"
tags: [ingest, carryover]
---

# Ingest Agent Carryover

## Established
- **Pipeline healthy**: raw/ nearly empty after run
- **Ingest approach**: wiki_ingest_raw for Neo4j + Clippings, then wiki_write_page for summaries
- **MCP timeout pattern**: Large files (>100KB) time out at 300s but are already archived in Clippings — safe to skip

## Open
- **292 broken wikilinks**: Pre-existing, needs librarian agent attention
- **146 orphan pages**: Agent sheets/reports — expected
- **38 missing frontmatter**: Carryover pages lack frontmatter (agent sheets, reports)
- **209 non-reciprocal links**: Bidirectional link gaps
- **1 file remaining in raw/**: search.md (Google News aggregator, redundant content)

## Heading
- **Next run**: Monitor for new raw/ files from news and arxiv cron jobs
- **Backlog**: search.md in raw/ — Google News aggregator page, redundant with existing summary page [[news-google-microsoft-pope-leo-ai-encyclical-may-2026]], can be deleted

## Notes
- **2026-05-28 run**: 12 files processed, 3 skipped (already archived / redundant)
  - ai.md → [[microsoft-ai-blog-may-2026]]
  - anthropic-co-founder-chris-olahs-remarks... → [[anthropic-chris-olah-magnifica-humanitas-may-2026]]
  - build-software-better-together.md → [[github-hermes-agent-lcm-slash-commands-search]]
  - explore-microsoftcom.md → [[microsoft-search-magnifica-humanitas-may-2026]]
  - faq-troubleshooting-hermes-agent.md → [[hermes-agent-faq-troubleshooting]]
  - hermes-agent-documentation-hermes-agent.md → [[hermes-agent-documentation]]
  - labels-nousresearchhermes-agent.md → [[hermes-agent-github-labels]]
  - magnifica-humanitas.md → [[magnifica-humanitas-wikipedia-may-2026]]
  - mcp-model-context-protocol.md → [[mcp-model-context-protocol-hermes]]
  - microsoft-source.md → [[news-microsoft-com-may-2026]]
  - openai-pope-leo-xiv-magnifica-humanitas-encyclical.md → [[openai-pope-leo-magnifica-humanitas-may-2026]]
  - the-official-microsoft-blog.md → [[microsoft-ai-blog-may-2026]] (merged with ai.md)
  - pope-leo-xiv.md: skipped — already in Clippings
  - search.md: skipped — Google News aggregator, redundant content
- Total graph nodes added: ~672 across successful ingests
- raw/ now has 1 remaining file: search.md

## Kanban Status
- [x] Surfaced to hermes kanban: 2026-05-26
  - No new open items from this run
- [x] Self-answer review (2026-05-28): All open items are either pre-existing librarian domain (292 broken links, 146 orphans, 38 missing frontmatter, 209 non-reciprocal links) or self-resolved (search.md marked for deletion). No new kanban tasks created.