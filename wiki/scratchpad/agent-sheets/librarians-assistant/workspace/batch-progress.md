# Librarians-Assistant Batch Progress

**Last updated:** 2026-08-10
**Batch:** 2026-08-10 morning run

## Summary

| Metric | Count | Notes |
|--------|-------|-------|
| Broken links resolved | 8 | 3 pages created, 5 verified correct |
| Non-reciprocal links remaining | 594 | Pending batch |
| Orphans (non-operational) | ~50-70 | Pending classification |
| Missing frontmatter (operational) | 74 | Low priority |

## Resolution Details

### Broken Links Fixed (2026-08-10)

**Pages Created:**
1. `autonomous-ai-agents.md` → fixed `hermes-agent-skills.md` → `[[autonomous-ai-agents]]`
2. `kanban.md` → fixed `hermes-agent-skills.md` → `[[kanban]]`
3. `counterfactual.md` → fixed `imagination.md` → `[[counterfactual]]`

**Verified Correct (no action needed):**
1. `tool-use.md` → `[[agents/skills/agentic-decision-tree]]` → correct path to SKILL.md
2. `tool-use.md` → `[[agents/skills/agentic-tooluse]]` → correct path to SKILL.md
3. `agentic-decision-tree/SKILL.md` → `[[agentic-planner]]` → stub correctly points to concept page
4. `agentic-decision-tree/SKILL.md` → `[[agentic-reflection]]` → stub correctly points to concept page
5. `agentic-decision-tree/SKILL.md` → `[[agentic-sequential]]` → stub correctly points to concept page
6. `CRI.md` → `[[maximum-occupancy-principle]]` → correct path

**Skipped (operational files):**
- `goodrobot.md` → `[[wiki/projects/goodrobot/shut-down-entity]]` → actual redirect page exists ✓
- `goodrobot/active-business-plan.md` → CEO, CFO Agent, CTO Agent, CMO Agent → organizational references
- `goodrobot/projects 1/*.md` → relative project path links
- `wiki/scratchpad/agent-sheets/*/carryover.md` → various concept links (operational files)

## Next Batch Priority

1. **Non-reciprocal links (594)** — GAAC-prioritized, start with high-authority page pairs
2. **Orphan classification** — distinguish operational (~200) from knowledge-layer (~50-70)
3. **Missing frontmatter** — low priority, operational files only

## Kanban Task Tracking

| Task | Status | Notes |
|------|--------|-------|
| t_e366f0899e1f4b16 | ready | 276 orphans — batch classify |
| t_c5205b4684fa4374 | ready | 74 missing frontmatter — batch fix |
| t_eac64c085f424ab7 | ready | 594 non-reciprocal links — batch close |
| t_f0fcb3dcd69d49b2 | ready | Merge: agentic-planner/reflection/sequential |

## Blockers

1. **GoodRobot** — Ty decision on canonical location (since 2026-07-29)
2. **gbrain synthesis-layer** — Ty decision on link intent (since 2026-07-29)