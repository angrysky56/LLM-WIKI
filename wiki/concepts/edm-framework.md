---
summary: Embedding Disruptiveness Measure — Kim, Kojaku & Ahn (2026) — directional skip-gram on citation networks yielding past/future vectors whose cosine distance quantifies scientific disruption
tags: [EDM, citation-network, embeddings, science-of-science, disruption, skip-gram, node2vec, simultaneous-discovery]
type: concept
sources: https://doi.org/10.1126/sciadv.adx3420
status: reference
updated: 2026-04-11T00:00:00Z
---

# EDM — Embedding Disruptiveness Measure

**Source:** Kim, Kojaku & Ahn — *Science Advances* 12, eadx3420 (2026)  
**DOI:** 10.1126/sciadv.adx3420  
**Authors:** Munjung Kim, Sadamori Kojaku, Yong-Yeol Ahn (Indiana University / Virginia)  
**Data/code:** https://doi.org/10.5281/zenodo.18404243

## What It Is

A neural embedding-based disruptiveness metric for scientific papers. Trained on 55M+ papers (Web of Science + APS), EDM learns two vectors per paper from citation network structure and measures their divergence as a disruption score.

## The Formal Definition

$$\Delta_i = 1 - \frac{f_i \cdot p_i}{|f_i||p_i|}$$

Cosine *distance* (not similarity) between:
- **Past vector** $p_i$ — aligns with antecedent papers (what paper $i$ cites, within $c$ citation steps)  
- **Future vector** $f_i$ — aligns with descendant papers (what cites paper $i$, within $c$ citation steps)

Cosine distance is used specifically to exclude vector norm effects, which reflect citation frequency ("attractiveness") — information the metric deliberately excludes.

## Training Objective

Directional skip-gram on direction-aware random walks over the citation network. Equivalent to **node2vec** applied to citation trajectories treated as "sentences," but with the window constrained to a single direction:

$$\mathcal{J} \approx \sum_{u \in V} \sum_{v \in A_c(u)} \kappa^{in}_u \log \Pr(v|u)$$

where $A_c(u)$ = antecedent papers of $u$ within $c$ steps, weighted by in-degree $\kappa^{in}_u$.

**Result:** $f_i$ points toward descendant papers; $p_i$ points toward antecedent papers. When a paper is disruptive, descendants rely less on antecedents — the two clusters diverge in embedding space, pulling $f_i$ and $p_i$ apart.

## Why Cosine Distance Increases for Disruptive Papers

Formally: the cosine distance between $f_i$ and $p_i$ approximates the cosine distance between the *mean future vector of antecedent papers* and the *mean past vector of descendant papers*. This increases as:

$$\sum_{j \in A_c(i)} \sum_{k \in D_c(i)} \log \Pr(j|k)$$

decreases — i.e., as descendant works less rely on antecedent works. This is the embedding analog of the original CD disruption index, but global (entire network) rather than local (1-hop neighborhood).

## Why EDM Outperforms the CD Index

| Property | CD Index (D) | EDM (Δ) |
|---|---|---|
| Score distribution | Highly degenerate, bunches at 0 | Continuous, smooth, high resolution |
| Scope | Local 1-hop citation neighborhood | Global multi-hop network structure |
| Simultaneous discoveries | **Catastrophic failure** | Robust |
| Nobel Prize correlation | Not statistically significant (p > 0.05) | Significant (OR 1.34, p < 0.001) |
| Milestone paper correlation | Not significant | Significant (OR 1.23, p < 0.001) |

### The Simultaneous Discovery Problem

The CD index's critical flaw: when two simultaneously disruptive papers cite each other, a single citation edge can flip D from maximum (+1) to minimum (−1). Examples:

- **J/ψ meson** (November Revolution, 1974): Richter & Ting simultaneously discovered it, cited each other → D dropped from top 1% to bottom 0%. EDM: top 5–7%.
- **Higgs mechanism** (1964): Higgs cited Englert & Brout → Higgs' D dropped from top 1.3% to bottom 0.1%. EDM: both papers top ~4%.
- Same pattern confirmed for: asymptotic freedom in QCD, reverse transcriptase, inelastic electron scattering.

## Bonus Finding: Future Vectors Identify Simultaneous Discoveries

Simultaneous discovery papers — reporting the same breakthrough — tend to be cited in the same conceptual contexts by future work. Therefore their **future vectors cluster as nearest neighbors** in embedding space, independent of citation count.

Empirical validation on APS dataset: of 80 high-citation paper pairs identified as nearest future-vector neighbors published in the same year, **64 (80%) were confirmed simultaneous discoveries**.

This means EDM's embedding space encodes enough conceptual structure to detect simultaneous discoveries without author lists or explicit mutual citations.

## Parameters (Main Results)

- Embedding dimension: $d = 100$
- Window size: $w = 5$  
- Walk length: 160 (WoS), 80 (APS)
- Results robust across parameter variations

## Limitations

1. Temporal analysis requires full retraining (computationally expensive)
2. Fails for papers with very few citations/references (excluded from random walks)
3. Less interpretable than topology-based CD index
4. Cannot detect simultaneous discoveries in isolated scholarly communities (e.g., Cook-Levin theorem across US/Soviet boundary)
5. Grounded in citation behavior — reflects sociological processes, not pure conceptual contribution

## Connections

- [[causal-state-edm-ood-isomorphism]] — theoretical grounding via epsilon machines and lumpability
- [[graphrag]] — citation graphs as retrieval and analysis substrate  
- [[zettelkasten-engine]] — disruption score applicable as insight curation signal
- [[persistent-knowledge-compilation]] — disruptive papers break compiled knowledge bases
