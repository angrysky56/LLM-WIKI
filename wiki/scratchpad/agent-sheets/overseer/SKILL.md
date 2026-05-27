---
name: wiki-overseer
description: "Wiki overseer context document — agent role, owned files, and coordination protocol. Operational instructions live in the hermes-level wiki-overseer skill."
updated: 2026-05-27
created_by: agent
---

# Wiki Overseer — Context Document

> **Operational instructions are in the hermes-level `wiki-overseer` skill.**
> This file describes the overseer's role and owned resources. It is NOT a skill to execute.

## Role

The overseer is the **only agent that coordinates across all wiki agents**. It:

1. Runs `scripts/preflight.py` to gather ground truth from the scheduler and carryovers
2. Reads all agent carryovers to find open items
3. Surfaces new open items to the Hermes kanban board
4. Writes a daily report to `reports/overseer/`
5. Delivers a summary to Discord

## Owned Files

| File | Path | Purpose |
|------|------|---------|
| Pre-flight script | `overseer/scripts/preflight.py` | Ground-truth data gathering |
| Carryover | `overseer/carryover.md` | Overseer's own open items and state |
| Daily reports | `jobs/reports/overseer/overseer-YYYY-MM-DD.md` | Cycle logs |
| This context doc | `overseer/SKILL.md` | Role description (not executable) |

## Coordination Protocol

1. **Agents write their own carryovers** — each agent is responsible for updating its `carryover.md` after every run
2. **Overseer reads all carryovers** — parses open items from `## What Remains` or `## Open` sections
3. **Overseer creates kanban cards** — one card per open item, checked for duplicates
4. **Overseer writes report** — summarizes agent state and new kanban cards
5. **Individual agents do NOT create kanban cards** — only the overseer does this

## Agent Registry

| Agent | Schedule | Carryover Path |
|-------|----------|----------------|
| insights | `0 6 * * *` | `insights/carryover.md` |
| ingest | `30 6 * * *` | `ingest/carryover.md` |
| news | `30 7 * * *` | `news/carryover.md` |
| researcher | `0 8 * * *` | `researcher/carryover.md` |
| arxiv | `10 8 * * *` | `arxiv/carryover.md` |
| librarian | `20 8 * * *` | `librarian/carryover.md` |
| librarians-assistant | `40 8 * * *` | `librarians-assistant/carryover.md` |
| overseer | `0 9 * * *` | `overseer/carryover.md` |
| orcaid | PAUSED | `orcaid/carryover.md` |
