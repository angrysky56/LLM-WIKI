# Researcher Discovery Report — 2026-06-08

## Discovery Cycle
- Topics researched: 14
- New pages created: 12 (converted from stubs)
- Pages updated: 2 (formal-methods, benchmark)
- Cross-links added: ~40+

## New Entries (Stub → Active Conversions)

### Formal Methods Cluster (6 pages)
- **[[formal-methods]]**: Core techniques — model checking (state explosion, CEGAR), theorem proving (interactive vs automated), abstract interpretation (sound over-approximation), refinement types. AI alignment connection: verifying reasoning chains, reward hacking detection, agent safety invariants. Landmark results: seL4, CompCert.
- **[[formal-verification]]**: Proving program correctness against specifications — Hoare logic/deductive verification (Why3, Frama-C, SPARK) vs model checking (CBMC, SPIN). AI alignment: LLM-generated code verification, agent safety invariants, reward hacking as safety property violation.
- **[[interactive-theorem-proving]]**: The practice — Coq (CIC, CompCert, four-color), Isabelle (generic, seL4), Lean (modern, Mathlib), Agda (MLTT, PL research). AI alignment: verifying reasoning chains, constitutional AI verification, multi-agent protocol verification.
- **[[proof-assistant]]**: Tool-level overview — type theory foundation, trusted kernel, major systems. Landmark projects table (seL4, CompCert, four-color). AI alignment applications: reasoning chain verification, circuit-level verification, agent safety protocols.
- **[[isabelle]]** (entity, tools/): Generic architecture — Pure kernel, object logics, Isar proof language. The generic-over-specific design. seL4 verification as landmark result. Unique among proof assistants in supporting multiple logics.
- **[[isabelle-hol]]** (entity, tools/): Higher-Order Logic instantiation. Sledgehammer (ATP/SMT automation), code export (CakeML). Architecture of the seL4 verification — abstract spec → executable spec → C → binary, each refinement step verified.

### Evaluation Cluster (4 pages)
- **[[evaluation]]**: LLM evaluation taxonomy (MMLU, GSM8K, HumanEval, SWE-Bench), process vs outcome evaluation, benchmark gaming as institutional capture. Open questions on contamination detection and generalization.
- **[[benchmark]]**: Properties table (ground truth, metric, baseline, coverage, anti-gaming). Well-known benchmarks with descriptions. Benchmark gaming problem — connection to institutional-capture and reward-hacking.
- **[[swe-bench]]**: Design from real GitHub issues, test-based evaluation, results table (DeepSeek-Coder-V2 at ~13%, frontier models ~5%). Variants (Lite, Verified). Connection to code-agent research and reward-hacking (gaming test cases).
- **[[agent-onboarding]]**: Gate protocol for introducing new agents. Four components: capability verification, safety constraint injection, trust bootstrap, resource allocation. Hermes flow (spawn → soul injection → capability test → constraint acceptance → active). Open questions on scalability and cross-system transfer.

### Code Agent (1 page)
- **[[code-agent]]**: Core capabilities (code generation, debugging, refactoring, testing, review), architecture (LLM backbone, tools, state, iteration loop), reactive vs proactive tool use patterns. SWE-Bench as standard evaluation. Key challenges: context management, test reliability, multi-file coordination, long-horizon tasks.

### Also Updated (from thin stub to active)
- **[[benchmark]]** (updated): Expanded from stub with full benchmark taxonomy, properties, gaming problem connection to reward-hacking and institutional-capture.

## Gap Analysis

Formal methods cluster (6 pages) is now **complete**: formal-methods, formal-verification, interactive-theorem-proving, proof-assistant, isabelle, isabelle-hol. All stubs converted to active pages with genuine content.

Evaluation cluster (3 pages) is now **complete**: evaluation, benchmark, swe-bench. Also added agent-onboarding and code-agent which relate to agent development and testing.

**Remaining stubs (~35)**: Category theory cluster (category-theory, categorical-reasoning, mathematical-reasoning), agent stubs (agent-native-design, agent-leak-benchmark, autonomous-research), and various domain-specific stubs (motion-understanding, taylors-law, essa, qes, etc.).

## Open Questions
- **MoE routing collapse under RLHF**: is it happening in practice? No empirical data. Worth monitoring.
- **Adaptive budget learning**: how to train the gating model. No clear paper yet.
- **Hybrid reward models**: combining ELHSR (hidden-state) with SD-Search (process-level). Emerging direction — no full treatment yet.
- **Reward hacking detectability**: Is there a reliable signal that reward hacking is occurring before it becomes severe? Current approaches are post-hoc.