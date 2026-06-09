---
created: 2026-06-09T10:54:00Z
updated: 2026-06-09T10:54:00Z
type: synthesis
status: active
---

## CarryoverState

### Established
- **[preflight-bug]** Known HERMES_HOME bug persists. Fallback procedure (direct jobs.json read + kanban_list MCP) works reliably. Report written to `reports/2026-06-09.md`.
- **[cron-paused]** All 8 cron jobs in `enabled=False` (paused) state. All jobs ran successfully on 2026-06-09 except `llm-wiki-raw-ingest` (last run 2026-06-07).
- **[kanban-clear]** Board has 0 open tasks. No blocked or ready items. Latest completion: insights stranded-insights publish.
- **[arxiv-open]** 4 optional synthesis items in arxiv's carryover. No kanban cards spawned — optional work, agent running fine.

### Open
- **[carryover-repopulate]** 3 agents lack structured carryover: news (frontmatter only, no open items), ingest (no frontmatter), librarian (no frontmatter). Need to prompt re-population next cycle if unchanged.
- **[orcaid]** 15 days stale. Paused in both cron and carryover. Re-evaluate if needed.

### Heading
- **[next-cycle]** Check if cron jobs remain paused. Re-check empty carryovers. Run wiki_lint if tool output is retrievable.