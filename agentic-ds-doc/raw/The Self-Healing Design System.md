---
title: "The Self-Healing Design System"
source: "https://learn.thedesignsystem.guide/p/the-self-healing-design-system"
author:
  - "[[Romina Kavcic]]"
published: 2026-04-04
created: 2026-06-15
description: "Agentic Design Systems, part 3"
tags:
  - "clippings"
---
👋 Get weekly insights, tools, and templates to help you build and scale design systems. More: [Design Tokens Mastery Course](https://thedesignsystem.guide/design-tokens-course) / [YouTube](https://www.youtube.com/@designsystemguide) / [My Linkedin](https://www.linkedin.com/in/rominakavcic/)

---

![](https://substackcdn.com/image/fetch/$s_!N4qr!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb55d8930-7ee1-422a-bae7-37810c34ffbd_2184x1455.png)

In Part 1 and 2, I made the case that design systems are the semantic layer that makes AI-assisted design possible. The understanding, not the code, is the asset.

Now let’s talk about the machinery AND the judgment calls. The architecture, the self-healing loop, what AI genuinely cannot do, and three phases you can start this week.

---

## The architecture

This is the architecture I’ve built over the past year.

At the center: **Claude Code** as the orchestration layer. Connected via MCP to **Figma** (through my Tidy plugin), to **GitHub**, to **Storybook**, to **PostHog** (analytics), to **[Granola](https://go.granola.ai/romina-kavcic)** (meeting notes), to **Sentry** for error monitoring, to the **documentation layer**, and to the **Observatory** dashboard.

**👋 A note on tooling:**

Claude Code is not the only option here. Because everything connects through MCP, the orchestration layer is swappable. I’ve tested Cursor, Codex, and other AI coding tools in this setup. **I also run the same exercises** across new models whenever they come out (Gemini, GPT 5.2 through 5.4, Llama, Mistral) to benchmark how they handle token naming, component composition, and system-level reasoning. Claude Code consistently delivered the best results for design system work, particularly in reasoning about component relationships and token semantics. But the architecture doesn’t lock you in. If a better tool shows up tomorrow, you swap the center, and everything else stays the same. That’s the point of building on a protocol, not a product.

The loop is:

1. **Watch.** Detect drift in tokens, components, and docs.
2. **Analyze.** Score severity, prioritize fixes.
3. **Execute.** Generate PRs, update docs, sync tokens.
4. **Observe.** Verify results and loop back.

But here’s the thing. This architecture only works because the **foundation is solid.** Without clean token naming, without component descriptions, without intent documentation, the agent has nothing meaningful to work with.