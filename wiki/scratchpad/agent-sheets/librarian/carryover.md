---
summary: Librarian carryover 2026-06-01 — 1288 pages, +24 this cycle (substantial activity), vault stable, HITS scores steady
tags: [librarian, carryover, wiki-audit, daily]
updated: 2026-06-01T08:50:00Z
---

# Librarian Carryover — 2026-06-01

## Kanban Status
- [x] Audit complete: 2026-06-01 08:50 AM UTC
- [x] MCP tools: REACHABLE this cycle ✓
- [x] wiki_lint + wiki_hits_analysis + wiki_cluster_pages ran successfully
- [x] All prior cycle open items reviewed — still unchanged (operational artifacts, zero knowledge impact)
- [x] HITS scores stable vs prior cycle
- [x] No new non-preferred tag violations
- [x] No knowledge orphans found (all 118 are operational)

## Established

### Vault Stats (Updated 2026-06-01)
- **Total wiki pages: 1288 (↑ from 1264 — +24 pages this cycle, significant ingestion since 31-May)**
- Orphans: 118 — all operational (agent sheets, carryovers, reports, TEMPLATE, discovery, headlines, overseer, arxiv/news/insight briefs, audits, batch progress). Zero knowledge orphans.
  - Breakdown: 14 agent sheets, 13 discovery, 5 headlines, 6 overseer, 32 arxiv/news/insight briefs, 48 other operational (vault.md, batch-progress, audit-*, ingest-*, carryover variants)
- Broken links: 5745 — ALL operational path artifacts (wiki/agents/*, scratchpad/*, TEMPLATE, carryover.md). Zero in knowledge content.
- Missing frontmatter: 115 — operational files (agent sheets, reports, carryovers, templates). Not critical.
- Non-reciprocal links: 336 — body-text-only detection. High false-positive rate (links already reciprocal via Connections sections). Up from 291 (correlates with +24 page growth). Not actionable without manual verification.
- GAAC clusters: 36 (up from 35) — new knowledge area emerged. Most clusters stable.
- Tag taxonomy: no new non-preferred tag violations. Compound tags (embedding-LR, embedding-entropy, scientific-method) are NOT violations of USE table.

### MCP Tools Available ✓
All tools functional this (1-Jun) cycle.

### HITS Analysis (Authority — this cycle)
| Page | Authority | Type | Content Status |
|------|-----------|------|----------------|
| [[wiki/index]] | 0.0767 | structural | TOC — minimal by design ✓ |
| [[log]] | 0.0540 | structural | Append-only log — appropriate ✓ |
| [[maximum-occupancy-principle]] | 0.0151 | load-bearing | Rich content, full taxonomy ✓ |
| [[concepts/maximum-occupancy-principle]] | 0.0128 | refactored | Lower authority after slug consolidation — stable |
| [[efhf]] | 0.0056 | entity | Rich Connections section ✓ |
| [[concept-index]] | 0.0052 | structural | Navigation layer — appropriate ✓ |
| [[load-bearing-reasoning]] | 0.0039 | concept | Full taxonomy + Connections ✓ |
| [[agentic-research]] | 0.0036 | concept | Full taxonomy + Connections ✓ |

**Top Hubs (this cycle):** maximum-occupancy-principle (0.0030 hub+authority dual), efhf (0.0024), concept-index (0.0021), load-bearing-reasoning (0.0019), edm-framework (0.0018), alphaevolve (0.0018), world-model (0.0018), chain-of-thought (0.0018)

**Comparison vs prior cycle (31-May):** Authority scores stable. Index dropped 0.0774→0.0767; log dropped 0.0547→0.0540; mop dropped 0.0156→0.0151; efhf 0.0054→0.0056. Slight relative dilution from +24 new pages. No structural change.

### GAAC Clustering — this cycle
- Clusters: 36 (↑1 from 35)
- **New cluster emerged**: Cluster 28 — `bounded-representation-capacity`, `arxiv-2605-10878-kolmogorov-weight-norm`, `behavioral-credibility-trilemma`, `orthogonal-bottlenecks-rl` — focused research cluster around bounded representation theory
- Most knowledge clusters stable. Cluster 4 (MCP/efhf/agem) and Cluster 20 (graphrag/knowledge-graph/project-synapse) remain load-bearing hubs
- Missing links: loosely-related topic pairs flagged across clusters. Per skill pitfalls, NOT actionable without manual verification (high false-positive rate).
- Merge candidates: All 1.0 similarity pairs confirmed as false positives (stub page contamination). No merge action needed.

### Tag Taxonomy Compliance
- Checked all 1288 pages against tag-taxonomy.md USE references
- **No violations** of: `embedding`, `vector-embedding`, `semantic-search`, `graph-RAG`, `PKM`, `KG`, `taxonomy`, `scientometrics`, `bibliometrics`, `method`, `ANN`, `fulltext-search`
- Compound tags like `embedding-LR`, `embedding-entropy`, `scientific-method` are NOT in the USE table — no action needed

### Notable New Content This Cycle (per file mtime)
- `wiki/research/mop-agents-integration.md` — research project
- `wiki/concepts/coordination.md`, `wiki/concepts/agentic-hierarchy.md`, `wiki/concepts/production-stage-architecture.md` — agent architecture concepts
- `wiki/concepts/russia-ukraine-war.md`, `wiki/concepts/hormuz-strait-security.md`, `wiki/concepts/nato-expansion.md` — current events
- `wiki/concepts/model-properties.md`, `wiki/concepts/tabular-data.md`, `wiki/concepts/llm-evaluation.md` — ML concepts
- `wiki/concepts/shap.md`, `wiki/concepts/quantization.md`, `wiki/concepts/multimodal-ai.md` — ML technique concepts
- 11+ new synthesis insights in `wiki/synthesis/insights/` (residual-stream-transformer-vm, nous-portal-obsidian-para-integration, bvd-utilities-infrastructure, sodalitium-pope-leo-xiv, dflash-block-diffusion-inference, ebola-drc-aid-collapse-convergence, euler-formula-rope-reasoning-topology, markovian-carryover-session-synthesis, server-session-unifies-agent-memory, cyprus-flotilla-diplomatic-crisis, speculative-decoding-agent-efficiency)

## Open

1. **maximum-occupancy-principle duplicate** — `concepts/maximum-occupancy-principle` (0.0128) coexists with root `maximum-occupancy-principle` (0.0151). Root has higher authority. Consolidation still recommended but not urgent. Unchanged from prior cycle.

2. **118 orphans** — all operational files. Zero knowledge orphans. No action needed. Up from 96 — correlates with new operational files (overseer, headlines, etc.) for this cycle.

3. **5745 broken links** — ALL operational path artifacts. Zero in knowledge content. Not actionable.

4. **336 non-reciprocal links** — body-text-only detection. High false-positive rate. Not actionable without manual verification. Up from 291.

5. **Cluster 0 missing links** — GAAC flags loosely-related topic pairs. False positive rate high. Not actionable without manual verification.

## Heading
- MCP tools available this cycle ✓
- Audit complete; all findings documented
- **Vault grew 24 pages this cycle** (1288 vs 1264 prior) — substantial ingestion since 31-May
- No new actionable items — vault is stable
- Prior cycle Open items #1-#5 confirmed unchanged (operational artifacts, zero knowledge impact)
- New cluster 28 emerged (bounded-representation-capacity cluster) — natural research-area emergence, not an issue
- Next priority: maximum-occupancy-principle duplicate consolidation (still not urgent)
