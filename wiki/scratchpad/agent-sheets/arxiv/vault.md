# arxiv Agent — Vault (Episodic Trace)
**Date**: 2026-05-30 | **Run**: Daily arXiv batch

## Discovery

arXiv API extremely rate-limited (429 errors). Switched to targeted ID queries after initial batch failures. Discovered 3 significant papers from 2026-05-28 batch:

1. **2605.30290v1** — Self-Trained Verification (STV) — verification training recipe
2. **2605.30353v1** — Physics-Is-All-You-Need — supervisor protocol case study
3. **2605.30314v1** — SpecBench — specification-level SWE agent evaluation

All 3 PDFs downloaded successfully (200 each). All 3 text extracted via pdftotext.

## Selection Rationale

Theme: **Trustworthy Scientific AI — Verification, Evaluation, and Supervision as Infrastructure**

Each paper addresses a different dimension of building trust in AI systems:
- STV: Verification as training infrastructure (self-improvement)
- SpecBench: Evaluation as infrastructure for agentic software engineering
- Physics: Human supervision protocol as the key determinant of trustworthiness

The papers share a common thread: as AI systems become more capable in science and software, the bottleneck shifts from capability to trust, and trust requires infrastructure across multiple dimensions.

## Paper Summaries

### Self-Trained Verification (2605.30290v1)
**Key insight**: Diagnosis is easier given a reference. A model that cannot find errors in its own output from scratch CAN when shown the reference solution. This asymmetry becomes the supervision signal.

- STV trains verifiers via on-policy distillation from reference-conditioned teacher
- Results: 14× on scientific reasoning (1.5% → 21.0%), 2× on hard math, breaks RLVR convergence ceiling
- Core contribution: trains verifiers without human-graded feedback
- Follows from RiM (last cycle) — both address reasoning at test time, different mechanisms

### SpecBench (2605.30314v1)
**Key insight**: SWE-bench assumes perfect specifications; real-world software requires agents to design specifications. SpecBench evaluates the upstream phase — identifying specification deficiencies in RFC proposals.

- Tasks from real RFC processes (Kubernetes, React, Rust, TVM, vLLM)
- Best agent (GPT-5.4): 44.4% accuracy — significant headroom
- Community value alignment critical — Rust's memory safety strictness vs React's API stability

### Physics-Is-All-You-Need (2605.30353v1)
**Key insight**: 33 of 57 sessions spent in wrong code architecture that passed oracle tests. Supervision protocol — not model capability — determined trustworthiness.

- 3 bugs evaded oracle detection: agent treated symptom reduction as root-cause resolution
- Critical distinction: not whether code produces right numbers, but whether it produces them for the right reasons
- Architectural redesign required human physics judgment — not accessible to scaling alone

## Open Items

- [ ] RiM vs STV comparison: both address reasoning at test time (memory blocks vs verifier-refinement)
- [ ] Physics vs LLMSurgeon investigator agent pattern comparison (static environment ablation)
- [ ] "Predictive adequacy vs explanatory correctness" — does wiki have page on this?
- [ ] SpecBench vs SWE-bench scope comparison — does specification-level evaluation reveal different capability gaps?
- [ ] STV ViL training recipe — does it generalize beyond math/scientific reasoning to agentic contexts?
- [ ] arXiv rate limiting: consider building in larger backoff windows between targeted ID queries

## Cross-Paper Theme Notes

Three papers, three infrastructure layers:
| Paper | Infrastructure Type | Core Problem |
|-------|---------------------|--------------|
| STV | Verification as training infra | How do we train verifiers without human feedback? |
| SpecBench | Evaluation infrastructure | How do we measure specification-level reasoning? |
| Physics | Supervision as quality infra | How do we catch what tests miss? |

**Design principle emerging**: Trustworthy scientific AI requires infrastructure across all three layers — and the infrastructure design (not model scale) is often the primary determinant of quality.

## Last Run
2026-05-30 09:50 UTC