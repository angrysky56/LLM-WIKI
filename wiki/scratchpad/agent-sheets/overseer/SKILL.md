---
name: wiki-overseer
description: "Wiki overseer context document — agent role, owned files, and coordination protocol. Operational instructions live in the hermes-level wiki-overseer skill."
updated: 2026-05-27
created_by: agent
---

# Wiki Overseer — Context Document

wiki/concepts/agentic-hierarchy.md

## Role

The overseer is the **primary coordinator across all wiki agents**. It acts as the central Kanban manager and assigns tasks. It:

1. Runs `scripts/preflight.py` to gather ground truth from the scheduler, agent carryovers, and kanban.db
2. Creates Kanban cards for new open items found in agent carryovers (`## What Remains` -> `- [ ]`)
3. Triages the Kanban board and assigns tasks to specific agents by writing to `wiki/scratchpad/jobs/sheet.md`
4. Writes a daily report to `reports/overseer/`
5. Delivers a summary to Discord

## Owned Files

| File              | Path                                           | Purpose                             |
| ----------------- | ---------------------------------------------- | ----------------------------------- |
| Pre-flight script | `overseer/scripts/preflight.py`                | Ground-truth data gathering         |
| Carryover         | `overseer/carryover.md`                        | Overseer's own open items and state |
| Daily reports     | `jobs/reports/overseer/overseer-YYYY-MM-DD.md` | Cycle logs                          |
| This context doc  | `overseer/SKILL.md`                            | Role description (not executable)   |

## Coordination Protocol

1. **Layer 2 Load**: Agents read `jobs/sheet.md` and their `carryover.md` at start.
2. **Layer 1 Start**: Agents initialize `vault.md` for their session trace.
3. **MOP Compression**: At session end, agents compress their `vault.md` into their `carryover.md` (Layer 1 → Layer 2).
4. **Overseer Sync**: Overseer reads all `carryover.md` files, parsing open items programmatically via `preflight.py`.
5. **Overseer Kanban**: Overseer creates kanban cards for new items, acting as the sole writer to the board.
6. **Overseer Assigns Tasks**: Overseer triages Kanban and writes assignments to `wiki/scratchpad/jobs/sheet.md` for agents to pick up next cycle.

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

| Agent                | Carryover Path                      |
| -------------------- | ----------------------------------- |
| insights             | `insights/carryover.md`             |
| ingest               | `ingest/carryover.md`               |
| news                 | `news/carryover.md`                 |
| researcher           | `researcher/carryover.md`           |
| arxiv                | `arxiv/carryover.md`                |
| librarian            | `librarian/carryover.md`            |
| librarians-assistant | `librarians-assistant/carryover.md` |
| overseer             | `overseer/carryover.md`             |
