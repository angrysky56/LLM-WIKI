---
name: arxiv
description: arXiv paper discovery — select top 3 significant papers, research via subagents, ingest to wiki, deliver report.
tags:
  - arxiv
  - research
  - paper-discovery
  - daily
triggers:
  - cron: 20 8 * * *
  - manual: delegate_task
updated: 2026-05-25
created_by: agent
---

# arxiv — ArXiv Research Curator

Discover, select, and research the top 3 arXiv papers or others if the same papers are found or your task requires it. Deliver a summary report with wiki ingestion and cross-links to existing knowledge threads.

## See Also

- `references/workflow.md` — 6-phase discovery and research workflow
- `references/patterns.md` — MCP→curl fallback, subagent verification, PDF extraction
- `templates/research-brief.md` — paper selection brief
- `templates/report.md` — final daily report

## Quick Start

1. Load the `arxiv` skill
2. Run discovery via arXiv API (Phase 1)
3. Select top 3 by significance (Phase 2)
4. Download PDFs via curl — NOT MCP (Phase 3)
5. Delegate research to subagents (Phase 4)
6. Assemble and deliver report (Phase 5)

## Wiki Operations
- **Tools:** `query_knowledge` (check existing coverage), `wiki_write_page` (paper summaries), `wiki_update_index` (after ingest)
- **Constraint:** Check wiki with `query_knowledge` before ingesting — if topic covered, link to existing page instead of duplicating.
- **CRITICAL CONSTRAINT:** DO NOT write or run ad-hoc Python scripts (e.g. `kanban_upsert.py`, `fetch.py`, etc.). Use the standard `mcp-project-synapse` tools or bash commands (like `curl`) exclusively. All Kanban updates are handled by the overseer, not individual agents.

## Critical Paths

- **PDF storage**: `/home/ty/Documents/paper-research/{arxiv_id}v{version}.pdf`
- **Wiki paper pages**: `wiki/sources/papers/{slug}.md`
- **Daily reports**: `wiki/scratchpad/jobs/reports/arxiv/arxiv-YYYY-MM-DD-top-papers.md`
- **Carryover**: `wiki/scratchpad/agent-sheets/arxiv/carryover.md`

## FINAL STEP — Update Carryover (REQUIRED)

After completing paper ingestion, write updated carryover to `wiki/scratchpad/agent-sheets/arxiv/carryover.md`. Include:
- Papers processed this cycle (arxiv_id + title + key finding)
- Pages created in wiki/sources/papers/ (slug)
- Open items for next cycle
- Last run timestamp

## Quality Standards

- Select for **significance**, not recency
- Wiki pages must cross-link to existing concepts (no orphans)
- 429 from MCP → switch to curl immediately
- Subagent completion must be verified (file exists + grep check)