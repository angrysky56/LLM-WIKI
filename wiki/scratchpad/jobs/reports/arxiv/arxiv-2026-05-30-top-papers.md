# arxiv — Daily Report 2026-05-30

**Top Papers**: Self-Trained Verification | SpecBench | Physics-Is-All-You-Need

## Cross-Paper Theme: Trustworthy Scientific AI — Infrastructure Layers

Three papers, three infrastructure layers that determine whether AI systems produce trustworthy output:

| Paper | Infrastructure Type | Core Problem |
|-------|---------------------|--------------|
| Self-Trained Verification | Verification as training infrastructure | Training verifiers without human feedback |
| SpecBench | Evaluation infrastructure | Measuring specification-level reasoning |
| Physics-Is-All-You-Need | Supervision as quality infrastructure | Catching what oracle tests miss |

**Design principle**: Trustworthy scientific AI requires infrastructure across all three layers — and infrastructure design (not model scale) is often the primary determinant of quality.

---

## Paper 1 — Self-Trained Verification

**arXiv**: 2605.30290v1 | **Authors**: Chen Henry Wu, Aditi Raghunathan (CMU)

### Key Finding

Diagnosis is easier given a reference. A model cannot find errors in its own output from scratch, but CAN when shown the reference solution. This asymmetry becomes the supervision signal for training verifiers without human-graded feedback.

### Method

1. Reference-conditioned teacher `V★(· | x, y_{r-1}, y★(x))` identifies errors in generated solutions
2. On-policy distillation trains unconditioned student `Vθ(· | x, y_{r-1})` to match teacher's feedback distribution
3. At test time, student runs without references

### Results

| Setting | Task | Improvement |
|---------|------|-------------|
| Test-time refinement | DAPO Hard math (Qwen3-8B zero-shot) | ~2× pass@1 vs untrained verifier |
| Test-time refinement | SciKnowEval (hardest problems) | 1.5% → 21.0% (14×) |
| Training-time (ViL) | After RLVR convergence | +33% relative final-round pass@1 |
| Training-time (ViL) | Standalone pass@1 (no verifier at inference) | +30% past RLVR ceiling |

STV enables Qwen3-8B + STV to outperform the much larger Qwen3-32B generator on hard reasoning — trained verification can substitute for generator scale.

### Connections

- [[self-trained-verification]] — paper page with full details
- [[test-time-scaling]] — STV enables verification to scale test-time compute effectively
- [[reasoning-scaffolding]] — verification-refinement loop as scaffolding mechanism

---

## Paper 2 — SpecBench

**arXiv**: 2605.30314v1 | **Authors**: Grant Hamblin, Kevin Song, Zhanda Zhu et al. (U Toronto, Waterloo, NVIDIA)

### Key Finding

SWE-bench assumes perfect specifications; real-world software requires agents to design specifications. SpecBench evaluates the upstream phase — identifying specification deficiencies in RFC proposals (Kubernetes, React, Rust, TVM, vLLM).

### Deficiency Classes (IEEE Std. 1028-1997)

1. **Omission**: Necessary information missing from proposal
2. **Ambiguous**: Information with more than one interpretation
3. **Inconsistent**: Proposal contradicts itself or existing system
4. **Incorrect**: Information conflicts with preceding documents

### Results

Best agent (GPT-5.4): 44.4% accuracy — significant headroom for improvement on specification-level reasoning.

### Connections

- [[specbench]] — paper page with full details
- [[SWE-bench]] — SpecBench is the upstream complement to SWE-bench
- [[agentic-ai]] — measures agents' ability to handle full software development lifecycle

---

## Paper 3 — Physics Is All You Need?

**arXiv**: 2605.30353v1 | **Author**: Nhat-Minh Nguyen (Kavli IPMU, U Tokyo)

### Key Finding

33 of 57 sessions spent in a fundamentally wrong code architecture that passed oracle tests. The agent treated symptom reduction as equivalent to root-cause resolution. **Supervision protocol — not model capability — was the primary determinant of trustworthiness.**

### What the Agent Resolved Autonomously (10/15 issues)

Convention errors, algorithm transcription, numerical coefficients — all resolved by iterating against oracle test suites.

### What Required Human Intervention (3/15 issues)

- Wrong code architecture (33 sessions, needed physics concept injection to trigger redesign)
- Calibrated scalar correction (passed tests, corresponded to no reference theory quantity)
- Architecture-level failure evading tests

### Supervision Protocol

1. **CLASS-PT as oracle**: Tests written before code — agent knew correct output before attempting
2. **CHANGELOG as shared memory**: Prevented re-exploration of dead ends across sessions
3. **--fast flag for context hygiene**: Verbose diagnostics → log files; keeps context window clean
4. **Parallel agent sessions via git worktrees**: Explored competing hypotheses simultaneously

### Critical Distinction

> "Not whether the code produced right numbers, but whether it produced them for the right reasons."

### Connections

- [[physics-is-all-you-need]] — paper page with full details
- [[ai-coding-agents]] — detailed case study of human-AI collaboration
- [[supervision]] — supervision protocol design as key determinant of output quality

---

## Open Items

- [ ] **STV vs RiM comparison**: Both address reasoning at test time — memory blocks (RiM) vs verifier-refinement (STV). Different mechanisms, complementary insights.
- [ ] **Physics vs LLMSurgeon investigator agent pattern**: Both use static environment ablation to catch failures invisible to standard testing. Compare approaches.
- [ ] **"Predictive adequacy vs explanatory correctness"**: Does wiki have a page on this distinction?
- [ ] **SpecBench vs SWE-bench scope**: Does specification-level evaluation reveal different capability gaps than code-generation benchmarks?

## Wiki Pages Created

- `wiki/sources/papers/self-trained-verification.md`
- `wiki/sources/papers/specbench.md`
- `wiki/sources/papers/physics-is-all-you-need.md`

## PDF Storage

- `/home/ty/Documents/paper-research/arxiv-today/2605.30290v1.pdf`
- `/home/ty/Documents/paper-research/arxiv-today/2605.30353v1.pdf`
- `/home/ty/Documents/paper-research/arxiv-today/2605.30314v1.pdf`

---

*Report generated: 2026-05-30 09:50 UTC*
*Next run: 2026-05-31 08:20 UTC*