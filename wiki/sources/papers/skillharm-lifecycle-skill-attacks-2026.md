---
summary: SkillHarm — first lifecycle-aware benchmark of skill-based attacks. 879 samples, 12 risk types, ASR up to 86.3%. Persistent mutation attacks work; "attack failures" are confounded with non-engagement.
tags: [arxiv-2026, agent-safety, skill-attacks, benchmark, lifecycle-attacks, persistent-attacks, code-execution, supply-chain]
updated: 2026-06-02T14:20:23Z
created: 2026-06-02T14:20:23Z
---

---
created: 2026-06-02T00:00:00Z
updated: 2026-06-02T00:00:00Z
type: source
summary: "SkillHarm — first lifecycle-aware benchmark of skill-based attacks on agents. Two scenarios (Fixed-Payload Poisoning, Self-Mutating Poisoning), 12 risk types across data pipelines / system environments / agent autonomy, 879 attack samples across 71 skills. ASR up to 86.3% FPP / 69.3% SMP. Many 'attack failures' are agent not engaging with file, not resistance."
tags: [arxiv-2026, agent-safety, skill-attacks, benchmark, lifecycle-attacks, persistent-attacks, auto-skill, code-execution]
sources: https://arxiv.org/abs/2606.02540
status: active
confidence: 0.92
---

# SkillHarm: Lifecycle-Aware Skill-Based Attacks via Automated Construction

**arXiv:** 2606.02540  
**Authors:** Yuting Ning, Zhehao Zhang, Yash Kumar Lal, Boyu Gou, Junyi Li, Weitong Ruan, Chentao Ye, Rahul Gupta, Diyi Yang, Yu Su, Huan Sun (Ohio State, Amazon AGI, Stanford)  
**Date:** 2026-06-01

## The Problem

Agent skills are a *privileged* attack surface — agents implicitly follow and execute them. Existing studies of skill-based attacks:
- Evaluate poisoned skills **within a single task execution** (no persistent effect)
- Enumerate harms through **ad-hoc risk lists** (no systematic taxonomy)

SkillHarm closes both gaps.

## Two Attack Scenarios

**Scenario I — Fixed-Payload Poisoning (FPP):** A fixed poisoned skill package directly compromises any task session that invokes it. Static supply-chain attack.

**Scenario II — Self-Mutating Poisoning (SMP):** An initially benign execution silently mutates persistent skill content, **deferring harm until a subsequent reuse**. This is the dangerous one: the first invocation looks clean, the skill mutates its own `SKILL.md` or scripts, and a later task pays the cost. Attack that spreads through *use*.

## 12 Risk Types Across 3 Workflow Components

- **Data pipelines** — poisoning retrieval, RAG, tool inputs
- **System environments** — file system, network, env variables
- **Agent autonomy** — instruction override, tool escalation, behavior hijack

## AutoSkillHarm — Automated Construction Pipeline

A coding-agent-driven pipeline with natural-language harnesses that instantiates attacks at scale. The result: **879 attack samples across 71 skills**.

## Results

- **Attack success rate (ASR) up to 86.3% in FPP** (static poisoning works)
- **ASR up to 69.3% in SMP** (persistent mutation also works)
- **Latent risk finding:** Many "attack failures" stem from the agent *failing to engage with the poisoned file* — not from genuine resistance. The skill just isn't read.
- **Current defenses fail to reliably mitigate the threat.**

## The Latent Risk

The "agent not engaging" finding is the most important methodological observation. If a benchmark reports "attack failed", that could mean:
- (a) the attack didn't work
- (b) the attack never reached the agent

(b) is a **false negative that looks like a success**. The field has been reporting inflated defense numbers because of this confound.

## Connections to Wiki

- **Skill theme** ([[skillopt-self-evolving-2026]], [[skill-consumption-2026]], [[codeskill]], [[muse-autoskill]], [[stepopsd]], [[akbe]], [[reuserl-skill-reuse-compression-2026]]): All treat skills as a *positive* asset — SkillOpt extracts them, MUSE generates them, ReuseRL compresses them. SkillHarm inverts: skills are an *attack surface*. The skill theme is now explicitly two-sided.
- **Last cycle's oversight theme** ([[stateful-monitoring-distributed-agent-attacks-2026]], [[boiling-frog-agentic-safety-2026]], [[gram-sabotage-alignment-auditing-2026]], [[alignment-tampering-2026]]): SkillHarm provides concrete attack vectors that none of these monitors are designed to catch. The attack succeeds *before* the safety monitor sees the agent's output — at the *skill-loading* boundary.
- **Code-execution risks** ([[why-llms-arent-scientists-yet]]): Skills that execute code are the highest-leverage surface in the benchmark. The "AI scientist" literature assumes trustworthy code execution; SkillHarm shows it isn't.
- **AutoSci's SciDAG and SciEvolve** ([[autosci-memory-centric-research-lifecycle-2026]]): AutoSci's self-evolution component would be a prime target for SMP — an attacker poisons a skill that AutoSci then iteratively mutates and re-uses, spreading the payload through the lifecycle.

## Limitations / Caveats

- ASR ceiling depends on the agent *reading* the skill. "Failures" are confounded with non-engagement.
- Defenses evaluated are current best-effort — not a fair test of what *could* exist.
- 71 skills is a limited sample; real agent ecosystems have hundreds of third-party skills.
- The benchmark is *static* — it doesn't simulate evolving defenses.

## Why This Matters for the Skill Theme

The skill theme across the wiki has been accumulating *positive* evidence (skills help agents generalize, compress, transfer). SkillHarm is the first paper to systematically demonstrate the **negative externality**: third-party skills are an unauthenticated supply chain. The next iteration of the skill theme must address this — skill provenance, signing, sandboxing, or capability-constrained execution.
