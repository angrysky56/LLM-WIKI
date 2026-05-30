---
created: 2026-05-22
updated: 2026-05-30
type: source
summary: "Essan vector encoding: symbol-only random encoding has no semantic signal; hybrid (symbol+NL) achieves 0.86 correlation with NL; hallucinated sequences detectable at 87.5% rate"
tags: [essan, vector-encoding, embeddings, semantic-similarity, hallucination-detection]
sources: 
status: active
confidence: 0.85
---

# Essan Vector Space Encoding Test Results

**Date:** May 22, 2026 | **Methodology:** Random unit vector encoding in 128-dimensional space; cosine similarity; cluster analysis

## Test A: Symbol-Only Encoding

**Mean upper-triangle similarity:** 0.7155 (high overlap due to shared symbol components, not semantic intent)

**Key pairwise similarities:**
- Core Pathway ↔ Short Variant: 0.9499 (shared `⧬⦿⧈⫰` prefix)
- Cycle Structure ↔ Simple Variant B: 0.9499 (shared `⧿⧬⦿⫰◬⧉` structure)

**Finding:** High clustering is a mathematical artifact of symbol overlap, not semantic clustering.

## Test B: Hybrid vs Symbol-Only vs Pure NL

| Encoding Pair | Mean Similarity |
|---------------|-----------------|
| Symbol-only ↔ Pure NL | **-0.0344** (essentially uncorrelated) |
| Hybrid ↔ Pure NL | **0.8623** (very high) |
| Symbol-only ↔ Hybrid | 0.4719 |

**Finding:** Hybrid encoding (60% symbol + 40% NL scaffold) bridges to natural language; symbol-only alone carries no semantic signal.

## Test C: Hallucination Detection

**Well-formed vs malformed sequences projected to embedding space:**

| Metric | Well-Formed | Malformed |
|--------|-------------|-----------|
| Mean similarity to WF centroid | **0.7087** | **0.2919** |
| Detection rate | — | **87.5%** (7/8) |

**Finding:** Malformed (hallucinated/incomplete) sequences project as detectable outliers at 87.5% rate with 0.42 separation gap.

## Summary

| Hypothesis | Result | Key Metric |
|------------|--------|------------|
| Symbol-only sequences cluster by semantic similarity | ⚠️ PARTIAL | Mean sim=0.72 (artifact of symbol sharing) |
| Hybrid encoding closer to NL than symbol-only | ✓ CONFIRMED | Gain=+0.897 |
| Malformed sequences detectable as outliers | ✓ CONFIRMED | 87.5% detection rate |

## Conclusions

1. **Symbol-only random encoding is not semantic** — high clustering is mathematical artifact
2. **Hybrid encoding effectively bridges symbols and NL** — NL scaffold dominates
3. **Hallucination detection is viable** — outlier projection successfully identifies structurally incomplete sequences
4. **Limitation:** "Malformed" cases were manually constructed; more rigorous testing needed

## Connections

- [[essan-mcp-logic-results]] — FOL formalization shows symbols are structurally consistent; vector test shows they're semantically empty
- [[essan-pidgin-results]] — 0% decode accuracy confirms symbol-only encoding lacks semantic bindings
- [[essan-vgcp-comparative-analysis]] — Essan's symbolic layer lacks VGCP's semantic verification via NLI entailment scoring
