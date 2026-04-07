# AGENTS — LLM-WIKI Schema

This document defines conventions for the LLM-WIKI Obsidian vault.
The LLM reads this file at the start of every session to understand
the structure, workflows, and rules for maintaining the wiki.

## Architecture

```
LLM-WIKI/
├── raw/              # Immutable source documents (user-curated)
├── wiki/             # LLM-generated pages (LLM owns this layer)
│   ├── index.md      # Auto-generated page catalogue
│   ├── log.md        # Append-only chronological activity log
│   ├── entities/     # Pages for people, orgs, tools, projects
│   ├── concepts/     # Pages for ideas, theories, patterns
│   └── sources/      # Summaries of ingested raw documents
├── Clippings/        # Obsidian Web Clipper output (treat as raw)
└── CLAUDE.md         # This file — wiki schema & conventions
```

## Frontmatter Format

Every wiki page MUST have YAML frontmatter:

```yaml
---
created: 2026-04-06T12:00:00Z
updated: 2026-04-06T12:00:00Z
type: entity | concept | source | comparison | synthesis
summary: One-line description for the index
tags: [tag1, tag2]
sources: [raw/filename.md]
confidence: 0.9
---
```

## Page Conventions

- **Atomic pages**: Each page covers one entity, concept, or source.
- **Wikilinks**: Use `[[Page Name]]` for all cross-references.
- **Headings**: H1 = page title, H2 = major sections, H3 = subsections.
- **Conflicts**: If sources disagree, create a `## Conflicts` section
  documenting both positions with timestamps — never silently merge.
- **Confidence**: Rate claims 0.0–1.0 in frontmatter. Below 0.7 = flagged.

## Workflows

### Ingest (new raw source)
1. Read the raw file.
2. Discuss key takeaways with the user.
3. Create `wiki/sources/<slug>.md` with summary + key claims.
4. Update or create entity/concept pages touched by this source.
5. Update `wiki/index.md`.
6. Append entry to `wiki/log.md`.

### Query
1. Read `wiki/index.md` to locate relevant pages.
2. Read those pages for context.
3. Synthesize an answer with `[[wikilinks]]` as citations.
4. If the answer is substantial, offer to file it as a new wiki page.

### Lint (health check)
1. Run `wiki_lint` tool.
2. Fix broken links by creating missing pages or correcting names.
3. Connect orphan pages by adding wikilinks from related pages.
4. Fill frontmatter gaps.
5. Flag stale claims (sources older than threshold).

## Synapse Integration

This vault is backed by Project Synapse (Neo4j graph DB + MCP).
When Synapse is connected:

- `wiki_ingest_raw` pushes raw files through the semantic pipeline
  into Neo4j AND creates wiki summary pages.
- `query_knowledge` can be used alongside `wiki_search` for
  graph-powered semantic retrieval.
- `explore_connections` discovers relationships the wiki hasn't
  surfaced yet — use findings to create new concept pages.
- `wiki_lint` + `generate_insights` together form the full
  health-check: structural integrity + semantic gap detection.

## Git / Version Control

The vault is synced via the Obsidian Git plugin to (check with user as this may change):
`https://github.com/angrysky56/LLM-WIKI`

All rollbacks are handled via git. The LLM does not need to
implement undo — destructive edits can be reverted with `git revert`.
