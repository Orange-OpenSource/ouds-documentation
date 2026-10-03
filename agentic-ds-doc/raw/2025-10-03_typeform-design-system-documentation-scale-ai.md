---
title: "Design System Documentation at Scale: Leveraging AI and Automation"
source: "https://medium.com/typeforms-engineering-blog/design-system-documentation-at-scale-leveraging-ai-and-automation-b09c9e1a8921"
author:
  - "[[Fernando Coelho]]"
published: 2025-10-03
created: 2026-06-22
description: "How Typeform's design system team (Echo) built a documentation pipeline using Notion as headless CMS, Docusaurus, GitHub Actions, and an MCP server — all fed by the same content pipeline."
tags:
  - "clippings"
---

In today's fast-paced development environment, maintaining up-to-date design system documentation while minimizing maintenance overhead presents a significant challenge. At Typeform, we've developed an innovative approach that leverages AI tools and Notion as a headless CMS, and automated workflows to ensure our documentation remains current with minimal manual intervention.

## The challenge

Design systems are living entities that constantly evolve. As components, patterns, and guidelines change, documentation must keep pace. The biggest challenge was having information scattered across multiple platforms. We had Figma for design specs, Notion for guidelines, and Storybook for code examples, with frequent inconsistencies between them. Developers would see one implementation in Storybook that didn't match what designers had documented in Figma, while separate guidelines existed in Notion documents. This fragmentation created confusion, slowed development, and led to implementation errors as team members struggled to identify the single source of truth for any given component or pattern.

Additionally, documentation often becomes siloed in design tools, making it inaccessible to developers who need it most. The distance between Figma documentation and developer-consumed resources creates a communication gap that slows development and introduces inconsistencies. Organizations also face high maintenance costs for custom documentation sites, while contribution friction discourages team members from making regular updates to keep documentation current.

## Our architecture: Monorepo approach

We structured our design system as a monorepo containing both packages and applications.

### Packages

We have 3 core packages in our design system: UI components which contains our React components. Design tokens, which contains our primitives for color, spacing and typography, and Assets which contains our icons, illustrations and other visual elements. These packages also encompass animations with standardized motion patterns and transitions, code snippet examples consumed by multiple applications, and a Notion API Client that fetches and transforms documentation content.

### Applications

Within the monorepo, we maintain a documentation website built with Docusaurus for comprehensive documentation, a Sandbox environment serving as an interactive playground for component experimentation, and an MCP Server providing AI-powered assistance for engineers and designers.

## How the system works

### Notion as a Content Management System

We built a system that democratizes contribution to a bespoke implementation of our documentation website while simultaneously feeding critical design system resources to our Model Context Protocol server. At the core of this approach is Notion, which serves as an accessible content management system where anyone on the team can contribute documentation using a familiar interface. Since our company already extensively uses Notion on a daily basis, it was only natural to leverage it for our documentation needs. This approach lowered the barrier of entry significantly, as we already had the Notion API setup in place. The API enables us to programmatically fetch and transform this content into markdown, which then flows to multiple destinations within our monorepo.

### Leveraging Notion databases for rich metadata

The power of this approach became particularly evident through our use of Notion's database page type. By structuring component documentation as database entries with rich metadata, we created a system that is both easy to update and remarkably information-dense. Each database row can contain API reference links, component status indicators, page thumbnails, and recursive database relationships that link related components and patterns. This structure allows us to generate comprehensive, interconnected documentation while maintaining it through a simple, familiar interface that requires no technical knowledge to update.

### Documentation website with Docusaurus

The documentation website itself is built with Docusaurus, providing the flexibility needed for a fully branded and customized experience. Despite requiring more maintenance than simpler solutions, Docusaurus gives us powerful MDX support for interactive documentation, built-in versioning to track design system evolution, and comprehensive search capabilities. The transformation pipeline converts Notion content into the markdown and MDX formats that Docusaurus consumes, handling everything from simple text blocks to complex code examples and interactive demos.

## Automated publishing pipeline

This architecture enables the production website to be updated without writing a single line of code. A GitHub Actions automation runs weekly and can also be triggered manually, fetching updated content from Notion and opening a pull request with the latest changes. Each PR requires review from both an engineer and a designer, maintaining quality standards while allowing anyone on the team to contribute documentation updates through Notion alone.

### AI-Powered assistance via MCP

The same content pipeline that feeds our documentation website also powers our Model Context Protocol server. The MCP server consumes multiple resources from the monorepo: the markdown documentation generated from the Notion API, our library of design tokens containing variables for colors, spacing, and typography, and the shared code snippets that demonstrate real-world usage patterns. This unified approach means the AI-powered assistant has access to the same documentation, tokens, and examples that developers and designers use, enabling it to provide contextual guidance, suggest appropriate components based on requirements, and highlight accessibility considerations during development.

## Shared code snippets

A critical aspect of our documentation strategy is a package that maintains a single source of truth for code snippets. By consuming this package across the documentation site, sandbox environment, and MCP server, we ensure consistency across all platforms while providing realistic implementation patterns for developers and training data for the AI-powered assistant. To illustrate that, our component pages feature an interactive playground with editable code examples that can be modified in real-time and seamlessly transferred to our sandbox for further experimentation, debugging, and implementation of new features in an isolated environment.

## Benefits realized

This architecture has delivered several key advantages across the organization. Designers benefit from a simplified contribution process through the familiar Notion interface, spending less time maintaining documentation and more time on design work. Developers gain access to always-current documentation through multiple channels, with AI-assisted implementation reducing development time and consistent examples demonstrating best practices. The organization as a whole experiences higher adoption rates of design system components, improved product consistency, reduced design debt through better documentation, and lower maintenance costs despite the sophisticated documentation system.

## Challenges and lessons learned

### Technical hurdles

While our approach has been largely successful, we encountered several technical challenges. We needed to adapt how Notion routes between pages to match Docusaurus's static site routing structure to maintain parity and minimize changes to how team members author content in Notion. Additionally, we implemented a careful fetching strategy to avoid being rate-limited by Notion's API infrastructure.

### Documentation segmentation

Another challenge was determining which content to write in markdown versus which to render as React components for specialized visuals. Styled markdown has limitations when presenting complex interactive examples and custom UI patterns. For instance, our design tokens — while displayed in table format — required rendering complex elements after being consumed by the tokens package.

### Future improvements

We continue to refine our documentation pipeline with plans to implement real-time updates for critical documentation changes and expand MCP capabilities to include code generation from design specs. We're also looking at adding usage analytics to identify documentation gaps and introduce interactive tutorials generated from documentation content.

By combining Notion's user-friendly interface, automated transformation pipelines, and AI-powered assistance, we've created a documentation system that scales with our design system while minimizing overhead maintenance. By creating a custom, streamlined design system documentation solution, we've already seen a big uptick in UI consistency and less back and forth between designers and engineers.

Design system documentation is always a challenge to keep up to date and relevant. By investing in a, on one hand custom, but at the same time automated solution where anyone can contribute all whilst baking in AI and MCP functionality, we can ensure Echo is truly setup for the future.
