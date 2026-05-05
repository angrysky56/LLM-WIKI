---

name: github-actions-troubleshooting

description: "Use when debugging GitHub Actions CI pipeline failures, especially related to Node.js deprecation warnings or Trunk formatting errors."

---

  

# GitHub Actions CI Troubleshooting

  

## When to Use

- You encounter Node.js deprecation warnings in GitHub Actions logs (e.g., "Node.js 20 actions are deprecated").

- You see warnings about `punycode` or `url.parse()` deprecations inside actions like `actions/cache`.

- Trunk check fails on `pyproject.toml` or other TOML files after running package managers like `uv`.

- Resolving C/C++ linker errors (like `undefined reference`) in CI that don't happen locally.

  

## Node.js Deprecation on GitHub Actions

  

GitHub is deprecating Node 20 as the default runtime for actions (e.g., `actions/checkout@v4`, `actions/cache@v4`), moving to Node 24 by June 2026.

  

### Fix: Force Node 24

To bypass the "Node.js 20 actions are deprecated" warnings and proactively migrate to the Node 24 runtime, set this environment variable at the top level of the workflow file (`.github/workflows/*.yml`):

  

```yaml

env:

FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true

```

  

### Note on `punycode` and `url.parse()` Warnings

When you force Node 24, you may see new warnings like:

- `DeprecationWarning: The punycode module is deprecated.`

- `DeprecationWarning: url.parse() behavior is not standardized...`

  

**Action:** Ignore them. These are harmless, internal warnings emitted by the official GitHub actions (like `actions/cache`) because their codebase hasn't been fully updated to remove these older APIs yet. They **will not** fail the build.

  

## Trunk Taplo Formatting Discrepancies

  

When updating dependencies using tools like `uv` (e.g., `uv add <package>`), the tool rewrites `pyproject.toml`. However, `uv`'s internal formatting may not perfectly match Trunk's `taplo` TOML formatter rules.

  

### Symptoms

Trunk CI fails with:

`Incorrect formatting, autoformat by running 'trunk fmt' taplo`

  

### Fix

Do not assume the code is logically broken. Instead, run the trunk formatter locally and commit the change:

```bash

trunk fmt pyproject.toml

git commit -am "style: format pyproject.toml with taplo"

```

  

## LADR / Legacy C/C++ Linker Errors in CI

  

If building older C/C++ projects (like LADR or Prover9) fails in CI with `undefined reference to 'round'` or similar math library (`libm`) linker errors, the issue is often order of compilation flags.

- Legacy Makefiles sometimes put `-lm` *before* the object files.

- Modern `gcc` in CI environments discards `-lm` if placed too early.

- **Fix:** Use a CMake build script if provided (e.g., `./run_cmake.sh`) instead of `make`, or modify the Makefile to place `-lm` at the end of the compile string.