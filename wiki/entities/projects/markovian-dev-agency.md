---
created: 2026-05-13
updated: 2026-05-13
type: entity
subtype: project
summary: Dev agency with 4 specialists that maintains persistent Markovian state across activations
tags: [agency, devops, markovian, persistent-agents, multi-specialist]
status: active
confidence: 0.9
sources: raw/paperclip Open-source orchestration for zero-human companies.md
---

# Markovian Dev Agency

Multi-specialty autonomous dev organization inspired by Paperclip's "zero-human company" model. Runs on Hermes with persistent Markovian carryover across activations.

## Structure

```
markovian-dev-agency/
├── soul.md              # Agency identity + principles
├── user.md              # Ty's preferences + project context
├── now.md               # Master state (active issues, specialist coordination)
├── carryover.md         # Markovian forward-state
├── specialists/         # Four operational specialists
│   ├── diagnostician/   # Root-cause analysis
│   ├── fixer/           # Code changes
│   ├── ticket-writer/   # Support tickets + docs
│   └── researcher/      # Pattern research
└── workspace/           # Shared operational space
    ├── active-issues/    # Issue tracking files
    ├── logs/            # Activity audit trail
    └── tickets/         # Draft support tickets
```

## Specialties

| Specialist | Function |
|------------|----------|
| **Diagnostician** | Root-cause analysis, issue investigation |
| **Fixer** | Code changes, refactoring, implementation |
| **Ticket Writer** | Support tickets, issue reports, documentation |
| **Researcher** | Technical research, patterns, solutions |

## Activation Protocol

1. Read `now.md` + `carryover.md` (master state)
2. Read all specialist carryovers (see who's doing what)
3. Assess `active-issues/` — what's blocked, ready, or new
4. Dispatch work to specialists via `delegate_task`
5. Synthesize results → update `now.md` + `carryover.md`
6. Report to board (Ty)

## Current Issues

- **Issue-001:** 115 garbage entities, 203 generic untyped nodes (~70% type correctness)
- **Issue-002/003:** Blocked on Issue-001 root cause

## Connections

- [[markovian-carryover]] — protocol
- [[bounded-structured-memory]] — architecture
- [[hermes-agent]] — execution framework
- [[paperclip]] — inspiration source