---
type: cross-agent-contract
applies_to: all wiki agents
last_updated: 2026-06-06
---

# Kanban Coordination Contract

All wiki agents share one kanban database at `~/.hermes/kanban.db`. There is no per-profile kanban — cross-agent visibility is the whole point.

## Reading your queue

Every agent's first action at the start of a cycle is to drain the cards assigned to it:

```
kanban_list(lane="ready", assignee="<your-profile>")
```

Profile names: `overseer`, `librarian`, `librarians-assistant`, `researcher`, `arxiv`, `news`, `ingest`, `insights`.

If the queue is empty, that's normal — most cycles the queue is empty. The system works because cards exist at the *moments* one agent identifies work for another, not as a steady stream.

## Updating a card

When you start a card:

```
kanban_update(task_id=<id>, status="in_progress", lane="in_progress")
```

When you finish (success):

```
kanban_update(task_id=<id>, status="done", lane="done")
```

When you can't finish (out of scope, need human, etc.):

```
kanban_update(task_id=<id>, status="blocked", reason="<one-line>")
```

## Creating cards (for OTHER agents)

Only the Overseer normally creates cross-agent cards. If you find work that belongs to a different agent:

```
kanban_create(
    title="...",
    description="...",
    priority="medium",       # low | medium | high | urgent
    tenant="<target_profile>",  # THIS is the routing key
    lane="triage",          # leave unrouted for the Overseer
    assignee=null,
    intent="<verb>",        # promote-stub, verify-claim, fetch-paper, etc.
    source_agent="<your-profile>",
)
```

**The `tenant` field is required.** Omitting it makes the card land in YOUR own queue, where no other agent will ever look. The Overseer's last run hit this bug four times.

If you're sure of the routing (e.g. you know it's for the librarian), use `lane="ready", assignee="librarian"` to skip triage.

## Intents (routing table summary)

| Intent | Routes to |
|--------|-----------|
| `promote-stub`, `verify-claim`, `re-cluster`, `cross-link` | `librarian` |
| `find-sources`, `verify-citation`, `re-research`, `cross-domain-bridge` | `researcher` |
| `fetch-paper`, `check-arxiv`, `index-paper` | `arxiv` |
| `daily-news`, `breaking-story`, `verify-event` | `news` |
| `process-inbox`, `ingest-url`, `defuddle` | `ingest` |
| `cluster-pages`, `find-insight`, `gap-analysis` | `insights` |
| `merge-candidates`, `archive-page`, `fix-wikilink` | `librarians-assistant` |

When in doubt: `lane="triage", assignee=null, intent=<closest verb>`. The Overseer routes the rest.

## The Overseer's role

The Overseer is the ONLY agent that:
1. Runs the daily cross-agent coordination report
2. Has the routing table (this file) loaded every cycle
3. Resolves `triage`-lane cards by setting `assignee` and moving to `ready`
4. Surfaces "stuck" cards to a wiki page for human review

If you're an agent and you have a card that's been in `triage` for >24h with no movement, escalate via a new card back to the Overseer with `intent="re-route-stuck"`.
