---
source_url: https://github.com/google-labs-code/design.md
ingested: 2026-06-26
slug: google-design-md-spec
---

# Google Labs — DESIGN.md (spécification officielle)

**URL** : https://github.com/google-labs-code/design.md
**Auteur** : Google Labs (google-labs-code)
**Licence** : Apache 2.0
**Version** : alpha, v0.2.0 (26 mai 2026)
**Stars** : 15 800 | **Forks** : 1 500

## Description

A format specification for describing a visual identity to coding agents. DESIGN.md gives agents a persistent, structured understanding of a design system.

## Le Format

A DESIGN.md file combines machine-readable design tokens (YAML front matter) with human-readable design rationale (markdown prose). Tokens give agents exact values. Prose tells them *why* those values exist and how to apply them.

```
---
name: Heritage
colors:
  primary: "#1A1C1E"
  secondary: "#6C7278"
  tertiary: "#B8422E"
  neutral: "#F7F5F2"
typography:
  h1:
    fontFamily: Public Sans
    fontSize: 3rem
  body-md:
    fontFamily: Public Sans
    fontSize: 1rem
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 0.75rem
rounded:
  sm: 4px
  md: 8px
spacing:
  sm: 8px
  md: 16px
---

## Overview
Architectural Minimalism meets Journalistic Gravitas. The UI evokes a
premium matte finish — a high-end broadsheet or contemporary gallery.

## Colors
The palette is rooted in high-contrast neutrals and a single accent color.
- **Primary (#1A1C1E):** Deep ink for headlines and core text.
- **Secondary (#6C7278):** Sophisticated slate for borders, captions, metadata.
- **Tertiary (#B8422E):** "Boston Clay" — the sole driver for interaction.
- **Neutral (#F7F5F2):** Warm limestone foundation, softer than pure white.
```

An agent that reads this file will produce a UI with deep ink headlines in Public Sans, a warm limestone background, and Boston Clay call-to-action buttons.

## CLI

```
npx @google/design.md lint DESIGN.md
npx @google/design.md diff DESIGN.md DESIGN-v2.md
npx @google/design.md export --format json-tailwind DESIGN.md
npx @google/design.md export --format css-tailwind DESIGN.md
npx @google/design.md export --format dtcg DESIGN.md
```

## Token Schema

```yaml
version: <string>
name: <string>
description: <string>
colors:
  <token-name>: <Color>
typography:
  <token-name>: <Typography>
rounded:
  <scale-level>: <Dimension>
spacing:
  <scale-level>: <Dimension | number>
components:
  <component-name>:
    <token-name>: <string | token reference>
```

## Section Order (canonical)

1. Overview / Brand & Style
2. Colors
3. Typography
4. Layout / Layout & Spacing
5. Elevation & Depth
6. Shapes
7. Components
8. Do's and Don'ts

## Linting Rules (9 rules)

- broken-ref (error) : token references qui ne résolvent pas
- missing-primary (warning) : pas de couleur primary définie
- contrast-ratio (warning) : paires bg/text sous WCAG AA (4.5:1)
- orphaned-tokens (warning) : tokens définis mais jamais référencés
- token-summary (info) : compte de tokens par section
- missing-sections (info) : sections optionnelles absentes
- missing-typography (warning) : couleurs sans typographie
- section-order (warning) : sections hors ordre canonique
- unknown-key (warning) : clé YAML ressemblant à une faute de frappe

## Export formats

- json-tailwind : Tailwind v3 theme.extend config
- css-tailwind : Tailwind v4 @theme { ... } block
- dtcg : W3C Design Tokens Format Module (tokens.json)

## Component Tokens

```yaml
components:
  button-primary:
    backgroundColor: "{colors.tertiary}"
    textColor: "{colors.on-tertiary}"
    rounded: "{rounded.sm}"
    padding: 12px
  button-primary-hover:
    backgroundColor: "{colors.tertiary-container}"
```

Valid component properties: backgroundColor, textColor, typography, rounded, padding, size, height, width.

## Status

Format alpha, spec active. Publié open-source depuis Google Stitch le 21 avril 2026.
