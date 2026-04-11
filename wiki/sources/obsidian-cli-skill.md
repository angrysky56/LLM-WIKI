---
summary: kepano's Obsidian CLI agent skill — command reference for reading, writing, searching, and managing Obsidian vaults from the terminal
tags: [obsidian, cli, agent, tool, kepano, vault-management]
updated: 2026-04-10T23:14:15Z
created: 2026-04-10T23:14:15Z
---

# Obsidian CLI — Agent Skill Reference

**Source:** https://github.com/kepano/obsidian-skills/blob/main/skills/obsidian-cli/SKILL.md  
**Author:** kepano (Steph Ango, Obsidian CEO)

> Requires Obsidian to be **open and running**. Targets the most recently focused vault by default.

## Key Command Patterns

```bash
# Read / create / append
obsidian read file="My Note"
obsidian create name="New Note" content="# Hello" template="Template" silent
obsidian append file="My Note" content="New line"

# Search
obsidian search query="search term" limit=10

# Daily notes
obsidian daily:read
obsidian daily:append content="- [ ] New task"

# Properties / metadata
obsidian property:set name="status" value="done" file="My Note"

# Tasks & tags
obsidian tasks daily todo
obsidian tags sort=count counts

# Backlinks
obsidian backlinks file="My Note"
```

## File Targeting

- `file=<name>` — resolves like a wikilink (no path/extension needed)
- `path=<vault-relative-path>` — exact path e.g. `wiki/concepts/para.md`
- No target → operates on active file

## Vault Targeting

```bash
obsidian vault="LLM-WIKI" search query="embedding"
```

## Useful Flags

| Flag | Effect |
|------|--------|
| `silent` | Prevents file from opening in Obsidian |
| `overwrite` | Replaces existing content on create |
| `--copy` | Copies output to clipboard |
| `total` | Returns count on list commands |

## Plugin Dev Cycle

```bash
obsidian plugin:reload id=my-plugin
obsidian dev:errors
obsidian dev:screenshot path=screenshot.png
obsidian eval code="app.vault.getFiles().length"
```

## Relevance to Synapse

The CLI gives agents a **direct read/write interface to any open vault** — an alternative to Desktop Commander file operations. Could be used to trigger Obsidian-native actions (templates, daily notes, backlink queries) that the wiki adapter doesn't currently expose.

## Connections

- [[llm-wiki-pattern]] — primary vault this CLI operates on
- [[project-synapse]] — Synapse wiki adapter vs. CLI as complementary interfaces
- [[obsidian-para-byarbrough]] — CLI can manage PARA folders natively
