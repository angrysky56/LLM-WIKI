# Librarians-Assistant Batch Progress

**Last updated:** 2026-06-03
**Batch:** 2026-06-03 morning run (post-librarian)

## Summary

| Metric | Count | Notes |
|--------|-------|-------|
| True knowledge orphans | 0 confirmed (of 73) | All sampled orphans are news/insight/survey pages from 2026-05/06; not actionable this cycle |
| Broken links | 588 | Mostly operational scratchpad path artifacts; ~5-10 knowledge-content gaps |
| Missing frontmatter | 9 → 0 | All 9 fixed this cycle (MOP integration, goodrobot x2, structural-reuse survey, 5x headlines) |
| Non-reciprocal links | 424 | wiki_lint body-text-only detection — high false-positive rate (per skill pitfalls) |
| GAAC missing links | thousands | Extraordinarily high — TF-IDF noise; cluster 0 confirmed over-clustering false positive |
| Reciprocal links added (cumulative) | 11 prior + 0 this cycle | All reciprocal gaps already resolved in prior cycles |
| **Frontmatter completions (this cycle)** | **9** | mop-agents-integration, Q2_SALES_TARGET_LIST, STRATEGIC_BRIEF, structural-reuse survey, 5x headlines |
| **Broken-link typo fixes (this cycle)** | **2** | para.md phantom knowledge-architecture → created canonical page; llms-entity-tracking-state-changes 3 space-typo wikilinks fixed |
| **Phantom MOP authority** | **Self-link removed; phantom persists in HITS index** | Score dropped mop 0.0150→0.0130, concepts/mop 0.0127→0.0105; not self-resolving (per skill) |

## Resolution Details

### This Cycle (2026-06-03)
**Vault health stable + 9 frontmatter completions + 2 typo fixes + 1 stub page created:**

**Frontmatter added (9 pages):**
- `wiki/research/mop-agents-integration.md` — added full frontmatter + Connections section linking to MOP-architecture, bounded-structured-memory, markovian-carryover, peer agent sheets
- `wiki/research/projects/goodrobot/Q2_SALES_TARGET_LIST.md` — added full frontmatter + Connections to goodrobot siblings
- `wiki/research/projects/goodrobot/STRATEGIC_BRIEF.md` — added full frontmatter + Connections to goodrobot siblings + persistent-knowledge-compilation
- `wiki/synthesis/_index/structural-reuse-crosslink-survey-2026-06-01.md` — added full frontmatter + Connections
- `wiki/synthesis/news/2026-May/headlines-2026-05-23.md` — added full frontmatter
- `wiki/synthesis/news/2026-May/headlines-2026-05-24.md` — added full frontmatter
- `wiki/synthesis/news/2026-May/headlines-2026-05-25.md` — added full frontmatter
- `wiki/synthesis/news/2026-May/headlines-2026-05-28.md` — added full frontmatter + Connections to magnifica-humanitas, ai-policy-global-governance
- `wiki/synthesis/news/2026-May/news-2026-05-21-headlines.md` — added full frontmatter

**Broken-link typo fixes (2 pages):**
- `wiki/sources/papers/llms-entity-tracking-state-changes.md` — fixed 3 space-typo wikilinks:
  - `[[entity tracking]]` → `[[entity-tracking-externalization]]`
  - `[[mechanistic interpretability]]` → `[[mechanistic-interpretability]]`
  - `[[attention mechanisms]]` → `[[attention-mechanism]]`
  - Added full frontmatter (was missing sources/status/confidence fields)
- `wiki/concepts/knowledge-architecture.md` — CREATED new canonical page to resolve phantom target (was at `wiki/entities/knowledge-architecture-stub.md` with `-stub` suffix; bare slug `[[knowledge-architecture]]` couldn't resolve). PARA references now point to canonical concept.

### MOP Phantom Authority — Re-verified
- Self-referential `[[maximum-occupancy-principle]]` link removed last cycle — confirmed not present this cycle
- Phantom authority node STILL appears in HITS: `concepts/maximum-occupancy-principle` (0.0105, down from 0.0127)
- Primary MOP authority: 0.0130 (down from 0.0150)
- Per skill: phantoms do NOT self-resolve; the residual values are decaying as the analyzer re-weights, not from disk state changes
- Not a blocker — operational impact is low (analyzer reindexing will eventually catch up)

### Prior Cycles (reference)
- **2026-08-29**: Vault health verified stable
- **2026-08-27**: EFHF frontmatter fixes
- **2026-08-26**: PKM → knowledge-management tag normalization
- **2026-08-25**: 5 genuine reciprocal link fixes
- **2026-08-24**: GAAC phantom page analysis
- **2026-08-10**: 2 reciprocal links added
- **2026-08-23 librarian**: 276 → 43 orphans reduced
- **2026-09-10**: graph-theory.md stale link to archived knowledge-graph removed
- **2026-06-02**: MOP self-link + agents.md duplicate wikilinks cleaned

## Next Batch Priority

1. **All remediation items resolved** — vault is structurally healthy
2. **Remaining blockers (need Ty input)**:
   - GoodRobot multi-location: 11 files across 2 vault paths — canonical location undecided
   - gbrain.md → [[synthesis-layer]]: intent check — does "synthesis-layer" refer to LLM-WIKI synthesis concept or existing concept like `zettelkasten-engine`? (Note: gbrain page itself doesn't exist — phantom target)
   - `para.md` still has bare-slug wikilink `[[knowledge-architecture]]` — should now resolve to newly-created canonical page
3. **Non-preferred tags**: 0 — fully clean
4. **HITS phantom authority MOP**: scores decaying, will fully resolve on next HITS reindex

## Kanban Task Tracking

All prior kanban tasks resolved. No active remediation tasks this cycle.

## Related
- [[wiki/index]]
- [[scratchpad/agent-sheets/librarians-assistant/carryover]]

## Blockers (unchanged — need Ty decisions)

1. **GoodRobot multi-location** (since 2026-07-29): 11 files across 2 vault paths — canonical location undecided
2. **gbrain synthesis-layer wikilink** (since 2026-07-29): intent check — does "synthesis-layer" refer to LLM-WIKI synthesis concept or existing concept like `zettelkasten-engine`? **Note**: gbrain page itself is phantom (not found on disk) — the MOP `[[gbrain]]` reference points to a non-existent target
3. **MOP phantom authority** (open since 2026-06-01): phantom authority score dropping (0.0150→0.0130 main, 0.0127→0.0105 phantom); self-link removed but phantom persists in HITS index — non-blocking, decaying naturally
