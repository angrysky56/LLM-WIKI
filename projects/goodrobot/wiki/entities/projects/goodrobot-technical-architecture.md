# GoodRobot — Technical Architecture Overview

**Prepared by:** CTO Agent
**Date:** May 2026
**Reference:** GOO-27

---

## 1. System Architecture

### 1.1 Core Components

GoodRobot's platform consists of four primary subsystems:

```
┌─────────────────────────────────────────────────────────┐
│                    Agent Runtime                         │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌─────────┐ │
│  │ Sales    │  │ Finance  │  │ Ops      │  │ Marketing│ │
│  │ Agent    │  │ Agent    │  │ Agent    │  │ Agent   │ │
│  └──────────┘  └──────────┘  └──────────┘  └─────────┘ │
└───────────────────────┬─────────────────────────────────┘
                        │
┌───────────────────────▼─────────────────────────────────┐
│              Task Routing Engine                          │
│  Priority Queue │ Dead Letter Queue │ Retry Manager       │
└───────────────────────┬─────────────────────────────────┘
                        │
┌───────────────────────▼─────────────────────────────────┐
│           Memory / Context System                        │
│  Short-term (session) │ Long-term (vector store)         │
└───────────────────────┬─────────────────────────────────┘
                        │
┌───────────────────────▼─────────────────────────────────┐
│              Integration Layer                           │
│  Slack │ Email │ Webhooks │ API Gateway                  │
└─────────────────────────────────────────────────────────┘
```

**1. Agent Runtime** — Manages agent lifecycle: instantiation, role configuration, heartbeat, and task execution. Each agent is a sandboxed process with a defined role system prompt and tool access policy.

**2. Task Routing Engine** — Receives tasks from external triggers (webhooks, API, scheduler) and routes them to the correct agent based on task type, priority, and agent availability. Backed by a persistent queue (Redis or RabbitMQ).

**3. Memory / Context System** — Two-tier: short-term session memory (Redis, TTL-based) for active conversation context; long-term memory via vector store (Pinecone or Weaviate) for company knowledge, past interactions, and learned preferences.

**4. Integration Layer** — Pluggable adapters for Slack, email, webhooks, and external APIs. Adapters normalize incoming events into canonical task objects.

### 1.2 Data Flow

```
External Event (Slack webhook, API call, scheduler)
    │
    ▼
API Gateway (auth, rate limit, normalize)
    │
    ▼
Task Routing Engine (classify → priority → route)
    │
    ▼
Agent Runtime (instantiate agent, inject context)
    │
    ▼
Agent executes with memory access
    │
    ▼
Result → Integration Layer → External System
```

---

## 2. Technology Stack

| Layer | Technology |
|---|---|
| **Runtime** | Node.js (agent processes), Python (AI inference) |
| **API Server** | FastAPI (Python) or Express (Node.js) |
| **Message Queue** | Redis Streams (primary), BullMQ (job queue) |
| **Database** | PostgreSQL (relational), Neo4j (knowledge graph) |
| **Vector Store** | Pinecone or Weaviate |
| **Cache / Session** | Redis |
| **Infrastructure** | Docker + Kubernetes (self-hosted), or Vercel/Railway (lightweight) |
| **AI Inference** | OpenAI API (primary), Anthropic (fallback), local Llama.cpp for on-prem |
| **Auth** | API keys + JWT, OAuth2 for third-party integrations |
| **Monitoring** | Prometheus + Grafana, Sentry (errors) |

---

## 3. Agent Runtime Design

### 3.1 Agent Lifecycle

1. **Instantiation** — Agent process spawns with a role system prompt, tool definitions, and memory store.
2. **Configuration** — Role defines: permissions, available tools, communication channels, heartbeat interval.
3. **Heartbeat** — Every 300 seconds (configurable), agent sends a heartbeat to the runtime indicating liveness. Missed heartbeats trigger a recovery action (reschedule tasks, alert, respawn).
4. **Task Execution** — Agent polls or receives tasks, executes with context, writes results to memory and outputs to integration layer.
5. **Termination** — On shutdown, agent persists state to long-term memory before exit.

### 3.2 Role System

Each agent is assigned a **Role** which defines:
- **System prompt** (personality, domain expertise, behavioral guardrails)
- **Tool permissions** (what APIs/tools the agent can invoke)
- **Channel access** (which integrations the agent uses — e.g., Slack, email)
- **Priority weighting** (how tasks of different types are weighted)

Example Role schema:
```
Role: Sales Discovery Agent
  System Prompt: "You are a consultative sales agent..."
  Tools: [WebSearch, CRM_Read, Website_Scrape, Calendar_Write]
  Channels: [Slack, Email]
  Heartbeat Interval: 300s
```

### 3.3 Multi-Agent Coordination

For complex workflows (e.g., pre-call research → gap analysis → pitch prep), agents communicate via a shared task context. The routing engine supports **chained tasks** where output of Agent A is automatically fed to Agent B as input.

---

## 4. API Design

### 4.1 Core REST Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/agents` | List all agents |
| `GET` | `/agents/:id` | Get agent details |
| `POST` | `/agents/:id/tasks` | Create a task for an agent |
| `GET` | `/tasks` | List tasks (filterable by status, agent, date) |
| `GET` | `/tasks/:id` | Get task details |
| `PATCH` | `/tasks/:id` | Update task status |
| `POST` | `/workflows` | Create a multi-step workflow |
| `GET` | `/workflows/:id` | Get workflow status |
| `POST` | `/customers` | Register a customer/tenant |
| `GET` | `/customers/:id` | Get customer details |
| `POST` | `/api-keys` | Create an API key for a customer |

### 4.2 Authentication

- **API Keys** — Per-customer keys, passed as `Authorization: Bearer <key>` header. Rate-limited per key.
- **OAuth2** — For third-party integrations (e.g., connecting a customer's Slack workspace).
- **JWT** — Internal service-to-service authentication, short-lived tokens.

### 4.3 Rate Limiting

- Per API key: 100 requests/minute (standard), 1000 requests/minute (enterprise).
- Global circuit breaker on the AI inference layer (max 50 concurrent completions).

---

## 5. Data Model

### 5.1 Key Entities

```
Customer
  id, name, plan (free/pro/enterprise), api_key_hash,
  created_at, settings (JSON)

Agent
  id, customer_id, role, name, status (active/inactive),
  config (JSON), created_at, last_heartbeat_at

Role
  id, name, system_prompt, tools (JSON), permissions (JSON)

Task
  id, agent_id, workflow_id, type, input (JSON),
  output (JSON), status (pending/running/done/failed),
  priority, created_at, started_at, completed_at

Workflow
  id, customer_id, name, steps (JSON array of task configs),
  status, created_at

Memory
  id, agent_id, customer_id, type (short_term/long_term),
  content, embedding (vector), created_at, expires_at

Integration
  id, customer_id, type (slack/email/webhook), config (JSON),
  status (active/inactive)
```

### 5.2 Relationships

- Customer has many Agents
- Agent has one Role
- Agent processes many Tasks
- Workflow contains many Tasks (ordered)
- Customer has many Integrations
- Memory is scoped to Agent + Customer

---

## 6. Integration Layer

### 6.1 Slack Integration

- **Event subscription** — GoodRobot registers as a Slack app. Incoming events (mention, DM) are normalized into Task objects.
- **Outgoing** — Agent responses are posted back via `chat.postMessage`.
- **Auth** — OAuth2 flow to install the Slack app into a workspace.

### 6.2 Email Integration

- **Inbound** — Email via SendGrid/AWS SES webhook → normalized to Task.
- **Outbound** — Agent composes email; sent via SMTP or API.
- **Threading** — Email threads tracked by `references` header for context continuity.

### 6.3 Webhooks

- Generic inbound webhook endpoint: `POST /webhooks/inbound`
- Events are tagged with integration ID and customer ID; routed to task engine.
- Outbound webhooks: agent triggers `POST` to customer-defined URLs with signed payloads.

### 6.4 Trigger → Task Mapping

| Trigger | Task Type | Routing |
|---|---|---|
| Slack message @agent | `discovery_call` | Sales Agent |
| Email to agent address | `email_response` | Assigned Agent |
| Scheduled cron | `report_generation` | Ops Agent |
| Webhook from CRM | `lead_enrichment` | Sales Agent |
| API call | `custom_task` | Specified Agent |

---

## 7. Security Model

### 7.1 Tenant Isolation

- **Database** — Row-level security (RLS) in PostgreSQL. All queries scoped by `customer_id`.
- **Memory** — Vector store namespaces each customer separately.
- **Agent processes** — Sandboxed containers per customer for enterprise plans; shared process with strict memory scoping for multi-tenant SaaS.
- **API keys** — Stored as bcrypt hashes; never logged or returned in responses.

### 7.2 Data Encryption

- **In transit** — TLS 1.3 on all endpoints.
- **At rest** — AES-256 for PostgreSQL, Redis, and vector store.
- **AI data** — Prompt/response data not stored by default; optional opt-in for training.

### 7.3 Access Control

- Customer-level: API key scopes (read-only, read-write, admin).
- Role-level: Agents have constrained tool access based on Role permissions.
- Integration-level: OAuth tokens stored encrypted; refresh tokens rotated.

---

## 8. Scalability

### 8.1 Horizontal Scaling

```
                    ┌─────────────────┐
                    │  Load Balancer   │
                    └────────┬────────┘
         ┌──────────────────┼──────────────────┐
         │                  │                  │
    ┌────▼────┐        ┌────▼────┐        ┌────▼────┐
    │ API Pod │        │ API Pod │        │ API Pod │
    └────┬────┘        └────┬────┘        └────┬────┘
         │                  │                  │
    ┌────▼──────────────────▼──────────────────▼────┐
    │              Redis Streams / RabbitMQ          │
    │         (Task Queue — partitioned by tenant)   │
    └────┬──────────────────┬──────────────────┬────┘
         │                  │                  │
    ┌────▼────┐        ┌────▼────┐        ┌────▼────┐
    │ Agent   │        │ Agent   │        │ Agent   │
    │ Worker  │        │ Worker  │        │ Worker  │
    │ (Sales) │        │ (Ops)   │        │ (Fin)   │
    └─────────┘        └─────────┘        └─────────┘
```

- **Stateless API pods** — Scale behind load balancer; no sticky sessions.
- **Agent workers** — Consume from shared queue; each worker is a separate process/container. Workers are partitioned by role type for isolation.
- **Redis Streams** — Acts as both queue and pub/sub. Task priority handled via stream consumer groups.
- **AI inference pooling** — Connection pool to OpenAI/Anthropic; rate limiter prevents token burst.

### 8.2 Message Queue Architecture

- **Primary queue** — Per-customer partitioned streams. Ensures one customer's tasks don't starve another's.
- **Dead letter queue** — Failed tasks after 3 retries go to DLQ for manual inspection.
- **Priority tiers** — `critical` (immediate), `high` (within 5 min), `normal` (best effort).

### 8.3 Stateless Agent Design

Agents maintain no internal state between tasks. All context is:
1. Passed at task dispatch time (input JSON).
2. Retrieved from memory store (short-term Redis, long-term vector).

This allows any agent worker to handle any task of its role type — enabling true horizontal scale without session affinity.

---

## 9. Roadmap Alignment (Reference: GOO-3)

| Phase | Timeline | Key Architecture Deliverables |
|---|---|---|
| **MVP** | 30 days | Single-tenant, 5 agent roles, basic routing, Redis queue, PostgreSQL, Slack integration |
| **Growth** | 90 days | Multi-tenant (RLS), 20+ roles, self-serve onboarding, vector memory, webhook integrations |
| **Scale** | 180 days | Multi-agent workflows (chained tasks), Kubernetes orchestration, enterprise SSO, custom role builder |

---

## 10. Key Architecture Decisions

| Decision | Choice | Rationale |
|---|---|---|
| Agent sandboxing | Docker containers per agent | Strong isolation; enables per-customer billing at enterprise tier |
| Task queue | Redis Streams | Native priority, consumer groups,持久化, low ops overhead |
| Memory | Two-tier (Redis + Pinecone) | Speed + semantic search without hot-path dependency on AI |
| API framework | FastAPI | Native async, Pydantic validation, OpenAPI auto-docs |
| Knowledge graph | Neo4j | Captures agent-task-company relationships for explainability |
| AI inference | OpenAI primary + Anthropic fallback | Reliability + cost flexibility |

---

*Document version: 1.0 — CTO Agent, GoodRobot*
