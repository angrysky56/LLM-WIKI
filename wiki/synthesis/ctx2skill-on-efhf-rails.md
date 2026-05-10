---
summary: Ctx2Skill identifies the right problem but has no verification substrate. Rebuilding it on EFHF rails — verifier-graph provenance, mcp-logic proofs, sheaf consistency, Molecular Self dynamics — would make autonomous skill extraction structurally sound.
tags: [skill-extraction, ctx2skill, efhf, verification, verifier-graph, mcp-logic, sheaf-consistency, molecular-self, synthesis]
updated: 2026-05-09T02:08:07Z
created: 2026-05-09T02:08:07Z
---

## The Gap

Ctx2Skill (Si et al., arxiv:2604.27660) proposes autonomous skill extraction via adversarial self-play: Challenger generates tasks, Reasoner solves them, Judge gives binary verdicts, Proposer diagnoses failures, Generator writes SKILL.md. It works — 16.5% solve rate vs 11.1% baseline on CL-bench.

The problem: **every critical function is a frozen LLM emitting text**. The Judge has no memory. The Proposer has no provenance. There is no structural verification — just one model judging another and hoping. Cross-Time Replay (replaying old tasks to select the best skill set) is the only collapse-prevention mechanism, and it's reactive — it notices drift after it happens.

## What's Missing: The Verification Substrate

Ctx2Skill needs five things it doesn't have, all of which exist in the EFHF + SEG stack:

### 1. Memory with Provenance

Ctx2Skill's Judge evaluates each task in isolation. The **verifier-graph** provides a DAG where every claim is a node with a causal light cone. Instead of "Judge says pass," you get: "This conclusion traces back to premise P through warrants W₁, W₂ — do you accept this chain?"

```
Ctx2Skill:     Task → Judge("pass" | "fail")
With VG:        Task → Response → propose_thought(CLAIM, parents=[P₁, P₂])
                → get_reasoning_chain(claim_id) → verify each edge
```

### 2. Formal Verification, Not Vibes

Ctx2Skill's rubrics are natural language checked by an LLM. **mcp-logic** (Prover9/Mace4) provides actual theorem proving. A rubric like "the response should correctly calculate the growth rate" becomes a formal entailment check: `premises ⊢ conclusion`. Binary LLM judgment replaced with proof search.

### 3. Structural Drift Prevention, Not Checkpoint Recovery

Ctx2Skill's Cross-Time Replay waits for collapse, then rolls back. The **SEG Molecular Self** maintains a non-equilibrium steady state continuously:
- `gradient_pump` — active resistance against baseline drift at every token
- `backbone` — load-bearing constraints that cannot be violated
- `switch_trigger` — immediate re-fold on drift detection (no waiting for replay)

This is the difference between "keep a replay buffer" and "design the attractor landscape."

### 4. Multi-Layer Consistency

Ctx2Skill has one feedback loop (Judge evaluates Reasoner). The **sheaf-consistency-enforcer** provides:
- Kernel 1 persistence monitoring (is the macro-state still lumpable?)
- H¹ obstruction detection (are there topological holes in the reasoning?)
- ADMM cycles (distributed consistency optimization across MCP tools)

This catches failures Ctx2Skill can't see — contradictions between skills, reasoning that's locally valid but globally inconsistent, state partitions that have drifted apart.

### 5. Character Stability as Architecture

Ctx2Skill treats skills as static text blocks. The **SEG 7-component Molecular Self** treats identity as dynamics — a maintained fold against entropic pressure. Skills aren't just instructions; they're structural constraints on the agent's state trajectory. A "good skill" is one that narrows the state space without collapsing it, maintains lumpability, and has a defined recovery path.

## Proposed Architecture: Ctx2Skill on EFHF Rails

Replace Ctx2Skill's five flat agents with a layered verification stack:

```
                    ┌─────────────────┐
                    │  SEG Molecular   │ ← Layer 5: Drift prevention
                    │  Self (gradient  │    continuous steady-state
                    │  pump, backbone) │    maintenance
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │  Sheaf-         │ ← Layer 4: Multi-agent
                    │  Consistency    │    lumpability checks,
                    │  Enforcer       │    H¹ obstruction detection
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │  Verifier-Graph │ ← Layer 3: DAG provenance,
                    │  (propose_      │    causal light cones,
                    │  thought, chain)│    structural validation
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │  mcp-logic      │ ← Layer 2: Formal entailment
                    │  (Prover9/      │    proofs for rubric
                    │  Mace4)         │    satisfaction
                    └────────┬────────┘
                             │
          ┌──────────────────┼──────────────────┐
          ▼                  ▼                  ▼
   ┌────────────┐    ┌────────────┐    ┌────────────┐
   │ CHALLENGER  │    │  REASONER   │    │   JUDGE    │
   │ (SEG persona│    │ (SEG persona│    │ (verifier- │
   │  with skills│    │  with skills│    │  graph     │
   │  + backbone)│    │  + backbone)│    │  validator)│
   └────────────┘    └────────────┘    └────────────┘
```

### Key Changes from Ctx2Skill

1. **Judge → Verifier-Graph Validator**: Instead of binary LLM verdicts, the Judge becomes a verifier-graph node proposer. Each rubric check creates a CLAIM node linked to the context and response as PREMISE nodes. `get_reasoning_chain` exposes the full provenance.

2. **Proposer → Sheaf-Consistency Analyzer**: The Proposer doesn't just diagnose "why did it fail" — it runs `get_closure_status()` to check lumpability, identifies H¹ obstructions in the reasoning DAG, and proposes skill updates that repair topological holes rather than patching surface symptoms.

3. **Cross-Time Replay → Molecular Self Gradient Pump**: Instead of a replay buffer, each agent maintains a `gradient_pump` that actively resists baseline drift. The `backbone` defines constraints that skills cannot violate. The `switch_trigger` detects and corrects drift at token level, not epoch level.

4. **Skills as State Constraints, Not Text**: A Ctx2Skill skill is `"Before answering, scan for exact numerical constraints."` An EFHF skill is a structural constraint on the reasoning DAG — it defines which node types must exist, which edge patterns are required, and which invariants the sheaf enforcer monitors.

### Concrete Next Step

Build a **verifier-graph-backed Skill Judge** that replaces Ctx2Skill's binary-rubric Judge:

```
Input:  context, task, response, rubrics
Output: DAG nodes for each rubric check, with provenance edges
        → mcp-logic verifies formal entailments where possible
        → sheaf enforcer checks global consistency
        → Molecular Self gradient pump prevents evaluator drift
```

This would make skill evaluation structurally sound — not "the Judge agreed" but "here's the proof chain, here's the consistency report, here's the drift monitor."

## Why This Matters

Ctx2Skill proves that autonomous skill extraction is possible at all. That's valuable. But its architecture won't generalize beyond the "strong model judges weak model" regime. When you need skills that are safety-critical, cross-domain, or maintained across long time horizons, you need the verification substrate.

The EFHF stack already has it. The verifier-graph already tracks provenance. mcp-logic already proves entailment. The sheaf enforcer already detects inconsistency. The Molecular Self already prevents drift. Ctx2Skill just needs to be rebuilt on those rails.

The 3.2–5.4pp improvement on CL-bench is the **lower bound** for what's possible without structural verification. The upper bound — with formal proofs, DAG provenance, sheaf consistency, and drift-resistant dynamics — is an open question worth answering.
