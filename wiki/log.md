---
updated: 2026-05-13T00:20:36Z
---

# 2026-05-13

## GoodRobot Paperclip → Obsidian Export

**Trigger:** Paperclip LLM Wiki plugin install fails with SQL validation regression (`Plugin migration objects must use fully qualified schema names` despite all SQL being fully qualified).

**Action taken:** Manual export of 14 Paperclip issues to `wiki/projects/goodrobot/`:

- `index.md` — GoodRobot project overview
- `business-concept.md` — Problem statement, TAM, value proposition
- `revenue-model.md` — Pricing tiers, unit economics
- `roadmap.md` — 30-day through 2-year milestones
- `hiring-plan.md` — Org chart, board composition
- `local-lead-gen.md` — Son's validated business (~$2,500/mo)
- `issues-index.md` — Full issue registry

**Entities:**
- `wiki/entities/projects/goodrobot.md` — Company entity page

**Source:** Paperclip API `GET /api/companies/d8634ba3.../issues?limit=50`

**Next:** Watch for plugin fix, or build cron-based sync if plugin remains broken.

---

## Earlier Log Entries

_see git history for earlier entries_

## [2026-05-13 00:20] write

Updated page: wiki/log.md

## [2026-05-13 18:28] ingest | Paperclip Workspaces.md

Ingested raw/Paperclip Workspaces.md into knowledge graph.

Preview: ## Workspaces  When an agent picks up a task that involves working with code or files, it needs a place to do that work — a folder with the right code checked out at the right state, ready for the age...
