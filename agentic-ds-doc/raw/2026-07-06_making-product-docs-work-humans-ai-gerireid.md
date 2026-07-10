---
title: "Making product documentation work for humans and AI"
source: "https://gerireid.com/blog/making-product-docs-work-for-humans-and-ai/"
author:
  - "[[Geri Reid]]"
published: 2026-04
created: 2026-07-06
description: "Companies are investing heavily in AI. This feels like our chance to quietly make documentation better for everyone."
tags:
  - "clippings"
---

If you build products, you're expected to write documentation. Nobody teaches you how. If you're a designer, developer, or product person, it just quietly becomes part of your job.

Documentation isn't just for humans anymore. As organisations rush to adopt AI, docs need to work for machines too. The interesting part is that the same things that make documentation more accessible for people also make it more useful for AI. Clear structure. Plain language. Accessible formats.

Companies are investing heavily in AI. This feels like our chance to quietly make documentation better for everyone.

## Rethinking how we write documentation

I've never been taught to write documentation properly and just picked it up along the way. That's started to feel like a problem, especially now documentation needs to work for both humans and machines.

So I've been trying to educate myself.

I've been reading about documentation frameworks, looking at how technical writers structure information, and trying to understand what actually works in product teams.

The more I looked, the more I realised something. The existing frameworks are useful, but they don't quite fit the kind of documentation we write day to day in product and tech organisations.

So I started experimenting with a different way of structuring documentation. This post proposes a simple idea: five questions that most product documentation is trying to answer.

## Why accessible documentation suddenly matters

Until recently, we've muddled along with mediocre documentation. Humans are good at working around bad systems. We ask questions and dig through Slack. It's inefficient, but it kind of works.

AI doesn't work like that.

When you feed a Large Language Model (LLM) poorly structured, contradictory, out-of-date docs, it doesn't admit ignorance. It finds patterns and constructs an answer. A confident, well-formatted, completely wrong answer delivered as fact. I ran a fun little experiment where I tried to use AI to write component accessibility documentation, and before I specified a list of approved components, it wildly hallucinated components based on their name.

Outdated documentation used to just slow humans down but now it can actively create bad outcomes. We're already seeing cases where AI agents surface sensitive information when safeguards fail, like this internal data leak at Meta.

Your team's messy Confluence space that nobody reads? Suddenly, it doesn't look quite so harmless.

## Why existing frameworks only get you so far

If documentation needs to work for both humans and machines, structure starts to matter. Several frameworks try to bring structure to docs.

The framework I've found the easiest to get onboard with is Diátaxis, which divides docs into tutorials, how-to guides, reference, and explanation. It's widely respected in technical writing and works well for software and open source documentation.

arc42 is a more complex framework for documenting software architecture. My takeaway from arc42 is this canvas, which captures key information on a single page. This one pager riffs on Alex Osterwalder's original Business Model Canvas and has evolved into other practical thinking tools like the Lean UX Canvas and architecture canvases used in engineering teams.

Frameworks like these are helpful for structuring documentation. But working in product and tech organisations, I kept running into gaps. The docs I write day to day don't fit neatly into these categories. Some don't really count as documentation in Diátaxis terms at all. Things like: component specifications, design token architecture, ownership matrices, Jira tickets, release notes, and design changelogs.

These are not user guides. They document systems, decisions, ownership, and work. Instead of forcing everything into existing categories, I've started thinking about documentation differently.

## Five questions for structuring documentation

In a modern product team, most documentation exists to answer one of five questions:

- What exists?
- What are the rules?
- What needs to be done?
- How do I do something?
- What changed?

These five questions form the knowledge architecture of a product and tech organisation. Almost every document you create will primarily answer one of them.

When documentation answers a question, its purpose becomes clearer. Readers can find answers faster, machines can interpret content more reliably, and as an author, you know what to include.

## 1. What exists? Reference

Reference documentation answers the question: what exists?

These docs define and describe things. They are lookup resources rather than instructional guides.

In a product and tech org, reference documentation might include:

- Team structures
- Design system component catalogues
- Component props
- RACI matrices
- API endpoints

Reference documentation is not about how to use something. It is about describing what something is.

For humans: good reference documentation enables fast lookup. People can quickly find what exists without asking around.

For machines: reference documentation provides definitions. AI tools rely on clear definitions to answer questions accurately.

Reference documentation forms the foundation of documentation infrastructure. You cannot define rules or write guides without first defining what exists.

## 2. What are the rules? Specifications

Specifications answer the question: what are the rules?

These documents define constraints, behaviours, and standards. If reference documentation defines what exists, then specifications define how things must behave.

In product and tech teams, specifications include:

- Naming conventions
- Design token architecture
- Technical accessibility standards
- API schemas

For humans: specifications reduce ambiguity. Teams align faster when expectations are written down.

For machines: specifications provide rules. AI systems can generate outputs that follow constraints and apply standards consistently.

Specifications turn decisions into infrastructure. Once written, they guide behaviour across teams and systems.

## 3. What needs to be done? Tasks

Tasks answer the question: what needs to be done?

These are planning artefacts that describe work to be completed.

In a product and tech org, tasks include:

- Work tickets in tools like Jira or Trello
- Task lists
- Implementation checklists

Tasks are often overlooked as documentation, but they are critical. They capture intent and record decisions where work happens.

For humans: a well written task reduces clarification questions and removes back and forth.

For machines: structured tasks enable automation. AI systems can summarise, prioritise, or generate follow up actions.

Tasks are documentation in motion. They capture work as it happens and create a record of intent.

## 4. How do I do something? How-to guides

How to guides answer the question: how do I do something?

These documents describe the steps required to complete a task.

In a product and tech org, how to guides might be things like:

- Deploying to production
- Setting up a development environment
- Testing with a screen reader
- Creating a new component

How to guides are some of the most frequently used documentation. They help people complete tasks independently and reduce reliance on individual knowledge.

For humans: this enables self service.

For machines: structured steps can be interpreted and reused.

How to guides turn knowledge into repeatable processes. They reduce onboarding time, improve consistency, and make work easier to scale.

## 5. What changed? Changelogs

Changelogs answer the question: what changed?

These documents capture history and preserve institutional knowledge.

In a product and tech org, changelogs include:

- Product changelogs
- Design system changelogs
- Release notes
- Architecture decision records

For humans: changelogs provide context and traceability. They help teams understand when something changed and why.

For machines: changelogs provide structured historical data that can be searched, summarised, and analysed.

Changelogs turn history into documentation. They help teams understand how systems evolve and make sure decisions are not lost over time.

## Where this goes next

Now I have a structure that works for me, I mapped it onto my own product documentation canvas.

This is still a work in progress. I'm using these five questions to shape how I write documentation and to see whether the structure actually holds up when I start researching stuff.

I expect this to evolve. Some parts will be wrong. Others might turn out to be more useful than I expected. I'm planning to explore each question in more detail and share examples from real product and tech teams.

Those boring docs no one reads are quietly becoming infrastructure.
