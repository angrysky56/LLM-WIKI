---
summary: O(1) deterministic knowledge retrieval via DCT-II geometric hashing + mmap — 345x faster than RAG, zero collisions
tags: [geometric-hashing, deterministic-retrieval, mojo, mmap, Nairobi_Protocol, GDE, O(1), knowledge-store, content-addressed-storage, DCT-II]
updated: 2026-05-22T19:44:50Z
---


summary: O(1) deterministic knowledge retrieval via DCT-II geometric hashing + mmap sparse files — 345x faster than RAG, zero collisions
tags: geometric-hashing, deterministic-retrieval, mojo, mmap, Nairobi_Protocol, GDE, O(1), knowledge-store, content-addressed-storage, DCT-II, RRD-Kenya



# Nairobi Protocol — Geometric Determinism Engine (GDE)

**Repository:** https://github.com/tkimingi25-spec/Nairobi_Protocol-GDE-
**Author:** Tom Kimingi — RRD Kenya
**License:** MIT
**DOI:** https://doi.org/10.5281/zenodo.20036883

## Overview

The GDE is a deterministic O(1) intermediary layer between a user, LLM, or agent and a knowledge store. Given any input key, it computes the exact byte address of the corresponding knowledge chunk and retrieves it directly via mmap. No scanning. No approximation. No training.

**This is not a vector database.** It does not search for similar vectors. It computes an exact deterministic address and jumps directly there. It is a **content-addressed storage engine** — a specialized hash table written to disk.

## Core Hash: DCT-II (Type-II Discrete Cosine Transform)

The hash function is a **Type-II DCT** applied to character byte values — the same math behind JPEG compression and audio fingerprinting. Not hand-waving, well-established signal processing.

```
Input:  first 32 bytes of lowered text → 32-byte signal
DCT-II: 24-dimensional float64 vector
Offset: Σ(|vi| × wi) mod AddressSpace,  wi = (i+1) × 2654435761 (Knuth multiplicative)
Slot:   (raw_offset // SLOT_SIZE) * SLOT_SIZE
```

| Property | Value |
|
|
|
| Hash dimensions | 24D float64 |
| Input signal | 32 bytes (first N chars of lowered text) |
| Determinism | Byte-level exact across different hardware |
| Speed | 48,451 queries/sec (20.64μs/hash+seek) |
| Collision rate (10K synthetic) | 0% |

**Warning at scale:** Address space is 100GB ÷ 256B slots ≈ 419M slots. Birthday paradox says collisions become likely past ~28K entries in a perfectly uniform hash. Real-world keys (multi-word titles, paragraphs) may cluster through DCT. **No collision resolution strategy exists yet** — collisions silently overwrite.

## Architecture

```
User / LLM / Agent
       |
       | input key
       v
universal_geometric_hash()     24D HashVector     phonological.mojo
       |  DCT-II
       v
coordinate_to_offset()         byte address       coordinate_bridge.mojo
       |  Σ(|vi| × wi) mod space
       v
mmap seek + read               exact knowledge    knowledge_store.bin
       |  sparse file, ext4-backed
       v
Knowledge chunk returned in O(1)
```

## Key Results (WSL2 Ubuntu, 1M queries)

| Metric | Value |
|
|
|
| Hash + offset + seek | 20.64μs |
| Full retrieval (+ 256B read) | 20.99μs |
| Queries/sec | 47,620 |
| Collision rate (10K words) | 0% |
| Speed vs RAG | 345x faster (claimed) |
| Cross-hardware (4GB vs 16GB) | Byte-level exact match |

## What It Actually Is

A **content-addressed storage engine** — deterministic O(1) key→value retrieval in a sparse file. Useful for:

- **Cache layer for LLM tool results** — store tool outputs at deterministic addresses so the same query never hits the tool twice
- **Offline knowledge base with known, enumerated keys** — dictionary, manual, FAQ
- **Deterministic audit trail** — every piece of stored knowledge has a provable, reproducible address

Where it won't work as described:
- Replacing vector databases (no similarity/approximate search)
- Open-ended natural language retrieval (no fuzzy matching — exact key or miss)
- Dynamic document stores at scale without collision handling

## Critical Gaps (from technical audit)

1. **No collision resolution** — at 100K+ entries, collisions likely. Silent overwrite is catastrophic.
2. **Exact-match only** — `"neural network architecture"` works; `"deep learning architectures"` misses entirely. For LLM integration: need a canonicalization layer or key catalog to map queries to stored keys.
3. **No metadata, no chunking** — 256B fixed slots, no source/timestamp/chunk-index, no deletion.
4. **No semantic retrieval** — the system cannot answer `"what is a neural network?"` — only `"neural network architecture"` if that exact key was stored.

## Project Structure

```
src/
  0_refinery/          Python: ontology_parser.py, contrast_lca.py (semantic layer)
  1_gateway/           Mojo: phonological.mojo (DCT hash), spectral.mojo, wavelet.mojo, persistence.mojo
  2_execution/         Mojo: coordinate_bridge.mojo (offset formula), atlas_manager.mojo, logic_kernels.mojo
  gde/                 [planned] Python canonical engine for MCP/CLI
data/                  benchmark data, knowledge_base.json (orphaned — nothing reads it)
docs/                  DEPLOYMENT.md, implementation_plan.md, analysis_results.md
tests/                 phonological_seed.mojo, collision benchmarks
```

## Implementation Plan (proposed)

- **Phase 1:** Canonical Python engine (hasher + store + manifest with FTS5) — single source of truth
- **Phase 2:** Document ingestion (chunking, key generation, slot chaining for >256B)
- **Phase 3:** MCP server with 4 tools: `gde_store`, `gde_retrieve`, `gde_list_keys`, `gde_search_keys`
- **Phase 4:** CLI wrapper

Key design decisions flagged for review:
- Hash dimensions: 24D (Mojo) vs 8D (Python reference) — recommend **24D with proper DCT-II scaling + L2 normalization**
- Slot size: fixed 256B vs variable-length with length header
- Collision strategy: linear probing with max probe count

## Absorbed Concepts

- **DCT-II as deterministic signal hash** — legitimate, not ad-hoc. Could be used elsewhere.
- **Sparse file mmap for huge virtual address space** — minimal physical storage, O(1) seeks
- **Knuth multiplicative hash for coordinate → offset mapping** — well-known technique
- **Content-addressed storage as LLM cache layer** — deterministic, reproducible, auditable

## Related

- [[geometric-hashing]] — core technique
- [[knowledge-store]] — retrieval patterns
- [[mojo-language]] — implementation language
- [[content-addressed-storage]] — the actual primitive this implements
