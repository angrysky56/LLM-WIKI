---
created: 2026-05-25
updated: 2026-05-25
type: synthesis
summary: Operating guide for maintaining the LLM-WIKI — conventions, workflows, best practices
tags: [wiki, documentation, conventions, workflow]
sources: []
status: reference
confidence: 1.0
---

# LLM-WIKI Operating Guide

> **Purpose**: Document conventions, workflows, and best practices for maintaining the wiki.

## Wiki Philosophy

- Keep knowledge nodes atomic and specific — one concept per page
- Write for future readers who need the distilled insight, not the original research trail
- Prefer linking over embedding; pages that grow too large should be split
- Every page needs frontmatter with `description` (used by search) and optionally `tags`

## Filenames and Slugs

Filenames are lowercase-hyphen slugs. Wikilinks resolve case-insensitively in Obsidian, but prefer lowercase slugs for consistency:
- `[[neo4j]]` → `wiki/entities/neo4j.md` ✓ (preferred)
- `[[Neo4j]]` → also resolves ✓ (acceptable)
- `[[design-thinking]]` → `wiki/concepts/design-thinking.md` ✓

For display text with wikilinks, use proper syntax examples outside of code blocks.
Never use full paths in wikilinks: prefer slug-only links.
Never write wikilink syntax inside backtick code spans — the linter will still parse it as a link.

## Lint Protocol

Run `wiki_lint` periodically. Ignore **all** links reported in `log.md` — structural false positives, unfixable by design.

Fix order for real pages:
1. Create stub pages for truly missing concepts
2. Fix slug typos and path errors
3. Remove links to deleted pages

## Wiki Structure

```
wiki/
  agents/         # agent configurations and logs
  concepts/       # atomic knowledge nodes
  entities/       # named entities, people, organizations
  research/       # research logs and extracted papers
  scratchpad/     # working notes, job reports
  synthesis/      # synthesized insights and patterns
  references/     # reference documents
  sources/        # raw ingested sources
```

## Page Status

- Use frontmatter `tags: []` to categorize (empty array if no tags)
- Use `created: YYYY-MM-DD` for newly created pages (optional)
- Dead pages should be moved to a `_archive/` directory, not deleted

## Link Conventions

- Page anchors: `[[slug#section-name]]` for section links
- Display aliases: `[[slug|Display Text]]` to override shown text
- Never link to paths: `[[concepts/foo]]` not `[[wiki/concepts/foo.md]]`
- Cross-namespace links are fine: `[[scratchpad/jobs/sheet]]` resolves correctly

## Ingest Pipeline

Raw sources go into `raw/` → ingested via `synapse_mcp` → summary written to `wiki/sources/`.

## Git Workflow

- Commit logical units: don't commit every news-batch individually
- UseConventional commits: `feat:`, `fix:`, `docs:`, `chore:`, `refactor:`
