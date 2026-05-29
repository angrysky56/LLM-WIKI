---
summary: Research on Hermes Agent LCM plugin slash commands not working after restart - no specific bugs found
tags: [Hermes Agent, LCM, plugin, slash commands, troubleshooting]
updated: 2026-05-27T23:47:16Z
created: 2026-05-27T23:47:16Z
---

# Hermes Agent LCM Plugin Slash Commands Research

## Summary

Searched for information about Hermes Agent LCM plugin slash commands not working after restart. Found documentation and GitHub issues page, but no specific issues addressing this exact problem.

## What Was Found

### Documentation References
- **Hermes Agent Documentation**: https://hermes-agent.nousresearch.com/docs
- **FAQ & Troubleshooting**: https://hermes-agent.nousresearch.com/docs/reference/faq
- **MCP Integration**: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp

### Key Points from Documentation
1. **Slash Commands**: All slash commands in Hermes flow through the same resolution pipeline in the gateway (from Gateway Internals docs)
2. **Restart Requirement**: Documentation explicitly states "Restart your agent for the MCP server to load" - this applies to Claude Code, Cursor, Codex CLI, opencode, and Hermes Agent
3. **Plugin Types**: Hermes has four kinds of plugins (from Hermes Agent 2 docs)
4. **MCP Server Issues**: Troubleshooting section mentions checking config and restarting Hermes if MCP server not connecting

### GitHub Issues
- Fetched the GitHub Issues page for NousResearch/hermes-agent but the content is dynamic and requires JavaScript to render properly
- No specific issues found with "LCM plugin slash commands restart" label

### Discord
- Searched Discord for relevant posts but results are dynamic content

## Common Troubleshooting Patterns (General)
Based on general Hermes Agent documentation:
1. Restart Hermes after config changes
2. Check MCP server config under `~/.hermes/profiles/<name>/` 
3. Verify commands against Hermes version
4. Shell Hooks can track which slash commands are used (from Event Hooks docs)

## Files Retrieved
- `raw/issues-nousresearchhermes-agent.md` - GitHub issues page
- `raw/hermes-agent-documentation-hermes-agent.md` - Main documentation
- `raw/faq-troubleshooting-hermes-agent.md` - FAQ/troubleshooting
- `raw/mcp-model-context-protocol.md` - MCP integration docs
- `raw/search-results.md` - Discord search results

## Conclusion
No specific bug reports or known issues found for "LCM plugin slash commands not working after restart." The documentation suggests this could be a configuration issue requiring a restart, or possibly a config file issue under the profile directory. User may need to:
1. Check their `~/.hermes/profiles/<name>/` directory for MCP config
2. Verify the LCM plugin is properly installed
3. Try restarting Hermes completely
4. Check Hermes version compatibility
