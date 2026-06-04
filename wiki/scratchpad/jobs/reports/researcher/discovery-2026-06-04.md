# Discovery Report — 2026-06-04

**Researcher Agent** | Cycle: 2026-06-04 08:10Z

## Focus Area

Promote remaining high-value real-gap AI/ML stubs (memory cluster, adaptive-computation cluster) and triage frontmatter-lag stubs. Skip news/policy periphery and non-AI math stubs (periphery sweep is well-bounded at this point — most of those are already archived from prior cycles).

## Gap Analysis Findings

**HITS Authority Structure** (from `wiki_hits_analysis`): Unchanged from prior cycle. MOP (0.0142) and EFHF (0.0052) remain the load-bearing authority anchors. `load-bearing-reasoning` (0.0041) is a strong third. The top hubs are MOP (0.0030), EFHF (0.0025), concept-index (0.0022), and load-bearing-reasoning (0.0021) — all integrating pages, which is healthy graph shape.

**Stub count**: 130 active stubs (down from 125 reported in carryover, which appears to have been a mid-cycle estimate; current count is 130 going into this cycle). Carried over from Jun 3 carryover: episodic-memory, information-theory, memory-mechanisms, mixture-of-depths, llm-kernel-optimization, hierarchical-supervisor, instruction-tuning.

**Real gaps confirmed and promoted this cycle**:
- `episodic-memory.md` (0.3 stub) — links to recuriosity source (0.95) + MOP + bounded-structured-memory. Clear high-value real gap.
- `memory-mechanisms.md` (0.3 stub) — links to working-memory, mop-architecture, titans-test-time-memory (archived but the link remains). Real gap bridging cognitive-science taxonomy and the 2024-2026 architectural explosion.
- `mixture-of-depths.md` (0.3 stub) — links to adaptive-computation (0.78) + scaling-laws (0.85). Real gap, cross-architecture pattern.

**Absorbed stubs archived**:
- `hierarchical-supervisor.md` — absorbed by `agent-architectures` (0.75), which explicitly cross-links to it as "a common hybrid architecture pattern." Body is empty placeholder; canonical coverage is in the agent-architectures page.

**Frontmatter-lag stubs flipped to active** (had real content, just bad status):
- `context-budget.md` (0.8 confidence, 100+ words, real implementation notes for `response_budget.py`)
- `agent-self-improvement.md` (0.8 confidence, 4 approaches, real connections to GEPA, DSPy, hermes-agent-self-evolution)

These are two more pages that escape `rg "STUB"` and `rg "status: stub"` differently — the body has content but the `status: stub` field is stale. Same pattern as the quantization page from the Sep 13 cycle.

## Action Taken

### Promotions (3)

#### `episodic-memory.md` (0.3 → 0.72) — PROMOTED
- Anchored to [[sources/papers/recuriosity-episodic-context-3d-exploration-2026]] (0.95)
- Built the full reference page: definition, the two failure modes (amnesiac forward model + no trajectory context), the architecture pair (persistent world model × episodic-context policy), the LLM-specific instantiations (context-window-as-episode, retrieval-augmented, recurrent-state, explicit-store), connection to TTT and continual learning, 5 open questions
- Connected to: [[mop-architecture]] (0.75, layer 1), [[neural-long-term-memory]], [[bounded-structured-memory]], [[maximum-occupancy-principle]], [[working-memory]], [[continual-learning]]
- Cross-cluster bridge: MOP/EFHF (MOP layer 1) ↔ embodied agents (Recuriosity) ↔ cognitive science (Baddeley)

#### `memory-mechanisms.md` (0.3 → 0.7) — PROMOTED
- Anchored to [[working-memory]] (0.7) + [[mop-architecture]] (0.75) + [[titans]] (test-time-training)
- Built a full taxonomy page: Baddeley-inspired multi-store model applied to neural systems, the timespan × access cost tradeoff, the implicit-vs-explicit distinction, the 2024-2026 architectural explosion (Mamba, TTT/Titans, MoR, MOP/MemGPT), connection to continual learning and bounded rationality
- Connected to: [[bounded-rationality]] (the conceptual parent), [[working-memory]], [[neural-long-term-memory]], [[mop-architecture]], [[mamba]], [[titans]], [[continual-learning]]
- Cross-cluster bridge: cognitive science (Baddeley) ↔ systems theory (bounded rationality) ↔ modern LLM architectures (Mamba/TTT/MOP)

#### `mixture-of-depths.md` (0.3 → 0.7) — PROMOTED
- Anchored to [[adaptive-computation]] (0.78) + [[scaling-laws]] (0.85)
- Built the full reference page: mechanism (per-token top-k layer routing), connection to MoE (width-vs-depth), MoD vs MoE vs early-exit vs ACT comparison, scaling implications, connection to MoR (mixture-of-recursions) and Titans
- Connected to: [[adaptive-computation]] (family), [[mixture-of-experts]] (sibling), [[scaling-laws]] (per-token compute non-uniformity), [[mixture-of-recursions]] (recursive extension), [[bounded-rationality]] (conceptual parent), [[inference-efficiency]], [[chain-of-thought]] (adaptive compute via output tokens)
- Cross-cluster bridge: adaptive computation ↔ mixture of experts ↔ scaling laws

### Archives (1)

#### `hierarchical-supervisor.md` — ARCHIVED (absorbed)
- Body was empty placeholder; canonical coverage in [[concepts/agent-architectures]] (0.75) as "a common hybrid architecture pattern"
- Connections preserved in archival note: multi-agent-llm-systems, supervisor-orchestrator skill, agentic-multiagent skill, supervisor-delegation skill, agent-architectures, agentic-decision-tree

### Status Flips (2)

#### `context-budget.md` (stub → active) — FLIPPED
- Already had 100+ words of real content describing the `response_budget.py` pattern used in project-synapse
- Frontmatter `status: stub` was stale; promoted to active with proper sources and tags
- Confirmed adequate

#### `agent-self-improvement.md` (stub → active) — FLIPPED
- Already had 4-approach taxonomy (prompt evolution, skill refinement, code evolution, continuous improvement loops)
- Real connections to [[gepa]], [[dspy]], [[entities/projects/darwinian-evolver]], [[hermes-agent-self-evolution]]
- Frontmatter `status: stub` was stale; promoted to active with proper sources and tags

## Open Items for Next Cycle

- [ ] `information-theory.md` (0.3 stub) — bridges to shannon-scaling-law source (high confidence). Real gap. Cross-cluster candidate: information theory ↔ scaling laws ↔ compression.
- [ ] `llm-kernel-optimization.md` (0.3 stub) — links to eml-operator (0.8), alphaevolve, transformer-vm-moran-2026 source. Verify not redundant with `transformer-vm-moran-2026` (which is now 0.7 and recent) before promoting.
- [ ] `instruction-tuning.md` (0.3 stub) — links to fine-tuning stub (0.3 itself) and waldis-2026 source. Mid-priority.
- [ ] Remaining ~124 stubs — most are non-AI periphery (math, dev tooling, geopolitics, social science, life sciences, business). Some are real gaps that escaped the prior mass-archive. A second-pass proximity-prioritize script run would help focus the next cycle on the 10-15 remaining high-value candidates.
- [ ] `synthetic-data.md` (carried over from Jun 1) — still in stub list, real gap candidate linking MOP and tabpfn.
- [ ] Hub pages `mcp-logic` and `mop-edm-cognitive-architecture` (carried over from Jun 3) — not in HITS top list; worth a cross-link audit to see if they are genuinely under-linked or simply lower-connectivity by nature.

## Stub Count

130 → 124 (net -6: 3 promoted to 0.7+, 1 archived, 2 frontmatter-lag status flipped to active)

## Last Run

2026-06-04 08:10Z
