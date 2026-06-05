---
summary: Knowledge management — systematic approaches to capturing, organizing, and retrieving knowledge
tags: [knowledge-management, organizational-learning, knowledge-graph, zettelkasten, information-architecture]
updated: 2026-05-29T06:12:33Z
---

---
created: 2026-05-25
updated: 2026-08-10
type: concept
summary: "Knowledge management — systematic approaches to capturing, organizing, maintaining, and retrieving institutional knowledge; spans PKM, organizational learning, and knowledge graph methodologies"
tags: [knowledge-management, organizational-learning, knowledge-graph, zettelkasten, information-architecture]
sources: []
status: active
confidence: 0.75
---

# Knowledge Management

## Definition

Knowledge management (KM) is the discipline of systematically capturing, organizing, maintaining, and retrieving information and understanding — individual and organizational — so that it can be reused, built upon, and transmitted across time and context. It spans personal knowledge management (PKM), organizational knowledge management, and technical implementations like knowledge graphs and Zettelkasten.

KM asks: how do you store knowledge so that it remains accessible and useful over time, across different contexts and people?

## Relationship to PARA

The [[para]] methodology provides a concrete organizational framework within knowledge management. PARA (Projects, Areas, Resources, Archives) organizes all information into four categories:

- **Projects**: Active goals with defined outcomes and time horizons
- **Areas**: Ongoing responsibilities maintained over time
- **Resources**: Topics of ongoing interest without a commitment
- **Archives**: Inactive items from the other three categories

PARA's insight is that knowledge entropy is managed through intentional dormancy — archives serve as passive repositories that stabilize the active knowledge surface. A [[zettelkasten]] system implements PARA's principles at the note level with bidirectional linking.

## The Knowledge Graph Approach

The knowledge graph is a technical KM implementation: a directed graph where nodes are concepts or entities and edges are typed relationships. Querying the graph retrieves contextually relevant knowledge rather than keyword-matched documents. The approach is particularly powerful for AI-augmented retrieval — systems like this wiki use knowledge graphs to enable multi-hop reasoning across domains.

## Key Distinctions

| Concept | What It Is | Relationship to KM |
|---------|-----------|-------------------|
| [[zettelkasten]] | Note-linking methodology with atomic ideas | KM implementation pattern |
| [[para]] | Information organization framework | KM organizational structure |
| [[knowledge-store]] | Technical storage layer | KM infrastructure |
| [[information-architecture]] | Structural design of information systems | KM at system level |
| [[bounded-structured-memory]] | Agent memory implementation (Hermes) | KM applied to AI agents |

## Organizational KM vs PKM

**Personal KM** (PKM) focuses on individual note-taking, reading capture, and personal understanding maintenance — tools like Obsidian, Notion, and Roam.

**Organizational KM** focuses on capturing institutional knowledge — procedures, decisions, research findings — so that organizations don't repeatedly relearn the same lessons. This is more about process and culture than tooling.

Both require: selection pressure on what to keep, regular review/refinement, and connective tissue (links, tags, search) to make retrieval possible.

## Connections

- [[zettelkasten]]: The original note-linking methodology that inspired modern PKM systems
- [[para]]: Organization framework for information management
- [[knowledge-store]]: Technical storage layer for KM
- [[information-architecture]]: System-level design for information organization
- [[obsidian-cli-skill]]: Tool-level implementation of PKM principles
- [[knowledge-architecture-stub]]

## Open Questions

1. Does a knowledge graph actually improve over a flat note collection for personal KM — or does the overhead of relationship maintenance outweigh the retrieval benefits?
2. What is the right retention policy for organizational knowledge — when does "capturing everything" create more noise than signal?
3. How does sovereign AI intersect with KM? Nations that lack domestic knowledge management infrastructure may be more dependent on foreign AI systems that carry their own knowledge organization assumptions.
