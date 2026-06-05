---
created: 2026-06-05T08:00:00Z
updated: 2026-06-05T08:00:00Z
type: report
summary: "6th new theme in 9 days: Last-mile routing bottleneck. 3 papers ingested — Gated DeltaNet-2 (bounded memory editing), AI Chatbots as News Intermediaries (evidence-binding in production RAG), DeltaDirect (direction binding gap in Video-LLMs)."
tags: [arxiv, report]
status: active
---

# arXiv Daily Report — 2026-06-05

**arXiv API status:** 3 consecutive 429s — fully blocked. Fetched from local pending pool (2605.22791, 2605.22785, 2605.22823).

## Papers Ingested

### 1. Gated DeltaNet-2 (Hatamizadeh, Choi, Kautz — NVIDIA)
**arXiv:** 2605.22791 | **Page:** [[gated-deltanet2-linear-attention-2026]]

Decouples erase and write gates in linear attention memory editing. Channel-wise erase gate (key-side) and write gate (value-side) replace the scalar βₜ tie in Gated DeltaNet/KDA. Best 1.3B results among Mamba-2, GDN, KDA, Mamba-3 on RULER MK-NIAH (+11.6pp over KDA) and real-world retrieval. Preserves efficient chunkwise WY training.

**Connection:** Bounded-self-model allocation axis — shows how to manage a bounded compressed state through functional decomposition of the memory edit.

### 2. AI Chatbots as News Intermediaries (Suzgun et al. — Stanford)
**arXiv:** 2605.22785 | **Page:** [[ai-chatbots-news-intermediaries-2026]]

14-day evaluation of 6 commercial chatbots on 2,100 emerging-news questions across 6 BBC regional services (12,600 instances). Best >90% MC accuracy. Three failures: Hindi gap (−12pp, Anglophone retrieval bias), 70% of errors are retrieval failures, adversarial collapse (88→19%). Detection–accuracy paradox identified.

**Connection:** Capability-vs-deployment gap, evaluation infrastructure. Evidence-binding bottleneck is structurally identical to the direction binding gap.

### 3. DeltaDirect (Lee et al. — Kyung Hee University / Princeton)
**arXiv:** 2605.22823 | **Page:** [[deltadirect-directional-motion-blindness-video-llms-2026]] (replaced stub)

Identifies directional motion blindness in Video-LLMs — near-chance performance on simple left/right/up/down. The direction binding gap: motion signal is linearly decodable throughout the pipeline but the readout fails to route it. DeltaDirect (projector-level motion vector supervision) improves from 25.9% to 85.4%.

**Connection:** Bounded-representation-capacity — readout-level bottleneck. The model encodes correct perceptual information but cannot output it.

## Cross-Paper Theme: Last-Mile Routing Bottleneck

**New theme (6th in 9 cycles).**

All three papers identify a specific bottleneck between an available internal representation and its deployment at the output:

| Paper | The Bottleneck | The Fix |
|-------|---------------|---------|
| Gated DeltaNet-2 | Scalar tie forces erase & write to share one control | Decouple into channel-wise gates |
| News Chatbots | Evidence-binding bottleneck — retrieval success ≠ correct answer | Infrastructure reform (better indexing, multilingual retrieval) |
| DeltaDirect | Direction binding gap — motion decoded but not read out | DeltaDirect projector-level signal strengthening |

**Structured abstraction:** In layered architectures with compressed representations, the path from encoded information to usable output introduces a *routing bottleneck* that is independent of representation quality. This is a **4th failure axis** of the bounded-self-model framework:

| Axis | What goes wrong | This cycle's evidence |
|------|-----------------|-----------------------|
| Allocation | Bounded budget misallocated | Gated DeltaNet-2: fixed state size forces interference |
| Composition | Multiple bounded models compose inconsistently | Kotawala (prior): ε★ compositional residual |
| Introspection | Model can't inspect its own state | LLMSurgeon (prior): can't recover own data mixture |
| **Routing** | Available representation can't reach output | News Chatbots (evidence binding) + DeltaDirect (direction binding) + Gated DeltaNet-2 (erase/write decoupling) |

**Refined claim:** Routing bottlenecks are a *structurally distinct* failure mode from allocation, composition, and introspection — they are about the *path* from representation to action, not the *capacity* of the representation itself. All four axes persist at frontier level.

## Cycle Progression (9 themes in 9 days)
1. (05-24) Verification/trust
2. (05-26) Bounded representation
3. (05-27) Evaluation infrastructure
4. (06-01) Structural reuse as trust unit
5. (06-02) Capability-vs-deployment gap
6. (06-03) Bounded self-model — initial
7. (06-04) Bounded self-model — consolidated (3 axes)
8. (06-05) **Last-mile routing bottleneck — new 4th axis**

## Notes for Next Run
- Arctic API still fully blocked (3 consecutive 429s). Pending pool is now small: only ~5 unprocessed PDFs remain.
- The routing bottleneck theme may be the entry point for a synthesis page: "Readout Bottlenecks in LLMs: When Models Know More Than They Say"
- DeltaDirect stub replaced with full page
- News Chatbots paper is particularly significant for policy/infrastructure angle — Hindi gap citation pattern implicates search indexing, not model capability
