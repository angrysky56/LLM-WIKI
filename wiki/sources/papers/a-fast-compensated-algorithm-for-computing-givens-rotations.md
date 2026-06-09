---
summary: Fast compensated algorithm for computing Givens rotations with improved numerical accuracy via error compensation techniques. Numerical Analysis (math.NA).
tags: [numerical-analysis, linear-algebra, givens-rotations, compensated-algorithms, mixed-precision]
updated: 2026-06-09T18:47:50Z
created: 2026-06-09T18:47:50Z
---

# A Fast Compensated Algorithm for Computing Givens Rotations

**arXiv:2406.02750** — Numerical Analysis (math.NA)

Author: Carlos F. Borges (June 2024)

## Summary

This paper presents a fast compensated algorithm for computing Givens rotations, a fundamental operation in numerical linear algebra used in QR decompositions and other matrix factorizations. The compensated approach improves numerical accuracy by applying error compensation techniques to the standard Givens rotation computation, achieving higher precision without significantly increasing computational cost. The algorithm is designed to be backward stable and provides near double-precision accuracy using only single-precision arithmetic in key computational steps.

## Key Contributions

- A novel fast compensated Givens rotation algorithm
- Error analysis demonstrating backward stability
- Performance comparisons showing improved accuracy over standard approaches
- Applicable to modern hardware where mixed-precision computation is efficient

## Connections

- [[numerical-linear-algebra]] — Core domain
- [[qr-decomposition]] — Primary application area
- [[mixed-precision-computation]] — Related methodology
