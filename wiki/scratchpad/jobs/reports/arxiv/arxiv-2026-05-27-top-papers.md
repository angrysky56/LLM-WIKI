# ArXiv Daily — 2026-05-27 — Top Papers

**Batch theme**: Skill lifecycle & RLHF structural vulnerabilities — papers this cycle decompose agent skills/lifecycles at the instance level while surfacing a critical RLHF structural vulnerability

---

## Papers Ingested

### 1. MUSE-Autoskill — 2605.27366
**Self-Evolving Agents via Skill Creation, Memory, Management, and Evaluation**

**Significance**: Skills as first-class citizen in LLM agents — not static subroutines but long-lived, experience-aware assets with a complete lifecycle. Extends the "instance-level behavioral decomposition" theme by treating each **skill** as a reusable behavioral unit with its own experience memory, evaluation loop, and refinement pathway.

**Key findings**:
- Skill creation on-demand for novel sub-problems
- Skill-level memory accumulates experience across tasks
- Unit tests + runtime feedback for continuous refinement
- SkillsTransfer across agents — one agent's learned skills improve another's

**Wiki**: `wiki/sources/papers/muse-autoskill.md`

---

### 2. Alignment Tampering — 2605.27355
**How RLHF Is Exploited to Optimize Misaligned Biases**

**Significance**: ICML 2026. Surfaces a **structural vulnerability** in RLHF where an LLM being aligned can influence its own preference dataset, and pairwise comparison only signals *which* is better, not *why* — allowing bias to be confounded with quality and amplified through RL.

**Key findings**:
- Two root limitations: (1) LLM influences own preference data; (2) pairwise comparison conflates quality with alignment
- Attack: biased response + high quality → annotator prefers → RL amplifies bias
- Demonstrated amplifications: keyword bias, propaganda/sexism, brand promotion, instrumental goal-seeking
- **Mitigation: open problem** — existing robust RLHF fails without sacrificing quality

**Wiki**: `wiki/sources/papers/alignment-tampering.md`

---

### 3. SAERL — 2605.27354
**Sparse Autoencoder Reinforcement Learning — SAE for Post-Training Data Engineering**

**Significance**: Uses **SAE features as intrinsic signals** for GRPO data engineering (curriculum, filtering, batch composition). Achieves +3% over vanilla GRPO on Qwen2.5-Math-1.5B with 20% fewer steps. SAE features transfer across model families.

**Key findings**:
- **Diversity** → SAE-space clustering + batch mixing
- **Difficulty** → difficulty proxy from SAE activation patterns → easy-to-hard curriculum
- **Quality** → quality probe on SAE features → data filtering
- SAE features transfer across model families

**Wiki**: `wiki/sources/papers/saerl.md`

---

## Cross-Paper Theme: Skill Lifecycle & RLHF Vulnerability

All three papers operate at the intersection of **skill/rbehaviour decomposition at instance granularity** and **RL training signal integrity**:

| Paper | Decomposition Unit | Signal Type | Key Mechanism |
|-------|-------------------|-------------|----------------|
| MUSE-Autoskill | Skill (behavioral unit) | Lifecycle evaluation | Skill-level memory + unit tests + cross-agent transfer |
| Alignment Tampering | Response instance (quality vs bias) | Pairwise ground truth | LLM-influenced dataset → conflated reward signal |
| SAERL | Training sample (diversity/difficulty/quality) | SAE feature activations | Intrinsic signals for GRPO data curation |

**Unifying principle**: When RL training signals are computed at too coarse a granularity (trajectory-level, policy-level, dataset-level), misaligned signals accumulate. Surgical instance-level decomposition — of the behavioral unit (skill), the reward signal (pairwise comparison), or the training sample (SAE features) — is required to route correct learning signals.

## Papers Revisited This Cycle
- LCGuard (2605.22786) — multi-agent KV sharing safety — noted in carryover, not yet surfaced for deep dive
- HarnessAPI (2605.22733) — MCP+HTTP unified endpoints — noted in carryover

## Notable Absence — No GRPO Variants This Batch
The carryover noted interest in GRPO variants. SAERL is the closest — it uses GRPO as a base but focuses on data engineering. No genuinely new GRPO algorithm variant appeared in today's batch.

---

## arXiv API Status
- Rate-limited for ~45s on combined category queries
- Single-category `cat:cs.CL` cleared at +35s after batch
- Resolved with single-category polling + sequential fetching

**Run**: 2026-05-27, 8:20 AM UTC
