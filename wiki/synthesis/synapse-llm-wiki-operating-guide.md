---
created: 2026-04-11T00:00:00Z
updated: 2026-05-24T09:43:58Z
type: synthesis
summary: Operating guide for LLM-WIKI — schema conventions, workflows, and agent architecture
tags: [meta, schema, conventions, workflow, agent-architecture, wiki-management]
sources:
status: active
confidence: 0.95
---


```




## Wikilink Rules

Filenames are lowercase-hyphen slugs. Wikilinks resolve case-insensitively in Obsidian, but prefer lowercase slugs for consistency:
- `[[neo4j]]` → `wiki/entities/neo4j.md` ✓ (preferred)
- `[[Neo4j]]` → also resolves ✓ (acceptable)
- `[[design-thinking]]` → `wiki/concepts/design-thinking.md` ✓

For display text: `[[page-slug|Display Text]]`  
Never use full paths in wikilinks: `[[slug|Display]]` ✓ / `[[Display|wiki/path/slug]]` ✗  
Never write wikilink syntax inside backtick code spans — the linter will still parse it as a link.




## Lint Protocol

Run `wiki_lint` periodically. Ignore **all** links reported in `log.md` — structural false positives, unfixable by design.

Fix order for real pages:
1. Broken links — create the missing page or fix the slug
2. Orphan pages — add wikilinks from related pages pointing to them
3. Missing frontmatter — fill required fields
4. Confidence < 0.7 — add a `## Caveats` section




## Insight Generation

`generate_insights` runs the Zettelkasten engine — autonomous pattern detection over the graph. Use after:
- A batch of 5+ new ingests
- User asks "what connections am I missing?"
- Periodic health check alongside `wiki_lint`

If an insight scores > 0.8 and is non-obvious, materialise it as a `wiki/concepts/` page with `type: synthesis`.




## What NOT to Do

- **Don't re-ingest** an already-processed file — check `wiki/log.md` first
- **Don't manually move** files from raw/ to Clippings/ — `wiki_ingest_raw` and `wiki_fetch_url` do it automatically
- **Don't reference raw/ file paths** in source pages — use the original URL; files move, URLs don't
- **Don't create pages** for things that fit as sections on existing pages
- **Don't lint log.md** — always false positives
- **Don't use the `obsidian-para` vault** at `/home/ty/Documents/obsidian-para` — unset-up download; PARA is handled via `status` frontmatter here




## Full Tool Reference

| Tool | When to use |
|
|
-|
| `wiki_fetch_url(url)` | Fetch + clean + ingest + archive any web URL |
| `wiki_ingest_raw(filename)` | Ingest file already in raw/ + auto-archive |
| `wiki_write_page(path, body)` | Create/update any wiki page |
| `wiki_read_page(path)` | Read a specific page |
| `wiki_search(query)` | Keyword search across wiki files |
| `wiki_list_pages()` | List all pages (useful for orientation) |
| `wiki_update_index()` | Rebuild index.md after writes |
| `wiki_lint()` | Health check — run periodically |
| `query_knowledge(query)` | Vector ANN search over Neo4j graph |
| `explore_connections(topic)` | Graph traversal for hidden relationships |
| `generate_insights()` | Zettelkasten pattern detection |




## Connections

- [[project-synapse]] — the MCP server backing this system
- [[llm-wiki-pattern]] — Karpathy's original pattern this extends
- [[obsidian]] — the human-readable vault layer
- [[neo4j]] — the graph/vector storage layer
- [[obsidian-skills-repo]] — defuddle and other Obsidian agent skills
- [[para-methodology]] — organizational concepts as frontmatter metadata
- [[obsidian-cli-skill]] — alternative vault interface when Obsidian is running
