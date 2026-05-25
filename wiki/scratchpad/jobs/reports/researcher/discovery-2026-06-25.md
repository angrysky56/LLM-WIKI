# Researcher Discovery Report — 2026-06-25

## Discovery Cycle
- Topics researched: 6 (recursive-transformers, working-memory, subagent-delegation, bounded-structured-memory, steering-vectors/knowledge-store duplicates)
- New pages created: 2 (recursive-transformers, working-memory — both upgraded from stub)
- Pages updated: 2 (subagent-delegation, bounded-structured-memory — stub→active)
- Cross-links added: 12+ (per new content above)
- Stubs resolved: 4 (subagent-delegation, bounded-structured-memory, steering-vectors, knowledge-store)
- Net stub count: 186 → 182 (before delete: 186; deleted: steering-vectors, knowledge-store; promoted: recursive-transformers, working-memory = 182)

## New Entries

### recursive-transformers.md (upgraded from stub)
Recursive transformer architectures reuse shared layer blocks across multiple forward passes per token, enabling adaptive per-token computation depth. Built on Mixture-of-Recursions (MoR) paper: parameter sharing via Middle-Cycle strategy, token-choice vs expert-choice routing, KV caching strategies. Per-token recursion depth connects to causal state complexity — deep recursion tokens may be OOD signals.

Key connections: mixture-of-recursions (primary source), reasoning (latent thinking substrate), latent-reasoning (vertical computation), adaptive-computation, causal-state-edm-ood-isomorphism.

### working-memory.md (upgraded from stub)
Full treatment of working memory as cognitive temporary storage system. Baddeley's model (phonological loop, visuospatial sketchpad, central executive, episodic buffer). Amnesiac agent problem in LLMs: attention weight decay, activation interference, retrieval failure. MOP-EDM framework integration: MOP path entropy maintained via working memory tracking, EDM disruption signal detects inconsistent representations, sheaf-consistency-enforcer monitors coherence.

Key connections: bounded-rationality, agent-native-design, world-model, recursive-transformers (recursion as working memory rehearsal), critical-initialization-biological-neural-networks, efhf.

## Updated Entries

### subagent-delegation.md (stub → active)
Promoted from stub. The existing content was substantive but lacked explicit status update. Content confirmed: isolation, parallelism, bounded context, non-durability as core characteristics; Hermes delegate_task specs (3 concurrent, configurable toolsets, isolated terminal). Confirmed connections to delegation, agentic-hierarchy, bounded-structured-memory, hermemes-agent are all valid and point to active pages.

### bounded-structured-memory.md (stub → active)
Promoted from stub. Layered memory architecture for agent continuity. Valid connections to markovian-carryover and hermes-agent (both active). Updated frontmatter from stub to active.

## Deleted Entries (duplicate/superfluous)

### steering-vectors.md — DELETED
Duplicate of `activation-steering.md`. The stub had minimal content and only linked to MOP. Activation-steering.md has comprehensive coverage of steering vectors (RepE, CAA, SHARP, EAST, PID Steering), so the stub added no value. No other pages link to steering-vectors.md.

### knowledge-store.md — DELETED
Generic stub with no clear scope. The concept of "knowledge storage and retrieval systems" is too broad and is better covered by existing pages: `titans.md` (three-tier memory), `memex.md` (Vannevar Bush associative trails), `persistent-knowledge-compilation.md` (knowledge curation). No pages link to knowledge-store.md.

## Gap Analysis

**~181 stubs remain** (182 after accounting for today's fills/deletions). Next priority clusters:

1. **epistemic-energy** — stub, connects to agent-native-design/EFHF (both active). Highest priority per carryover.
2. **scale-related stubs** — taylors-law (ecological scaling, connects to scaling-laws), scaling-law (singular of scaling-laws, mostly duplicate)
3. **qes / directed-preferential-placement** — evaluated but deferred; qes is a NAS tool with thin source, DPP is a language evolution model with no clear MOP connection. Both need external research to fill properly.
4. **superposition** — stub but neural-interpretability already has full treatment in-body (line 44-48 discusses it extensively). The stub is redundant.
5. **Domain batch**: esa, mcp-model-context-protocol, llm-inference, llm-training — all stubs, all need evaluation before filling

**Duplicate detection findings**:
- `steering-vectors.md` → duplicate of `activation-steering.md` (DELETED)
- `knowledge-store.md` → superseded by `titans.md`, `memex.md` (DELETED)
- `scaling-law.md` (singular) → likely duplicate of `scaling-laws.md`; recommend evaluating and deleting
- `superposition.md` → redundant with neural-interpretability.md treatment; recommend evaluating for deletion

## Open Questions (from carryover — verified against wiki before listing)

1. **MoE routing collapse under RLHF** — No empirical data. Still unresolved. Monitor.
2. **Adaptive budget learning** — No clear paper yet. Still unresolved.
3. **Hybrid reward models (ELHSR + SD-Search)** — Emerging direction, no full treatment. Still unresolved.
4. **Reward hacking detectability** — No reliable early-warning signal. Still unresolved.
5. **Category theory for neural network verification** — Category theory filled (Jun 26); neural-interpretability filled. The specific question (attention = closed monoidal category) remains unresolved but lower priority.
6. **Cognitive world models for LLM agents** — world-model filled; the specific question of text-based agent representation remains open but not actively researched.
7. **MOP training for transformers** — agent-native-design filled; the specific training question remains open.

## Stub Count Note

Accurate count as of this cycle: **182 concept stubs** (down from 186). Counting method: `rg "status: stub" wiki/concepts/*.md -l | wc -l`. Entity stubs (in wiki/entities/) are distinct and not included in this count.