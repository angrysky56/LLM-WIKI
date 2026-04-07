---
summary: Markdown knowledge app — the human-readable frontend for the wiki
tags: [tool, knowledge-management, frontend]
updated: 2026-04-07T20:36:11Z
created: 2026-04-07T20:36:11Z
---

# Obsidian

Markdown-based knowledge management application used as the human-facing layer of the [[LLM Wiki Pattern|wiki/sources/llm-wiki-pattern]].

## Role in This System

- Renders the wiki/ directory as an interlinked knowledge base
- Graph view visualizes connections between pages via `[[wikilinks]]`
- Obsidian Web Clipper captures articles as Markdown into raw/
- Git plugin syncs the vault to GitHub for version control and rollback
- Dataview plugin can query YAML frontmatter across pages

## Key Metaphor

From [[Andrej Karpathy]]: "Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase."
