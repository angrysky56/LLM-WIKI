---
summary: kepano's agent skill definitions for Obsidian — markdown, bases, canvas, CLI, and defuddle web extraction
tags: [obsidian, skills, kepano, agent, bases, defuddle, tooling]
updated: 2026-04-11T00:58:29Z
created: 2026-04-11T00:58:29Z
---

# obsidian-skills (kepano)

**Repo:** `/home/ty/Repositories/obsidian-skills`  
**Source:** https://github.com/kepano/obsidian-skills  
**Author:** Steph Ango (kepano), Obsidian CEO

## What It Is

Agent skill definitions (SKILL.md files) teaching AI agents how to work with Obsidian-specific file formats. Follows the [Agent Skills specification](https://agentskills.io/specification) — compatible with Claude Code, Codex CLI, OpenCode.

## Available Skills

| Skill | File type | Use case |
|-------|-----------|----------|
| `obsidian-markdown` | `.md` | Wikilinks, embeds, callouts, properties, Obsidian-flavored syntax |
| `obsidian-bases` | `.base` | Database-like YAML views — table, cards, list, map with filters/formulas |
| `json-canvas` | `.canvas` | Visual node/edge diagrams native to Obsidian |
| `obsidian-cli` | — | Programmatic vault interaction via terminal |
| `defuddle` | — | Clean markdown extraction from web pages (clutter removal) |

## Most Relevant for This System

**`obsidian-bases`** — The `.base` format creates live database views filtered by frontmatter properties. Currently used in this vault:
- `raw-inbox.base` — queue view of unprocessed files in `raw/`

**`obsidian-markdown`** — Canonical reference for Obsidian wikilink syntax, callouts, embeds, properties. Useful when the linter reports issues — check syntax here first.

**`defuddle`** — Could replace or supplement the Obsidian Web Clipper workflow for web content. Strips navigation, ads, and boilerplate before sending to the ingestion pipeline, saving tokens.

## Potential Uses

- Create additional `.base` views: orphaned wiki pages, pages below confidence threshold, recently updated entities
- Use `defuddle` as a pre-processing step before dropping content into `raw/`
- Reference `obsidian-markdown` for correct callout and embed syntax when writing wiki pages

## Connections

- [[obsidian]] — the tool these skills extend
- [[obsidian-cli-skill]] — the CLI skill (also from this repo)
- [[project-synapse]] — wiki adapter as alternative to CLI for agent access
