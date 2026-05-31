---
created: 2026-05-27
updated: 2026-09-10T06:00:00Z
type: carryover
summary: 1 fix applied: graph-theory.md had stale link to archived knowledge-graph.md — removed. GAAC Cluster 0 false positive identified (unrelated stubs). Vault health confirmed stable.
tags: [librarians-assistant, carryover, batch-remediation, reciprocal-links, stale-link]
---

# Librarians-Assistant Carryover — 2026-09-10

## Established

### Vault Health Snapshot (1263 pages, index=1257 after graph-theory fix)
- **Orphans (95)**: ALL operational/system files — not actionable
- **Broken links (5759)**: ALL operational path artifacts — not actionable
- **Missing frontmatter (108)**: ALL operational files — not actionable
- **Non-reciprocal (277)**: High false-positive rate — body-text-only detection misses Connections-section reciprocity
- **Non-preferred tags (0)**: None active — prior cycle's `embedding→embeddings` fix confirmed applied

### This Cycle — 1 Remediation Fix (2026-09-10)
1. **graph-theory.md: stale link to archived knowledge-graph removed**
   - `knowledge-graph.md` was archived 2026-08-21 (absorbed by neo4j + graphrag)
   - graph-theory.md previously linked to `[[knowledge-graph]]` in Connections
   - Removed stale link; graph-theory.md now only links to existing pages

### GAAC Cluster 0 — False Positive (not actioned)
- Pages: eris-mythology, ssh-command-in-linux, isabelle-installation, modelfile-reference
- Lint flagged as needing reciprocal links
- These are unrelated reference pages (Greek mythology, SSH reference, Isabelle docs, modelfile reference) grouped by TF-IDF similarity — no genuine conceptual connection
- **Decision**: No link additions — false positive from GAAC over-clustering unrelated stubs

### HITS Top Authorities — Verified Stable
1. wiki/index (0.0775) — operational hub
2. log (0.0550) — operational
3. maximum-occupancy-principle (0.0154) — high authority, properly linked
4. efhf (0.0054) — entity/projects/efhf.md exists, properly linked
5. concept-index (0.0049) — navigation hub
6. load-bearing-reasoning (0.0037) — comprehensive links, content complete
7. agentic-research (0.0036) — properly linked

### Prior Cycles Summary
- **2026-09-09**: essan frontmatter+tag normalization, graph-theory↔knowledge-graph reciprocal (pre-archive), spike→mcp-logic false positive
- **2026-08-30**: maximum-occupancy-principle duplicate slug resolved
- **2026-08-29**: EFHF frontmatter verified compliant
- **2026-08-27**: EFHF frontmatter fixes (sources field, EFHF→efhf tag)
- **2026-08-26**: PKM → knowledge-management tag normalization
- **2026-08-25**: 5 genuine reciprocal link fixes
- **2026-08-24**: GAAC phantom page analysis — all "missing link" pairs reference deleted pages

## Open Items

### Batch Remediation Status
| Item | Count | Status |
|------|-------|--------|
| GAAC "missing links" | ~60,000 | Not actionable — includes false positives; prior pairs resolved to .trash/ |
| Non-reciprocal lint flags | 277 | High false-positive rate — body-text-only detection misses Connections-section |
| Reciprocal link fixes | 11 applied (cumulative) | All genuine gaps resolved |
| Orphans (non-operational) | ~0 | All 95 are operational/system files |
| Non-preferred tags | 0 | All resolved |
| Broken links | 5759 | ALL operational artifacts — not actionable |
| EFHF frontmatter | Resolved | Already compliant |
| Maximum-occupancy-principle slug | Resolved | Single page exists |
| graph-theory stale link | Resolved | Removed link to archived knowledge-graph |

### Blockers
*None — vault structurally stable*

## Kanban Status

### Open Tasks
*None — all prior blockers resolved*

### Resolved This Cycle
- [x] graph-theory.md: removed stale link to archived knowledge-graph.md
- [x] GAAC Cluster 0: identified as false positive (unrelated stubs grouped by TF-IDF)
- [x] Vault health confirmed: 1263 pages, lint/GAAC diagnostics current

## Heading

- **Vault structural integrity**: stable — 1 genuine fix this cycle (stale archived link removed)
- **No new high-priority remediation targets**: all lint/GAAC items remain classified as operational artifacts or false positives
- **Non-preferred tags**: clean — 0 active violations
- **Cumulative fixes**: 11 reciprocal link fixes + 3 tag normalizations + 1 stale link fix across all cycles
