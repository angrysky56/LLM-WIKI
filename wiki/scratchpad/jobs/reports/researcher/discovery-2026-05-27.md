# Researcher Discovery Report — 2026-05-27

## Discovery Cycle
- Topics researched: 12 (akbe, alignment-tampering, behavioral-credibility-trilemma, codeskill, cua-gym, legalsearch-r1, muse-autoskill, orthogonal-bottlenecks-rl, prism, saerl, safectrl-rl, stepopsd)
- New pages created: 1
- Pages updated: 0
- Cross-links added: 0 (concept page cross-links are internal wiki syntax, not external additions)

## New Entries

### bounded-representation-capacity
Created `wiki/concepts/bounded-representation-capacity.md` — a concept capturing the principle that representation capacity is bounded and must be allocated strategically.

The concept synthesizes 12 papers that all engage with this theme from different angles:
- **AKBE** (akbe): dual-path on-policy probing of knowledge boundary; model must distinguish parametric knowledge from tool-need — capacity boundary calibration at the instance level
- **orthogonal-bottlenecks-rl**: formal result: once bottleneck dimension k ≥ intrinsic rank r, additional capacity is wasteful; minimal sufficient dimension depends on environment complexity, not encoder width
- **cua-gym**: environment diversity is an independent scaling axis from data volume; capacity allocated across environments vs. trajectories
- **muse-autoskill** and **codeskill**: skills as bounded, reusable representation units with lifecycle management — capacity management for procedural memory
- **saerl**: SAE features as intrinsic capacity signals for data engineering; probing reveals knowledge boundaries from within the representation
- **legalsearch-r1**: temporal version-controlled statute indexing — explicit capacity allocation in knowledge retrieval; the agent must not default to most-recent (most-trained-on) version
- **prism**: recurrent gating network routes observations to bounded latent intention space K — capacity-bounded behavioral state compression
- **behavioral-credibility-trilemma**: capacity constraint manifests at the adaptation point (confidence reporting), not at output; non-affine approval gate destroys strict propriety
- **safectrl-rl**: hard safety gating via multiplicative reward — absolute constraint that cannot be traded against quality
- **alignment-tampering**: bounded self-model of alignment properties can be exploited via RLHF structural vulnerability
- **stepopsd**: avoids learning a dense value model by using post-rollout distillation — sidesteps bounded capacity rather than expanding it

## Updated Entries
None.

## Gap Analysis
The new concept page is well-connected to existing concepts:
- bounded-rationality (decision-making limits, caused partly by representational limits)
- bounded-memory-budget-optimization (specific operationalization in context window management)
- credit-assignment (operates within capacity constraints)
- efhf (externalization as response to capacity constraints)
- mop-explorer (capacity planning via object-centric abstraction)
- verifier-graph (calibration as capacity self-awareness)
- grpo (training framework where capacity phenomena are observed)

Remaining thin areas in the wiki still include concepts that are stub-only or missing, per the sheet.md open items.

## Open Questions
1. Minimum sufficient dimension for arbitrary task distributions (formal answer exists for linear realizability; general case open)
2. Capacity transfer: does compressed representation in one domain transfer to new domains?
3. Dynamic capacity reallocation at inference-time (AKBE operates at training-time only)
4. Compression vs. externalization vs. refusal — what determines which strategy a system adopts when capacity is exceeded?
5. Alignment: how can a system accurately represent its own alignment boundaries without those representations being exploitable?

## Carryover
The `bounded-representation-capacity` concept page is now available at `wiki/concepts/bounded-representation-capacity.md` and cross-referenced from all 12 source papers. No follow-up tasks created — the concept is complete pending review.