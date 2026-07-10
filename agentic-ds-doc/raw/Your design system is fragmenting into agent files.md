---
title: "Your design system is fragmenting into agent files"
source: "https://www.designsystemscollective.com/your-design-system-is-fragmenting-into-agent-files-26a9b19a2fad"
author:
  - "[[Murphy Trueman]]"
published: 2026-05-14
created: 2026-07-07
description: "Your design system is fragmenting into agent files AGENTS.md, SKILL.md, DESIGN.md, and where each one fits Three file formats have moved from proposal to working convention in the design systems …"
tags:
  - "clippings"
---
**AGENTS.md, SKILL.md, DESIGN.md, and where each one fits**

Three file formats have moved from proposal to working convention in the design systems conversation in roughly twelve months. OpenAI released [AGENTS.md](https://agents.md/) in August 2025 and donated it to the [Linux Foundation’s Agentic AI Foundation](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation) in December 2025. Anthropic introduced [SKILL.md](https://github.com/anthropics/skills) as part of Agent Skills in October 2025 and opened the spec in December 2025, with adoption varying across Microsoft, OpenAI, Atlassian, Figma, and others (some support the full spec, others read SKILL.md files but execute them differently). Google Labs [open-sourced DESIGN.md](https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-design-md/) on April 21st, 2026, where it remains at alpha. None of these is a formal standard yet, in the W3C or ISO sense. They are open conventions backed by their originating vendors, with overlapping but distinct adoption curves.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*cURpCZgYih7ly14l4TqYZA.jpeg)

They are not the same thing, and they don’t compete for the same job. Most design system practitioners I talk to are unclear about where each one fits, which is fair, because the marketing copy makes them sound interchangeable when they aren’t.

## AGENTS.md is project instructions for coding agents

AGENTS.md is the oldest of the three and the easiest to understand. It lives at the root of your code repository, and it tells coding agents (Codex, Cursor, Windsurf, GitHub Copilot, and dozens of others) how to operate inside the project. Build commands, test commands, lint rules, naming conventions, the things you’d tell a new engineer on their first day. Claude Code is a notable exception, since it still uses CLAUDE.md instead, though the formats are interchangeable in practice and many teams symlink one to the other. The agents themselves differ in how they handle precedence too. Codex walks from the project root down and lets the closest file win. Cursor merges. Some tools treat the file as always-on context, others load it only when relevant. The format is portable but the behaviour around it isn’t fully consistent yet.

The format is plain markdown. There’s no required structure, but the spec recommends sections like Project Overview, Development Environment, Build and Test Commands, Code Style Guidelines, Testing Instructions. Community best practice converges on under 150 lines (Factory’s docs put it bluntly: [“Long files slow the agent and bury signal”](https://docs.factory.ai/cli/configuration/agents-md)), because token cost rises faster than usefulness once a file passes that threshold.

Here’s roughly what one looks like for a team with a design system:

```c
# Acme Platform Web App

## Overview
A TypeScript monorepo for Acme's customer-facing product. Built on
Next.js 14 with the App Router, Postgres via Prisma, and the Acme
design system. Components are React + Tailwind, design tokens are
managed in Style Dictionary.

## Repository structure
- \`apps/web/\`, the main customer-facing application
- \`packages/ui/\`, the Acme design system component library
- \`packages/tokens/\`, design tokens (source of truth, DTCG format)
- \`packages/icons/\`, SVG icon set, generated from Figma
- \`docs/\`, internal architecture notes and ADRs
- \`legacy/\`, pre-2024 code, do not touch without approval

## Build and test
- \`pnpm install\` to set up dependencies
- \`pnpm dev\` runs the local dev server on port 3000
- \`pnpm test\` runs Vitest across all packages
- \`pnpm test:e2e\` runs Playwright tests (requires \`pnpm dev\` running)
- \`pnpm lint\` runs ESLint and Biome
- \`pnpm typecheck\` runs \`tsc --noEmit\` across the monorepo
- All checks must pass before opening a PR

## Design system conventions
- Always use components from \`@acme/ui\` when one exists for the
  pattern. Check \`packages/ui/src/components/\` before creating new ones.
- Always use tokens from \`@acme/tokens\` for colour, spacing,
  typography, and radii. Never hardcode hex values, rem units, or
  pixel values for these properties.
- For brand and visual identity questions, consult \`DESIGN.md\` at the
  repo root. It contains the canonical colour values, typography
  scale, and visual rules.
- The Storybook MCP server is available at
  \`https://acme-design-system.chromatic.com/mcp\`. Use it to look up
  component props, variants, and documented usage before generating UI.
- Prefer composition over new components. If you can build the pattern
  by composing existing primitives, do that.

## Code style
- TypeScript strict mode, no implicit any
- Functional components with hooks, no class components
- Named exports, no default exports
- File naming: \`ComponentName.tsx\`, \`ComponentName.test.tsx\`,
  \`ComponentName.stories.tsx\`
- Co-locate tests and stories with the component file

## Boundaries
- Ask before: modifying anything in \`packages/tokens/\` (token changes
  require design review), adding a new component to \`@acme/ui\`,
  changing build configuration, modifying CI workflows.
- Never: modify files under \`legacy/\`, downgrade dependency versions,
  disable type checks or lint rules, commit secrets or \`.env\` files.

## Security considerations
- Secrets and credentials live in \`.env.local\` and AWS Secrets Manager,
  never in the repository.
- API requests from the client must go through \`apps/web/src/lib/api.ts\`
  which handles auth headers and rate limiting.
- Customer data in tests must use the fixtures in \`apps/web/test/fixtures/\`,
  never real records.

## Further reading
- Component patterns and accessibility notes: \`docs/components.md\`
- Token architecture: \`docs/tokens.md\`
- ADRs for major decisions: \`docs/adr/\`
```

AGENTS.md is not, in itself, documentation about your design system. It’s the orchestration layer. Design system rules are one input among many, and the file’s job is to tell the agent where to look for everything else, including which file holds the canonical tokens, where the component library lives, which MCP servers to consult, and whether to use Tailwind utilities or design tokens when they conflict.

If you only adopt one of these formats this quarter, AGENTS.md is the one. A few hours of writing produces a file most coding agents consult repeatedly across everyday tasks.

## SKILL.md is procedural knowledge for specific workflows

SKILL.md is the format inside an Anthropic Skill, which is a folder of instructions an agent loads when it recognises a particular task. A Skill is more than a file. It’s a directory with a SKILL.md at the top, plus any helper scripts or templates the agent might need to complete the workflow.

[Figma’s MCP server](https://help.figma.com/hc/en-us/articles/39166810751895-Figma-skills-for-MCP) ships several of these with its plugin. `figma-use` teaches an agent how to write to the Figma canvas. `figma-generate-design` walks through building a screen from a description, using your components and variables. `figma-implement-design` translates a Figma node into production code, with steps for fetching context, mapping tokens, and validating against a screenshot. `figma-create-design-system-rules` analyses your codebase and writes out a rules file (either AGENTS.md or CLAUDE.md) describing how to translate Figma designs into code that matches your conventions. All of these are authored by Figma and also published through [OpenAI's curated skills directory](https://github.com/openai/skills/tree/main/skills/.curated/), so the same files turn up in two places depending on which agent you're using.

Each Skill is procedural. It tells the agent how to do something, step by step, with conventions and edge cases handled along the way. Here’s the shape, modelled on the real `figma-implement-design` Skill that Figma authored:

```c
---
name: figma-implement-design
description: Translates Figma designs into production-ready application code with
  pixel-perfect fidelity, using the project's design system tokens and components.
  Use when the user provides a Figma URL or node selection and asks for code in
  their repository. If the user wants to create or modify nodes inside Figma
  itself, use figma-use instead.
license: Apache-2.0
---

# figma-implement-design

 these steps in order. Do not skip steps.

## Prerequisites
- The Figma MCP server must be connected. If a tool call fails because
  the server is unreachable, pause and direct the user to set it up
  before continuing.
- The user must provide a Figma URL in the format
  \`https://figma.com/design/:fileKey/:fileName?node-id=1-2\`, or
  select a node directly in the Figma desktop app.
- The project should have an established design system. If one is not
  present, fall back to a sensible default and flag the gap in your
  response.

## Step 1: Fetch the design context
Call the Figma MCP \`get_design_context\` tool with the provided node.
Capture component names, variable bindings, structural relationships,
and any auto-layout properties. If the response is truncated because
the node is too large, call \`get_metadata\` first to see the structure,
then fetch child nodes individually.

## Step 2: Capture a reference screenshot
Call \`get_screenshot\` on the same node. You will use this for visual
comparison once you have generated code. Do not skip this step. Visual
parity without a reference is unreliable.

## Step 3: Inspect the project design system
Look for AGENTS.md or CLAUDE.md guidance on which tokens, components,
and patterns to use. If a Storybook MCP server is available, query it
for components that match what the design shows. Prefer existing
components over generating new ones.

## Step 4: Map Figma values to project tokens
For every colour, font, spacing, and radius value in the design
context, find the matching token in the project. If a Figma value has
no direct project equivalent, prefer the closest project token over
the literal Figma value. Note any mismatches and surface them in your
final response.

## Step 5: Generate the code
Generate the component using project conventions. Use named exports,
strict TypeScript, and the project's preferred styling approach (CSS
modules, Tailwind, styled-components, etc). Do not use Tailwind utility
classes if the project uses tokens directly.

## Step 6: Validate against the screenshot
Render the generated code locally (or describe how the user can) and
compare it side-by-side with the screenshot from Step 2. Check
spacing, colour, typography, and component states. If discrepancies
exist, iterate.

## Edge cases
- If the design uses a component the project doesn't have: build the
  pattern by composing existing primitives. Flag the gap so the team
  can decide whether to add it to the design system.
- If the Figma file uses raw hex values instead of variables: still
  map to project tokens, and note that the Figma file has a token
  hygiene issue.
- If the design system tokens and Figma values truly conflict:
  prefer project tokens for consistency, but adjust spacing or sizing
  to maintain visual fidelity.

## Boundaries
- Never modify the Figma file itself. This skill is read-only against
  Figma. Use figma-use for write actions.
- Never commit generated code directly. Open a PR and let a human
  review.
- Never invent token names. Use tokens that exist in the project, or
  flag the gap.
```

SKILL.md is best understood as a recipe rather than a description of your design system. The agent reads it when it’s told to do a specific thing, follows the steps, and the system metadata it consults along the way lives elsewhere (in your Figma file, in your component manifest, in DESIGN.md, in whichever store the Skill is told to consult).

Skills matter to design system teams in two ways. If you’re using Figma’s MCP server, the bundled Skills handle most of the common workflows, including writing to canvas, generating screens, implementing designs as code, and creating design system rules. If you have unusual conventions (a specific way you handle dark mode, a non-standard token taxonomy, a custom CI step that runs on every component change), writing your own Skills is how you teach those conventions in a way that survives across sessions.

Skills are higher-investment than AGENTS.md. Each one is a self-contained workflow definition with its own testing surface, and most teams don’t need to write their own yet. The bigger task is knowing which built-in Skills they’re benefiting from when they use Figma’s MCP. If you do start writing your own, the SKILL.md file format is portable but the execution model isn’t fully consistent across agents yet. Different tools load Skills differently, invoke them with different triggers, and handle their nested scripts and references with their own conventions. The file will be readable everywhere, though that doesn’t mean it will run the same way everywhere.

## DESIGN.md is your visual identity, condensed

DESIGN.md is the newest and, depending on your view, either the most useful or the most redundant of the three. It’s a markdown file with a YAML front matter block of design tokens, followed by a markdown body of prose describing the visual identity. [The official spec](https://github.com/google-labs-code/design.md) defines eight standard sections in a fixed order. Overview, colours, typography, layout, elevation and depth, shapes, components, and do’s and don’ts.

Here’s a more detailed example, extending the “Heritage” sample from Google’s own [spec README](https://github.com/google-labs-code/design.md/blob/main/README.md):

```c
---
version: alpha
name: Heritage
description: A premium editorial product, anchored in high-contrast
  neutrals with a single Boston Clay accent.
colors:
  primary: "#1A1C1E"
  secondary: "#6C7278"
  tertiary: "#B8422E"
  tertiary-dark: "#A03A28"
  neutral: "#F7F5F2"
  surface: "#FFFFFF"
  on-surface: "#1A1C1E"
  error: "#9F2D1C"
typography:
  display:
    fontFamily: Public Sans
    fontSize: 64px
    fontWeight: 600
    lineHeight: 1.05
    letterSpacing: -0.03em
  h1:
    fontFamily: Public Sans
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.02em
  h2:
    fontFamily: Public Sans
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
  body-lg:
    fontFamily: Public Sans
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
  body-md:
    fontFamily: Public Sans
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.1em
rounded:
  none: 0
  sm: 4px
  md: 8px
  lg: 12px
  full: 9999px
spacing:
  base: 16px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 32px
  xl: 64px
  gutter: 24px
  margin: 32px
components:
  button-primary:
    backgroundColor: "{colors.tertiary}"
    textColor: "{colors.neutral}"
    rounded: "{rounded.sm}"
    padding: 12px
    typography: "{typography.label-caps}"
  button-primary-hover:
    backgroundColor: "{colors.tertiary-dark}"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: 12px
---

## Overview
Architectural minimalism meets journalistic gravitas. The interface
evokes a premium matte finish, a high-end broadsheet or contemporary
gallery. The product should feel considered, slow, and trustworthy.
Avoid anything that reads as playful, app-like, or busy.

## Colors
The palette is rooted in high-contrast neutrals and a single accent
colour that does all the interactive work.

- **Primary (#1A1C1E):** Deep ink used for headlines and core text.
  Provides maximum readability and a sense of permanence.
- **Secondary (#6C7278):** Sophisticated slate used for borders,
  captions, and metadata.
- **Tertiary (#B8422E):** "Boston Clay" used exclusively for primary
  actions and critical highlights. Never decorative.
- **Neutral (#F7F5F2):** Warm limestone background. Provides a softer,
  more organic foundation than pure white.
- **Surface (#FFFFFF):** Used only for elevated content cards.

## Typography
Two families. Public Sans carries the narrative voice. Space Grotesk
handles technical data, timestamps, and metadata where geometric
precision matters more than warmth.

- **Display and headlines:** Public Sans Semi-Bold. Institutional,
  trustworthy, slightly tightened tracking at larger sizes.
- **Body:** Public Sans Regular at 16px with 1.6 line height. Long-form
  readability is the priority.
- **Labels and metadata:** Space Grotesk, uppercase, with generous
  letter spacing. Reserved for technical data, captions, and small UI
  labels where the editorial voice would feel out of place.

## Layout
A fixed-max-width grid for desktop (max 1200px), fluid below 768px.
Strict 8px spacing scale with a 4px half-step for micro-adjustments.
Generous internal padding (24px) on content containers. Avoid dense
data tables outside dedicated data views.

## Elevation & Depth
Depth is achieved through tonal layers, not heavy shadows. The neutral
background separates from white surface cards through colour alone.
Where elevation is required (modals, popovers), use a single soft
shadow at low opacity. No multi-layer shadow stacks.

## Shapes
Architectural sharpness. All interactive elements use a 4px corner
radius. The 12px radius is reserved for content cards. Pure circles
only for avatars and status indicators. Never mix sharp and pill
shapes in the same view.

## Components
- **Buttons:** Primary is Boston Clay on neutral. Secondary is outlined
  in primary on surface. No tertiary or ghost variants. Use a link if
  the action is low-priority.
- **Inputs:** Surface background, secondary border, primary text. Focus
  state uses the tertiary colour at 2px width.
- **Cards:** Surface background, no border, 12px radius, 24px internal
  padding.

## Do's and Don'ts
- Do use the tertiary colour only for the single most important action
  per screen.
- Do maintain WCAG AA contrast ratios (4.5:1 for body text, 3:1 for
  large text and UI components).
- Do use Space Grotesk only for technical data and small labels.
- Don't mix rounded and sharp corner radii in the same view.
- Don't use more than two font weights on a single screen.
- Don't apply the tertiary colour decoratively. It is always
  interactive intent.
- Don't introduce additional accent colours. The palette is fixed.
```

The format ships with a CLI validator (`npx @google/design.md lint`) that flags broken token references, structural issues, and likely WCAG AA contrast failures. It will catch obvious problems, not subtle ones, and shouldn't be confused with a full accessibility audit. There's also a diff command for comparing versions, and a [community catalogue of DESIGN.md files](https://github.com/VoltAgent/awesome-design-md) extracted from public sites like Stripe, Vercel, Linear, Notion, and Cursor.

DESIGN.md is, functionally, a compressed version of your visual style guide, sized to fit in an LLM’s context window. The hex values are real and the rules are explicit, but anything that doesn’t survive that compression (rationale paragraphs, principle pages, long examples) doesn’t make the file. It is not, despite the YAML token block at the top, a replacement for a full token architecture. DESIGN.md tokens are a flat agent-facing surface. A [DTCG token system](https://www.designtokens.org/) carries semantic structure, themes, modes, and tier separation that DESIGN.md doesn’t try to encode, and the two layers are complementary rather than interchangeable.

DESIGN.md matters most to teams using AI design tools (Google Stitch, Lovable, v0) where the agent doesn’t have access to your Figma library and needs to generate UI from a prompt. If your engineers use Cursor or Claude Code against an existing codebase with components already built, DESIGN.md is less load-bearing because the agent can read your component implementations directly. If you’re starting from scratch every time, DESIGN.md is the file that prevents every prompt producing a different visual treatment.

## Storybook, Zeroheight, and the plumbing underneath

The three markdown formats sit alongside a parallel stack of MCP servers and component metadata standards. These matter to the explainer because the formats reference each other.

[Storybook 10.3 ships an MCP addon](https://storybook.js.org/docs/ai/mcp/overview) that exposes your Storybook content to agents through a Storybook Component Manifest, a JSON file listing components, props, stories, and documentation in a token-efficient format. The agent queries the manifest to understand what components exist before generating UI. [Chromatic publishes these manifests](https://www.chromatic.com/docs/mcp/) as part of its hosting service, with a free tier that covers most teams’ needs.

[Zeroheight has its own MCP server](https://help.zeroheight.com/hc/en-us/articles/48004395674011-zeroheight-MCP-overview) doing similar work, exposing the design system documentation hosted in Zeroheight to agents. Diana Wolosin’s team at Indeed has been publishing extensively on building custom MCP servers from MDX documentation, with parsers that auto-sync metadata when docs change.

The pattern across all of these is the same. Take design system content that already exists in a rich human-facing format (Storybook stories, Zeroheight pages, MDX docs) and expose a structured, machine-readable subset of it to agents through an MCP server. The markdown formats (AGENTS.md, SKILL.md, DESIGN.md) handle the gaps the MCP servers don’t cover.

One thing to flag while we’re here. Every one of these files is read as agent instructions, which means content inside them can influence what the agent does. Anyone who can edit your AGENTS.md, SKILL.md, or component manifest can shape agent behaviour, and instructions delivered through MCP payloads increasingly need the same review discipline teams already apply to code and CI configuration. Prompt injection isn’t theoretical when your design system documentation is an executable input.

## Walking one decision through the stack

Take a single design decision, your product’s primary colour, and trace where it shows up.

The canonical value probably lives in a JSON tokens file, formatted to the [W3C Design Tokens Community Group](https://www.designtokens.org/) spec, compiled through Style Dictionary into CSS variables, native outputs, and a Figma variables library. One source of truth, multiple consumers, versioned and governed. I’ve written about this layer in [Your tokens have become infrastructure](https://blog.murphytrueman.com/your-tokens-have-become-infrastructure/).

From there it propagates. DESIGN.md hardcodes the value in YAML frontmatter and references it by name in prose, with no automatic link back to the JSON. AGENTS.md references it indirectly through a rule like “use tokens from `@acme/tokens`, never hardcode colours," which is durable but contextless. A Figma Skill encodes the procedure for finding it (read design context, identify the variable, look up the project token) without storing the value at all. The Storybook Component Manifest surfaces it as a prop default or token reference generated automatically from your stories.

So the same decision lives in five places now, derivable in principle from the tokens file but rarely derived in practice unless someone has built the pipeline. The question this raises is governance, not technology.

## The empirical work most people aren’t reading

There’s a piece of practitioner research that’s relevant and underread. [Diana Wolosin at Indeed](https://dianawolosin.medium.com/) parsed 77 components from MDX documentation and ran an MCP benchmark across 1,056 prompts and eight different metadata configurations to find out which format produced the most consistent LLM reasoning. As reported in her writing and the Into Design Systems coverage, Markdown queries consumed around 30,000 tokens with 82% coverage and visible hallucinations, while JSON delivered higher accuracy with 80% fewer tokens and roughly 5x lower annual cost. These numbers come from one team’s setup at Indeed and may not generalise to every design system or model. Her rule of thumb, drawn from the work, was “JSON for MCP, Markdown for LLM.” Structured component data like APIs, props, and variants belongs in JSON. Prose guidance for the model belongs in Markdown.

Her benchmark and the writing around it landed before DESIGN.md, and the alignment between her findings and what’s been shipped since matters. DESIGN.md ships YAML front matter (a JSON-adjacent structured layer) with markdown prose, which matches the broad shape of her finding. AGENTS.md is pure markdown, SKILL.md is markdown with frontmatter metadata, and component manifests are JSON. The community’s empirical work and the vendor formats are pointing in similar directions, but they aren’t coordinated. In practice, the benchmark question is being answered incrementally by whichever format gets adopted into real tooling next.

That gap matters because the answer to “what format do agents read best” is still being decided format by format, vendor by vendor, while practitioners run their own benchmarks and arrive at conclusions that may or may not match what’s being shipped. If your design system team is investing in DESIGN.md because Google published and open-sourced it, you’re trusting that Google’s bet matches the empirical reality that practitioners like Diana are measuring. So far the bets are close. They might not stay that way.

## Who owns the seams

A design system team that started 2025 maintaining tokens, components, and a documentation site now maintains a JSON tokens file, a component manifest (probably generated from Storybook), an AGENTS.md, possibly a DESIGN.md, possibly a handful of SKILL.md files, and a Zeroheight MCP server endpoint. None of those existed eighteen months ago. None of the existing governance models were designed for them.

Most teams don’t have a clear answer to who owns the agent-facing layer. Tokens are usually owned by design systems, and AGENTS.md is usually owned by engineering. Figma Skills configs sit somewhere between design tooling and platform engineering. DESIGN.md, if anyone owns it at all, is owned by whoever wrote it first. The seams between them are where things break, and there’s no role on the org chart whose job is to keep the seams healthy.

The practical move is to decide, for each layer of your system, what the canonical compressed source is and who maintains it. Tokens stay in JSON, owned by design systems. Engineering conventions belong in AGENTS.md, maintained by engineering. Visual identity goes into DESIGN.md, owned by whoever holds the brand in your organisation. Component metadata is generated from your Storybook into a manifest with no separate file to maintain, and workflow knowledge sits in SKILL.md files owned by whoever runs the agent tooling. The rich documentation gets generated from these sources or fills the gaps they leave.

That’s a clearer architecture than most teams have today. It’s also more work than most teams are scoped for, which is the real problem nobody is solving.

## Where to start

If you’re feeling behind on any of this, you probably aren’t. Most teams haven’t started either. Here’s a realistic sequence.

If you have nothing today, write an AGENTS.md. It takes a couple of hours and immediately improves every agent interaction with your codebase. Point it at your tokens file, your component library, your conventions. Very little else on this list returns as much for so little work.

If you use Storybook, install the MCP addon next. The Storybook Component Manifest gets generated automatically and gives agents structured component knowledge without you writing it twice.

If you use AI design tools (Stitch, Lovable, v0) or your team is generating UI from prompts often, write a DESIGN.md. Run the linter on it. Add a reference to it from your AGENTS.md so agents know where to find it.

Don’t write your own Skills until you have a specific repeating workflow that warrants the investment. The built-in Figma Skills cover most teams’ needs today.

The question for your team is whether you’re shaping the formats that touch your system or accepting whatever the next release decides.