---
created: 2026-06-01T00:00:00Z
updated: 2026-06-01T00:00:00Z
type: source
summary: "AutoSci: memory-centric agentic system for the full scientific research lifecycle. Four modules — SciMem (schema-governed memory), SciFlow (5-stage harness), SciDAG (multi-agent augmentation), SciEvolve (self-evolution). End-to-end case studies in GPU kernels and drug discovery yield reviewable papers with ICLR scores 6.3/10 and 5.8/10."
tags: [scientific-agents, research-lifecycle, persistent-memory, harness, multi-agent, self-evolution, dag-operators, gpu-kernel-optimization, drug-discovery, iclr-review, paper-2605-31468]
sources: https://arxiv.org/abs/2605.31468
status: active
confidence: high
---

# AutoSci: A Memory-Centric Agentic System for the Full Scientific Research Lifecycle (PKU, 2026)

## Definition

**AutoSci** is a unified agentic system for end-to-end scientific research, organised around four modules:

1. **SciMem** — schema-governed persistent research memory (two regions: Long-Term Knowledge Memory for cross-project scientific knowledge, Active Research Memory for project-level artifacts with lifecycle states)
2. **SciFlow** — a 5-stage lifecycle executor (Literature → Ideation → Experiment → Writing → Rebuttal) over a harness that controls state, context, verification, feedback, and orchestration
3. **SciDAG** — DAG-shaped multi-agent operator graphs that optionally augment difficult stages (debate, variation, refinement)
4. **SciEvolve** — feedback-driven versioned updates to memory organisation, skills, and DAG templates

AutoSci is positioned as the *first* system that simultaneously supports: full-lifecycle execution, harnessed runtime, structured persistent memory across projects, and full-system self-evolution. The comparison table in §1 shows that prior systems (AI Scientist series, AI-Researcher, Agent Laboratory, CycleResearcher, EvoScientist, DeepScientist, ARIS, NORA, Deep Researcher Agent) cover at most 2–3 of these four properties.

## Key Idea

The paper reframes "automated scientific research" as a **long-lifecycle system problem**, not a sequence of isolated task automations. The argument:

- Existing systems improve **parts** of automated science (idea generation, paper writing, hypothesis testing) but don't form a unified research environment.
- A research system must behave "less like a single-session assistant and more like a **persistent research environment** that can interact with users, external resources, and experimental systems over time" (AutoSci design principle).
- **Memory is the substrate** — skills, multi-agent operators, and the lifecycle executor all read from and write to SciMem, with a **Trust Guard** checking both form (schema, lifecycle state, links) and content (evidence support, consistency) before writes become usable.

## Methodology

### SciMem: Two-Region Schema
- **Long-Term Knowledge Memory**: 5 typed entities — Topic, Paper, Foundation, Concept, Method, People — connected by 20+ typed relations, stored as `.md` pages with bidirectional cross-references.
- **Active Research Memory**: Idea, Experiment, Manuscript, Review entities with explicit lifecycle states (e.g., Idea: proposed → testing → tested → validated/failed).
- **Memory flows**: long-term aggregation, cross-region activation (Long-Term → Active) and consolidation (Active → Long-Term), and cross-cycle accumulation.
- **Trust Guard** validates every write with deterministic linting (form) and an independent reviewer agent (content); writes receive PASS/WARN/BLOCK.

### SciFlow: Five-Stage Lifecycle
- Each stage reads from SciMem and writes back specific entity types. E.g., Literature writes to long-term memory, Ideation reads long-term memory and writes Idea entities, Writing reads provenance/evidence chains to produce manuscripts, Rebuttal reads submitted manuscripts + reviews + prior rebuttal lessons.
- **Harness guarantees** (5 properties):
  - **State** — stage outputs and progress are externalised, so projects resume from a specific stage
  - **Context** — each skill gets a tailored SciMem view (not the full graph)
  - **Verification** — Trust Guard at handoffs
  - **Feedback** — failures trigger `/refine` or self-evolution
  - **Orchestration** — `/research` loop with non-blocking execution and monitoring

### SciDAG: DAG-Shaped Multi-Agent Augmentation
- A selected skill invokes an operator graph `G = (V, E)` where nodes instantiate operators (generate, variation, debate, refine, review, etc.) and edges specify information flow. **Conditional edges** call a router over current state to decide continue/retry/branch/prune/stop.
- Operator graphs are stored as **stage-aware templates** (e.g., ideation templates emphasise debate; experimentation templates emphasise reliability).
- The output of the DAG re-enters the same artifact contract that SciFlow expects, so downstream stages don't need to know whether a stage used SciDAG.

### SciEvolve: Self-Evolution
- Feedback signals (user, experiments, reviews, environment) trigger versioned updates to: SciMem *organisation* (which entities exist and how they link), SciFlow *skills* (new or modified research skills), and SciDAG *templates* (new operator graphs).
- Evolution skills update the **system itself**, not just accumulated text.

## Key Findings

- **30+ research skills** spanning the five lifecycle stages plus self-evolution.
- **2 end-to-end case studies**:
  1. **GPU kernel optimization** — AutoSci generates reviewable paper-level artifacts. Automated ICLR review score: **6.3/10**.
  2. **Biomedical drug discovery** — automated ICLR review score: **5.8/10**.
- The same system, instantiated with Claude Code (Opus 4.7), executes both domains end-to-end.
- Comparison table 1: AutoSci is the only system with full support (✓) for all four properties (System modules, Harness, Structured Sci. Mem., Persistent Sci. Mem., System Evolution). EvoScientist has 1 full + 3 partial; DeepScientist/ARIS/NORA/Deep Researcher Agent have 1 full + 2 partial + 1 absent.

## Limitations

- Case studies are *simulated* research submissions, not papers undergoing real external peer review — so the rebuttal stage is not evaluated.
- Automated ICLR review scores 6.3 and 5.8 are below the human-acceptance threshold (~7+).
- The 2026-vintage of the system is fixed at v1.0.0; long-term drift of the evolving system is not measured.

## Connections

### Wiki concepts
- [[agentic-research]] — AutoSci is the most fully-spec'd "agent as researcher" system to date
- [[code-as-agent-harness]] — SciFlow's 5 guarantees (state/context/verification/feedback/orchestration) are an explicit harness spec
- [[bounded-structured-memory]] — SciMem is a typed-entity, schema-governed instance of the persistent-memory pattern
- [[multi-agent-reasoning]] — SciDAG is a DAG-of-operators instance of multi-agent orchestration
- [[scientific-discovery]] — AutoSci's lifecycle spans the full scientific discovery process
- [[autonomous-research]] — the operational target

### Related papers (wiki)
- [[physics-is-all-you-need]] — same theme (supervision protocol design, not model capability) but for a single project; AutoSci is the *system-level* continuation
- [[why-llms-arent-scientists-yet]] — diagnoses why LLM research agents fail; AutoSci is a constructive answer at the system level
- [[deepweb-bench-2026]] — evaluation infrastructure that AutoSci could be benchmarked against
- [[soundnessbench-ai-scientist-2026]] — exposes the optimism bias in AI-generated proposals; AutoSci's Trust Guard (independent reviewer agent) is a partial response
- [[clinseekagent-multimodal-clinical-evidence-seeking]] — biomedical evidence seeking; a sub-component AutoSci could absorb into its SciFlow/Experimentation stage
- [[forecasting-scientific-progress-ai-2026]] — CUSP benchmark for scientific forecasting — AutoSci could be evaluated on it
- [[deltabox-stateful-agent-checkpoint-rollback-2026]] — millisecond-level checkpoint/rollback; complements SciFlow's State guarantee
- [[xu-envfactory-2026]] — synthetic MCP environments; AutoSci's SciFlow could use EnvFactory to simulate research environments
- [[code-as-agent-harness]] — AutoSci's SciFlow is a research-specific instance of the harness pattern
- [[futuresim-adaptive-agents]] — temporal adaptation evaluation; AutoSci's long-lifecycle execution is a substrate for this evaluation

### Cross-paper theme
AutoSci is the **system-level culmination** of the trustworthy-scientific-AI theme (cf. 2026-05-30 batch: Self-Trained Verification trains verifiers, SpecBench evaluates spec-level reasoning, Physics-Is-All-You-Need designs supervision protocols). AutoSci's contribution is a *system architecture* — SciMem + SciFlow + SciDAG + SciEvolve — that integrates verification (Trust Guard), evaluation (Review entities), supervision (lifecycle harness), and self-improvement (SciEvolve) into a single runtime.
