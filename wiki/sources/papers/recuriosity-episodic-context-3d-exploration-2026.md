---
summary: Wiki source page for Recuriosity (2605.22814v1) — curiosity-driven 3D exploration with persistent 3DGS world model and episodic RGB transformer policy
tags: [source, paper, curiosity, 3DGS, exploration, RL, world-model]
updated: 2026-05-23T14:13:37Z
created: 2026-05-23T14:13:37Z
---

---
created: 2026-05-23
updated: 2026-05-23
type: source
summary: "Recuriosity uses online 3DGS as a persistent world model + episodic RGB transformer policy for curiosity-driven 3D exploration, outperforming map-based baselines and enabling zero-shot generalization to AI-generated worlds."
tags: [curiosity-driven-exploration, 3DGS, world-model, episodic-memory, RL, exploration, 3D-reconstruction, habitat, photorealistic]
sources: [https://arxiv.org/abs/2605.22814]
status: active
confidence: 0.95
---

# Remember to be Curious: Episodic Context and Persistent Worlds for 3D Exploration

**Recuriosity** (arXiv:2605.22814v1) is a curiosity-driven RL framework for exploring photorealistic 3D indoor environments using only RGB input at deployment. The key innovation is using **online 3D Gaussian Splatting (3DGS) as a persistent forward model** paired with a **transformer-based episodic RGB history policy**. This dual design addresses the core failure mode of prior curiosity approaches: amnesiac agents that collapse into local loops because their world model cannot maintain spatial persistence.

## Paper Metadata

| Field | Value |
|-------|-------|
| **Title** | Remember to be Curious: Episodic Context and Persistent Worlds for 3D Exploration |
| **Authors** | Lily Goli (UofT/Vector), Justin Kerr (UC Berkeley), Daniele Reda (Wayve), Alec Jacobson (UofT/Vector), Andrea Tagliasacchi (UofT/Wayve/SFU), Angjoo Kanazawa (UC Berkeley) |
| **arXiv ID** | 2605.22814v1 |
| **Published** | 21 May 2026 |
| **Categories** | cs.LG (Machine Learning), cs.AI (Artificial Intelligence), cs.RO (Robotics) |
| **Code** | recuriosity.github.io |

## Executive Summary

**Problem:** Curiosity-driven exploration in complex photorealistic 3D environments fails because agents become trapped in local loops — they receive fresh rewards for revisiting "forgotten" states when the forward model lacks spatial persistence.

**Key Innovation:** Two-component design: (1) an **online 3DGS forward model** that maintains a persistent, continuously-updated 3D reconstruction of the environment, providing reliable curiosity rewards based on novel view disagreement; and (2) a **long-context transformer policy** conditioned on full RGB observation history (episodic context) that enables planning toward novel regions, including backtracking through already-seen areas.

**Result:** Trained purely via curiosity on HM3D (800 scenes), the agent outperforms active-mapping RL baselines and generalizes zero-shot to Gibson and AI-generated worlds (World Labs). Fine-tuning on downstream tasks (apple-picking, image-goal navigation) outperforms from-scratch training in sparse-reward regimes.

## Technical Approach

### Core Insight: Amnesiac Exploration Failure

Prior curiosity methods (ICM and variants) fail in photorealistic 3D because:
1. **No spatial persistence**: The forward model is a statistical prior over lifelong experience, not an episodic record — revisiting an area produces fresh prediction errors (= false novelty rewards).
2. **No episodic context**: The agent lacks history to plan toward unseen regions; it cannot learn to "traverse already-seen areas to find novel branches."

The paper shows these two failures compound: without persistence, revisiting produces spurious rewards; without episodic memory, the agent cannot execute strategies like backtracking to reach unexplored branches.

### Persistent 3D Forward Model (3DGS)

The forward model instantiates an **online 3DGS representation** that:
- Is initialized from each incoming RGB-D frame (color, depth, camera pose) as gaussian primitives per pixel
- Is optimized at fixed intervals on randomly selected past frames
- Is densified and pruned following 3DGS-MCMC
- Renders predicted views from any query pose via differentiable rasterization
- At each step, compares the rendered prediction against the observed RGB to compute curiosity reward

The curiosity reward is binary: `r_new > 0` when filtered prediction error exceeds threshold τ (unexplained view), `r_old < 0` for already-explained views. This avoids rewarding high-frequency texture noise.

> "Without historical context, agents repeatedly revisit the same locations; simultaneously, without a persistent and continuously updating world model, predictive errors spuriously arise in these revisited areas, yielding false novelty rewards for forgotten states."

### Episodic RGB Transformer Policy

The agent backbone is a **transformer over RGB-action sequences** — no geometric map, no depth sensor at deployment:
- Each RGB frame is encoded via patch embeddings + DINOv2 features, fused through a learnable query token
- Causal sliding-window self-attention processes temporal context
- A global linear-attention memory module (inspired by TTT/LoGeR) enables long-range information propagation without full O(n²) attention
- Actor-critic heads emit actions and value estimates

The policy is conditioned on full observation history `π(· | o₁:t, a₁:t₋₁)`, giving it the episodic memory needed to discover strategies like backtracking. Actions are geometrically encoded as Plücker-ray images representing intended camera transformations.

### Training: PPO + Random Action Regularization

- Optimized with PPO; curiosity reward is the only training signal
- Random action mixing: at each step, action sampled from `(1-β)π + βU` where β is annealed from 20%→0% over training
- This overcomes "reward-less stretches" where the agent must traverse already-seen regions to find novel branches
- No imitation learning bootstrapping or hierarchical goal selection required

## Key Results

### HM3D Exploration Performance (Primary Metric: 3D Scene Completeness %)

| Method | @256 steps | @512 steps | @1024 steps |
|--------|------------|------------|-------------|
| ANS-RGB | 45.28 | 54.68 | 65.39 |
| ANS-depth | 51.02 | 61.45 | 69.68 |
| OccA-RGB | 47.67 | 58.32 | 68.86 |
| OccA-RGBD | 52.71 | 64.91 | 74.62 |
| **Ours** | **56.50** | **66.69** | **74.94** |

All baselines require depth or explicit mapping. Ours requires only RGB at deployment.

### Memory Ablation (HM3D Completeness @1024)

| Configuration | Completeness % |
|--------------|----------------|
| ICM (no persistence) | 37.36 |
| Short Memory 3DGS (64 frames) | 43.44 |
| Transformer, ctx=1 | 40.66 |
| Transformer, ctx=4 | 50.39 |
| Transformer, ctx=16 | 60.56 |
| **Ours (3DGS + full ctx)** | **74.94** |

Shows that both persistent world model AND long context are necessary.

### Downstream Task Fine-tuning (Apple-Picking)

Fine-tuning after pretraining outperforms from-scratch training, especially when rewards are sparser (fewer apples). Zero-shot pure exploration also hits some apples.

### Zero-Shot Generalization

Zero-shot to:
- **Gibson** (86 office scenes): 82.42% completeness @1024, avg dist 0.10m
- **AI-generated worlds** (World Labs Hobbit World, Spaceship): coherent navigation, only 2-3 collisions over 256 steps — despite different rendering pipeline (3DGS representation vs realistic mesh scans)

> "The agent exhibits coherent exploratory behavior: it navigates corridors, discovers doors to new spaces, and avoids collisions."

## Relevance to EFHF/AGEM/MOP Research Connections

### efhf
The paper's two-component architecture (persistent world model + episodic policy) mirrors the EFHF layer separation:
- The 3DGS forward model functions as a **grounding/world model layer** (Layer 2 analog: semantic persistence)
- The transformer policy maintains episodic context akin to **Layer 4 meta-cognitive monitoring** (long-horizon state tracking)
- The curiosity reward is an emergent signal from the mismatch between predicted and observed — similar to how EFHF monitors coherence across layers

### mop-explorer
Recuriosity is a physical-world instantiation of MOP (Molecular Object Protocol) explorer principles:
- The agent is an **autonomous entity** that maintains an internal model of environmental state
- Episodic context functions as **short-term working memory** (the "focus" of exploration)
- The 3DGS representation is a **persistent internal world state** that the agent navigates within
- Curiosity reward drives **explorative behavior** without external guidance — core MOP pattern

### agentic-research
The fine-tuning result directly connects to agentic research pipelines:
- Pre-training on curiosity (self-supervised, no labels) → fine-tuning on sparse downstream reward
- This is a two-stage agentic pipeline: exploration pretraining + task-specific adaptation
- The finding that exploration pretraining outperforms from-scratch even with equal total steps validates the "exploration as densification" argument for agentic research

### verifier-graph
The verifier-graph's causal provenance tracking is analogous to how Recuriosity's curiosity reward works:
- Mismatch between predicted world-state and observed world-state = "violation" signal
- The 3DGS forward model is effectively a **world-state predictor** whose errors signal novel observations
- Planning via episodic memory is navigating a **reasoning graph** where nodes are observations and edges are actions

### mcp-logic
The structural verification role connects to Recuriosity's architecture:
- Both require maintaining a **consistent internal model** (world model in Recuriosity, logical theory in MCP)
- The curiosity signal (prediction error) is structurally similar to **theory contradiction** in logic — both signal anomalies in the model
- The agent's backtracking behavior mirrors abductive reasoning: traversing known areas to find unexplored branches

### graphrag
Recuriosity's episodic context is analogous to a graph traversal:
- Each RGB observation is a node; actions are edges
- The agent maintains the full trajectory graph (observation history) and plans over it
- The 3DGS persistent model can be seen as a **compressive 3D summarization** of the graph
- Zero-shot generalization suggests the policy learns general graph traversal heuristics, not scene-specific

### maximum-occupancy-principle
The curiosity reward implicitly follows a maximum-occupancy logic:
- Novel views are "unoccupied" in the agent's world model → high reward
- Revisited views are "occupied" → small penalty
- The agent seeks to maximize coverage of the state-space, analogous to maximum occupancy in multi-agent coordination

## Key Quotes

> "In this work, we show that enabling curiosity requires both a persistent model of the world and an agent equipped with episodic context."

> "Without historical context, agents repeatedly revisit the same locations; simultaneously, without a persistent and continuously updating world model, predictive errors spuriously arise in these revisited areas, yielding false novelty rewards for forgotten states."

> "We achieve this using an online 3D reconstruction as a persistent model of the world, while the agent policy is parameterized as a sequence model over RGB observations to maintain episodic context."

> "Crucially, because our policy does not require explicit mapping at test time, it remains fully end-to-end and highly adaptable."

> "Our end-to-end policy enables efficient adaptation to downstream tasks, such as apple picking and image-goal navigation, outperforming from-scratch baselines."

## Structural Insights

### Design Space: Curiosity Approaches

| Approach | World Model | Agent Memory | Failure Mode |
|----------|-------------|--------------|--------------|
| ICM-style | Learned dynamics (no persistence) | Short RNN | Collapses to local loops; false novelty rewards |
| Map-based RL (ANS, OccAnt) | Explicit geometric map | Policy conditioned on map | Requires depth; brittle geometry; no semantic flexibility |
| Video diffusion world models | Generative (no persistence) | None | Spatial forgetting; open-loop collapse |
| **Recuriosity (ours)** | **Online 3DGS (persistent)** | **Full RGB sequence transformer** | **Static scenes only (limitation)** |

### Key Finding: Persistence is the Bottleneck

The paper demonstrates experimentally that the primary bottleneck for curiosity in photorealistic environments is **world model persistence**, not agent architecture. The 3DGS forward model is used as a "controlled proxy" for what action-conditioned video models should eventually provide — but current video models fail at spatial persistence (LingBot-World fails at simple 360° turns). This suggests the field needs better persistent world representations more than better exploration policies.

### Implication for AGEM/MOP

The agent's dual memory system — persistent world model + episodic policy history — maps cleanly onto AGEM's distinction between the Molecular System (persistent state) and the Explorer (episodic context). The curiosity reward is the emergent signal that drives the explorer to seek novel regions of the molecular system's state space.

### Temporal Credit Assignment

The random action regularization (mixing with uniform) solves the temporal credit assignment problem for long-horizon exploration: reaching novel regions may require 100s of steps through already-explored space with no intermediate reward. The mixture guarantees exploration even when the learned policy collapses.

## Connections

- [[curiosity-driven-exploration]] — General concept; Recuriosity is a specific implementation
- [[3dgs]] — 3D Gaussian Splatting used as persistent forward model
- [[world-model]] — Connection to world modeling literature and the persistence problem
- [[episodic-memory]] — The transformer's RGB history as episodic context
- [[habitat]] — The 3D environment simulator used for training/evaluation
- [[mop-explorer]] — MOP pattern for autonomous exploration agents
- [[agentic-research]] — Two-stage pretraining → fine-tuning pipeline validated
- [[verifier-graph]] — World-state mismatch as anomaly signal (parallels to verification)
