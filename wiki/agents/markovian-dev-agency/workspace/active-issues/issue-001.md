---
created: 2026-05-13
updated: 2026-05-13
type: issue
priority: high
status: diagnostic-in-progress
specialist: diagnostician
---

# Issue-001: Synapse Garbage Entities

## Summary

115 garbage entities and 203 generic untyped `Entity` nodes found in Synapse graph. ~70% type correctness overall. Persistent problem — recent fixes didn't fully address it.

## Evidence

- Audit ran 2026-05-13 (research-brief session)
- 115 garbage entities: nodes without proper type labels or semantic meaning
- 203 generic untyped nodes: `Entity` label but no further distinction
- ~70% type correctness

## Root Cause Hypotheses

1. **Ingest sanitization failure** — bad content slipping through ingest pipeline
2. **Graph schema enforcement gap** — SSL schema exists in bounded-structured-memory.md but not enforced at ingest time
3. **Neo4j constraint missing** — no uniqueness/type constraints at DB level

## Attempts So Far

| Date | Attempt | Outcome |
|------|---------|---------|
| 2026-05-13 | Audit run | Found 115 garbage, 203 generic |
| 2026-05-13 | Recent fixes | Did not address everything |

## What's Needed

1. Query Neo4j directly to see actual entity/relationship patterns
2. Identify what triggers garbage pattern
3. Determine if fix is: (a) our ingest code, (b) Synapse framework config, (c) DB-level constraints
4. Design migration strategy for 18K nodes if needed

## Next Steps

- [ ] Query Neo4j for sample garbage entities
- [ ] Compare pattern against bounded-structured-memory schema
- [ ] Identify specific ingest path that produces garbage
- [ ] Document root cause

## Related Issues

- Issue-002 (generic untyped nodes) — likely same root cause
- Issue-003 (type correctness <70%) — consequence of same root cause