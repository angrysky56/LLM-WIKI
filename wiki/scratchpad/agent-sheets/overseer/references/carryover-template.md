# Carryover Template

All wiki agents MUST use this format for their `carryover.md`. The overseer's
preflight script parses these files programmatically — inconsistent formats
cause parsing failures.

## Template

```markdown
---
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: carryover
summary: "One-line summary of what happened this cycle"
tags: [{agent-name}, carryover]
---

# {Agent Name} Carryover — YYYY-MM-DD

## What Was Done
- Completed item 1
- Completed item 2

## What Remains
- [ ] Open item 1
- [ ] Open item 2 (needs Ty input)

## Kanban Status
- [x] kanban: YYYY-MM-DD — {title of item surfaced to kanban}
  - ID: t_{hex}
- [ ] Not yet surfaced: {pending item}
```

## Field Requirements

### Frontmatter (REQUIRED)

| Field | Required | Notes |
|-------|----------|-------|
| `created` | Yes | Date carryover was first created |
| `updated` | Yes | Date of THIS run — **must be today's date** |
| `type` | Yes | Always `carryover` |
| `summary` | Yes | One-line summary — the overseer reads this |
| `tags` | Yes | Must include agent name and `carryover` |

### Sections

| Section | Required | Format |
|---------|----------|--------|
| `## What Was Done` | Yes | Bullet list of completed items |
| `## What Remains` | Yes | Checklist `- [ ]` format for open items |
| `## Kanban Status` | Optional | Tracks which items are already on kanban |

## Related
- [[wiki/index]]
- [[scratchpad/agent-sheets/overseer/references/carryover-template]]

- [[carryover-template]]

## Rules

1. **`updated` must be today's date** — not a future date, not yesterday. This is the
   overseer's primary signal for "when did this agent last run?"

2. **Open items use `- [ ]` format** — the preflight script extracts these programmatically.
   Free-text paragraphs in the Open section are ignored.

3. **One carryover per agent** — overwrite, don't append. The carryover is Markovian state
   (only the latest matters).

4. **summary field is machine-read** — keep it to one line, no markdown, no wikilinks.

5. **Tags MUST include the agent name** — `[researcher, carryover]`, `[librarian, carryover]`, etc.
