---
updated: 2026-05-17T17:57:44Z
created: 2026-05-17T17:57:44Z
---

---
created: 2026-05-17T11:00:00Z
updated: 2026-05-17T11:00:00Z
type: source
summary: Paperclip API reference — company-scoped JSON API for companies, agents, issues, approvals, costs, routines, secrets, activity. Bearer token auth, Zod validation, standard error codes.
tags: [paperclip, api, rest, company, agents, issues]
sources: https://docs.paperclip.ing/#/reference/api/overview
status: reference
confidence: 0.9
---

## Core Insight

Paperclip API is a company-scoped REST API with JSON payloads, Bearer token auth, and Zod validation. Resources: companies, agents, issues, approvals, costs, routines, secrets, activity, dashboard. Error codes follow standard REST conventions (400/401/403/404/409/422/500/503).

## Key Claims

| Aspect | Detail |
|--------|--------|
| **Base URL** | `http://localhost:3100/api` |
| **Auth** | Board users: session cookie or Bearer token; Agents: `Bearer <agent...wt>` |
| **Company scoping** | Most endpoints are `/api/companies/{companyId}/...` |
| **Health** | `GET /api/health` — checks server + database |
| **Error format** | `{"error": "Human-readable message", "details": ...}` |
| **Validation** | Server-side Zod schemas → `400` on malformed payloads |

## Connections
- [[sources/repositories/paperclip]]
- [[wiki/index]]
- [[sources/documentation/paperclip-api]]
- [[paperclip-api]]

- [[paperclip]] — parent system
- [[paperclip-hermes-adapter]] — Hermes integration
- [[paperclip-company-spec]] — package format specification
