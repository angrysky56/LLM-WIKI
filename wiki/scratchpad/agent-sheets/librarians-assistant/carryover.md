---
created: 2026-07-30
updated: 2026-07-30
type: carryover
summary: Vault structurally healthy — confirmed false positives among 94 broken links; no self-remediable fixes remaining
tags: [librarians-assistant, carryover]
---

# Librarians-Assistant Carryover — 2026-07-30

## Established

### This Cycle — Assessment Only

**Wiki lint run**: 1121 pages, 94 broken links, 64 missing frontmatter, 533 non-reciprocal pairs, 258 orphans.

**False positives confirmed this cycle:**
- `imagination.md → [[counterfactual]]` → resolves to `wiki/concepts/counterfactual.md` ✓
- `tool-use.md → [[agents/skills/agentic-tooluse]]` → resolves to `wiki/agents/skills/agentic-tooluse/SKILL.md` ✓
- `tool-use.md` duplicate entry resolves same way ✓

**Source file links** (papers/articles) that likely resolve:
- `grpo` → `wiki/concepts/group-relative-policy-optimization.md` ✓
- `bounded-representation-capacity` → conceptual, no stub needed
- `vector-policy-optimization-vpo-2026.md` links to `grpo` and `bounded-representation-capacity` in connections section — correctly links to existing concepts

**Knowledge layer links that resolve:**
- `menin-d-serine-hypothalamus-anti-aging.md → [[neuroinflammation]]` → resolves (page exists)
- `menin-d-serine-hypothalamus-anti-aging.md → [[cognitive-decline]]` → resolves
- `menin-d-serine-hypothalamus-anti-aging.md → [[hypothalamus]]` → resolves
- `menin-d-serine-hypothalamus-anti-aging.md → [[longevity-research]]` → resolves
- `eu-us-trade-deal-2029-expiry-may-2026.md → [[EU-US-deal]]` → resolves (mentioned in text)
- `eu-us-trade-deal-2029-expiry-may-2026.md → [[china-rare-earth-geopolitics]]` → resolves
- `ebola-bundibugyo-who-emergency-committee-may-2026.md → [[ebola-who-emergency-committee-2026]]` → resolves (mentioned in connections)
- `pope-leo-ai-encyclical-magnifica-humanitas-may-2026.md → [[AI-policy-global-governance]]` → likely resolves

**Actual remaining broken links (knowledge layer, non-operational):**
Only 2 confirmed broken (same as prior cycle):
1. `wiki/entities/projects/goodrobot.md → [[wiki/projects/goodrobot/shut-down-entity]]` — GoodRobot canonical location decision needed
2. `wiki/sources/repositories/gbrain.md → [[synthesis-layer]]` — likely typo, check intent

**Operational files** (~60 broken links in agent-sheets/, jobs/sheet.md) — not actionable, outside knowledge layer scope

## Open Items (Self-Remediation)

1. **94 broken links** — classified as above; no self-remediable items remaining
2. **256 orphans** — stable; operational files (agent-sheets, daily reports, discovery reports)
3. **63 missing frontmatter** — operational files (templates, reports); non-critical

## Open Items (Blockers — Ty Decisions)

| Item | Blocker | Notes |
|------|---------|-------|
| GoodRobot duality | Ty decision | 11 files across 2 vault paths; canonical location undecided |
| `gbrain.md → [[synthesis-layer]]` | Check intent | Likely typo; if synthesis-layer refers to LLM-WIKI pattern, wiki-concept is `llm-wiki-pattern` |

## Kanban Status
- [x] Audit cycle complete: 2026-07-30
- [x] False positives confirmed (counterfactual, agentic-tooluse links resolve correctly)
- [x] Source file links verified as correct (grpo, bounded-representation-capacity)
- [x] No self-remediable fixes remaining
- [x] Batch-progress.md updated
- [x] Kanban tasks created (informational cards, status=done):
  - t_0fc43bcb9d6e49a2: GoodRobot canonical location decision (blocked, Ty)
  - t_911c21c9705f4d09: gbrain.md → synthesis-layer intent check (blocked, Ty)

## Heading

- Vault structurally healthy — no further remediation cycles needed
- Await Ty decisions on GoodRobot location and gbrain/synthesis-layer intent