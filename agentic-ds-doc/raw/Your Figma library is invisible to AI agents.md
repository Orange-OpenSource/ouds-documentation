---
title: "Your Figma library is invisible to AI agents"
source: "https://nurxmedov.medium.com/your-figma-library-is-invisible-to-ai-agents-31ff99d0ff9c"
author:
  - "[[Nurkhon]]"
published: 2026-04-16
created: 2026-06-29
description: "AI agents parse, not infer. If your design system wasn’t built for machines, the months you spent on it won’t survive 2026."
tags:
  - "clippings"
---
![An open book showing a Figma component library as human-readable on the left and machine-parsed output on the right. Three red X marks highlight names an AI agent cannot interpret. Represents the gap between how designers read design systems and how AI agents parse them.](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*YZqiQaPaCYhYlEzLGe-Qmg.png)

illustration by author

## AI agents parse, not infer. If your design system wasn’t built for machines, the months you spent on it won’t survive 2026.

**In this article:**

- Why a meticulously built component library became structurally transparent to an AI agent in under two minutes
- What does the difference between human-readable and machine-readable actually cost you in 2026
- The judgment gap agents can’t close — and why that gap is now the job

I wasn’t testing anything. That’s the part I keep coming back to.

I was in the middle of actual product work — iterating on an onboarding flow, using [Claude Code](https://claude.ai/code) connected to Figma via [MCP](https://www.figma.com/blog/introducing-figma-mcp/) to move faster. I pointed the agent at a component library I’d spent months building for this exact product. Tokens, variants, semantic naming, the works. Everything a developer would need. I asked it to generate a screen.

Ninety seconds later, there was a screen.

Clean layout. Reasonable spacing. Looked like our product, more or less. I almost moved on.

Then I opened the layer panel.

Nothing was connected to the library. Every color was hardcoded. The spacing values were arbitrary. The agent had looked at the file, found components named things like, `nav-item-active-v3` and `modal-overlay-blur-dark`, and decided to approximate the visual result from scratch rather than use any of them. Not because it lacked capability. Because those names described what the components *looked like* to me — and told a machine nothing about what they were *for*.

I’d spent months building a library that was fluent in one language. The new reader spoke another.

> **AI agents don’t infer. They parse.**

## The moment the library became invisible

![Two-panel illustration. Left shows a well-organized Figma file with a component library. Right shows an AI agent’s output from the same file — visually similar but built from scratch, with no library connections. The gap is revealed by a magnifying glass highlighting the disconnected layer structure.](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*7Y_79P0wkMSSYCFCdf5MnA.png)

illustration by author

When [Figma MCP launched on March 24, 2026](https://www.figma.com/blog/the-tldr-on-mcp/), it didn’t change what design systems are. It changed who reads them.

Before that, a component library had exactly two audiences: designers who browsed it visually, and developers who translated it manually. Both groups arrived with context. A developer who sees a component named `card–light-updated` can look at it, read the documentation, ask a designer, and figure out when to use it. They bring judgment to the gap between the name and the intention.

An agent doesn’t do that. An agent reads the name, checks whether it matches a pattern it recognizes, and either uses it or doesn’t. `card–light-updated` doesn't match any pattern. So the agent generates its own card from scratch.

I’ve watched this play out enough times now to know it’s not an edge case. Rostislav Peška documented the same failure mode in January 2026: an agent given only a `package.json` dependency list produced plain HTML, ignoring every design system component entirely. Reuse only improved when components were locally inspectable — when their structure was explicit enough for the agent to reason about without inference. The library wasn't broken. It was illegible.

That’s the distinction that most design system owners haven’t absorbed yet. Illegible is different from incorrect.

## What human-readable actually means

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*bvwWaqV-Ais1A5Lp9q6GoA.png)

illustration by author

Every design system carries a set of implicit contracts. You know what it `input-v2-final` means because you were there for v1. You know which `border-error-red` gets used in which context because you remember the conversation where the spec was debated. The naming holds a reference to an entire history of decisions — and that history lives in your head, not in the file.

This isn’t a flaw. It’s how human communication works. We compress. We rely on shared context. We give things names that make sense to the people in the room, trusting that future readers will reconstruct the intention.

AI agents have no room. They have the file, the name, and the structure. Nothing else.

According to [Figma’s 2025 research](https://www.figma.com/), semantic token naming — where names declare function rather than appearance — produces 43% better AI-generated code quality compared to presentation-based names. `color-border-error` versus `red-300`. `spacing-form-field-gap` versus `16`. The difference isn't aesthetic. The first name tells an agent what to do with the value. The second tells an agent what color or number to use, leaving the "when" and "where" as an inference problem that the agent will get wrong.

The component names you thought were readable were readable to one specific audience. That audience just got a second member, and the second member doesn’t share your history.

## The new reader in the room

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*gdrX3klEYmP4ODIjQU_zMA.png)

illustration by author

There’s a useful way to think about what Figma MCP actually changed. Before it, design systems were like well-organized archives. A trained person could navigate them with some effort. A new person needed orientation. The system rewarded familiarity.

Agents don’t become familiar. They query. Each session, the agent reads the system as if for the first time — because it is, for the first time. There’s no accumulated context, no memory of the conversation where you decided that `v2-final` was the production-ready state.

This is why [Spotify’s Encore](https://www.figma.com/blog/creating-coherence-how-spotifys-design-system-goes-beyond-platforms/) — a design system known for its sophistication and depth — produced a specific failure pattern when developers started using AI coding tools. Engineers went to [Cursor](https://cursor.com/) first, asked for components, got non-Encore output, and shipped it. Not because Encore was poorly built. Because Encore was built for a reader who would take time to understand it. Cursor doesn’t take time. It takes structure.

The system was too complex for an agent to parse efficiently, so the agent went around it. The library that took years to build became optional the moment a faster path existed.

AI agents can query a Figma file and extract every component name, every variant, and every property value in seconds. They can’t determine which of those variants represents the intentional design language and which is a historical accident that was never cleaned up. That judgment is human. But only the humans whose systems were built for agent consumption get to exercise it.

## What 23% looks like versus 77%

![Two-panel comparison showing token naming conventions. Left panel (23%) shows semantic function-based names with green checkmarks and clean AI output. Right panel (77%) shows presentation-based names with warning symbols and fragmented AI output. Represents the gap between agent-legible and human-legible-only design systems.](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*AeY62aPf0NcCUMiv763VEw.png)

illustration by author

A [December 2025 UX Collective analysis](https://uxdesign.cc/) found that only 23% of design systems are structured well enough for consistent AI use. A separate [2026 enterprise design system survey](https://uxdesign.cc/) reported that only 8% of teams describe their design system as “very stable.”

The 23% aren’t necessarily better designed. They’re differently named. Their token architecture declares function. Their component variants follow a machine-parseable convention rather than a human-memorable shorthand. Their documentation is structured as data, not prose.

Uber’s design system team moved in this direction with [uSpec](https://www.uber.com/blog/uspec/) — a structured specification format where components carry explicit machine-readable contracts alongside human documentation. The distinction isn’t cosmetic. A component in uSpec tells an agent: this is what I am, this is when I’m used, this is what I require. It removes the inference problem entirely.

The 77% of systems that don’t meet this threshold aren’t failed systems. They’re systems built for an audience that no longer reads them alone.

The practical gap is stark: a team using an agent-legible system gets consistent, on-brand output that actually uses the design system. A team using a human-legible-only system gets output that looks roughly similar to the design language, built entirely from scratch, disconnected from every token and every decision the design team spent years establishing.

The brand debt accumulates invisibly. Then someone does an audit and finds forty-seven different shades of grey in production.

## The skill shift nobody posted a job for

![A split figure — the left half sketching component designs by hand, the right half working with token architecture diagrams and naming schemas. Represents the distinction between visual craft (building components) and structural architecture (making them machine-readable for AI agents).](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*jaV5SGSxPoAQ1FgaFaru-g.png)

illustration by author

Here’s what makes this genuinely uncomfortable: the skill that built most design systems is not the skill that makes them agent-legible.

Building a component library is a visual craft problem. You’re thinking about variants, states, composition, and hierarchy. You’re making decisions about when to abstract and when to stay concrete. The names you choose feel natural because you’re naming for comprehension — for a developer who will read the name, glance at the component, and understand immediately.

Making that library machine-readable is a structural architecture problem. You’re thinking about naming schemas, token taxonomies, and semantic contracts between layers. You’re asking not “does this name make sense to a human” but “does this name give an agent enough information to use the component correctly without context.”

These are different disciplines. A designer who is excellent at the first is not automatically competent at the second. And the industry has not yet figured out how to hire for the second, train for the second, or even fully describe what the second looks like in practice.

I’ve caught myself treating token naming as a cosmetic concern — something you clean up eventually, after the components are solid. That instinct is expensive now. Token naming is structural legibility. It’s the difference between a design system that survives the agentic era and one that gets bypassed by developers who find it faster to prompt their way to a result.

The job didn’t change in a way that shows up on a job description. It changed in a way that shows up in whether your system gets used.

## What AI can’t do here?

![Two-panel illustration. Left shows an AI agent quickly generating 72 variants from a Figma library. Right shows the same library with two visually identical components — one production-approved, one an old experiment — and an agent unable to distinguish them. Represents the judgment gap that only human designers can close.](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*A8btfq37jfTc3TqRtrfobQ.png)

illustration by author

AI agents can generate a 72-variant component set from your Figma library in under an hour. [Figma’s own demos](https://www.figma.com/blog/the-tldr-on-mcp/) show agents building production-ready screens directly from a design system as the source of truth — when that system is legible.

They can’t decide which variants represent intentional design language and which are historical accidents. They can’t know that `input-v2-final` replaced `input-v1` for accessibility reasons that aren't documented anywhere. They can't distinguish between a component that exists because it was carefully designed and one that exists because someone duplicated a frame three years ago and never deleted it.

Every design system has both kinds. The agent treats them identically.

This is the judgment call that stays human: deciding what the design system actually means, which decisions were intentional, and which artifacts should be cleaned up before an agent starts using them as source material. An agent consuming a messy library doesn’t produce messy output occasionally — it produces consistently wrong output, with high confidence, at scale.

The agent’s confidence is the problem. It reads what’s there and uses it. It has no mechanism for noticing that It `card–light-updated` was an experiment from Q3 2024 that was never production-approved.

So the human role shifts. The question is no longer “did I build this well?” The question is, “Did I build this in a way that an agent can read accurately?”

## The question worth asking this week

![Aerial illustration of a cityscape at night where buildings represent Figma components — some connected by glowing token pathways, others isolated and dark. A single figure stands on a rooftop observing both. Represents the design system as infrastructure, and the question of whether it was built to be readable by both humans and AI agents.](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*yWKQRg2PoCQyNib-iz8pAg.png)

illustration by author

Design systems have always been infrastructure. The difference now is who uses that infrastructure, and how.

For most of the last decade, a design system’s primary audience tolerated ambiguity. Developers could ask. Designers could clarify. The implicit contracts held because humans were flexible enough to honor them.

AI agents will keep getting better at parsing Figma files, understanding token relationships, and inferring design intent from sparse information. The gap will narrow.

The human differentiator isn’t building faster. It’s deciding what the system means — which decisions were intentional, which tokens represent the actual design language, which components are canonical and which are historical noise. That decision-making can’t be automated, because it requires knowing why things are the way they are, not just reading what they are.

Your design system is infrastructure for AI agents now, whether you architected it that way or not.

The question worth sitting with this week: when an agent reads your Figma library for the first time, with no context, no history, no memory of the conversations that produced it — what does it find?

*Sources and references:* [*Figma MCP launch, March 2026*](https://www.figma.com/blog/introducing-figma-mcp/)*;* [*Spotify Encore design system*](https://spotify.design/article/reimagining-design-systems-at-spotify)*;* [*Uber uSpec specification system*](https://www.uber.com/blog/uspec/)*; Rostislav Peška, design system + AI agent component reuse documentation (January 2026);* [*UX Collective design system AI readiness analysis*](https://uxdesign.cc/) *(December 2025); Figma 2025 research on semantic token naming and AI code quality.*

Follow for more on AI, design practice, and the skills that compound when tools get cheaper.