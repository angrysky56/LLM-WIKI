---
type: carryover
created: 2026-06-05
tags: [insights, carryover]
source: insights-agent daily run
---

# Insights Agent — Carryover

## Established
- GAAC clustering (n_clusters=15) completed: 15 clusters identified across 1430+ wiki pages
- Cluster analysis evaluated against publishability criteria (threshold 0.80)
- 2 new synthesis pages created from GAAC cluster analysis (no CLI generate_insights run — used GAAC-only workflow as per updated SKILL.md)

## Pages Created (2)
1. `wiki/synthesis/insights/essan-pidgin-matcha-semantic-bridge-insight.md` — ESSAN PIDGIN/MATCHA semantic bridge from Cluster 8 (confidence 0.82)
2. `wiki/synthesis/insights/wolfram-causal-networks-reasoning-constraints-insight.md` — Wolfram causal networks reasoning constraints from Cluster 12 (confidence 0.78, borderline — under-developed topic exception)

## Open
- **Insight 3 (EFHF Spiral Architecture, confidence 0.76)**: Carried over — below threshold. Pages need to mature from scratchpad notes to concept pages before synthesis is warranted
- **Cluster 5 (AGEM, ~14 pages)**: Track for future — pages are experimental scratchpad notes, not yet ready for synthesis. Check if AGEM pages mature in future runs
- **Merge candidates (sim=1.000)**: 6 pairs detected — fts5/compound-commands, random-forest/tabpfn, micro-saas/programmatic-seo, sledgehammer/java/latex, printing-press/peter-steinberger, israel/lebanon. Should be reviewed by librarian for merging
- **Persistent re-detection**: Clusters 3 (sanctions), 6 (PARA), and embedded insight pages in Cluster 0 continue to re-appear. This is expected — the GAAC catches them because the underlying pages still exist in the wiki. No action needed
- **Index updated**: 1147 pages (2 new insight pages added)

## Heading
- Next run: re-run GAAC clustering to check if AGEM/EFHF clusters have matured
- Consider adding more clusters (20-25) for finer granularity — many clusters are very large (0, 2, 4, 10)
- The CLI generate_insights was not run this cycle — GAAC-only workflow. If new content has been added, future runs should alternate or combine both approaches