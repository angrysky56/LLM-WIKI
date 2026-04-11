---
summary: LLM-WIKI schema, conventions, and workflow guide for the AI agent maintaining this vault
tags: [meta, schema, conventions, workflow]
updated: 2026-04-10T23:19:28Z
---

# AGENTS — LLM-WIKI Schema

This document defines conventions for the LLM-WIKI Obsidian vault.
Read this at the start of every session to understand structure, workflows, and maintenance rules.

> **Agent operating guide:** For tool decision logic, workflow details, and what to avoid, see [[synapse-llm-wiki-operating-guide]].

## Architecture

```
LLM-WIKI/
├── raw/              # INBOX ONLY — unprocessed files; should be empty after each session
├── Clippings/        # Permanent source archive — processed files live here
├── raw-inbox.base    # Obsidian Base view of current raw/ queue
├── wiki/             # LLM-generated pages (LLM owns this layer)
│   ├── index.md      # Auto-generated page catalogue (rebuild after any write session)
│   ├── log.md        # Append-only chronological activity log (EXCLUDE from lint scans)
│   ├── entities/     # Pages for people, orgs, tools, projects
│   ├── concepts/     # Pages for ideas, theories, patterns, methodologies
│   └── sources/      # Compressed summaries of ingested raw documents
└── AGENTS.md         # This file — schema, conventions, and self-improvement notes
```

## Frontmatter Format

Every wiki page MUST have YAML frontmatter:

```yaml
---
created: 2026-04-06T12:00:00Z
updated: 2026-04-06T12:00:00Z
type: entity | concept | source | synthesis
summary: One-line description for the index
tags: [tag1, tag2]
sources: [raw/filename.md]
status: active | reference | archived
confidence: 0.9
---
```

**Field notes:**
- `status` — borrowed from PARA: `active` = currently being developed; `reference` = stable reference material; `archived` = superseded or dormant
- `confidence` — rate key claims 0.0–1.0. Below 0.7 = add a `## Caveats` section
- `sources` — reference the **original URL** (not the raw file path); the raw file is a temporary artifact
- `tags` — **check `wiki/concepts/tag-taxonomy.md` first**; use only preferred terms listed there
- `log.md` and `index.md` are exempt from frontmatter requirements

## Page Conventions

- **Atomic**: One entity, concept, or source per page. If a page needs to cover two things, split it.
- **Wikilinks**: Use `[[page-slug]]` (lowercase-hyphenated filename, no extension). Do NOT use `[[Display Text]]` format for slugs that don't match filenames — use `[[slug|Display Text]]` instead.
- **Headings**: H1 = page title, H2 = major sections, H3 = subsections. No H1 in frontmatter — it goes in the body.
- **Conflicts**: If sources disagree, add a `## Conflicts` section documenting both positions with source + date. Never silently merge.
- **Progressive Summarization**: `sources/` pages = compressed summary of raw. `concepts/` pages = further distillation across multiple sources. Each layer loses some specificity but gains connectivity.
- **Log exemption**: `wiki/log.md` contains raw log entries that may include wikilinks as text. Do NOT lint log.md for broken links — it will always produce false positives.

## Wikilink Slug Convention

Page filenames use lowercase-hyphen slugs. Wikilinks must match exactly:
- `[[neo4j]]` → `wiki/entities/neo4j.md` ✓
- `[[project-synapse]]` → `wiki/entities/project-synapse.md` ✓
- `[[obsidian-cli-skill]]` → `wiki/sources/obsidian-cli-skill.md` ✓

When creating a new page, choose the slug first, then use it consistently everywhere.

## Workflows

### Session Start
1. Read this file (AGENTS.md).
2. Check `wiki/index.md` for current page inventory (structural TOC).
3. Check `wiki/concept-index.md` for concept-to-page mapping (conceptual index).
4. Note any user-indicated new raw files to process.

### Ingest (new raw source)
1. Run `wiki_ingest_raw` to push through semantic pipeline into Neo4j.
2. Create `wiki/sources/<slug>.md` — use the **original source URL** as the canonical reference, not the raw file path.
3. Update or create any entity/concept pages touched by this source.
4. Run `wiki_update_index`.
5. Append a brief entry to `wiki/log.md`.
6. **Tell Ty to move the raw file to `Clippings/`** — raw/ should be empty after each session.

### Query
1. Read `wiki/index.md` to locate relevant pages.
2. Read those pages for context.
3. Use `query_knowledge` or `explore_connections` for graph-powered synthesis.
4. Synthesize with `[[wikilinks]]` as citations.
5. If the synthesis is substantial and non-obvious, offer to file it as a new concept page.

### Lint (health check)
1. Run `wiki_lint`.
2. **Ignore all reported links in `log.md`** — these are structural false positives.
3. Fix broken links in actual wiki pages: create missing pages or correct slug spelling.
4. Connect orphan pages by adding wikilinks from related pages.
5. Fill frontmatter gaps (missing `summary`, `status`, `confidence`).

### Self-Improvement
- This is an experimental system. When a structural pattern seems wrong, fix it.
- Document the reasoning in `wiki/log.md` under a `## [date] schema-update` entry.
- Update this file when conventions change.

## PARA Integration

Rather than a separate PARA vault, this wiki uses PARA concepts as **metadata overlays**:

| PARA concept | LLM-WIKI implementation |
|---|---|
| Projects | Pages tagged `status: active` with a clear goal state |
| Areas | Pages tagged `status: reference` for ongoing standards |
| Resources | Most `sources/` and `concepts/` pages |
| Archives | Pages tagged `status: archived` |
| Progressive Summarization | `raw/` → `sources/` → `concepts/` compression chain |

See [[para-methodology]] for full details.

## Obsidian CLI

The `obsidian` CLI (requires Obsidian running) provides an alternative to Desktop Commander for vault interaction. Useful for:
- Vault-aware operations: backlinks, tasks, daily notes, tags
- Property/frontmatter manipulation: `obsidian property:set`
- Search without MCP: `obsidian vault="LLM-WIKI" search query="..."`

See [[obsidian-cli-skill]] for full command reference.

## Synapse Integration

This vault is backed by Project Synapse (Neo4j + MCP). When connected:

| Tool | Purpose |
|------|---------|
| `wiki_ingest_raw` | Semantic pipeline → Neo4j + creates sources/ page |
| `wiki_write_page` / `wiki_read_page` | CRUD on wiki Markdown |
| `query_knowledge` | Vector ANN semantic search over graph |
| `explore_connections` | Graph traversal for hidden relationships |
| `wiki_lint` | Structural health check (broken links, orphans, missing frontmatter) |
| `generate_insights` | Semantic gap detection — combine with lint for full health check |

See [[project-synapse]] for architecture details.

## Git / Version Control

Vault synced via Obsidian Git plugin to `https://github.com/angrysky56/LLM-WIKI`.
All rollbacks via git — the LLM does not need to implement undo.
