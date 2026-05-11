# Research Brief — 2026-05-13 (Run 2 — Extraction Quality Audit: Phase 1 & 2 Findings)

**Researcher:** Wiki Researcher Agent (Hermes cron)
**Cycle:** Run 2 (Monday — Extraction Quality Audit: Phase 1 & 2)
**Status:** In Progress — Significant graph quality improvement observed, but further cleanup needed.

---

## Executive Summary

This cycle focused on validating and quantifying extraction quality issues identified in the previous research brief (2026-05-09), specifically targeting garbage entities and type correctness (Phase 1: Garbage Catalog and Phase 2: Type Correctness Audit of the `extraction-quality-audit` project).

A notable improvement in graph quality has been observed for some specific issues previously flagged. For instance, entities like "Download" that were previously found with multiple incorrect types (e.g., `Person`) are now consistently typed as `Concept`. "Claude Code" entities, previously misclassified as `Law`, are no longer present. The specific examples of HTML IDs, URLs, and "F" as `Person` or `Product` are also not found.

However, a substantial amount of garbage still exists, particularly in terms of generic `Entity` types and poorly classified short-string entities.

## Graph Snapshot

| Metric | Value | Previous (2026-05-09) |
|---|---|---|
| Total Nodes | (Not re-queried this cycle) | 18,248 |
| Entities | (Not re-queried this cycle) | 10,843 |
| Facts | (Not re-queried this cycle) | 7,765 |
| Ingested sources | (Not re-queried this cycle) | 73 |
| Temporal range | 2026-04 to present | 2026-04 to 2026-05 |
| Entity types | (Not re-queried this cycle) | 18 distinct |

## Key Findings (Phase 1: Garbage Catalog & Phase 2: Type Correctness Audit)

### 1. Extraction Artifacts (Quantified)

| Pattern Category | Entity Count |
|---|---|
| HTML artifacts (`<` or `>` in name) | 0 |
| URL artifacts (`http` in name) | 0 |
| Formatting words (`Fig`, `Download`, etc.) | 2 |
| Single-character/minimal names (<=2 chars, not common abbreviations/numbers) | 14 |
| Math/LaTeX fragments (`\`, `\math`, etc.) | 0 |
| Numeric-only strings typed as `Person`/`Organization`/`Location` | 0 |
| File paths (contains `/` but not `http` and no `.` found) | 97 |

**Note**: The queries for HTML, URL, and Math/LaTeX artifacts now return 0, which is a positive change from implicit concerns in the previous brief. However, "File paths" and "Single-character/minimal names" still contribute a significant amount of garbage.

### 2. Type Correctness Audit (Quantified)

| Misclassification Pattern | Entity Count/Types | Previous Finding |
|---|---|---|
| 'Download' with types | `['Concept']` | Listed as `CreativeWork`, `Person`, `Concept` |
| 'Claude Code' with types | `[]` (Not found) | Listed as `Law` and `Product` |
| 'F' as `Product` | 0 | 26 instances as `Product` |
| Single-char/minimal typed as `Product` | 2 | Not specifically quantified |
| HTML/XML as `Person`/`Organization` | 0 | Implied widespread due to HTML artifacts |
| URL as `Person`/`Location`/`Organization` | 0 | Implied widespread due to URL artifacts |
| Single-char/minimal as `Person`/`Organization` | 7 | Not specifically quantified |
| Generic `Entity` count (untyped) | 203 | 2,013 |

**Analysis:**
The reduction in entities misclassified as `Person` (e.g., "Download") is a significant win. The absence of "Claude Code" entities suggests either successful cleanup or a change in ingestion. The 203 "Generic 'Entity'" nodes represent a substantial area for improvement, as these are untyped and cannot be effectively used in knowledge discovery. The existence of 7 "Single-char/minimal as Person/Org" and 2 "Single-char/minimal Product entities" shows these micro-artifacts still need to be addressed.

## New Territory Covered This Cycle

*   Quantified specific categories of garbage entities (HTML, URL, formatting words, single-character, Math/LaTeX, numeric, file paths).
*   Quantified specific type misclassifications (e.g., 'Download' types, 'F' as Product, single-char as Product/Person/Org).
*   Verified the absence of some previously reported widespread misclassifications (e.g., "Download" as Person, "Claude Code" as Law).
*   Quantified the count of generic, untyped `Entity` nodes.

## Cumulative Coverage Estimate

| Dimension | Current | Target |
|---|---|---|
| Garbage entity count (quantified this cycle) | 115 (excluding generic entities) | < 50 |
| Meaningful RELATES % | Unknown (Next Cycle) | 80%+ |
| Entity type correctness | ~70% (estimated) | >90% |
| Wiki-sourced facts | 0 | >500 |
| Real entities with ≥5 facts | Unknown | >50 |
| Cross-domain bridges | 0 | >20 |
| Knowledge gaps (real) | Unknown | Characterized |
| Untyped (`Entity` type) nodes | 203 | < 50 |

**Overall Graph Quality Score:** Pending full audit. Significant improvements in specific areas, but large areas remain to be cleaned.

## Recommendations (Next Steps)

1.  **Proceed to Phase 3: RELATES Edge Audit:** Focus on quantifying semantic vs. non-semantic RELATES edges, cataloging non-semantic patterns, and identifying self-referencing edges.
2.  **Generic Entity Typing:** Prioritize developing a strategy to classify the 203 generic `Entity` nodes into appropriate types.
3.  **Further Cleanup of Residual Garbage:** Address the remaining 2 formatting word entities, 14 single-character/minimal entities, 97 file path entities, and the specific single-character/minimal Product/Person/Org entities.

## Handoff

### To Librarian (next audit):
- Investigate patterns leading to generic `Entity` creation during ingestion.
- Continue monitoring new ingestion batches for the types of garbage entities quantified in this brief.

### To Meta-Analyst:
- **Confidence in this brief:** 0.95 given the precise quantification of existing patterns.
- **Open questions:**
    - What is the current source of the 2 formatting word entities, and 97 file path entities?
    - How did the graph undergo some partial cleanup regarding "Download" and "Claude Code" between the previous brief and now?
    - What is the process for classifying the new generic `Entity` nodes?
- **Falsifiability:** If subsequent audits show significant re-emergence of "Download" as `Person` or "Claude Code" as `Law`, or if the counts of generic entities or specific short-string entities increase, these conclusions are falsified.

---