---
title: "obsidian-skills/skills/obsidian-cli/SKILL.md at main"
source: "https://github.com/kepano/obsidian-skills/blob/main/skills/obsidian-cli/SKILL.md"
author:
published:
created: 2026-04-10
description: "Agent skills for Obsidian. Teach your agent to use Markdown, Bases, JSON Canvas, and use the CLI. - obsidian-skills/skills/obsidian-cli/SKILL.md at main · kepano/obsidian-skills"
tags:
  - "clippings"
---
| name | obsidian-cli |
| --- | --- |
| description | Interact with Obsidian vaults using the Obsidian CLI to read, create, search, and manage notes, tasks, properties, and more. Also supports plugin and theme development with commands to reload plugins, run JavaScript, capture errors, take screenshots, and inspect the DOM. Use when the user asks to interact with their Obsidian vault, manage notes, search vault content, perform vault operations from the command line, or develop and debug Obsidian plugins and themes. |

## Obsidian CLI

Use the `obsidian` CLI to interact with a running Obsidian instance. Requires Obsidian to be open.

## Command reference

Run `obsidian help` to see all available commands. This is always up to date. Full docs: [https://help.obsidian.md/cli](https://help.obsidian.md/cli)

## Syntax

**Parameters** take a value with `=`. Quote values with spaces:

```
obsidian create name="My Note" content="Hello world"
```

**Flags** are boolean switches with no value:

```
obsidian create name="My Note" silent overwrite
```

For multiline content use `\n` for newline and `\t` for tab.

## File targeting

Many commands accept `file` or `path` to target a file. Without either, the active file is used.

- `file=<name>` — resolves like a wikilink (name only, no path or extension needed)
- `path=<path>` — exact path from vault root, e.g. `folder/note.md`

## Vault targeting

Commands target the most recently focused vault by default. Use `vault=<name>` as the first parameter to target a specific vault:

```
obsidian vault="My Vault" search query="test"
```

## Common patterns

```
obsidian read file="My Note"
obsidian create name="New Note" content="# Hello" template="Template" silent
obsidian append file="My Note" content="New line"
obsidian search query="search term" limit=10
obsidian daily:read
obsidian daily:append content="- [ ] New task"
obsidian property:set name="status" value="done" file="My Note"
obsidian tasks daily todo
obsidian tags sort=count counts
obsidian backlinks file="My Note"
```

Use `--copy` on any command to copy output to clipboard. Use `silent` to prevent files from opening. Use `total` on list commands to get a count.

## Plugin development

### Develop/test cycle

After making code changes to a plugin or theme, follow this workflow:

1. **Reload** the plugin to pick up changes:
	```
	obsidian plugin:reload id=my-plugin
	```
2. **Check for errors** — if errors appear, fix and repeat from step 1:
	```
	obsidian dev:errors
	```
3. **Verify visually** with a screenshot or DOM inspection:
	```
	obsidian dev:screenshot path=screenshot.png
	obsidian dev:dom selector=".workspace-leaf" text
	```
4. **Check console output** for warnings or unexpected logs:
	```
	obsidian dev:console level=error
	```

### Additional developer commands

Run JavaScript in the app context:

```
obsidian eval code="app.vault.getFiles().length"
```

Inspect CSS values:

```
obsidian dev:css selector=".workspace-leaf" prop=background-color
```

Toggle mobile emulation:

```
obsidian dev:mobile on
```

Run `obsidian help` to see additional developer commands including CDP and debugger controls.