# Discovery Report — 2026-06-01

**Researcher Agent** | Cycle: 2026-06-01 08:10

## Focus Area
Closed out the prior cycle's open list (xgboost, vlm, version-control, ux-design, civil-rights, momoa-researcher, AGEM stub, algebra, scientific-method, retrieval-augmented-generation, concept-index stub) with a single promotion + archival pass. Promoted `shap` to a real concept page; archived 11 absorbed/periphery stubs.

## Gap Analysis Findings
- HITS top authorities: `maximum-occupancy-principle` (0.0152), `efhf` (0.0056), `concept-index` (0.0052), `load-bearing-reasoning` (0.0040), `agentic-research` (0.0035). Top hubs: `maximum-occupancy-principle`, `efhf`, `alphaevolve`, `world-model`, `chain-of-thought` — the MOP/EFHF/agentic cluster dominates.
- Active stub inventory: 219 active stubs in `wiki/concepts/`. Proximity scan to hub cluster (MOP/EFHF/load-bearing-reasoning/agentic-research/alphaevolve/world-model/chain-of-thought) found 81 stubs with ≥1 hub link.
- **Highest-priority real gap discovered**: `shap.md` (model interpretability, links to MOP + tabpfn + proxy-shapley-2026 paper). Genuine AI/ML concept, distinct from `shapley-values.md` (game theory foundation) — the application (feature attribution for ML models) is a separate concept.
- **Absorbed-stub detection**: `retrieval-augmented-generation.md` is a duplicate alias of `rag.md` (1.0). `concept-index.md` is a navigation stub duplicating `wiki/concept-index.md`. `vlm.md` is absorbed by decoupling-perception-reasoning source (0.8). `xgboost.md` is absorbed by tabpfn. `momoa-researcher.md` and `agent-group-evolving-molecular-system-agem.md` are project/mislabelled stubs with no clean canonical target.
- **Non-AI periphery**: `version-control`, `ux-design`, `civil-rights`, `algebra`, `scientific-method` — all outside AI/ML core, no promotion path.

## Action Taken

### shap.md (0.3 → 0.72) — PROMOTED
Full concept page written. Content: definition (axiom-grounded SHAP framework), core idea (cooperative-game formulation, Shapley value formula), why SHAP vs classical Shapley (KernelSHAP/TreeSHAP/DeepSHAP/etc. algorithm variants), tabular algorithm comparison, connections to feature importance vs attribution, model trustworthiness, foundation models (TabPFN ships SHAP, VLMs use ProxySHAP for token attribution per 2026 paper), practical considerations (baseline choice, computational cost, adversarial robustness — Slack 2020 fooling attacks).

Cross-links: [[shapley-values]] (theoretical foundation), [[maximum-occupancy-principle]] (memory commit decisions), [[tabpfn]] (built-in extension), [[sources/papers/proxy-based-shapley-banzhaf-2026]] (2026 SOTA), [[behavioral-credibility-trilemma]] (transparency tool), [[llm-agent-architecture]] (tool selection attribution), [[model-interpretation]] (broader concept).

Open questions section: causal SHAP, SHAP for retrieval/RAG attribution, distribution shift faithfulness, multimodal SHAP (early-stage).

### retrieval-augmented-generation.md — ARCHIVED
Absorbed by [[rag]] (1.0). The graphrag (0.9) and rag (1.0) pages cover RAG comprehensively. This stub was a duplicate alias.

### concept-index.md — ARCHIVED
Navigation stub duplicating `wiki/concept-index.md` (the canonical wiki navigation page per AGENTS.md). The "connections" section was a flat list of wiki links — not concept content. Should never have been a content page.

### version-control.md — ARCHIVED
Developer tooling stub. Related canonical: [[git]] and [[github]] cover the development-context version control. No AI/ML knowledge graph promotion path.

### ux-design.md — ARCHIVED
Non-AI design discipline. Adjacent stubs: [[human-computer-interaction]] and [[information-architecture]] are the application areas. Outside AI/ML core.

### xgboost.md — ARCHIVED
ML library stub. XGBoost is the legacy comparison baseline for [[tabpfn]] (foundation model for tabular data). No concept-page target — the wiki already has tabpfn and tabular foundation models as canonical coverage.

### civil-rights.md — ARCHIVED
US politics stub. Linked to SCOTUS news and voting-rights news — outside AI/ML knowledge graph scope.

### vlm.md — ARCHIVED
Absorbed by [[sources/papers/decoupling-perception-reasoning-vlm-post-training]] (0.8). That source comprehensively covers VLM post-training architecture and the perception/reasoning decoupling finding. The stub adds no new information.

### momoa-researcher.md — ARCHIVED
Project entity stub. Links to [[agentic-research]] (0.8) and [[alphaevolve]] (0.8), both of which cover the MOP-aligned agent research domain fully. MOPOA is a project-internal term, not a wiki concept.

### agent-group-evolving-molecular-system-agem.md — ARCHIVED
**Mislabelled stub**: title claims "agent group architecture with evolutionary molecular dynamics" but the only source link is to `xu-envfactory-2026` (EnvFactory, which is about MCP tool environment synthesis for agentic RL — unrelated to molecular dynamics). No canonical source for the AGEM molecular system concept exists in the wiki. Archive as misnomer.

### algebra.md — ARCHIVED
Math stubs cluster (mathematics, applied-mathematics, numerical-methods, optimization all archived Jun 1). Algebra is foundational but has no AI/ML concept-page target — covered in-context in transformer attention, optimization, and linear-algebra-derived pages.

### scientific-method.md — ARCHIVED
Meta-discipline stub. [[research-methodology]] and [[scientific-reasoning]] are also stubs (weak cluster). [[agentic-research]] (0.8) covers the AI-for-science workflow specifically. No clean promotion target.

## Open Items for Next Cycle
- [ ] Audit remaining active stubs in `wiki/concepts/` with high hub-cluster proximity — especially `synthetic-data.md` (real gap, links to MOP + tabpfn) and `seg-molecular-self.md` (MOP-adjacent, 2 hub hits)
- [ ] Re-scan HITS authorities for any thin-content pages that need deepening (e.g., `load-bearing-reasoning` 0.0040 is a top authority — verify its content density)
- [ ] Check for stubs in `wiki/entities/people/` and `wiki/entities/projects/` matching the previously-archived entity-stub pattern (politics, public-health)
- [ ] Consider promoting `concept-index` as a top-level navigation upgrade (the real `wiki/concept-index.md`) — but that's a librarian/curator task, not researcher

## Stub Count
362 → 362 (confidence: 0.3) — 1 promotion (shap), 11 archives. Net −1 confidence:0.3 files.
291 → 291 (status: stub) — 12 status changes. Net −12 active stubs.
(Index has 1278 pages total.)
