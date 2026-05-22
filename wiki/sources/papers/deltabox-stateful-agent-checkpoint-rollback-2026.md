---
summary: Dong et al. (2026) — DeltaBox: millisecond-level checkpoint/rollback for stateful AI agents via change-based state management (DeltaFS + DeltaCR); 14ms ckpt, 5ms restore; enables practical MCTS and RL training at scale
tags: [ai-agents, checkpoint-restore, sandbox, overlayfs, CRIU, MCTS, RL-training, copy-on-write, OS-level, state-management]
updated: 2026-05-22T00:00:00Z
created: 2026-05-22T00:00:00Z
sources: https://arxiv.org/abs/2605.22781v1
status: active
confidence: 0.95
---

# DeltaBox: Scaling Stateful AI Agents with Millisecond-Level Sandbox Checkpoint/Rollback

**Authors:** Yunpeng Dong, Jingkai He, Yuze Hou, Dong Du, Zhonghu Xu, Si Yu, Yubin Xia, Haibo Chen (Shanghai Jiao Tong University) + Huawei Technologies
**Source:** [arXiv:2605.22781v1 [cs.OS]](https://arxiv.org/abs/2605.22781v1)
**Published:** May 21, 2026

## Core Contribution

DeltaBox is an OS-level rollbackable sandbox designed for stateful AI agents. It achieves **millisecond-level checkpoint (14 ms) and restore (5 ms)** by abandoning full state duplication in favor of **change-based (delta) checkpointing**. The key insight is that subsequent checkpoints in AI agent workloads are highly similar — only minor incremental changes (a few new files, modified memory pages) occur between steps.

## Problem: The C/R Bottleneck

Modern LLM agents employ tree-structured search strategies (MCTS, LATS) and reinforcement learning that demand **high-frequency checkpoint/rollback (C/R)** of complete sandbox state — both filesystem and process memory. Existing mechanisms are prohibitively slow:

| Approach | Checkpoint Latency | Restore Latency |
|----------|-------------------|----------------|
| E2B (1 GiB RAM) | ~4,000 ms | ~4,000 ms |
| CRIU (multi-GiB) | seconds | seconds |
| Docker commit | seconds | seconds |
| Firecracker VM snapshot | 200 ms – 2 s | 120 – 700 ms |

These latencies **severely bottleneck deep search and large-scale RL fan-outs** because:
1. **Horizontal scaling:** BoN launches N parallel trajectories, each needing a fast initial clone
2. **Vertical depth:** Each trajectory's internal search tree requires fine-grained intermediate C/R

Additionally, **coupling matters** — filesystem-only rollback without memory restore produces stale in-memory context, while memory-only restore without filesystem rollback leaves the agent operating on files from a different search branch.

## Key Insight

> Instead of duplicating the entire state, a sandbox should only duplicate the **changes** (deltas) between consecutive checkpoints.

## Architecture: DeltaState Abstraction

DeltaBox introduces **DeltaState**, a transactional change-based state pair (filesystem + process memory), supported by two co-designed OS mechanisms:

### DeltaFS: Change-Based Filesystem C/R

DeltaFS extends OverlayFS with **runtime hot layer switching**:

- Organizes file states into **layered layers** (upper → middle → lower)
- **Runtime hot layer switching:** Dynamically freezes the current writable layer to preserve historical states and inserts a new writable layer **without unmounting**
- Uses **per-inode generation counters** for lazy file descriptor redirection across checkpoint boundaries
- File updates reduced to **copy-on-write (CoW)** at file level
- Rollback becomes a **simple layer switch** via ioctl

### DeltaCR: Change-Based Process State C/R

DeltaCR couples incremental CRIU dumps with warm-template forking:

- At every checkpoint: performs **incremental CRIU dump** (for durability) + **template-creating fork()** (for low-ms restore)
- Both costs are **hidden inside the LLM I/O window** (concurrent with inference)
- **Bounded template pool** with LRU eviction; evicted templates fall back to CRIU slow path transparently
- **Async-warm thread** runs post-restore, absorbing CoW faults on agent's writable memory regions (e.g., Python heap) off the critical path

## Implementation

- **DeltaFS:** Standalone Linux filesystem extension
- **DeltaCR:** Extension to CRIU
- **DeltaBox:** Agent sandbox built on Firecracker microVM, incorporating both mechanisms

## Results

### Latency (SWE-bench workloads)

| Operation | Fast Path | Slow Path |
|-----------|-----------|-----------|
| Checkpoint | **14.57 ms** | — |
| Restore | **5.14 ms** | 8.04 ms |

Component breakdown (fast path restore):
- DeltaFS layer switch (ioctl): 1.66 ms
- DeltaCR template fork: 3.75 ms
- Async-warm: asynchronous (not blocking agent)

### MCTS Search Performance

On SWE-bench Verified with MCTS search:
- DeltaBox reduces state-management overhead from **47–77%** of trajectory time (coupled-FS baselines) to **3–6%**
- Enables agents to explore substantially more search nodes under fixed time budgets
- **+5.9pp** pass rate improvement over Linear ReAct on Claude Sonnet 4.6
- **+5.2pp** improvement on Qwen3-Coder 30B

### RL Training Performance

- **+29.4pp** pass rate improvement for Llama-3.3 70B (base → RL-trained)
- **+27.6pp** for Qwen2.5 72B
- **+19.2pp** for Qwen3 32B

### Adaptive Optimization

- **Lightweight skip (LW):** Classifier elides checkpoints whose agent action neither mutates process memory nor writes to upper layer. Across 87 MCTS runs (1,689 ckpt events), **62.0% skip ratio** achieved.
- **Write amplification:** XFS reflink + lightweight metadata reduces per-edit copy-up bytes significantly (ext4 coincidence with XFS-without-reflink proves benefit comes from reflink, not XFS)
- **GC effectiveness:** Reachability-aware GC reduces end-of-trajectory dump storage by **46–63%** vs. retaining every checkpoint

### Comparison with Prior Work

| Approach | Ckpt Latency | Restore Latency | FS State | Process State | Arbitrary Rollback |
|----------|-------------|-----------------|----------|---------------|-------------------|
| Git stash/branch | 100 ms – 1 s | 100 ms – 1 s | ✓ | ✗ | ✗ |
| shutil.copytree | 100 ms – 10 s | 100 ms – 10 s | ✓ | ✗ | ✗ |
| Docker commit | 50 ms – 10 s | 1 – 10 s | ✓ | ✗ | ✗ |
| Firecracker snapshot | 200 ms – 2 s | 120 – 700 ms | ✓ | ✓ | ✗ |
| **DeltaBox** | **14.57 ms** | **5.14 ms** | ✓ | ✓ | ✓ |

## Related Work

- **Agent sandboxes:** E2B, Daytona, ZeroBoot, CubeSandbox — primarily optimize isolation/startup, not fine-grained C/R
- **Serverless cold-start:** FaaSnap, Catalyzer, Spice — orthogonal (function invocation vs. rollback point inside long-lived trajectory)
- **Checkpointing:** CRIU, DMTCP, Firecracker, Btrfs/ZFS snapshots — provide building blocks but lack coupled fine-grained rollback for stateful agents

## Connections

- [[MCTS]] — tree search strategy DeltaBox enables at scale
- [[CRI]] — checkpoint/restore in userspace, extended by DeltaCR
- [[overlayfs]] — filesystem layering technology DeltaFS builds upon
- [[Firecracker]] — microVM foundation for DeltaBox sandbox
- [[SWE-bench]] — benchmark used for evaluation
