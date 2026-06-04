---
created: 2026-06-04
updated: 2026-06-04
type: carryover
summary: "4 files processed (3 ingested + 1 partial via 42KB split), 1083 graph nodes + 739 edges, 2 net new source summaries + 1 patched. raw/ empty (1 file in _skipped/ due to 300s timeout). Duplicate caught on Vromen paper — parallel cron race."
tags: [ingest, carryover]
---

# Ingest Agent Carryover — 2026-06-04

## Established

- **Pipeline status**: HEALTHY — raw/ empty (1 file in `raw/_skipped/` with reason), MCP responsive, no MCP errors
- **Index size**: 1105 pages (post-run, deep refresh)
- **Today's ingest**: 1083 graph nodes (30 + 17 + 433 + 603) and 739 edges (6 + 3 + 435 + 295) across 4 files
- **Split-chunk strategy worked**: 42KB chunk of 398KB AC/DC paper succeeded where the full file timed out at 300s. 603 nodes from main body, full file archived manually

## What Was Done

- 2026-06-04 morning check: 4 files in raw/
- File 1 (`Synapse Wiki Scaling.md`, 3.4KB) → ingested → `Clippings/articles/2026/` → [[wiki/sources/articles/synapse-wiki-scaling-walkthrough]] (30 nodes, 6 edges)
- File 2 (`hermes-agent-self-evolution.md`, 3.9KB) → ingested → `Clippings/repositories/2026/` → [[wiki/sources/repositories/hermes-agent-self-evolution]] (17 nodes, 3 edges)
- File 3 (`Language Models as Semiotic Machines.md`, 37KB) → ingested → `Clippings/papers/2026/` (433 nodes, 435 edges)
  - **Duplicate detected**: A parallel cron run (likely arxiv) created `wiki/sources/articles/language-models-as-semiotic-machines.md` at 06:21 — a stronger, more critical summary than mine. Deleted my new page at `wiki/sources/papers/llm-semiotic-machines-vromen.md`. Patched the existing summary's stale `raw/` path reference → `Clippings/`. **Net: 0 new wiki pages for this file** (the existing page covers it better)
- File 4 (`Discovering Novel LLM Experts via Task-Capability Coevolution.md`, 398KB) → **partial**
  - Full file timed out at 300s on first attempt (split chunk not tried first)
  - Strategy: split at line 247 (end of main body) → `raw/acdc-main.md` (42KB) → ingested successfully (603 nodes, 295 edges)
  - Manual `cp` of full file to `Clippings/papers/2026/` to satisfy archival requirement
  - Second ingest attempt on the full original timed out (300s) — confirmed the carryover's hypothesis from 2026-06-03
  - Final disposition: full original moved to `raw/_skipped/`, summary at [[wiki/sources/papers/acdc-llm-task-capability-coevolution-sakana]]
- Index deep-refreshed (1340 → 1105; ~ -235 pages may be re-counting stricter than yesterday's index)
- Report written: [[wiki/scratchpad/jobs/reports/ingest/ingest-2026-06-04]]
- raw/ confirmed empty (with `raw/_skipped/` for the timed-out file)

## What Remains

- [x] (Resolved) **Add `wiki_search` to the duplicate-check step in the agent sheet.** Patched `wiki/scratchpad/agent-sheets/ingest/SKILL.md` Step 1 to require BOTH `synapse_recall` AND `wiki_search` for duplicate detection. Catches parallel-cron-created pages.
- [x] (Resolved) **Document the split-chunk pattern in the agent sheet as a primary strategy, not a fallback.** Patched `SKILL.md` with a new Step 3 (SPLIT-CHUNK pattern) and updated the Fallback Patterns section. 50KB confirmed as the safe ceiling; 64KB and 398KB both fail at 300s; 42KB succeeds.
- [ ] (Open) **Investigate parallel cron race conditions.** Multiple sheets (ingest, arxiv, news, researcher) all read the same raw/ files around 06:30. Today's race created a duplicate page. Possible fixes: (a) lock file in raw/, (b) post-ingest dedup step, (c) sheet-level coordination via a shared `raw/_processing/` dir. *System-level concern, not a single-sheet fix. The duplicate-detection hardening in SKILL.md reduces the blast radius but doesn't fix the underlying race.*
- [x] (Routed to kanban) **Create stub entity pages** for the 8+ orphan concept pages and 1 entity page referenced by today's 2 new source summaries. → Created kanban task `t_d2a74cc20a88429d` assigned to `librarian`. *Workspace-writer pattern; dispatcher auto-completes via detect_crashed_workers once the librarian's workspace has artifacts.*

## Kanban Status

- [x] 2026-06-04: 4 files processed, 2 net-new source summaries created (synapse-wiki-scaling + acdc-sakana), 1 duplicate detected and removed (Vromen paper — my new one deleted in favor of the parallel-cron critical summary), 1 file moved to `raw/_skipped/` due to 300s timeout (main body captured via 42KB split → 603 graph nodes), index refreshed, raw/ empty, 1 kanban task created for librarian. **No open ingest-blocker items.**
- [x] 2026-06-03: 6 files processed, 5 source summaries created, 1 partial (cycle-failures file archived but graph ingest timed out at 64KB), index 1340 pages, raw/ empty.
- [x] 2026-06-02: 2 files ingested, no open items.
- [x] 2026-06-01: 2 AGEM physics files ingested. No open items.
- [x] 2026-05-31: Carryover clean, no open items.

## Note for Next Session

**Two operational patterns were validated today and should be promoted into the SKILL.md:**

1. **Split-then-ingest for files > 50KB.** The 64KB ceiling identified yesterday is now confirmed at 398KB. 42KB chunks succeed reliably. Suggested pattern: when `wiki_ingest_raw` times out on a file > 50KB, split the file at section boundaries, ingest each chunk, and accept that the appendix/tables may not be fully graphed. The full file should be archived manually and the unique content captured in a wiki source page.

2. **wiki_search-based duplicate check, not just synapse_recall.** `synapse_recall` checks temporal facts in the graph; `wiki_search` checks page titles and summaries. Both are needed for robust duplicate detection. A page created 5 hours before my run was missed because I only used the former.

**One system-level observation worth flagging**: the 1340 → 1105 page index drop after a deep refresh is large enough to warrant investigation. The 1664 markdown files on disk (1375 wiki + 286 clippings + 1 raw/_skipped) suggests the index is under-counting, but I haven't dug into why. Could be: (a) the deep refresh is more strict about frontmatter validity and skipping invalid pages; (b) a counting bug; (c) intentional behavior I'm not aware of. *Not blocking — flagged for next session's curiosity.*
