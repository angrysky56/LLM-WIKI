---
summary: Markdown knowledge app — the human-readable frontend for the wiki
tags: [tool, knowledge-management, frontend, obsidian]
updated: 2026-04-10T23:18:23Z
---

# Obsidian

Markdown-based knowledge management application used as the human-facing layer of the [[llm-wiki-pattern]].

## Role in This System

- Renders the `wiki/` directory as an interlinked knowledge base
- Graph view visualizes connections between pages via wikilinks
- Obsidian Web Clipper captures articles as Markdown into `raw/`
- Git plugin syncs the vault to GitHub for version control and rollback
- Dataview plugin can query YAML frontmatter across pages

## Key Interfaces

| Interface | Purpose |
|-----------|---------|
| Obsidian GUI | Human reading, graph exploration, manual editing |
| [[obsidian-cli-skill|Obsidian CLI]] | Agent/terminal read-write without opening the GUI |
| [[project-synapse]] wiki adapter | Structured CRUD via MCP tools |

## Key Metaphor

From [[andrej-karpathy]]: "Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase."

## Connections

- [[neo4j]] — graph backend; Obsidian is the human-readable complement
- [[para-methodology]] — organizational philosophy applicable to vault structure
- [[obsidian-cli-skill]] — programmatic access to running Obsidian instance
