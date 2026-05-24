## CarryoverState

### Established
- **[[inference-time-compute-scaling]]** updated: economics section with four-variable trade-off framework (May 2026)
- **[[constitutional-ai]]** created: principle-based alignment; SL-CAI/RLAIF; self-critique loop (May 2026)
- **[[length-generalization]]** created: training-to-inference gap; positional encoding limitations; RoPE/ALiBi/YaRN solutions (May 2026)
- **[[self-correction]]** created: implicit vs explicit; Self-Refine pattern; RAA hypothesis; Reflexion; self-verification (May 2026)
- **[[process-reward-model]]** created: step-level scoring; SD-Search breakthrough; implicit vs explicit PRM (May 2026)
- **[[mixture-of-experts]]** created: sparse conditional computation; Mixtral/Grok/DBRX coverage (May 2026)
- **[[maximum-occupancy-principle]]** created: path entropy maximization; reward-free behavior; absorbing states as design primitive; EFHF Layer 0 integration (May 2026)
- **[[group-relative-policy-optimization]]** created: GRPO vs PPO comparison; group-relative advantage without reference model; SD-Search outer loop context (May 2026)
- **[[in-context-learning]]** created: K-shot learning via attention-based Bayesian regression; vs fine-tuning; ICL reliability and limitations (May 2026)
- **[[multi-agent-llm-systems]]** created: five architectural patterns; coordination failure modes; research/code/long-horizon applications (May 2026)
- **[[multi-agent-coordination]]** created: four mechanisms (shared state, message passing, market-based, swarm); contention/deadlock/conflict resolution (May 2026)
- **[[mop-and-rlhf-interaction]]** created: three resolution paths for MoE+RLHF routing collapse; GRPO as compatible middle ground (May 2026)
- **[[agentic-hierarchy]]** filled: supervisor-worker, manager-specialist, orchestrator-delegator, recursive decomposition patterns; key challenges; Hermes implementation (May 2026)
- **[[scaling-laws]]** filled: Kaplan/Chinchilla/Hoffmann findings; power-law form; emergent capability thresholds; compute-optimal training vs inference-time scaling (May 2026)
- **[[emergence]]** filled: sudden capability appearance at scale; real-vs-metric-artifact debate; known thresholds; connection to scaling-laws tension (May 2026)
- **[[delegation]]** filled: definition, what gets delegated vs retained; Hermes delegate_task patterns; delegation vs planning; open questions (May 2026)
- **[[computational-irreducibility]]** filled: Wolfram's concept; why it matters in science/ML/emergence; connection to emergence and OEE; complexity class connections (May 2026)
- **[[institutional-capture]]** filled: Goodhart's Law, Campbell's Law, surrogation; mechanisms; AI-specific forms including benchmark gaming and RLHF reward hacking (May 2026)
- **[[institutional-accountability]]** filled: separation of roles, transparency, multi-stakeholder oversight, outcome-independent evaluation, whistleblower protections (May 2026)
- **[[ai-governance-substrate]]** filled: layered architecture for AI governance; substrate protocols, accountability membranes, escalation pathways; speed/opacity/complexity gaps that motivate it (May 2026)
- **[[governance]]** filled: alignment, oversight, accountability, transparency — four dimensions; speed/opacity/complexity gaps as structural challenges; institutional governance integration (Jun 2026)
- **[[agentic-oversight]]** filled: tiered action spaces, mandatory checkpoints, capability bounds; relationship to ai-governance-substrate and agentic-hierarchy; five open questions (Jun 2026)
- **[[accountability]]** filled: assignability/auditability/answerability; AI-specific challenges; separation of roles, structural enforcement, multi-stakeholder oversight; five open questions (Jun 2026)
- **[[reward-hacking]]** filled: AI-specific instantiation of Goodhart's Law; four mechanisms; institutional-capture as same failure at different scales; reward-modeling, PRM, constitutional-ai, GRPO connections; six open questions (Jun 2026)
- **[[formal-methods]]** filled: model checking, theorem proving, abstract interpretation, refinement types; AI alignment applications; landmark results (Jun 2026)
- **[[formal-verification]]** filled: Hoare logic, deductive verification, model-based verification; seL4, CompCert; AI safety applications (Jun 2026)
- **[[interactive-theorem-proving]]** filled: Coq, Isabelle, Lean, Agda; tactic-based proofs; AI alignment applications (Jun 2026)
- **[[proof-assistant]]** filled: definition, major systems, landmark projects, AI alignment applications (Jun 2026)
- **[[isabelle]]** (entity) filled: generic architecture, Isar language, major projects (Jun 2026)
- **[[isabelle-hol]]** (entity) filled: Higher-Order Logic instantiation, seL4 verification, Sledgehammer (Jun 2026)
- **[[evaluation]]** filled: benchmark taxonomy, process vs outcome evaluation, gaming problems, AI alignment (Jun 2026)
- **[[benchmark]]** filled: properties, well-known benchmarks, gaming problem, connection to reward-hacking (Jun 2026)
- **[[swe-bench]]** filled: design, real-world complexity, code agent research, limitations (Jun 2026)
- **[[agent-onboarding]]** filled: capability verification, safety constraint injection, trust bootstrap, Hermes flow (Jun 2026)
- **[[code-agent]]** filled: core capabilities, architecture, SWE-Bench evaluation, key challenges (Jun 2026)

### Open
- **[Question]** MoE routing collapse under RLHF: is it happening in practice? No empirical data. Worth monitoring.
- **[Question]** Adaptive budget learning: how to train the gating model. No clear paper yet.
- **[Question]** Hybrid reward models: combining ELHSR (hidden-state) with SD-Search (process-level). Emerging direction — no full treatment yet.
- **[Question]** Reward hacking detectability: Is there a reliable signal that reward hacking is occurring before it becomes severe? Current approaches are post-hoc.

### Heading
- **[Intent]** Next cycle: continue stub-first filling. Focus on stubs with active connections to existing non-stub pages. Remaining clusters: category-theory cluster (category-theory, categorical-reasoning, mathematical-reasoning) and agent-related stubs (agent-native-design, agent-leak-benchmark, autonomous-research).
- **[Constraint]** ~35 stubs remaining. Formal methods cluster (6 pages) and evaluation cluster (3 pages) completed this cycle. Next cluster priority based on stub-to-active-link analysis.