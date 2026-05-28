---
summary: 63-skill inventory with categories, descriptions, and connection links
tags: [hermes-agent-skills, agent-framework, skills-inventory, configured-skills]
updated: 2026-05-27T05:45:09Z
---

# Hermes Agent Skills

*Configured skill repertoire for this Hermes Agent instance — 64 skill directories, 33 with active SKILL.md content.*

## Skills Inventory

### Agentic & Orchestration
| Skill | Description |
|---|---|
| `autonomous-ai-agents` | Spawning and orchestrating autonomous AI coding agents and multi-agent workflows |
| `handoff` | Compact the current conversation into a handoff document for another agent |
| `meta-harness-domain-bootstrapping` | Bootstrap a new meta-harness domain from domain_spec.md through Phase 0 |
| `meta-meta-process` | Meta-cognitive process for recursive self-improvement |
| `wiki-overseer` | Monitor agent carryovers, maintain central jobs sheet, assign cross-agent tasks |

### Code & Development
| Skill | Description |
|---|---|
| `ai-cli` | Modern CLI tools (rg, fd, ast-grep, jq, tokei, delta, hyperfine) via LocalREPL shell bridge |
| `codegraph` | Local code intelligence via tree-sitter AST graph and MCP tools |
| `diagnose` | Disciplined diagnosis loop: Reproduce → minimise → hypothesise → instrument → fix |
| `git-guardrails-claude-code` | Block dangerous git commands (push, reset --hard, clean) before execution |
| `improve-codebase-architecture` | Find deepening opportunities, refactoring paths, testability improvements |
| `migrate-to-shoehorn` | Migrate `as` type assertions to @total-typescript/shoehorn |
| `prototype` | Throwaway prototypes: terminal apps for state questions, or UI variations |
| `review` | Two-axis code review: Standards + Spec, run in parallel sub-agents |
| `scaffold-exercises` | Create exercise directory structures with sections, problems, solutions |
| `setup-matt-pocock-skills` | Set up agent skills block in AGENTS.md and docs/agents/ |
| `setup-pre-commit` | Husky pre-commit hooks with lint-staged, type checking, tests |
| `software-development` | General software development patterns |
| `tdd` | Test-driven development with red-green-refactor loop |
| `to-issues` | Break plans/PRDs into independently-grabbable issues via tracer-bullet slices |
| `to-prd` | Turn conversation context into a PRD and publish to issue tracker |
| `triage` | Triage issues through a state machine driven by triage roles |
| `zoom-out` | Zoom out for broader context or higher-level perspective |

### Creative & Writing
| Skill | Description |
|---|---|
| `creative` | Creative content generation — ASCII art, diagrams, visual design |
| `edit-article` | Edit and improve articles by restructuring and tightening prose |
| `writing-beats` | Shape an article as a journey of beats, choose-your-own-adventure style |
| `writing-fragments` | Mine the user for fragments and append to a raw material document |
| `writing-shape` | Shape raw material into an article through conversational drafting |

### Research & Knowledge
| Skill | Description |
|---|---|
| `research` | Academic research, paper discovery, literature review |
| `knowledge-management` | Knowledge management workflows |
| `graphify` | Any input → knowledge graph → clustered communities → HTML + JSON + audit |
| `note-taking` | Note taking with Obsidian vault integration |
| `obsidian-vault` | Search, create, manage notes with wikilinks and index notes |
| `hindsight-docs` | Complete Hindsight documentation for AI agents |

### ML/AI & Data
| Skill | Description |
|---|---|
| `mlops` | Machine Learning Operations — training, fine-tuning, deployment, optimization |
| `data-science` | Data science workflows — interactive exploration, Jupyter, analysis, visualization |

### GitHub & Collaboration
| Skill | Description |
|---|---|
| `github` | GitHub workflow: PR lifecycle, code review, issues, CI/CD via gh CLI |

### Productivity & Tools
| Skill | Description |
|---|---|
| `productivity` | Document creation, presentations, spreadsheets workflows |
| `agent-sheets` | Google Sheets integration via agent-sheets |
| `email` | IMAP/SMTP email from terminal via himalaya |
| `gsd` | "Get Shit Done" productivity system |

### Platform & Integration
| Skill | Description |
|---|---|
| `mcp` | MCP (Model Context Protocol) servers, tools, and integrations |
| `smart-home` | Control smart home devices — lights, switches, sensors, automation |
| `social-media` | X/Twitter, Yuanbao group interactions |
| `media` | YouTube transcripts, GIF search, music generation, audio visualization |
| `gaming` | Game server setup, modpacks, Minecraft server hosting |
| `apple` | Apple platform integrations |
| `seg-soul` | SEG-based soul architecture and sub-agent replicants for Hermes personality |

### Ops & Debugging
| Skill | Description |
|---|---|
| `devops` | DevOps — webhook subscriptions, kanban orchestration, container supervision |
| `kanban` | Kanban workflow — pitfall examples, retry diagnostics, edge cases |

### Input/Validation Only (no SKILL.md)
`autonomous-ai-agents`, `apple`, `creative`, `data-science`, `devops`, `diagramming`, `domain`, `email`, `engineering`, `gaming`, `gifs`, `gsd`, `inference-sh`, `in-progress`, `kanban`, `knowledge-management`, `mcp`, `media`, `misc`, `mlops`, `note-taking`, `personal`, `productivity`, `red-teaming`, `research`, `smart-home`, `social-media`, `software-development`

## Connections
- [[index]]
- [[concepts/hermes-agent-skills]]
- [[sources/documentation/automate-anything-with-cron]]
- [[log]]
- [[hermes-agent-skills]]

- [[hermes-agent]] — parent concept
- [[autonomous-ai-agents]] — autonomous AI agents skill; multi-agent orchestration parent
- [[kanban]] — kanban workflow skill with lifecycle documentation

## Notes

- 31 skills have `SKILL.md` with actual description/content
- 33 skills lack `SKILL.md` and are only directory-placeholders
- Skill directory: `~/.hermes/skills/`
- Active skills loaded per-profile from `~/.hermes/profiles/<profile>/skills/`
- Bundled manifest: `~/.hermes/skills/.bundled_manifest` (25507 bytes as of 2026-05-26)
