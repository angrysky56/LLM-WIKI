
---
created: 2026-06-02T00:00:00Z
updated: 2026-06-02T00:00:00Z
type: source
summary: "Maturity-staged agent monitoring — 3x3 scope×dimension grid (within-run, cross-run, structural) × (quality, suitability, efficiency) using variance (CV) as the characterization signal. Triage routes 97% to automated tracking; 2% to humans. Stage 1 finding: structural diagnosis must precede error detection."
tags: [arxiv-2026, agent-monitoring, agentic-systems, FMEA, evaluation-methodology, structural-failure, reliability]
sources: https://arxiv.org/abs/2606.02494
status: active
confidence: 0.9
---

# Monitoring Agentic Systems Before They're Reliable

**arXiv:** 2606.02494  
**Authors:** Marisa Ferrara Boston, Glen Hanson, Effi Georgala, JD Hudgens (Reins AI), Heather Frase (Veraitech)  
**Date:** 2026-06-01

## The Problem

Agentic systems entering production are *partially integrated assemblies* — not yet stable systems. The authors observe that at this maturity level, **structural defects (not task-level errors) dominate the failure landscape**. Task-level error detection is infeasible because structural failure modes mask the signal that task-level monitors are designed to detect.

This is a direct theoretical response to the wave of papers building task-level agent monitors ([[finharness]], [[interaction-ssd-2026]], [[matcha-2026]]) — Boston et al. argue those monitors are the wrong tool for early-stage systems.

## Method: 3×3 Decomposition + Variance Signal

The monitoring methodology decomposes agentic evaluation into a 3×3 grid:

| Scope \ Dimension | Quality | Suitability | Efficiency |
|---|---|---|---|
| **Within-run** | deterministic stage defects (CV=0.02) | — | — |
| **Cross-run** | stochastic integration consequences (CV=1.25, 24% at L2) | — | — |
| **Structural** | integration gaps (CV=0.00, perfect consistency) | — | — |

**Variance (CV) is the characterization signal.** Low variance = deterministic (within-run and structural). High variance = stochastic (cross-run). The CV itself tells you *which kind of failure* is present, before you even know what the error is.

Findings are routed through a **severity classification adapted from FMEA** (Failure Mode and Effects Analysis — the manufacturing-safety discipline), concentrating human attention on the small subset that warrants investigation.

## Three Results from Synthetic Testbed

The methodology was evaluated on a **synthetic testbed of 220 runs across 120 document bundles with controlled error injection**, processed by an early-stage system with known integration defects.

1. **Monitor scope determines failure type.** Within-run monitors surface deterministic stage defects (CV=0.02). Cross-run monitors surface stochastic integration consequences (CV=1.25, 24% at severity L2). A structural monitor identifies an integration gap with **perfect consistency (CV=0.00)**.

2. **Injected task-level errors are indistinguishable from clean baselines.** This confirms the central thesis: structural defects *mask* task-level signal. You cannot task-monitor your way out of an integration defect.

3. **Deterministic triage routes 97% of findings to automated tracking** — only 2% reach human investigators. The 2% reflects *variable* system behavior (the stochastic integration consequences).

## Maturity-Staging Model

The authors propose a **maturity-staging model** in which monitoring transitions across three stages as integration defects are resolved:

1. **Stage 1 — Structural characterization** (this paper's focus). Variance + scope grid. The system is too broken for error detection; we can only characterize *how* it fails.
2. **Stage 2 — Error detection.** Once structural defects are resolved, task-level monitors become viable. This is the regime where [[finharness]], [[matcha-2026]], and [[interaction-ssd-2026]] operate.
3. **Stage 3 — Reliability tracking.** Once errors are detectable, the system enters steady-state SLI/SLO tracking. This is unaddressed by current literature.

The headline claim: **"Deploy monitoring early: the first thing it finds is the most important thing to fix."**

## Connections to Wiki

- **Last cycle's oversight theme** ([[stateful-monitoring-distributed-agent-attacks-2026]], [[boiling-frog-agentic-safety-2026]], [[gram-sabotage-alignment-auditing-2026]], [[calibrating-conservatism-scalable-oversight-2026]], [[finharness]], [[alignment-tampering-2026]]) all build *task-level* safety/oversight monitors. This paper argues that for early-stage systems those monitors operate in the wrong stage.
- **Evaluation-infrastructure thread** ([[matcha-2026]], [[finharness]], [[interaction-ssd-2026]], [[soundnessbench-ai-scientist-2026]]): Boston et al. argue the field has skipped Stage 1 and gone directly to Stage 2 monitors. The maturity-staging model is a counter-argument.
- **Scientific-AI thread** ([[autosci-memory-centric-research-lifecycle-2026]], [[physics-is-all-you-need-2026]], [[why-llms-arent-scientists-yet]], [[deepweb-bench-2026]], [[soundnessbench-ai-scientist-2026]]): AutoSci, DeepWeb-Bench, and SoundnessBench all evaluate task-level performance. This paper would predict those benchmarks cannot distinguish a system that fails for structural reasons from one that fails because the task is hard.

## Limitations / Caveats

- Evaluated on a **synthetic testbed** with *controlled* error injection — not field deployment.
- Domain is document-driven multi-stage agentic workflows in regulated industries (authors are at Reins AI). The 3×3 grid *transfers architecturally*; specific calibrations are domain-specific.
- FMEA is a manufacturing-era framework from the 1960s. Adapting it to LLM agents is a *claim*, not a proven transfer.
- The paper is silent on Stage 2 and Stage 3 — only Stage 1 evidence is presented.

## Cross-Cycle Theme

This is the **fourth paper in 6 days** on the agent oversight/monitoring thread. The pattern across the four:
- [[stateful-monitoring-distributed-agent-attacks-2026]] — attack-surface monitoring (what the agent can do)
- [[boiling-frog-agentic-safety-2026]] — drift monitoring (how the agent changes over time)
- [[gram-sabotage-alignment-auditing-2026]] — training-time monitoring (audit before deploy)
- **This paper** — maturity-staged monitoring (when monitoring is *appropriate* for the system's life-cycle stage)

The four together describe a **monitoring lifecycle** that is currently unarticulated in the literature. Boston et al.'s maturity-staging model is the first explicit framework for which *kind* of monitor to deploy *when*.
