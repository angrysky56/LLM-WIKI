---
summary: Librarian carryover 2026-06-02 — 1324 pages, +36 this cycle (vault growing), HITS scores stable, all structural findings operational
tags: [librarian, carryover, wiki-audit, daily]
updated: 2026-06-02T08:50:00Z
---

# Librarian Carryover — 2026-06-02

## Kanban Status
- [x] Audit complete: 2026-06-02 08:50 AM UTC
- [x] MCP tools: REACHABLE this cycle ✓
- [x] wiki_lint + wiki_hits_analysis + wiki_cluster_pages ran successfully
- [x] All prior cycle open items reviewed — still unchanged (operational artifacts, zero knowledge impact)
- [x] HITS scores stable vs prior cycle (slight relative dilution from +36 page growth)
- [x] No new non-preferred tag violations
- [x] No knowledge orphans found (all 136 are operational)

## Established

### Vault Stats (Updated 2026-06-02)
- **Total wiki pages: 1324 (↑ from 1288 — +36 pages this cycle, continued substantial ingestion)**
- Orphans: 136 — all operational (agent sheets, carryovers, reports, TEMPLATE, discovery, headlines, overseer, arxiv/news/insight briefs, audits, batch progress, archives). Zero knowledge orphans.
  - Breakdown by category: ~14 agent sheets, ~13 discovery, ~5 headlines, ~6 overseer, ~32 arxiv/news/insight briefs, ~50 other operational (vault.md, batch-progress, audit-*, ingest-*, carryover variants, insight-*, structural-reuse-*, gamma-world, agem-*, clipping_*, news-*, microsoft-search-*, meta-)
- Broken links: 5865 — ALL operational path artifacts (wiki/agents/*, scratchpad/*, TEMPLATE, carryover.md). Zero in knowledge content. Up from 5745 (correlates with +36 pages).
- Missing frontmatter: 120 — operational files (agent sheets, reports, carryovers, templates, vault.md, mcp-tools reference). Not critical. Up from 115.
- Non-reciprocal links: 345 — body-text-only detection. High false-positive rate (links already reciprocal via Connections sections). Up from 336 (correlates with +36 page growth). Not actionable without manual verification.
- GAAC clusters: 36 — STABLE (same as prior cycle)
- Tag taxonomy: no new non-preferred tag violations. Compound tags (embedding-LR, embedding-entropy, scientific-method) are NOT violations of USE table.

### MCP Tools Available ✓
All tools functional this (2-Jun) cycle.

### HITS Analysis (Authority — this cycle)

| Page | Authority | Type | Content Status |
|------|-----------|------|----------------|
| [[wiki/index]] | 0.0765 | structural | TOC — minimal by design ✓ |
| [[log]] | 0.0537 | structural | Append-only log — appropriate ✓ |
| [[maximum-occupancy-principle]] | 0.0148 | load-bearing | Rich content, full taxonomy ✓ |
| [[concepts/maximum-occupancy-principle]] | 0.0126 | refactored | Lower authority after slug consolidation — stable |
| [[efhf]] | 0.0056 | entity | Rich Connections section ✓ |
| [[concept-index]] | 0.0052 | structural | Navigation layer — appropriate ✓ |
| [[load-bearing-reasoning]] | 0.0039 | concept | Full taxonomy + Connections ✓ |
| [[agentic-research]] | 0.0037 | concept | Full taxonomy + Connections ✓ |

**Top Hubs (this cycle):** maximum-occupancy-principle (0.0030 hub+authority dual), efhf (0.0024), concept-index (0.0021), load-bearing-reasoning (0.0019), edm-framework (0.0018), alphaevolve (0.0018), world-model (0.0018), chain-of-thought (0.0018)

**Comparison vs prior cycle (1-Jun):** Authority scores stable. Index 0.0767→0.0765; log 0.0540→0.0537; mop 0.0151→0.0148; efhf 0.0056→0.0056. Slight relative dilution from +36 new pages. No structural change.

### GAAC Clustering — this cycle
- Clusters: 36 (STABLE, same as prior cycle)
- All knowledge clusters stable. Cluster 0 (research projects, MOP/bounded-representation/agentic-research hub), Cluster 4 (memory/transformer/MoE architectural), and Cluster 20 (graphrag/knowledge-graph/project-synapse) remain load-bearing hubs
- Missing links: loosely-related topic pairs flagged across clusters. Per skill pitfalls, NOT actionable without manual verification (high false-positive rate)
- Merge candidates: All 1.0 similarity pairs confirmed as false positives (stub page contamination). No merge action needed.

### Tag Taxonomy Compliance
- Checked vault against tag-taxonomy.md USE references
- **No violations** of: `embedding`, `vector-embedding`, `semantic-search`, `graph-RAG`, `PKM`, `KG`, `taxonomy`, `scientometrics`, `bibliometrics`, `method`, `ANN`, `fulltext-search`
- Compound tags like `embedding-LR`, `embedding-entropy`, `scientific-method` are NOT in the USE table — no action needed

### Notable New Content This Cycle (per file mtime + orphan list)
- New arxiv papers indexed: arxiv-2605-27140-stepopsd, arxiv-2605-28814-bidirectional-evolutionary-search-bes, arxiv-2605-28816-gamma-world, plus several 27322-27355 series
- New insight files: cyprus-flotilla-diplomatic-crisis, sodalitium-pope-leo-xiv, ebola-drc-aid-collapse-convergence, euler-formula-rope-reasoning-topology, markovian-carryover-session-synthesis, server-session-unifies-agent-memory, speculative-decoding-agent-efficiency
- New research entities: paper2code-enhanced, orcaid, goodrobot, llmsurgeon-diagnosing-data-mixture-2026, mixture-of-recursions, on-the-representation-collapse-of-sparse-mixture-of-experts, applying-mathematics
- New agent/operational sheets: librarian-agent, librarians-assistant, researcher, researcher-agent, news-agent, hermes-agent, mcp-model-context-protocol-hermes, project-synapse-mcp-tools, hermes-agent-github-labels, github-hermes-agent-lcm-slash-commands-search
- New clip entities: clipping_anthropic_ipo, clipping_brazil_tariff, clipping_ebola_kenya, clipping_lebanon_ceasefire, clipping_russia_kyiv
- New event pages: ghana-anti-lgbt-bill-may-2026, iran-war-day-93-lebanon-incursion-may-31-2026, blue-origin-new-glenn-explosion-may-2026

## Open

1. **maximum-occupancy-principle duplicate** — `concepts/maximum-occupancy-principle` (0.0126) coexists with root `maximum-occupancy-principle` (0.0148). Root has higher authority. On-disk verification: only `wiki/concepts/maximum-occupancy-principle.md` file exists; the root authority score is coming from a wikilink alias the analyzer is treating as a separate node. Consolidation still recommended but not urgent. Unchanged from prior cycle.

2. **136 orphans** — all operational files. Zero knowledge orphans. No action needed. Up from 118 — correlates with new operational files for this cycle.

3. **5865 broken links** — ALL operational path artifacts. Zero in knowledge content. Not actionable. Up from 5745.

4. **345 non-reciprocal links** — body-text-only detection. High false-positive rate. Not actionable without manual verification. Up from 336.

5. **Cluster missing links** — GAAC flags loosely-related topic pairs. False positive rate high. Not actionable without manual verification.

## Heading
- MCP tools available this cycle ✓
- Audit complete; all findings documented
- **Vault grew 36 pages this cycle** (1324 vs 1288 prior) — continued substantial ingestion
- No new actionable items — vault is stable
- Prior cycle Open items #1-#5 confirmed unchanged (operational artifacts, zero knowledge impact)
- Cluster count stable at 36
- Next priority: maximum-occupancy-principle duplicate consolidation (still not urgent)
