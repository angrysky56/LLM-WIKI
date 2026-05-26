# Librarian Carryover — 2026-07-27

## Kanban Status
- [x] Audit complete: 2026-07-27 08:50 AM UTC
- [x] MCP tools: REACHABLE this cycle ✓
- [x] Vault health: wiki_lint + wiki_hits_analysis ran successfully
- [x] Kanban tasks already created for open items (prior cycle):
  - t_029ba0b1e28a199f: GoodRobot multi-location — blocked, needs Ty
  - t_0adf1f46e814ee2f: 8 stub concepts — ready (delegate)
  - t_8d4282a9420e6d6e: 85 broken links — ready (delegate)

## Established

### Vault Stats (Updated 2026-07-27)
- Total wiki pages: 1112 (+10 since last carryover 2026-07-26)
- concepts/: 488 | entities/: ~70 | synthesis/: ~130 | sources/: ~224 | projects/: ~13
- Stub concepts (≤15 lines): 6 (unchanged — Greek stubs fully frontmatter'd)
  - beta, delta, epsilon, gamma, zeta, legal-accountability-stub
  - All fully frontmatter-compliant with created/updated/type/summary/status/confidence
- .bak files: 0 (was 44 — bulk deleted 2026-05-26)
- 471/488 concepts pages have `## Connections` sections (96.5% coverage)
- Linking culture: strong — 471 pages with Connections sections out of 1112 total

### MCP Tools Available ✓
MCP server confirmed reachable. `wiki_lint`, `wiki_hits_analysis`, `wiki_cluster_pages` all functional this cycle.

### HITS Analysis (Top Authorities)
1. maximum-occupancy-principle (0.0426) — highest authority, load-bearing node
2. efhf (0.0215)
3. agentic-research (0.0110)
4. bounded-structured-memory (0.0096)
5. mop-explorer (0.0094)

Top Hubs: carryover, maximum-occupancy-principle, concept-index

### GoodRobot Duality (UNCHANGED — Ty decision still needed)
- `wiki/entities/projects/goodrobot.md` — SHUT DOWN (May 18)
- `wiki/projects/projects 1/goodrobot.md` — Active (May 13)
- Both type: entity — different writeups of same entity from different angles
- Related: gtm-strategy.md, research-pipeline.md, technical-architecture.md (in projects/projects 1/)
- Also: wiki/synthesis/news/goodrobot-revenue-model.md
- Priority: MEDIUM — storage redundancy, no functional breakage

## Open

1. **GoodRobot multi-location** — 5-6 files across 3 vault locations for same entity — needs Ty consolidation decision
2. **104 broken links** (↑ from 85 — due to `sheet.md` having 40+ duplicate double-bracket refs to same paths; adjusted actual missing refs: ~60)
   - Teaching examples in operating docs: `[[Planning-stub]]`, `[[counterfactual-reasoning]]`, `[[bradley-terry]]`, `[[test-time-compute-scaling]]`
   - Genuine missing: `[[qora]]`, `[[MOP]]`, `[[tool-use]]`, `[[diffusion-models]]`, `[[grpo]]`
   - GoodRobot cross-refs: `[[wiki/projects/goodrobot/shut-down-entity]]` etc.
3. **6 stub concepts** — low-value minimal pages (beta, delta, epsilon, gamma, zeta, legal-accountability-stub) — needs expand/merge/delete review
4. **256 orphans** — stable (operational files: agent-sheets, news/headlines, discovery reports; genuine orphans are mostly daily timestamped reports no longer linked after creation)
5. **63 missing frontmatter files** — mostly agent-sheet templates + reports (non-critical, operational files)

## Heading

- MCP tools: available this cycle
- Open items unchanged from last cycle — all require Ty judgment or delegate action
- Ready for kanban surfacing per kanban-review skill
