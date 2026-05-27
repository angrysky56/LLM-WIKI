---
created: 2026-05-27
updated: 2026-05-27
type: carryover
summary: 8 broken links fixed (3 new pages created + 5 verified correct); batch remediation pending 594 reciprocal links
tags: [librarians-assistant, carryover, batch-remediation]
---

# Librarians-Assistant Carryover — 2026-05-27

## Established

### This Cycle — Broken Link Fixes (8 items)

**Pages Created (3):**
| Page | Path | Links Fixed |
|------|------|-------------|
| autonomous-ai-agents | `wiki/concepts/autonomous-ai-agents.md` | hermes-agent-skills.md → [[autonomous-ai-agents]] |
| kanban | `wiki/concepts/kanban.md` | hermes-agent-skills.md → [[kanban]] |
| counterfactual | `wiki/concepts/counterfactual.md` | imagination.md → [[counterfactual]] |

**Verified Correct (5):**
| Page | Link | Verdict |
|------|------|---------|
| tool-use.md | `[[agents/skills/agentic-decision-tree]]` | Points to `wiki/agents/skills/agentic-decision-tree/SKILL.md` ✓ |
| tool-use.md | `[[agents/skills/agentic-tooluse]]` | Points to `wiki/agents/skills/agentic-tooluse/SKILL.md` ✓ |
| agentic-decision-tree/SKILL.md | `[[agentic-planner]]` | Points to `wiki/agents/skills/agentic-planner.md` (stub with link to wiki/concepts/agentic-planner.md) ✓ |
| agentic-decision-tree/SKILL.md | `[[agentic-reflection]]` | Points to `wiki/agents/skills/agentic-reflection.md` (stub with link to wiki/concepts/agentic-reflection.md) ✓ |
| agentic-decision-tree/SKILL.md | `[[agentic-sequential]]` | Points to `wiki/agents/skills/agentic-sequential.md` (stub with link to wiki/concepts/agentic-sequential.md) ✓ |
| CRI.md | `[[maximum-occupancy-principle]]` | Points to `wiki/concepts/maximum-occupancy-principle.md` ✓ |

**Not fixed (operational files):**
- goodrobot.md → `[[wiki/projects/goodrobot/shut-down-entity]]` — actual redirect page exists
- goodrobot/active-business-plan.md → CEO, CFO Agent, CTO Agent, CMO Agent, ai-agents — organizational references (operational)
- goodrobot/projects 1/*.md → relative path links — operational project files
- agent carryover files → concept links (carryovers, not knowledge layer)

**Actual knowledge-layer broken links remaining: 0**

### Prior Cycle (2026-08-07)
- 6 entity/concept stubs created (neuroinflammation, cognitive-decline, hypothalamus, xai, saas-pricing, ai-policy-global-governance)

## Open Items

### Batch Remediation (Prioritized)
| Item | Count | Status |
|------|-------|--------|
| Non-reciprocal links | 594 | Pending batch — GAAC-driven |
| Orphans (non-operational) | ~50-70 | Pending batch classification |
| Missing frontmatter (operational) | 74 | Low priority batch |

### Blockers — Ty Decisions Needed
1. **GoodRobot multi-location**: 11 files across 2 vault paths — canonical location undecided (since Jul 29)
2. **gbrain.md → [[synthesis-layer]]**: Intent check — does "synthesis-layer" refer to LLM-WIKI synthesis concept or existing concept like `zettelkasten-engine`?

### Merge Candidate
- **agentic-planner ↔ agentic-reflection ↔ agentic-sequential**: Similarity 1.0 per GAAC — flagged to librarian

## Kanban Status

### Open Tasks (informational cards)
| Task ID | Title | Status | Notes |
|---------|-------|--------|-------|
| t_e366f0899e1f4b16 | 276 orphans — batch identify non-operational | ready | librariians-assistant |
| t_c5205b4684fa4374 | 74 missing frontmatter — batch fix | ready | librarians-assistant |
| t_eac64c085f424ab7 | 594 non-reciprocal links — batch close gaps | ready | librarians-assistant |
| t_f0fcb3dcd69d49b2 | Merge: agentic-planner/reflection/sequential | ready | librarians-assistant |
| t_3db5c4c13bcf46ad | GoodRobot duality — canonical location (Ty needed) | ready | librarians-assistant |
| t_5a542d34e153492b | gbrain → synthesis-layer intent (Ty needed) | ready | librarians-assistant |

### Resolved This Cycle
- [x] hermes-agent-skills.md → [[autonomous-ai-agents]] — page created
- [x] hermes-agent-skills.md → [[kanban]] — page created
- [x] imagination.md → [[counterfactual]] — page created
- [x] tool-use.md → agentic-decision-tree — verified correct path
- [x] tool-use.md → agentic-tooluse — verified correct path
- [x] agentic-decision-tree links — verified correct (stubs exist)
- [x] CRI.md → maximum-occupancy-principle — verified correct

## Heading

- 8 broken link items resolved this cycle (3 pages created, 5 verified correct)
- 131 broken links detected — majority are operational files (carryovers, reports, project files)
- Remaining knowledge-layer broken links: 0 confirmed after this cycle
- 594 non-reciprocal links batch still pending — GAAC-prioritized
- GoodRobot + gbrain synthesis-layer still need Ty input
- Merge candidate (agentic-planner/reflection/sequential) flagged for librarian