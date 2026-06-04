---
summary: Memory mechanisms in neural systems — taxonomy of implicit vs explicit memory, the timespan-access tradeoff, and the 2024-2026 architectural explosion (Mamba, TTT, Titans, MOP)
tags: [memory, neural-networks, attention, recurrent, mamba, transformer, lifelong-learning]
updated: 2026-06-04T14:07:22Z
---

---
created: 2026-05-25
updated: 2026-06-04
type: concept
summary: "Memory mechanisms in neural systems — taxonomy of implicit (recurrent/attention) vs explicit (episodic/semantic store) memory, the timespan-access pattern tradeoff, and how modern LLM architectures blur the line"
tags: [memory, neural-networks, attention, recurrent, mamba, transformer, lifelong-learning]
sources: [https://arxiv.org/abs/2310.18357 (TTT, Sun et al. 2023), https://arxiv.org/abs/2402.17427 (Titans, Behrouz et al. 2024), https://en.wikipedia.org/wiki/Memory_(engineering) (Baddeley, multi-store model), https://arxiv.org/abs/2406.07584 (Mamba-2)]
status: active
confidence: 0.7
---

# Memory Mechanisms

## Definition

**Memory mechanisms** in neural systems are the architectural and algorithmic means by which information from past computations is carried forward into future ones. The term is intentionally broad: it spans attention (a transient, content-addressable cache over the current context), recurrence (a compressed state carried across steps), explicit storage (an external, queryable database), and parameter memory (information baked into weights through training).

The central question that organizes this space: *how should past information be represented, indexed, and retrieved to influence future computation?* Different mechanisms answer this question with different tradeoffs on retention time, access cost, capacity, and updateability.

## Why a Taxonomy Matters

The 2023–2026 generation of LLM architectures has been defined by a steady expansion of memory mechanisms. The original Transformer is essentially memoryless: every token is computed from the current context, with no carry-forward state. Subsequent work has added:

- **Recurrent state-space models** (S4, Mamba, RWKV): a fixed-size recurrent state compressed from the entire context, read at each step.
- **Long-context attention** (RoPE extension, sliding window, ring attention): extended the context window from 2K to 1M+ tokens.
- **Test-time training / long-term memory modules** (TTT, Titans, Atlas): a learnable memory module updated *at inference time* on the input sequence.
- **Retrieval-augmented memory** (RAG, RETRO, kNN-LM): external vector stores read at each step, indexed by content similarity.
- **Tool/external-store memory** (MemGPT, MOP, agent scratchpads): explicit structured logs maintained by the agent itself, outside the model's context window.

These are not just implementation choices. They correspond to *different cognitive roles* — short-term scratch, working context, episodic record, semantic knowledge, parametric skill. Treating them as interchangeable misses the structural distinctions that cognitive science has known for decades.

## Baddeley-Inspired Taxonomy for Neural Systems

A useful frame is to import Baddeley's multi-store model from cognitive science and ask which neural mechanism plays each role:

| Cognitive role | Neural analogue | Properties |
|---|---|---|
| **Sensory buffer** | Token embeddings + initial layers | High-bandwidth, sub-second, no persistence |
| **Working memory** | Self-attention over current context | Limited capacity, content-addressable, ephemeral |
| **Episodic buffer** | Explicit episodic store (MOP Layer 1) | Time-indexed, queryable, persistent across sessions |
| **Long-term memory** | Recurrent state / TTT module / Mamba state | Compressed, fast access, implicit |
| **Semantic memory** | Model parameters (from pretraining) | Slow to update, high capacity, only via training |
| **Procedural memory** | Tool-use policies, cached skills | Action-level, hard to inspect, persistent |

The mapping is not perfect — neural systems collapse some distinctions (e.g., long-term and semantic are partially fused in a transformer) — but it gives a vocabulary. A useful diagnostic for any new memory mechanism: *which of Baddeley's roles does this mechanism play, and what did the previous mechanism leave undone?*

## The Timespan × Access Cost Tradeoff

Memory mechanisms are best understood by a single tradeoff axis:

- **Timespan** (how long the memory persists): transient (one forward pass) < short-term (a few hundred tokens) < long-term (a context window) < persistent (across sessions) < permanent (in weights).
- **Access cost** (how much compute to read or write): O(1) < O(log n) < O(n) attention < O(n²) full attention < O(n × d) external retrieval.

The "good corner" — long timespan AND low access cost — is the design target. Mamba achieves it with a fixed-size recurrent state (long timespan, O(1) per step) but at the cost of lossy compression. Full attention has O(n) access (relative to the cached KV) but no compression — every previous token is preserved exactly. TTT and Titans try to have it both ways: a learnable long-term memory that is compressed but lossless, updated by gradient steps at test time.

The architectural progression in the 2024–2026 era is mostly an attempt to push the Pareto frontier outward — longer timespan, lower cost, less loss. There is no winner yet; the right answer depends on the workload.

## Implicit vs Explicit Memory

The most consequential structural distinction is between **implicit** and **explicit** memory:

- **Implicit memory** is encoded in the parameters or state of the model itself. A transformer with KV-cache has implicit memory of the conversation; a Mamba has implicit memory of the sequence; a trained model has implicit memory of its training data. The user cannot inspect, edit, or index this memory directly.

- **Explicit memory** is a first-class, addressable object outside the model's weights. An episodic log, a vector store, a knowledge graph, a scratchpad — all explicit. The user can query it, edit entries, and reason about its contents. The model reads it via retrieval or tool calls.

The tradeoff: implicit memory is fast (parallel attention, recurrent state) but opaque; explicit memory is slow (retrieval round-trip) but inspectable. The strongest agent architectures combine both — implicit for speed and continuity, explicit for auditability and grounded reasoning.

## The 2024–2026 Architectural Explosion

A few notable memory mechanisms from the recent literature, organized by where they sit on the timespan/cost tradeoff:

### Mamba and State-Space Models

[[mamba]] and its descendants use a fixed-size recurrent state with selective input gating. The state is compressed; capacity is O(state_dim) regardless of context length. The tradeoff: bounded capacity, but O(1) per-step compute. Mamba-2 (2024) shows the connection to linear attention more formally.

### Test-Time Training (TTT) and Long-Term Memory

[[titans]] and the TTT line introduce a learnable memory module that is *updated at inference time* via gradient steps on the input. The memory is compressed (small relative to the sequence) but trained, so it can be lossless in the sense of carrying the information needed for downstream tasks. Titans' long-term memory is a 256-dim or 1024-dim vector, but the fact that it is *learned* on the input gives it a different expressive power from a fixed recurrent state.

### Recurrent Depth and Adaptive Computation

The [[mixture-of-recursions]] line combines the MoE and adaptive-computation ideas: route tokens through different *depths* of recursive processing, paying more compute on hard tokens. This is a memory mechanism in a different sense — the memory is the route history, and the policy decides which tokens to "remember" (process deeply) versus pass through.

### Tool-Based and External Memory

[[bounded-structured-memory]], [[mop-architecture]], and agent frameworks like MemGPT make the memory layer an *external* store, written to and read from via tool calls. The model is responsible for what to write and what to retrieve; the store is responsible for retention, indexing, and query. This is the explicit-memory regime: the user can inspect the store directly, and the model's "memory" is portable across context windows and sessions.

## Connection to Continual Learning and Plasticity

Memory mechanisms are the *inference-time* face of a deeper problem: how should a learning system integrate new information over time? [[continual-learning]] addresses the training-time version (catastrophic forgetting, plasticity-stability dilemma). Memory mechanisms address the inference-time version (what does the model "know" right now about this user, this session, this task?). The two are linked: an inference-time memory mechanism can act as a *bridge* to fine-tuning (MemGPT-style), and a training-time continual-learning method can be backed by an inference-time store (rehearsal buffers).

The [[bounded-rationality]] page is the conceptual parent of this whole line. The bounded-rational agent has finite memory, finite compute, and finite attention; the entire field of memory mechanisms is the engineering response to that constraint.

## Connections

- [[working-memory]] (0.7) — the active-context tier of the memory hierarchy, content-addressable via attention.
- [[neural-long-term-memory]] — implicit, recurrent, compressed forms.
- [[mop-architecture]] (0.75) — the explicit-memory framework; Layer 1 is episodic, Layer 2 is semantic, Layer 3 is parametric.
- [[bounded-structured-memory]] — the implementation pattern for explicit stores.
- [[mamba]] — the canonical state-space example.
- [[titans]] — the test-time-training example.
- [[concepts/maximum-occupancy-principle]] — the behavior theory that motivates MOP; combined with explicit memory, gives a complete agent substrate.
- [[continual-learning]] — the training-time analog; experience replay is a memory mechanism.
- [[bounded-rationality]] — the conceptual parent.
- [[sources/papers/recuriosity-episodic-context-3d-exploration-2026]] — the embodied-agent exemplar; the architecture pair (persistent world model + episodic policy) is a concrete memory-mechanism composition.

## Source Anchors

- [[working-memory]] (0.7) — the in-context tier, fully defined.
- [[mop-architecture]] (0.75) — the explicit-memory framework.
- [[titans]] (active) — test-time training memory module.
- [[bounded-structured-memory]] — the explicit-store pattern.
- [[sources/papers/recuriosity-episodic-context-3d-exploration-2026]] (0.95) — the embodied-agent exemplar.

## See Also

- [[episodic-memory]] — the time-indexed, queryable tier of explicit memory.
- [[agent-memory-patterns]] — design patterns for memory in LLM agents.
- [[bounded-memory-budget-optimization]] — what to do when memory grows beyond budget.
- [[memory-augmented-neural-networks]] — the broader NTM/DNC tradition.
- [[reasoning-memory-tradeoff]] — how memory capacity affects reasoning depth.

## Open Questions

- [ ] What is the *correct* interface between implicit (recurrent) and explicit (stored) memory? Should the model decide what to externalize, or should this be a system-level policy?
- [ ] How much can a TTT-style long-term memory module replace explicit storage? The two are functionally overlapping; the boundary is unclear.
- [ ] What is the right update rate for a long-term memory module — every step, every token, every context-window handoff?
- [ ] Can memory mechanisms be *composed hierarchically* (a fast L1 over recent context, a slow L2 over session history, a permanent L3 in weights) without losing the ability to reason across them?
- [ ] How do memory mechanisms interact with [[mixture-of-experts]] routing? A token that has been "forgotten" by the routing policy is effectively pruned from memory; this is a failure mode the field has not yet characterized.
