# How Uber Built an Agentic System to Automate Design Specs in Minutes

**Source** : https://www.uber.com/us/en/blog/automate-design-specs/
**Auteur** : Ian Guisard (Lead, Uber Base design system)
**Date** : March 11, 2026
**Tags** : design-system, agentic, MCP, figma, specs, accessibilite, open-source

---

## Contenu brut

Uber Base design system serves thousands of engineers, and every component they ship depends on specs that are accurate, complete, and current. When those specs fall behind, engineering builds from assumptions instead of definitions, which causes inconsistencies and tech debt.

## uSpec

uSpec is an agentic system that connects an AI agent in Cursor to Figma through the open-source Figma Console MCP. The agent crawls your actual component and sub-component structure, compiles that data with any additional context you provide, and generates finished spec pages directly in your Figma file in minutes. The entire pipeline runs locally, so no proprietary design data ever leaves your network.

## The Enterprise Documentation Problem

A complete component spec includes:
- **Anatomy**: Numbered markers identifying each element of a component with an attribute table
- **API**: Every configurable property, its values, and defaults
- **Properties**: Variant axes and boolean toggles with instance previews
- **Color annotation**: Each element mapped to its design token across states
- **Structure**: Heights, padding, and spacing across size and density variants
- **Screen reader**: Accessibility properties for VoiceOver, TalkBack, and ARIA

The screen reader section alone covers 3 accessibility APIs, each with hundreds of properties: VoiceOver modifiers and traits, TalkBack semantics, and ARIA roles and states. Designers spend hours cross-referencing references, and a single wrong property means a broken experience for assistive technology users.

Uber's design system has hundreds of components shipping across 7 implementation stacks: UIKit, SwiftUI, Android XML, Android Compose, Web React, Go, and SDUI. Each component spec serves as the single reference for all of them.

## The Process (2 steps)

**Step 1: Share a Figma Link and Context**
Open Cursor and reference an agent skill with your Figma component link. Add context about states, variants, or platform-specific behavior that the agent can't infer from the design alone.

**Step 2: The Agent Reads Your Figma File and Renders the Spec**
The AI agent connects to your Figma file through the Figma Console MCP, extracts component structure, design tokens, variables, and styles, then maps the parent-child relationships between layers and sub-components to render a finished spec page directly in your Figma file. No intermediate steps, no manual formatting—the agent goes from reading the component to placing the completed documentation in one pass.

## Agent Skills per Spec Section

| Skill | What it generates |
|---|---|
| Anatomy | Numbered markers on a component instance with an attribute table |
| API | Properties, values, defaults, and configuration examples |
| Properties | Variant axes and boolean toggles with instance previews |
| Color annotation | Token mapping for every element and state |
| Structure | Dimensions, spacing, and padding across variants |
| Screen reader | VoiceOver, TalkBack, and ARIA in a single pass |

## How It Works Under the Hood

Two layers work together: agent skills that carry the spec-writing expertise, and an MCP bridge that gives the agent direct read-write access to your Figma file.

**Agent Skills Encode Domain Knowledge**: Each skill loads its own instruction file with validation rules, structured schemas, and reference documentation. The screen reader skill, for example, loads platform-specific accessibility property references before analyzing the component. The agent doesn't guess at property names—it selects from documented APIs.

**The Figma Console MCP Connects the Agent to Figma**: The MCP connects the agent to Figma through a local connection to Figma Desktop. The MCP connection enables something that screenshot analysis can't: the agent crawls the component tree, identifies sub-component structures and slot-based compositions, detects when designers have used variables in place of variants, and translates Figma's internal modeling patterns into clean API documentation.

**The Agent Renders Directly in Figma**: Once the agent has built a complete picture of the component, it imports the matching documentation template from your library, detaches it, and populates it—filling text fields, cloning sections, building tables, and placing markers—all through the MCP. There's no intermediate output.

Programmatic plugins can extract component data from Figma, but they can't interpret what that data means. uSpec combines both: AI judgment where interpretation matters—classifying accessibility semantics, selecting the right token mappings, deciding how to structure a spec—and programmatic scripts where precision matters, rendering the result directly in Figma.

## Why This Matters at Enterprise Scale

- **Security**: The entire pipeline runs locally. No cloud API, no proprietary design data leaving your network.
- **Consistency**: Every spec follows the same structure. Structured schemas and templates enforce it, not authors.
- **Speed**: A full screen reader spec covering 3 platforms generates in under 2 minutes.
- **Accuracy**: The agent reads real token names and variant values from Figma. No transcription errors.
- **Multi-platform**: One prompt generates iOS, Android, and Web accessibility specs in a single pass.
- **Maintainability**: Changelogs update directly in Figma via MCP with a single prompt.

A system with hundreds of components that previously required months of spec-writing can generate complete specs in days.

## Open Source Foundation

uSpec depends on the Figma Console MCP, built by Southleft (TJ Pitre) and released as open source. It's the bridge between an AI agent and Figma.

"We built the Figma Console MCP because we needed it for our own enterprise engagements. When we decided to open source it, that was about paying back the community that made us who we are." — TJ Pitre, CEO of Southleft

uSpec is open-source on GitHub: https://github.com/redongreen/uSpec
Full process documented at: https://uspec.design

## What Comes Next

Ideas on the roadmap: drift detection, code-to-spec generation, and new spec types.
