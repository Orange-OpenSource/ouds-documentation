# Design Systems MCP: The Complete Guide

**Source** : https://www.intodesignsystems.com/design-systems-mcp
**Auteurs / conférenciers** : Diana Wolosin (Indeed), Jesse Gardner (New York State), Laura Fehre (Figma), Romina Kavcic (The Design System Guide)
**Contexte** : Synthèse de 4 talks de l'AI Design Systems Conference 2026 par Into Design Systems
**Ingéré le** : 2026-06-17

---

## What is a Design System MCP?

A Model Context Protocol (MCP) gives AI agents on-demand access to external tools and structured knowledge. A design system MCP codifies your components, tokens and guidelines into machine-readable metadata so LLMs can query and generate UI code that conforms to your system. This guide is based on real talks from 4 speakers at the AI Design Systems Conference 2026 by Into Design Systems: Diana Wolosin (Indeed, with her 1056-prompt benchmark), Jesse Gardner (New York State), Laura Fehre (Figma) and Romina Kavcic (The Design System Guide).

## Key concepts

- **AI is a new user** (Diana Wolosin, Indeed): Your design system was written for humans. The new user is AI, and it needs structured metadata, not documentation prose.
- **MCP deterministic, LLM stochastic** (Diana Wolosin, Indeed): Same MCP query returns the same data every time. Same MCP results sent to the LLM produce different reasoning each time. Structured data mitigates that randomness.
- **JSON for structured data, Markdown for rules** (Diana Wolosin, Indeed): JSON for MCP component APIs (props, sizes, variants): it's a contract. Markdown for natural-language instructions and rules for the LLM.
- **Progressive disclosure of context** (Diana Wolosin, Indeed): Always-on rules for foundations (spacing, color, typography), MCP on-demand for components, AGENTS.md as orchestration layer. Together they form a plugin.
- **Foundations must be always-on** (Diana Wolosin, Indeed): MCP only returns what you asked for. If the prompt says 'build me a card,' the LLM fills gaps with assumptions. Spacing and color belong in always-on rules.
- **Guidelines are not laws** (Laura Fehre, Figma): Writing more rules into a guideline file doesn't control the outcome. In nearly 100% of cases the prompt will win over the guidelines.
- **Don't just plug MDX into an MCP** (Diana Wolosin, Indeed): Connecting human documentation to an MCP is 5x more expensive and less accurate than structured JSON. Diana's benchmark proved this on Indeed's real design system.
- **Code as source of truth for MCP** (Jesse Gardner, New York State): JSDoc on Lit web components feeds the MCP with props, types, and usage guidance. Design and code stay in sync through a single structured source.

## Diana's MCP benchmark findings

- Setup: Cursor plus Claude Sonnet 4.5 plus Indeed's design system MCP, stored in Vectra (open source vector DB). 22 prompts run 3 times each across 8 MCP configurations for a total of 1,056 prompts.
- Formats tested: Markdown MDX (the original human docs), plain Markdown, hybrid Markdown + JSON, JSON (baseline and variations), and TOON (Token-Oriented Object Notation designed for AI).
- Metrics: Input quality (cost, average tokens, relevance, query coverage) and output quality (coverage, hallucinations, average props found).
- Finding #1: MCP is deterministic, LLM is stochastic. Same input to MCP returns the same output. Same MCP results sent to the LLM produce different reasoning each time.
- Finding #2: Structured data mitigates AI uncertainty. Hybrid (MD + JSON) showed the most variation across runs and was unreliable. JSON showed the most consistency.
- Finding #3: JSON has the highest accuracy when verified against actual documentation, and uses 80% fewer tokens than hybrid Markdown for equal or better accuracy.
- Winner: JSON. Sharpest responses at the lowest token cost.

## Real-world implementations

**Indeed (Diana Wolosin):** 77 components processed via JavaScript parsers (one per knowledge domain: accessibility, development, localization, design) generating structured JSON. Original MDX in GitLab → parsers built with Cursor → JSON → ingestion into Vectra vector DB. Pipeline auto-triggers on every MDX update. The pilot produced 4,300 AI prototypes in 4 months using React design system components and Indeed Visual Language.

**New York State (Jesse Gardner):** Web components built with Lit and TypeScript, Figma parity via Code Connect. Custom MCP server exposes components and tokens documented via JSDoc with usage guidance baked in. Rich JSDoc → custom element manifest → MCP server. Fed a 5-page foster-adoptive parent PDF into Claude Code to generate a working multi-step NY State-styled form in 13 minutes. "50-80k tokens wasted when you point AI at raw custom elements code."

**Figma (Laura Fehre):** Experiment translating Figma Make output (React, Tailwind, shadcn, Radix) into SwiftUI for a Notes app clone. Cursor parsed Apple Human Interface Guidelines URL into structured markdown files, drag-and-dropped into Figma Make's code editor with a mapping file translating Radix components to HIG components.

**The Design System Guide (Romina Kavcic):** Tidy Figma plugin with 66 MCP tools: audits naming, scores health across 6 categories, validates new variables, composes patterns (login form, destructive confirmation) from existing components. Paired with Observatory, a dashboard visualizing the knowledge graph across Figma, GitHub, Storybook, Linear, Chromatic, Playwright and PostHog.

## How to build your design system MCP (9 steps)

1. Start small — Just add naming conventions, 5–10 components. Plant seeds, not trees. (Romina Kavcic)
2. Codify foundations first — Naming conventions, token taxonomy, component intent. Structure before automation. (Romina Kavcic)
3. Pick a parser strategy — JavaScript parsers per knowledge domain (a11y, dev, localization, design) that read MDX and emit JSON. (Diana Wolosin)
4. Use JSON for structured data — JSON for component APIs, props, sizes, variants. Markdown with frontmatter for natural-language rules. Don't dump MDX as-is. (Diana Wolosin)
5. Build the pipeline — Ingestion → chunking → indexing → vector database. Vectra is open source. (Diana Wolosin)
6. Automate freshness — Trigger the parser on every MDX update so metadata is always current. (Diana Wolosin)
7. Add always-on rules and AGENTS.md — Foundations go into always-on rules. MCP is on-demand, rules are safety net. (Diana Wolosin)
8. Benchmark before committing — Test multiple formats. Measure cost, accuracy, hallucinations. (Diana Wolosin)
9. Add usage guidance, not just APIs — JSDoc with "use filled for primary action, outline for secondary." Guidance is useful for both humans and AI. (Jesse Gardner)

## Common mistakes

- Don't just plug MDX into an MCP: 5x more expensive, less accurate.
- Don't expect rules alone to control output: the prompt wins in nearly 100% of cases. (Laura Fehre)
- Don't put everything in one big markdown file: overstretches context window. (Laura Fehre)
- Don't rely on MCP for foundations: MCP is on-demand, spacing/color must be always-on.
- Don't point AI at the raw codebase: 50–80k tokens fills the context window. (Jesse Gardner)
- Don't skip designers in the loop: vibe coding without systems thinkers recreates silos. (Jesse Gardner)

## Citations clés

- "AI is a new user. And just like you design components for humans to use, you now need to codify your knowledge so LLM can consume it, reason over it and build with it." (Diana Wolosin)
- "JSON is like a contract. It has explicit keys, explicit values, explicit boundaries and there is no ambiguity." (Diana Wolosin)
- "You don't unlock AI infrastructure by writing better prompts. You unlock it by closing the gap between design and code." (Jesse Gardner)
- "Code generation is becoming a commodity. But what's not becoming a commodity is trustworthy implementation. And that's the gap." (Jesse Gardner)
- "Markdown isn't about formatting. It's about communication. It's about making your intent visible and building something that both humans and machines can actually agree on." (Laura Fehre)
- "Guidelines are not laws. In nearly 100% of cases the prompt will win over the guidelines." (Laura Fehre)
- "The MCP is deterministic, the LLM is stochastic. Same input, different output. Structured data mitigates AI uncertainty." (Diana Wolosin)
