---
summary: Kim, Kojaku & Ahn (Science Advances 2026) — introduces EDM embedding-based disruption metric; outperforms CD index; detects simultaneous discoveries via future vector nearest-neighbor clustering
tags: [EDM, disruption, citation-network, simultaneous-discovery, science-of-science, science-advances, 2026]
updated: 2026-04-11T00:47:00Z
---

# Kim, Kojaku & Ahn — Uncovering Simultaneous Breakthroughs (2026)

**Journal:** *Science Advances* 12, eadx3420 (2026)  
**DOI:** 10.1126/sciadv.adx3420  
**Published:** 1 April 2026  
**Raw file:** `raw/Uncovering simultaneous breakthroughs with a robust measure of disruptiveness.md`

## Abstract (paraphrased)

Progress in science is punctuated by disruptive innovations. The authors introduce EDM — an embedding-based disruptiveness metric — which outperforms the standard CD disruption index by using global multi-hop citation structure rather than local 1-hop topology. Applied to 55M+ papers, EDM reliably identifies Nobel Prize–winning papers and APS milestone papers, and — crucially — recovers simultaneous discoveries that the CD index misclassifies.

## Core Contribution

Two findings of roughly equal importance:

**1. EDM as a better disruption metric**  
Past/future vectors trained via directional skip-gram; cosine distance = disruption score. Validated against 302 Nobel Prize papers and 278 APS milestone papers. CD index is not statistically significant for either benchmark (p > 0.05); EDM is highly significant (OR 1.34 Nobel, 1.23 milestone).

**2. Future vectors detect simultaneous discoveries**  
Papers reporting the same discovery are cited in the same conceptual contexts → their future vectors cluster as nearest neighbors. 80% precision on 80 manually annotated high-citation candidate pairs. Works even when citation counts differ substantially between the papers.

## Key Technical Details

- Training: direction-aware random walks → node2vec-style skip-gram, single-direction window
- Score: Δᵢ = 1 − (fᵢ · pᵢ) / (|fᵢ||pᵢ|)
- Cosine distance chosen specifically to exclude norm effects (citation frequency/"attractiveness")
- Null model: randomized citation network preserving in/out-degree and temporal structure
- Parameters: d=100 dimensions, w=5 window, walk length 160 (WoS) / 80 (APS)

## Simultaneous Discovery Cases

Higgs mechanism, J/ψ meson (November Revolution 1974), asymptotic freedom in QCD, inelastic electron-neutron scattering, reverse transcriptase. In every case, CD index assigned bottom-percentile scores due to mutual citations; EDM correctly scored all top 4–7%.

## Limitations

- Temporal change analysis requires full retraining
- Fails for papers with no/few citations (excluded from random walks)
- Sociological biases in citation behavior propagate into metric
- Isolated scholarly communities produce undetectable simultaneous discoveries (e.g. Cook-Levin theorem)

## Connections

- [[edm-framework]] — full technical entity page with formal math
- [[causal-state-edm-ood-isomorphism]] — theoretical synthesis connecting EDM to epsilon machines and LLM OOD detection
