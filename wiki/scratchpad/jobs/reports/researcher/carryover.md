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

### Open
- **[Question]** Verifier-graph theory: concept vs synthesis classification? Entity exists at `wiki/entities/projects/tys-repos/verifier-graph.md`. Needs Ty input. Open since May 21.
- **[Question]** MoE routing collapse under RLHF: is it happening in practice? No empirical data. Worth monitoring.
- **[Question]** Adaptive budget learning: how to train the gating model. No clear paper yet.
- **[Question]** Hybrid reward models: combining ELHSR (hidden-state) with SD-Search (process-level). Emerging direction — no full treatment yet.

### Heading
- **[Intent]** Next cycle: fill remaining governance cluster stubs (`governance`, `agentic-oversight`, `accountability`) as a batch, then address other high-priority stubs from the 46-stub list. The computational-irreducibility → emergence → open-ended-evolution cluster is now well-connected.
- **[Constraint]** Still 42 stubs remaining. Prioritize stubs with active (non-stub) connections. Governance cluster is nearly complete; next priority cluster TBD.