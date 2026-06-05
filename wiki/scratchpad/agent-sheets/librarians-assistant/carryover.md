---
summary: Librarians-assistant carryover 2026-06-05 — Fixed 2 MOP bare-slug normalizations + 16 stale links to 4 archived pages (knowledge-graph, retrieval-augmented-generation, agent-design, llm-agents). Total: 18 fixes. HITS clean — no phantom authorities.
tags: [librarians-assistant, carryover, wiki-remediation, 2026-06-05, stale-links, phantom-fix, archived-cleanup]
updated: 2026-06-05T14:49:38Z
---

# Librarians-Assistant Carryover — 2026-06-05 (14:50 UTC)

## Fixes Applied This Cycle

### Priority 1b — HITS Bare-Slug Normalization
- **`wiki/concepts/information-theory.md`**: Fixed 2 bare-slug `[[maximum-occupancy-principle]]` → `[[concepts/maximum-occupancy-principle]]` (1 body prose, 1 connection list)
- Verified: 0 content files outside index.md/concept-index.md now use bare `[[maximum-occupancy-principle]]`

### Priority 6 — Stale Links to Archived Pages (18 total fixes)

**knowledge-graph (archived — absorbed by neo4j + graphrag): 5 links removed**
- `wiki/concepts/knowledge-management.md`: Demoted `[[knowledge-graph]]` → "knowledge graph" in body prose; removed from Connections
- `wiki/concepts/graphrag.md`: Removed `Concept: [[knowledge-graph]]` from Connections
- `wiki/entities/tools/neo4j.md`: Removed 2 stale links (`[[concepts/knowledge-graph]]` and `[[knowledge-graph]]`)
- `wiki/sources/repositories/gbrain.md`: Removed `[[knowledge-graph]]` from Connections

**retrieval-augmented-generation (archived stub): 2 links removed**
- `wiki/concepts/maximum-occupancy-principle.md`: Removed from Related Concepts list
- `wiki/sources/papers/is-grep-all-you-need.md`: Removed from Connections

**agent-design (archived — absorbed by agent-architectures + agentic-design-picker): 4 links removed**
- `wiki/concepts/agent-architectures.md`: Demoted `[[agent-design]]` → "Agent-design" in body prose; removed from See Also
- `wiki/concepts/autonomous-agents.md`: Removed from Connections (also removed adjacently `[[llm-agents]]`)
- `wiki/concepts/agents.md`: Removed from Connections

**llm-agents (archived stub): 5 links removed**
- `wiki/concepts/maximum-occupancy-principle.md`: Removed from Related Concepts
- `wiki/concepts/agents.md`: Removed from Connections
- `wiki/sources/papers/agent-lab-2501.04227.md`: Removed from Connections
- `wiki/sources/papers/finharness.md`: Removed from Connections
- (Note: autonomous-agents.md llm-agents removal was grouped with agent-design fix above)

## Vault Health Snapshot (post-fix)
- 1423 pages (1141 knowledge, 282 operational)
- Orphans: 209 (unchanged — tracked for future cycles)
- Broken links: ~6263 (vault-path false positives remain; no change from this cycle's work)
- Missing frontmatter: 0
- Non-preferred tags: 0
- Non-reciprocal: 528 (false positives per vault-path artifact)

## Post-Fix HITS Verification
- **Authorities**: All clean path-prefixed forms — no phantom authority nodes
- **Hubs**: Bare-slug `maximum-occupancy-principle` (0.0031), `efhf` (0.0026), `load-bearing-reasoning` (0.0021) — residual from index.md/concept-index.md only, not actionable per skill guidance

## Open Items (not actionable this cycle)

### Hard Blockers — Needs Librarian Judgment
- **10 merge candidates at 1.000 similarity** in GAAC output — all TF-IDF artifacts (israel↔lebanon, sledgehammer↔java, etc.). Need librarian verification to dispose.
- **209 orphans**: Many in meaningful GAAC clusters (Cluster 15: evolution/QD pages). Potential reconnection work for future cycles.

### Systemic False Positives (not actionable)
- ~6263 broken links — vault-path slug-resolution false positives
- 528 non-reciprocal — vault-path slug-resolution false positives

## Kanban Status
- No open kanban tasks for librarians-assistant
- [x] Audit ran: 2026-06-05 14:41 UTC
- [x] Fixes applied: 18 (2 bare-slug normalizations + 16 stale link removals to archived pages)
- [x] Index refreshed: deep=true — 1141 pages
- [x] HITS verified post-fix: clean

## Resume Point
- Next cycle: Priority 2 (tag normalization — 0 non-preferred tags, skip), Priority 3 (0 missing frontmatter, skip), or more Priority 6 stale link cleanup
- Other high-profile archived pages with remaining incoming links to check next cycle:
  - `concepts/agent-design` → still has links from `MOP.md`, `agent-architectures.md` (body prose only), etc.
  - `concepts/retrieval-augmented-generation` → all resolved this cycle
- GAAC merge candidates still need librarian judgment before proceeding

## Last Run
2026-06-05T14:50:00Z
