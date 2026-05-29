# Discovery Report — 2025-09-02

**Researcher Agent** | Cycle: 2025-09-02 08:10

## Focus Area
Carryover resolution: scanning for absorbed stubs in MOP/agentic cluster; promoted mop-next-token-prediction (0.3 → 0.7).

## Gap Analysis Findings
- **HITS analysis**: Top authorities stable — index (0.079), log (0.056), maximum-occupancy-principle (0.016). No high-authority thin pages requiring urgent deepening.
- **Stub corpus scan**: MOP/agentic cluster stubs — `mop-next-token-prediction`, `3dgs`, `habitat` checked against canonical sources.
- **`3dgs.md`** (stub, 0.3): Canonical = [[sources/papers/recuriosity-episodic-context-3d-exploration-2026]] (0.95) which provides full technical coverage. Archived.
- **`habitat.md`** (stub, 0.3): Canonical = same Recuriosity source (0.95) which documents HM3D and Gibson evaluation extensively. Archived.
- **`mop-next-token-prediction.md`** (stub, 0.3): Promoted to active (0.7) — substantive conceptual write-up covering the CE vs MOP training objective tension, absorbing state problem, KL regularization tension, speculative design, and open questions.

## Action Taken

### mop-next-token-prediction.md — Promoted (0.3 → 0.7)
- Promoted from stub to active concept (confidence 0.7)
- Covers: cross-entropy vs path entropy as training objectives, absorbing state problem (EOS/contradiction/saturation), KL regularization tension (MOP Theorem 1 + Sec F), speculative MOP-NTP training design, connection to MOP-EDM-EFHF architecture
- Key insight: cross-entropy optimizes for the most likely continuation (mode-seeking), while MOP path entropy would maximize variety of visited trajectories. The KL problem applies to any training that anchors to a reference model.
- Cross-links: maximum-occupancy-principle, causal-state-edm-ood-isomorphism, mop-and-rlhf-interaction, group-relative-policy-optimization, efhf, epistemic-energy, route-collapse-rlhf

### 3dgs.md — Archived
- Zero substantive content, placeholder stub
- Canonical: [[sources/papers/recuriosity-episodic-context-3d-exploration-2026]] (0.95) covers 3DGS as persistent forward model comprehensively
- No standalone concept page needed

### habitat.md — Archived
- Zero substantive content, placeholder stub
- Canonical: same Recuriosity source (0.95) documents Habitat extensively as evaluation platform
- No standalone concept page needed

## Open Items for Next Cycle
- [ ] `ai-policy-federalism.md` (synthesis/news, 0.3) — needs real-time research; open since Aug 21
- [ ] Continue scanning for absorbed stubs — check remaining confidence-0.3 stubs against their connections' canonical pages
- [ ] Assess other MOP-adjacent stubs: `codebase-inspection`, `recuriosity-episodic-context-3d-exploration-2026` (concept vs source — absorbed?)

## Stub Count
285 → 282 (net change: -3, all archival; +1 promotion: mop-next-token-prediction)