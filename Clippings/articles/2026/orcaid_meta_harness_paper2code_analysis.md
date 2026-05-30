# OrCAID + Meta-Harness + Paper2Code-Enhanced: Unified System Analysis

**Date**: 2026-05-24  
**Analyst**: Pathfinder Agent  
**Repos**: `/home/ty/Repositories/ai_workspace/OrCAID`, `/home/ty/Repositories/ai_workspace/meta-harness`, `/home/ty/Repositories/ai_workspace/Paper2Code-Enhanced`

---

## 0. Executive Summary

The three systems are not merely composable — they form a **closed-loop meta-optimization architecture** when integrated correctly. None produces this capability independently.

**The Novel Capability**: "Autonomous Paper Reproduction Engine with Learned Verification Strategy Evolution" — meta-harness evolves Knowledge Pack strategies, OrCAID executes paper-to-code tasks using those evolved packs as context, and the three-bond classifier directs verification strategy selection per failure mode, closing the loop back into the pack.

---

## 1. System Architecture Mapping

### 1.1 OrCAID — Orchestrated Centralized Asynchronous Isolated Delegation

**Role in the unified system**: Multi-agent execution engine with self-healing verification

**Core components**:
- `Manager` — orchestrates scan → plan → delegate → collect → review
- `SubAgentRunner` — spawns isolated git worktrees per engineer
- `Verification Bridge` (`bridge.py`) — hooks at each handoff for scoring/drifts
- `bond_classifier.py` — three-bond deficit classification (deep_reasoning, self_reflection, self_exploration)
- `orchestrator-memory/` — verified/, drift_logs/, escalations/, index/

**Key data flow**:
```
SubAgent completes → _verify_and_return() → bridge.verify_subagent_completion()
  → PASS: write_verified_outcome()
  → FAIL: write_drift_log() + correction_context → retry or escalate
```

### 1.2 Meta-Harness — Knowledge Pack Evolution Framework

**Role in the unified system**: Meta-layer that searches over knowledge artifacts, not just code

**Core components**:
- `EvolutionEngine` — orchestrates Phase 0–3 loop
- `domain_analyzer.py` — Phase 0: emits domain_analysis.json (confusion matrix, failure clusters, ontology gaps)
- `domain_curator` skill — Phase 1: proposes PackDelta entries against named gaps
- `coder_instructions` skill — Phase 2: gated architecture changes
- `HermesWrapper` — bridge to Hermes Agent proposer
- `Knowledge Pack` schema — ontology/, workflows/, rules/, failure_modes/, examples/

**Key data flow**:
```
Phase 0: analysis/domain_analysis.json
Phase 1: curator → PackDelta (distinguisher/failure_mode/example/workflow/rule/concept)
Phase 2: architect → code change (gated, rare)
Phase 3: feedback → failure_mode catalog updates, confidence tuning
```

### 1.3 Paper2Code-Enhanced — PDF-to-Repository Pipeline

**Role in the unified system**: Task-level pipeline (planning → analyzing → coding → debugging → evaluation)

**Core components**:
- `codes/0_pdf_process.py` — PDF ingestion with VLM/local/olmocr modes
- `codes/1_planning.py` + `1_planning_llm.py` — specification generation
- `codes/2_analyzing.py` + `2_analyzing_llm.py` — algorithm extraction
- `codes/3_coding.py` + `3_coding_llm.py` — code generation
- `codes/4_debugging.py` — iterative repair
- `codes/eval.py` — model-based evaluation (o3-mini-high, 8 samples)
- `paper2code-cli/` — Go Cobra CLI + MCP server

**Key data flow**:
```
paper PDF → cleaned JSON → planning artifact → analyzing artifact → coding artifact → debugging → repo → eval
```

---

## 2. Non-Obvious Connections

### Connection 1: Drift Log Schema ↔ Pack Failure Mode Catalog

OrCAID's bridge writes drift_log entries with this structure:
```yaml
task_type: research_reproduction
criterion_id: code_matches_spec
category: criteria_mismatch
missing_bond: self_reflection  # from bond_classifier
```

Meta-harness's `failure_modes/` directory contains entries with fields like:
```yaml
name: repeated_criteria_mismatch
bond_deficit: self_reflection  # ← same label
trigger_count: 3
fixes_attempted: [...]
```

**Insight**: The `missing_bond` field from OrCAID's bond classifier is the primary key for indexing into meta-harness's failure mode catalog. This means OrCAID execution is self-documenting in the exact format meta-harness needs for Phase 1 curation.

### Connection 2: Three-Bond Classifier ↔ Pack Delta Kinds

The bond classifier produces one of three labels, each mapping to a specific pack element:

| Bond Deficit | Pack Element | Meta-Harness Phase |
|---|---|---|
| `deep_reasoning` | `ontology/` (missing concept) | Phase 0 → Phase 1 curator |
| `self_reflection` | `failure_modes/` (repeated failure) | Phase 1 curator → PackDelta |
| `self_exploration` | `examples/` + `rules/` (stuck in basin) | Phase 1 curator → PackDelta |

**Insight**: The bond classifier is a named failure interface between execution and meta-learning. Each deficit type has a distinct fix pathway in the pack, making the selection of correction_context in retry deterministic.

### Connection 3: Paper2Code Artifact JSON ↔ OrCAID Task Context

Paper2Code's planning stage produces `planning_artifacts/` JSON files containing:
- Paper section → code module mapping
- Algorithm specification with hyperparameters
- Data flow diagram
- Evaluation criteria

OrCAID's `scan_and_analyze()` takes a repo + task and produces a task graph. If OrCAID were given the planning artifact as prior context, it could:
1. Skip the scan phase (context already populated)
2. Use the paper-section mapping to assign engineers to paper sections
3. Use the evaluation criteria to configure the verification checklist

**Insight**: The planning artifact is a ready-made task decomposition — the main missing piece is a stage adapter that feeds it into OrCAID's manager.

### Connection 4: Meta-Harness OrCAID Domain ↔ Self-Improve Task

Meta-harness already has an `orcaid` domain under `domains/orcaid/` with:
- `OrcaidEvaluator` class
- `domain_analysis.json` (already run Phase 0)
- `domain_pack.yaml` with 5 task_types

OrCAID has a `SelfImproveTask` (`tasks/self_improve.py`) that refactors OrCAID's own codebase. This is a natural loop: meta-harness runs evolution on the orcaid domain → proposes PackDelta → OrCAID executes self_improve using the evolved pack → results feed back into orchestrator-memory → meta-harness reads them for next iteration.

**Insight**: OrCAID can self-improve using meta-harness as the meta-layer. The orcaid domain's evaluator already reads from `~/.hermes/orchestrator-memory/` — the integration is already wired at the data layer.

### Connection 5: Paper2Code Evaluation ↔ OrCAID Verification Bridge

Paper2Code's `eval.py` uses o3-mini-high to score generated repos (reference-free or reference-based, 8 samples averaged). OrCAID's bridge scores subagent results against YAML checklists. Both are verification systems, but at different granularities:
- Paper2Code eval: single model-based judgment of entire repo
- OrCAID bridge: multi-checklist scoring of per-subagent output

**Insight**: If OrCAID were to use a model-based evaluator like Paper2Code's for paper reproduction tasks (replacing the simple checklist), it would gain semantic alignment scoring. Conversely, Paper2Code's debugging stage could use OrCAID's bond classifier to select repair strategy.

---

## 3. Dual Relationships

### Dual 1: OrCAID as Both Executor and Evaluation Subject

OrCAID is the executor for meta-harness tasks (it runs the actual code changes), but the `orcaid` domain evaluator measures OrCAID's own performance. This creates a self-referential loop that can be bootstrapped:

```
meta-harness → proposes pack deltas
→ OrCAID self_improve task applies them
→ OrCAID bridge writes verified/drift
→ OrcaidEvaluator reads them
→ meta-harness reads scores → next iteration
```

### Dual 2: Paper2Code as Both Task and Evaluator

Paper2Code has its own task type (`paper2code`) in OrCAID, but Paper2Code's evaluation stage could assess OrCAID's generated code for other tasks. This cross-system evaluation is currently not leveraged — Paper2Code only evaluates Paper2Code output.

### Dual 3: Meta-Harness as Both Evolution Driver and Evolution Subject

Meta-harness evolves packs for domains, but the `text_classification` reference example is itself a domain. Meta-harness could, in principle, evolve its own framework prompts (the `domain_curator` skill, `coder_instructions` skill) by treating "meta-harness pack quality" as the fitness metric.

---

## 4. Ruled-Out Paths

### Ruled-Out 1: Direct Stage Coupling (OrCAID → Paper2Code stages)

**Rejected**: Making OrCAID directly call Paper2Code stage scripts as subagents.

**Reason**: OrCAID expects a git repository + task spec. Paper2Code is a pipeline that produces a repository. Forcing OrCAID to treat individual stages as subagents breaks the isolation model and introduces cyclic dependency (Paper2Code repo doesn't exist until the pipeline runs).

**Better path**: Use Paper2Code as a preprocessor — run it first to produce the repo, then OrCAID evaluates/improves it.

### Ruled-Out 2: Meta-Harness Evolving Paper2Code Without OrCAID

**Rejected**: Using meta-harness Phase 1 to evolve Paper2Code stage prompts in isolation.

**Reason**: Without OrCAID's multi-agent verification bridge, there's no mechanism to validate that the evolved prompts actually produce better code. Paper2Code's eval.py provides feedback, but it's a single-model scorer not a self-healing loop with retry and escalation.

**Better path**: Meta-harness evolves the pack (including evaluation strategy), OrCAID executes Paper2Code task with evolved context and bridge verification.

### Ruled-Out 3: Verifier-Graph Alone for Paper→Code Provenance

**Rejected**: Using `verifier-graph` MCP to formalize paper→code provenance without the Knowledge Pack layer.

**Reason**: The graph can represent causal chains (paper section → implementation), but without meta-harness's failure_mode catalog and curation process, there's no mechanism to learn from failures and evolve the provenance model.

**Better path**: verifier-graph projects provenance chains into Synapse; meta-harness reads failure_mode entries to identify which provenance edges are most error-prone; pack curator adds rules for those edges.

### Ruled-Out 4: Tight Integration of Bond Classifier Into Phase 2 Architect

**Rejected**: Calling the bond classifier directly from the Phase 2 coder skill.

**Reason**: The bond classifier is rules-first and deterministic — it's correctly placed in OrCAID's bridge. Phase 2 architect works on named gaps that have resisted ≥3 pack-level fixes, which is a higher-level signal than per-attempt bond deficit.

**Better path**: Bond deficit counts per task_type aggregate into a metric that feeds Phase 0 analysis → gap identification → Phase 1 curation. Not a Phase 2 input.

---

## 5. Unexplored Directions

### Direction 1: Bond-Classifier Gating of Verification Checklist Selection

**What**: OrCAID's bridge uses a fixed checklist per task type (e.g., `checklist_research_reproduction.yaml`). With bond-classifier integration, the checklist could be dynamically selected based on the deficit type:

| Bond Deficit | Verification Strategy |
|---|---|
| `deep_reasoning` | Run ontology consistency check — does output match paper's conceptual structure? |
| `self_reflection` | Re-run same criteria with tighter tolerance — detect if correction_context was applied |
| `self_exploration` | Inject diverse file targeting — does agent explore beyond stuck files? |

**Novelty**: This is a self-adaptive verification system that selects its own debug strategy based on failure classification. None of the three systems does this independently.

**Uniqueness**: Neither Paper2Code (single-agent eval) nor meta-harness (pack-level evaluation) operates at this granularity of per-attempt strategy selection.

### Direction 2: Synapse Query for Workflow-Aware Paper Processing

**What**: Enable a query like "what workflows handle paper X's architecture section?" by projecting Paper2Code's stage outputs into Synapse and wiring the `synapse` section of `domain_pack.yaml`:

```yaml
synapse:
  enabled: true
  database: synapse
  graph_namespace: paper2code
  cypher_path: workflows/_graph.cypher
```

This would allow an agent processing a new paper to query: "what common failure patterns have occurred when implementing attention mechanisms?" — using the pack's failure_modes as graph edges.

**Novelty**: Currently no system connects Paper2Code papers to meta-harness failure modes via a graph query interface.

### Direction 3: Phase 2 Architect for Persistent Bond Deficits

**What**: When a named failure_mode has `trigger_count >= 3` and all PackDelta fixes have failed, meta-harness Phase 2 fires — the `coder_instructions` skill receives a `phase_2_brief.json` and implements one targeted code change. This could be:
- Adding a new bond classifier rule when the deficit doesn't match existing patterns
- Creating a new verification checklist template for a novel failure shape
- Implementing a new self-healing hook in OrCAID's bridge

**Novelty**: This closes the loop between meta-learning (pack evolution) and system architecture (code changes). Currently no system automates architecture changes based on failure mode persistence.

### Direction 4: Multi-Agent OrCAID Optimizing Meta-Harness

**What**: OrCAID's `SelfImproveTask` is designed exactly for this — running OrCAID against its own codebase. The `orcaid` domain in meta-harness already has an evaluator that reads from orchestrator-memory. If meta-harness proposes pack deltas for the orcaid domain, OrCAID could apply them via `self_improve` task, creating a self-hosting evolution loop.

**Novelty**: This is bootstrapping a meta-system that improves itself. Meta-harness evolves the pack; OrCAID applies the changes; the evaluator measures the result; meta-harness reads the result for the next iteration. No human in the loop after initial setup.

### Direction 5: Paper2Code Debugging Stage Uses Bond Classifier

**What**: Paper2Code's `4_debugging.py` runs iterative repair on generated code. Currently it uses a fixed retry strategy. If it called the bond classifier on failure, it could select repair strategy:

| Bond Deficit | Debugging Strategy |
|---|---|
| `deep_reasoning` | Re-analyze paper section — regenerate spec before retrying code |
| `self_reflection` | Apply correction_context from previous attempt — don't repeat same fix |
| `self_exploration` | Target different files/modules — break out of stuck basin |

**Novelty**: This would make Paper2Code's debugging stage self-adaptive, using the same failure classification system as OrCAID's verification bridge.

---

## 6. The Novel Capability (What None Produces Alone)

### "Closed-Loop Paper Reproduction with Self-Evolving Verification Strategy"

**Component Roles**:
1. **Meta-Harness** — Provides the meta-layer: Phase 0 analysis identifies failure patterns; Phase 1 curator proposes PackDelta entries targeting bond deficits; Phase 3 writes back metrics
2. **OrCAID** — Provides the execution layer: multi-agent orchestration, isolated worktrees, self-healing bridge with bond classifier, orchestrator-memory storing verified/drift data in the exact format meta-harness consumes
3. **Paper2Code** — Provides the task layer: PDF→repo pipeline, stage artifacts, evaluation

**The Loop**:
```
1. Meta-harness Phase 0: analyze Paper2Code benchmark
   → domain_analysis.json: self_reflection bond deficit dominates in coding stage
   
2. Meta-harness Phase 1: curator proposes PackDelta
   → Add self-correction workflow to pack's workflows/
   → Add "apply correction_context" rule to rules/
   → Bump pack version to 0.2.0
   
3. OrCAID runs paper2code task with evolved pack as context
   → Manager uses pack's self-correction workflow as delegation strategy
   → Engineers generate code → bridge verifies
   → Bond classifier fires: self_reflection
   → Bridge uses correction_context from pack for retry
   
4. Meta-harness Phase 3: feedback
   → OrcaidEvaluator reads: escalation_rate down, task_completion_rate up
   → Pack's failure_mode for self_reflection: resolved=true
   
5. Next iteration: pack is now version 0.2.1 with learned verification strategy
```

**Why this is novel**: Each system contributes something the others can't replicate alone:
- **Meta-harness** can't execute multi-agent tasks or run verification bridges
- **OrCAID** can't evolve its own pack or learn from failure pattern analysis
- **Paper2Code** can't use self-healing verification or learn from its own failures across runs

**Concrete deliverables this enables**:
1. A Paper2Code system that improves itself across runs (not just per-paper)
2. A verification system that adapts strategy based on failure type
3. A provenance graph that connects paper sections to implementation failure modes
4. A self-hosting meta-system that evolves its own orchestration strategies

---

## 7. Integration Risks and Constraints

1. **Data format alignment**: OrCAID's drift_log YAML frontmatter must match meta-harness's failure_mode entry schema — currently partially aligned (bond_deficit label is shared), but correction_context format is ad-hoc.

2. **Phase 2 architectural changes require careful regression testing** — a code change to OrCAID's bridge could break the evaluator's assumptions about orchestrator-memory format.

3. **Circular dependency risk** in self-improvement loop: meta-harness evolves pack → OrCAID applies → evaluator reads → meta-harness reads. Must ensure base case (pack v0.1.0) is sufficiently capable to not loop forever.

4. **Paper2Code evaluation is single-model** (o3-mini-high per-sample) vs OrCAID's multi-agent bridge — for paper reproduction tasks, bridging these evaluation modalities would require a new checklist that captures model-based scoring criteria.

---

## 8. Immediate Action Items (Pathfinder Recommendations)

| Priority | Action | Rationale |
|---|---|---|
| High | Wire OrCAID's `paper2code` task to use Paper2Code's `planning_artifacts/` as prior context | Skips scan phase, uses paper's structural decomposition directly |
| High | Add `bond_classifier` output to drift_log YAML frontmatter | Enables meta-harness Phase 1 to index by bond deficit directly |
| Medium | Create `checklist_paper_reproduction.yaml` using Paper2Code eval criteria | Gives OrCAID semantic scoring for paper tasks, not just structural |
| Medium | Enable Synapse projection for `paper2code` domain pack | Enables "what workflows handle this paper section?" queries |
| Low | Run Phase 0 on `paper2code` domain using meta-harness analyzer | Kickstarts the evolution loop for paper reproduction |
| Low | Implement Phase 2 brief generator for persistent bond deficits | Closes loop on failures that resist pack-level fixes |

---

*This report was generated by the Pathfinder Agent as part of the Hermes-Ops pathfinder role. It represents a creative mapping of the problem space and should be validated against implementation constraints before execution.*