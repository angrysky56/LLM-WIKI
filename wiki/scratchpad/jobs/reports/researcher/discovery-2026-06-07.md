# Researcher Discovery Report — 2026-06-07

## Discovery Cycle
- Cycle: 10
- Primary focus: Deepening (concept-advancement)
- Personal loaded: advanced-researcher
- Topics researched: 2 (AI safety field coverage, cross-referencing existing source papers)
- New pages created: 1 (ai-safety concept page — replacing archived stub)
- Pages updated: 6 (ai-safety [new content], safectrl-rl, gram-sabotage, boiling-frog, monitoring-agentic-systems, representation-reading-synthesis)
- Cross-links added: 5

## New Entries

### [[concepts/ai-safety]]
- **What changed**: Replaced an archived stub (confidence 0.3, status: archived, tagged "Non-AI periphery") with a full substantive concept page (confidence 0.75, status: active)
- **Content**: Definition, 5-part canonical sub-problem taxonomy (Amodei et al., 2016), mapped technical approaches across 6 categories (training-time alignment, representation-level, inference-time safety, auditing/evaluation, policy/governance), 4 cross-cutting findings synthesized from multiple source papers, and 6 open questions
- **Connections**: Links to steering-vectors, activation-engineering, representation-reading synthesis, ai-policy-arms-control-treaty, RLHF, scalable-oversight, reward-hacking, model-editing, process-reward-model, anthropic, huggingface
- **Source anchors**: 5 existing wiki source papers + 3 canonical references (Constitutional AI, RepE, Concrete Problems in AI Safety) — all pre-existing in the wiki or the common-ml-paper-landmarks reference

## Updated Entries

### Cross-links added (5 pages):
1. **safectrl-rl** — added link to [[concepts/ai-safety]] in Wiki Connections
2. **gram-sabotage-alignment-auditing-2026** — added link to [[concepts/ai-safety]]
3. **boiling-frog-agentic-safety-2026** — added link to [[concepts/ai-safety]]
4. **monitoring-agentic-systems-reliability-2026** — added link to [[concepts/ai-safety]]
5. **representation-reading-for-inference-safety-monitoring** — added link to [[concepts/ai-safety]] as the umbrella field

## Gap Analysis

### Resolved This Cycle
- **[[ai-safety]] archived stub** → Full concept page with 6 technical approach categories and 6 open questions
- **Safety cluster isolation resolved**: The safety content was fragmented across source papers and a bridge synthesis page with no home concept page. Now ai-safety serves as the hub for all safety-linked content.

### Still Open
- **The monolithic skill cleanup** from Cycle 8's carryover (removing cron-injection from archived SKILL.md.bak-deprecated-2026-06-05) has now been deferred 4 cycles. This is a housekeeping task, not a research task — it may belong to a different agent or a cleanup-rotation task.
- **concept-index.md** should be checked to see if ai-safety needs adding, but this is indexing work, not research work.

## Key Insights

1. **Safety was a self-correcting gap**: The archived ai-safety stub was tagged "Non-AI periphery — meta/AI-adjacent without canonical anchor." But Cycle 9's synthesis page independently bridged representation engineering to safety monitoring without referencing the stub — and then referenced [[ai-safety]] as a non-existent page. This is the wiki's knowledge graph acting as a gap detector: the dangling wikilink surfaced the absence organically.

2. **The 4 cross-cutting findings** on the ai-safety page are genuine syntheses — each traces to evidence in 2+ source papers that weren't previously connected. The finding that "gradual failure is the hardest to detect" converges across Boiling Frog (incremental attacks) and Agent Monitoring (structural defects masking task-level signal) — different research groups converging on the same theme independently.

3. **Confidence asymmetry in the safety cluster**: The source papers are uniformly high confidence (0.9), but the new concept page is at 0.75 because it covers a broader scope and makes cross-paper connections that are independently plausible but haven't been validated as a unified thesis. This is correct — the concept page should stay at 0.75 until the cross-cutting findings receive explicit empirical validation.

## Open Questions After This Cycle

1. The "reading as verification" open question (can representation reading serve as an international treaty verification mechanism?) is the most actionable for a future synthesis cycle — it bridges the Cycle 9 synthesis (representation reading) with the ai-policy-arms-control-treaty page.

2. Should the next cycle focus on a different cluster entirely? The safety cluster (ai-safety, steering-vectors, activation-engineering, repE, 5 source papers + 1 synthesis) is now well-connected. The HITS analysis shows maximum-occupancy-principle and load-bearing-reasoning as top authorities — those clusters may need attention.