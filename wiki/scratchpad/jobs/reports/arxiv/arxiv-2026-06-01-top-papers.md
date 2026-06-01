---
created: 2026-06-01T14:30:00Z
updated: 2026-06-01T14:30:00Z
type: report
summary: "arxiv-agent daily report 2026-06-01: 3 papers ingested from 2026-05-29 batch — ReuseRL (MDL-grounded skill reuse), AutoSci (memory-centric research lifecycle), Stateful Monitoring (catches distributed agent attacks). Trustworthy scientific AI + agent architecture + oversight theme."
tags: [arxiv, daily-report, trustworthy-ai, agent-architecture, oversight]
sources:
  - https://arxiv.org/abs/2605.31509
  - https://arxiv.org/abs/2605.31468
  - https://arxiv.org/abs/2605.31593
status: active
confidence: high
---

# arxiv Daily — 2026-06-01 Top 3 Papers

**Run window:** 2026-05-29 batch (IDs 2605.31468–2605.31603)
**Coverage:** cs.AI, cs.LG, cs.CL — 100 most recent submissions
**New IDs vs. prior ceiling (2605.30353):** 50+ papers in 2605.31xxx range

## Selection Criteria

Papers selected on **significance** (depth of contribution, new architectural lever, direct cross-link to prior wiki themes) over raw recency. Three papers were chosen that span the trustworthy-scientific-AI + agent-architecture + oversight design space.

---

## 1. ReuseRL — Skill Reuse as Compression in Agentic RL (2605.31509)
**Authors:** Xu, Feng, Dineen, Shi, Zhao, Zhou (ASU / UPenn / USC)
**Categories:** cs.LG, cs.AI
**PDF:** `/home/ty/Documents/paper-research/processed/2605.31509v1.pdf`

### Key Finding
Grounds agentic RL in the **Minimum Description Length** principle: extract a shared skill dictionary from successful trajectories (greedy BPE-style merging) and add a segmentation-cost penalty to GRPO. Proves a **PAC-Bayes generalisation bound** for the compression penalty. Pure round-length penalty is a *degenerate fixed-code* segmentation cost (Proposition 1) — it under-explores and collapses (74% burned-failure rate on TW-Cooking).

### Headline Numbers
| Metric | GRPO | Pure Len. | SegCost (buf) | SegCost (no-buf) |
|--------|------|-----------|---------------|------------------|
| ALFWorld IID — Success length | 15.3 | 8.7 | 9.3 | 8.4 |
| TW-Cooking — Burned failures | 21.1% | 74.0% | 3.3% | 9.7% |
| Countdown — 0-RESET success | 58.0% | 82.0% | 80.3% | **99.9%** |

### Why It Matters
- Provides the **theoretical generalisation anchor** for the 2026-05-26 skill theme (SkillOpt, SkillLens, CodeSkill, MUSE-Autoskill). Earlier papers describe *what skills are* and *how to optimise them*; ReuseRL explains *why skill accumulation generalises* — structural compressibility.
- Reinterprets **SkillRL and ERL as implicit, partial MDL minimisers** — a unifying lens.
- **Wiki page:** `wiki/sources/papers/reuserl-skill-reuse-compression.md`

---

## 2. AutoSci — Memory-Centric Agentic System for the Full Scientific Research Lifecycle (2605.31468)
**Authors:** Qian*, Xu*, Xie*, Fan, Tang, Chen, Wu, Yang, Di, Li, Tung, Lai, Xia, Guo, Xu, Qin, Gan, Miao, Cui (Peking University)
**Categories:** cs.AI
**PDF:** `/home/ty/Documents/paper-research/processed/2605.31468v1.pdf`

### Key Finding
First agentic system to simultaneously support: full lifecycle, harnessed runtime, structured persistent memory across projects, and full-system self-evolution. Four modules: **SciMem** (schema-governed two-region memory: Long-Term Knowledge + Active Research with lifecycle states), **SciFlow** (5-stage harness: Literature → Ideation → Experiment → Writing → Rebuttal), **SciDAG** (DAG-shaped multi-agent operator graphs as optional augmentation), **SciEvolve** (versioned updates to memory, skills, and DAG templates from feedback). A **Trust Guard** validates every memory write (form: schema linting; content: independent reviewer agent) with PASS/WARN/BLOCK.

### Headline Numbers
- **30+ research skills** spanning 5 lifecycle stages + self-evolution
- **9 reusable multi-agent operators** (generate, variation, debate, refine, review, etc.)
- **2 end-to-end case studies:**
  - **GPU kernel optimization** — automated ICLR review score: **6.3/10**
  - **Biomedical drug discovery** — automated ICLR review score: **5.8/10**
- **Comparison table 1:** AutoSci is the only system with full support (✓) for all four properties (harness + structured memory + persistent memory + system evolution)

### Why It Matters
- System-level culmination of the **trustworthy-scientific-AI theme** (cf. 2026-05-30 batch: STV trains verifiers, SpecBench evaluates spec reasoning, Physics-Is-All-You-Need designs supervision protocols). AutoSci is the *system architecture* integrating verification (Trust Guard), evaluation (Review entities), supervision (lifecycle harness), and self-improvement (SciEvolve) into a single runtime.
- Validates **Why LLMs Aren't Scientists Yet**'s diagnosis: the gap is *system architecture* (memory + harness + multi-agent + evolution), not model capability.
- **Wiki page:** `wiki/sources/papers/autosci-memory-centric-research-lifecycle.md`

---

## 3. Stateful Online Monitoring Catches Distributed Agent Attacks (2605.31593)
**Authors:** Brown, Bhargav, Santhanam, Hong, Zhang, Shtepel, Chern, Robey, Wong, Hassani (UPenn / CMU)
**Categories:** cs.CR, cs.AI
**PDF:** `/home/ty/Documents/paper-research/processed/2605.31593v1.pdf`

### Key Finding
**Two contributions:** (1) The first **distributed agent attack** — an ARTEMIS-based multi-agent scaffold where a supervisor decomposes a hard cybersecurity task into sub-tasks distributed across many user accounts. gpt-oss-120b solves 0% directly but 36.7–40.0% via the scaffold. Standard monitors catch it only **20% as often** as prior attacks. (2) An **online stateful monitor** using stream clustering of agent-context embeddings, escalating only rarely to an LM judge that reasons across the cluster. Catches distributed attacks **30% earlier** at negligible additional latency for ~99% of traffic. A 2-month red-team with white-box access hardened the monitor and revealed it *also catches standard jailbreaks* — adaptive attackers reuse attack variants across accounts.

### Headline Numbers
| Metric | Standard Monitor | Online Stateful Monitor |
|--------|------------------|--------------------------|
| Detection of distributed attacks | 20% recall | ~80% recall (Pareto dominates) |
| Time-to-detection | baseline | **30% earlier** (up to 31%) |
| Per-request latency for 99% of traffic | baseline | ~equal to standard |
| Catches standard jailbreaks? | yes | **yes (with bonus)** |

### Why It Matters
- Extends the **oversight / agentic-safety theme** (2026-05-24: Boiling the Frog; 2026-05-28: Gram, CCO) to the **architectural level**. The standard monitor's per-context scoring is the *causal bottleneck* allowing distributed attacks to succeed — and the fix is *not* a better single-context judge but a *new monitor architecture* aggregating weak signals across many contexts in real time.
- Empirical demonstration that **attackers reusing patterns across accounts** is a structural feature exploitable by monitors — same logic as MUSE-Autoskill's *re-use* of skills across tasks.
- **Wiki page:** `wiki/sources/papers/stateful-monitoring-distributed-agent-attacks.md`

---

## Cross-Paper Theme: Agentic Systems in Three Layers

| Layer | Paper | Architectural Lever |
|-------|-------|---------------------|
| **Training** (how the agent learns) | ReuseRL | MDL-grounded skill-dictionary penalty; PAC-Bayes generalisation |
| **Runtime** (how the agent executes) | AutoSci | Schema-governed persistent memory + lifecycle harness + DAG augmentation + self-evolution |
| **Oversight** (how the agent is monitored) | Stateful Monitoring | Stream clustering across user accounts; new class of safety monitor |

**Design principle:** All three layers converge on the same idea: **structural reuse is the unit of trustworthiness** — ReuseRL uses it as a training regulariser, AutoSci uses it as a memory substrate, Stateful Monitoring uses it as a detection signal for distributed attacks.

## Inbox Status
- Inbox empty — no manual PDFs to process.

## Operational Notes
- **arXiv rate limiting** remains aggressive; had to use single-category queries with backoff. Multiple full category searches timed out or 429'd.
- All 3 PDFs downloaded successfully. All 3 wiki pages written with proper frontmatter, summary, methodology, key findings, limitations, and connections sections.
- Wiki pages cross-link to existing relevant concept/sources pages only — no broken wikilinks.
- Wiki index updated (now 1281 pages).
- PDFs moved to `processed/`; carryover and research-carryover updated.
