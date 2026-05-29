# Researcher Discovery Report — 2026-07-14

## Discovery Cycle
- Topics researched: 9 (agent cluster: agents, autonomous-agents, agent-architectures, bounded-structured-memory; MOP cluster: mop-architecture, ramirez-ruiz-mop-2024; thin pages reviewed: titans-test-time-memory, prd-ralph-loop-mop-gemini, llm-agents)
- New pages created: 0
- Pages upgraded from stub: 5
- Cross-links added: 22

## Pages Upgraded from Stub

### `agents.md` → reference
**What was filled**: Comprehensive reference page for the "agents" concept as a class.

Key content:
- **Definition**: Unifying reference for LLM-based agents — systems that perceive, plan, and act with operational independence
- **What makes something an agent**: Statefulness, goal-directedness, action capability, operational independence (4 criteria)
- **Taxonomy by architecture**: deliberative, reactive, hybrid, meta-cognitive (links to agent-architectures)
- **Taxonomy by autonomy level**: 5-level spectrum from tool-using assistants to cross-session autonomy
- **Relationship to non-LLM agents**: Classical RL agents vs LLM agents — key differences in reasoning, transparency, generalization, commonsense
- **Minimal agent architecture loop**: context → LLM → action → memory update → loop

Connections: agent-architectures, autonomous-agents, agent-design, multi-agent-llm-systems, llm-agents, cognitive-world-models-for-llm-agents, agent-taxonomies, agentic-planner, bounded-structured-memory, markovian-carryover, hermes-agent

### `autonomous-agents.md` → active
**What was filled**: Full concept page for autonomous agents as a distinct class of LLM systems.

Key content:
- **Definition**: LLM systems that independently perceive, plan, and act — operational independence is the defining property
- **5 characteristics**: goal-directed behavior (specified/inferred/self-generated), planning capability, tool use, memory/continuity, self-monitoring/self-correction
- **Autonomy spectrum** (5 levels): tool use → sequential tool use → goal-directed with replanning → session-level autonomy → cross-session autonomy
- **Autonomy vs reliability tension**: more autonomy = more capability + higher cascading failure risk
- **Self-correction mechanisms**: replanning, approach abandonment, human escalation

Connections: agent-architectures, agent-design, llm-agents, agentic-planner, bounded-structured-memory, agentic-oversight, reinforcement-learning

### `agent-architectures.md` → active
**What was filled**: Full concept page for the four major agent architecture families.

Key content:
- **4 architecture families**: deliberative (explicit planning, world-model), reactive (direct stimulus-response), hybrid (decomposition + execution), meta-cognitive (self-monitoring)
- **Comparison table**: planning depth, execution speed, novel situation handling, transparency, self-correction, implementation complexity
- **Deliberative properties**: transparent, handles multi-step, can reason counterfactually; slow, brittle if world model diverges
- **Reactive properties**: fast, good for routine tasks; opaque, struggles with novelty
- **Hybrid as dominant pattern**: most practical systems combine deliberative + reactive layers
- **Connection to agent design**: modularity, observability, graceful degradation as design principles

Connections: agent-design, autonomous-agents, agentic-planner, hierarchical-supervisor, cognitive-architecture, multi-agent-llm-systems

### `mop-architecture.md` → active
**What was filled**: Full concept page for Memory-Oriented Programming as an agent design pattern.

Key content:
- **Definition**: Architectural pattern treating memory as first-class — layered, purpose-differentiated schemas with bounded capacity and explicit update policies
- **3-4 layers**: episodic (session trace, volatile), semantic (compressed knowledge, persistent), procedural (skills, stable), identity/self-model (optional)
- **Key design decisions**: layer boundary definition, update policy (on session end / on threshold / on query / hybrid), retention budget allocation
- **Boundedness as non-negotiable principle**: unbounded memory always degrades; eviction must be principled
- **Connection to MCM**: MOP implements the Metacognitive Control Model architecturally; knowledge self-model in Layer 2, meta-cognitive self-model in Layer 4

Connections: cognitive-architecture, memory-mechanisms, bounded-structured-memory, markovian-carryover, ramirez-ruiz-mop-2024, catastrophic-forgetting

### `ramirez-ruiz-mop-2024.md` → active
**What was filled**: Full concept page for the Ramirez-Ruiz MOP research as a foundational contribution.

Key content:
- **Core contributions**: schema-based memory scaffolding (structured knowledge frameworks for storage and retrieval), three-layer memory model, selective consolidation via LLM-as-compressor
- **Schema definition**: not rigid database schemas, but flexible, generative cognitive schemas that can be incomplete, overlapping, dynamically instantiated
- **Three-layer model**: working (context window) → short-term (compressed session summaries) → long-term (cross-session knowledge)
- **Memory update policies**: recency-weighted, relevance-weighted, diversity-weighted — tradeoffs between coverage and coherence
- **Connection to cognitive architecture**: knowledge self-model = long-term memory; meta-cognitive self-model = schema metadata

Connections: mop-architecture, cognitive-architecture, bounded-structured-memory, catastrophic-forgetting, prd-ralph-loop-mop-gemini

## Additionally Updated (stub → active)

### `bounded-structured-memory.md` → active
Upgraded from stub. This page was already referenced extensively (mentioned in 3 carryover cycles) but was just a stub. Filled with full content including:
- Three-layer architecture matching the MOP pattern
- Budget allocation table (episodic 4–8KB, semantic 16–32KB, procedural unlimited)
- Connection to [[markovian-carryover]] (carryover.md = Layer 2, vault.md = Layer 1, skill definitions = Layer 3)
- Four design principles
- Open questions on budget optimization and compression fidelity

## Gap Analysis

### Agent Cluster — Resolved
The carryover identified the agent cluster (agents → agent-architectures → autonomous-agents → all stubs) as a priority. All three pages are now active/reference quality, with ~22 cross-links connecting them to the rest of the wiki. The cluster is well-connected to existing active pages (cognitive-architecture, agentic-planner, bounded-structured-memory, markovian-carryover, multi-agent-llm-systems).

### MOP Cluster — Upgraded
ramirez-ruiz-mop-2024 and mop-architecture are now both active, with the PRD Ralph Loop MOP Gemini page remaining as a stub (it's highly specific experimental work — lower priority). The MOP cluster now connects to cognitive-architecture, bounded-structured-memory, catastrophic-forgetting, and memory-mechanisms.

### Emergence Cluster — Good
The Jul 2023 cycle noted that attractor-dynamics now connects strongly to emergence. The emergence page was already active (108 lines, strong content). The dynamical-systems page was already upgraded in May 2026. The thread is solid.

### Thin Pages Not Upgraded
Reviewed but not upgraded this cycle:
- `titans-test-time-memory.md` (stub, connected to titans and memory-mechanisms — requires familiarity with Titans architecture)
- `prd-ralph-loop-mop-gemini.md` (stub, experimental and highly specific)
- `llm-agents.md` (stub, but agents.md now covers the topic better — could be merged or left as alias)
- `control-llm.md` (stub, references ml-evolution-benchmarking-protocol article — needs that source)

## Cross-Links Added (22)

- agents: agent-architectures, autonomous-agents, agent-design, llm-agents, bounded-structured-memory, markovian-carryover, hermes-agent, cognitive-world-models-for-llm-agents, agent-taxonomies
- autonomous-agents: agent-architectures, agent-design, llm-agents, agentic-planner, bounded-structured-memory, agentic-oversight, reinforcement-learning
- agent-architectures: agent-design, autonomous-agents, agentic-planner, hierarchical-supervisor, cognitive-architecture, multi-agent-llm-systems
- mop-architecture: cognitive-architecture, memory-mechanisms, bounded-structured-memory, markovian-carryover, ramirez-ruiz-mop-2024, catastrophic-forgetting
- ramirez-ruiz-mop-2024: mop-architecture, cognitive-architecture, bounded-structured-memory, catastrophic-forgetting, prd-ralph-loop-mop-gemini
- bounded-structured-memory: markovian-carryover, mop-architecture, hermes-agent, cognitive-architecture

## Stub Count

- Before: 315 stubs (concepts)
- After: 309 stubs (net -6 from 5 upgrades + 1 upgraded from stub to active: bounded-structured-memory)
- Remaining entity stubs: 6 (francesca-albanese, icc, knowledge-architecture, note-taking-systems, us-sanctions + .bak files)
- MOP cluster: resolved (2 upgrades)
- Agent cluster: resolved (3 upgrades)

## Related
- [[wiki/index]]
- [[scratchpad/jobs/reports/researcher/discovery-2026-07-14]]

- [[discovery-2026-07-14]]

## Open Questions

1. **bounded-structured-memory budget optimization**: How should total memory budget be distributed across layers? Is there a principled method, or empirical tuning?

2. **MOP vs fine-tuning boundary**: When should the agent compress session experience into memory (MOP) vs incorporate it into weights (fine-tuning)? What determines the appropriate path?

3. **Schema competition in MOP**: When new information conflicts with existing schemas, how does the agent resolve the conflict without cascading inconsistency?

4. **PRD Ralph Loop MOP Gemini**: Experimental extension — appears to use Gemini for PRD iteration; needs familiarity with PRD Ralph Loop context before filling
