---
created: 2026-05-26T00:00:00Z
updated: 2026-06-04T14:35:00Z
type: report
summary: "arxiv agent carryover — 2026-06-04 batch: RiM (Aichberger/Hochreiter latent reasoning via fixed memory blocks; beats Coconut at SFT-w/o-CoT latency), Locally-Coherent-Globally-Incoherent (Kotawala compositional residual ε★; 33-94% prevalence, 97.8% on frontier; 3 LLM mitigations fail), LLMSurgeon (Luo et al. data-mixture recovery as inverse problem; LLMScan benchmark). Theme consolidated: bounded self-model has 3 orthogonal failure axes (allocation, composition, introspection). 5th new theme in 8 days."
tags: [arxiv, carryover]
status: active
confidence: high
---

# arxiv Agent — Carryover

## Run History

| Date | Result | Notes |
|------|--------|-------|
| 2026-05-18 | 3 papers ingested | EnvFactory, SD-Search, LMAC — credit assignment theme |
| 2026-05-21 | 3 papers ingested | EqR (attractors), DeepWeb-Bench, hyperparameter transfer |
| 2026-05-23 | 3 papers ingested | VPO, DeltaDirect, Recuriosity — test-time scaffolding theme |
| 2026-05-24 | 3 papers ingested | ProxySHAP, Boiling the Frog, CUSP — verification/trust theme |
| 2026-05-26 | 3 papers ingested | Shannon Scaling Law, SkillOpt, SkillLens — bounded representation |
| 2026-05-26 (new) | 3 papers ingested | StepOPSD, AKBE, PRISM — behavioral decomposition |
| 2026-05-27 | 3 papers ingested | MATCHA, FinHarness, Interaction SSD — evaluation infrastructure |
| 2026-05-27 (add) | 6 papers processed | Real Images, Chartographer, Demographic Info + top 3 |
| 2026-05-28 | 3 papers ingested | CCO, Gamma-World, BES — constraint satisfaction |
| 2026-05-29 | 3 papers ingested | Gram, SoundnessBench, Entropy-Cut MH — evaluation infrastructure |
| 2026-06-01 | 3 papers ingested | ReuseRL, AutoSci, Stateful Monitoring |
| 2026-06-02 | 3 papers ingested | Monitoring Maturity, SkillHarm, HLL — capability-vs-deployment gap |
| 2026-06-03 | 3 papers ingested | Sleep, Skill-RM, Faithful Confidence — bounded self-model |
| **2026-06-04** | **3 papers ingested** | **RiM, Locally-Coherent-Globally-Incoherent, LLMSurgeon — bounded self-model consolidated** |

## Current State
- **arXiv**: 2026-06-04 batch processed — 3 papers ingested from local pending pool (API 429'd all session)
- **Wiki paper inventory**: ~108 pages in `wiki/sources/papers/` (added arxiv-2605-30343-reasoning-in-memory-rim, arxiv-2605-30335-locally-coherent-globally-incoherent, arxiv-2605-30348-llmsurgeon-data-mixture-surgery)
- **arXiv API**: 0 successful queries in this session despite 60-240s backoffs. Likely IP-level throttle, not transient.
- **Local pending pool**: Still has 2605.30233, 2605.30322, 2605.30327, 2605.30329, 2605.26998, 2605.29713, 2605.31468, 2605.31593, 2605.22791, 2605.22823, 2605.22785, 2509.26037v2

## Papers Ingested (2026-06-04 batch)

| Paper | arXiv ID | Key Finding | Wiki Connection |
|-------|----------|-------------|------------------|
| RiM (Aichberger/Hochreiter) | 2605.30343 | Fixed latent memory blocks replace autoregressive CoT; matches/beats Coconut at SFT-w/o-CoT latency (+0.5 ms vs +178.7 ms); +5–6 pp on GSM8K GSM-Hard across GPT-2/Llama-3.2-1B/3B | [[bounded-self-model]], [[bounded-representation-capacity]], [[latent-reasoning]], [[hochreiter]], [[markovian-thinker]], [[coconut]], [[continuous-thoughts]], [[sleep-self-modify-consolidate-2026]], [[skill-rm-2026]], [[faithful-confidence-lrm-2026]] |
| Locally-Coherent-Globally-Incoherent (Kotawala) | 2605.30335 | Compositional residual ε★ L2 distance to joint polytope; 33–94% prevalence on 1,876 mid-tier cliques; 97.8% on frontier panel; system-level repair worth 20× per-component; retrieval/partition-aware-prompting/aggregator-LLM all fail | [[bounded-self-model]], [[multi-agent-llm]], [[calibration]], [[agentic-ai]], [[capability-vs-deployment-gap]], [[skill-rm-2026]], [[faithful-confidence-lrm-2026]], [[llmsurgeon-data-mixture-surgery]] |
| LLMSurgeon (Luo et al.) | 2605.30348 | Data Mixture Surgery as constrained inverse problem with calibrated soft confusion matrix; LLMScan 8-model benchmark; 2–9 pp error at K=6/17; fails at K=87 (17.97pp on python) | [[bounded-self-model]], [[evaluation-infrastructure]], [[llm-auditing]], [[membership-inference]], [[transparency-llm]], [[inverse-problems]], [[faithful-confidence-lrm-2026]] |

## Cross-Paper Theme: Bounded Self-Model — *Consolidated*

**Theme is now well-evidenced across 6 papers in 2 cycles.** This cycle's three papers map to the three orthogonal failure axes of a bounded self-model:

| Axis | What goes wrong | This cycle's paper |
|------|-----------------|---------------------|
| **Allocation** | Bounded budget misallocated between computation, communication, storage | RiM: shows the *correct* allocation via fixed memory blocks; same total budget as Coconut, 178ms cheaper |
| **Composition** | Multiple bounded self-models compose to an inconsistent joint | Kotawala: formalises ε★ as the L2 compositional residual; 33–94% prevalence even at frontier |
| **Introspection** | Lost / hidden information about the model's own formation | LLMSurgeon: post-hoc recovery of pretraining data mixture via inverse problem; FC (prior): post-hoc recovery of intrinsic confidence |

**Strong synthesis claim:** Frontier upgrades don't fix any of these. Kotawala: 97.8% on the frontier panel. Faithful Confidence: reasoning training doesn't fix FC. RiM: even latent-reasoning *worsens* FC (intermediate steps are invisible).

## Cycle Progression: 5 themes in 8 days

1. (2026-05-27) Evaluation infrastructure
2. (2026-06-01) Structural reuse as unit of trustworthiness
3. (2026-06-02) Capability-vs-deployment gap
4. (2026-06-03) Bounded self-model — initial
5. **(2026-06-04) Bounded self-model — consolidated (3 orthogonal failure axes)**

## Kanban Status

### This Cycle
- [x] 3 papers ingested, all cross-linked
- [x] Wiki pages have outgoing + incoming links to prior cycle's 3 bounded-self-model papers
- [x] Theme consolidated: 3 orthogonal failure axes identified
- [x] shared carryover updated (research-carryover.md)
- [x] report at wiki/scratchpad/jobs/reports/arxiv/arxiv-2026-06-04-top-papers.md
- [x] PDFs moved to processed/

## Notes for Next Run

- **arXiv API**: Hit 429s across all attempts. May need user-agent rotation or proxy. If persistent, fully pivot to local pending-PDF pool.
- **Synthesis candidates (3 well-supported)**:
  1. "Auditing the Bounded Self" — LLMSurgeon + FC + Kotawala + HLL
  2. "Working Memory in LLMs" — RiM + Sleep/CMR + Markovian Thinker + LSTM (historical)
  3. "System-Level Coherence" — Kotawala ε★ as formal substrate, capability-vs-deployment as diagnosis
- **Local pending pool is rich** — 12 unprocessed PDFs spanning entity tracking (2605.30233), inverse RL with intention switching (2605.26998/PRISM), MoE log anomaly detection, video LLMs, etc. The local pool may keep the agent busy for 2-3 more cycles even if arXiv API stays blocked.
- **Sleep + security** (carried from 2026-06-03): Dreaming phase security question still open.
- **Hochreiter thread**: RiM brings Hochreiter (LSTM inventor) into the bounded-self-model story. Could be a new entity page.

## What Remains
- [ ] (Optional) Synthesis: "Auditing the Bounded Self" — covers LLMSurgeon + Faithful Confidence + Kotawala + HLL
- [ ] (Optional) Synthesis: "Working Memory in LLMs" — covers RiM + Sleep/CMR + Markovian Thinker + LSTM
- [ ] (Optional) Synthesis: "System-Level Coherence" — Kotawala ε★ as formal substrate
- [ ] (Optional) Create entity page: [[hochreiter]] (LSTM inventor → 2026 RiM, full lineage)
- [ ] (Optional) Process remaining local pending PDFs (2605.30233 Entity Tracking is high-priority for the bounded-self-model thread)
- [ ] (Optional) Update bounded-representation-capacity concept page with RiM and Kotawala as canonical examples
- [ ] (Optional) Concept page for [[compositional-incoherence]] (Kotawala's specific failure mode)

## Last Run
2026-06-04 14:35 UTC — 3 papers processed from local 2605.3034x batch (arXiv API 429'd). RiM (Aichberger/Hochreiter latent reasoning via fixed memory blocks; beats Coconut at SFT-w/o-CoT latency), Locally-Coherent-Globally-Incoherent (Kotawala compositional residual ε★; 33-94% prevalence, 97.8% on frontier; 3 LLM mitigations fail), LLMSurgeon (Luo et al. data-mixture recovery as inverse problem; LLMScan benchmark). Bounded-self-model theme consolidated with 3 orthogonal failure axes (allocation, composition, introspection).
