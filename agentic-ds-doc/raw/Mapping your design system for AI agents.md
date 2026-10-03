---
title: "Mapping your design system for AI agents"
source: "https://www.designsystemscollective.com/codebase-indexing-for-design-systems-agents-c0f6b563a39e"
author:
  - "[[Cristian Morales Achiardi]]"
published: 2026-01-14
created: 2026-06-15
description: "Mapping your design system for AI agents Without a map, AI explores. With a map, AI navigates. The difference is determinism. This article is about system design, it might be super technical but …"
tags:
  - "clippings"
---
## Without a map, AI explores. With a map, AI navigates. The difference is determinism.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*4ALBhtCcE0mfF107PuuNEQ.png)

Cover generated with Midjourney

*This article is about system design, it might be super technical but totally necessary for those wanting to go deep into agentic design systems.*

I built ThoughtCard for the blog archive page. A clickable card with cover image, title, excerpt, date. Dashed border that brightens on hover. The whole thing wrapped in an anchor tag.

A few weeks later, I asked Claude to create a ThoughtsSection for the homepage. Same cards, different container. Claude created the section component. It even imported ThoughtCard at the top of the file. Then it recreated the cards from scratch. Raw HTML. Inline styles. The import sat there unused.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*GVzp3-Fqo5gUALZFbzvUNQ.jpeg)

Thoughts section on giorris.dev

This was worse than not knowing the component existed. The import was right there. Claude found it, referenced it, then ignored it.

This kept happening. Links written as `<a>` tags instead of using my Link atom. Buttons with hardcoded styles instead of the Button component. Every time I asked for something new, there was a coin flip: would Claude actually use the existing building block, or just acknowledge it and reinvent anyway?

Exploration mode works fine for prototyping. For production code, it creates drift. Inconsistent styling. Duplicated logic. Technical debt that compounds with every generation.

The component metadata files solve ***what****.* They document component APIs, usage patterns, selection criteria. But Claude still needed to understand ***where*** things fit in the system and ***how*** they relate to each other. It needed a map.

## The cost of not having a map

I ran an experiment. Eleven trials over four days. Same model (Claude Sonnet 4.5), same codebase, same questions. The only variable: whether Claude had access to pre-indexed architecture.

Without infrastructure, Claude explored. It ran `find src/components`, grepped for imports, read files one by one. It took 4-5 minutes per run. And it missed things.

The codebase had 55 components. Claude found 43–44. It missed layouts, pages, components in subdirectories that `find` didn't catch. The structure of my project (what counted as a component, where they lived) wasn't something Claude could infer from file paths alone.

Worse: Claude made false negatives. It reported Tooltip as “unused” when Tooltip was actively used. The problem was the dependency chain. Tooltip lives inside CopyButton. CopyButton lives inside CodeBlock. CodeBlock lives inside SkillCard. SkillCard appears on multiple pages.

If you grep for `<Tooltip>` in my pages, you find nothing. Tooltip is three levels deep. But it's very much in use.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*wOVC5Ugl5NfvWSdQvCwvWQ.png)

Tooltip component relationship graph

When Claude reported Tooltip as unused, that wasn’t just a wrong metric. That was a refactoring recommendation. “You should delete this component.” If I’d followed that suggestion, I would have broken copy-to-clipboard functionality across the site.

## What the index actually contains

The solution was to pre-compute relationships and give Claude a queryable map. Three pieces:

### 1\. Component inventory

Every component, its category, its path, whether it has metadata:

```hs
components:
  Button:
    path: src/components/atoms/Button/Button.astro
    category: atoms
    metadata: true
  ThoughtCard:
    path: src/components/molecules/ThoughtCard/ThoughtCard.astro
    category: molecules
    metadata: true
```

### 2\. Relationship graph

Who uses whom. Who is used by whom:

```hs
ThoughtCard:
  uses[0]:
  usedBy[2]: ThoughtsSection, [slug].astro
  
CopyButton:
  uses[1]: Tooltip
  usedBy[1]: CodeBlock
  
Tooltip:
  uses[0]:
  usedBy[1]: CopyButton
```

This is where the Tooltip problem gets solved. Claude doesn’t need to grep. It reads the graph. Tooltip is used by CopyButton. CopyButton is used by CodeBlock. The chain is explicit.

### 3\. Summary statistics

Total counts, metadata coverage, relationship density:

```hs
summary:
  totalComponents: 55
  componentsWithMetadata: 54
  relationshipsMapped: 302
```

Claude loads this once. Around 4,000 tokens for the full index. Then it answers questions by reasoning over the cached data instead of re-reading files.

## The format problem

JSON would work. But JSON has overhead. Brackets, quotes, colons, commas. For structured data with consistent shape like a component index, that syntax tax adds up.

I found [TOON](https://github.com/toon-format/toon) through a LinkedIn post. It’s a format designed for token efficiency. Same semantics as JSON, 30–60% fewer tokens in some cases.

```hs
// JSON: 89 characters
{"Button":{"path":"src/components/atoms/Button","category":"atoms","metadata":true}}
```
```hs
// TOON: 67 characters
Button:
  path: src/components/atoms/Button
  category: atoms
  metadata: true
```

The savings compound. My full index is around 300 relationships. The token reduction matters when you’re loading context at the start of every conversation.

TOON works because my data has consistent structure. Every component has the same fields. When structures vary wildly, the format loses its advantage. For codebase indexing, it’s a good fit.

## Deep tracing: following the chain

The index tells Claude that Tooltip exists and that CopyButton uses it. But some questions require following the full chain.

“List all atoms used on the homepage.”

The homepage imports BaseLayout, ThoughtsSection, FeaturedSkillsSection. Those are direct imports. But atoms live deeper. BaseLayout contains Nav. Nav contains MenuItem. MenuItem contains Link and Icon.

To find atoms, Claude needs to trace recursively:

```hs
index.astro
  → BaseLayout
    → Nav
      → MenuItem
        → Link (atom)
        → Icon (atom)
      → Image (atom)
    → Footer
      → Heading (atom)
      → Text (atom)
      → Link (atom)
      → Icon (atom)
```

The tracing rules are documented in the protocols. When Claude reads the index files, it also loads instructions for how to traverse them. “For questions about atoms, follow dependency chains to leaf nodes. Components with `uses[0]` are terminal."

This is where the Tooltip case gets caught. When tracing atoms through SkillCard → CodeBlock → CopyButton, the chain ends at Tooltip. `uses[0]`. It's a leaf node. It's an atom. It's actively used.

## Instance counting: imports vs. usage

The index tracks import relationships. ThoughtCard is imported by 2 files. But import count isn’t the same as usage.

A page might import Button once but have five instances. The metadata dashboard on my site shows this distinction:

- Total components: 55
- Total instances: 530
- Component efficiency: 9.6x (average instances per component)
- Most instanced: Icon.astro with 126 instances

Instance counting requires parsing templates, not just imports. Count `<Button>` tags, not `import Button` statements. The algorithm handles nesting. If Card contains two Buttons, and the page has three Cards, that's six Button instances.

There’s an edge case with slots. Button contains a `<slot />`. If I write `<Button><Icon /></Button>`, the Icon instance belongs to the parent scope, not to Button's internals. The counting rules handle this: detect slot components, don't recurse into them for instance counting.

These details matter for adoption metrics. Import count tells you how many files reference a component. Instance count tells you how much the component actually gets used.

## Query protocols: teaching Claude how to read the map

The index files are data. The protocols are instructions.

```hs
# Query Optimization Rules

When answering questions about codebase structure:
1. Check context first. Before any file read, verify if data 
   exists from previous tool calls.

2. Never re-read relationship files. If component-usage.toon 
   was loaded earlier, use that data.

3. Follow-up questions should be cheap. Q3 and Q4 should reason 
   over cached data, not trigger new reads.
```

These rules eliminate the variance I saw in early trials. Without protocols, Claude would sometimes cache data and sometimes re-read files. The token cost for follow-up questions ranged from 0 to 36,000 depending on which approach Claude chose.

With protocols, the behavior is deterministic. Load the index once. Reason over cached data for follow-ups. My optimized trials showed 0.04% variance across runs. The protocols converted exploration into directed analysis.

I adapted the indexing approach from [Cursor’s codebase indexing documentation](https://cursor.com/docs/context/codebase-indexing). The core insight transfers: pre-compute what you can, give the agent structured data instead of making it explore every time.

## ROI calculation

The index and protocols cost more tokens upfront. You’re loading instructions, relationship graphs, and component inventories before the agent writes a single line of code. In my benchmarks, the indexed approach used slightly more tokens per session (~28K vs ~27K).

But looking at ***session cost*** misses the point. The real cost is the **technical debt** that accumulates when agents guess.

When an agent works without a map (Exploration Mode), it incurs a small “drift tax” on every interaction:

- **Duplication:** It recreates a Button because it couldn’t find the existing one.
- **Inconsistency:** It hardcodes hex values because it missed the design tokens.
- **False Negatives:** It suggests deleting “unused” code that is actually critical deep in the dependency tree.

This is **compound technical debt**. You pay for the generation tokens today, but you pay 10x that amount next week when you have to refactor five different versions of a “Card” component or debug a broken utility chain.

The indexed approach effectively front-loads this cost. You pay an “accuracy premium” at the start of the context window to ensure zero drift. The result is that I spend my time describing *what* a section should do, rather than code-reviewing *how* Claude decided to style it.

## The indexing workflow

The index is auto-generated. A Python script scans `src/components`, parses imports, builds the relationship graph, outputs TOON files. Run it after adding or removing components. Commit the output alongside your code.

```hs
"""
Codebase Indexer
Scans a codebase to generate a token-efficient relationship map (TOON format).
"""

# Configuration for detecting various frameworks
FRAMEWORK_CONFIGS = {
    "react":   { "extensions": [".jsx", ".tsx"], "patterns": [...] },
    "vue":     { "extensions": [".vue"], "patterns": [...] },
    "svelte":  { "extensions": [".svelte"], "patterns": [...] },
    "astro":   { "extensions": [".astro"], "patterns": [...] },
    "angular": { "extensions": [".ts"], "patterns": [...] },
}

class TOONEncoder:
    """
    Custom Encoder for 'Token-Optimized Object Notation' (TOON):
      1. Removing structural quotes
      2. Minimizing delimiters
      3. Using whitespace-significant nesting
    """
    def encode(self, data):
        # ... logic to convert dicts to simplified TOON string ...
        pass

class CodebaseIndexer:
    def __init__(self, project_root):
        self.project_root = project_root
        self.relationships = {}

    def scan(self):
        """Main execution flow"""
        self._detect_framework()     # Auto-detects (e.g., Next.js, Astro)
        self._scan_components()      # Maps component hierarchy & imports
        self._scan_utilities()       # Tracks usage of shared utils/lib
        self._scan_schemas()         # Finds data shapes (Zod, TypeScript)
        self._scan_data_queries()    # Extracts API calls & DB queries
        self._scan_styles()          # Maps CSS/Tailwind definitions
        self._generate_outputs()     # Writes the TOON files

    def _generate_outputs(self):
        # Output: .ai/relationships/component-usage.toon
        # Output: .ai/relationships/data-flow.toon
        pass

if __name__ == "__main__":
    # Example Usage
    indexer = CodebaseIndexer("./my-project")
    indexer.scan()
```

It handles the mechanical parts: finding components, tracing imports, detecting metadata files. The protocols handle the semantic parts: what counts as a component, how categories are assigned, when to trace deep vs. shallow.

## What this enables

In Part 3: [**Design system documentation as structured metadata**](https://www.designsystemscollective.com/design-system-documentation-as-structured-metadata-315f62c6eab1) I described an approach for structured knowledge of individual components. This is about giving agents knowledge of the whole system.

Combined, the metadata and index answer different questions:

- **Metadata:** “How do I use Button?” → Check Button.metadata.ts
- **Index:** “Where is Button used?” → Check component-usage.toon
- **Both:** “Should I create a new card component?” → Check index for existing cards, check metadata for their capabilities

The next parts of the series cover what happens when you combine this infrastructure with agent orchestration. When Claude can audit the system, report on patterns, and propose fixes. The index is the foundation that makes those workflows possible.

## The agentic design system

I’m writing a series diving into each component:

[**Part 1: Building an AI-Ready design system**](https://www.designsystemscollective.com/building-an-ai-ready-design-system-35e709f54edf)**.** How I accidentally created a RAG pipeline for design systems.

[**Part 2: Towards an agentic design system.**](https://www.designsystemscollective.com/towards-an-agentic-design-system-c7e0a6469bb1) When does AI stop consuming your design system and start governing it?.

[**Part 3: Design system documentation as structured metadata**](https://www.designsystemscollective.com/design-system-documentation-as-structured-metadata-315f62c6eab1)**.** An approach for structured data that AI agents can query to understand when and how to use components correctly.

→ **Part 4: Mapping your design system for AI agents.** Created the map that agents need to understand ***where*** things fit in the system and ***how*** they relate to each other.

[**Part 5: Orchestration for agentic design systems**](https://medium.com/design-systems-collective/agent-orchestration-for-design-systems-da0f6a5f24fb)**.** Setting up strategies, context and tools for design system agents.

[**Part 6: Encoding governance on agentic design systems**](https://medium.com/@crmorales.achiardi/encoding-governance-on-agentic-design-systems-1a8c70420fec)**.** How AI makes it possible for a designer to encode, enforce, and guarantee design decisions at scale.

More soon

*The codebase-index skill I use is open source and available in my* [*website*](https://www.giorris.dev/skills)*.*

*Note: Treat this as a reference implementation, not a binary you just run. Every design system is structured differently. Your framework might be Svelte, your atomic design folder structure might be unique. Use this as the foundation, then adjust the scripts and folder paths to match your specific architecture.*