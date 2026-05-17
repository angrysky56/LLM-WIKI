---
updated: 2026-05-17T17:57:45Z
created: 2026-05-17T17:57:45Z
---

---
created: 2026-05-17T11:00:00Z
updated: 2026-05-17T11:00:00Z
type: source
summary: Agent Company spec — filesystem/GitHub-native format using markdown+yaml for company/team/agent/project/task packages, extending the Agent Skills SKILL.md model.
tags: [paperclip, spec, company, team, agent, package-format]
sources: (unknown — file from raw/)
status: reference
confidence: 0.85
---

## Core Insight

Agent Company (agentcompanies/v1-draft) is a vendor-neutral filesystem and GitHub-native format for describing companies, teams, agents, projects, and tasks using markdown files with YAML frontmatter. Extends the existing Agent Skills `SKILL.md` model rather than replacing it. Key principle: Markdown is canonical, Git repos are valid package containers, registries are optional discovery layers.

## Key Claims

| Package Kind | Root File |
|-------------|-----------|
| Company | `COMPANY.md` |
| Team | `TEAM.md` |
| Agent | `AGENTS.md` |
| Project | `PROJECT.md` |
| Task | `TASK.md` |
| Skill | `SKILL.md` |

Reserved files: `COMPANY.md`, `TEAM.md`, `AGENTS.md`, `PROJECT.md`, `TASK.md`, `SKILL.md`, `.paperclip.yaml`, `HEARTBEAT.md`, `SOUL.md`, `TOOLS.md`.

## Connections

- [[paperclip]] — Paperclip is the runtime for Agent Companies
- [[agent-skills-spec]] — Agent Skills spec that this extends
