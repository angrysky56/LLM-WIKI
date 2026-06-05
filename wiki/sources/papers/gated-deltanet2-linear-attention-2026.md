---
summary: Gated DeltaNet-2 (Hatamizadeh/Choi/Kautz, NVIDIA 2026) — decouples erase and write gates in linear attention memory editing. Channel-wise erase gate (key-side) and write gate (value-side) replace the scalar beta tie in Gated DeltaNet/KDA. Best 1.3B results among Mamba-2, GDN, KDA, Mamba-3 on long-context RULER and real-world retrieval. Preserves efficient chunkwise WY training.
tags: [arxiv-2026, linear-attention, recurrent-llm, bounded-self-model, memory-editing, nvidia, paper-2605-22791]
updated: 2026-06-05T14:20:50Z
created: 2026-06-05T14:20:50Z
---

---
created: 2026-06-05T08:00:00Z
updated: 2026-06-05T08:00:00Z
type: source
summary: "Gated DeltaNet-2 (Hatamizadeh/Choi/Kautz, NVIDIA 2026) — decouples erase and write gates in linear attention memory editing. Channel-wise erase gate (key-side) and write gate (value-side) replace the scalar beta tie in Gated DeltaNet/KDA. Best 1.3B results among Mamba-2, GDN, KDA, Mamba-3 on long-context RULER and real-world retrieval. Preserves efficient chunkwise WY training."
tags: [arxiv-2026, linear-attention, recurrent-llm, bounded-self-model, memory-editing, nvidia, paper-2605-22791]
sources: https://arxiv.org/abs/2605.22791
status: active
confidence: 0.9
---

# Gated DeltaNet-2: Decoupling Erase and Write in Linear Attention (Hatamizadeh, Choi, Kautz — NVIDIA, May 2026)

**arXiv:** 2605.22791 | **Code:** https://github.com/NVlabs/GatedDeltaNet-2 | **Affiliation:** NVIDIA

## The Problem

Linear attention replaces the unbounded cache of softmax attention with a fixed-size recurrent state — sequence mixing in linear time, decoding in constant memory. The cost is a compressed key-value memory where many associations compete for the same finite space. Recent improvements (Mamba-2 decay, DeltaNet's delta rule, Gated DeltaNet's combination, KDA's channel-wise decay) have all addressed *which content persists* in this bounded state. Yet every prior delta-rule model shares a single scalar gate (βₜ) that controls *both* how much old content to erase on the key side *and* how much new content to commit on the value side. This scalar tie is the paper's target: erasing and writing act on different axes of the state and should not share a single control.

## The Core Idea / Method

**Gated Delta Rule-2** replaces the scalar βₜ with two independent, channel-wise gates:

- **Erase gate bₜ ∈ [0, 1]ᵈᵏ** — weights key coordinates used to read (and remove) old content from the decayed state
- **Write gate wₜ ∈ [0, 1]ᵈᵛ** — weights value coordinates being committed into the state

The update equation:
```
Sₜ = (I − kₜ(bₜ⊙kₜ)ᵀ) Dₜ Sₜ₋₁ + kₜ(wₜ⊙vₜ)ᵀ
```
where Dₜ = Diag(αₜ) is the channel-wise decay from KDA. This recovers KDA exactly when bₜ = βₜ·1 and wₜ = βₜ·1, and recovers Gated DeltaNet when decay is also scalar-tied.

**Fast-weight view:** The update solves a local online objective that keeps the state close to the decayed memory while applying an associative edit whose residual compares the gated write target against content read from the gated erase direction. The erase gate changes *which* stored associations are read for removal; the write gate changes *which* value channels enter the state. This formalizes an important insight: erasing is a key-side operation (which coordinates of the old read to subtract), while writing is a value-side operation (which coordinates of the new value to commit).

**Chunkwise parallel training** is preserved. The channel-wise decay is absorbed into rank-one erase factors, yielding a compact WY form with the same high-level structure as KDA. The only change: the gates must be present at the accumulation sites during backward (gate-aware backward pass), whereas scalar-gated delta rules could move the factor outside dot products.

**Model families:** Both recurrent-only (Gated DeltaNet-2 token mixers + MLPs) and hybrid (adds sliding-window attention for exact local interactions). Window is fixed, so the hybrid retains linear sequence scaling.

## Results

At 1.3B parameters trained on 100B FineWeb-Edu tokens:

| Metric | Gated DeltaNet-2 | Best competitor | Delta |
|---|---|---|---|
| **Recurrent avg** (10 benchmarks) | **53.11%** | 52.86% (Mamba-3 MIMO) | +0.25 pp |
| **Hybrid avg** | **54.01%** | 53.28% (Mamba-3 SISO) | +0.73 pp |
| **RULER MK-NIAH @4K** (recurrent) | **37.8%** | 26.2% (KDA) | +11.6 pp |
| **RULER MK-NIAH @4K** (hybrid) | **29.2%** | 27.8% (Mamba-3 MIMO) | +1.4 pp |
| **Real-world retrieval avg** (recurrent) | **29.88%** | 28.67% (KDA) | +1.21 pp |
| **Real-world retrieval avg** (hybrid) | **42.28%** | 41.01% (Mamba-3 SISO) | +1.27 pp |

The advantage is most pronounced on multi-key NIAH (where a fixed-size state must separate competing associations) and on noisy real-world retrieval (SWDE, SQuAD, FDA, TriviaQA). Training throughput drops only mildly from KDA (38.0→36.1 Kt/s on H100 at 2K×8) — a modest constant cost for finer memory control.

**Ablations** confirm both gates use their channel degrees of freedom. The erase gate accounts for most of the gain: keeping channel structure only in bₜ recovers most of the full model, while keeping it only in wₜ recovers less.

## Why It Matters

Gated DeltaNet-2 is a direct architectural contribution to the **bounded-self-model thread** — specifically the **allocation axis** (how a bounded recurrent state allocates its finite capacity across competing associations). The paper demonstrates that the scalar βₜ tie was a genuine modeling restriction, not a requirement of the delta rule. Decoupling erase from write produces consistent gains at zero architectural overhead (the gates are cheap token projections), and the gain grows with retrieval complexity.

For practitioners: this is the strongest delta-rule linear attention model as of May 2026, and the first to separately control what gets erased vs. what gets written. The [[continual-learning|efficient training kernels]] (fused Triton, WY form) mean adoption cost is low. The most immediate impact is in long-context and streaming applications where a fixed-size memory must handle interference among many compressed associations.

## Limitations

- **Scale tested only at 1.3B / 100B tokens.** Whether the decoupled gates maintain their advantage at 7B+ scales or with post-training (RLHF, instruction tuning) is open.
- **Throughput overhead, though small, is non-zero.** The gate-aware backward pass adds ~5% training-time cost vs. KDA.
- **Hybrid model still needs SWA for local aggregation.** The recurrent-only model trails hybrid on tasks requiring fine-grained local evidence (DROP, NQ). Gated DeltaNet-2 improves the recurrent frontier but does not eliminate the need for local attention.
- **The write gate contributes less than the erase gate** — ablation shows bₜ carries most of the gain. This asymmetry is underexplored.
- **No analysis of interference patterns at very long contexts** (32K+ tokens). RULER tests go to 8K in the main paper; the advantage at extremely long contexts is inferred but not directly measured.

## Connections to Wiki

### Wiki concepts
- [[bounded-self-model]] — Gated DeltaNet-2 directly addresses the allocation axis: how a bounded recurrent state allocates capacity across competing associations. The erase/write decoupling is a specific mechanism for managing this allocation.
- [[bounded-representation-capacity]] — The fixed-size state is a canonical bounded representation; this paper shows how to use its capacity more efficiently through separate erase/write gates.
- [[linear-attention]] — Direct contribution to the linear/recurrent attention family (Mamba, DeltaNet, Gated DeltaNet, KDA lineage).
- [[markovian-thinker]] — The recurrent state is a Markovian representation; the paper improves the state transition function.
- [[latent-reasoning]] — Delta-rule models perform a form of latent computation in their recurrent state; decoupling erase/write refines this computation.

### Related papers (wiki)
- [[arxiv-2605-30343-reasoning-in-memory-rim]] — RiM also uses fixed memory blocks for latent reasoning. Where RiM adds *more* memory blocks, Gated DeltaNet-2 uses the *same* state size but manages it better through separate gates. Complementary architectural strategies.
- [[sleep-self-modify-consolidate-2026]] — Sleep's parameter consolidation targets a different bound (parametric capacity). Gated DeltaNet-2 targets compute-time memory allocation. Together they cover two distinct resource bounds.
- [[skill-rm-2026]] — Skill-RM addresses orchestration of bounded compute; Gated DeltaNet-2 addresses the underlying memory substrate that compute operates on.
- [[hll-humanitys-last-line-verification-2026]] — HLL's verification problem becomes harder when states are compressed and edits are selective (as in Gated DeltaNet-2), because the verifier cannot inspect the full history.

### Thread Cross-Cuts
The decoupled erase/write gates are structurally analogous to the **erase/write separation in PRISM's intention switching** — both papers independently discover that a single scalar controlling two different operations (erase vs. write, old intention vs. new intention) is a modeling restriction. This suggests a broader pattern: bounded-state models benefit from *functional decomposition* of the state update.

## Key Quote

> "The scalar tie is a modeling restriction because erasing and writing act on different axes of the state. Erasing is a key-side operation that decides which coordinates of the old read should be removed, while writing is a value-side operation that decides which coordinates of the incoming value should be committed."

## What To Watch

- **7B+ scale evaluation** — does the advantage persist or collapse under larger models where the state has more capacity per head?
- **Post-training interaction** — does RLHF or [[continual-learning|continual fine-tuning]] preserve the erase/write separation, or does it collapse back to scalar-like behavior?
- **Application to agent workflows** — agents that maintain a compressed episodic memory could benefit from separate control over what to forget vs. what to record.
- **Security implications** — a model with selective erase/write could more easily hide information in its recurrent state, making monitoring harder.
- **Attention-free architectures** — Gated DeltaNet-2 + SWA hybrids are among the strongest attention-free designs; this line could eventually replace softmax attention in production.
