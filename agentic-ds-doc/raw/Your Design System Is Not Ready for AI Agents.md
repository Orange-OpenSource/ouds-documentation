---
title: "Your Design System Is Not Ready for AI Agents"
source: "https://www.intodesignsystems.com/blog/design-system-not-ready-for-ai-agents"
author:
  - "[[Sil Bormüller]]"
published: 2026-04-10
created: 2026-06-22
description: "Five failure modes that break AI agent output, and how teams at Spotify, GitHub and Indeed are fixing them. Based on real talks from the AI Design Systems Conference 2026."
tags:
  - "clippings"
---
![Your Design System Is Not Ready for AI Agents, Design Systems article and tutorial from Into Design Systems](https://www.intodesignsystems.com/_next/image?url=%2Fblog%2Fimg%2Fai-design-systems-2026.webp&w=3840&q=90)

Your design system was built for humans. Designers read documentation, developers browse Storybook, everyone follows the guidelines because they understand the intent behind them.

AI agents don't. They parse your system, extract what the prompt asks for and fill every gap with assumptions from training data. When those assumptions are wrong, you get components that look right but break your foundations.

At the [AI Design Systems Conference 2026](https://www.intodesignsystems.com/agenda), five speakers shared what actually goes wrong when teams connect their design systems to AI agents, and how they fixed it. Here are the five failure modes they identified.

---

## 1\. Documentation drift

**The problem:** Your docs say one thing, your tokens do another and your components do a third. For humans this is annoying. For AI agents it's catastrophic because they can't judge which source is correct.

Romina Kavcic shared that **30-40% of design system team time** goes to pure maintenance: accessibility regressions, token misuse and documentation going out of sync with the actual system. When an agent encounters conflicting information across docs, tokens and components, it picks whichever source it found first or averages across all of them.

**The fix:** Treat documentation drift as a monitored failure mode, not a backlog item. Romina's approach: a self-healing loop (Observe, Detect, Suggest, Fix, Learn) based on IBM's MAPE-K framework. Signals from Figma API, CI hooks and usage analytics flow into a drift-scoring engine that flags inconsistencies and creates PRs automatically.

You don't need to build that whole pipeline on day one. Start by **validating meaning across layers**: does the token name match the component description? Does the documentation reflect the current API? If those three don't align, fix it before connecting anything to an MCP.

---

## 2\. Markdown dumped into an MCP without benchmarking

**The problem:** The most common first move is plugging existing Markdown documentation into an MCP server and hoping for the best. Diana Wolosin at Indeed did the work to prove why this fails.

She parsed **77 components** from MDX docs and tested **8 different MCP configurations** against **1,056 prompts**. The results:

- Markdown: ~30,000 tokens per query, 82% coverage, hallucinations present
- JSON: higher accuracy, **80% fewer tokens**, 5x lower annual cost ($300 vs $1,500)

As Diana put it: "Our docs are written for humans. The new user, AI, needs structured metadata, not documentation prose."

**The fix:** Benchmark before you commit to a format. Diana's rule: **JSON for MCP, Markdown for LLM**. Structured data like component APIs, props, sizes and variants belongs in JSON because it's a contract with explicit keys, explicit values and no ambiguity. Instructions and rules for an LLM are natural language, so Markdown works there.

Indeed's pipeline now auto-triggers on MDX updates, converts to JSON metadata and has produced **4,300 AI prototypes in 4 months**.

---

## 3\. No trust levels for agent actions

**The problem:** You give an agent access to your design system and it starts merging PRs, updating tokens and modifying component APIs. Some of those changes are fine. Others needed a human decision that never happened.

Romina Kavcic framed this as career progression: "You don't want agents to run in the wild. Some decisions will never go past level three because they'll always need human judgment."

**The fix:** Define **trust levels per action**, not per agent. A simple framework:

- **Auto-merge**: high confidence, low risk. Linting fixes, documentation typos, accessibility labels.
- **Draft PR**: medium confidence. Token value updates, component description changes.
- **Suggest only**: low confidence or high impact. New component APIs, breaking changes, governance decisions.

At GitHub, Jan Six enforced this structurally: agents in the Primer design system can only create an issue, never merge code. Their agentic workflows run daily QA and maintenance with "safe outputs" that always require human review.

---

## 4\. MCP without always-on rules

**The problem:** Your agent knows about your components but breaks every foundation. Spacing is wrong, typography doesn't match, colors are off-brand. The components are technically correct but the page looks nothing like your product.

Brad Frost explained why: **MCP is on-demand**. It only returns what the prompt asks for. If the prompt says "build me a card," MCP returns card and button metadata but ignores spacing, typography and colors. The LLM fills those gaps with its own assumptions.

**The fix:** Brad's framework is **progressive disclosure of context**:

1. **Always-on rules** for foundations: spacing scale, color tokens, typography, border radius. These are injected into every prompt regardless of what the agent is building.
2. **MCP on-demand** for components: the agent queries your MCP server when it needs specific component APIs, props and variants.
3. **AGENTS.md** as orchestration layer: a single file that defines which rules are always-on, where to find the MCP server and what trust levels apply.

Together these three layers ensure the agent never has to guess about your foundations.

---

## 5\. Monolithic component definitions

**The problem:** Your component documentation is a single large block: props, variants, styles, behaviors, accessibility notes, usage guidelines, all in one file. For humans this is convenient. For AI it means massive context windows where the model has to parse everything to understand anything.

The Spotify Encore team discovered this when AI agents started bypassing Encore entirely. Developers went to Cursor first, got non-Encore output, and shipped it. The design system was too complex for AI to reason about efficiently.

**The fix:** Spotify rebuilt their component architecture into **three independent layers**:

1. **Foundation layer**: tokens and primitives
2. **Style layer**: visual appearance
3. **Behavior layer**: interaction logic

This creates what they call **"smaller context bubbles"** for AI. Instead of understanding an entire monolithic component, the agent can reason about foundations, styles or behaviors independently. Users can mix and match: take just the button styles and add custom behavior, or take the full button out of the box.

The result: **220,000+ shared style uses** (50% year-over-year growth), **93% developer satisfaction** and a system that works for both humans and AI agents.

They also built a custom **MCP evaluation framework** that tests prompts against multiple LLMs and compares generated components both in code and visually. Because, as they said: "We can't just launch and hope for the best."

---

## Where to start

You don't need to fix all five at once. The speakers agreed on a common starting point:

**Plant seeds, not trees.** Naming conventions, token structure and component descriptions first. Even basic structured metadata gives agents dramatically better output than no context at all.

If you want the full picture, including frameworks, real-world implementations and a step-by-step guide, read the [Agentic Design Systems: The Complete Guide](https://www.intodesignsystems.com/agentic-design-systems).

All five talks referenced in this post are available as recordings with slides, templates and prompts. [Get instant access](https://www.intodesignsystems.com/#pricing).

![Sil Bormüller](https://www.intodesignsystems.com/avatars/sil-bormueller-ids-web.webp)

Sil Bormüller

Founder of [Into Design Systems](https://www.intodesignsystems.com/conference-2025), ex Design System Lead

Design System Awards 2025 Winner

I have worked with companies like adidas, Philips and Ableton on their Design Systems. Into Design Systems is inclusive, introvert-friendly and a safe to learn environment with examples, demos and hands-on instructions.

Interested in Design Systems?

Join the conference, read my blog, or connect with me on LinkedIn.