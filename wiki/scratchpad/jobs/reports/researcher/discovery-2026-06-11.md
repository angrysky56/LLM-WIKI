# Researcher Discovery Report — 2026-06-11

## Discovery Cycle
- Topics researched: 2
- New pages created: 2
- Pages updated: 3
- Cross-links added/repaired: ~12

## Focus
Concept Advancement — governance cluster completion. Primary sub-skill: concept-advancement.

## New Entries

### wiki/concepts/ai-policy-federalism.md (79 lines)
US federal AI governance page covering:
- Trump administration regulatory retreat (May 2026) — abandoned AI model vetting
- Historical context of U.S. light-touch approach vs EU binding regulation
- California as de facto regulator (emissions/privacy precedent applied to AI)
- Other active states: NY, Colorado, Texas, Washington
- Preemption tensions — express, field, and conflict preemption analyses
- Practical dynamics of large-market state regulation setting national standards
- 6 source anchors and 4 open questions

### wiki/concepts/eu-ai-act-implementation.md (82 lines)
EU AI Act implementation page covering:
- Risk-based framework with 4-tier categorization table
- Foundation model provisions (2025 amendment) with compute thresholds
- Implementation timeline through 2027
- Enforcement architecture (European AI Office, national authorities, penalties up to 7% turnover)
- Vatican/encyclical validation of EU approach (May 2026)
- Implementation challenges: member state divergence, SME burden, standards gap
- Brussels effect analysis with regulatory friction vs US and China
- 5 open questions

## Updated Entries

### wiki/concepts/ai-policy-global-governance.md (67 lines)
**Critical fixes applied:**
- Removed 2 self-links (page was linking to itself)
- Fixed `[[AI-policy-federalism]]` → `[[concepts/ai-policy-federalism]]` (wrong slug case)
- Fixed `[[AI-policy-arms-control-treaty]]` → `[[concepts/ai-policy-arms-control-treaty]]` (wrong slug case)
- Fixed `[[trump-abandons-ai-model-vetting-may-2026]]` → `[[sources/articles/trump-abandons-ai-model-vetting-may-2026]]` (missing path prefix)
- Fixed `[[pope-leo-ai-encyclical...]]` → `[[sources/articles/pope-leo-ai-encyclical...]]` (missing path prefix)
- Fixed `[[concepts/sovereign-ai.md]]` → `[[concepts/sovereign-ai]]` (removed .md extension)
- Added `[[concepts/eu-ai-act-implementation]]` link for EU model contrast
- Deduplicated 3 duplicate eu-ai-act links caused by replacement logic error

### wiki/concepts/compute-governance.md (101 lines)
Added reciprocal cross-links to:
- `[[concepts/eu-ai-act-implementation]]` — EU compute thresholds for systemic-risk designation
- `[[concepts/ai-policy-federalism]]` — federal fragmentation complicates hardware-layer governance

### wiki/concepts/ai-policy-arms-control-treaty.md (92 lines)
Added reciprocal cross-links to:
- `[[concepts/eu-ai-act-implementation]]` — EU approach as binding treaty template
- `[[concepts/ai-policy-global-governance]]` — broader governance architecture context
- `[[concepts/ai-policy-federalism]]` — federal fragmentation complicates treaty negotiation

## Cluster Status
The governance/verification cluster is now structurally complete with 5 concept pages:

| Page | Lines | Status |
|------|-------|--------|
| ai-policy-arms-control-treaty.md | 92 | Established |
| compute-governance.md | 101 | Established |
| ai-policy-global-governance.md | 67 | Fixed & expanded |
| ai-policy-federalism.md | 79 | **NEW** |
| eu-ai-act-implementation.md | 82 | **NEW** |

Cross-link graph shows all 5 pages now mutually reachable with proper reciprocal links.

## Gap Analysis
- **[MED]** Compute governance survey source page (arXiv:2406.02854) — cited in treaty page, no source summary exists. Fetch still failing.
- **[MED]** Nonlinear probe/erasure duality empirical test paper — open question from previous synthesis bridge. Worth researching if wiki_fetch_url becomes reliable.
- **[LOW]** Trump admin internal debate on AI governance — mentioned in sheet.md discovery areas, could become a distinct page or a section of federalism.

## Carryover Updates
- Carryover's HIGH priority item (global-governance page creation) resolved — page already existed, required repair instead.
- New HIGH priority established: ensure governance cluster cross-links are maintained as cluster grows.
- New MED priority: source-anchor the governance cluster pages with real source summaries when fetch capability restored.

## Verification Notes
- **wiki_fetch_url**: Made one attempt (artificialintelligenceact.eu) — appeared to succeed but file did not produce in a visible window. Pages written from training knowledge with confidence ≤ 0.75.
- **Confidence**: Both new pages written at confidence 0.70 — solid training knowledge but unverified against live sources.
- **Cross-link repair**: 3 broken links and 2 self-links identified and fixed in the existing global-governance page. Critical fix — self-links can cause infinite traversal in graph queries.

## Open Questions
- Does the sovereign-ai concept page need expansion to integrate with the governance cluster?
- Should the governance cluster become a bridge cluster to sovereign-AI / defense-AI concepts?
- Does the Vatican encyclical source page exist or is it an unresolved wiki_fetch_url artifact?