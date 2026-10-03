---
title: "Stop 'Trying AI' — Start Using It: Agent Workflows for Design System Teams"
source: "https://medium.com/design-bootcamp/stop-trying-ai-start-using-it-agent-workflows-for-design-system-teams-6e90fddd6eef"
author:
  - "[[gerard-pamies]]"
published: 2026-03-01
created: 2026-06-18
tags:
  - "clippings"
---

A practical look at how our design system team uses AI agents for documentation, benchmarking, contribution support, and component QA. Real workflows, reusable templates, and structured inputs you can apply with any LLM — no MCP connection required.

## Agent for design systems

An agent can give expert-level answers to short prompts because it has project context (documentation, conventions, decisions, terminology). This boosts teamwork: you get consistent answers similar to what you'd get from the most knowledgeable person on the team — without interrupting them.

If we feed the agent structured, aligned data, it can also help keep the team consistent on:
- terminology and naming
- component structure and conventions
- documentation patterns and rules

Note: As a single user you can create a Project in ChatGPT to store md files and start getting an AI "assistant" for your tasks.

## How we use our agent

### 1) In-house inventory

By providing the agent with data from our existing Design System, we can analyze technical documentation and spot differences quickly.

Examples:
- generate a summary of a component (great for onboarding and reviews)
- compare components between the previous and the current Design System
- identify structural differences and missing properties

### 2) Research & benchmarking

If we provide a list of inspirational Design Systems, the agent can review them and create a benchmark (e.g., properties, behaviors, API patterns).

This used to take a long time manually. Now it helps us prepare inputs faster before aligning on the API table for a new component.

### 3) Writing documentation

High-quality component documentation takes time. The agent helps by generating a first draft based on an agreed structure — especially helpful when designers are writing documentation primarily intended for developers (and for future AI-assisted consumption).

AI can also help close technical knowledge gaps (e.g., platform constraints, implementation notes) that designers may not fully own.

Documentation artifacts we generate:
- Figma component set documentation (using an uploaded Markdown template for consistency)
- Variant documentation (a matrix of semantic descriptions across combinations)
- Component documentation pages (usage, properties, do's & don'ts) as a strong starting point

To do this well, the agent needs reliable component data. One thing we do is keep a Markdown file in the agent's folder listing components and their properties. That enables the agent to produce consistent documentation quickly.

A sample markdown with the existing design system components:

```
<!-- List of existing components in my Design system -->

# MyComponentName_01
| Name | Description | Values | CodeOnly |
|---|---|---|---|---|
| propertyName | Description text | list of variants | - |

## Nested components:

# MyComponentName_02
....
```

### 4) Contribution support

When multiple teams contribute to a component, they can ask the agent how to implement it in a specific technology. The agent can reference ADRs and internal decisions to give a consistent, "expert" answer.

### 5) Ask the agent instead of reading documentation

Because the agent has access to Design System knowledge (including token JSON and documentation), designers can ask questions conversationally — without navigating atomic documentation structures.

It can also surface knowledge that's spread across foundations, tokens, and components, and return only what's relevant in the moment.

### 6) Audit my component

A powerful use case is auditing components. We export a JSON via the Anova plugin and use it as input for our agent — helping us with faster QA and consistency checks.

## Key principle

These examples are just a starting point — but they already show how much value you can unlock with simple, practical workflows. Most of them work with any LLM, and they don't require an MCP connection: what matters is providing clear prompts, reusable templates, and structured inputs like Markdown, ADRs, and token/component exports. For teams just beginning to introduce AI into design processes, this is an easy way to move from experimentation to real impact.

Note: to use this approach in ChatGPT first create a "Project" and then upload MD files with your context.
