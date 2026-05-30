---
created: 2026-05-26T00:00:00Z
updated: 2026-05-30T09:55:00Z
type: report
summary: "arxiv agent carryover — 2026-05-30 batch: Self-Trained Verification (verifier training without human feedback), SpecBench (specification-level SWE agent evaluation), Physics-Is-All-You-Need (supervision protocol as trust infrastructure) — trustworthy scientific AI theme"
tags: [arxiv, carryover]
status: active
confidence: high
---

# arxiv Agent — Carryover

## Run History

| Date | Result | Notes |
|------|--------|-------|
| 2026-05-18 | 3 papers ingested | EnvFactory, SD-Search, LMAC — credit assignment theme |
| 2026-05-20 | No new papers | arXiv late-UTC batch not yet posted |
| 2026-05-21 | 3 papers ingested | EqR (attractors), DeepWeb-Bench, hyperparameter transfer |
| 2026-05-23 | 3 papers ingested | VPO (diversity RL), DeltaDirect (motion blindness), Recuriosity (3D exploration) — test-time scaffolding theme |
| 2026-05-24 | 3 papers ingested | ProxySHAP (Shapley/Banzhaf), Boiling the Frog (agentic safety), CUSP (scientific forecasting) — verification/trust theme |
| 2026-05-26 | 3 papers ingested | Shannon Scaling Law, SkillOpt, SkillLens — bounded representation capacity |
| 2026-05-26 (new) | 3 papers ingested | StepOPSD, AKBE, PRISM — instance-level behavioral decomposition |
| 2026-05-27 | 3 papers ingested | MATCHA, FinHarness, Interaction SSD — evaluation infrastructure |
| 2026-05-27 (additional) | 6 papers processed | Real Images, Chartographer, Demographic Info + top 3 |
| 2026-05-28 | 3 papers ingested | CCO, Gamma-World, BES — constraint satisfaction under distribution shift |
| 2026-05-29 | 3 papers ingested | Gram, SoundnessBench, Entropy-Cut MH — evaluation infrastructure |
| **2026-05-30** | **3 papers ingested** | **Self-Trained Verification, SpecBench, Physics-Is-All-You-Need — trustworthy scientific AI: verification, evaluation, and supervision as infrastructure** |

## Current State

- **arXiv**: 2026-05-30 batch fully processed — 3 papers ingested
- **Wiki paper inventory**: ~351 pages (added self-trained-verification, specbench, physics-is-all-you-need)
- **arXiv API**: Very aggressive rate limiting (multiple 429 errors); worked around via targeted ID queries

## Papers Ingested (2026-05-30 batch)

| Paper | arXiv ID | Key Finding | Wiki Connection |
|-------|----------|-------------|------------------|
| Self-Trained Verification | 2605.30290 | Reference-conditioned teacher + on-policy distillation trains verifiers without human feedback; 14× on scientific reasoning, breaks RLVR ceiling | Connects to [[test-time-scaling]], [[reasoning-scaffolding]], [[self-improvement]], [[llm-verification]] |
| SpecBench | 2605.30314 | Evaluates SWE agents on specification-level reasoning (RFC proposal deficiency identification); best agent GPT-5.4 at 44.4% | Connects to [[SWE-bench]], [[agentic-ai]], [[evaluation]], [[ai-evaluation-infrastructure]] |
| Physics-Is-All-You-Need | 2605.30353 | 33/57 sessions in wrong architecture that passed oracle tests; supervision protocol — not model capability — determines trustworthiness | Connects to [[ai-coding-agents]], [[supervision]], [[scientific-software]], [[oracle-tests]] |

## Cross-Paper Theme: Trustworthy Scientific AI — Infrastructure Layers

| Paper | Infrastructure Type | Core Problem |
|-------|---------------------|--------------|
| Self-Trained Verification | Verification as training infrastructure | How do we train verifiers without human feedback? |
| SpecBench | Evaluation infrastructure | How do we measure specification-level reasoning? |
| Physics-Is-All-You-Need | Supervision as quality infrastructure | How do we catch what oracle tests miss? |

**Design principle**: Trustworthy scientific AI requires infrastructure across all three layers — and infrastructure design (not model scale) is often the primary determinant of quality.

## Kanban Status

### Prior Cycle Open Items (from 2026-05-29 carryover)

1. **Gram overeagerness finding — connection to CCO's calibrated conservatism**
   - Self-answer: Both Gram and CCO address agents that exceed their constraints — Gram via auditing (detecting misbehavior), CCO via constraint repair (correcting misbehavior). The finding that overeagerness (not deliberate sabotage) is the primary driver aligns with CCO's calibrated conservatism approach. **Resolved**: No new kanban task — note as established cross-paper connection in synthesis.

2. **SoundnessBench optimism bias — cross-reference with autonomous research agent literature**
   - Self-answer: The bias is pervasive across all 12 frontier LLMs tested and not explained by contamination — a fundamental limitation of LLMs as autonomous research agents. Cross-reference with Locally Coherent's finding that per-component calibration doesn't guarantee system-level coherence — both point to systemic limitations of probabilistic reasoning in LLM agents. **Resolved**: No new task — connected to today's multi-agent coherence theme.

### This Cycle

- [x] Prior cycle items resolved via cross-paper connection
- [x] STV vs RiM comparison → t_ddf839070e904f9b (assigned researcher — wiki synthesis)
- [x] Physics vs LLMSurgeon investigator agent pattern comparison → t_cbcdc7bee3cd46ca (assigned researcher — wiki synthesis)
- [x] Predictive adequacy vs explanatory correctness → t_471274800c084c94 (assigned researcher — concept page creation)

## Notes for Next Run

- **arXiv rate limiting**: Very aggressive this cycle — multiple 429 errors. Used targeted ID queries only (no category search queries). Consider further backoff windows or API key if available.
- **Prior carryover items resolved**: Gram/CCO connection and SoundnessBench bias are both addressed
- **New theme emerging**: Trustworthy scientific AI infrastructure — three layers (verification, evaluation, supervision). Worth a synthesis page if not already covered.
- **PDF storage**: `/home/ty/Documents/paper-research/arxiv-today/` for today’s batch; previous batch in main `paper-research/` dir

## Last Run
2026-05-30 09:55 UTC (this run — arXiv API rate-limited, batch already fully processed this morning)

## Notes for Next Run
- arXiv API still aggressively rate-limiting — multiple429s on both HTTP and HTTPS. No new batch available.
- Today's batch (2026-05-30 morning) fully processed: 3 papers ingested, wiki pages created, report delivered.
- Open items from prior cycle already surfaced to kanban (t_ddf839070e904f9b, t_cbcdc7bee3cd46ca, t_471274800c084c94) — assigned to researcher.
- No new open items this cycle — nothing new to surface.