---
created: 2026-05-29
updated: 2026-06-08
type: concept
summary: Code agent — AI agent specialized in software development tasks including code generation, debugging, refactoring, testing, and code review
tags: [agents, software-engineering, coding]
sources: 
status: active
confidence: 0.8
---

# Code Agent

A code agent is an AI agent specialized in software development tasks. Unlike narrow code generation (a single-shot model), code agents interact with their environment — reading files, running tests, using tools, and iterating on solutions.

## Core Capabilities

Code agents typically perform:
- **Code generation**: Writing code from specifications or natural language
- **Debugging**: Identifying and fixing bugs via error analysis, code inspection, test execution
- **Refactoring**: Improving code structure without changing behavior
- **Testing**: Generating and running test suites to verify correctness
- **Code review**: Analyzing code for issues, security vulnerabilities, style violations
- **Repository navigation**: Understanding large codebases, finding relevant files, tracing dependencies

## Architecture

Code agents generally have:
1. **LLM backbone**: The reasoning engine (typically a frontier model)
2. **Tool access**: File system, shell, git, documentation lookup, test runners
3. **State management**: Tracking progress, managing context window
4. **Iteration loop**: Planning → executing → verifying → repeating

### Tool Use Patterns

Code agents use tools in two patterns:
- **Reactive**: Agent reacts to errors (test failures, exceptions) by modifying code
- **Proactive**: Agent plans a sequence of changes, executes them, then verifies

Both require the agent to understand the feedback loop between code changes and outcomes.

## SWE-Bench as the Evaluation Standard

[[swe-bench]] is the standard benchmark for code agents — real GitHub issues from popular repositories. Performance on SWE-Bench is the primary measure of code agent capability.

Code agents can also be evaluated on:
- **HumanEval**: Simple Python problems (less realistic)
- **Custom benchmarks**: Repository-specific tasks

## Key Challenges

1. **Context management**: Large repositories exceed context windows; agents must select relevant code intelligently
2. **Test reliability**: Tests may be flaky or environment-dependent
3. **Multi-file changes**: Coordinating changes across multiple files without breaking dependencies
4. **Long-horizon tasks**: Issues requiring many steps are harder than single-function problems
5. **Debugging without stack traces**: In sandbox environments, getting full stack traces is difficult

## Connection to Hermes

The [[hermes-agent]] framework provides infrastructure for building code agents:
- `delegate_task()` for spawning code agents
- Tool registry for file system, shell, git operations
- State management for iteration loops
- Safety constraints via soul configuration

## Connections

- [[swe-bench]] — benchmark for code agents
- [[benchmark]] — evaluation frameworks
- [[agentic-research]] — agents conducting research via code execution
- [[hermes-agent]] — framework for building code agents
- [[code-generation]] — generating code (the narrow task)
- [[load-bearing-reasoning]] — identifying critical reasoning steps in code generation
- Concept: [[autonomous-research]]
- Concept: [[llm-agent-architecture]]
