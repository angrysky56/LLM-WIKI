# ArXiv Top Papers — 2026-06-04

> **Selection:** 3 papers, all on the **bounded-self-model** thread (cycle 4 of 4 in 8 days).
> **Run mode:** Cron — no `delegate_task` available. Inline research with pymupdf + `wiki_write_page`.
> **Source pool:** Local pending PDFs (`2605.30343`, `2605.30335`, `2605.30348`). arXiv API was 429'd across all attempts in this session (60–240s backoff insufficient). Verified pending list in `research-carryover.md`.

---

## The Three Papers

### 1. **Reasoning in Memory (RiM)** — Aichberger & Hochreiter (JKU/NXAI)
- **arXiv:** [2605.30343](https://arxiv.org/abs/2605.30343) · 21 pages
- **One-line:** Fixed latent memory blocks in the forward pass replace autoregressive chain-of-thought. Latent reasoning at SFT-w/o-CoT latency.
- **Key result:** On GSM8K, RiM beats Coconut (33.6 vs 31.1 greedy on GPT-2; 42.1 vs 36.9 on Llama-3.2-1B) at the *same latency* as direct-answer SFT. Coconut pays +178.7 ms; RiM pays +0.5 ms.
- **Why it matters:** This is the first demonstration that LLMs can be trained to *use* the bounded working-memory capacity already latent in the residual stream — without paying for autoregressive step generation. Direct lineage from Hochreiter's 1997 LSTM constant-error-carousel.
- **Wiki:** [[arxiv-2605-30343-reasoning-in-memory-rim]]
- **Bounded-self-model facet:** *Compute-side allocation of the bounded workspace.* Sleep (2026-06-03) allocates the budget to *storage*; RiM allocates it to *computation*. Same total budget, different design.

### 2. **Locally Coherent, Globally Incoherent** — Kotawala (Princeton)
- **arXiv:** [2605.30335](https://arxiv.org/abs/2605.30335) · 25 pages · ICML 2026 workshops (CTB, AgenticUQ, FAGEN)
- **One-line:** Formal compositional residual ε★ for multi-component LLM agents. Each component locally coherent; composition violates basic probability axioms.
- **Key result:** ε★ > 0 on **33–94% of 1,876 ensemble cliques** across Claude-Haiku-4.5/GPT-5.4-mini/GPT-5.4-nano/Llama-3.3-70B. **Frontier-panel rerun: 97.8% prevalence** — upgrading components reduces *magnitude* but not *prevalence*. The +0.115 nats-per-bet regret under proportional allocation collapses to +0.006 when each component is asked to self-coherentise.
- **Why it matters:** Three intuitive LLM-side mitigations (retrieval, partition-aware prompting, aggregator-LLM) all *fail or regress*. The system-level repair is worth ~20× the per-component repair. **Scaling the components does not fix compositional incoherence.**
- **Wiki:** [[arxiv-2605-30335-locally-coherent-globally-incoherent]]
- **Bounded-self-model facet:** *Multi-agent version.* The components' self-models are individually well-formed but jointly inconsistent. Same root as [[faithful-confidence-lrm-2026]] (intra-model "what the model says vs what it knows"), extended to inter-component "what component A says vs what the system jointly knows."

### 3. **LLMSurgeon** — Luo et al. (VILA Lab, MBZUAI)
- **arXiv:** [2605.30348](https://arxiv.org/abs/2605.30348) · 16 pages
- **One-line:** Recovers the pretraining data mixture of an LLM from generated text only. Constrained inverse problem with a calibrated soft confusion matrix.
- **Key result:** Across 8 open-source models in the new LLMScan benchmark (OLMo, Amber, Pythia, GPT-Neo, StarCoder at 1B–65B params), LLMSurgeon recovers domain mixtures with 2–9% per-class error at coarse/mid-grained (K=6, K=17). Fine-grained (K=87 programming languages) fails — 17.97pp error on `python`.
- **Why it matters:** First practical post-hoc, weight-free method for auditing a closed LLM's "digital DNA". The data provenance question becomes answerable without model-developer cooperation. A governance primitive.
- **Wiki:** [[arxiv-2605-30348-llmsurgeon-data-mixture-surgery]]
- **Bounded-self-model facet:** *Training-time self.* The model cannot introspect its own pretraining data. LLMSurgeon is a *post-hoc* recovery of information the model has lost access to — a different facet of the bounded-self-model problem (capability, composition, introspection).

---

## Cross-Paper Theme: Bounded Self-Model — *consolidated*

This is the **fourth cycle in 8 days** with a unifying theme. The theme *consolidates* rather than evolves:

| Cycle | Date | Theme | Self-Model Facet |
|-------|------|-------|------------------|
| 1 | 2026-05-27 | Evaluation infrastructure | (infrastructure for auditing) |
| 2 | 2026-06-01 | Structural reuse as unit of trustworthiness | (reusable unit) |
| 3 | 2026-06-02 | Capability-vs-deployment gap | (deployment self) |
| 4 | 2026-06-03 | Bounded self-model (storage, evaluation, expression) | (capacity, procedure, expression) |
| **5** | **2026-06-04** | **Bounded self-model (computation, composition, introspection)** | **(allocation, multi-agent, training-time)** |

**Synthesis claim (this cycle):** The bounded self-model has *three orthogonal axes* of failure:
1. **Allocation** — what fraction of the bounded budget goes to computation vs communication vs storage (RiM addresses; Sleep addresses; Coconut and CoT fail to optimise).
2. **Composition** — how well do bounded self-models compose into a coherent system (Kotawala formalises ε★ as the L2 distance; this is the multi-agent version of any single-model self-report gap).
3. **Introspection** — what information can be recovered about the model's own formation post-hoc (LLMSurgeon: training data; Faithful Confidence: intrinsic confidence; Skill-RM: evaluation procedure).

The unifying observation: **the model has bounded capacity to represent its own state, and any system that depends on the model accurately representing itself will fail along the axis it doesn't allocate budget to.** The fact that frontier upgrades don't fix compositional incoherence (Kotawala) and don't fix the FC gap (Faithful Confidence) is a strong empirical claim that bounded self-model is a *structural* failure, not a *capability* failure.

---

## Cross-Cycle Synthesis Candidates (open work)

Three new synthesis pages are now well-supported by the corpus:

1. **"Auditing the Bounded Self"** — covers LLMSurgeon (data), Faithful Confidence (calibration), Kotawala (compositional coherence), HLL (verification). All four are *third-party* audits of properties the model cannot self-report.
2. **"Working Memory in LLMs"** — covers RiM (compute), Sleep/CMR (storage), Markovian Thinker (state-bounded), the 1997 LSTM constant-error-carousel (historical lineage), Coconut (latent but un-bounded).
3. **"System-Level Coherence"** — Kotawala's ε★ as the formal substrate, capability-vs-deployment gap as the diagnosis, structural-reuse / skill-theme as the architectural response.

All three are candidates for a `wiki/synthesis/` page. Not produced this cycle (focus on getting the three core papers right); flagged for the next run or for a follow-up task card.

---

## Operational Notes

- **arXiv API was 429'd throughout this session.** Tried 60s, 90s, 180s, 240s backoff; no successful query. Fell back to local pending-PDF pool, which had unprocessed 2605.30343, 2605.30335, 2605.30348.
- **Cron context lacks `delegate_task`** — all research done inline with `pymupdf` + `wiki_write_page`. Subagent verification step skipped; verified each page exists on disk via `ls` and `head` per cron-fallback reference.
- **Local pending pool still has many unprocessed papers:** 2605.30233 (Entity tracking), 2605.30322/30327/30329 (Gram/ReasWithSampling/SoundnessBench), 2605.26998 (PRISM), 2605.31593 (Stateful Monitoring — already linked in carryover from prior cycle), 2605.31468 (AutoSci), 2605.29713 (book), 2605.22791 (Gated DeltaNet-2), 2605.22785 (News Chatbots), 2605.22823 (Video LLM motion), 2509.26037v2 (CoLLM-NAS).
- **Cross-links written:** Each new paper page has a "Cross-cycle" section with incoming+outgoing links to the 3 prior-cycle bounded-self-model papers (Sleep, Skill-RM, Faithful Confidence). Each prior-cycle page has a "Cross-cycle (2026-06-04 batch)" section with outgoing links back.

---

## Wiki Pages Produced

- `wiki/sources/papers/arxiv-2605-30343-reasoning-in-memory-rim.md` (7044 chars)
- `wiki/sources/papers/arxiv-2605-30335-locally-coherent-globally-incoherent.md` (7341 chars)
- `wiki/sources/papers/arxiv-2605-30348-llmsurgeon-data-mixture-surgery.md` (8031 chars)

## Wiki Pages Updated

- `wiki/sources/papers/sleep-self-modify-consolidate-2026.md` (added cross-cycle section)
- `wiki/sources/papers/skill-rm-2026.md` (added cross-cycle section, fixed duplicate header)
- `wiki/sources/papers/faithful-confidence-lrm-2026.md` (added cross-cycle section)
- `paper-research/research-carryover.md` (updated timestamp + summary)

## Last Run
2026-06-04 14:35 UTC — 3 papers processed from local 2605.3034x batch: RiM (Aichberger/Hochreiter latent reasoning via fixed memory blocks), Locally-Coherent-Globally-Incoherent (Kotawala compositional residual ε★), LLMSurgeon (Luo et al. data-mixture recovery as inverse problem). Bounded-self-model theme consolidated.
