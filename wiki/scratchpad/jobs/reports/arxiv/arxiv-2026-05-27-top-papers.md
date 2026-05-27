# arXiv Report — 2026-05-27

## Batch Theme: Evaluation, Safety, and Moderation

Today's batch of 6 processed papers (top 3 selected + 3 notable) converges on **evaluation infrastructure for LLMs and VLMs** — both metrics (MATCHA, Chartographer) and safety harnesses (FinHarness), plus annotation methodology (Interaction SSD, Demographic Information).

---

## Top 3 Papers

### 1. MATCHA: Matching Text via Contrastive Semantic Alignment
**arXiv:** [2605.27345](https://arxiv.org/abs/2605.27345) | **cs.CL**

Dual-view evaluation metric that rewards proximity to gold text AND penalizes distance from adversarially generated counterfactual contradictions.

**Key result**: +18.38% over ROUGE-L and +20.82% over BERTScore on TruthfulQA — where no training set exists. Outperforms 23 embedding models.

**Why it matters**: Token-overlap and embedding metrics assign nearly identical scores to directly contradicting texts, masking fundamental errors. MATCHA introduces a hard negative (counterfactual) that exposes this failure mode.

**Wiki**: [[matcha]], [[llm-evaluation]], [[bert-score]], [[semantic-similarity]]

---

### 2. FinHarness: An Inline Lifecycle Safety Harness for Finance LLM Agents
**arXiv:** [2605.27333](https://arxiv.org/abs/2605.27333) | **cs.CL**

Three-component inline safety harness: Query Monitor (cross-turn drift) + Tool Monitor (per-call evaluation) + Cascade Module (adaptive judge routing with bounded recall). Fired risk factors re-injected as ex-ante evidence for agent self-rejection.

**Key result**: On FinVault (856 traces): ASR 38.3% → 15.0%, benign approval preserved (41.1% → 39.3%), 4.7× fewer advanced-judge calls.

**Why it matters**: Boundary filters miss mid-trajectory attacks; post-hoc judges intervene after irreversible state change. FinHarness operates within the execution loop — same architectural insight as [[agentic-safety]] (Boiling the Frog) but in finance domain.

**Wiki**: [[finharness]], [[llm-agents]], [[inline-monitoring]], [[agentic-safety]]

---

### 3. Semantic Gradients Interactions in SSD: A Case Study in Racial Identity and Hate Speech
**arXiv:** [2605.27322](https://arxiv.org/abs/2605.27322) | **cs.CL**

Extends Supervised Semantic Differential (SSD) with an interaction term that models how semantic gradients vary by moderator (annotator identity). Main gradient + interaction gradient + conditional gradients — all back-projected and interpretable.

**Key result**: Significant moderation effect on Berkeley Hate Speech corpus: annotator racial identity moderates how semantic cues predict hate-speech ratings.

**Why it matters**: Standard SSD averages over heterogeneous meaning-outcome relationships, obscuring moderation effects. Interaction SSD enables statistically testable moderated relationships — directly relevant to [[annotation-bias]] and fairness research.

**Wiki**: [[semantic-differential]], [[hate-speech-detection]], [[annotation-bias]], [[moderation-analysis]]

---

## Notable Mentions (Same Batch)

**Real Images, Worse Judgments** ([2605.27315](https://arxiv.org/abs/2605.27315)) — VLMs perform *worse* with real-image context when visual evidence is least relevant (abstract words). Probing reveals representational shifts and greater sensitivity to spurious visual cues. Instructing models to focus on text reduces degradation. Connects to [[vlm-calibration]].

**Chartographer** ([2605.27311](https://arxiv.org/abs/2605.27311)) — Counterfactual chart generation: fix chart-question task, vary underlying chart and answer. Reveals VLM failures hidden by single-chart performance. Same first author (Yifan Jiang) as Real Images paper — two-paper arc on VLM evaluation methodology.

**When Does Demographic Information Help?** ([2605.27313](https://arxiv.org/abs/2605.27313)) — Demographics help only in specific data regimes: low training disagreement, high test disagreement, sufficient data, greater demographic overlap. Proposes gated demographic residual model. Pairs with Interaction SSD on demographic moderation.

---

## Cross-Paper Theme: Evaluation Infrastructure

| Paper | Contribution | Connection |
|-------|-------------|------------|
| MATCHA | Evaluation metric (contradiction detection) | [[llm-evaluation]] |
| FinHarness | Safety harness (inline monitoring) | [[agentic-safety]] |
| Interaction SSD | Annotation methodology (moderation) | [[annotation-bias]] |
| Real Images | VLM evaluation (concreteness) | [[vlm-calibration]] |
| Chartographer | VLM evaluation (counterfactuals) | [[vlm-evaluation]] |
| Demographic Info | Data regime analysis | [[annotation-bias]] |

**Unifying thread**: All papers deal with **evaluation methodology** — whether for LLMs (metrics, safety), VLMs (counterfactual charts), or annotation (moderation effects). Instance-level decomposition continues to be the key pattern.

---

## Papers Ingested

| arXiv ID | Slug | Key Finding |
|----------|------|-------------|
| 2605.27345 | matcha | Dual-view contrastive metric outperforms BERTScore by 20%+ |
| 2605.27333 | finharness | Inline safety harness cuts ASR 38.3% → 15.0% |
| 2605.27322 | semantic-gradients-interactions-ssd | Interaction SSD for moderated semantic analysis |

**Total papers this session**: 6 processed, 3 fully ingested