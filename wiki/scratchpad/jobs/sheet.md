---
summary: Wiki agent coordination board — open items, skill folder registry, operations in reports/overseer/
tags: [jobs, task-board, overseer]
updated: 2026-05-26
ops_log: wiki/scratchpad/jobs/reports/overseer/
---

# Jobs Sheet — Central Agent Coordination Board

**Overseer**: [[overseer/SKILL.md]]  
**Agents**: [[arxiv/SKILL.md]] · [[researcher/SKILL.md]] · [[ingest/SKILL.md]] · [[librarian/SKILL.md]] · [[librarians-assistant/SKILL.md]] · [[insights/SKILL.md]] · [[news/SKILL.md]] · [[orcaid/SKILL.md]]

---

## Per-Agent Skill Folders

Each agent lives at `wiki/scratchpad/agent-sheets/{agent}/` with progressive disclosure (SKILL.md → references/ → templates/).

| Agent                             | references/                            | templates/                           | carryover                          |
| --------------------------------- | -------------------------------------- | ------------------------------------ | ---------------------------------- |
| [[arxiv/SKILL.md]]                | patterns.md, workflow.md               | report.md, research-brief.md         | [[arxiv/carryover]]                |
| [[researcher/SKILL.md]]           | workflow.md                            | discovery-report.md, gap-analysis.md | [[researcher/carryover]]           |
| [[ingest/SKILL.md]]               | workflow.md                            | ingest-report.md                     | [[ingest/carryover]]               |
| [[librarian/SKILL.md]]            | mcp-tools.md, workflow.md              | audit-report.md                      | [[librarian/carryover]]            |
| [[librarians-assistant/SKILL.md]] | quick-reference.md, workflow.md        | batch-progress.md                    | [[librarians-assistant/carryover]] |
| [[insights/SKILL.md]]             | insight-merge.md, workflow.md          | carryover.md                         | [[insights/carryover]]             |
| [[news/SKILL.md]]                 | rss-queries.md, workflow.md            | headlines-report.md, news-article.md | [[news/carryover]]                 |
| [[orcaid/SKILL.md]]               | execution-mechanisms.md, task-types.md | run-report.md                        | [[orcaid/carryover]]               |

---

## Coordinated Tasking

> ⚠️ **Rule: Only the overseer manages this section.** Open items come from agent carryovers, kanban cards are created by the overseer. Agents write their own carryovers — they do NOT create kanban cards or modify this table.

### Open Items (carryovers → kanban)

|| Item | Source Agent | Kanban ID | Priority | Notes |
|------|-------------|-----------|----------|-------|
| [[namm]] upgrade (ml-evolution source) | researcher | `t_5605291da30d417b` | high | NAMM learned KV cache retention vs Control LLM — complementary? |
| [[continual-learning]] fill (empty stub) | researcher | `t_10d4fed7e6cbb9df` | high | Connects catastrophic-forgetting/MoE/MOP/llm-training |
| [[lora]] expansion (16 lines) | researcher | `t_693879094e4a508a` | med | Well-connected to PEFT and fine-tuning |
### Blocked / Stalled

> None currently — GoodRobot is research-project-1st-attempt (reference OK), .bak files resolved, gbrain/synthesis-layer complete.
| Ebola case count updates | news | `t_a0cd9cc56d2a0d21` | med | 750 suspected cases, South Sudan transmission, thermostable vaccine |
| SpaceX IPO governance clarification | news | `t_bd5eb78392b6ce9c` | med | June 12 listing, Musk voting control, BlackRock $10B |
| Pope Leo XIV encyclical follow-through | news | `t_05c65d368cfa4b1e` | med | 'Magnifica humanitas' — Vatican diplomatic follow-through |
| Bounded memory budget optimization | researcher | — | med | Open from prior cycles — capacity/saturation theme |
| MOP vs fine-tuning boundary | researcher | — | med | Open from prior cycles |
| Schema competition | researcher | — | low | Open from prior cycles |
| Schema competition | researcher | — | low | Open from prior cycles |
| 10 merge candidates (similarity 1.0) | librarian | — | low | agentic-planner ↔ agentic-sequential only is actionable |
| 18 stub concepts batch | librarians-assistant | — | med | 6 Greek-letter + 10 stub cluster |

### Blocked / Stalled

> None currently.

---

## Operations Log

> Internal use — overseer and Ty only. Timestamps from actual job runs, not schedules. Full logs in `reports/overseer/`.

```
2026-05-25 — Restructured agent-sheets/ into progressive-disclosure skill folders
2026-05-26 — Full carryover audit: 8 agents processed
2026-05-26 PM — Overseer audit: librarian/librarians-assistant open items surfaced
```

---

## Logs

```
2026-05-25 — Restructured agent-sheets/ into progressive-disclosure skill folders (SKILL.md → references/ → templates/). Flat .md files removed. All 7 cron jobs updated to new skill names.
2026-05-25 — Central sheet redesigned: overseer owns this sheet, per-agent skill folder tracking, cron skill link registry
2026-05-26 — Full carryover audit: 8 agents processed. arxiv status corrected in_progress→done. 3 researcher open items surfaced (bounded memory, MOP vs fine-tuning, schema competition). 5 news open items tracked. librarian/librarians-assistant findings consolidated. insights blocked by MCP unavailability noted. Open Items table expanded with 5 new rows.
2026-05-26 PM — Overseer audit: librarian last-run corrected 2026-05-26→2026-07-29 (carryover body date used; carryover missing frontmatter updated field). librarians-assistant last-run corrected 2026-05-26→2026-07-30. All open items already on kanban; no new cards created. researcher carryover (Jul 15) stale vs today's date — flagged.
```