---
created: 2026-05-26T00:00:00Z
updated: 2026-06-05T10:00:00Z
type: report
summary: "arxiv agent carryover — 2026-06-05 batch: Gated DeltaNet-2 (NVIDIA erase/write decoupling in linear attention), AI Chatbots as News Intermediaries (Stanford 14-day RAG evaluation across 6 languages), DeltaDirect (Video-LLM direction binding gap diagnosis + projector-level fix). Theme: last-mile routing bottleneck — 4th axis of bounded self-model. 9 themes in 9 days."
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
| 2026-05-27 | 3 papers ingested | StepOPSD, AKBE, PRISM — behavioral decomposition |
| 2026-05-28 | 3 papers ingested | MATCHA, FinHarness, Interaction SSD — evaluation infrastructure |
| 2026-05-29 | 6 papers processed | Real Images, Chartographer, Demographic Info + top 3 |
| 2026-06-01 | 3 papers ingested | ReuseRL, AutoSci, Stateful Monitoring — structural reuse |
| 2026-06-02 | 3 papers ingested | Monitoring Maturity, SkillHarm, HLL — capability-vs-deployment |
| 2026-06-03 | 3 papers ingested | Sleep, Skill-RM, Faithful Confidence — bounded self-model |
| 2026-06-04 | 3 papers ingested | RiM, Locally-Coherent-Globally-Incoherent, LLMSurgeon — bounded self-model consolidated (3 axes) |
| **2026-06-05** | **3 papers ingested** | **Gated DeltaNet-2, AI Chatbots as News Intermediaries, DeltaDirect — last-mile routing bottleneck (4th axis)** |

## Current State
- **arXiv API**: 3 consecutive 429s — fully blocked. Pending pool used (2605.22791, 2605.22785, 2605.22823).
- **Wiki paper inventory**: ~111 pages in `wiki/sources/papers/` (added 3 new, replaced 1 stub)
- **Pending pool decreasing**: ~5 unprocessed PDFs remain (2605.26998, 2605.22779, 2605.22776, 2605.22773, 2605.22738, 2605.22681, 2605.15156, 2509.26037)

## Papers Ingested (2026-06-05 batch)

| Paper | arXiv ID | Key Finding | Wiki Connection |
|-------|----------|-------------|------------------|
| Gated DeltaNet-2 (NVIDIA) | 2605.22791 | Decouples erase/write gates in linear attention memory editing. Channel-wise erase gate (key-side) and write gate (value-side). Best 1.3B among Mamba-2, GDN, KDA, Mamba-3. +11.6pp MK-NIAH over KDA. | [[bounded-self-model]] (allocation axis), [[linear-attention]], [[continual-learning]], [[markovian-thinker]] |
| AI Chatbots as News Intermediaries (Stanford) | 2605.22785 | 14-day eval of 6 production chatbots on 2,100 news questions across 6 BBC languages. >90% MC, but Hindi gap (−12pp, Anglophone retrieval bias), 70% of errors are retrieval failures, adversarial collapse 88→19%. | [[capability-vs-deployment-gap]], [[evaluation-infrastructure]], [[rag]], [[multilingual]], [[calibration]] |
| DeltaDirect (Kyung Hee/Princeton) | 2605.22823 | Directional motion blindness in Video-LLMs. Direction signal linearly decodable but readout fails to route it. DeltaDirect projector objective improves 25.9% → 85.4%. Replaced stub. | [[bounded-representation-capacity]], [[faithfulness]], [[mechanistic-interpretability]], [[video-llms]] |

## Cross-Paper Theme: Last-Mile Routing Bottleneck

**6th new theme in 9 cycles. Identifies the 4th axis of bounded-self-model.**

All three papers share a structural pattern: **an available internal representation fails to reach the correct output channel through a specific, identifiable bottleneck.**

| Axis | What goes wrong | This cycle's evidence |
|------|-----------------|-----------------------|
| **Allocation** | Bounded budget misallocated | Gated DeltaNet-2: fixed state size forces interference; fixed by decoupled erase/write |
| **Composition** | Multiple bounded models compose inconsistently | Kotawala ε★ (prior) |
| **Introspection** | Model can't inspect its own state | LLMSurgeon (prior): data mixture recovery as inverse problem |
| **Routing (NEW)** | Available representation can't reach output | News Chatbots: evidence-binding bottleneck (70% errors = retrieval routing) + DeltaDirect: direction binding gap (signal decoded but not read out) + Gated DeltaNet-2: scalar gate tied erase to write |

**Synthesis claim added to the bounded-self-model framework:** Routing bottlenecks are structurally distinct from the other three axes — they're about the *path* from representation to action, not the *capacity* of the representation itself. All four axes persist at frontier level.

## What Remains
- [ ] (Optional) Synthesis: "Readout Bottlenecks in LLMs: When Models Know More Than They Say" — covers DeltaDirect + News Chatbots + Faithful Confidence + RiM
- [ ] (Optional) Synthesis: "Auditing the Bounded Self" — LLMSurgeon + Faithful Confidence + Kotawala + HLL
- [ ] (Optional) Process pending PDFs: 2605.26998 (PRISM version?), 2605.22779 (FAME), 2605.15156 (MEMO)
- [ ] (Optional) Try arXiv API again next cycle with fresh user-agent

## Last Run
2026-06-05 10:00 UTC — 3 papers processed from local pending pool (arXiv API 429'd). Gated DeltaNet-2 (NVIDIA erase/write decoupling), AI Chatbots as News Intermediaries (Stanford 14-day 6-language RAG evaluation), DeltaDirect (Video-LLM direction binding gap). Theme: last-mile routing bottleneck — the 4th axis of bounded self-model.