# Skill Scaffolding Template

Copy and paste this structure when creating a new skill.

## 1. Directory Structure

```bash
mkdir -p skills/new-skill-name/{references,scripts,assets}
```

## 2. SKILL.md Template

```markdown
---
name: new-skill-name
description: "Use when [TRIGGER]. This skill provides [VALUE]."
---

# Skill Name Title

> [!TIP]
> **TL;DR**: [Concise 1-2 sentence summary of purpose and primary tool].

## Quick-Start Card

| Concern      | Action   | Tool/Method |
| :----------- | :------- | :---------- |
| [Scenario A] | [Action] | [Tool]      |
| [Scenario B] | [Action] | [Tool]      |

## Overview

Briefly describe the domain and capability.

## Instructions

1. [Step 1]
2. [Step 2]

## Reference Files

- [Detailed Technical Guide](references/DETAILS.md)
```

## 3. Reference Template (references/DETAILS.md)

```markdown
# Detailed Reference for [Skill Name]

## Technical Specifications

[Data tables, schemas, complex logic]

## Edge Cases

[List of common failures and fixes]
```
