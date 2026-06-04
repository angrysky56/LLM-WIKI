# Session Techniques — 2026-06-04

## 1. Persistent arXiv API 429 → pivot to local pending-PDF pool first

**Pattern:** arXiv API can be **persistently 429'd** from this IP (4 consecutive attempts at 60s/90s/180s/240s backoff, all 429). Do NOT keep retrying. After 2 failures, **switch to the local pending-PDF pool immediately** — check `/home/ty/Documents/paper-research/research-carryover.md` for the `Unprocessed … Batch PDFs` table and claim from there. The local pool can keep the agent productive for 2-3 more cycles even if the API stays blocked.

**Verification:** today's run processed 2605.30343, 2605.30335, 2605.30348 entirely from local PDFs (downloaded by a prior process) without any successful arXiv API call.

**Caveat:** The local pool ages out — the most recent unprocessed PDFs are usually 1-3 days old. For "live" new submissions, the API fallback chain (HTML list page → wiki_fetch_url per-paper) still applies.

## 2. Cross-cycle paper pages: write BOTH directions of wikilinks

**Pattern:** When a new batch (N) cross-links to a prior batch (N-1), update BOTH:
- New pages get a "Cross-cycle (N-1 batch)" section citing prior pages
- Prior pages get a "Cross-cycle (N batch)" section citing new pages

This produces a dense bidirectional web that makes the bounded-self-model / theme-arc actually navigable. Today's run:
- 3 new pages each cited Sleep, Skill-RM, Faithful Confidence 2-4 times in Wiki Connections + Cross-cycle sections
- 3 prior pages each added a "Cross-cycle (2026-06-04 batch)" section with 3 outgoing links

Verify with: `grep -c 'sleep-self-modify\|skill-rm\|faithful-confidence' newpage.md` (forward) and `grep -c 'arxiv-2605-3034' priorpage.md` (reverse). All should be ≥ 1.

## 3. Wiki Connections → wikilink to concepts, not just to papers

The wiki's wikilink resolver accepts forward references to concepts that don't yet have a page. Linking to `[[bounded-self-model]]` (a concept) is more useful than linking only to source pages because:
- It builds the concept index in the link graph even before the concept page exists
- When a synthesis page IS later created, the backlinks are already in place
- Lint will flag the missing concept pages as candidates for next-cycle work

## 4. Patch tool artifact: duplicate header after re-edit

**Bug:** When you `patch` to *insert* a section immediately after an existing `## Header` line, and the `old_string` doesn't include enough context, the patch can produce a duplicated header on the line just above the inserted content (e.g., `## What To Watch\n## What To Watch\n- item...`).

**Fix:** Run a second `patch` with the exact `## What To Watch\n## What To Watch` two-line pattern and replace it with the single `## What To Watch`. Cheap to fix, ugly in `git diff`.

## 5. Index update timing

`wiki_update_index()` is idempotent and fast. Run it AFTER the last wiki write of the session, not after each write. Today's run did 2 updates total — both returned "Index updated with 1130 pages" in < 1s. No need to be more granular.

## 6. PyMuPDF install path (cron context)

`pymupdf` is NOT pre-installed in cron context. `pip3 install pymupdf` works on this system (Python 3.13 via miniconda at `/home/ty/miniconda3/bin/python3`, ~25MB, 6.9MB/s). Install before first `import pymupdf`. Single-shot install; persists across cron runs.
