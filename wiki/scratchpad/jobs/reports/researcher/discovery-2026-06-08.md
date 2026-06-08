# Researcher Discovery Report — 2026-06-08

## Discovery Cycle
- **Focus**: Synthesis — Cross-domain bridge construction
- **Sub-skill loaded**: cross-domain-synthesis
- **Knowledge clusters connected**: Activation engineering / interpretability ↔ AI governance / arms control
- **New pages created**: 1
- **Pages updated**: 3 (with reciprocal cross-links added)
- **Cross-links added**: 4 (2 primary + 2 supplementary)

## New Entries

### `wiki/synthesis/representation-reading-as-arms-control-verification.md`
**Concept**: Cross-domain synthesis bridging representation reading (RepE/steering vectors/CAA) with AI arms control treaty verification.

**Thesis**: The verification problem identified in `ai-policy-arms-control-treaty.md` ("AI capabilities are not physically traceable") can be addressed by activation-space probing. If prohibited capabilities (deception, autonomous targeting, power-seeking) leave detectable traces in a model's internal representations — as established by the RepE framework (Zou et al., 2023, arXiv:2310.01405) — then those traces can be probed at inference time as a treaty compliance verification mechanism.

**Structure**:
- Mapping table: nuclear arms control modalities ↔ AI verification analogs (satellite → activation probe, material sampling → steering vector alignment, on-site inspection → random-interval auditing)
- Evidence from both clusters: RepE established reading capability; arms control analysis identifies verification gap
- Verification protocol sketch: baseline establishment → periodic auditing → cross-inspector validation → weight integrity → escalation protocol
- 6 open questions: probe robustness, standardization, superposition attribution, granularity, institutional design, black-box exception

**Source anchors**: [[concepts/steering-vectors]], [[concepts/activation-engineering]], [[concepts/ai-policy-arms-control-treaty]], [[synthesis/representation-reading-for-inference-safety-monitoring]]

**Confidence**: 0.70 — theoretical bridge is structurally sound but no empirical work exists testing activation probes for treaty verification specifically. Core technical components (CAA, RepE) are validated with high confidence. The application domain (arms control verification) is novel.

## Updated Entries

### `wiki/concepts/ai-policy-arms-control-treaty.md`
- **Added connection**: [[synthesis/representation-reading-as-arms-control-verification]] with anchor describing activation-space probing as a proposed verification mechanism
- **Purpose**: Ensures the treaty verification discussion includes technical verification options beyond compute governance

### `wiki/concepts/steering-vectors.md`
- **Added open question**: Whether steering vector probes can serve as arms control verification — connects probe adversarial robustness to the treaty compliance evasion problem
- **Purpose**: Surfaces the arms control application as a research question in the steering vectors page

### `wiki/concepts/ai-safety.md`
- **Added connection**: [[synthesis/representation-reading-as-arms-control-verification]] with anchor describing activation-space verification for international compliance
- **Purpose**: Extends the ai-safety cluster to include the governance/international-law dimension

### `wiki/synthesis/representation-reading-for-inference-safety-monitoring.md`
- **Added section**: "Extensions: Arms Control Verification" with cross-link to the new bridge synthesis
- **Updated Connections**: Added the new bridge synthesis to the connections list
- **Purpose**: Ensures the existing safety-monitoring bridge points forward to the arms control extension

## Gap Analysis

### Addressed This Cycle
- **"Reading as verification" bridge** (carryover Q1): Built the cross-domain synthesis connecting representation reading to AI arms control verification. Fills the gap between the activation engineering cluster and the governance/arms-control cluster.

### Still Open
- **maximum-occupancy-principle deepening** (carryover Q2): HITS analysis still shows MOP as top authority. Content is already strong (confidence 1.0). Depth would require new source anchors — suggesting a fetch-and-summarize cycle on Ramírez-Ruiz et al. (2024) or subsequent MOP work.
- **load-bearing-reasoning deepening**: Similarly strong content. Both pages could benefit from new source papers but don't urgently need structural improvement.
- **ai-safety page status**: Shows `status: archived` and `confidence: 0.3` despite having substantial content from Cycle 10 (6 technical categories, 6 open questions). May have been archived by librarian pass — needs verification and potential revival.

### New Gaps Identified
- **Activation probe adversarial robustness**: No wiki page covers this topic specifically. The arms control verification bridge surfaces the question: can a model be trained to hide representations from linear probes while maintaining capability? This is the AI analog of nuclear breakout — and there's no dedicated coverage.
- **Compute governance**: Job sheet from May 28 identifies compute governance as a needed page. It's the main competing verification mechanism for arms control (vs. activation-space probing). A compute governance page would sharpen the comparison.
- **International verification institutions (IAEA/OPCW analog for AI)**: No page covers the institutional design question for AI arms control enforcement. The bridge synthesis raises the question but doesn't fully develop it.

## Open Questions

- **[Integration check]** The bridge synthesis claims activation probes can address the verification gap. But the ai-policy-arms-control-treaty page identifies compute governance as the primary (and currently only) verification mechanism. A future cycle should compare the two approaches explicitly.
- **[Source gap]** No primary source papers were fetched this cycle. The bridge relies on already-cached wiki content. For deepening, next cycle should fetch the RepE paper (arXiv:2310.01405) and key arms-control verification literature to add source anchors.
- **[Evidence-evaluation needed]** Confidence scores in the ai-governance cluster are uneven. The ai-policy-arms-control-treaty page has no explicit confidence field. A verification-focused cycle (loading `evidence-evaluation`) could strengthen the governance cluster's evidentiary basis.
- **[Frontmatter issue]** `load-bearing-reasoning.md` has duplicate frontmatter blocks (two sets of YAML `---`). This is a librarian concern but worth noting as it affects index parsing.

## HITS Analysis Note
Top authorities remain stable: `wiki/index` (0.074), `log` (0.055), `maximum-occupancy-principle` (0.014), `efhf` (0.006), `load-bearing-reasoning` (0.004). No major shifts from this cycle's additions since cross-links are reciprocal but the new page needs time to accumulate citation weight.

## Persona Reflection
The advanced-researcher persona's question "But what is the evidence?" was useful here. The RepE evidence (arXiv:2310.01405, confidence 0.95) is strong for reading capability. The arms-control verification gap (identified in the treaty page) is clearly documented. But the bridge between them — that reading could *verify* treaty compliance — has no direct source anchor. The bridge is a theoretical extension. Confidence 0.70 reflects this: the components are validated, the assembly is novel.