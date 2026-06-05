# Batch Progress — Librarians-Assistant 2026-06-05

## Summary
- **61 fixes applied** (1 self-link removal + 60 bulk normalizations)
- **Resolved**: EFHF HITS phantom authority node
- **Carryover updated**: see `carryover.md`

## Fixes Applied

### Priority 1a — HITS Phantom Self-Link Removal
1. `wiki/entities/projects/efhf.md` — removed `- [[efhf]]` self-referential wikilink from Connections section

### Priority 1b — Bulk Bare-Slug Wikilink Normalization
Normalized `[[efhf]]` → `[[entities/projects/efhf]]` in 60 files:
- `wiki/concepts/agent-native-design.md`
- `wiki/concepts/agentic-research.md`
- `wiki/concepts/bounded-rationality.md`
- `wiki/concepts/eml-operator.md`
- `wiki/concepts/epistemic-energy.md`
- `wiki/concepts/maximum-occupancy-principle.md`
- `wiki/concepts/mcp-model-context-protocol.md`
- `wiki/concepts/mop-next-token-prediction.md`
- `wiki/concepts/motion-understanding.md`
- `wiki/concepts/open-ended-evolution.md`
- `wiki/concepts/seg-molecular-self.md`
- `wiki/concepts/synthetic-data.md`
- `wiki/concepts/vision-language-alignment.md`
- `wiki/concepts/working-memory.md`
- `wiki/entities/people/tyler-hall.md`
- `wiki/entities/projects/meta-harness.md`
- `wiki/entities/projects/mop-explorer.md`
- `wiki/entities/projects/tys-repos.md`
- `wiki/entities/projects/tys-repos/advanced-reasoning-mcp.md`
- `wiki/entities/projects/tys-repos/agem.md`
- `wiki/entities/projects/tys-repos/conscience-servitor.md`
- `wiki/entities/projects/tys-repos/graph-rlm.md`
- `wiki/entities/projects/tys-repos/hipai-montague.md`
- `wiki/entities/projects/tys-repos/mcp-coordinator.md`
- `wiki/entities/projects/tys-repos/mcp-logic.md`
- `wiki/entities/projects/tys-repos/nexus.md`
- `wiki/entities/projects/tys-repos/project-synapse-mcp.md`
- `wiki/entities/projects/tys-repos/sheaf-consistency-enforcer.md`
- `wiki/entities/projects/tys-repos/verifier-graph.md`
- `wiki/entities/tools/hipai-montague.md`
- `wiki/entities/tools/mcp-logic.md`
- `wiki/sources/articles/agem-cycle-reflexive-honest-messenger.md`
- `wiki/sources/papers/akbe.md`
- `wiki/sources/papers/alphaproof-nexus-formal-proof-search-2026.md`
- `wiki/sources/papers/awarevln-self-aware-vision-language-navigation-2026.md`
- `wiki/sources/papers/bae-lmac-2026.md`
- `wiki/sources/papers/behavioral-credibility-trilemma.md`
- `wiki/sources/papers/boiling-frog-agentic-safety-2026.md`
- `wiki/sources/papers/cua-gym.md`
- `wiki/sources/papers/forecasting-scientific-progress-ai-2026.md`
- `wiki/sources/papers/legalsearch-r1.md`
- `wiki/sources/papers/proxy-based-shapley-banzhaf-2026.md`
- `wiki/sources/papers/shannon-scaling-law-2026.md`
- `wiki/sources/papers/skill-consumption-2026.md`
- `wiki/sources/papers/skillopt-self-evolving-2026.md`
- `wiki/sources/papers/sleep-self-modify-consolidate-2026.md`
- `wiki/sources/papers/stepopsd.md`
- `wiki/sources/papers/tokenisation-convex-relaxations-2026.md`
- `wiki/sources/papers/utimula-openpraparat-2025.md`
- `wiki/sources/papers/why-llms-arent-scientists-yet.md`
- `wiki/sources/papers/xu-envfactory-2026.md`
- `wiki/sources/repositories/agem.md`
- `wiki/sources/repositories/nexus.md`
- `wiki/synthesis/causal-state-edm-ood-isomorphism.md`
- `wiki/synthesis/cross-layer-drift-falsification.md`
- `wiki/synthesis/efhf-mcp-configuration.md`
- `wiki/synthesis/intelligence-as-entropic-sculpting.md`
- `wiki/synthesis/minimal-generative-architectures.md`
- `wiki/synthesis/mop-edm-cognitive-architecture.md`
- `wiki/synthesis/seg-scientist-agent-design.md`

## HITS Verification (Post-Fix)
- `entities/projects/efhf` authority: 0.0057 (consolidated from bare-slug phantom at 0.0053)
- Bare `efhf` hub: 0.0026 (residual from index.md/concept-index.md only — excluded files)
- Other phantoms (MOP hub 0.0030, LBR hub 0.0021): residual from index.md only — not actionable