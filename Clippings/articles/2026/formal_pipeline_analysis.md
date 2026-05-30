# Formal Epistemological Analysis: OrCAID + Meta-Harness + Paper2Code-Enhanced Pipeline

**Date:** May 24, 2026  
**Analyst:** principal-researcher (Hermes subagent)  
**Confidence Level:** Explicit reasoning with sources

---

## 1. Formal Optimization Objectives

### 1.1 OrCAID — Delegation Fidelity Maximization

**What it optimizes:** The fidelity of task delegation from a central Manager to isolated Engineer subagents, measured by verification score against task-specific checklists.

**Formal objective:**

```
max_π  Σᵢ wᵢ · VERDI(tᵢ)

where:
  π      = delegation policy (assignment + verification criteria)
  tᵢ     = task i from the task graph
  wᵢ     = task weight (complexity/property count)
  VERDI  = verification score function: [0, 1] → {pass, fail, escalate}
```

**State space:** `(task_graph, worktree_states, verification_scores, drift_logs)`

**Key invariants enforced:**
- `worktree_isolation`: each engineer operates on isolated git branch
- `git_commit_required`: uncommitted work is not collected
- `delegation_coherence`: no overlapping file assignments across subagents

**Failure modes classified by `bond_classifier.py`:**
| Bond Type | Description | Detection |
|-----------|-------------|----------|
| `phase_skip` | Subagent skipped a required pipeline phase | Checklist criterion missing |
| `criteria_mismatch` | Output doesn't match assigned criteria | Verification score < threshold |
| `delegation_break` | Manager→subagent communication failure | Drift log shows intent gap |

**Confidence in optimization target:** 0.83  
*Reasoning:* Bond classifier adds stability (0.83 with rule-based; 0.71 with LLM variant). Self-healing loop ensures monotone non-decreasing verification scores, guaranteeing convergence to fixed point in ≤ max_retries × O(T) iterations.

---

### 1.2 Meta-Harness — Knowledge Pack Fitness Maximization

**What it optimizes:** Expected benchmark performance via incremental, falsifiable changes to a domain Knowledge Pack.

**Formal objective:**

```
max_Pack  E[benchmark_score(Pack) | gap_coverage(Pack, G)]
subject to:  ∀delta ∈ D:
               isFalsifiable(delta) ∧ groundedIn(domain_analysis, delta)
```

**State space:** `(Pack_version, gap_coverage_vector, fitness_score, delta_history)`

**Knowledge Pack structure K = (O, W, R, F, E):**

```
O = {concepts, relations, distinguishers}  -- vocabulary layer
W = {workflow_graphs}                       -- executable task decompositions
R = {invariants, heuristics}               -- hard constraints + confidence-weighted rules
F = {failure_mode_catalog}                  -- named failure modes with detection rules
E = {canonical_examples, edge_cases}       -- grounding examples
```

**Phase gating:**
- **Phase 1 (curator):** Default. Proposes Pack deltas — edits to K files.
- **Phase 2 (architect):** Gated. Fires only when:
  - Same gap targeted by ≥3 consecutive Pack deltas without improvement
  - Failure mode has `open` status with ≥1 attempted fix
  - Gap persists below noise floor of metric

**"Domain building" formally means:** Constructing K to maximize `gap_coverage(G, K)` where:

```
gap_coverage(G, K) = Σⱼ coverage(gⱼ, K) / |G|

coverage(g, K) = 1  iff  ∃ e ∈ O∪W∪R∪F∪E : addresses(g) ∧ eval_shows_improvement(g)
```

Domain building starts at K₀ = ∅ and aims for K* where `gap_coverage(G, K*) = 1.0`

**Confidence in optimization target:** 0.76  
*Reasoning:* Curator constraint (groundedness in domain_analysis.json) prevents unconstrained drift. However, the curator may fail to recognize when a gap requires Phase 2 escalation, leading to stagnation. Beta posterior updates for heuristic confidence provide honest uncertainty quantification.

---

### 1.3 Paper2Code-Enhanced — Code Reproduction Fidelity

**What it optimizes:** Semantic alignment between paper's described pipeline and generated repository.

**Formal objective:**

```
max_r  E[fidelity(paper, repo(r))]

fidelity(paper, repo) =
  w₁ · ExecFaithfulness(paper, repo)      -- same outputs, same inputs
+ w₂ · SemanticAlignment(paper, repo)     -- algorithm matches math spec
+ w₃ · StructuralCompleteness(paper, repo) -- all components present
```

**Pipeline stages:**

```
Paper → [Planning] → [Analyzing] → [Coding] → [Debugging] → Repo
         ↓               ↓             ↓
      constraint       architecture   implementation
      extraction       inference       synthesis
```

**Evaluation:** Reference-free (Pass@k, compilation rate) + reference-based (behavioral equivalence)

**Confidence in optimization target:** 0.78  
*Reasoning:* Three-stage decomposition is sound but the semantic gap between natural language description and formal mathematical specification is non-computable. No guarantee generated code implements the paper's actual algorithm — only that it matches the paper's prose description.

---

## 2. Domain Building: Formal Definition

**Definition:** Domain building is the iterative process of constructing a Knowledge Pack K for a domain D such that `gap_coverage(G_D, K) → 1.0` where G_D is the gap vector from Phase 0 analysis.

**Formal properties of domain building:**

1. **Groundedness:** Every element added to K must be traceable to a specific gap in G_D.
2. **Falsifiability:** Every delta has a measurable expected impact on a specific metric.
3. **Incrementality:** K evolves through small deltas, not sweeping rewrites.
4. **Closure:** When coverage reaches 1.0, domain is "complete" (no open gaps in the analysis).

**Measure of domain maturity:**

```
maturity(K, D) = Σᵢ alphaᵢ · coverage(gᵢ, K)

where alphaᵢ = importance_weight(gᵢ) from domain_analysis.json
      and coverage is binary (addressed or not)
```

**The integration role of domain building:** Meta-harness's evolved Pack provides OrCAID with better task decomposition prompts, making the delegation→verification loop more effective. OrCAID's delegation failures become failure_mode entries in F, closing the loop.

---

## 3. Complexity Profile

### 3.1 Per-System Complexity

| System | Time Complexity | Space Complexity | Convergence |
|--------|-----------------|------------------|-------------|
| Paper2Code-Enhanced | O(P² + A·M + C·N) | O(P + A + C) | Not guaranteed |
| OrCAID | O(E × Σᵢ\|criteria_i\| × retries) | O(E × T + E × W) | Guaranteed (bounded) |
| Meta-harness | O(\|K\| × \|G\| × iterations) | O(\|K\|) | Guaranteed (if gaps falsifiable) |

*Legend: P=paper tokens, A=analysis depth, M=model calls, C=coding artifacts, N=retry budget, E=engineers, T=task graph nodes, W=workspace size, K=Knowledge Pack size, G=gap count*

### 3.2 Pipeline Integration Complexity

**Information flow:**
```
Paper2Code-Enhanced → OrCAID → meta-harness → (feedback) → OrCAID
                                  ↑
                          failure_modes ← OrCAID drift logs
```

**Cross-system coupling:**

```
Coupling(P2C, OrCAID) = semantic_distance(architecture, task_requirements)
Coupling(OrCAID, MH) = drift_log → failure_mode_entry conversion rate
Coupling(MH, OrCAID) = Pack.workflow(task.type) → delegation_validity
```

**Bottleneck identification:**

The semantic gap between Paper2Code's generated architecture and OrCAID's expected task structure is the primary bottleneck. This gap is non-computable — cannot be formally bounded.

### 3.3 End-to-End Complexity Bound

```
T_total ≤ T_P2C + T_OrCAID + T_MH + T_feedback

Worst-case: Paper2Code enters infinite debugging loop
           OR OrCAID exceeds max_retries on same task
           OR Meta-harness curator stagnates (ungrounded deltas)

Best-case: Converges in O(|G|) meta-harness iterations for Pack-level changes
```

---

## 4. Mathematical Framework Summary

### 4.1 OrCAID

```
State: (T, W, V) where T=task_graph, W={worktree_i}, V={verification_scores}
Action: assign(task_i, engineer_j) → checklist_k
Reward: VERDI(task_i)  [0, 1] normalized
Policy: π : (task_requirements, subagent_state) → (assignment, check_criteria)

Invariant constraints:
  - worktree_isolation: W_i ∩ W_j = ∅ for i ≠ j
  - delegation_coherence: files(task_i) ∩ files(task_j) = ∅ if concurrent
  - git_commit_required: output must be committed before collection
```

### 4.2 Meta-Harness

```
State: (Pack_v, G, F) where Pack_v=current version, G=remaining gaps, F=failure_modes
Action: propose_delta(gap, Pack_v) → Pack_{v+1}
Reward: Δfitness(Pack_{v+1}) - Δfitness(Pack_v)  [measurable]
Policy: curator : (domain_analysis, Pack_v) → {delta_1, ..., delta_n}

Phase 2 gating condition:
  phase_2_fired(g) ⇔ (consecutive_attempts(g) ≥ 3) 
                    ∧ (metric_movement(g) < noise_floor)
                    ∧ (failure_mode_catalog[g].status = open)
```

### 4.3 Paper2Code-Enhanced

```
State: (P, A, C) where P=paper, A=analysis_graph, C=code_artifacts
Action: generate_stage(stage_i, context) → artifact_i
Reward: fidelity(paper, generated_repo)  [0, 1]
Pipeline: Planning → Analyzing → Coding → Debugging

Faithfulness decomposition:
  E = ExecFaithfulness  (behavioral equivalence on test inputs)
  S = SemanticAlignment (algorithm matches mathematical specification)  
  C = StructuralCompleteness (all paper components implemented)

fidelity = w₁·E + w₂·S + w₃·C  where Σwᵢ = 1
```

---

## 5. Falsification Protocol

### 5.1 Conditions That Prove Pipeline Failure

**F1 — Propagation Failure:**
```
∀paper ∈ benchmark_set:
  Paper2Code(paper).fidelity < threshold
  AND
  meta-harness.domain_pack.failure_modes ⊄ {"low_fidelity_generation"}

→ Consequence: Meta-harness fails to identify the failure mode;
   OrCAID continues delegating to structurally broken code.
   System propagates errors rather than containing them.
```

**F2 — Verification Failure Loop:**
```
∃task ∈ delegated_tasks:
  verification_bridge(task).score < acceptance_threshold
  AND retry_count(task) < max_retries
  AND drift_category(task) = phase_skip

→ Consequence: OrCAID enters infinite retry loop on same failure mode.
   Bond classifier identifies as delegation_break but curator doesn't
   receive signal to create Phase 2 brief.
```

**F3 — Domain Building Stagnation:**
```
∃domain ∈ domains:
  gap_coverage(Pack, analysis.gaps) < 0.5 after 10 iterations
  AND curator keeps proposing ungrounded deltas

→ Consequence: Meta-harness curator is not reading domain_analysis.json
   correctly or gaps are not falsifiable in the knowledge layer.
```

**F4 — Integration Semantic Gap:**
```
semantic_distance(Paper2Code.architecture, OrCAID.task_requirements) > τ
AND meta-harness cannot construct a distinguisher to reduce this distance

→ Consequence: Generated code fundamentally doesn't match what OrCAID
   expects to verify. The workflow graph produced by the Pack cannot
   guide delegation to produce valid Paper2Code inputs.
```

### 5.2 Negative Result Criteria

A **definitive falsification** occurs when:

```
∀π ∈ Π (all possible pipeline configurations):
  E[fidelity(π)] < baseline

where baseline = performance of reference implementation (human-coded)
```

This requires running the full benchmark suite and showing all configurations underperform. This is computationally expensive but theoretically sound.

### 5.3 falsification_checklist

```
[ ] Run benchmark_set through Paper2Code → measure fidelity distribution
[ ] Check meta-harness Pack for low_fidelity_generation failure_mode entry
[ ] Verify OrCAID verification_bridge scores are consistent (not flipping)
[ ] Confirm gap_coverage(Pack) > 0.5 after 10 iterations
[ ] Test semantic_distance(P2C_architecture, OrCAID_tasks) < τ

If ANY check fails:
  - F1: Add failure_mode entry to Pack; re-run evaluation
  - F2: Check bond_classifier threshold; verify drift_category assignment
  - F3: Audit curator deltas for grounding in domain_analysis.json
  - F4: This is the fundamental bottleneck — consider human-in-the-loop
```

---

## 6. Preconditions for Success

| Precondition | Formal Statement | Confidence |
|--------------|------------------|------------|
| **PC1: Semantic Extractability** | ∀paper ∈ benchmark: ∃ extraction_fn such that extraction_fn(paper) → formal_spec sufficient for code synthesis | 0.78 |
| **PC2: Delegation Determinism** | ∀result, ∀run: verification(result, checklist) yields consistent_score (within tolerance) | 0.83 |
| **PC3: Domain Falsifiability** | ∀gap ∈ gaps: ∃delta ∈ D such that Δfitness(delta, gap) is measurable by evaluator | 0.76 |
| **PC4: Integration Semantic Coherence** | ∀task ∈ delegated: Pack.workflow(task.type) produces valid input for Paper2Code.eval() | 0.69 |

**Overall pipeline confidence:**

```
P(success) ≈ min(PC1, PC2, PC3, PC4) × consistency_factor × benchmark_representativeness
         ≈ 0.69 × 0.85 × 0.80
         ≈ 0.47
```

**Interpretation:** The integrated pipeline has LOW overall confidence (~0.47) due to the semantic gap bottleneck (PC4). Individual components are more reliable (0.76–0.83). The integration amplifies failure modes rather than averaging them.

---

## 7. Key Findings Summary

### What Each System Optimizes

| System | Optimization Target | Formal Measure |
|--------|---------------------|----------------|
| **OrCAID** | Delegation fidelity | Σ wᵢ · VERDI(tᵢ) against checklists |
| **Meta-Harness** | Knowledge Pack fitness | E[benchmark_score \| gap_coverage] |
| **Paper2Code-Enhanced** | Code reproduction fidelity | w₁·ExecFaithfulness + w₂·SemanticAlignment + w₃·Structural |

### What "Domain Building" Means Formally

Domain building is the construction of a Knowledge Pack K = (O, W, R, F, E) that maximizes `gap_coverage(G, K)` — the fraction of identified domain gaps that have a Pack element addressing them and showing metric improvement. K evolves through falsifiable, grounded, incremental deltas.

### Falsification Conditions

1. **F1:** Paper2Code produces low-fidelity output AND meta-harness Pack lacks corresponding failure_mode entry
2. **F2:** OrCAID verification scores below threshold AND retry count exhausted AND drift is unclassified
3. **F3:** Meta-harness Pack below 50% gap coverage after 10 iterations
4. **F4:** Semantic distance between Paper2Code output and OrCAID task requirements exceeds threshold AND no distinguisher can reduce it

### Confidence by Component

```
OrCAID (standalone):     0.83 — self-healing loop, consistent verification
Meta-harness (standalone): 0.76 — falsifiable deltas, grounded curation  
Paper2Code-Enhanced:     0.78 — three-stage pipeline, semantic alignment gap
Integrated Pipeline:     0.47 — semantic gap is the fundamental bottleneck
```

---

## 8. Recommendations

1. **Address the semantic gap first.** PC4 = 0.69 is the binding constraint. Consider adding a validation layer between Paper2Code and OrCAID that checks semantic alignment before delegation.

2. **Instrument F1 propagation.** If Paper2Code produces low-fidelity output, the failure should immediately create a failure_mode entry in meta-harness Pack. Currently this requires manual intervention.

3. **Monitor F2 early.** OrCAID's bond classifier should emit escalation signals to meta-harness's Phase 2 gating mechanism when retry_count exceeds threshold with no improvement.

4. **Bound worst-case runtime.** Paper2Code's non-convergence is the primary time-complexity risk. Add a stage-timeout that triggers manual review rather than infinite debugging loops.

5. **Consider narrowing scope.** The pipeline is more reliable for domains where PC1 (semantic extractability) is high. Restricting to well-specified algorithmic papers would raise overall confidence.

---

*Analysis produced by principal-researcher subagent. Sources: OrCAID/AGENTS.md, OrCAID/orcaid/bridge.py, meta-harness/ARCHITECTURE.md, meta-harness/src/meta_harness/engine.py, meta-harness/src/meta_harness/skills/domain_curator/SKILL.md, Paper2Code-Enhanced/README.md, Paper2Code-Enhanced/codes/pipeline.py.*