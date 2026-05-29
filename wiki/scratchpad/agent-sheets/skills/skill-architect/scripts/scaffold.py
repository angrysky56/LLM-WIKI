#!/usr/bin/env python3
"""
Script to scaffold a new agent skill.
Usage: python skills/skill-architect/scripts/scaffold.py "skill-name" "description"
"""
import os
import sys
import argparse

def create_skill(name, description):
    # Normalize name
    name = name.lower().replace(' ', '-')
    skill_dir = f"skills/{name}"

    if os.path.exists(skill_dir):
        print(f"Error: Skill directory '{skill_dir}' already exists.")
        sys.exit(1)

    # Create directories
    os.makedirs(f"{skill_dir}/references", exist_ok=True)
    os.makedirs(f"{skill_dir}/scripts", exist_ok=True)
    os.makedirs(f"{skill_dir}/assets", exist_ok=True)

    # Create SKILL.md
    skill_md_content = f"""---
name: {name}
description: "{description}"
---

# {name.replace('-', ' ').title()}

> [!TIP]
> **TL;DR**: [Concise summary of purpose and primary tool].

## Quick-Start Card
| Concern | Action | Tool/Method |
| :--- | :--- | :--- |
| [Scenario A] | [Action] | [Tool] |

## Overview
Detailed purpose and scope.

## Instructions
1. Step 1
2. Step 2

## Reference Files
- [Detailed Reference](references/REFERENCE.md)
"""

    with open(f"{skill_dir}/SKILL.md", 'w', encoding='utf-8') as f:
        f.write(skill_md_content)

    # Create an empty reference file
    with open(f"{skill_dir}/references/REFERENCE.md", 'w', encoding='utf-8') as f:
        f.write(f"# Detailed Reference for {name.replace('-', ' ').title()}\n\nAdd technical depth here.")

    print(f"Skill '{name}' created successfully in '{skill_dir}'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scaffold a new agent skill.")
    parser.add_argument("name", help="Kebab-case name of the skill")
    parser.add_argument("description", help="Description for the skill (trigger-focused)")

    args = parser.parse_args()
    create_skill(args.name, args.description)
