# insights — Creating Wiki Pages from Insights

## Threshold Rule

Only create wiki pages for insights with `confidence >= 0.7`.

Lower-confidence insights should be noted in carryover but not given full pages.

## Slug Mapping

Transform insight titles into URL-safe slugs:

| Insight Title | Slug |
|---------------|------|
| Titans Memory Architecture | `titans-memory-efficiency-insight` |
| Reward Model Overestimation | `reward-model-overestimation-insight` |
| Cross-Task Generalization Gap | `cross-task-generalization-gap-insight` |

**Rules:**
- Lowercase
- Replace spaces with hyphens
- Remove apostrophes and special characters
- Append `-insight` suffix

## Frontmatter Template

```yaml
---
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: synthesis
summary: {one-line summary from insight title}
tags: [insights, zettelkasten, {topic}]
sources: [{evidence sources from insight.json}]
status: active
confidence: {confidence score from insight}
---
```

## Page Body Structure

```markdown
# {Insight Title}

## Insight
{insight content / main finding}

## Evidence
- {evidence chain item 1}
- {evidence chain item 2}
- {evidence chain item 3}

## Connections
- [[scratchpad/agent-sheets/insights/references/insight-merge]]
- [[index]]
- [[insight-merge]]
- [[related-concept-1]]
- [[related-concept-2]]

## Open Questions
- {questions raised by this insight}
```

## Tag Conventions

Always include: `insights`, `zettelkasten`
Add topic-specific tag: `memory`, `reward-modeling`, `generalization`, etc.