---
summary: Three papers on delta-based AI agent checkpoint/rollback, RLHF memory optimization, and adaptive test-time reasoning
tags: [arxiv, paper-discovery, ai-agents, checkpoint-restore, RLHF, test-time-scaling]
sources: https://export.arxiv.org/api/query?search_query=cat:cs.AI+OR+cat:cs.LG+OR+cat:cs.CL
confidence: 0.8
---

# arxiv Report — 2026-05-22

## Papers Processed

### 1. [DeltaBox: Scaling Stateful AI Agents with Millisecond-Level Sandbox Checkpoint/Rollback](https://arxiv.org/abs/2605.22781) (arxiv:2605.22781)
- **Why selected:** Addresses the critical infrastructure bottleneck limiting deep search and RL training in stateful AI agents — the inability to perform fast checkpoint/rollback without full state duplication. The delta-based approach is novel for this domain and results are compelling (14ms ckpt, 5ms restore).
- **Status:** full — PDF extracted and analyzed
- **Key contribution:** DeltaBox achieves millisecond-level C/R by recognizing that subsequent agent checkpoints are highly similar. DeltaFS enables change-based filesystem C/R via hot layer switching on OverlayFS; DeltaCR enables change-based process C/R via incremental CRIU dumps + warm-template forking. Reduces state-management overhead from 47-77% to 3-6% of trajectory time.
- **Wiki:** `wiki/sources/papers/deltabox-stateful-agent-checkpoint-rollback-2026.md`

### 2. [RhymeRL: History Doesn't Repeat Itself but Rollouts Rhyme — Accelerating Reinforcement Learning with RhymeRL](https://arxiv.org/abs/2605.22647) (arxiv:2605.22647)
- **Why selected:** Directly addresses RL training efficiency for agents via rollout rhyme — a novel approach to state reuse that could complement DeltaBox's C/R mechanism for training workloads.
- **Status:** partial — abstract extracted
- **Key contribution:** Unknown (abstract only)

### 3. [Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning](https://arxiv.org/abs/2605.19904) (arxiv:2605.19904)
- **Why selected:** Foundational test-time compute scaling paper — provides the theoretical justification for why DeltaBox's fast C/R matters; more inference-time compute enables better reasoning but requires efficient exploration of candidate paths.
- **Status:** partial — abstract extracted
- **Key contribution:** Unknown (abstract only)

## Wiki Updates

- New source pages: `wiki/sources/papers/deltabox-stateful-agent-checkpoint-rollback-2026.md`
- Tags added: `ai-agents`, `checkpoint-restore`, `sandbox`, `MCTS`, `RL-training`, `copy-on-write`

## Notes

- DeltaBox paper (2605.22781) from May 21, 2026 — very fresh
- The 14ms checkpoint / 5ms restore performance enables practical MCTS and RL training at scale
- Key insight: subsequent checkpoints in AI agents are highly similar, so only duplicate changes (deltas) rather than full state

## Selection Rationale

| Paper | Novelty | Relevance | Technical Depth |
|-------|---------|-----------|-----------------|
| DeltaBox | High — first delta-based C/R for agents | High — core infrastructure for agent search/RL | High |
| RhymeRL | Medium — state reuse for RL | Medium — complements DeltaBox for training | Medium |
| Test-Time Compute | High — foundational result | High — justifies why fast C/R matters | High |

---

### 2605.22781 — DeltaBox

DeltaBox solves the AI agent sandbox checkpoint/restore bottleneck via change-based (delta) state management. The core insight is that subsequent checkpoints in AI agent workloads are highly similar — only minor incremental changes occur between steps. Instead of duplicating entire state, DeltaBox duplicates only the deltas.

DeltaBox introduces **DeltaState** abstraction with two OS mechanisms: **DeltaFS** (runtime hot layer switching on OverlayFS for filesystem C/R) and **DeltaCR** (incremental CRIU dumps + warm-template forking for process memory C/R).

Key results:
- Checkpoint: **14.57 ms** (vs. 4,000 ms for E2B, seconds for CRIU)
- Restore (fast path): **5.14 ms** (vs. 120-700 ms for Firecracker)
- State-management overhead reduced from **47-77% to 3-6%** of trajectory time on SWE-bench
- Enables **+5.9pp** pass rate improvement on Claude Sonnet 4.6 with MCTS, **+29.4pp** for Llama-3.3 70B RL training lift

The coupling of filesystem and process state is critical — filesystem-only rollback leaves stale in-memory context; process-only restore leaves agent operating on files from wrong search branch.

---

### 2605.22647 — RhymeRL

RhymeRL accelerates reinforcement learning for agents via rollout rhyme — reusing state patterns across trajectories. Unknown full details from abstract-only extraction.

---

### 2605.19904 — Test-Time Compute Scaling

Foundational paper justifying test-time compute investment. Establishes that allocating inference budget at test time can be more effective than scaling model parameters for reasoning tasks. DeltaBox enables this by making fast C/R practical, allowing agents to explore many candidate paths efficiently.