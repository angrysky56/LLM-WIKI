# arxiv Papers Researched — 2026-06-03

## 2606.03979 — Language Models Need Sleep: Learning to Self-Modify and Consolidate Memories
**Authors:** Ali Behrouz, Farnoosh Hashemi, Vahab Mirrokni (Google / Cornell)
**Wiki page:** `wiki/sources/papers/sleep-self-modify-consolidate-2026.md`

**Key finding:** Wake/sleep lifecycle for LLMs with two mechanisms — (1) Memory Consolidation via low-rank expert addition + upward distillation from smaller self, (2) Dreaming via RL-generated synthetic curriculum. Outperforms SFT, GRPO, OPSD on AIME-24/25, HMMT-25; near-perfect BABILong at 10M tokens; 80% success on few-shot ARC vs SEAL's 72.5%; beats continual learning baselines on novel-language translation.

**Significance:** First concrete wake/sleep paradigm for LLMs. Replaces train/test dichotomy with a frequency-spectrum of memory modules. Makes a strong case that *offline* self-modification is the right abstraction for continual learning.

**Wiki connections:** [[continual-learning]], [[catastrophic-forgetting]], [[bounded-representation-capacity]], [[mixture-of-experts]], [[lora]], [[reinforcement-learning]], [[bounded-structured-memory]], [[reuserl-skill-reuse-compression]], [[stepopsd-2026]], [[akbe-2026]], [[skillopt-self-evolving-2026]], [[saerl]], [[muse-autoskill]], [[codeskill]]

---

## 2606.03980 — Skill-RM: Unifying Heterogeneous Evaluation Criteria via Agent Skill
**Authors:** Tao Chen, Gangwei Jiang, Pengyu Cheng et al. (Alibaba Qwen Team + 4 universities)
**Wiki page:** `wiki/sources/papers/skill-rm-2026.md`

**Key finding:** Reformulates reward modeling as the execution of a reusable Reward-Evaluation Skill — procedural specification (M_RM) + structured resource bank (U_RM: criteria, evidence-producing procedures, calibration rules). At matched Qwen3.5-27B backbone, Skill-RM achieves 86.2 avg on RewardBench2/RM-Bench/JudgeBench — beats raw LLM-as-Judge by 2.3 pts and best agentic judge (RewardAgent) by 9.9 pts.

**Significance:** Confirms the agent-skill abstraction as the unifying primitive for evaluation. Extends the wiki's skill theme (now 8 papers) into the reward modeling domain. The natural security follow-up: a poisoned reward-evaluation skill is the highest-leverage attack on the entire RL training pipeline.

**Wiki connections:** [[bounded-representation-capacity]], [[agent-skills]], [[reward-models]], [[rubric-evaluators]], [[verifier-graphs]], [[agentic-evaluation]], [[reuserl-skill-reuse-compression]], [[skillopt-self-evolving-2026]], [[skillharm-lifecycle-skill-attacks-2026]], [[muse-autoskill]], [[codeskill]], [[ctx2skill]]

---

## 2606.03969 — Quantifying Faithful Confidence Expression in Large Reasoning Models
**Authors:** Areeb Gani, Asal Meskin, Gabrielle Kaili-May Liu, Arman Cohan (Yale)
**Wiki page:** `wiki/sources/papers/faithful-confidence-lrm-2026.md`

**Key finding:** First systematic framework for measuring whether LRMs *linguistically express* their intrinsic confidence. Three complementary estimators (RCC, DeepConf, prefix-conditioned sampling consistency) and a new cMFG* metric. Across 7 models × 5 datasets: LRMs are systematically unfaithful; reasoning training does NOT fix it; prompt interventions from non-reasoning LLMs do not transfer.

**Significance:** Establishes faithful calibration as a *necessary and under-examined* alignment problem for LRMs. The decisiveness-confidence gap is a deployment-readiness barrier: a model that confidently reports its low confidence (or underconfidently reports its high confidence) is unsafe in any workflow that depends on self-reported uncertainty.

**Wiki connections:** [[calibration]], [[faithfulness]], [[uncertainty-quantification]], [[agent-trust]], [[bounded-representation-capacity]], [[verifier-graphs]], [[meta-cognitive-agents]], [[parallel-reasoning]], [[oMCD]], [[finharness-2026]], [[matcha-2026]], [[soundnessbench-ai-scientist-2026]], [[hll-humanitys-last-line-verification-2026]], [[autosci-memory-centric-research-lifecycle-2026]], [[stateful-monitoring-distributed-agent-attacks-2026]], [[monitoring-agentic-systems-reliability-2026]], [[boiling-frog-agentic-safety-2026]], [[skillopt-self-evolving-2026]]

---

## Cross-Paper Theme: Bounded Self-Model
All three papers address the same deep problem: **the model has a bounded capacity to represent its own state, and the gap between internal state and externalised representation is the locus of failure.**

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
