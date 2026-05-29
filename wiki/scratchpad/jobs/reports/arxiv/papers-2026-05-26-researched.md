---
created: 2026-05-26
updated: 2026-06-27
type: report
summary: arxiv papers researched — Shannon Scaling Law, SkillOpt, SkillLens, bounded representation capacity theme
tags: [arxiv, report]
---

# arxiv Research Report — 2026-05-26

## Related
- [[wiki/index]]
- [[scratchpad/jobs/reports/arxiv/papers-2026-05-26-researched]]

- [[papers-2026-05-26-researched]]

## Papers Processed

### 2605.23901 — Shannon Scaling Law
Non-monotonic scaling laws are real. The Shannon-Hartley theorem maps cleanly to LLM capacity — model size = bandwidth, tokens = signal power, noise from data and model interaction. The critical insight: there is a finite Shannon capacity for LLMs, beyond which U-shaped degradation emerges. Extrapolation from 6.9B to 12B at 307B tokens gives R²=0.847; monotonic baselines collapse. **One-sentence finding**: scaling without SNR maintenance is not just suboptimal — it actively degrades performance.

### 2605.23904 — SkillOpt
First systematic text-space optimizer for agent skills. Skill document = external trainable state of frozen agent. Frontier optimizer model proposes add/delete/replace edits; validation gate accepts only strictly-improving edits. Best/tied-best on all 52 evaluated cells. **One-sentence finding**: skills are trainable artifacts, not just static prompts, and the optimization discipline (learning rate, validation, momentum) is what makes them reliably improve.

### 2605.23899 — SkillLens
First full-lifecycle study of model-generated agent skills. Negative transfer is common and non-trivial. Skill utility is independent of model scale or baseline strength — a model can be a strong extractor but weak consumer. Meta-skill that guides extraction toward transferable features reduces negative transfer. **One-sentence finding**: the skill lifecycle is factorable into extraction quality and consumption quality, and optimizing extraction toward utility-features is what matters for transfer.