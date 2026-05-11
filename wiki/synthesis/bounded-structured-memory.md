---
created: 2026-05-13
updated: 2026-05-13
type: synthesis
summary: Unifying SSL schema + Markovian carryover + Memory Curse fixes into a bounded structured memory architecture for Synapse
tags: [memory, architecture, SSL, markovian, memory-curse, entity-extraction, skill]
status: active
confidence: 0.85
sources: 
  - https://arxiv.org/abs/2605.08060 (Memory Curse)
  - https://arxiv.org/abs/2604.24026 (SSL)
  - https://arxiv.org/abs/2510.06557 (Markovian Thinker)
---

# Bounded Structured Memory: SSL + Markovian Carryover for Synapse

**Type:** Synthesis — architectural proposal  
**Derives from:** [[synapse-retrieval-architecture]], [[persistent-knowledge-compilation]], [[zettelkasten-engine]]  
**Supersedes:** raw extraction pipeline (current)

---

## Motivation

Three recent papers converge on the same diagnosis from different angles:

| Paper | Finding | Implication for Synapse |
|---|---|---|
| **Memory Curse** (2605.08060) | Expanded recall degrades cooperative intent; fix is *content curation* — synthetic cooperative records restore cooperation even at fixed prompt length | Ingest-time sanitization > post-hoc cleanup; what gets stored shapes agent behavior |
| **SSL** (2604.24026) | Skills represented as raw text are machine-unfriendly; disentangling into Scheduling/Structural/Logical layers gives +12% MRR in retrieval, +24% F1 in risk assessment | Entity nodes need structured schema, not just raw name + embedding |
| **Markovian Thinker** (2510.06557) | Bounded state decouples reasoning length from context size; linear compute, constant memory; agents learn to write a textual *carryover state* sufficient to continue after reset | Session working state must be bounded and explicitly synthesized, not raw transcript |

The synthesis: **structured, bounded, content-curated memory** — where structure comes from SSL, bounded persistence from Markovian carryover, and content curation from the Memory Curse fix.

---

## The Core Proposal: Two-Layer Memory Architecture

```
Session Layer (bounded carryover state)
  └─ Current working context: topic, open questions, intended direction
  └─ SSL-structured: scheduling / structural / logical slots
  └─ Bounded size: ~512 tokens max

Knowledge Graph Layer (persistent, curated)
  └─ Entities: SSL-schema nodes replacing raw extraction outputs
  └─ Facts: evidence-bearing edges with source grounding
  └─ Skill records: structured invocation interfaces
  └─ Carryover history: compressed session summaries
```

### Layer 1 — Knowledge Graph: SSL-Schematized Entity Nodes

Replace raw entity nodes (name + type + embedding) with three-slot SSL-structured nodes:

```
EntityNode {
  name: String              # Canonical form (lowercased, deduped)
  
  scheduling: {              # WHEN is this entity relevant?
    trigger_queries: [String] # Natural queries that should surface this
    context_window: [String]  # Session types where this fires
    recency_decay: Float     # 0.0–1.0, how fast relevance decays
    forward_looking: Boolean # Does this entity encode intent/goals?
  }
  
  structural: {               # WHAT can this entity connect to?
    supertype: String        # Entity type (Person, Tool, Concept, etc.)
    subrels: [String]       # Valid relation types this entity participates in
    reciprocal_links: [String] # Expected inverse relations
    capacity: String        # 'source' | 'sink' | 'transformer' | 'anchor'
  }
  
  logical: {                 # WHY does this entity hold?
    evidence: [FactRef]      # Grounded facts supporting this entity
    provenance: String       # Source file or ingest batch ID
    confidence: Float        # 0.0–1.0 extraction confidence
    contradictions: [String] # Known conflicting entities or facts
    forward_state: String    # Markovian carryover: what to remember about this
  }
}
```

**Why this matters:** The Memory Curse paper shows that *content* of recall determines behavior. SSL's scheduling slot encodes *when to retrieve* this entity — it is itself a curation signal, not just metadata. The `forward_state` slot is the Markovian carryover concept applied per-entity: instead of storing all past interactions with this entity, store a compact synthesized state sufficient to continue.

**Addressing Synapse's garbage problems:**

| Garbage pattern | SSL fix |
|---|---|
| File path entities (97) | `structural.capacity == 'source'` with path validation in scheduling |
| Single-char entities (14) | `scheduling.trigger_queries` minimum length enforcement; reject at ingest |
| Generic untyped `Entity` (203) | `structural.supertype` required; untyped → quarantine for manual review |
| Formatting artifacts | Stripped in `scheduling` normalization before write |
| Misclassified types | `structural.subrels` constrains valid relation types per supertype |

### Layer 2 — Session: Markovian Carryover State

Each session maintains a bounded working state that summarizes the current interaction context:

```
CarryoverState {
  session_id: String
  topic: String              # 1-line current topic
  open_questions: [String]  # Unresolved threads (max 5)
  intended_direction: String # What the session is working toward
  entity_context: [String]   # Entity names in scope (max 20)
  
  # SSL-structured working slots
  scheduling: {
    active_queries: [String]     # What the user is currently asking
    retrieval_mode: String       # 'explore' | 'verify' | 'build' | 'audit'
  }
  structural: {
    current_domain: String      # Which subgraph is active
    connection_frontier: [String] # Entities at the edge of current context
  }
  logical: {
    current_facts: [String]     # Facts currently in reasoning scope
    confidence: Float            # Session confidence 0.0–1.0
    divergence_signal: Boolean   # True if reasoning is going off-rails
  }
}
```

**Bounded size:** Hard cap of ~512 tokens. This is the Markovian chunk — the entire carryover state must fit in a fixed-size window, exactly as Delethink uses C=8192 token chunks.

**Carryover semantics:** At session end, the carryover state is *compressed and written to the graph* as a forward-looking `SessionSummary` node linked to all entities that were active. On session resume, this summary is the only thing loaded into the working context — not raw transcript, not full entity history.

**Relation to Memory Curse:** The Memory Curse triggers when expanded history makes agents lose *forward-looking intent*. The carryover state explicitly encodes forward-looking intent: `open_questions`, `intended_direction`, `divergence_signal`. Storing this compactly — rather than full conversation history — is the direct analog of the paper's "memory sanitization" (replacing visible history with synthetic cooperative records).

---

## Ingest Pipeline: Sanitization Layer

Insert between raw extraction and Neo4j write:

```
Raw Source Text
    │
    ├─ Lexical extraction (current)
    │       ↓
    ├─ SSL normalization
    │   ├─ Reject: single-char names, paths, formatting artifacts
    │   ├─ Classify: scheduling.trigger_queries from context
    │   ├─ Constrain: structural.supertype from relation context
    │   └─ Score: logical.confidence from extraction certainty
    │       ↓
    ├─ Carryover synthesis
    │   └─ Generate: logical.forward_state per entity
    │       (compact ~2-sentence summary of entity's role in source)
    │       ↓
    └─ Neo4j write (sanitized nodes only)
```

This is the direct implementation of the Memory Curse paper's finding: *memory sanitization* (fixed prompt length, cooperative content) restores cooperation substantially. Applied here: fixed node schema, curated content, forward-looking state synthesis.

---

## Retrieval: Bounded Recall with SSL-Constrained Expansion

```
Query
    │
    ├─ Carryover state (loaded from last session summary)
    │   └─ Sets: current_domain, active_queries, retrieval_mode
    │
    ├─ Stage 1: SSL-constrained entity seed
    │   └─ Match: scheduling.trigger_queries overlap with query
    │   └─ Filter: structural.supertype consistent with retrieval_mode
    │
    ├─ Stage 2: Bounded graph expansion
    │   └─ Max 2-hop traversal from seed entities
    │   └─ logical.confidence filter (reject < 0.5)
    │
    ├─ Stage 3: Wikilink expansion (current Stage 3)
    │   └─ Unchanged
    │
    └─ Stage 4: Insight generation (current Stage 4)
            └─ Unchanged

    ↓
Output: entity hits + facts + wiki links + insights
       (bounded: max 20 entities, 50 facts in context window)
```

**Why bounded expansion matters:** The Memory Curse shows that *more recall is not always better*. Constraining graph expansion to 2-hop from SSL-matched seeds keeps the retrieval focused. The carryover state's `current_domain` acts as an anchor — the query can only expand outward from entities relevant to the current session context.

---

## Relationship to Existing Architecture

| Component | Current | Proposed |
|---|---|---|
| Entity node schema | `name + type + embedding` | Full SSL schema (scheduling/structural/logical) |
| Session state | Full conversation transcript | Bounded CarryoverState (~512 tokens) |
| Ingest | Lexical extraction → Neo4j | Sanitization layer → SSL normalization → Neo4j |
| Extraction confidence | Implicit in embedding | Explicit `logical.confidence` score |
| Forward-looking state | None | `logical.forward_state` per entity + SessionSummary nodes |
| Graph expansion | Unbounded ANN + BM25 | SSL-constrained + bounded 2-hop |
| Garbage entities | Post-hoc cleanup (audit reports) | Ingest-time rejection + scheduling validation |

---

## Open Questions

1. **Carryover synthesis quality:** Who/what generates `logical.forward_state` for each entity? A separate fine-tuned model (as the Memory Curse paper did with LoRA on forward-looking traces), or a prompted LLM with explicit synthesis instructions?
2. **Carryover window size:** 512 tokens is a guess. Delethink uses C=8192 chunks for 24K effective budget. The right size depends on how much session context is actually needed to resume coherently.
3. **SSL schema validation:** The three SSL layers need formal constraints (what values are valid for each slot) before they can be used for ingest-time rejection rather than just post-hoc tagging.
4. **Migration of existing nodes:** 18K+ nodes already in Neo4j. Full re-ingest with the new pipeline vs. gradual migration with backfill? The domain-graph-orchestrator MCP notes recommend full re-ingest for legacy data quality — same logic applies here.

---

## Connections

- [[synapse-retrieval-architecture]] — current pipeline this extends
- [[synapse-llm-wiki-operating-guide]] — operating procedures this would replace parts of
- [[persistent-knowledge-compilation]] — paradigm this implements
- [[load-bearing-reasoning]] — what makes a reasoning trace worth storing (vs. scaffolding)
- [[maximum-occupancy-principle]] — EFHF Layer 0 connection; absorbing states ↔ stale entity nodes
- [[chain-of-thought]] — the Memory Curse finding: CoT amplifies the curse; structured carryover may be safer than raw CoT storage
- [[graphrag]] — this is GraphRAG with bounded, SSL-structured, content-curated nodes
