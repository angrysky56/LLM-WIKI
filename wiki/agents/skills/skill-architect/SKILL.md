# Skill Architecture & Generation Guide

> [!TIP]
> **TL;DR**: This skill is for creating, updating, and standardizing agent skills within this repository. Use it when you need to package new domain knowledge, build a specialized agent persona, or refactor existing documentation to follow the [Agent Skills](file:///home/ty/.gemini/antigravity/global_workflows/agent-skills.md) specification.
> **Key Action**: Follow the [Scaffolding Template](references/TEMPLATE.md) to initialize a new skill directory.

## Quick-Start Card

| Stage        | Action                                              | Standard                             |
| :----------- | :-------------------------------------------------- | :----------------------------------- |
| **Scaffold** | `scripts/scaffold.py "name" "desc"`                 | Lowercase, hyphen-only names         |
| **Draft**    | Write `SKILL.md` with YAML frontmatter              | < 500 lines (Progressive Disclosure) |
| **Optimize** | Add TL;DR and Quick-Start Card                      | Direct, "hard-edged" prose           |
| **Validate** | Run [Compliance Checklist](references/CHECKLIST.md) | No second-person, no fluff           |

## The Specification (At a Glance)

A skill is a self-contained directory following the [Agent Skills](file:///home/ty/.gemini/antigravity/global_workflows/agent-skills.md) standard.

### Directory Layout

```
skill-name/
├── SKILL.md          # Required: Entry point and instructions
├── references/       # Optional: Technical deep-dives
├── scripts/          # Optional: Executable utilities
└── assets/           # Optional: Diagrams, templates, data
```

### Frontmatter Requirements

```yaml
---
name: skill-name # lowercase-hyphen-only
description: "Use when..." # starts with trigger-ready description
---
```

## Progressive Disclosure Standard

To minimize context pollution, skills MUST use the following hierarchy:

1.  **Frontmatter**: Loaded at startup for discovery.
2.  **TL;DR + Quick-Start Card**: Immediate orientation for the agent.
3.  **Operational Instructions**: The "how-to" for the agent.
4.  **Reference Files**: Technical depth that is ONLY loaded if the agent explicitly decides to read it.

## Writing Style & Tone

- **Hard-Edged Prose**: No "helpful" or "friendly" AI tics. Use direct, imperative language.
- **No Placeholders**: provide working examples or real data.
- **Trigger-Focused**: The description should explicitly mention the symptoms, errors, or goals that require the skill.

## Advanced Capabilities

For complex skills, utilize the following patterns:

- [Template Scaffolding](references/TEMPLATE.md) — Pre-configured YAML and Markdown structure.
- [Validation Checklist](references/CHECKLIST.md) — Self-audit guide before deployment.
- [Tool Design Rules](file:///home/ty/.gemini/antigravity/skills/tool-design/SKILL.md) — If the skill introduces new tools or scripts.
