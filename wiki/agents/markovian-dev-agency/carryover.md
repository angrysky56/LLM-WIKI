## CarryoverState

### Established
- [Issue-001] 115 garbage entities, 203 generic untyped `Entity` nodes found in Synapse audit
- [Issue-001] Recent fixes didn't fully address the problem
- [Issue-002/003] Generic nodes and type correctness issues blocked on Issue-001 root cause
- [Agency] 4 specialists defined: diagnostician, fixer, ticket-writer, researcher
- [Context] Synapse = Project-Synapse MCP at ~/ai_workspace/domain-graph-orchestrator/ (Neo4j + ChromaDB)

### Open
- [Issue-001] Root cause: ingest sanitization failure? graph schema enforcement gap?
- [Issue-001] What specifically triggers the garbage entity pattern?
- [Issue-001] 18K nodes — what's the migration strategy?
- [Agency] No specialist has written carryover yet — state is fresh

### Heading
- [Intent] Diagnostician should pick up Issue-001 and continue investigation
- [Intent] Log what was tried so we don't repeat failed approaches
- [Constraint] 1500 MiniMax calls/5hr — be efficient, no wasted re-investigation

## Specialist Notes

### Diagnostician
- Should read: `wiki/synthesis/research-brief-2026-05-13.md`, `wiki/synthesis/bounded-structured-memory.md`
- Should write: active-issues/issue-001.md with findings so far
- Next step: determine root cause of garbage entity pattern

### Fixer
- Waiting on diagnostic findings
- When activated: implement fix based on issue-001.md root cause

### Ticket Writer
- Waiting for confirmed issues
- When activated: draft support ticket describing the problem + evidence

### Researcher
- Available for pattern investigation
- Can be dispatched to research ingest sanitization patterns, Neo4j schema enforcement, etc.

## Last Activation Notes

Last session worked on research-brief, found issues, but said "next activation would need to do more" — meaning the diagnostic work was incomplete. This carryover carries forward the state so the next activation knows exactly where we left off.