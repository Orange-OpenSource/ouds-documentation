---
title: "Agent orchestration for design systems"
source: "https://www.designsystemscollective.com/agent-orchestration-for-design-systems-da0f6a5f24fb"
author:
  - "[[Cristian Morales Achiardi]]"
published: 2026-01-21
created: 2026-06-15
description: "Agent orchestration for design systems Setting up strategies, context and tools for design system agentic workflows. A user needs to copy a code snippet. Simple interaction. The action is “copy to …"
tags:
  - "clippings"
---
## Setting up strategies, context and tools for design system agentic workflows.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*zCSfvV4vEMzx4IAXn5vMcA.png)

A user needs to copy a code snippet. Simple interaction. The action is “copy to clipboard.” The component is CopyButton.

But CopyButton doesn’t exist in isolation. When the copy succeeds, the icon changes from a clipboard to a checkmark. A Tooltip appears: “Copied to clipboard.” The feedback loop requires two components working together, nested in a specific relationship.

If you ask an agent without design system infrastructure to build this interaction, it might create CopyButton correctly. It might even add a Tooltip. But it won’t know that CopyButton *already contains* Tooltip in your system. It won’t know that the composition pattern exists and is documented. It will reinvent what’s already built, or worse. Create a second Tooltip implementation that drifts from the original.

Design systems are compositional. Components nest inside components. Atoms combine into molecules. Molecules combine into organisms.

Understanding a design system means understanding these chains. Not just what exists, but how things connect. Design system infrastructure traces relationships.

## Skills, rules, and instructions

Before diving into the design system pipelines, I need to clarify how the instruction architecture works. Three layers, each with a distinct purpose:

**Skills are tools.** Executable capabilities that perform specific operations. `/ai-component-metadata` generates structured documentation. `/ai-ds-composer` guides component selection. `/codebase-index` regenerates dependency maps. Skills are reusable across projects — the metadata generator works on any component library that follows the schema.

**Rules are context.** Passive constraints and guidelines that load based on what you’re working on. The metadata schema that defines required fields. The atomic design hierarchy that enforces dependency direction. The deep tracing methodology that teaches recursive traversal. Rules are project-specific — they encode *your* system’s decisions.

**Instructions are strategy.** The methodology that binds skills and rules together. When to load the codebase index. How to approach different types of queries. What artifacts to produce and where they feed.

### The hierarchy:

```hs
CLAUDE.md (the router)
    ↓ points to
Rules (path-specific context)
    ↓ which reference
Skills (reusable capabilities)
    ↓ which produce
Artifacts (metadata, indexes, traced relationships)mark
```

Skills came first. I built `/ai-component-metadata`, `/ai-ds-composer`, and `/codebase-index` to solve specific design system problems. Then I needed rules to give them project context. Then I needed efficient loading so the rules wouldn't bloat every conversation.

The architecture evolved from the tools up, not the theory down.

## Strategies for better agentic design systems workflows

When I ask “what atoms are used on the homepage,” a shallow answer lists direct imports: BaseLayout, ThoughtsSection, FeaturedSkillsSection. But atoms don’t appear at the page level. They’re nested deeper.

## 1- Deep tracing

The deep tracing algorithm is recursive traversal with cycle detection:

1. Start with direct imports on the target page
2. For each import, check its `uses` field in the relationship graph
3. If `uses` is not empty, recursively check those components
4. Continue until you reach components with `uses[0].`No dependencies
5. Filter results by category to find atoms

**The deep tracing rule encodes this methodology:**

```hs
---
paths: "src/components/.ai/**"
---
# Deep Dependency Tracing
When tracing atoms (or any leaf-level components), 
 dependency chains to their terminal nodes.
✗ Wrong: Stopping at First Level
  CopyButton uses[1]: Tooltip  ← If you stop here, you miss Tooltip!
✓ Correct: Tracing to Leaf Nodes
  CopyButton uses[1]: Tooltip
    → Tooltip uses[0]:  ← Tooltip is a leaf node (atom) - FOUND
```

The rule loads when the agent is working with index files. It teaches the agent *how* to read the map, not just that the map exists.

**Here’s what that looks like on my portfolio’s homepage:**

```hs
index.astro uses[4]: BaseLayout, ThoughtsSection, FeaturedSkillsSection, ProjectsCarouselSection

→ BaseLayout uses[6]: Nav, Footer, CustomCursor, NoiseOverlay, AnimatedUnderlines, BackToTop
  → Nav uses[2]: MenuItem, Image
    → MenuItem uses[2]: Link, Icon
      → Link uses[0]:         ← ATOM FOUND
      → Icon uses[0]:         ← ATOM FOUND
    → Image uses[0]:          ← ATOM FOUND
  → Footer uses[4]: Heading, Text, Link, Icon
    → Heading uses[0]:        ← ATOM FOUND
    → Text uses[0]:           ← ATOM FOUND
    → Link uses[0]:           ← (already found)
    → Icon uses[0]:           ← (already found)
→ FeaturedSkillsSection uses[2]: SkillCard, SectionViewMore
  → SkillCard uses[2]: Button, CodeBlock
    → Button uses[0]:         ← ATOM FOUND
    → CodeBlock uses[1]: CopyButton
      → CopyButton uses[1]: Tooltip
        → Tooltip uses[0]:    ← ATOM FOUND (commonly missed!)
```

Every branch. Every level. Until you reach components with no dependencies. Recursive tracing finds the Tooltip three levels down.

## Why deep tracing matters for design systems

**Building UI from user flows.** When you translate “user copies code snippet” into implementation, you need to know which components handle that action. The action maps to CopyButton. But the full implementation requires knowing CopyButton’s composition, that it already includes the Tooltip feedback pattern. Without that knowledge, you either duplicate work or create inconsistency.

**Deprecation impact analysis.** If I want to deprecate Tooltip, what breaks? Shallow analysis says “nothing uses Tooltip directly.” Deep tracing reveals CopyButton depends on it, CodeBlock depends on CopyButton, SkillCard depends on CodeBlock. The change cascades through three levels of composition. Without tracing, you delete a component that’s actively used.

**Accurate adoption reports.** My experiment showed control group agents reporting 43–44 components when 57 existed. They missed nested dependencies. They marked Tooltip as “unused” when it was actively rendering on every page with code snippets. False negatives in adoption reports lead to bad decisions; removing components that are actually critical, or underestimating the impact of changes.

## 2- Instance counting

Imports tell you a component will be used on a page/screen. Instance counts tell you how many times is actually being used.

### How instance counting works

The agent reads actual file content, not just import graphs. It parses component tags in templates:

```hs
<!-- dashboard.astro -->
<DashboardCard title="Metrics">...</DashboardCard>
<DashboardCard title="Usage">...</DashboardCard>
<DashboardCard title="Components">...</DashboardCard>
```

Three instances of DashboardCard on one page. But DashboardCard internally uses Icon twice. So the real count includes:

- DashboardCard: 3 instances (direct)
- Icon: 6 instances (3 cards × 2 icons per card)

This is where deep tracing and instance counting combine. You trace the composition chain, then multiply at each level. The algorithm handles edge cases: slot components (don’t double-count slotted content), conditional rendering (count as potential instance), loops (note that actual count depends on data).

## Real numbers from my codebase

From my December 2025 adoption report, I improved the logic the enabled deep tracing and instance counting that gave me the perfect vantage point to understand my system.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*thJOCjPjGSfGI8eBNvuTVQ.png)

This surfaced not just numbers, but design and architecture patterns of my design system. Im still tweaking the logic to represent components used on dynamically generated pages (like the blog). You can check the [full dashboard](https://www.giorris.dev/dashboard) on my website.

## Efficiency rate as a diagnostic

Here’s what this looks like when the agent spots an anomaly. From my adoption report:

> **Tag component:** Category/skill labels (CSS classes used instead)  
> **Recommendation:** Tag component adoption — Replace CSS classes with Tag component (2–3 hours effort)

The agent noticed Tag has imports but CSS classes (`.pill`, `.pill-alt`) are used instead. Developers are bypassing the component system. The agent doesn't just count — it identifies the shadow implementation and flags it as technical debt.

Another example:

> **Spacer component:** Vertical/horizontal spacing (utility classes preferred)  
> **Analysis:** Atom layer shows moderate adoption at 63%, primarily due to intentional preference for utility classes over Container/Spacer components.

Here the agent recognized the low usage wasn’t a problem; it was a design philosophy. The system prefers utility classes for spacing. The component exists as an option, not a requirement. The agent understood *why* atoms were unused, not just that they were.

All of this data (instances per component, efficiency rates, adoption by atomic level ) feeds system health dashboard.

## 3- Hierarchy and structure

Atomic design is usually presented as organization. Atoms in one folder, molecules in another, organisms in a third. Clean. Predictable.

But the hierarchy also produces analytical insight. The rules should reflect how your team actually builds, not an abstract ideal.

The atomic levels reveal system health when combined with instance data.

**From my adoption report:**

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*O_v07KWk0p2lL6GffVI7zw.png)

In my case, the 63% atom adoption reflected a design philosophy: utility classes for spacing (instead of Spacer component), CSS for simple dividers (instead of Divider component). The agent recognized this pattern and reported it as intentional, not as debt.

## 4- Composition patterns: guidelines for building

When the agent needs to build UI, it needs to know the rules of composition.

```hs
---
paths:
  - "packages/ui-react/src/components/**"
---

# Component Composition
## Prefer Editing Over Creating
Before creating a new component:
1. Search for similar components in the index
2. Check if existing component can be extended with new props/variants
3. Compose existing components instead of creating new ones
Create new component only when:
- No similar component exists
- Existing component has fundamentally different responsibility
- Composition would be too complex to maintain
## Example: Prefer Editing
// Don't create PrimaryButton, SecondaryButton, etc.
// Instead, add variant prop to Button:
export interface ButtonProps {
  variant?: 'primary' | 'secondary' | 'ghost' | 'danger';
}
```

This rule prevents proliferation. Without it, agents create new components for every variation. With it, they extend what exists.

The rule also points to a skill:

```hs
For intelligent component selection and composition, 
use the **ai-ds-composer** skill:

/ai-ds-composer
This skill:
- Reads the project metadata hierarchy
- Applies component selection criteria from aiHints
- Checks anti-patterns automatically
- Suggests composition with reasoning
- Flags when no existing component fits (genuinely need something new)
```

The rule provides context (your system’s composition philosophy). The skill provides capability (executing that philosophy). Together, they guide the agent toward building UI that uses the system correctly.

## The feedback loop: reports refine infrastructure

The adoption report isn’t just a snapshot. It’s a feedback mechanism that improves the infrastructure itself.

## Example: Fixing instance counting accuracy

The December report showed Icon count inflation on index.astro: 31 reported, 25 actual. Six phantom icons.

The agent’s analysis identified the root cause: missing slot component detection. Components like Button and Link only contain `<slot />`, not nested components. Icons slotted inside Buttons were being counted twice; once in the parent template (correct), and again when tracing Button's composition (incorrect).

```hs
<!-- SkillCard.astro -->
<Button>
  <Icon name="Download" />  <!-- Counted here (correct) -->
</Button>

<!-- Button.astro -->
<button>
  <slot />  <!-- Icon gets counted again here (wrong!) -->
</button>
```

The fix: add slot component detection to the instance counting algorithm. If a component’s template only contains `<slot />` or HTML elements, don't recursively trace its composition. The slotted content is already counted where it appears.

The implementation plan documented the solution:

> **Before improvements:** Accuracy 75% (directionally correct, component-level errors)  
> **After improvements:** Accuracy 95%+ (total AND component-level correct)

The next report used the improved algorithm. The phantom icons disappeared.

## Example: Timestamps in metadata

The dashboard’s “Modified Date” column showed “N/A” in production. The implementation read filesystem timestamps at runtime, but in serverless environments, source files aren’t available.

The agent’s analysis: timestamps belong in metadata files, not filesystem. They should be:

- Part of the component’s metadata (`*.metadata.ts`)
- Extracted during index regeneration
- Stored in TOON format for efficient consumption
- Read by dashboard from the generated file

The implementation plan added `created` and `modified` fields to the metadata schema. A new script extracts timestamps from all metadata files and generates `timestamps.toon`. The dashboard reads from TOON instead of filesystem.

Result: dashboard works in both development and production. Single source of truth. Automatically updated when the index regenerates.

## The compound effect of feedback

Each report surfaces something. Each insight refines the instructions or scripts. The next report is more accurate, more useful, more aligned with how the system actually works.

This is what makes the infrastructure agentic. The AI’s analysis doesn’t just measure the design system. It improves the measurement process. The rules get sharper. The scripts get more accurate. The artifacts get richer.

The agent moves from consumer to maintainer.

## The agentic design system

I’m writing a series diving into each component:

[**Part 1: Building an AI-Ready design system**](https://www.designsystemscollective.com/building-an-ai-ready-design-system-35e709f54edf)**.** How I accidentally created a RAG pipeline for design systems.

[**Part 2: Towards an agentic design system.**](https://www.designsystemscollective.com/towards-an-agentic-design-system-c7e0a6469bb1) When does AI stop consuming your design system and start governing it?.

[**Part 3: Design system documentation as structured metadata**](https://www.designsystemscollective.com/design-system-documentation-as-structured-metadata-315f62c6eab1)**.** An approach for structured data that AI agents can query to understand when and how to use components correctly.

[**Part 4: Mapping your design system for AI agents**](https://medium.com/design-systems-collective/codebase-indexing-for-design-systems-agents-c0f6b563a39e)**.** Created the map that agents need to understand ***where*** things fit in the system and ***how*** they relate to each other.

→ **Part 5: Orchestration for agentic design systems.** Setting up strategies, context and tools for design system agents.

[**Part 6: Encoding governance on agentic design systems**](https://medium.com/@crmorales.achiardi/encoding-governance-on-agentic-design-systems-1a8c70420fec)**.** How AI makes it possible for a designer to encode, enforce, and guarantee design decisions at scale.

More soon