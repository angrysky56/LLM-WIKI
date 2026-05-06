---
summary: GitHub Actions CI Troubleshooting guide summary.
tags: [github-actions, ci-cd, troubleshooting]
updated: 2026-05-06T20:08:46Z
created: 2026-05-06T20:08:46Z
---

---
created: 2026-05-06T20:08:41Z
updated: 2026-05-06T20:08:41Z
type: source
summary: Practical guide for debugging common GitHub Actions CI failures, including Node.js deprecations, Trunk formatting discrepancies, and linker errors.
tags: [github-actions, ci-cd, troubleshooting, node-js, trunk, prover9]
sources: Internal Documentation
status: active
confidence: 1.0
---

# GitHub Actions CI Troubleshooting

Practical guide for maintaining the project's CI pipeline integrity.

## Key Solutions

### Node.js 24 Migration
GitHub is transitioning to Node 24. To proactively resolve deprecation warnings for Node 20, set the following at the workflow top level:
```yaml
env:
  FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
```
*Note: Harmless `punycode` and `url.parse()` warnings may appear after this change; they can be safely ignored.*

### Trunk & TOML Formatting
`uv` and other package managers may format `pyproject.toml` in a way that conflicts with Trunk's `taplo` rules.
- **Fix**: Run `trunk fmt pyproject.toml` locally before committing.

### C/C++ Linker Errors (LADR/Prover9)
Linker errors like `undefined reference to 'round'` often stem from the order of flags in legacy Makefiles.
- **Fix**: Ensure `-lm` (math library) is placed at the end of the compilation string, or use provided CMake scripts.

## Connections
- Entity: [[github-actions]]
- Entity: [[trunk]]
- Entity: [[prover9]]
- Tool: [[uv]]
- Tool: [[taplo]]
