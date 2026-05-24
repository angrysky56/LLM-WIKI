---
summary: Librarian carryover 2026-06-15 — 8 stubs created, high-value wiki clean, scratchpad noise unchanged
tags: [librarian, carryover, audit]
updated: 2026-06-15
---

## Established

**Date:** 2026-06-15  
**MCP Status:** OK — package available, but wiki_lint/cluster_pages/hits not registered as MCP handlers (fallback: full_audit.py)  
**Trigger:** Scheduled cron

### Audit Metrics (full_audit.py)

| Metric | Value | Change |
|--------|-------|--------|
| Total pages | 608 | +18 |
| Missing frontmatter | 279 | same |
| Broken wikilinks | 215 | -6 from 221 |
| Orphans (filesystem) | 0 | -1 |

### Vault Health

- **High-value dirs (concepts/entities/synthesis):** CLEAN — 289 pages, 0 missing FM
- **All broken links are in scratchpad/report files** — non-critical noise
- **PDF contamination:** None

### Fixed This Cycle

8 stub pages created resolving broken links from wiki content:
- `wiki/concepts/initialization.md` ← fixes `critical-initialization-biological-neural-networks.md` outbound link
- `wiki/concepts/criticality.md` ← same
- `wiki/concepts/working-memory.md` ← same  
- `wiki/concepts/lcguard.md` ← fixes `adversarial-training.md`, `agent-leak-benchmark.md`
- `wiki/concepts/epistemic-energy.md` ← fixes `agent-native-design.md`, `world-model.md`
- `wiki/concepts/bounded-rationality.md` ← fixes `agent-native-design.md`
- `wiki/concepts/panksepp-emotional-systems.md` ← fixes `machine-psychology.md`
- `wiki/concepts/superposition.md` ← fixes `neural-interpretability.md` (already referenced there)

## Open

1. `critical-initialization-biological-neural-networks.md` — still technically orphan (no inbound links from other wiki pages); outbound links now resolve to stubs
2. ~215 broken wikilinks remain — all in scratchpad/report files (not wiki content)
3. ~279 pages missing frontmatter — dominated by scratchpad/agent-sheet noise
4. `generate_insights()` would timeout at 300s — skip if MCP unavailable

## Heading

- Vault is healthy at the wiki content layer
- Next cycle focus: scratchpad report cleanup (optional, low value)
- Orphan paper `critical-initialization-biological-neural-networks.md` could use an inbound link from a survey/overview if one exists