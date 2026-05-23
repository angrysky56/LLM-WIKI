# Researcher Discovery Report — 2026-05-29

## Discovery Cycle
- Topics researched: 4
- New pages created: 0 (filled stubs)
- Pages updated: 4 (agentic-hierarchy, scaling-laws, emergence, delegation — all stub → active)
- Cross-links added: ~15 new wikilinks across the four pages
- Confidence improvements: 4 pages moved from 0.3 → 0.8+

## New Entries
*(none — all work was stub-filling)*

### Filled Stubs

**[[agentic-hierarchy]]** (stub → active, confidence: 0.3 → 0.8)
- Filled with organizational patterns: supervisor-worker, manager-specialist, orchestrator-delegator, recursive decomposition
- Added key challenges (coherence across levels, credit assignment, information flow)
- Connected to hermes-agent, bounded-structured-memory, subagent-delegation, markovian-carryover

**[[scaling-laws]]** (stub → active, confidence: 0.3 → 0.85)
- Expanded from stub notes to full treatment of Kaplan/Chinchilla/Hoffmann findings
- Added power-law mathematical form, compute-optimal training vs inference-time scaling
- Table of emergent capability thresholds by scale
- Connections to inference-time-compute-scaling, emergence, mixture-of-experts, chinchilla

**[[emergence]]** (stub → active, confidence: 0.3 → 0.8)
- Full definition of emergence in LLM context (sudden capability appearance at scale thresholds)
- Coverage of the real-vs-metric-artifact debate (Wei et al. 2022 vs Schaeffer et al. 2023)
- Known emergence threshold table
- Connection to scaling-laws (explains tension between smooth power-law loss and discontinuous capability appearance)

**[[delegation]]** (stub → active, confidence: 0.3 → 0.8)
- Filled from stub to full concept: definition, what gets delegated vs retained, delegation mechanics
- Hermes-specific delegate_task patterns (flat, hierarchical, market-based)
- Delegation vs planning comparison table
- Open questions on granularity, cost-benefit, trust/verification, cross-model delegation

## Gap Analysis
- **Verifier-graph theory** — still unresolved. Entity page exists at `wiki/entities/projects/tys-repos/verifier-graph.md`. No concept page. Needs Ty decision: concept or synthesis?
- **Adaptive budget learning** — how to train gating models for difficulty estimation. No clear paper yet.
- **Hybrid reward models** — combining ELHSR (hidden-state) with SD-Search (process-level). Emerging direction.
- **MoE routing collapse under RLHF** — empirical question, no published data yet. Continue monitoring.

## Open Questions
- [ ] Verifier-graph classification decision — Ty input needed
- [ ] Adaptive budget learning — no paper yet, monitoring
- [ ] Hybrid reward models — no full treatment yet
- [ ] MoE+RLHF routing collapse — monitoring for empirical data
- [ ] Self-correction depth — SD-Search result suggests implicit self-correction more capable than assumed; needs follow-up

## Heading
- **Next cycle**: If Ty resolves verifier-graph decision, treat it as the top priority. Otherwise continue stub-filling — the `governance`, `institutional-capture`, `computational-irreducibility` cluster remains thin. `computational-irreducibility` links to `emergence` and `open-ended-evolution` — could be a generative cycle if all three were fleshed out.