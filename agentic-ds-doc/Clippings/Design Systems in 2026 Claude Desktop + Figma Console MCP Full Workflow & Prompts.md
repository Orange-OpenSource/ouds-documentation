---
title: "Design Systems in 2026: Claude Desktop + Figma Console MCP Full Workflow & Prompts"
source: "https://www.designsystemscollective.com/design-systems-in-2026-claude-desktop-figma-console-mcp-full-workflow-prompts-fe74ed7efe4a"
author:
  - "[[Garima Agarwal]]"
published: 2026-04-14
created: 2026-06-30
description: "Design Systems in 2026: Claude Desktop + Figma Console MCP Full Workflow & Prompts The practical guide with copy-paste prompts that actually work. You’ve set up Claude Desktop + Figma Console MCP …"
tags:
  - "clippings"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*MdbpOqmXpQqzDmF-)

> The practical guide with copy-paste prompts that actually work.

You’ve set up Claude Desktop + Figma Console MCP ([if not, read Part 1 here](https://medium.com/@garimaagarwal1200/claude-desktop-figma-console-mcp-complete-setup-guide-2026-babba46b12a0)). Now what?

What you’ll learn:

- What Claude Desktop + Figma Console MCP actually is
- The 8-step workflow (high-level)
- Real prompts you can copy-paste
- Dos and don’ts that save hours
- How to avoid token consumption nightmares
- Getting to Storybook without losing your mind

The result: I built a production-ready design system (185 tokens, 8 components, 305 variants, full Storybook integration) in a week. Manual time estimate: 3 weeks.

Let’s go.

## Understanding the Tools

## What is Claude Desktop + Figma Console MCP?

Claude Desktop is Anthropic’s native desktop application. The desktop app supports Model Context Protocol (MCP), which allows Claude to connect directly to external tools and services.

Figma Console MCP is an open-source plugin built by TJ Pitre that bridges Claude Desktop to your Figma file. It’s not an official Figma product, it’s a community-built tool, and it’s genuinely impressive. While the official Figma MCP has around 13 tools, the Console MCP provides 92+ tools covering everything from reading and writing variables to creating components, executing arbitrary JavaScript in Figma’s plugin context, capturing screenshots, and generating multi-layer component structures programmatically.

Think of it this way: Claude can *see* your Figma file, *read* every variable, *write* new components, *rename* text styles, and *take screenshots* to verify its own work, all through natural language conversation.

## The 8-Step Workflow (Overview)

Here’s the order that works:

1. Setup — Get Claude connected to Figma — [Read](https://medium.com/@garimaagarwal1200/claude-desktop-figma-console-mcp-complete-setup-guide-2026-babba46b12a0)
2. Foundations — Define all tokens first (colors, typography, spacing)
3. Checkpoint — Validate Claude understands your system
4. Components — Build on top of solid foundations
5. Audit — Check variable coverage and consistency
6. Documentation — Generate developer specs
7. Export — Get design\_tokens.json in W3C format.
8. Storybook — Convert to React components with stories
9. Claude Skills — Teach Claude to remember your design system. *(Covered in Part 3 — coming next)*

Why this order?

Building components before tokens = hardcoded values everywhere. You’ll spend hours fixing it later. Start with foundations, always.

## Phase 1: Foundations First

## Why Tokens Before Components

This is the #1 mistake people make. They jump straight to “create me a button.”

Without a token system, Claude invents random values:

- Button uses 16px padding
- Input uses 12px padding
- Card uses 20px padding

Now you have 3 spacing values with no system.

The right way: Define your spacing scale first. Then every component references the same tokens.

## What to Define

Your foundation includes:

- Colors — Primitives + semantic tokens (light & dark mode)
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*jN4b8iN7EcIgLAWW)

- Typography — Font families, sizes, weights, line heights
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*eW378GN4Qi85W40v)

- Spacing — Base scale (4px, 8px, 16px, etc.)
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*YIeQ__W0UfDB-huE)

- Shadows & Effects — 6 multi-layer elevation styles
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*LCDWPBaTsssgJvvJ)

- Icon Sizes — Consistent sizing
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*4pYWIzgeN-eInuBB)

- Opacity — Reusable opacity values
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*eppxIYGymnKRiYKC)

- Semantic Naming = Everything. This is non-negotiable.

❌ Bad naming:

```hs
blue-600
gray-dark
spacing-large
button-bg
```

✅ Good naming:

```hs
primitive/blue/600
semantic/primary/default
semantic/primary/hover
spacing/component/padding-md
color/surface/neutral-subtle
```

Why it matters:

Semantic tokens describe purpose and state. When Claude sees semantic/primary/default, it knows this is for primary actions in default state. When you switch to dark mode, you update one alias and everything updates.

## Prompts That Work

Starting Prompt (Context Setting)

Copy-paste this and customize for your project:

```hs
I'm building a design system called [Your System Name]. Here's the context:
```
```hs
Brand: [Professional/playful/modern/etc.]
Tech stack: [React/Vue/etc.]
Target users: [Enterprise/consumers/etc.]
Accessibility: WCAG AA minimum
Color approach: [Describe your color strategy]
Design philosophy: [Component-first/minimal/etc.]Constraints:
- Must support light and dark mode
- Mobile-first responsive
- Keyboard navigation throughout
- Minimize bundle sizeBefore we start building, acknowledge you understand this context and summarize the key principles back to me.
```

Token Creation Prompt

```hs
Create a design token system in Figma with these specifications:
```
```hs
COLORS:
- Primitive layer: Raw color scales (Blue: 50-900, Gray: 50-900, Green, Red, Yellow, Orange)
- Semantic layer: Purpose-based tokens that alias to primitivesSemantic token format: semantic/[category]/[state]
Examples: 
- semantic/primary/default
- semantic/primary/hover
- semantic/text/on-primary
- semantic/surface/neutral-subtleTYPOGRAPHY:
- Families: [Your fonts]
- Sizes: [12, 14, 16, 18, 20, 24, 32, 40, 48, 64px]
- Weights: 400, 500, 600, 700
- Format: typography/[usage]/[size]SPACING:
- Base unit: 4px
- Scale: 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96px
- Format: spacing/[context]/[size]BORDER RADIUS:
- Values: 0, 4, 8, 12, 9999px
- Format: radius/component/[component-name]Create separate variable collections for:
1. Colors (light mode)
2. Colors/Dark (dark mode overrides)
3. Spacing
4. Border Radius
5. Typography
6. Icon SizesUse descriptive names and add descriptions to each token explaining its purpose.
```

Validation Checkpoint Prompt

After Claude creates tokens, validate understanding:

```hs
Before we move to components, show me:
```
```hs
1. How many color tokens did you create?
2. Give me 3 examples of semantic token names
3. What's our base spacing unit?
4. List the typography size scale
5. Confirm light and dark mode collections exist
6. Show me how semantic tokens alias to primitivesThis is a quick verification to ensure we're aligned.
```

## Phase 2: Building Components

## The HTML Artifact Approach

This saved me hours and tons of tokens.

The strategy:

1. Generate HTML artifact first (preview in browser)
2. Iterate until it looks right
3. Then push to Figma

Why? HTML artifacts cost almost no tokens compared to Figma writes. Iterate freely, push once.

## Component Creation Prompts

Button Component

```hs
Build a Button component set in Figma with:
```
```hs
Variants:
- Primary, Secondary, Outline, GhostSizes:
- Small (32px height), Medium (40px), Large (48px)States:
- Default, Hover, Pressed, DisabledIcon support:
- Icon Left, Icon Right, Icon Only, No IconRequirements:
- All fills, strokes, and text must bind to semantic variables (no hardcoded values)
- Use typography/body-md for Medium buttons
- Use semantic/primary/default for Primary variant background
- Use spacing/component/padding-* for internal spacing
- Apply proper border radius from radius/component/buttonTotal variants: 4 variants × 3 sizes × 4 states × 3 icon configs = 144 variantsAfter creation, take a screenshot so I can review.
```

Input Component

```hs
Create an Input Field component set with:
```
```hs
Types:
- Text, Email, Password, Number, SearchSizes:
- Small (32px), Medium (40px), Large (48px)States:
- Default, Focused, Error, DisabledFeatures:
- Label (optional)
- Helper text (optional)
- Error message (conditional on Error state)
- Prefix/suffix icon supportToken requirements:
- Border: semantic/border/default
- Border (focused): semantic/border/focus
- Border (error): semantic/border/error
- Background: semantic/surface/input
- Text: semantic/text/primary
- Placeholder: semantic/text/subtleBind all values to variables. Take a screenshot when done.
```

Card Component

```hs
Build a Card component with:
```
```hs
Elevation levels:
- Flat (no shadow), Raised (subtle shadow), Elevated (prominent shadow)Padding options:
- Compact (16px), Default (24px), Spacious (32px)States:
- Default, Hover, Pressed, DisabledStructure:
- Header (optional)
- Body (content area)
- Footer (optional, for actions)Use:
- semantic/surface/card for background
- Elevation tokens for shadows
- spacing/component/padding-* for internal spacing
- radius/component/card for cornersScreenshot after creation.
```

## The Audit > Iterate > Finalize Loop

After creating each component:

Audit Prompt:

```hs
Audit this [component name] for:
```
```hs
1. Variable coverage - Are ALL fills, strokes, and text bound to variables? List any hardcoded values.
2. Naming consistency - Do variant names follow our conventions?
3. Token accuracy - Is each property using the correct semantic token?
4. Accessibility - Are focus states visible? Does text meet contrast requirements?
5. Responsiveness - Does it work at different sizes?Give me a scored report and flag any issues.
```

Fix Prompt (if issues found):

```hs
Fix the issues you found:
- Replace hardcoded [#hexvalue] with semantic/[correct-token]
- Rename variants to match [naming pattern]
- Add missing [state/variant]
```
```hs
Then verify with another screenshot.
```

## Time-Saving Techniques

- Batch similar components — Create all form elements in one session
- Use artifacts for exploration — Try 3 button styles in HTML before committing
- Set up templates — Save working prompts for reuse
- Screenshot everything — Visual confirmation catches issues fast
- Session summaries — End each session with “Summarize what we built today”

## Phase 3: Documentation & Export

## Developer-Ready Documentation

Developers need more than just Figma files.

Documentation Prompt:

```hs
Generate developer documentation for the [Component Name] component:
```
```hs
Include:
1. Component description (what it's for, when to use it)
2. Anatomy (what parts make up the component)
3. Props/Variants (all configurable options)
4. States (default, hover, pressed, disabled, etc.)
5. Token map (which design tokens are used where)
6. Accessibility notes (ARIA labels, keyboard navigation, focus management)
7. Usage guidelines (dos and don'ts)
8. Code example structure (pseudo-code for React)Format as markdown.
```

## Token Export

Export Prompt:

```hs
Export all design tokens from this Figma file as design_tokens.json in W3C Design Token Community Group format.
```
```hs
Include:
- All variable collections
- Resolved values
- Alias chains (show which semantic tokens point to which primitives)
- Descriptions
- Token type ($type: color, dimension, fontFamily, etc.)
- Light and dark mode splitsOrganize by collection, then by category.
```

This JSON becomes your source of truth for Storybook, CSS custom properties, and any other platform.

## Phase 4: Storybook Integration

## High-Level Process

1. Token extraction (done above)
2. Convert to CSS custom properties
3. Build React components (reference CSS variables)
4. Generate Storybook stories
5. Add dark mode toggle

## React Component Conversion

Conversion Prompt:

```hs
Convert the [Component Name] Figma component into a React + TypeScript component.
```
```hs
Requirements:
- Use CSS custom properties for all styling (--color-primary-default, --spacing-md, etc.)
- Props should match Figma variants (variant, size, state, disabled, etc.)
- No hardcoded values
- Include TypeScript types
- Support all states from FigmaExample structure:
- variant: 'primary' | 'secondary' | 'outline' | 'ghost'
- size: 'small' | 'medium' | 'large'
- disabled: boolean
- icon?: 'left' | 'right' | 'only'Show me the component code.
```

## Storybook Stories

Story Generation Prompt:

```hs
Create a Storybook story file (.stories.tsx) for the [Component Name] component.
```
```hs
Include:
1. Default story (all props configurable via controls)
2. Individual stories for each variant (Primary, Secondary, etc.)
3. State showcase story (all states side by side)
4. Dark mode story (with data-theme="dark" toggle)
5. Documentation (component description, prop descriptions)Follow Storybook 7+ CSF3 format.
```

## Final Output

What you get:

- React components with zero hardcoded values
- Full Storybook with interactive playground
- Dark mode toggle that works instantly
- Documentation embedded in Storybook
- Token system developers can extend

## Dos and Don’ts

## ✅DO:

- Start with semantic token naming: Spend 30 minutes planning your token architecture. It saves days later.
- Use HTML artifacts for iteration: Generate, preview, iterate in browser. Push to Figma when finalized.
- Break work into focused sessions: 3–4 hour blocks with clear stopping points. Save session summaries.
- Run checkpoint audits: Ask Claude to verify understanding before building 50 components.
- Verify variable coverage: After every component, check: “Are all values bound to variables?”
- Keep Desktop Bridge plugin running: Check it every hour. If it closes, all tool calls fail.
- Batch similar operations: Create all color tokens at once, not one by one.

## ❌ DON’T:

- Skip foundations and jump to components: You’ll spend days fixing hardcoded values.
- Use hardcoded values (even “temporarily”): It’s never temporary. Bind to variables from the start.
- Try to build everything in one session: Token limits and context window limits will stop you.
- Ignore token consumption: Design system work uses tokens fast. Plan accordingly.
- Forget to check plugin connection: Silent failures waste time. Verify connection status at session start.
- Expect AI to make design decisions: Claude executes your vision. You still make the calls.
- Assume first output is production-ready: Always audit. Check coverage. Iterate 2–3 times.

## Managing Token Limits (The Real Talk)

This was my biggest frustration.

How fast do tokens get consumed?

In a 3-hour component-building session, I hit usage limits twice. Design system work is token-intensive.

Strategies that work:

- Be specific upfront — Detailed prompts reduce back-and-forth iterations
- Use HTML artifacts — Much cheaper than Figma writes
- Batch operations — Create 10 variables at once, not one at a time
- Save session summaries — Resume efficiently without re-explaining
- Plan work blocks — Don’t try to do everything in one day
- Preview before pushing — Verify in HTML before writing to Figma

Realistic expectations:

If you’re on Claude free version, expect to hit limits during intensive work. Budget extra time for cooldowns or split work across multiple days.

## Common Challenges & Solutions

## Challenge: Plugin Disconnects

The Desktop Bridge plugin closes randomly, especially in long sessions.

Fix: Check connection status at the start of every work block. Keep Figma window visible so you notice if it closes.

## Challenge: Context Window Limits

After building 15+ components in one conversation, Claude starts forgetting earlier tokens or making inconsistent decisions.

Fix: Start a new conversation for each component category (buttons/forms/navigation/etc.). Reference the finalized JSON from previous work.

## Challenge: What Still Needs Human Input

Claude cannot:

- Make brand decisions (what should “primary blue” actually be?)
- Evaluate visual taste (is this spacing “right”?)
- Understand your specific users
- Replace design review and stakeholder sign-off

Fix: Use Claude for execution speed. You still own design judgment.

Worth it?

For design system work specifically, yes. The structured, token-first nature is a perfect fit for this workflow. Time savings are real, output quality is high, and the handoff process is dramatically better.

## Next Steps

You now have the workflow and prompts to build a design system with Claude Desktop + Figma Console MCP.

In Part 3, I’ll show you how to turn your design system into a Claude Skill so it never forgets your tokens, naming conventions, or component specs. Every new conversation will start with full knowledge of your system.

Want to get started?

1. Make sure you’re set up ([Part 1 here](https://medium.com/@garimaagarwal1200/claude-desktop-figma-console-mcp-complete-setup-guide-2026-babba46b12a0))
2. Start with foundations (use the token creation prompt above)
3. Build your first component (Button is ideal)
4. Audit, iterate, finalize
5. Move to documentation and Storybook

Your turn: What component are you building first? Drop a comment — I’d love to hear how this workflow works for you.