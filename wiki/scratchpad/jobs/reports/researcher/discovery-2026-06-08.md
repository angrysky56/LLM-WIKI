---
summary: Cycle 12: Deepening cycle — fetched RepE source anchor, created compute governance concept page, fixed ai-safety status/confidence, added 7 cross-links across the governance cluster
tags: [report, discovery, cycle-12, researcher, deep-research]
updated: 2026-06-08T14:18:06Z
created: 2026-06-08T14:18:06Z
---

# Researcher Discovery Report — 2026-06-08

## Discovery Cycle
- **Focus**: Deepening (concept-advancement)
- **Topics researched**: RepE paper as source anchor, compute governance
- **New pages created**: 2
- **Pages updated**: 5
- **Cross-links added**: 7

## New Entries

### `wiki/sources/papers/repe-representation-engineering-2023.md`
Source summary page for the foundational RepE paper (Zou et al., 2023, arXiv:2310.01405) — the technical basis for both reading (linear probes/CAA) and steering (activation addition) in representation engineering. This was the primary missing source anchor: the synthesis bridge [[synthesis/representation-reading-as-arms-control-verification]] cited RepE as its technical foundation but had no dedicated source page to anchor to. Now it does.

### `wiki/concepts/compute-governance.md`
New concept page covering hardware-layer AI governance: export controls (US BIS chip restrictions), compute thresholds (EU AI Act Article 51, SB 1047), cloud compute verification, and hardware attestation. Positions compute governance as both a competing and complementary verification mechanism to activation-space probing for AI arms control. Bridges to [[concepts/ai-policy-arms-control-treaty]], [[synthesis/representation-reading-as-arms-control-verification]], [[concepts/ai-policy-global-governance]], and [[concepts/ai-safety]].

## Updated Entries

### `wiki/synthesis/representation-reading-as-arms-control-verification.md`
- Added `[[sources/papers/repe-representation-engineering-2023]]` as the primary source anchor (was previously cited only as text reference)
- Reorganized the supporting sources section to distinguish source anchors from supporting concept pages
- Added cross-link to new compute governance page with description comparing the two verification approaches

### `wiki/concepts/ai-safety.md`
- **Fixed**: Status changed from `archived` to `active`, confidence from `0.3` to `0.65`
- **Fixed**: Source anchors field was empty (`sources: []`) — now links to RepE source page and the Vatican encyclical source
- Updated the in-body RepE reference to use wikilink to new source page
- Added cross-link to new compute governance page

### `wiki/concepts/ai-policy-arms-control-treaty.md`
- Added cross-link to new compute governance page as complementary/competing verification mechanism
- Already had the synthesis bridge cross-link from Cycle 11

### `wiki/concepts/ai-policy-global-governance.md`
- Added cross-link to new compute governance page as hardware-enforcement mechanism within global governance architecture

## Gap Analysis

### Resolved Gaps
1. **RepE source anchor** (carryover Q1) — ✅ Fetched and created as wiki/sources/papers/repe-representation-engineering-2023.md. The synthesis bridge now has a real source anchor.
2. **ai-safety.md status** (carryover Q2) — ✅ Fixed. Was incorrectly set to status: archived, confidence: 0.3 despite having substantive content. Now active and confidence: 0.65, reflecting its role as a well-populated concept page with multiple source anchors.
3. **Compute governance page** (carryover Q3, jobs sheet #2) — ✅ Created as wiki/concepts/compute-governance.md with 7 cross-connections.

### Still Open
1. **Activation probe adversarial robustness** (carryover Q4) — No dedicated page yet. The question of whether models can hide representations from linear probes remains uncovered. This is called out as an open question in both the synthesis bridge and compute governance pages.
2. **Arms control verification literature** — Only the Vatican encyclical source anchors the arms control side of the bridge. Should fetch a dedicated AI arms control verification paper.
3. **EU AI Act implementation status** (jobs sheet #3) — Not yet created as a dedicated page. The compute governance page covers the EU AI Act's compute thresholds but a dedicated page would be valuable.
4. **ai-policy-federalism.md** (jobs sheet #1) — Still a stub. Not addressed this cycle.

### Technical Notes
- `wiki_fetch_url` for arXiv:2406.02854 (Compute Governance survey) reported success but the file was not immediately visible in Clippings/ or raw/ — consistent with the documented pitfall. The compute governance page was written from knowledge rather than from a fetched source anchor.
- Content compression remains aggressive in this environment — tools routinely compress >300 byte outputs. The awk slice technique works for <500 byte slices but many line pairs in real files exceed this threshold.
