---
summary: Wiki agent registry — static reference for agent coordination
tags: [jobs, registry, overseer]
updated: 2026-05-27
---

# Wiki Agent Registry

**Overseer**: [[overseer/SKILL.md]]  
**Live state**: `wiki/scratchpad/jobs/reports/overseer/` (daily reports)  
**Kanban board**: `hermes kanban list` (open tasks)

---

## Agents

| Agent | Schedule | Skill (hermes) | Carryover | Reports |
|-------|----------|----------------|-----------|---------|
| insights | `0 6 * * *` | `insights-agent` | [[insights/carryover]] | `reports/insights/` |
| ingest | `30 6 * * *` | `ingest-agent` | [[ingest/carryover]] | `reports/ingest/` |
| news | `30 7 * * *` | `news-agent` | [[news/carryover]] | `reports/news/` |
| researcher | `0 8 * * *` | `researcher-agent` | [[researcher/carryover]] | `reports/researcher/` |
| arxiv | `10 8 * * *` | `arxiv-agent` | [[arxiv/carryover]] | `reports/arxiv/` |
| librarian | `20 8 * * *` | `librarian-agent` | [[librarian/carryover]] | `reports/librarian/` |
| librarians-assistant | `40 8 * * *` | `librarians-assistant-agent` | [[librarians-assistant/carryover]] | `reports/librarians-assistant/` |
| overseer | `0 9 * * *` | `wiki-overseer` | [[overseer/carryover]] | `reports/overseer/` |
| orcaid | PAUSED | `orcaid` | [[orcaid/carryover]] | `reports/orcaid/` |

---

## Skill Folder Structure

Each agent lives at `wiki/scratchpad/agent-sheets/{agent}/`:

```
{agent}/
├── SKILL.md          # Agent sheet (role, workflow, tools)
├── carryover.md      # Markovian state (agent writes after each run)
├── references/       # Patterns, templates, tool guides
└── scripts/          # Helper scripts
```

---

## Coordination Rules

1. **Agents write their own carryovers** — final step of every run
2. **Overseer reads all carryovers** — runs preflight.py then surfaces open items to kanban
3. **Kanban is the work queue** — `hermes kanban list` shows all open tasks
4. **This file is a static registry** — it does NOT track live state (that's in overseer reports and kanban)

---

## Quick Reference

```bash
# List all agent carryovers
ls wiki/scratchpad/agent-sheets/*/carryover.md

# View overseer's latest report
ls -t wiki/scratchpad/jobs/reports/overseer/ | head -1

# View kanban board
hermes kanban list

# Run preflight manually
python3 wiki/scratchpad/agent-sheets/overseer/scripts/preflight.py
```