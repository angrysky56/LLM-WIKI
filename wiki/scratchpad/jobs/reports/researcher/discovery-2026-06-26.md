# Researcher Discovery Report — 2026-06-26

## Discovery Cycle
- Topics researched: 5 (epistemic-energy, mcp-model-context-protocol, rlhf, superposition duplicate, scaling-law duplicate)
- New pages created: 3 (epistemic-energy, mcp-model-context-protocol, reinforcement-learning-from-human-feedback — all upgraded from stub)
- Pages updated: 2 (neural-interpretability.md — removed broken link to deleted superposition stub; index.md — fixed duplicate entries)
- Cross-links added: 10+
- Stubs resolved: 5 (epistemic-energy, mcp-model-context-protocol, rlhf promoted; superposition, scaling-law singular deleted)
- Net stub count: 182 → 175 (3 promoted, 2 deleted, 7 net reduction)

## New Entries

### epistemic-energy.md (stub → active)
Full concept page for epistemic energy as a first-class information-theoretic resource in agentic AI systems. Content: definition as reasoning energy analogous to metabolic energy, EDM disruption as depletion signal (high Δ = accelerated depletion), EFHF Layer 4 coherence monitoring implementation, candidate measurement approaches (attention entropy, context utilization, perplexity on known facts). Connects to agent-native-design (where it was first introduced), MOP/EFHF (Layer 0/4), and working-memory (active maintenance substrate). 4 open questions on measurement, refill mechanisms, cross-session transfer, and individual differences.

### mcp-model-context-protocol.md (stub → active)
Full concept page for MCP as an open standard protocol for AI-tool interoperability. Covers: client-server architecture, tool discovery and invocation, Hermes Agent's bidirectional MCP support (client + server), the MCP servers in the LLM-WIKI stack (mcp-logic, project-synapse, verifier-graph, etc.), and mcp-logic's role as EFHF Layer 3. 85% confidence.

### reinforcement-learning-from-human-feedback.md (stub → active)
Full concept page for RLHF as the dominant alignment training methodology. Covers: the standard pipeline (comparison data → reward model → RL fine-tune), PPO vs DPO vs GRPO algorithm comparison, MOP tension with KL-regularization (PPO pushes deterministic, MOP requires stochastic), GRPO's structural compatibility with MOP, reward hacking and limitations. 85% confidence.

## Deleted Entries

### superposition.md — DELETED (duplicate)
Redundant stub. The `neural-interpretability.md` page has comprehensive superposition treatment in lines 42–63 (neurons ≠ features, sparse autoencoders, Anthropic's key insights). The stub added no value. Removed the broken `[[superposition]]` link from neural-interpretability.md Connections section (replaced with inline note pointing to the existing treatment). Index.md updated.

### scaling-law.md — DELETED (duplicate of scaling-laws.md)
Singular form of the already-covered `scaling-laws.md`. The stub's only outgoing links were to active pages (scaling-laws, power-law-scaling, inference-time-compute-scaling) so no broken links were introduced. Index.md updated to point to the canonical `scaling-laws.md` entry.

## Gap Analysis

**~175 stubs remain** (net -7 from Jun 25's 182). Next priority clusters per carryover:

1. **epistemic-energy** ✓ filled this cycle
2. **scale-related batch**: taylors-law (ecological scaling, connects to scaling-laws), power-law-scaling (needs evaluation — it actually has decent content), allometric-scaling (biological stub)
3. **mcp-model-context-protocol** ✓ filled this cycle
4. **llm-inference** (stub, NAMM + KV cache mentions — has more content than typical stub, should evaluate)
5. **llm-training** (stub, mentions catastrophic-forgetting/control-llm/GRPO/RLHF connections)
6. **reinforcement-learning-from-human-feedback** ✓ filled this cycle
7. **esa** — file doesn't exist; carryover listed it but no stub found. Possibly ingested elsewhere.
8. **hermes-agent-skills**, **agentic-design-picker** — system stubs, not AI/ML research

**Remaining duplicate candidates**: power-law-scaling has more content than a typical stub (it already has the neural scaling law formula) — should evaluate for upgrade vs keep as-is rather than delete.

## Open Questions (from carryover — verified against wiki before listing)

1. **MoE routing collapse under RLHF** — No empirical data. Still unresolved. Monitor.
2. **Adaptive budget learning** — No clear paper yet. Still unresolved.
3. **Hybrid reward models (ELHSR + SD-Search)** — Emerging direction, no full treatment. Still unresolved.
4. **Reward hacking detectability** — No reliable early-warning signal. Still unresolved.
5. **Category theory for neural network verification** — Category theory filled; neural-interpretability filled; the specific question (attention = closed monoidal category) remains unresolved.
6. **Cognitive world models for LLM agents** — world-model filled; the specific question of text-based agent representation remains open.
7. **MOP training for transformers** — agent-native-design filled; the specific training question remains open.

## Stub Count
Accurate count as of this cycle: **175 concept stubs** (net -7 from Jun 25's 182). Counting method: `rg "status: stub" wiki/concepts/*.md -l | wc -l`.
