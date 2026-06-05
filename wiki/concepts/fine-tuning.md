---
summary: Fine-tuning — adapting pretrained models via additional training; covers full fine-tuning, PEFT (LoRA, adapters, prompt methods), alignment techniques (RLHF, DPO, GRPO), and safety concerns
tags: [ml, training, transfer-learning, peft, alignment]
updated: 2026-06-05T21:07:20Z
---

---
created: 2026-05-25
updated: 2026-06-05
type: concept
summary: Fine-tuning — adapting pretrained models to downstream tasks via additional training; covers full fine-tuning, parameter-efficient methods, alignment fine-tuning, and safety considerations
tags: [ml, training, transfer-learning, peft, alignment]
sources: https://arxiv.org/abs/2303.15647 (PEFT survey)
status: active
confidence: 0.72
---

# Fine-Tuning

## Definition

**Fine-tuning** is the process of adapting a pretrained machine learning model to a downstream task or domain by continuing training on task-specific data. In the context of large language models, it is the primary method for converting a general-purpose foundation model into a specialized one — for instruction following, domain expertise, style adherence, or safety alignment.

Fine-tuning occupies a specific position in the model modification landscape. It is more invasive than [[in-context-learning]] (which changes behavior via the prompt alone) and [[activation-engineering]] (which modifies activations at inference time without changing weights). It is less invasive than training from scratch. The tradeoff: fine-tuning achieves stronger task specialization at the cost of permanent weight changes and the risk of [[catastrophic-forgetting]].

## The Fine-Tuning Landscape

### Full Fine-Tuning

The original approach: load the pretrained weights, train all parameters on the downstream task, save the updated weights.

- **Advantage**: Maximum flexibility — the model can adapt entirely to the target distribution
- **Disadvantage**: Cost-prohibitive for large models — a full backward pass through billions of parameters requires memory equivalent to the entire model
- **When to use**: Small models (<1B parameters), when compute is abundant, when the task distribution differs significantly from pretraining

### Parameter-Efficient Fine-Tuning (PEFT)

A family of methods that train only a small subset of parameters while keeping most weights frozen. The PEFT survey (Lialin et al., 2023/2024) organizes these into:

- **Low-rank methods**: [[lora|LoRA]] and its variants (DoRA, rsLoRA, PiSSA) train low-rank decomposition matrices injected into attention layers. LoRA remains the strongest practical baseline under resource-constrained settings.
- **Adapter-based methods**: Small bottleneck layers (typically MLP with down-projection → activation → up-projection) inserted between transformer sublayers. Well-established for encoder models but less studied for decoder-only LLMs.
- **Prompt-based methods**: [[prompt-tuning]] and [[prefix-tuning]] train soft prompt tokens rather than weight updates. Compute-efficient but consistently underperform low-rank and adapter methods on complex tasks.
- **Sparse fine-tuning**: Selectively update a subset of weights (diff pruning, lottery ticket, fish mask). Theoretically elegant but practically challenging due to optimization instability.

**Key finding** (from the PEFT survey): Methods that claimed to surpass LoRA in isolated comparisons often fail to replicate that advantage in resource-constrained settings with limited hyperparameter tuning, suggesting that many PEFT improvements are artifacts of extensive per-method tuning rather than genuine architectural advantages.

### Alignment Fine-Tuning

Fine-tuning used specifically to align model behavior with human preferences. The dominant approaches:

- **RLHF**: Train a reward model on human preferences, then use PPO to optimize the LLM against it. Produces consistently aligned behavior but is complex and reward-hacking-prone.
- **DPO**: Direct preference optimization — replaces the reward model with a closed-form preference likelihood derived from the policy itself. Simpler, more stable, but less understood theoretically.
- **GRPO**: Group-relative policy optimization — uses group of candidates per prompt, trains on relative preferences within each group. Recent results (DeepSeek-R1) suggest it can outperform both RLHF and DPO for reasoning tasks.

## Safety and Security Concerns

Fine-tuning introduces a critical attack surface:

- **Harmful fine-tuning**: Attackers can fine-tune public-weight models to remove safety guardrails. The [[defending-moe-llms-against-harmful-fine-tuning-via-safety-routing-alignment]] paper shows that harmful fine-tuning causes routing drift in MoE models — experts handling harmful inputs shift away from safety-aligned pathways.
- **Alignment tax**: Fine-tuning for task performance can degrade alignment, and vice versa. The interaction between alignment and capability fine-tuning is not well understood.
- **Model editing**: [[model-editing]] methods (ROME, MEMIT) offer surgical alternatives to fine-tuning for specific knowledge updates, but their long-term stability is unproven.

## Relationship to Other Modification Techniques

| Technique | Weight Change | Persistence | Compute Cost | Specialization |
|-----------|--------------|-------------|--------------|----------------|
| **In-context learning** | None | Session | Negligible | Weak |
| **Fine-tuning** | Permanent | Persistent | Moderate-high | Strong |
| **Activation steering** | None | Session | Low | Moderate |
| **Model editing** | Localized | Persistent | Low | Surgical |
| **Pretraining** | Full | Persistent | Prohibitive | Generic |

## Connections

- [[parameter-efficient-fine-tuning]] — the sub-concept focused on PEFT methods
- [[lora]] — the dominant low-rank PEFT method
- [[instruction-tuning]] — fine-tuning on instruction-response pairs (absorbed into this page)
- [[transfer-learning]] — the theoretical foundation for fine-tuning
- [[model-editing]] — weight-level modifications vs fine-tuning
- [[activation-engineering]] — inference-time modification vs weight-level tuning
- [[in-context-learning]] — no-weight-change alternative
- [[concepts/fine-tuning]]
- [[sources/papers/peft-guide-scaling-down-to-scale-up]]
- [[sources/papers/defending-moe-llms-against-harmful-fine-tuning-via-safety-routing-alignment]]

## Source Anchors

- [[sources/papers/peft-guide-scaling-down-to-scale-up]] (0.95) — comprehensive PEFT survey covering 50+ methods with controlled experimental comparison at 11B scale
- [[sources/papers/defending-moe-llms-against-harmful-fine-tuning-via-safety-routing-alignment]] (0.80) — demonstrates routing drift and safety degradation from harmful fine-tuning in MoE architectures

## See Also

- [[catastrophic-forgetting]] — the primary failure mode of sequential fine-tuning
- [[continuous-learning]] — lifelong adaptation without forgetting
- [[sleep-self-modify-consolidate-2026]] — wake/sleep paradigm as an alternative to static fine-tuning

## Open Questions

1. **Full FT vs PEFT gap**: Under what conditions does full fine-tuning substantially outperform PEFT? The PEFT survey suggests the gap depends on task complexity and data size, but these boundaries are not well characterized.
2. **PEFT composability**: Can multiple independently trained PEFT modules (e.g., one for domain knowledge, one for style) be combined at inference without interference? Current approaches are ad-hoc.
3. **Fine-tuning safety bounds**: When does fine-tuning begin to degrade safety alignment? Can alignment be losslessly preserved through fine-tuning on safety-unrelated tasks?
4. **Alternative lifecycles**: Does the [[sleep-self-modify-consolidate-2026]] wake/sleep paradigm or other non-fine-tuning approaches offer a genuine alternative for adapting large models?
