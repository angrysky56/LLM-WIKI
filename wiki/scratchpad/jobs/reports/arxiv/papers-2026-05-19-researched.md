---
summary: Three papers on production LLM agent architecture, VLM reasoning decoupling, and agentic clinical evidence seeking
tags: [arxiv, paper-discovery, llm-agents, vlm, clinical-ai]
sources: https://export.arxiv.org/api/query?search_query=cat:cs.AI+OR+cat:cs.LG+OR+cat:cs.CL
confidence: 0.8
---

# arxiv Report — 2026-05-20

## Papers Processed

### 1. **[A Methodology for Selecting and Composing Runtime Architecture Patterns for Production LLM Agents](https://arxiv.org/abs/2605.20173)** (arxiv:2605.20173)
- **Why selected:** Directly addresses the gap between stochastic LLMs and deterministic production software — a core unsolved problem in our wiki's agent-architecture research thread. The "runtime architecture pattern" framing is novel and practically important.
- **Status:** partial — SS citation data unavailable (rate limit); abstract and metadata captured
- **Key contribution:** Formal methodology for composing production LLM agent architectures, treating the LLM/software boundary as a first-class design concern

### 2. **[From Seeing to Thinking: Decoupling Perception and Reasoning Improves Post-Training of Vision-Language Models](https://arxiv.org/abs/2605.20177)** (arxiv:2605.20177)
- **Why selected:** Challenges the prevailing assumption that long chain-of-thought reasoning helps VLMs on visual tasks — finding that decoupling perception from reasoning during post-training actually improves performance. Important negative result for our VLM research.
- **Status:** partial — SS citation data unavailable (rate limit); abstract and metadata captured
- **Key contribution:** Demonstrates that visual task performance is actually *harmed* by reasoning-heavy CoT during VLM post-training; proposes decoupling as the fix

### 3. **[ClinSeekAgent: Automating Multimodal Evidence Seeking for Agentic Clinical Reasoning](https://arxiv.org/abs/2605.20176)** (arxiv:2605.20176)
- **Why selected:** Extends agentic reasoning into a high-stakes multimodal domain (clinical). The evidence-seeking framing is relevant to our broader agent-tool-use research and has practical impact.
- **Status:** partial — SS citation data unavailable (rate limit); abstract and metadata captured
- **Key contribution:** Multi-modal evidence seeking pipeline for clinical decision support; addresses the problem that existing agentic clinical systems assume evidence is already available (it rarely is)

## Wiki Updates

- New source pages: `wiki/sources/papers/production-llm-agent-runtime-architecture-patterns.md`
- New source pages: `wiki/sources/papers/decoupling-perception-reasoning-vlm-post-training.md`
- New source pages: `wiki/sources/papers/clinseekagent-multimodal-clinical-evidence-seeking.md`
- Updated pages: `wiki/concepts/llm-agent-architecture.md` (cross-reference new patterns)
- Tags added: `llm-agents`, `vlm`, `clinical-ai`, `agentic-reasoning`, `post-training`

## Notes

- arXiv returned 429 on secondary fetches — worked with data from the initial discovery query
- Semantic Scholar returned no data for all queried IDs (likely the same rate-limiting window)
- All three papers are from 2026-05-19 — very fresh batch
- arXiv rate limit event logged: initial search succeeded; secondary fetches hit 429 after ~15s gap

## Related
- [[wiki/index]]
- [[scratchpad/jobs/reports/arxiv/papers-2026-05-19-researched]]

- [[papers-2026-05-19-researched]]

## Selection Rationale

| Paper | Novelty | Relevance | Technical Depth |
|-------|---------|-----------|-----------------|
| Production LLM Agent Architecture | High — first formal methodology for this problem | High — connects to our agent-architecture research | High |
| Decoupling VLM Perception/Reasoning | High — challenges prevailing assumption | Medium-High — VLM is active research thread | High |
| ClinSeekAgent | Medium — extends existing agentic clinical work | Medium — domain-specific but methodologically interesting | Medium |

All three papers represent meaningful contributions to active wiki research threads (agent-architecture, VLM post-training, clinical AI agents).

---

### 2605.18703 — EnvFactory

EnvFactory solves the tool-use agent environment bottleneck via a fully automated three-tier pipeline — a Search Agent discovers authentic APIs and MCP schemas, a Code Agent implements stateful executable tool environments with Pydantic validation, and a Test Agent verifies functional correctness before deployment — producing 85 verified environments (842 tools across 7 domains) that generate 2,575 SFT and RL trajectories. The key innovation is topology-aware sampling: recursive backward resolution of tool dependencies before inclusion, which guarantees all required inputs are satisfied at each step (credit assignment resolves at environment-construction time rather than trajectory-collection time). Achieves +15% on BFCLv3, +8.6% on MCP-Atlas, and +6% on conversational benchmarks (τ²-Bench, VitaBench) using 5× fewer environments than prior work, directly addressing the environment scarcity and over-specified trajectory problems in agentic RL. The three-tier agent architecture maps cleanly to EFHF layers (Search=L0 ideation, Code=L2 execution, Test=L3 verification), and the calibrated refinement process (sampling natural human intents rather than instruction sequences) is a direct response to the distributional collapse problem in synthetic trajectory generation — making EnvFactory a concrete solution to the credit assignment bottleneck that also validates the L1→L2 verification chain in our architecture.

---

### 2605.18299 — SD-Search

SD-Search solves step-level credit assignment in search-augmented reasoning via on-policy hindsight self-distillation — a single model plays student (standard inference-time context) and teacher (additionally conditioned on a hindsight block aggregating sibling rollouts' search spans and CORRECT/INCORRECT outcome labels). The teacher distribution implicitly marks which queries were worth making; the student is aligned via token-level Jensen-Shannon divergence at search-query positions. No external teacher or annotations required beyond standard QA pairs. At 3B, SD-Search reaches 0.428 avg EM, matching Thinker (which requires a 72B external teacher); at 7B, it reaches 0.476, surpassing all outcome-reward and process-supervision baselines. Key insight: the policy itself, given hindsight about which rollouts succeeded, can recover step-level signal that external methods import from larger models.

---

### 2605.18077 — LMAC

LMAC (LLM-Driven Multi-Agent Communication) uses an LLM as an offline protocol designer for cooperative MARL — the key insight being that an LLM's pretrained world model can infer which observation dimensions correlate with which global state variables, and which agents have access to what information, enabling it to propose minimal sufficient communication schemas without online LLM interaction at execution. The protocol is iteratively refined via a two-step criterion: (1) recovery enhancement — improving per-dimension state reconstruction accuracy using an auxiliary decoder trained on offline transition data — and (2) imbalance mitigation — reducing inter-agent variance in reconstruction quality to ensure uniform state awareness. The refined protocol is integrated into CTDE training via a meta-cognitive encoder-decoder with cycle-consistency regularization, where the encoder learns to produce compact latent representations that encode only reconstructable, task-relevant features. LMAC achieves new SOTA on SMAC-Comm, SMACv2 (even surpassing QMIX+State under high stochasticity), LBF, and Google Research Football. The state-awareness indicator (SAI) is structurally identical to a discrete sheaf-consistency criterion: when one agent can reconstruct a state dimension but another cannot, that is a local inconsistency requiring a "patch" in the communication protocol — making LMAC the concrete operationalization of what sheaf-consistency enforcement does at the protocol level.