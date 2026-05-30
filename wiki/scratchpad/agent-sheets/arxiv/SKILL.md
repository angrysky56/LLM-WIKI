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

1. **Layer 2 Load**: Read `wiki/scratchpad/jobs/sheet.md` and `wiki/scratchpad/agent-sheets/arxiv/carryover.md`
2. **Layer 1 Start**: Initialize or clear `vault.md` to act as your episodic scratchpad for this session
3. Run discovery via arXiv API (Phase 1), logging findings to `vault.md`
4. Select top 3 by significance (Phase 2)
5. Download PDFs via curl — NOT MCP (Phase 3)
6. Delegate research to subagents (Phase 4)
7. Assemble and deliver report (Phase 5)
8. **MOP Compression**: Compress `vault.md` into `carryover.md` (Layer 1 → Layer 2)

## Wiki Operations
- **Tools:** `query_knowledge` (check existing coverage), `wiki_write_page` (paper summaries), `wiki_update_index` (after ingest)
- **Constraint:** Check wiki with `query_knowledge` before ingesting — if topic covered, link to existing page instead of duplicating.
- **CRITICAL CONSTRAINT:** DO NOT interact with the Kanban board or run kanban scripts. Output open items as `- [ ]` in the `## What Remains` section of your `carryover.md`. The overseer will create Kanban tickets and assign them to you in `jobs/sheet.md`. Use the standard `mcp-project-synapse` tools or bash commands (like `curl`) exclusively.

## Critical Paths

- **PDF storage**: `/home/ty/Documents/paper-research/{arxiv_id}v{version}.pdf`
- **Wiki paper pages**: `wiki/sources/papers/{slug}.md`
- **Daily reports**: `wiki/scratchpad/jobs/reports/arxiv/arxiv-YYYY-MM-DD-top-papers.md`
- **Carryover**: `wiki/scratchpad/agent-sheets/arxiv/carryover.md`

## FINAL STEP — MOP Compression (Layer 1 → Layer 2)

After completing paper ingestion, read your `vault.md` (Episodic Trace) and compress it into your strict `wiki/scratchpad/agent-sheets/arxiv/carryover.md` (Semantic State), adhering to the ~512 token bound. Include:
- Papers processed this cycle (arxiv_id + title + key finding)
- Pages created in wiki/sources/papers/ (slug)
- Open items for next cycle (as `- [ ]` checklist)
- Last run timestamp

Once compressed, clear or archive your `vault.md` so the next session starts fresh.

## Quality Standards

- Select for **significance**, not recency
- Wiki pages must cross-link to existing concepts (no orphans)
- 429 from MCP → switch to curl immediately
- Subagent completion must be verified (file exists + grep check)