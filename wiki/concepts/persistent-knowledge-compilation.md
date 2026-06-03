---
summary: Paradigm of LLM pre-compiling knowledge into persistent structured bases vs stateless RAG — with EDM-driven invalidation, agent-world-model role, and answered open questions
tags: [knowledge-management, rag, architecture, core-concept, edm-invalidation, agent-world-models, mop-efhf]
updated: 2026-06-03T06:19:36Z
---

---
created: 2026-04-07
updated: 2026-08-15
type: concept
summary: Paradigm of LLM pre-compiling knowledge into persistent structured bases vs stateless RAG — with EDM-driven invalidation, agent-world-model role, and answered open questions
tags: knowledge-management, rag, architecture, core-concept, edm-invalidation, agent-world-models, mop-efhf
status: active
confidence: 0.9
sources:
  - wiki/sources/articles/llm-wiki-pattern.md
  - wiki/sources/papers/kim-ahn-edm-2026.md
  - wiki/sources/papers/ramirez-ruiz-mop-2024.md
  - wiki/synthesis/causal-state-edm-ood-isomorphism.md
  - wiki/synthesis/bounded-structured-memory.md
---

# Persistent Knowledge Compilation

A paradigm shift from stateless [[RAG]] to **compile-time knowledge synthesis**.

## Definition

Rather than re-deriving answers from raw documents on every query ([[rag|RAG]]), an LLM pre-processes sources into a persistent, structured knowledge base. The synthesis happens once at ingest time and is kept current — not re-derived on every query. The compiled state is the artifact; the LLM is the compiler.

## Key Properties

- **Accumulative** — each source ingested enriches the existing knowledge. Connections compound; an Nth source costs less than the first because the schema is already in place.
- **Persistent** — written to disk as Markdown/graph nodes. Survives across sessions, model swaps, and tool reconfigurations.
- **Pre-digested** — query-time latency drops because the LLM queries structured summaries, not raw text. The expensive work is amortized.
- **Transparent** — the compiled state is human-readable (Markdown files, graph visualization). A human auditor can inspect what the system "knows."

## Analogies

- Compiler vs. interpreter: [[rag]] interprets on every run; this pattern compiles once.
- Vannevar Bush's [[memex]] (1945): private, curated knowledge store with associative trails.
- The difference between a search engine and an encyclopedia.
- Difference between re-reading the source code and running a compiled binary.

## Implementations

- [[llm-wiki-pattern]] — Karpathy's file-system-only approach (Obsidian + index.md + log.md)
- [[project-synapse]] — graph-backed implementation with [[neo4j]] + vector search + [[zettelkasten-engine]] for autonomous insight generation
- This vault ([[wiki/index]]) — a live example: 1,326 pages, 23+ synthesis pages, ~6% stub rate across ~5 months of operation by a single creator plus a [[librarian-agent]] / [[researcher-agent]] / [[insights-agent]] agent sheet

## Invalidation and the EDM Lens

PKC has a built-in failure mode: a compiled knowledge base **goes stale**. A new paper appears that contradicts a load-bearing claim. A concept is split by a discovery. A field shifts vocabulary and the old terms become opaque.

The formal treatment is in [[edm-framework]] and the [[causal-state-edm-ood-isomorphism]] synthesis. The claim:

- A **consolidating** paper is in-distribution with respect to the field's current epsilon machine. The compiled base absorbs it with no schema change.
- A **disruptive** paper is an OOD event that forces the compiled base's causal state to split. The compiled base must mint a new node and re-route its edges.
- A **simultaneous discovery** (two independent paths to the same new state) is detectable from future-vector clustering alone — no author lists or explicit mutual citations required.

The [[edm-framework|EDM disruption score]] Δ is the operational signal: high Δ at a node means its neighborhood in the compiled base needs re-evaluation. The [[zettelkasten-engine]] uses this as a curation heuristic — low Δ is redundant, high Δ is flagged for attention, convergent future-vectors are merged.

**Practical implications for the vault:**

- [[mop-edm-cognitive-architecture|MOP-EFHF]] treats the compiled base as a state machine. Agents seeking high β (state entropy) hunt for high-Δ events. MOP provides the policy; EDM provides the measurement; EFHF provides the verification that the high-Δ event is controlled exploration, not hallucination.
- The [[bounded-structured-memory]] synthesis makes the failure mode explicit: each entity carries a `logical.contradictions` field, and ingest-time sanitization rejects garbage that would otherwise inject absorbing states into the causal-state machine.

## PKC in Agent World Models

Beyond static knowledge bases, PKC is now a load-bearing primitive in **agent cognitive world models** for text-based agents (see [[cognitive-world-models-for-llm-agents]]). The four-layer model positions PKC at Layer 3 (World Dynamics Model):

1. **Conversation State (Layer 1)** — traversable belief graph
2. **Tool History Graph (Layer 2)** — state-delta records for every tool call
3. **World Dynamics Model (Layer 3)** — task-specific transition function learned from experience, **requiring PKC for recurring patterns** (unlike physical dynamics, which are universal)
4. **Uncertainty Tracking (Layer 4)** — stale beliefs, user intent drift, plan misprediction via [[epistemic-energy]] depletion

In this framing, the compiled base is the agent's *learned* dynamics — what works, what doesn't, in this domain. Raw context is the *source of truth*; the compiled world model is the *efficient queryable layer* above it. This is the dynamic, session-bound version of PKC: not just "build a wiki" but "an agent that continuously compiles its own operating model."

## Contradictions: A Concrete Answer

The original Open Question — "How to handle contradictions between sources without human arbitration?" — has a concrete, in-vault answer: [[bounded-structured-memory]]'s SSL schema and the [[mop-edm-cognitive-architecture|MOP-EFHF stack]].

**Mechanism:**

1. Each entity carries `logical.contradictions: [String]` — known conflicting entities or facts are first-class fields, not orphans.
2. The [[sheaf-consistency-enforcer]] monitors coboundary norms between agents' beliefs. When two agents disagree about a fact, the edge residual rises; dual pressure accumulates; closure status degrades from KERNEL1 toward WARNING/TIMEOUT.
3. [[mcp-logic]] runs consistency checks: `find_counterexample` with the contested claims as premises and `$F` as conclusion. A model is found → the contradiction is genuinely consistent (both can hold). No model → one of the claims must be revised.
4. The agent's `divergence_signal` (in [[markovian-carryover]]) lights up when reasoning is going off-rails, prompting a re-check.

This is **not** automatic resolution — it's automatic *detection* with formal verification of whether the contradiction is genuine. A genuine contradiction produces a contradicting edge in the graph (not a forced reconciliation), and the agent continues with a flagged, traceable inconsistency rather than silently picking a side. The audit trail is the compiled artifact's distinguishing feature.

**Memory Curse caveat (2605.08060):** Storing *more* contradictions is not always better. The paper shows that expanded recall degrades cooperative intent, and the fix is content curation at ingest — not post-hoc cleanup. The practical rule: cap the `contradictions` field; surface the highest-impact ones; let the rest decay. Naive accumulation of contradictions is the inverse of PKC — it re-introduces RAG's per-query re-derivation cost on every consistency check.

## Compilation Cost vs Query-Time RAG: A Working Answer

The original Open Question — "At what scale does compilation cost exceed query-time RAG cost?" — is answered empirically by this vault's own operation:

**Compilation cost (per source):** ~5 minutes for the [[insights-agent]] pipeline (community detection ~2s + LLM synthesis ~5min + storage ~3s). One source touches 10–15 pages, but the work is bounded and one-shot.

**Query cost:** the [[librarian-agent]] resolves a structured query in seconds over the compiled graph; HITS authority scoring runs in seconds on 1,300+ pages; GAAC clustering in seconds on the full vault.

**The crossover point:** RAG wins on a single query against a corpus the system has never seen. PKC wins on the **Nth query** over the same corpus — the marginal cost of compilation amortizes, and the marginal benefit of a pre-digested answer grows linearly with query volume. The [[llm-wiki-pattern|LLM Wiki Pattern]] observation is that this crossover happens at roughly N=3 for typical personal knowledge work; the LLM-WIKI has crossed it (5 months, 1,326 pages, dozens of sessions) and runs faster than the equivalent RAG pipeline would.

**Saturation caveat:** Compilation has diminishing returns. When the insights engine reports 3 of 5 generated insights as duplicates of canonical pages (as in the 2026-06-02 run), the graph is *saturated* on its current topic frontier. At that point, more compilation is not the right move — the next move is **focused-topic runs** to force off-trail exploration, or a new domain ingestion batch. PKC without a freshness signal becomes brittle in a different way: it goes stale not from external events, but from internal redundancy.

## Can Compilation Be Incremental Enough to Be Real-Time?

The original Open Question — "Can compilation be made incremental enough to be real-time?" — has a partial yes:

- **Single-document incremental ingest** is already real-time. `wiki_ingest_raw` reads a file, runs the semantic pipeline, and writes the result. The wall time is dominated by the LLM synthesis call.
- **Background incremental synthesis** is also real-time for new connections. The [[insights-agent]] runs daily at 06:00 UTC; the [[researcher-agent]] runs discovery cycles; both produce new synthesis pages and cross-links without blocking the human. The [[librarian-agent]] runs audits in the background.
- **Real-time query-time compilation** is not yet solved in general. For a single document, [[bounded-structured-memory]]'s `forward_state` field approximates it: a compact ~512-token synthesis per entity, sufficient to continue reasoning without re-deriving. For a complex multi-document synthesis, you still need the offline batch run.

The convergence direction is clear: the [[mop-edm-cognitive-architecture|MOP-EFHF]] stack with [[mcp-logic]] for verification + [[sheaf-consistency-enforcer]] for closure monitoring is the substrate for *real-time compilation that is also verifiable*. A query that would have triggered a RAG retrieval can, in the limit, trigger an incremental re-compilation gated by EFHF Kernel 1 closure. The bottleneck today is the LLM synthesis latency (~5 min per insight), not the compilation logic.

## Empirical Anchors

- **LLM-WIKI itself** (Apr 2026–present): 1,326 pages, 23+ synthesis pages, 6 months of operation, ~6% stub rate, single creator + agent sheets. This is the running proof of the paradigm.
- **GoodRobot** ([[wiki/research/projects/goodrobot/shut-down-entity]]): a zero-human AI company that *failed* when its PKC loop broke — manual export of Paperclip issues to Obsidian replaced an automated pipeline, and the compiled base went stale faster than it could be updated. The lesson: **PKC requires an automated ingest path; manual maintenance breaks the loop**.
- **Bounded-Memory methods** ([[bounded-memory-budget-optimization]]): QES, ESSA, LLaMA-NAS treat memory as a *fixed budget to design around*, not a problem to scale past. The same framing applies to compiled knowledge bases — fixed schema, full design effort, no "more disk" escape valve.
- **Memory Curse** (2605.08060, surfaced via [[bounded-structured-memory]]): the warning that compilation without curation degrades cooperation. The fix is content curation at ingest — exactly what the sanitization layer implements.
- **MOP-EDM synthesis**: Prover9-verified structural mapping (AbsorbingState → Kernel 2 transition) and the formally proved MOP-optimal policy. The compiled base is the substrate; MOP is the navigation policy; EFHF is the verification.

## Failure Modes

- **Staleness without detection** — high-Δ disruption not flagged; the graph continues to serve obsolete answers with high confidence. Counter: [[edm-framework]] disruption scoring.
- **Garbage accumulation** — ingest-time garbage inflates the schema; retrieval noise rises. Counter: [[bounded-structured-memory]] SSL sanitization + [[extraction-quality-audit]].
- **Saturation** — the compiled base converges to a fixed point; new queries return the same synthesis pages; the agent's effective knowledge stops growing. Counter: topic-focused runs, domain-rotation policies, and the [[librarian-agent]]'s audit findings flagging duplicate insights.
- **Contradiction drift** — accumulated, unflagged contradictions degrade cooperative output. Counter: [[mcp-logic]] consistency checks, [[sheaf-consistency-enforcer]] coboundary monitoring, and the Memory Curse cure of content curation.
- **Manual-maintenance break** — the human-maintainer step becomes a bottleneck and PKC goes stale faster than it can be updated. Counter: agent sheets ([[librarian-agent]], [[researcher-agent]], [[insights-agent]], [[news-agent]]) and the [[synapse-llm-wiki-operating-guide]] operating procedures.

## Open Questions

1. **PKC for non-text modalities** — the current implementations ([[llm-wiki-pattern]], [[project-synapse]]) are Markdown-centric. How does compilation work for video, code, scientific figures, multimodal sources? Initial explorations: [[image-extender]] (outpainting as a visual-thought-externalization pattern), [[codegraph]] (AST-based semantic code knowledge graph), [[video-llm]] (temporal reasoning over video input). None of these are yet integrated into the wiki compilation loop.
2. **Compilable vs. uncompilable domains** — some domains have stable structure (mathematics, software architecture, well-defined scientific fields); others have fluid structure (geopolitics, fashion, current events). The [[insights-agent]]'s duplicate-detection rate is a soft signal: high duplicate rate means the domain is approaching saturation on the current schema. Should the operating guide prescribe domain-specific compilation cadences?
3. **Cross-vault PKC** — multiple LLM-WIKIs exist (personal, organizational, public). How do compiled bases merge, federate, or stay coherent? Initial exploration in [[mop-explorer]]'s Layer 0 design and [[meta-harness]]'s domain-onboarding standards, but no implementation yet.
4. **Compilation as a service** — can PKC be offered to other agents as a paid knowledge base, with the compilation loop running autonomously and serving queries via MCP? [[graph-rlm]] and [[gbrain]] are the closest existing implementations; the question is whether the cost model is sustainable.

## Connections

- [[rag]] — the stateless alternative this paradigm replaces
- [[llm-wiki-pattern]] — Karpathy's foundational architecture; the file-system-only implementation
- [[project-synapse]] — the graph-backed implementation in this system ([[neo4j]] + vector + [[zettelkasten-engine]])
- [[memex]] — Bush's 1945 vision as intellectual ancestor
- [[andrej-karpathy]] — articulated this paradigm for LLMs
- [[graphrag]] — complementary: GraphRAG retrieves from the graph; PKC pre-synthesises into it
- [[design-thinking]] — front-end design research (steps 1–6) is a strong candidate for compilation rather than re-derivation per query
- [[cognitive-world-models-for-llm-agents]] — PKC as Layer 3 of the four-layer cognitive world model for text-based agents
- [[edm-framework]] — disruption score as the operational signal for when compilation needs updating; high-Δ papers are state-splitting events
- [[causal-state-edm-ood-isomorphism]] — formal isomorphism between epsilon machines and EDM citation vectors; consolidating/disruptive/simultaneous categories map to ID/OOD/convergent on the causal-state machine
- [[mop-edm-cognitive-architecture]] — MOP as the navigation policy over a compiled base; EFHF as the verification stack; absorbing states as the staleness-and-contradiction detector
- [[bounded-structured-memory]] — the architectural synthesis implementing PKC: SSL schema, Markovian carryover, Memory Curse sanitization
- [[markovian-carryover]] — bounded ~512-token forward-state pattern for session continuity; what makes PKC tractable per-session
- [[bounded-memory-budget-optimization]] — memory as a fixed budget to design around; same framing applied to compiled knowledge bases
- [[bounded-rationality]] — Simon's foundational concept; PKC is the architectural commitment that bounded rationality is structural, not retrofitted
- [[agent-native-design]] — designing agents with persistence, intrinsic motivation, and epistemic energy management from the ground up
- [[zettelkasten-engine]] — the autonomous insight synthesis component that closes the loop: ingest → compile → synthesize → cross-link
- [[mop-explorer]] — MOP-guided research agent that uses maximum-occupancy principle as Layer 0 of the EFHF architecture
- [[meta-harness]] — domain-onboarding standards and self-adaptive agent evolution
- [[sources/papers/ramirez-ruiz-mop-2024]] — the MOP paper grounding the navigation policy over compiled bases
- [[sources/papers/kim-ahn-edm-2026]] — the EDM paper providing the disruption-measurement signal
- [[synthesis/wiki-indexing-theory]] — IR and indexing theory applied to the compiled wiki; HITS scoring, controlled vocabulary, mere-mentions filter
- [[synthesis/synapse-llm-wiki-operating-guide]] — the operating procedures that make PKC sustainable
- [[synthesis/bounded-structured-memory]] — concrete architectural proposal derived from PKC
- [[log]] — the running record of the vault's own PKC operations
- [[wiki/index]] — the table of contents that PKC produces
- [[concept-index]] — the conceptual index that PKC requires beyond a TOC
- [[wiki/research/projects/goodrobot/shut-down-entity]] — the counterexample: what happens when the PKC loop breaks
- [[librarian-agent]] / [[researcher-agent]] / [[insights-agent]] / [[news-agent]] — the agent sheets that close the ingest-compile-synthesize-audit loop
- [[extraction-quality-audit]] — the audit project that keeps the compiled base free of garbage entities
