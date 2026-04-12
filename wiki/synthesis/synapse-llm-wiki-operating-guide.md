---
summary: Agent operating instructions for the Synapse + LLM-WIKI system — tool decision logic, content lifecycle, ingest and fetch workflows, writing conventions
tags: [meta, agent, operating-guide, workflow, synapse, llm-wiki, defuddle]
updated: 2026-04-11T03:50:24Z
---

# Using the Synapse + LLM-WIKI System

**Type:** Agent operating instructions  
**Audience:** Claude (me) at the start of any session involving this system  
**Last updated:** 2026-04-11

---

## What This System Is

Two layers that work together:

| Layer | Tool | Role |
|-------|------|------|
| **Graph** | Neo4j via `project-synapse` MCP | Semantic storage, vector search, relationship traversal, insight generation |
| **Wiki** | Obsidian vault at `/home/ty/Documents/LLM-WIKI` | Human-readable output, browsable Markdown, Git-versioned |

They are not duplicates. Neo4j stores structured knowledge for machine retrieval. The wiki stores compressed, interlinked prose for human reading and my own orientation. **Both should be updated together.**

The vault schema lives in `AGENTS.md` at the vault root. Read it if conventions are unclear.

---

## Session Start Checklist

1. Read `wiki/index.md` — get the current page inventory in one scan
2. Check `raw/` — any files there need processing before the session ends
3. If the user mentions a specific topic, run `wiki_search` before doing anything else — avoid re-creating existing knowledge

---

## Tool Decision Logic

### Fetching web content

```
Need content from a URL?
│
├─ URL is a standard article/page → wiki_fetch_url(url)
│     defuddle strips clutter, ingests into Neo4j,
│     archives to Clippings/ automatically — one call
│
└─ URL is already markdown (.md, raw GitHub, etc.) → use web_fetch directly
      then save manually to raw/ and wiki_ingest_raw()
```

### Retrieving existing knowledge

```
User asks about a topic
│
├─ Likely already in the wiki?
│   └─ YES → wiki_search first, then wiki_read_page on hits
│
├─ Relationship / connection question?
│   └─ YES → explore_connections (graph traversal)
│
├─ Semantic / meaning question?
│   └─ YES → query_knowledge (vector ANN search)
│
└─ Synthesising across multiple topics?
    └─ YES → query_knowledge + wiki_read_page combo
              then offer to file result as a new concept page
```

### When to write to the wiki

| Page type | Create when |
|-----------|-------------|
| `wiki/sources/` | A source has been ingested (raw file or URL fetch) |
| `wiki/concepts/` | A pattern spans multiple sources, or a synthesis emerges that isn't captured |
| `wiki/entities/` | A person, tool, project, or org appears in multiple places |

**Prefer updating over creating.** If the information fits as a section on an existing page, add it there rather than making a new page.

---

## Content Lifecycle

```
Ty clips/saves → raw/            (your inbox)
     or
I fetch → wiki_fetch_url(url)    (web research)
               │
         [defuddle cleans]
               │
         [semantic pipeline] → Neo4j
               │
         wiki_write_page → wiki/sources/
               │
         auto-move → Clippings/  (permanent archive)
```

`raw/` is an **inbox only** — it should be empty at the end of every session. `Clippings/` is the permanent record. Source pages reference the **original URL**, not the file path, so nothing breaks when files move.

---

## Ingest Workflow (file in raw/)

```
1. wiki_ingest_raw(filename)
      → Neo4j nodes + embeddings
      → auto-moves file to Clippings/ ✅ (automatic, no manual step)
2. wiki_write_page(wiki/sources/<slug>.md)
      → Compressed summary, key claims, original URL in frontmatter
3. Update touched concept/entity pages with new wikilinks or sections
4. wiki_update_index()
```

## Fetch Workflow (URL)

```
1. wiki_fetch_url(url)
      → defuddle strips clutter
      → Neo4j nodes + embeddings
      → auto-archives to Clippings/ ✅ (automatic)
2. wiki_write_page(wiki/sources/<slug>.md)   ← still my job
3. Update touched concept/entity pages
4. wiki_update_index()
```

Use `wiki_fetch_url(url, ingest=False)` to save to raw/ first for review before ingesting.

---

## Writing Good Wiki Pages

**Sources** (`wiki/sources/`): Compress the raw material. One "Core Insight" capturing the non-obvious takeaway. Key claims as a table. Original URL in frontmatter `sources` field. Don't reproduce — summarise and point.

**Concepts** (`wiki/concepts/`): Define precisely, show the mechanism. Include a `## Connections` section with wikilinks and a `## Open Questions` section — this is how the system surfaces gaps.

**Entities** (`wiki/entities/`): Role in this system first. A table of interfaces/relationships is more useful than prose.

**Frontmatter required fields:**
```yaml
---
created: <ISO timestamp>
updated: <ISO timestamp>
type: entity | concept | source | synthesis
summary: One-line description (used in index)
tags: [tag1, tag2]
sources: <original URL>
status: active | reference | archived
confidence: 0.0–1.0
---
```

---

## Wikilink Rules

Filenames are lowercase-hyphen slugs. Wikilinks resolve case-insensitively in Obsidian, but prefer lowercase slugs for consistency:
- `[[neo4j]]` → `wiki/entities/neo4j.md` ✓ (preferred)
- `[[Neo4j]]` → also resolves ✓ (acceptable)
- `[[design-thinking]]` → `wiki/concepts/design-thinking.md` ✓

For display text: `[[page-slug|Display Text]]`  
Never use full paths in wikilinks: `[[slug|Display]]` ✓ / `[[Display|wiki/path/slug]]` ✗  
Never write wikilink syntax inside backtick code spans — the linter will still parse it as a link.

---

## Lint Protocol

Run `wiki_lint` periodically. Ignore **all** links reported in `log.md` — structural false positives, unfixable by design.

Fix order for real pages:
1. Broken links — create the missing page or fix the slug
2. Orphan pages — add wikilinks from related pages pointing to them
3. Missing frontmatter — fill required fields
4. Confidence < 0.7 — add a `## Caveats` section

---

## Insight Generation

`generate_insights` runs the Zettelkasten engine — autonomous pattern detection over the graph. Use after:
- A batch of 5+ new ingests
- User asks "what connections am I missing?"
- Periodic health check alongside `wiki_lint`

If an insight scores > 0.8 and is non-obvious, materialise it as a `wiki/concepts/` page with `type: synthesis`.

---

## What NOT to Do

- **Don't re-ingest** an already-processed file — check `wiki/log.md` first
- **Don't manually move** files from raw/ to Clippings/ — `wiki_ingest_raw` and `wiki_fetch_url` do it automatically
- **Don't reference raw/ file paths** in source pages — use the original URL; files move, URLs don't
- **Don't create pages** for things that fit as sections on existing pages
- **Don't lint log.md** — always false positives
- **Don't use the `obsidian-para` vault** at `/home/ty/Documents/obsidian-para` — unset-up download; PARA is handled via `status` frontmatter here

---

## Full Tool Reference

| Tool | When to use |
|------|-------------|
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

---

## Connections

- [[project-synapse]] — the MCP server backing this system
- [[llm-wiki-pattern]] — Karpathy's original pattern this extends
- [[obsidian]] — the human-readable vault layer
- [[neo4j]] — the graph/vector storage layer
- [[obsidian-skills-repo]] — defuddle and other Obsidian agent skills
- [[para-methodology]] — organizational concepts as frontmatter metadata
- [[obsidian-cli-skill]] — alternative vault interface when Obsidian is running
