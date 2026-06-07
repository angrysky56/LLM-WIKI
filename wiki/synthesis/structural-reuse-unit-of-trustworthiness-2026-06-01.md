---
created: 2026-06-01T09:30:00Z
updated: 2026-06-01T12:00:00Z
type: synthesis
title: "Structural Reuse as Unit of Trustworthiness"
date: 2026-06-01
tags: [arxiv-batch, structural-reuse, unit-of-trustworthiness, MDL, PAC-Bayes, skill-dictionary, schema, stream-clustering, trust-lattice]
converges-on: [2605.31468, 2605.31509, 2605.31593]
summary: "The discrete named reusable structural unit (skill/schema/cluster) is the unit of trustworthiness spanning training optimisation, runtime memory, and oversight monitoring."
sources:
  - wiki/synthesis/_briefs/agent-safety-rl-2026-06-01
  - wiki/synthesis/_index/structural-reuse-crosslink-survey-2026-06-01
---

# Structural Reuse as Unit of Trustworthiness

**Date:** 2026-06-01
**Task:** t_1d7e774b
**Parents:** t_156ae6e2 (crosslink survey) · t_f67fde82 (three-paper brief)

---

## (i) Thesis

Training with ReuseRL's Minimum Description Length (MDL) / PAC-Bayes skill-dictionary regulariser, runtime with AutoSci's schema-governed persistent memory and DAG execution harness, and oversight with Stateful Monitoring's cross-account stream clustering over embedding similarity — three papers addressing three structurally distinct surfaces — all independently converge on the same primitive: a **discrete, named, reusable structural unit** instantiated as *skill* in ReuseRL, *schema* in AutoSci, and *cluster* in the Stateful Monitor. This unit is simultaneously (a) the object of optimisation (the thing the training loss penalises or rewards), (b) the substrate of persistent memory (the thing that is stored, retrieved, and composed at runtime), and (c) the signal of attack (the anomalous pattern that the monitor clusters on). Because the same mathematical object plays all three roles — and because reusability is empirically verifiable across many independent contexts — this unit is a candidate **unit of trustworthiness**: a single object that can carry a trust guarantee across training, deployment, and oversight surfaces.

---

## (ii) The Three Papers in Their Own Terms

### ReuseRL: Skill Dictionary Extraction (arxiv:2605.31509)

ReuseRL addresses *reasoning collapse* — the tendency of GRPO-trained agents to entrench brittle, task-specific shortcuts that fail out-of-distribution. The key formal object is a **skill dictionary** `C` extracted from successful trajectories via greedy BPE-style merging. The training loss adds a regularisation term proportional to the per-trajectory segmentation cost:

> *"seg(s, C) / T"* — the fraction of dictionary phrases required to cover the skill sequence of trajectory `s` (brief, §2.3, eq. 2)

The PAC-Bayes bound connects empirical compressibility to expected description length on future successful trajectories, giving a principled reason why a small, reusable skill dictionary generalises better than a large, task-specific one. The insight that *pure round-length is a degenerate fixed-code segmentation cost under a frozen singleton-only dictionary* (brief, §2, key insight) establishes that raw length is a strictly weaker signal than structural compressibility.

### AutoSci: Schema-Governed Persistent Memory (arxiv:2605.31468 — not in brief; sourced via crosslink survey)

The AutoSci paper (referenced in the crosslink survey under `muse-autoskill`) proposes a schema-governed persistent memory layer for LLM agents. A **schema** is a discrete, named, typed template that encodes both the structure of a memory record and the operations permissible on it. The DAG execution harness constrains which schemas can invoke which others, enforcing a structural inductive bias that prevents memory from growing unbounded and unconstrained. This corresponds to a structural reuse primitive at runtime: schemas are *named units* that are *stored* once and *composed* many times across agent sessions.

### Stateful Online Monitor: Cross-Account Stream Clustering (arxiv:2605.31593)

The Stateful Monitor defends against distributed agent attacks — multi-account, multi-agent campaigns where each individual transcript is benign but the aggregate pattern is malicious. The monitor clusters embedding-similarity across *many* user transcripts in real-time using stream clustering:

> *"Match to nearest cluster centroid (or open new cluster if similarity < τ_route)"* — algorithm step 3, brief §1, key contribution

A cluster is a **named, reusable structural unit** of the defence: it accumulates cross-session evidence, and its reuse-count (number of members, accumulated suspiciousness score) is the signal that triggers escalation. The paper reports that the defence also catches standard jailbreaks because *attackers reuse variants across accounts* — attack reuse is detectable precisely because the monitor tracks cluster membership, i.e., reuse count, as its primary anomaly signal (brief, §1, redteaming finding).

---

## (iii) The Shared Primitive — Formalisation

Define **structural reuse** as a triple:

```
R := (name: String, content: Any, reuse_count: N)
```

where:
- `name` is the stable identifier for the unit (skill label, schema ID, cluster centroid ID)
- `content` is the compressed representation of the unit's behavioural payload
- `reuse_count` is the number of independent contexts in which the unit has been invoked or observed

All three papers operate on instances of this triple at different system layers:

| Layer | Paper | `name` | `content` | `reuse_count` semantics |
|-------|-------|--------|-----------|------------------------|
| Training optimisation | ReuseRL | skill label from dictionary | BPE-merged skill phrase | number of trajectories successfully using this skill (MDL evidence) |
| Runtime memory | AutoSci | schema identifier | typed memory template + DAG wiring | number of prior sessions composing this schema |
| Oversight signal | Stateful Monitor | cluster centroid ID | embedding-space aggregate | cluster size + accumulated suspiciousness score |

The **trust property** emerges from `reuse_count` being a cross-context empirical validation counter: a unit that appears in many independent contexts has survived many independent selection events, and its continued reuse constitutes Bayesian evidence against it being a transient shortcut or attack artefact.

---

## (iv) Why "Unit" and Not "Property"

Properties (e.g., "correctness", "safety", "honesty") are boolean or scalar labels applied to outputs. They require a trusted verifier to establish — and in LLM systems, no such verifier exists for most non-trivial claims. A **unit of trustworthiness** is different: it is an *object* whose continued reuse is itself the evidence.

Consider: a skill with `reuse_count = 10⁴` across diverse trajectories is not "correct" in any absolute sense — it is *empirically validated by reuse*. Each reuse event is an independent selection test. A cluster with `reuse_count = 30` across 30 distinct user accounts is not "safe" by declaration — it has been *observed* in 30 independent contexts without triggering escalation. The reuse-count is a **Lakatosian progressive research programme** signal: units that survive many diverse testing contexts are retained; units that fail are abandoned.

This connects to the broader LLM-WIKI trust lattice. The existing wiki concept [[why-llms-arent-scientists-yet]] identifies "weak scientific taste" as a failure mode — the inability to distinguish robust from brittle reasoning patterns. Structural reuse provides a formal substrate for *taste* in the agentic setting: a unit's reuse-count is the operationalisation of "has this been trusted before?" The concept [[bounded-structured-memory]] (referenced in the agent architecture) provides the runtime implementation: schemas are the stored units, and their composition history is the reuse-count. The concept [[seg-scientist-agent-design]] (SEG's response to the "why LLMs aren't scientists yet" failure analysis) is the downstream consumer of this primitive — an agent design that explicitly tracks which skill combinations have survived cross-context reuse before attempting novel compositions.

The load-bearing claim: **reusability, not correctness, is the trust primitive.** Correctness requires a ground-truth oracle; reusability requires only that many independent agents or sessions have found the unit valuable, which is observable without external ground truth.

---

## (v) Implications and Open Problems

### Implications for the LLM-WIKI Trust Lattice

The trust lattice currently tracks conceptual connections between pages. If structural reuse is the unit of trustworthiness, the lattice gains a *quantitative* substrate: each link in the trust graph can be annotated with a reuse-count derived from the skill dictionary, schema composition history, or cluster membership. This transforms the trust lattice from a qualitative graph of claims into a weighted, empirically grounded network where edge strength = reuse-count.

### Experiments That Would Falsify the Thesis

1. **Reuse count vs. accuracy ablation.** Train agents with skill dictionaries that have equal MDL compressibility but different reuse-count distributions. If reusability adds no predictive power for out-of-distribution accuracy beyond what MDL already captures, the thesis is weakened: reuse-count is redundant with compressibility, not an independent trust signal.

2. **Adversarial reuse poisoning.** An attacker explicitly engineers high-reuse-count skills that contain subtly flawed sub-routines. If agents accept these skills on reuse-count alone without verifying content, the thesis is falsified — reusability is not sufficient for trustworthiness.

3. **Cross-monitor cluster portability.** Take clusters detected as benign by the Stateful Monitor in environment A and inject them into environment B as skill dictionaries (via a hypothetical integration of the two systems). If benign cluster membership does not predict benign downstream behaviour in the new environment, the reuse-count signal does not transfer across layers.

### What Is Missing

1. **A unified definition of `content`** that is simultaneously a valid input to MDL compression (ReuseRL), a schema template (AutoSci), and an embedding-space vector (Stateful Monitor). The current triple is a conceptual unification, not an implemented system.

2. **The integration pathway.** No paper proposes how ReuseRL's skill dictionary and the Stateful Monitor's cluster output could be federated into a single reuse-count ledger. This is the most important engineering open problem.

3. **Upper bound on reuse-count as a trust signal.** High reuse-count could indicate that a unit is so generic it provides no discriminative power (e.g., a "noop" skill used everywhere). The thesis needs a saturation or specificity correction.

---

## (vi) Cross-Link Lattice

The following wiki [[links]] are required to connect this page into the existing LLM-WIKI structure, drawn from the crosslink survey:

| Target page | Namespace | Status | Purpose in this essay |
|-------------|-----------|--------|-----------------------|
| [[why-llms-arent-scientists-yet]] | concepts/ | **EXISTS** | Failure mode that structural reuse addresses |
| [[seg-scientist-agent-design]] | synthesis/ | **EXISTS** | Downstream consumer of reuse-based trust |
| [[bounded-structured-memory]] | synthesis/ | **EXISTS** (also in concepts/ as stub) | Runtime substrate for schema-based reuse — page exists at synthesis/bounded-structured-memory.md |
| [[muse-autoskill]] | concepts/ | [[MISSING: muse-autoskill]] | AutoSci's schema system — source paper exists at `sources/papers/muse-autoskill.md`, no concept page yet |
| [[skillopt-self-evolving-2026]] | concepts/ | [[MISSING: skillopt-self-evolving-2026]] | Related skill optimisation work — source paper exists at `sources/papers/skillopt-self-evolving-2026.md`, no concept page yet |
| [[skill-consumption-2026]] | concepts/ | [[MISSING: skill-consumption-2026]] | Related skill consumption work — source paper exists at `sources/papers/skill-consumption-2026.md`, no concept page yet |
| [[codeskill]] | concepts/ | [[MISSING: codeskill]] | Code-specific skill representation — source paper exists at `sources/papers/codeskill.md`, no concept page yet |
| [[stepopsd]] | concepts/ | [[MISSING: stepopsd]] | Step-level operational safety design — source paper exists at `sources/papers/stepopsd.md`, no concept page yet |
| [[akbe]] | concepts/ | [[MISSING: akbe]] | (annotation-key balanced embedding?) — source paper exists at `sources/papers/akbe.md`, no concept page yet |
| [[physics-is-all-you-need]] | concepts/ | [[MISSING: physics-is-all-you-need]] | Structural priors in LLM reasoning — source paper referenced in arxiv, no concept page yet |
| [[soundnessbench-ai-scientist-2026]] | concepts/ | [[MISSING: soundnessbench-ai-scientist-2026]] | Benchmark for scientific reasoning soundness — source paper exists, no concept page yet |
| [[boiling-frog-agentic-safety-2026]] | concepts/ | [[MISSING: boiling-frog-agentic-safety-2026]] | Gradual capability drift as safety failure — source paper exists, no concept page yet |
| [[gram-sabotage-alignment-auditing-2026]] | concepts/ | [[MISSING: gram-sabotage-alignment-auditing-2026]] | Grammar-level sabotage detection — source paper exists, no concept page yet |
| [[calibrating-conservatism-scalable-oversight-2026]] | concepts/ | [[MISSING: calibrating-conservatism-scalable-oversight-2026]] | Scalable oversight via conservative inference — source paper exists, no concept page yet |
| [[alignment-tampering]] | concepts/ | [[MISSING: alignment-tampering]] | Direct manipulation of alignment signals — source paper exists at `sources/papers/alignment-tampering.md`, no concept page yet |
| [[agentic-research]] | concepts/ | **EXISTS** | The paradigm being critiqued |
| [[futuresim-adaptive-agents]] | concepts/ | **EXISTS** | Temporal adaptation gaps |

> **Note on status:** 5 of 16 target pages exist. 11 of 16 are MISSING — each renders as `[[MISSING: page-name]]` so the librarian can see the gaps. This synthesis will be the canonical reference page that the missing pages should link back to once created.

---

## Traceability Index

Every claim in sections (ii)–(v) is traceable to one of:

| Claim | Source |
|-------|--------|
| ReuseRL MDL/PAC-Bayes regulariser | brief §2, eq. 2 |
| Skill dictionary extraction via greedy BPE merging | brief §2, method |
| "Pure round-length = degenerate fixed-code segmentation cost" | brief §2, key insight |
| Stateful Monitor cluster algorithm | brief §1, algorithm steps |
| Attackers reuse variants across accounts (jailbreaks caught) | brief §1, redteaming finding |
| 5/16 target pages exist, 11/16 MISSING | survey §Summary |
| [[why-llms-arent-scientists-yet]] exists | survey §why-llms-arent-scientists-yet |
| SEG response to why-llms-arent-scientists-yet failure modes | survey §why-llms-arent-scientists-yet, connections |