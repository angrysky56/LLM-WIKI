---
summary: Central agent coordination board — overseer-managed, per-agent skill folders
tags: [jobs, task-board, overseer]
updated: 2026-05-25
---

# Jobs Sheet — Central Agent Coordination Board

**Overseer**: [[overseer/SKILL.md]]  
**Agents**: [[arxiv/SKILL.md]] · [[researcher/SKILL.md]] · [[ingest/SKILL.md]] · [[librarian/SKILL.md]] · [[librarians-assistant/SKILL.md]] · [[insights/SKILL.md]] · [[news/SKILL.md]] · [[orcaid/SKILL.md]]

---

## Agent State Overview

| Agent | Cron ID | Schedule | Last Run | Last Status | Next Run |
|-------|---------|----------|----------|--------------|----------|
| [[arxiv/SKILL.md]] | `72599f850df2` | 08:20 | 2026-05-26 | **in_progress** | — |
| [[researcher/SKILL.md]] | `8ea33cfa560a` | 08:00 | 2026-05-26 | **done** | — |
| [[ingest/SKILL.md]] | `c838e81a1496` | 06:30 | — | — | — |
| [[librarian/SKILL.md]] | `48a3a009a820` | 08:20 | 2026-05-26 | **done** | — |
| [[librarians-assistant/SKILL.md]] | `385aa0819a57` | 08:40 | — | — | — |
| [[insights/SKILL.md]] | `723e76246970` | 06:00 | — | — | — |
| [[news/SKILL.md]] | `eaaa6bdc8503` | 07:30 | — | — | — |
| [[orcaid/SKILL.md]] | — | PAUSED | — | — | — |

**Kanban Review**: `0a34e742931a` · [[librarians-assistant/SKILL.md|kanban-review]] · schedule 08:30 · on-demand trigger supported

---

## Per-Agent Skill Folders

Each agent lives at `wiki/scratchpad/agent-sheets/{agent}/` with progressive disclosure (SKILL.md → references/ → templates/).

| Agent | SKILL.md | references/ | templates/ | carryover |
|-------|----------|-------------|-----------|-----------|
| [[arxiv/SKILL.md]] | 43 lines | patterns.md, workflow.md | report.md, research-brief.md | [[arxiv/carryover]] |
| [[researcher/SKILL.md]] | 40 lines | workflow.md | discovery-report.md, gap-analysis.md | [[researcher/carryover]] |
| [[ingest/SKILL.md]] | 41 lines | workflow.md | ingest-report.md | [[ingest/carryover]] |
| [[librarian/SKILL.md]] | 39 lines | mcp-tools.md, workflow.md | audit-report.md | [[librarian/carryover]] |
| [[librarians-assistant/SKILL.md]] | 42 lines | quick-reference.md, workflow.md | batch-progress.md | [[librarians-assistant/carryover]] |
| [[insights/SKILL.md]] | 45 lines | insight-merge.md, workflow.md | carryover.md | [[insights/carryover]] |
| [[news/SKILL.md]] | 48 lines | rss-queries.md, workflow.md | headlines-report.md, news-article.md | [[news/carryover]] |
| [[orcaid/SKILL.md]] | 46 lines | execution-mechanisms.md, task-types.md | run-report.md | [[orcaid/carryover]] |

---

## Coordinated Tasking

### Open Items (carryovers → kanban)

| Item | Source Agent | Kanban ID | Priority | Notes |
|------|-------------|-----------|----------|-------|
| [[namm]] upgrade (ml-evolution source) | researcher | `t_5605291da30d417b` | high | NAMM learned KV cache retention vs Control LLM — complementary? |
| [[continual-learning]] fill (empty stub) | researcher | `t_10d4fed7e6cbb9df` | high | Connects catastrophic-forgetting/MoE/MOP/llm-training |
| [[lora]] expansion (16 lines) | researcher | `t_693879094e4a508a` | med | Well-connected to PEFT and fine-tuning |
| GoodRobot duality — Ty decision | librarian | `t_7c481cbf1017a19f` | med | entities/projects/goodrobot.md vs projects/projects 1/goodrobot.md |
| 44 .bak files — Ty decision | librarian | `t_df8558e119306ce2` | med | Delete all or selective restore? |
| Index 4 insight pages + episodic memory | insights | `t_44f165d523d34fff` | med | titans-memory-architecture, para-system-cluster, oee-knowledge-cluster, francesca-albanese-sanctions |
| Ebola case count updates | news | `t_a0cd9cc56d2a0d21` | med | 750 suspected cases, South Sudan transmission, thermostable vaccine |
| SpaceX IPO governance clarification | news | `t_bd5eb78392b6ce9c` | med | June 12 listing, Musk voting control, BlackRock $10B |
| Pope Leo XIV encyclical follow-through | news | `t_05c65d368cfa4b1e` | med | 'Magnifica humanitas' — Vatican diplomatic follow-through |

### Blocked / Stalled

| Agent | Blocked By | Since | Notes |
|-------|-----------|-------|-------|
| — | | | |

---

## Cron Skill Links (updated 2026-05-25)

All 8 agent cron jobs now reference the new skill folder names:

| Cron ID | Agent | Skills |
|---------|-------|--------|
| `8ea33cfa560a` | researcher | `["researcher", "kanban-review"]` |
| `72599f850df2` | arxiv | `["arxiv", "kanban-review"]` |
| `eaaa6bdc8503` | news | `["news", "kanban-review"]` |
| `c838e81a1496` | ingest | `["ingest", "kanban-review"]` |
| `48a3a009a820` | librarian | `["librarian", "kanban-review"]` |
| `385aa0819a57` | librarians-assistant | `["librarians-assistant", "kanban-review"]` |
| `723e76246970` | insights | `["insights", "kanban-review"]` |
| `0a34e742931a` | kanban-review | `["kanban-review"]` |
| `3a3811943ca9` | kanban-dispatcher | `["kanban-dispatcher"]` |

---

## Logs

```
2026-05-25 — Restructured agent-sheets/ into progressive-disclosure skill folders (SKILL.md → references/ → templates/). Flat .md files removed. All 7 cron jobs updated to new skill names.
2026-05-25 — Central sheet redesigned: overseer owns this sheet, per-agent skill folder tracking, cron skill link registry
```