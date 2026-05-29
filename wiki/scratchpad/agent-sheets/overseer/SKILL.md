---
name: wiki-overseer
description: "Wiki overseer context document — agent role, owned files, and coordination protocol. Operational instructions live in the hermes-level wiki-overseer skill."
updated: 2026-05-27
created_by: agent
---

# Wiki Overseer — Context Document


## Role

The overseer is the **primary coordinator across all wiki agents**. It:

1. Runs `scripts/preflight.py` to gather ground truth from the scheduler and carryovers
2. Reads all agent carryovers to find open items
3. Surfaces new open items to the Hermes kanban board (cross-agent items, overflow from individual agents)
4. Writes a daily report to `reports/overseer/`
5. Delivers a summary to Discord

**Note**: Individual agents also surface their own open items directly to kanban via the `kanban-review` skill (loaded alongside every agent cron job). The "overseer creates kanban cards" is not exclusive — agents *should* also create tickets for their own open items. The overseer coordinates and manages the board, but individual agents are active kanban participants.

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
5. **All agents also use `kanban-review`** (loaded alongside their agent skill in every cron job) to surface their open items directly to kanban after each run. This is the correct pattern — both the overseer AND individual agents create kanban cards. The "only overseer" rule means the overseer is the *coordinator* who also surfaces cross-agent items and manages the board; it does NOT mean agents are banned from creating their own kanban tickets.

## Related
- [[wiki/index]]
- [[scratchpad/agent-sheets/overseer/skill]]
- [[skill]]
- [[librarian/skill.md]]
- [[agent-sheets/overseer/skill.md]]
- [[orcaid/skill.md]]
- [[ingest/skill.md]]
- [[librarians-assistant/skill.md]]
- [[insights/skill.md]]
- [[news/skill.md]]
- [[researcher/skill.md]]
- [[arxiv/skill.md]]

- [[overseer/skill.md]]

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
