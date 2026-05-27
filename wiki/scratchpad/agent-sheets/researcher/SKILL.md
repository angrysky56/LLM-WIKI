---
name: researcher
description: "Daily wiki knowledge discovery — gap analysis, new topic research, cross-link enforcement, deliver discovery report. Schedule: 08:10 AM."
tags: [research, discovery, knowledge-graph, daily]
triggers:
  - cron: "10 8 * * *"
  - manual: delegate_task
updated: 2026-05-25
created_by: agent
---

# researcher — Wiki Knowledge Discovery Agent

Identify gaps in the LLM-WIKI knowledge graph and research new topics to fill those gaps. Default focus: AI/ML architecture, reasoning systems, agent frameworks, knowledge graph methodologies.

## See Also

- `references/workflow.md` — 6-step discovery workflow
- `templates/discovery-report.md` — discovery report format
- `templates/gap-analysis.md` — gap analysis output format

## Quick Start

1. Load the `researcher` skill
2. Read the jobs sheet for Ty-assigned focus areas
3. Run gap analysis on the wiki
4. Research and write new pages or update existing
5. Deliver discovery report
6. Update carryover

## Critical Paths

- **Wiki root**: `/home/ty/Documents/LLM-WIKI`
- **Discovery reports**: `wiki/scratchpad/jobs/reports/researcher/discovery-YYYY-MM-DD.md`
- **Carryover**: `wiki/scratchpad/agent-sheets/researcher/carryover.md`

## Wiki Operations
- **Tools:** `query_knowledge` (gap analysis), `wiki_search` (find related pages), `wiki_write_page` (new/update pages), `wiki_update_index` (after changes)
- **Constraint:** Check wiki first via `query_knowledge` — if concept exists, update it. Only research external for gaps.

## Quality Standards

- Write in your own voice — not generic AI filler
- Each concept page: definition, relevance, connections, open questions
- Cite sources; don't duplicate existing content