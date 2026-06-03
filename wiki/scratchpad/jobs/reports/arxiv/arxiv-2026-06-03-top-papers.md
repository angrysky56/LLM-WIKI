# arxiv Report — 2026-06-03

## Papers Processed

### 1. **Language Models Need Sleep: Learning to Self-Modify and Consolidate Memories** (arxiv:2606.03979)
- **Why selected:** First concrete wake/sleep paradigm for LLMs; replaces static train/test lifecycle with frequency-spectrum of memory modules; outperforms all RL baselines on math reasoning.
- **Status:** ingested → `wiki/sources/papers/sleep-self-modify-consolidate-2026.md`
- **Wiki connections:** [[continual-learning]], [[catastrophic-forgetting]], [[bounded-representation-capacity]], [[mixture-of-experts]], [[reinforcement-learning]], [[reuserl-skill-reuse-compression]], [[stepopsd-2026]], [[akbe-2026]], [[skillopt-self-evolving-2026]], [[saerl]]

### 2. **Skill-RM: Unifying Heterogeneous Evaluation Criteria via Agent Skill** (arxiv:2606.03980)
- **Why selected:** Reformulates reward modeling as execution of a reusable Reward-Evaluation Skill — extends the wiki's skill theme (8th paper) into the evaluation domain. Strong empirical gains at matched backbone.
- **Status:** ingested → `wiki/sources/papers/skill-rm-2026.md`
- **Wiki connections:** [[bounded-representation-capacity]], [[agent-skills]], [[reward-models]], [[rubric-evaluators]], [[verifier-graphs]], [[reuserl-skill-reuse-compression]], [[skillopt-self-evolving-2026]], [[skillharm-lifecycle-skill-attacks-2026]], [[muse-autoskill]]

### 3. **Quantifying Faithful Confidence Expression in Large Reasoning Models** (arxiv:2606.03969)
- **Why selected:** First systematic framework for measuring whether LRMs linguistically express their intrinsic confidence. LRMs are systematically unfaithful — reasoning training doesn't fix it, prompt interventions don't transfer. New cMFG* metric and prefix-conditioned sampling estimator are method upgrades.
- **Status:** ingested → `wiki/sources/papers/faithful-confidence-lrm-2026.md`
- **Wiki connections:** [[calibration]], [[faithfulness]], [[uncertainty-quantification]], [[agent-trust]], [[bounded-representation-capacity]], [[meta-cognitive-agents]], [[finharness-2026]], [[matcha-2026]], [[hll-humanitys-last-line-verification-2026]], [[stateful-monitoring-distributed-agent-attacks-2026]]

## Wiki Updates
- New pages: 3 (`sleep-self-modify-consolidate-2026.md`, `skill-rm-2026.md`, `faithful-confidence-lrm-2026.md`)
- Tags added: paper, arxiv, arxiv-2026, plus per-paper themes
- Cross-links: 12+ wiki concepts and 15+ related papers linked

## Cross-Paper Theme: Bounded Self-Model
**New theme emerging across this cycle:** all three papers address the same deep problem — the model has a *bounded capacity to represent its own state*, and the gap between internal state and externalised representation is the locus of failure.

| Paper | Self-Representation | Failure Mode |
|---|---|---|
| Sleep | Memory modules at different frequencies | In-context knowledge never consolidated into parameters |
| Skill-RM | Procedural evaluation skill | Reward criteria implicit in prompt; no resource orchestration |
| Faithful Confidence | Confidence-decisiveness alignment | What the model *thinks* vs what the model *says* diverges |

This is the **fourth new theme in 7 days** for the agentic-systems / meta-cognition thread:
1. (2026-05-27) Evaluation infrastructure
2. (2026-06-01) Structural reuse as unit of trustworthiness
3. (2026-06-02) Capability-vs-deployment gap
4. (2026-06-03) **Bounded self-model** — current candidate

The bounded-self-model theme also subsumes yesterday's capability-vs-deployment gap: the deployment gap is *exactly* a bounded self-model problem (the model doesn't know what it doesn't know, and can't express what it does know).

## Operational Notes
- All 3 papers share theme: bounded self-model (memory consolidation, evaluation skills, confidence expression)
- arXiv rate limit events: 4 (429s + one 503) before first 200; 60-180s backoff worked
- Inbox: empty
- Used curl for PDF download (MCP 429 fallback); all 3 PDFs downloaded successfully
- The 2026-06-02 arXiv batch was the only new listing on 2026-06-03 morning UTC; today's 20:00 UTC batch is not yet posted

## Related
- [[wiki/index]]
- [[scratchpad/agent-sheets/arxiv/templates/report]]
- [[wiki/scratchpad/agent-sheets/arxiv/workspace/papers-2026-06-03-researched]]
