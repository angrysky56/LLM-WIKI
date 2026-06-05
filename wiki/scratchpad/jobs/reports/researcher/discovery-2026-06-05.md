# Researcher Discovery Report — 2026-06-05

## Discovery Cycle
- Source pages created: 2
- Concept pages promoted: 2
- Hub marker applied: 1
- Total pages written or updated: 5

## Focus
**Concept Advancement** — promoted two ML-relevant concept stubs from 0.3 to 0.72 via source-anchored expansion.

## New Source Summaries

### [[sources/papers/repe-representation-engineering]]
The RepE paper (Zou et al., 2023, arXiv:2310.01405) — "Representation Engineering: A Top-Down Approach to AI Transparency." Introduces contrastive activation addition (CAA/ActAdd), the canonical method for extracting steering vectors from LLM activations. Fetched, ingested, summarized with 95% confidence.

### [[sources/papers/peft-guide-scaling-down-to-scale-up]]
The PEFT survey (Lialin et al., 2023/2024, arXiv:2303.15647) — "Scaling Down to Scale Up: A Guide to Parameter-Efficient Fine-Tuning." Systematic survey of 50+ PEFT methods with controlled head-to-head comparison at 11B scale. Fetched, ingested, summarized with 95% confidence.

## Concept Advancements

### [[concepts/steering-vectors]] (0.3 → 0.72)
**Previously**: Empty stub — "Steering vectors — directional activation patterns that bias model behavior" with no content and no source anchors.

**Now**: Full-page covering:
- Definition: Directional vectors in activation space encoding high-level cognitive phenomena
- Extraction methods: CAA/ActAdd (RepE), PCA-based, probe-based
- Mathematical properties: orthogonality (mixed evidence), superposition (fundamental to distributed representations), stability (limited transferability across model versions)
- The RepE distinction: Reading (monitoring) vs Controlling (steering)
- Clear separation from activation-engineering: steering-vectors = the *object*, activation-engineering = the *practice*
- 4 genuine open questions (transferability, optimal extraction, orthogonal decomposition, minimal data requirements)
- Source anchors: RepE paper + emotion-concepts-llm article

### [[concepts/fine-tuning]] (0.3 → 0.72)
**Previously**: Thin page (~63 words) — "Fine-tuning adapts pretrained models to downstream tasks via additional training" but no depth, no section structure, no open questions.

**Now**: Full-page covering:
- Definition and position in the modification landscape (vs ICL, activation steering, model editing, pretraining)
- Full fine-tuning vs Parameter-Efficient Fine-Tuning (PEFT)
- PEFT taxonomy: low-rank (LoRA), adapter-based, prompt-based, sparse methods
- Alignment fine-tuning: RLHF, DPO, GRPO
- Safety and security: harmful fine-tuning, routing drift in MoE models
- Comparison table of 5 modification techniques
- 4 genuine open questions (full FT vs PEFT gap, PEFT composability, safety bounds, alternative lifecycles)
- Source anchors: PEFT survey + SafeMoE paper

### [[concepts/machine-learning]] — Hub marker added
Added `subtype: hub` to frontmatter and updated `tags: [ai, ml, hub]` to signal to future audits that this is a lightweight navigation hub, not a thin knowledge page. Confidence adjusted to 0.5 to reflect that it's not a deep page (as intended).

## Carryover Items Completed
- [x] (a) **steering-vectors** promoted with RepE source anchor
- [x] (a) **fine-tuning** promoted with PEFT survey source anchor (also absorbs archived instruction-tuning)
- [x] (d) **machine-learning.md** hub-type marker added to frontmatter (+ `subtype: hub` field)

## Carryover Items Deferred
- [ ] (b) Entity stubs (huggingface, anthropic, google-deepmind, openai-o-series, sakana-ai, priorlabs) — still pending; entity promotion is a different workflow than concept advancement

## Vault Health
- 1144 pages indexed after deep refresh
- 2 new source anchor pages in `wiki/sources/papers/`
- 2 previously-stub concepts now promoted to reference status
- 1 hub page properly tagged

## Open Questions for Next Cycle
1. **Entity stub promotion**: Carryover item (b) — promoting entity stubs like huggingface, anthropic, google-deepmind. These need different research (company/product documentation, not papers). Worth a dedicated cycle.
2. **Ongoing ML concept stubs**: ~75 ML-relevant concept stubs remain (nlp, language-models, graph-theory, shapley-values, open-source-ai). Next cycle could pick shapley-values (has a source anchor in proxy-based-shapley-banzhaf-2026) or open-source-ai (relevant to current AI governance discourse).
3. **Cross-domain synthesis check**: With 2 recently-promoted ML concepts, check if cross-domain connections exist between them and non-ML clusters that were previously unreachable.