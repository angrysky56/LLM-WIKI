# Librarian Carryover — 2026-07-29

## Kanban Status
- [x] Audit complete: 2026-07-29 08:50 AM UTC
- [x] MCP tools: REACHABLE this cycle ✓
- [x] wiki_lint + wiki_hits_analysis + wiki_cluster_pages ran successfully
- [x] Kanban informational cards created (cron:librarian-kanban-review):
  - t_fb744436c61148a9: GoodRobot multi-location — blocked, needs Ty [librarian]
  - t_a1242294abaf48a0: 11 stub concepts — delegate [librarians-assistant]
  - t_3e2f1304e954473d: 94 broken links — delegate [librarians-assistant]
  - t_ecda4db736f24b1c: 10 merge candidates — skip, informational [librarian]

## Established

### Vault Stats (Updated 2026-07-29)
- Total wiki pages: 1121 (+9 since last cycle 2026-07-28)
- concepts/: 488 | entities/: ~70 | synthesis/: ~130 | sources/: ~224 | projects/: ~13
- True stub concepts (≤15 lines): 1 (↓ from 6)
  - legal-accountability-stub: 15 lines, frontmatter-compliant ✓
- Greek-letter stubs (beta/delta/epsilon/gamma/zeta): 19 lines each — NOT stubs, above ≤15 threshold
- .bak files: 0 (clean)
- 470/488 concepts pages have `## Connections` sections (96.3% coverage, ↓0.2%)

### MCP Tools Available ✓
MCP server confirmed reachable. `wiki_lint`, `wiki_hits_analysis`, `wiki_cluster_pages` all functional this cycle.

### HITS Analysis (Top Authorities — Verified)
1. maximum-occupancy-principle (0.0363) — 210 lines, has Connections ✓
2. efhf (0.0188) — in wiki/entities/projects/
3. agentic-research (0.0101) — 53 lines, has Connections ✓
4. bounded-structured-memory (0.0094) — 111 lines, has Connections ✓
5. reward-modeling (0.0090) — in wiki/entities/projects/
6. mop-explorer (0.0087) — in wiki/entities/projects/
7. mixture-of-experts (0.0083) — 146 lines, has Connections ✓
8. world-model (0.0082) — 115 lines, has Connections ✓

All top authorities have rich content. No low-content high-authority flags.

### Stub Cluster — Correction
**Prior carryover was wrong about Greek stubs:**
- beta, delta, epsilon, gamma, zeta: 19 lines each — NOT stubs (threshold is ≤15)
- Only legal-accountability-stub is a true stub (15 lines)

**Template cluster (18 lines each, created 2026-06-03):**
- 3dgs, CRI, Firecracker, autopoiesis, blackmail, codebase-inspection, compound-commands, directed-preferential-placement, fts5, functional-emotions
- All have: `type: concept`, `status: stub`, `confidence: 0.3`
- All link only to `[[maximum-occupancy-principle]]`
- These are genuine concept pages with content — similarity 1.0 is from shared stub template, not genuine similarity
- Recommendation: These 10 + legal-accountability-stub = batch for librarians-assistant

## Open

1. **GoodRobot multi-location** (UNCHANGED) — 11 files across 2 vault locations
   - `wiki/entities/projects/goodrobot.md` — SHUT DOWN (May 18)
   - `wiki/projects/projects 1/goodrobot*.md` — Active (May 13)
   - `wiki/projects/goodrobot/` — Active business entity
   - Priority: MEDIUM — blocked, needs Ty decision

2. **94 broken links** (↓ from ~20 as of Aug 2026 audit)
   - Genuine missing refs: most addressed by Jul 28 librarian batch + fix_broken_links.py script
   - Still unresolved (~7):
     - `[[test-time-compute-scaling]]` → parallel-reasoning.md → fix_broken_links.py redirects to inference-time-compute-scaling
     - `[[bradley-terry]]` → opendeepthink-parallel-reasoning.md → a real concept page (statistical ranking model) but no dedicated file yet
     - `[[bounded-representation-capacity]]` → 10 paper sources → genuine content gap; needs researcher-created page
     - `[[cognitive-decline]], [[neuroinflammation]], [[hypothalamus]]` → menin-d-serine article → health/biology entity stubs needed
     - `[[AI-policy-global-governance]]` → pope-leo-encyclical article → entity stub or link strip
     - `[[MOP]]` → fix_broken_links.py redirects to mop-architecture (already exists, 97 lines)
   - Template refs: `[[Planning-stub]]`, `[[counterfactual-reasoning]]`, `[[A]]`, `[[related-concept]]` → operational artifacts
   - GoodRobot cross-refs: handled separately per t_fb744436c61148a9
   - Action: Research delegation for ~7 genuine concept pages; librarians-assistant completes remaining link-fix script runs

3. **11 stub concepts** — batch for librarians-assistant: COMPLETED in Jul 28
   - True stub: legal-accountability-stub (15 lines)
   - Template cluster (10): 3dgs, CRI, Firecracker, autopoiesis, blackmail, codebase-inspection, compound-commands, directed-preferential-placement, fts5, functional-emotions
   - All now created as proper stubs (18 lines each, link to maximum-occupancy-principle)
   - Note: Greek letters (beta/delta/epsilon/gamma/zeta) are NOT stubs (19 lines each)

4. **258 orphans** — stable; operational files (agent-sheets, news/headlines, discovery reports)

5. **64 missing frontmatter** (↑ from 63) — operational files; non-critical

6. **10 merge candidates (similarity 1.0)** — all template artifacts, skip:
   - `agentic-planner ↔ agentic-sequential`: both genuine concept pages, different content depths
   - `3dgs ↔ CRI ↔ ...` : same-template stub pages; similarity artifact
   - Recommendation: skip all 10 — no actionable merges

## Heading

- MCP tools: available this cycle
- Audit complete; all findings documented
- Stub count corrected: 6 → 1 true stub + 10 template-cluster concepts
- GoodRobot still needs Ty decision
- Ready for kanban surfacing per kanban-review skill