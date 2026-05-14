# Skill Validation Checklist

Run this checklist before finalizing a new skill.

## 1. Compliance (Agent Skills Spec)

- [ ] Directory name is lowercase-hyphen-only.
- [ ] Directory name exactly matches `name:` in frontmatter.
- [ ] `SKILL.md` is the entry point file.
- [ ] Frontmatter contains both `name` and `description`.
- [ ] Description is trigger-focused (starts with "Use when...").

## 2. Progressive Disclosure

- [ ] `SKILL.md` is under 500 lines.
- [ ] Contains a `> [!TIP]` TL;DR block at the top.
- [ ] Contains a `## Quick-Start Card` table.
- [ ] Dense technical reference material is moved to `references/`.

## 3. Style & Quality

- [ ] No second-person ("you should", "you can"). Use imperative ("Load", "Run").
- [ ] No "helpful assistant" fluff or filler phrases.
- [ ] All file links use absolute paths (or relative paths correctly).
- [ ] No generic names (e.g., `utility`, `helper`). Use descriptive gerunds or nouns.

## 4. Integration

- [ ] Skill is discoverable (description contains relevant keywords).
- [ ] Links to related skills are included where appropriate.
- [ ] `scripts/` are executable and well-documented if present.
