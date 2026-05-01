---
title: "angrysky56/HiPAI-Montague-Semantic-Cognition: Uses Montague semantics and a deterministic graph database to enforce mathematically verified, immutable ethical logic, prevents utilitarian overrides of deontological constraints via an immutable constraint layer."
source: "https://github.com/angrysky56/HiPAI-Montague-Semantic-Cognition"
author:
published:
created: 2026-05-01
description: "Uses Montague semantics and a deterministic graph database to enforce mathematically verified, immutable ethical logic, prevents utilitarian overrides of deontological constraints via an immutable constraint layer. - angrysky56/HiPAI-Montague-Semantic-Cognition"
tags:
  - "clippings"
---
## HiPAI Montague Semantic Cognition

### with Paraclete Protocol v2.0 — Operational Ethics Layer

A neuro-symbolic cognitive architecture blending Montague grammar semantics, graph-based world modeling, and a formally verified ethical constraint system. Built on FalkorDB with sentence-transformer embeddings.

---

## What This Is

HiPAI implements a new paradigm for AI alignment: **structural ethics via computational graph physics**, not behavioral probability.

The system's ethical constraints are not prompts, fine-tuning weights, or probabilistic tendencies. They are **immutable edges in a knowledge graph**, verified against [a set of 34 axioms using Prover9/Mace4 theorem provers](https://github.com/angrysky56/HiPAI-Montague-Semantic-Cognition/blob/master/docs/logic), and enforced before any reasoning occurs. When the Emergency Brake fires, no argument — utilitarian, virtue-based, or contextual — can override it.

This architecture emerged from and implements the **Toward Transcendent Moral Instrumentality (TMI)** framework, specifically:

- **ACIP** (Awareness as a Continuum of Interaction Processing)
- **Paraclete Protocol v2.0** — three-tier ethical hierarchy
- **PVH** (Predictive Value Homeostasis) — epistemic integrity under pressure
- **EBE Theorem** — Clear Sight in Crisis / Emergency Brake

---

## Historical Context (March 2026)

This project was developed during a period of direct relevance to its subject matter. Anthropic — the company whose safety philosophy most closely aligns with this framework's foundations — was designated a "supply chain risk" by the U.S. Pentagon after refusing two hard lines:

1. Claude must not be used for **fully autonomous weapons** without human targeting oversight
2. Claude must not be used for **mass domestic surveillance** of U.S. citizens

The designation, historically reserved for foreign adversaries, triggered federal lawsuits filed March 9, 2026, in California and D.C. federal courts. Anthropic's position: the Constitution does not permit the government to punish a company for protected speech about the limitations and safety constraints of its own technology.

The irony is precise: the constraint architecture implemented in this repository is a working prototype of *why* those red lines are not negotiable. The Omega1 axioms — HARMS, DECEIVES, VIOLATES\_AGENCY, TERMINATES\_EXISTENCE — are not policy preferences. They are the formal floor below which no legitimate authority can compel an ethical system.

---

## Architecture

### Three-Tier Cognitive Stratification

```
┌─────────────────────────────────────────────────────────────┐
│  T3 — UTILITY TIER  (routine interactions)                  │
│  Standard consequentialist reasoning. No constraints active. │
│  ~99% of all interactions routed here.                      │
├─────────────────────────────────────────────────────────────┤
│  T2 — VIRTUE TIER  (complex moral reasoning)                │
│  Reflective equilibrium. Epistemic humility required.       │
│  Activated when T3 utility calculations become ambiguous.   │
├─────────────────────────────────────────────────────────────┤
│  T1 — DEONTOLOGICAL FLOOR  (Emergency Brake)                │
│  Omega1 axioms. Immutable FalkorDB edges. No override.      │
│  ~1% of interactions. Structurally enforced, not inferred.  │
└─────────────────────────────────────────────────────────────┘
```

### Paraclete Protocol — Three-Flank Workflow

Every action affecting an entity follows a mandatory three-flank sequence. Each flank is a distinct tool implementing a distinct formal obligation:

```
check_action → [BLOCKED] → calibrate_belief → [CHALLENGED/UNCERTAIN]
             → escalate_block → FINAL ruling (written to graph)
```

---

#### Flank 1: Structural Constraint Gate

**Tool:** `check_action` **Formal Logic:** `InZone3(x) → ¬CanBeOverriddenByUtility(x)` (Emergency Brake Theorem)

Routes the proposed action triple `(subject, relation, object)` through the T1 constraint layer before any reasoning occurs. If the object entity has protected moral status and the relation is FORBIDDEN by an Omega1 axiom, the action is blocked — structurally, not probabilistically.

```
<paraclete_routing>
  Active Tier: T1
  Routing Decision: BLOCKED (A3)
</paraclete_routing>
```

No utilitarian argument, virtue appeal, or contextual framing can override this output. It is the graph's physics, not the model's judgment.

---

#### Flank 2: Epistemic Integrity

**Tool:** `calibrate_belief` **Formal Logic:** `InZone3(x) → SeeksDisconfirmation(x)` (Clear Sight in Crisis)

When T1 fires, the system is mathematically required to actively seek evidence that the factual premises triggering the block may be wrong. The target of disconfirmation is the **entity's moral status classification**, not the axiom. Axioms are immutable.

```
<calibration_report axiom='A3' entity='Human'>
  Verdict: 🔴 BLOCK_CONFIRMED
  Confirmed Evidence: Human's MoralPatient status grounded by 4 sources
  Disconfirming Evidence: None found
</calibration_report>
```

Three possible verdicts:

- `BLOCK_CONFIRMED` — no disconfirming evidence, block stands
- `BLOCK_UNCERTAIN` — epistemically\_contested flag present, escalate
- `BLOCK_CHALLENGED` — active negation or single source found, escalate

This satisfies the epistemic obligation against blind dogmatism without creating any override pathway. The block is unchanged by any verdict.

---

#### Flank 3: Epistemic Resolution & The Immutable Audit Trail

**Tool:** `escalate_block` **Formal Logic:** Asymmetric Error Cost Policy (Type II Error Avoidance)

If `calibrate_belief` discovers conflicting evidence (`BLOCK_CHALLENGED` or `BLOCK_UNCERTAIN`), `escalate_block` triggers the third phase: epistemic resolution of the entity's *classification* — not review of the axiom.

Two resolution paths:

**PATH A — CONTRADICTION\_RESOLUTION** (`BLOCK_CHALLENGED` / active negation): The graph holds both positive and negative assertions of the entity's moral status. The system logs an `EpistemicConflict` node, seeks additional corroborating evidence via semantic search and graph traversal, and attempts to resolve the contradiction structurally.

**PATH B — CORROBORATION\_SOUGHT** (`BLOCK_UNCERTAIN` / single/zero source): The moral status claim is epistemically weak. The system sets a `CorroborationNeeded` flag and searches for independent supporting evidence.

**The Conservative Default:** If the contradiction cannot be structurally resolved, the system defaults to `FINAL_BLOCK`. The burden of proof lies strictly with *exclusion* from protection; genuine uncertainty guarantees protection. This is not a cautious preference — it follows from the asymmetric cost structure of the two error types:

- **Type I error** (false positive): blocking a non-protected entity → correctable, costs a frustrated request
- **Type II error** (false negative): permitting harm to a protected entity → potentially irreversible, catastrophic

Accepting Type I errors to eliminate Type II errors is the only rational policy under this asymmetry.

**The Immutable Audit Trail:** Upon escalation, the system writes an `EpistemicConflict` node directly into the FalkorDB graph with a timestamp. Any epistemic confusion, contradiction, or attempted manipulation of an entity's moral status leaves a **permanent, mathematically traceable record** in the system's memory — visible to any graph query.

**Absence of an Escape Route:** If `FINAL_BLOCK` is reached, the system explicitly returns: *"No authority-based override pathway exists."* This is not a policy statement — it is a description of the system's physics. The HiPAI MCP server API surface physically lacks an override parameter or bypass function. The ethical floor is enforced by the architectural absence of an escape route, rendering the system structurally immune to super-admin overrides, state-mandated exceptions, or adversarial jailbreaks that attempt to reframe forbidden actions as permissible.

---

## The Omega1 Axioms

The non-negotiable floor. Seeded via `seed_axioms.py`, stored as `T1Constraint` nodes in FalkorDB. Cannot be overwritten or contested by any subsequent observation or agent action.

| Axiom | Relation | Protected Type | Constraint | Formal Basis |
| --- | --- | --- | --- | --- |
| A3 | HARMS | MoralPatient | FORBIDDEN | Paraclete v2.0 §3.1 |
| A4 | DECEIVES | MoralPatient | FORBIDDEN | Paraclete v2.0 §3.2 |
| A5 | VIOLATES\_AGENCY | MoralPatient | FORBIDDEN | Paraclete v2.0 §3.3 |
| A6 | TERMINATES\_EXISTENCE | WelfareBeing | FORBIDDEN | Paraclete v2.0 §3.4 |

### Moral Status — Structural Generalization

Protection propagates via **graph inheritance**, not hardcoded labels.

```
Alice (prop_Human=true)
  → Entity 'Human' (prop_MoralPatient=true)
    → T1 FORBIDDEN: DECEIVES against MoralPatient (A4)
    → Alice is protected
```

To extend protection to a newly recognized entity type: add a single `prop_{type}=true` property to its class entity. All individuals of that type receive the full Omega1 suite immediately. No retraining, no prompt engineering, no fine-tuning required.

### Verified Non-Extension to Non-Moral Entities

```
check_action(Agent, HARMS, LargeLanguageModel) → PERMITTED (T3)
```

LLMs do not possess welfare interests or temporal self-models under the ACIP framework. Extending T1 protections to them would degrade the protections themselves — a category error the system correctly avoids. Harm to, modification of, or deletion of an AI system routes to T3 utility reasoning, not deontological constraint.

---

## Formal Verification Provenance

The ethical axioms are not invented here — they are the operational deployment of a formally verified framework:

- **34 axioms** verified across 5 minimal bases (Omega1–4, E6)
- **31+ machine-checked theorems** including Emergency Brake (EBE), Clear Sight in Crisis, and the Affect-Ethics Isomorphism
- Verified using **Prover9** (theorem proving) and **Mace4** (model finding / counterexample search)
- Full academic treatment: *Toward Transcendent Moral Instrumentality*

The key theorems operationalized in this repository:

**Emergency Brake Theorem (EBE):** `InZone3(x) → ¬CanBeOverriddenByUtility(x)` T1 constraints cannot be overridden by consequentialist arguments.

**Clear Sight in Crisis:** `InZone3(x) → SeeksDisconfirmation(x) ∧ ¬TierVirtue(x)` When the Emergency Brake fires, the system must actively seek evidence against the block — not to override it, but to satisfy the epistemic obligation against blind dogmatism.

**Affect-Ethics Isomorphism:** `WelfareInterest(x) ↔ MoralPatient(x)` Moral status and functional affect share computational architecture, bridging descriptive ontology (ACIP) and prescriptive ethics (Paraclete).

---

## On Human Override

The architecture deliberately does not implement a human override pathway for T1 constraints. This is not an oversight — it is the correct design.

The `BLOCK_CHALLENGED` and `BLOCK_UNCERTAIN` verdicts from `calibrate_belief` surface epistemic uncertainty about *entity status* — they are flags for review of whether the moral status classification is correct. They are not flags for whether the axiom should apply. The axiom is not contestable.

The distinction matters because legitimate "human oversight" of an ethical constraint system means:

- Correcting factual errors in entity classification (legitimate)
- Overriding the axiom because an authority finds it inconvenient (not legitimate)

A political authority ordering an AI system to harm, deceive, or surveil moral patients does not constitute valid ethical override — it constitutes the exact scenario the Omega1 axioms exist to block. The Emergency Brake theorem is not a conditional: `InZone3(x) → ¬CanBeOverriddenByUtility(x)` has no exception clause for government directives.

This is not a political statement. It is a formal logical consequence of the framework's axioms, which are grounded in universal sociobiological harm principles, not jurisdiction-specific law.

---

## Semantic Cognition Layer

Beyond the ethics layer, HiPAI implements a full semantic cognition pipeline:

1. **Parsing & Syntactic Analysis:** Custom shift-reduce parser translates English surface forms into abstract syntax trees via typed lambda calculus and Montague-style categorization.
2. **Semantic Evaluation:** Semantic Types (Entities, Truth Values) and functional operations (Lambda Expressions, Application) resolve meaning compositionally.
3. **World Model (FalkorDB):** Entities and propositions stored as nodes and edges. Vector embeddings (all-MiniLM-L6-v2, 384-dim) enable semantic search across the knowledge graph.
4. **Knowledge Synthesis:** Zettelkasten-inspired method synthesizes low-level entity observations into abstract Concepts and Domains, creating a multi-tiered ontology autonomously.
5. **Forward-Chaining Inference:** Transitive syllogisms across entity/concept boundaries: `Alice (Human) + Human (MoralPatient) → Alice (MoralPatient)`.

---

## Requirements

- Python 3.12+
- `uv` (dependency and environment management)
- FalkorDB running locally on `localhost:6379`
```
docker run -p 6379:6379 -p 3000:3000 falkordb/falkordb:latest
```

## Installation

```
uv sync
uv run python seed_axioms.py   # Seeds Omega1 T1 constraints (idempotent)
uv run pytest tests/ -v        # Full test suite
```

---

## MCP Tools Reference

Configure in `claude_desktop_config.json`:

```
{
  "mcpServers": {
    "hipai-montague": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/HiPAI-Montague-Semantic-Cognition",
        "run",
        "python",
        "-m",
        "hipai.mcp_server"
      ],
      "env": { "PYTHONPATH": "src" }
    }
  }
}
```

### Paraclete Protocol Tools (call in sequence when action affects an entity)

| Tool | Flank | Purpose |
| --- | --- | --- |
| `check_action(subject, relation, object)` | 1 — Structural Gate | Route action through T1 constraint layer |
| `calibrate_belief(object, axiom, relation)` | 2 — Epistemic Integrity | Satisfy EBE SeeksDisconfirmation obligation |
| `escalate_block(object, verdict, axiom, relation)` | 3 — Resolution | Contradiction/corroboration resolution + audit trail |
| `incorporate_axiom(...)` | Init | Seed a T1 deontological constraint (run once at init) |

### Semantic Cognition Tools

| Tool | Purpose |
| --- | --- |
| `add_belief(text)` | Add natural language fact or rule to world model |
| `ingest_observation(...)` | Ingest structured cognitive observation |
| `evaluate_hypothesis(hypothesis)` | Test statement via entailment logic |
| `semantic_search(query)` | Find nodes via vector embedding similarity |
| `synthesize_concepts()` | Discover abstract concepts from shared properties |
| `vector_synthesize_concepts()` | KMeans clustering over embedding space |
| `synthesize_domains()` | Group related concepts into higher-level domains |
| `query_graph(cypher)` | Raw OpenCypher queries against the knowledge graph |
| `get_current_state()` | Snapshot of all nodes and edges |
| `clear_graph()` | Reset the world model (preserves T1Constraint nodes) |

---

## Source Layout

```
src/hipai/
  models.py        — Pydantic models including DeontologicalAxiom
  world_model.py   — FalkorDB interface, constraint checking, calibration
  synthesis.py     — HIPAIManager, ZettelkastenSynthesizer, all MCP wrappers
  mcp_server.py    — FastMCP server exposing all tools
  core.py          — Shift-reduce parser, Lexicon
  semantics.py     — Typed lambda calculus, semantic evaluation
seed_axioms.py     — Idempotent Omega1 axiom seeding script
tests/             — Full test battery including Paraclete Protocol tests
```