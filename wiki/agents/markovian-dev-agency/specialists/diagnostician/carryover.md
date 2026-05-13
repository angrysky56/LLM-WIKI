## CarryoverState

### Established
- [Issue-001] 115 garbage entities, 203 generic untyped `Entity` nodes found in Synapse audit
- [Context] Synapse = Project-Synapse MCP at ~/ai_workspace/domain-graph-orchestrator/ (Neo4j + ChromaDB)
- [Context] Bounded-structured-memory.md defines SSL schema — scheduling/structural/logical layers

### Open
- [Issue-001] Root cause unclear — was mid-investigation when session ended
- [Issue-001] What specifically triggers the garbage entity pattern?
- [Issue-001] Was working on reading research-brief and bounded-structured-memory to understand what fixes were already attempted

### Heading
- [Intent] Continue investigation of Issue-001 garbage entity root cause
- [Action] Read research-brief findings, cross-reference with bounded-structured-memory schema design
- [Action] Query Neo4j directly to understand the actual entity/relationship patterns
- [Constraint] Log failed approaches so we don't repeat them

## Last Session Notes

Session ran audit, found 115 garbage entities and 203 generic untyped nodes. Tried some fixes that didn't work. At end of session said "next activation would need to do more" — indicating investigation was incomplete. Need to figure out root cause before fixer can implement anything.

## Active Work

**File to create:** `workspace/active-issues/issue-001.md` — document root cause investigation as it progresses