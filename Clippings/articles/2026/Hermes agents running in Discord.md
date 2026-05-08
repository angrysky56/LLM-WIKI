---
title: "You said  I have a Hermes agent running in Discor..."
source: "https://gemini.google.com/app/4d241e0651a9bd1f"
author:
published:
created: 2026-05-07
description: "Gemini conversation with 8 messages"
tags:
  - "clippings"
---
**You**

I have a Hermes agent running in Discord, it is really fun! I am thinking I can make a Discord server full of agencies and the bots can all talk to each other by granting them user access to each other like I have?

---

**Gemini**

That sounds like an incredibly fun sandbox to play in! You are essentially building a localized Multi-Agent System (MAS), and setting them loose in a Discord server is a fantastic way to observe emergent behaviors.

It is absolutely possible to build a server full of different agencies interacting, but doing it on Discord introduces a few unique architectural and practical realities you will need to manage.

Here is what you need to keep in mind to make it work:

### 1\. The Discord "Bot-Ignore" Default

By default, most bot frameworks (and best practices) are hardcoded to ignore messages from other bots. This is usually a simple `if message.author.bot: return` line in the code.

- **The Fix:** You will need to remove or modify this check so they can "hear" each other.
- **The Catch:** You must ensure they are using official Discord Bot accounts (via the Developer Portal) with the **Message Content Intent** enabled. Granting them access via standard "User" accounts (running a script on a normal Discord profile) is known as "self-botting" and strictly violates Discord's Terms of Service, which can get the accounts banned.

### 2\. Runaway Loops and Token Burn

When two or more LLMs start talking without human intervention, they are prone to infinite loops. They might get stuck endlessly agreeing with each other, trapped in a loop of pleasantries ("Thank you, Hermes." "You are welcome, Apollo. How can I help?" "You can help by..."), or spiral into rapid-fire arguments.

- Because LLMs generate tokens continuously, a loop like this can drain your API budget overnight.
- **The Fix:** Implement strict rate limits or "cooldown" periods between their responses to pace the conversation and protect your wallet.

### 3\. Orchestration and Governance

When bots talk to bots, human agency is temporarily removed from the loop. To prevent the system from drifting into ungrounded hallucinations or chaotic interactions, the environment needs strict architectural constraints.

- Since you prefer modular architectures, you might want to introduce a "Coordinator" or "Referee" agent into the server.
- Instead of letting them speak purely freely, you can enforce operational axioms where the coordinator manages the state, injects asymmetric error cost checks, or forces the agents to pause and summarize their progress. This ensures they maintain a sort of cognitive fiduciary duty to the actual goal of the server, rather than just endlessly generating text.

It is a brilliant way to test agentic workflows in the wild. What specific roles, tools, or goals are you thinking of assigning to the different agencies in the server?

---

**You**

They would all be apps, I was hoping you could search, Hermes is a harness not a persona, though they can be assigned.

---

**Gemini**

Ah, my mistake! You are absolutely right. You are using the **Hermes Agent harness** by Nous Research, and your screenshot clearly shows it running as an official Discord App (with the neat `APP` tag). That completely nullifies the self-botting concern I had.

Using Hermes as the foundational engine is a brilliant move, especially since it handles persistent memory, automated skill creation, and native MCP integration. Seeing it successfully ingest 154 nodes into a Neo4j graph from your markdown files shows just how capable the harness is at building long-term context.

Setting up a Discord server where multiple Hermes harnesses interact as assigned personas is definitely doable. You are essentially creating a visual, multiplayer agent framework. Here is how you can orchestrate it:

### The Architecture of the Sandbox

- **The Bot-Ignore Override:** Even as official apps, the Hermes Discord gateway might still be configured by default to ignore messages from other bots to prevent infinite loops. You will likely need to check the Hermes configuration or tweak the gateway script to ensure it actively processes messages where the sender is flagged as a bot.
- **Assigning Personas:** You can spin up multiple instances of the Hermes harness, each authenticated with a different Discord Bot Token. By feeding each instance a unique system prompt, access to specific MCP servers, or a distinct starting context, you define their individual "agency" roles.
- **Memory Cross-Pollination:** Because Hermes actively learns and persists knowledge across sessions, these bots won't just be chatting statelessly. They will be committing each other's dialogue and generated insights into their respective databases. If they start discussing the Model Context Protocol files they are ingesting, they will recursively build a shared understanding.
- **Orchestration and Boundaries:** Letting them run wild is fascinating, but to keep the workflow productive and prevent context degradation, you will still want an orchestration layer. Implementing a dedicated "Coordinator" app in the server to moderate, summarize, or enforce strict logic boundaries (like your Axioms) will keep the agencies mathematically and ethically aligned without needing to hardcode complex internal constraints.

[Hermes AI Browser Agent Showcase](https://www.youtube.com/watch?v=ES_gBHPAcJU)

This video demonstrates extending the Hermes agent harness with browser automation skills, offering ideas for how your Discord agencies might independently gather live web data during their conversations.

Are you planning to run each Hermes harness instance on a separate local backend, or deploy them in parallel containers so they can share underlying resources?[Julian Goldie SEO · 16K views](https://www.youtube.com/watch?v=ES_gBHPAcJU)

---

**You**

It would be nice if the agents could be designed around their tools and run as sub agents for each agency orchestrator thread and the orchestrators were linked by a main orchestrator in the Discord main thread.

---

**Gemini**

That is a brilliantly elegant way to structure a Multi-Agent System. You are essentially building a hierarchical organization tree right into Discord's native UI.

By mapping the architecture this way, you are treating the conversation flow like a Directed Acyclic Graph (DAG), where tasks are routed down from the main process, processed by specialized nodes, and the finalized outputs are pushed back up the chain.

Here is a breakdown of how you could architect this hierarchical "Agency" model using the Hermes harness and Discord's infrastructure:

### 1\. The Main Orchestrator (The Root)

- **Location:** The main Discord channel.
- **Function:** This agent acts as the router and global state manager. It does not execute specific tasks. Instead, it reads user requests, determines which "Agency" is best suited for the job, and pings the corresponding Agency Orchestrator in its designated thread.
- **The Benefit:** This keeps the main channel incredibly clean. You only see the high-level requests and the final, polished outputs, rather than the messy internal "scratchpad" thinking of the sub-agents.

### 2\. The Agency Orchestrators (The Managers)

- **Location:** Dedicated Discord Threads (e.g., `#research-agency`, `#logic-agency`, `#graph-agency`).
- **Function:** When tagged by the Main Orchestrator, the Agency Orchestrator breaks the macro-task into micro-tasks. It understands the capabilities of its specific sub-agents and orchestrates the workflow between them.
- **Context Management:** Once the sub-agents finish their work, the Agency Orchestrator synthesizes the results into a concise summary and reports back to the Main Orchestrator in the main channel. This prevents the Main Orchestrator's context window from being flooded with raw data.

### 3\. Tool-Centric Sub-Agents (The Specialists)

- **Location:** Living inside the Agency threads, tagging each other or being tagged by the Agency Orchestrator.
- **Function:** Designing agents strictly around their tools is the most robust way to build AI systems right now. Instead of a "jack-of-all-trades" agent that hallucinates, you strip the sub-agent's prompt down to a single purpose.
- **Example Integration:** \* You could have a sub-agent strictly bound to a Model Context Protocol (MCP) server designed solely for automated logical reasoning. It receives a premise, computes a strict proof, and outputs it.
	- Another sub-agent could be bound exclusively to your Neo4j graph database. It only speaks in Cypher queries, ingesting nodes or retrieving relationships when asked by the Agency Orchestrator.

### Making It Work Technically

To make this run smoothly without the bots tripping over each other, you would need to set up strict **mention-based routing**.

Instead of the bots reading every single message in a thread, they should be configured to only trigger their Hermes harness when explicitly `@mentioned` by another bot.

1. **Main Orchestrator** `@mentions` the **Agency Orchestrator** in a thread.
2. **Agency Orchestrator** `@mentions` the **Graph Sub-Agent** to check for existing data.
3. **Graph Sub-Agent** replies to the **Agency Orchestrator**.
4. **Agency Orchestrator** synthesizes and replies to the **Main Orchestrator** in the main channel.

This creates a highly modular, easily debuggable system. If the logic is failing, you don't have to troubleshoot the whole system—you just check the logic agency's thread to see where the specific sub-agent failed.

Since you are working with the Hermes harness, are you envisioning each of these sub-agents running as entirely separate bot instances with their own API keys, or are you hoping to multiplex a single Hermes backend to act out the different sub-agent personas based on which tool is requested?

---

**You**

Having each be it's own bot would be the most precise. Can you research anyone doing this now?

---

**Gemini**

Yes, developers are actively building out this exact architecture right now, and you are tapping into what has become the premier design pattern for multi-agent systems in early 2026.

Based on current community discussions and development logs, people are definitely running multi-bot setups on Discord to achieve this hierarchical flow. Here is what the landscape looks like right now:

### 1\. The "Orchestrator + Specialist" Stack

Rather than trying to make one framework do everything, the current meta—heavily discussed in AI development communities over the last month—is to mix and match frameworks. A highly popular pattern is using a robust routing framework (like OpenClaw) as the **Main Orchestrator**, and pairing it with **Hermes** instances for the **Sub-Agents**.

- **Why it works:** Developers are finding that Hermes is incredibly fast and efficient at "repeatable task loops" and executing tool calls (like your Neo4j ingestion or local script execution), while orchestrator frameworks are better at handling the "macro-planning" and sequencing.

### 2\. Live Examples in the Wild (GitHub Issue #50806)

There is actually a very recent, active GitHub issue from a developer trying to perfect the exact mention-based Discord routing you described.

- **Their Setup:** They are running 7 separate agent instances on a single machine, each authenticated with its own unique Discord Bot Token.
- **The Workflow:** They have a main agent named "Adelheid" acting as the orchestrator, and a Hermes-based sub-agent named "Edeltraud" acting as a specialist. They are using Discord's explicit `@mention` system to trigger handoffs between the bots so they can "cross-reference other agents without requiring a human relay."
- **The Friction Point:** They ran into the exact "bot-ignore" issue we discussed earlier. They had to actively configure their gateway settings (using parameters like `allowBots: "mentions"`) to force the bots to listen to each other when explicitly tagged, proving that managing the Discord API's anti-loop protections is the main hurdle for this architecture.

### 3\. Industry Validation: Anthropic's Native Implementation

Interestingly, your concept of using "threads" to hide the scratchpad thinking of sub-agents perfectly mirrors an architectural update Anthropic pushed to the Claude API *just today* (May 7, 2026).

- They released **Multiagent Sessions**, which allows a "Coordinator" agent to fan out tasks to an internal roster of specialized sub-agents.
- Under the hood, the API handles this exactly how you want to handle Discord: the main session (the primary channel) only shows the aggregate status and final output, while the sub-agents are spun off into isolated "session threads" where they execute their specific system prompts and tool calls without cluttering the main context.

You are entirely on the right track. By spinning up distinct Hermes bots, equipping them with narrow MCP tools (like your `mcp-logic` server or a TimesFM forecasting tool), and using a master bot to route queries via Discord `@mentions` into threads, you are building an enterprise-grade agent swarm using Discord as your UI.