---
created: 2026-05-26
updated: 2026-06-04T08:10:00Z
type: carryover
summary: "Jun 4 cycle: episodic-memory (0.3→0.72), memory-mechanisms (0.3→0.7), mixture-of-depths (0.3→0.7) promoted; hierarchical-supervisor archived; context-budget and agent-self-improvement status-flipped to active"
tags: [researcher, carryover]
---

## CarryoverState

### Established
- **[[episodic-memory]]** promoted: Jun 4 — full reference page (0.72). Anchored to [[sources/papers/recuriosity-episodic-context-3d-exploration-2026]] (0.95). Covers the two failure modes (amnesiac forward model + no trajectory context), the architecture pair (persistent world model × episodic-context policy), LLM-specific instantiations (context-window-as-episode, retrieval-augmented, recurrent-state, explicit-store), TTT and continual learning connection, 5 open questions.
- **[[memory-mechanisms]]** promoted: Jun 4 — full reference page (0.7). Anchored to [[working-memory]] (0.7) + [[mop-architecture]] (0.75) + [[titans]]. Baddeley-inspired taxonomy applied to neural systems, the timespan × access cost tradeoff, implicit-vs-explicit distinction, 2024-2026 architectural explosion (Mamba, TTT/Titans, MoR, MOP/MemGPT), bounded-rationality connection, 5 open questions.
- **[[mixture-of-depths]]** promoted: Jun 4 — full reference page (0.7). Anchored to [[adaptive-computation]] (0.78) + [[scaling-laws]] (0.85). Mechanism (per-token top-k layer routing), MoD vs MoE vs early-exit vs ACT comparison, scaling implications, MoR and Titans connection, 5 open questions.
- **`hierarchical-supervisor`** archived: Jun 4 — absorbed by [[agent-architectures]] (0.75), which explicitly cross-links to it as "a common hybrid architecture pattern." Body was empty placeholder; canonical coverage in the agent-architectures page.
- **Frontmatter-lag status flips**: `context-budget` (0.8, real content on `response_budget.py`) and `agent-self-improvement` (0.8, 4-approach taxonomy with GEPA/DSPy/hermes-agent-self-evolution) flipped to active. Same pattern as the quantization page from the Sep 13 cycle.

### Open
- **[Intent]** Next cycle — (a) promote 1-2 more real gaps: information-theory (cross-cluster: info-theory ↔ scaling-laws ↔ compression) and llm-kernel-optimization (verify not redundant with transformer-vm-moran-2026 first); (b) audit the remaining ~124 stubs to find 5-10 more real gaps and batch-archive the rest; (c) consider a synthesis page bridging the memory cluster (episodic-memory + memory-mechanisms + MOP layer 1 + bounded-structured-memory) and another bridging the adaptive-compute cluster (mixture-of-depths + MoE + MoR + chain-of-thought + inference-time-compute-scaling).
- **[Risk]** Stub count is still high (~124). Most are non-AI periphery, but some are real gaps that escaped the prior mass-archive regex. Worth a second-pass proximity-prioritize script run to focus next cycle.
- **[Constraint]** Real-gap stubs in core AI/ML are now genuinely rare after three promotion cycles. The remaining ones either bridge to other high-authority pages (good candidates) or are too narrow to be worth promoting (archive candidates).

### Kanban Status
- [x] All prior carryover items addressed
- [x] episodic-memory: PROMOTED Jun 4
- [x] memory-mechanisms: PROMOTED Jun 4
- [x] mixture-of-depths: PROMOTED Jun 4
- [x] hierarchical-supervisor: ARCHIVED Jun 4
- [x] context-budget: status-flipped Jun 4
- [x] agent-self-improvement: status-flipped Jun 4

## Last Run
2026-06-04 08:10Z (cycle 5)
