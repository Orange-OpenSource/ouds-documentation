---
title: "Your design system might be AI-ready. Your organisation probably isn't."
source: "https://blog.murphytrueman.com/your-design-system-might-be-ai-ready/?utm_campaign=Design%2BSystems%2BWeekly&utm_medium=web&utm_source=Design_Systems_Weekly_216"
author:
  - "[[Murphy Trueman]]"
published: 2026-03-05
created: 2026-07-06
description: "The technical preparation is well underway. The organisational questions it creates are a different problem entirely."
tags:
  - "clippings"
---
I’ve been watching the design systems community gear up for AI with considerable energy. Token structures are getting cleaner, documentation is becoming more explicit, component naming is moving from visual description to semantic intent. Teams are putting in serious structural work, and it matters.

The focus, across most of those conversations, is on making systems readable by machines. The question of what happens when that actually works gets much less attention.

There’s a statistic doing the rounds from [Figma’s research on AI-augmented product development](https://www.figma.com/reports/design-systems-power-the-pace/?ref=blog.murphytrueman.com): according to their findings, 55% of product builders are now taking on tasks outside their usual scope – PMs prototyping in design tools, marketers generating interfaces, engineers influencing design decisions far earlier in the process than before. The linear workflow, as Figma’s VP of Product, Paige Costello, has described it, has “collapsed”.

That collapse is framed as progress. And maybe it is. But it’s also a governance crisis that most organisations haven’t begun to address.

## The question after “can AI use our system?”

The technical readiness conversation has a clear shape now: make your tokens machine-readable, document intent rather than just appearance, and add higher-order compositions so AI can generate layouts rather than simply dropping in components. Connect design and code through tools like [Code Connect](https://www.figma.com/developers/code-connect?ref=blog.murphytrueman.com) and [Figma’s MCP server](https://developers.figma.com/docs/figma-mcp-server/?ref=blog.murphytrueman.com). I’ve written about this before in [Your next design system user is an agent](https://blog.murphytrueman.com/your-next-design-system-user), and the broader industry is converging on the same set of recommendations.

But technical readiness answers one question: can AI successfully consume your design system and produce something that follows the rules? It doesn’t touch the harder ones. Who decides whether AI’s output is good enough to ship? What happens when velocity increases but craft doesn’t keep pace? How do you prevent your carefully governed system from being overwhelmed by contributions you never anticipated? Those are organisational problems, and most teams haven’t started solving them.

## When everyone can build, who maintains quality?

The democratisation of interface creation opens up real possibilities for exploration and prototyping – more people building, faster iteration, lower barriers to getting something in front of users.

But design systems exist precisely because quality doesn’t scale automatically. You built governance structures, contribution models, and review processes because you learned what happens when everyone does their own thing: entropy, drift, the slow accumulation of “just this once” exceptions that eventually undermine the system entirely. I explored this dynamic in [The hidden cost of design system entropy](https://blog.murphytrueman.com/p/design-system-entropy), and AI accelerates everything I described there, including the rate at which your system can be misused by well-meaning people.

Imagine a PM generates a complete feature interface using your components. Every token is correct, every component is used as documented, and technically it passes every automated check you could throw at it. But the composition is mediocre. The hierarchy is confusing, and the flow doesn’t account for edge cases your designers would have caught instinctively.

Who rejects that? On what authority? Your current review process probably assumes a designer made intentional choices that can be interrogated, but when the creator is a PM using AI, the conversation changes entirely. You’re not critiquing craft decisions anymore – you’re potentially telling a colleague their work isn’t good enough when they followed all the rules. Your governance model was never designed to handle that situation.

## The accountability gap

This is where the conversation tends to go quiet, and it’s the part that carries the most organisational risk.

If AI generates an interface using your design system and it ships with an accessibility failure, who owns that? The design system team who built the components? The person who prompted the AI? The engineer who implemented it? The QA process that didn’t catch it?

Your components might be accessible in isolation, but accessibility isn’t just about individual elements. It’s about context, flow, cognitive load, and the relationships between things – and AI can assemble accessible parts into an inaccessible whole. That’s not a hypothetical edge case. It’s the kind of failure that compounds at speed when no single person feels responsible for the composite experience.

The problem gets harder when you think about it across multiple failure modes: an on-brand button in an off-brand flow, a correct component in a confusing hierarchy, a technically valid interface with a fundamentally broken mental model. Each of those can emerge from AI-generated work that cleared every automated check you have, because your existing accountability structures were designed for human authors with legible intent – not for outputs where nobody made a deliberate choice.

This will land on someone’s desk. As AI-generated interfaces start shipping in production, someone will have to answer for the failures they produce. It’s better to decide now whose desk that is, under what circumstances, and with what escalation path.

![An illustrated desk overwhelmed by a precarious tower of colourful documents and folders, with a coffee cup, notebook, and keyboard visible beneath the chaos, representing accumulated backlog and organisational overload.](https://storage.ghost.io/c/4e/57/4e57da7f-7503-46c8-b61e-0031c03eb394/content/images/2026/03/6108d7b5-d8cc-4fb7-ad34-b1ffe6c4d8b4_1456x816-jpeg.jpg)

An illustrated desk overwhelmed by a precarious tower of colourful documents and folders, with a coffee cup, notebook, and keyboard visible beneath the chaos, representing accumulated backlog and organisational overload.

## Contribution models built for human proposers

Most design system contribution processes assume a human is proposing something. There’s context behind the request, a problem being solved, a conversation to be had about whether this belongs in the system or should remain a one-off. I wrote about the psychology of this in [The component adoption gap](https://blog.murphytrueman.com/the-component-adoption-gap), and the human dynamics I described there get considerably weirder when AI enters the picture.

If AI identifies that teams keep combining three components in the same way, should that become an official pattern? Who evaluates that? How do you distinguish between “this keeps happening because it’s useful” and “this keeps happening because AI keeps suggesting it”? The feedback loop gets strange when the tool proposing contributions is also the tool generating the usage data.

I don’t have clean answers here. But teams who wait until AI is actively contributing to figure out how to evaluate those contributions will find themselves in reactive chaos.

## The role clarity problem

Design systems have always navigated the tension between enabling autonomy and maintaining coherence – you want teams to move fast, and you also want the product to feel like one product. Those goals exist in tension, and your governance model is how you manage that tension. I explored this balance in [Encouraging design system adoption through empathy and empowerment](https://blog.murphytrueman.com/design-system-adoption), but that tension compounds when AI multiplies the number of potential contributors overnight.

As the volume of decisions increases and the pool of potential contributors expands, the traditional signals you used to gauge quality – who made something, what their track record is, what problem they were solving – become less reliable. I’ve found that the teams handling this best aren’t the ones with the most sophisticated AI tooling. They’re the ones who got serious about decision rights before AI forced the question, who know who can approve what, under which circumstances, and with what level of review. That clarity becomes essential when the speed of creation outpaces the speed of human judgment.

![ An illustrated scene of a person arm-wrestling a large industrial robot against an autumn landscape, with small figures in the background, representing the tension between human judgment and machine capability.](https://storage.ghost.io/c/4e/57/4e57da7f-7503-46c8-b61e-0031c03eb394/content/images/2026/03/3dc5506b-796f-429b-aa90-09291151567f_1456x816-jpeg.jpg)

An illustrated scene of a person arm-wrestling a large industrial robot against an autumn landscape, with small figures in the background, representing the tension between human judgment and machine capability.

## What organisational readiness actually looks like

The technical checklist for AI readiness is well-documented at this point. The organisational one is something most teams are still writing in real time.

If I were advising a team on where to start, I’d push them toward a few foundational questions. What does “good enough to ship” mean when the creator is a PM with a prompt rather than a designer with years of craft context? You probably have an implicit answer buried somewhere in your team’s collective judgment, but making it explicit – in a way that can be applied regardless of who made the thing – is uncomfortable work. It requires naming standards that currently live in designers’ heads.

From there, decision rights need to be mapped before you need them. Who can approve AI-generated output for production? Does it require designer review, and does the threshold change based on what’s being created? A content change probably needs less scrutiny than a new user flow, and those distinctions need to be settled before you’re having the conversation under deadline pressure with a specific stakeholder.

Accountability for composite failures is the piece most teams skip. When accessible components combine into an inaccessible whole, someone owns that. When on-brand elements produce an off-brand experience, someone catches it. Whether that responsibility sits with the design system team, the product team, or somewhere shared with clear escalation paths is less important than deciding before ambiguity becomes expensive.

Contribution models are where most teams find the gap they weren’t expecting. If AI starts surfacing patterns or identifying opportunities for new components, what makes an AI-identified pattern worthy of promotion versus something to be actively discouraged? Your process almost certainly wasn’t designed for this, and adapting it before you need it is considerably easier than adapting it under pressure.

If you want a structured way to assess where your organisation actually sits across these dimensions, I built a readiness assessment at [designsystemsforai.com](https://designsystemsforai.com/?ref=blog.murphytrueman.com) for exactly this purpose – one that covers governance, accountability, and contribution models, which is where most teams find the gaps they weren’t expecting.

## Design systems have always been about people

Every design system problem I’ve worked through has had a technical surface and a human core. The tooling changes, the org dynamics don’t.

AI doesn’t change the fact that design systems are fundamentally about how people work together, make decisions, and maintain shared standards while preserving autonomy. What it does is intensify those dynamics – the volume of creation goes up, the speed goes up, and the number of people who can produce something that looks right increases dramatically. All of that puts pressure on exactly the structures that most organisations have left implicit.

Your design system might be ready for AI. Whether your organisation is ready for what happens when AI actually starts using it is a harder question. And it's not one you can answer with better token architecture.

---

Thanks for reading! Subscribe for free to receive new posts directly in your inbox.

This article is also available on [Medium](https://medium.com/@murphytrueman?ref=blog.murphytrueman.com), where I share more posts like this. If you’re active there, feel free to follow me for updates.

I’d love to stay connected – join the conversation on [X](https://x.com/murphytrueman?ref=blog.murphytrueman.com) and [Bluesky](https://bsky.app/profile/murphytrueman.com?ref=blog.murphytrueman.com), or connect with me on [LinkedIn](https://linkedin.com/in/murphytrueman?ref=blog.murphytrueman.com) to talk design systems, digital products, and everything in between. If you found this useful, sharing it with your team or network would mean a lot.

---

On a separate note, I also recently launched [The Component Bestiary](https://thecomponentbestiary.com/?ref=blog.murphytrueman.com), a catalogue of UI components rated by implementation danger. Think D&D monster manual, but for design systems. Volume I is live if you want to take a look.