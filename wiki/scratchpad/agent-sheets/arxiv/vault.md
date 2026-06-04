# arxiv — Episodic Vault (2026-06-04 run)

## State
- Inbox: empty
- Carryover last run: 2026-06-03 (3 papers: Sleep, Skill-RM, Faithful Confidence)
- Theme: bounded self-model
- arxiv API: known aggressive rate limiting; use curl with backoff

## Plan
1. Check unprocessed pending PDFs (priority order from research-carryover.md)
2. Query arXiv API for 2026-06-03 / 2026-06-04 new submissions
3. Select top 3 by significance
4. Download PDFs (curl, parallel)
5. Extract text via pymupdf
6. Write wiki pages inline (no delegate_task in cron)
7. Assemble report
8. MOP compress to carryover.md

## Run log
- arXiv API: 4 attempts, all 429'd. 60-240s backoff insufficient. Pivoted to local pending-PDF pool.
- Selected 2605.30343 (RiM), 2605.30335 (Kotawala), 2605.30348 (LLMSurgeon).
- All 3 PDFs extracted via pymupdf. 3 wiki pages written. PDFs moved to processed/.
- Cross-links written to/from prior cycle (Sleep, Skill-RM, FC).
- Shared carryover + report + this vault's successor (carryover.md) updated.

## Outcome
- 3 pages created
- 3 prior pages updated with cross-cycle links
- Theme consolidated: bounded self-model has 3 orthogonal failure axes (allocation, composition, introspection)
- This vault cleared (compressed into carryover.md) — next session starts fresh.
