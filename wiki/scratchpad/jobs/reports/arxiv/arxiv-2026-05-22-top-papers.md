---
summary: 3 papers from 2026-05-21 batch: MOSS (source-level self-evolution), DeltaBox (ms-level C/R), LCGuard (KV sharing privacy)
tags: [arxiv, daily-report]
updated: 2026-05-22T19:00:00Z
created: 2026-05-22T10:00:00Z
---

# arxiv Report — 2026-05-22

## Papers Processed

All three papers from the 2026-05-21 arXiv batch. arXiv HTML list scraping confirmed new batch posted; API metadata + curl PDF download succeeded for all candidates.

|| # | Paper | arXiv ID | Primary Category | Core Finding |
||---|-------|----------|------------------|--------------|
|| 1 | **MOSS: Self-Evolution through Source-Level Rewriting** | 2605.22794 | cs.AI | Source-level self-evolution lifts mean grader score 0.25→0.61 in one cycle without human intervention — only system reaching the harness layer |
|| 2 | **DeltaBox: Stateful Agent Checkpoint/Restore** | 2605.22781 | cs.OS | Delta-based C/R achieves 14ms checkpoint / 5ms restore; reduces state overhead from 47-77% to 3-6% of trajectory time |
|| 3 | **LCGuard: Latent KV Communication Guard** | 2605.22786 | cs.AI | Adversarial-learned KV transformations reduce reconstruction-based leakage 65-75% while maintaining task utility |

## Theme: Agent Infrastructure for Autonomy and Safety

This batch converges on a single theme: **what it takes to make deployed agents actually work in production**. MOSS addresses the adaptation problem (agents stuck after deployment), DeltaBox addresses the search/RL problem (agents can't explore efficiently), and LCGuard addresses the privacy problem (agents leak through latent channels). Together they cover the three orthogonal failure modes of production agentic systems.

## Paper Summaries

### 1. MOSS (2605.22794) — Source-Level Self-Evolution

**Problem:** All prior self-evolving agents (Hermes Agent, SkillClaw, GenericAgent, EvoAgentX) are confined to text-mutable artifacts — prompts, skills, memory schemas, workflow graphs. The **harness layer** (routing, state management, hook ordering, dispatch) is never modified. Failures originating in the harness are unreachable from the text layer.

**Key insight:** Source-level adaptation is strictly more general than text-mutable evolution: Turing-complete, strict superset of all text-mutable scope, deterministic (no base-model compliance dependency), and stable under long-context drift.

**Architecture:** Five components — substrate, `moss evo` CLI, pluggable external coding-agent CLI (Claude Code, Codex, DeepSeek-TUI, OpenCode), host-daemon, ephemeral trial workers. The evolution loop is directed by production-failure evidence batches (auto-scan + manual flagging), runs through a 7-stage pipeline with two review gates, and deploys via user-consent-gated in-place container swap with health-probe rollback.

**Result:** On OpenClaw with DeepSeek V3.2, single evolution cycle lifted four-task mean grader score from **0.25 → 0.61** without human intervention.

**Wiki connections:** [[agentic-research]], [[efhf]], [[self-prompting-via-production-stage-architecture]], [[load-bearing-reasoning]]

### 2. DeltaBox (2605.22781) — Millisecond-Level Checkpoint/Restore

**Problem:** LLM agents require high-frequency checkpoint/rollback for tree search (MCTS) and RL training. Existing mechanisms are prohibitively slow: E2B ~4,000ms, CRIU seconds, Firecracker 200ms-2s checkpoint / 120-700ms restore.

**Key insight:** Subsequent checkpoints in AI agent workloads are highly similar — only minor incremental changes occur between steps. Instead of duplicating entire state, duplicate only the deltas.

**Architecture:** DeltaState abstraction with two OS mechanisms:
- **DeltaFS:** Hot layer switching on OverlayFS — freezes writable layer, inserts new one without unmounting; rollback = simple layer switch via ioctl
- **DeltaCR:** Incremental CRIU dumps + warm-template forking; restore via fork() from frozen template process

**Results:** Checkpoint 14.57ms, restore 5.14ms (fast path). State-management overhead reduced from 47-77% to 3-6% of trajectory time. Enables +5.9pp pass rate improvement on SWE-bench with MCTS, +29.4pp for Llama-3.3 70B RL training.

**Wiki connections:** [[agentic-research]], [[verifier-graph]], [[swe-bench]]

### 3. LCGuard (2605.22786) — Latent KV Communication Guard

**Problem:** Multi-agent LLM systems increasingly use KV caches as a communication substrate (higher bandwidth, richer semantics than text). But KV caches encode contextual inputs, intermediate reasoning states, and attention structure — sensitive information can be reconstructed from shared latent representations even when never disclosed in text. Vanilla KV sharing achieves ASR up to 0.900 on AgentLeak benchmark.

**Key insight:** The threat is operationalized as **reconstruction-based leakage**: shared KV artifact is unsafe if an adversarial decoder can recover agent-specific sensitive inputs from it. This leads to an adversarial training formulation where the adversary learns to reconstruct and LCGuard learns to suppress.

**Architecture:** LCGuard learns representation-level transformations (residual bottleneck: K_san = K + W_K2·GELU(LN(K))) before KV transmission. Two variants: Per-Agent (single link) and Full-System (accounts for compositional leakage across all artifacts).

**Results:** Full-System LCGuard reduces ASR from 0.871 to 0.216 (75% reduction) while maintaining helpfulness 0.71 vs 0.78 baseline. System-level consistently outperforms per-agent — confirming leakage is compositional.

**Wiki connections:** [[multi-agent-llm-systems]], [[kv-cache]], [[privacy-utility-tradeoff]], [[sheaf-consistency-enforcer]]

## Wiki Updates

- New source pages: 3
  - `wiki/sources/papers/moss-self-evolution-source-rewriting-2026.md`
  - `wiki/sources/papers/deltabox-stateful-agent-checkpoint-rollback-2026.md`
  - `wiki/sources/papers/lcguard-kv-communication-guard-2026.md`
- Tags added: `self-evolving-agents`, `source-level`, `checkpoint-restore`, `sandbox`, `MCTS`, `RL-training`, `multi-agent-systems`, `llm-security`, `kv-cache`, `latent-communication`
- Total wiki pages: 308 (up from 305)

## Thematic Threads

### Thread: Production Agent Infrastructure

This batch forms a coherent triplet around the question "what do agents need to actually work in production?":
- **MOSS** → agents must be able to adapt their own code (not just prompts)
- **DeltaBox** → agents must be able to explore efficiently (fast C/R enables deep search)
- **LCGuard** → agents must not leak through latent channels (KV representations are an opaque attack surface)

The three papers are individually strong and collectively more interesting — they address orthogonal but interacting concerns for production agentic systems.

## Related
- [[index]]
- [[scratchpad/jobs/reports/arxiv/arxiv-2026-05-22-top-papers]]

- [[arxiv-2026-05-22-top-papers]]

## Jobs Sheet Update

- **Status**: complete
- **arXiv API**: rate-limited during discovery → switched to HTML list page scraping (always works)
- **PDF download**: all succeeded via curl (200 status each)
- **Next run**: daily at 10:00 UTC
