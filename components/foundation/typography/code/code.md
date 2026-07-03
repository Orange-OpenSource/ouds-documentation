# Guideline

## Intro 👈🤖

Code is the monospace style for technical content — snippets, commands, and identifiers — preserving character alignment in a single, consistent size.

---

## Definition

The Code style is dedicated to technical content such as code snippets, commands, system values, and identifiers. It uses a monospace typeface to preserve character alignment and improve readability of structured content. Available in a single size, it provides a consistent presentation of technical information throughout the product. Its use should be limited to content that requires an accurate code-like representation.

---

## Best for 👈🤔

✅ Inline code snippets and keywords within running text

✅ Multi-line code blocks and configuration examples

✅ Terminal commands and shell instructions

✅ System values, tokens, and identifiers

✅ File paths, URLs, and environment variables

✅ API endpoints, parameters, and response samples

✅ Error codes and log output

✅ Any content where character alignment must be preserved

✅ Distinguishing literal, copyable text from surrounding prose

✅ Technical documentation requiring an accurate code-like representation

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Font family | Theme `code` monospace font-family token | N |
| 2 | Monospace metrics | Fixed-width glyphs that preserve character alignment | N |
| 3 | Font size | Single, consistent Code type size | N |
| 4 | Line height | Vertical rhythm tuned for readable structured content | N |
| 5 | Letter spacing | Tracking suited to monospace technical text | N |
| 6 | Font weight | Weight applied to Code content | N |

---

# Specs

## States

🚧 Not applicable — Code is a non-interactive typography style and has no interactive states.

---

## Layout and spacing

🚧 Content to be added

---

# Accessibility 👈🤖

## Accessibility intro

Code styles must meet WCAG 2.2 Level AA, staying legible and resizable while clearly signalling technical content to everyone. For comprehensive guidance, see the [Orange Unified Design System Accessibility Overview](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability).

---

## Accessibility Challenges

Monospace technical text introduces specific challenges: it must keep sufficient contrast, remain resizable and reflowable (or scroll predictably for long lines), and its code-like meaning should be conveyed semantically rather than by appearance alone.

### Key Challenges

- Maintaining ≥4.5:1 contrast for code text on its background
- Handling long lines without trapping content off-screen
- Conveying "this is code" semantically, not by monospace styling alone
- Keeping code legible and resizable up to 200% zoom

### Critical Success Factors

1. Use semantic `<code>`/`<pre>` elements for inline and block code
2. Keep ≥4.5:1 contrast, including for syntax-colored tokens
3. Allow horizontal scroll within the code block rather than clipping content
4. Use relative units so code resizes with user settings

---

## Design Requirements

### Structure & Labels

- [ ] **Semantic markup**: Use `<code>` for inline and `<pre><code>` for blocks ([Structure guidance](https://a11y-guidelines.orange.com/en/web/develop/page-structure/))
- [ ] **Meaning not style-only**: Don't rely on the monospace look alone to signal code
- [ ] **Copy support**: Ensure code text is selectable and copyable

### Visual Design

- [ ] **Contrast**: Meet ≥4.5:1 for code and any syntax-highlight colors ([Contrast guidance](https://a11y-guidelines.orange.com/en/web/design/color-and-contrast/))
- [ ] **Long lines**: Scroll the block horizontally instead of clipping content
- [ ] **Resize**: Use relative units so code scales to 200%

### Content

- [ ] **Scoped use**: ❌ Monospace for emphasis / ✅ Monospace only for real code ([Content guidance](https://a11y-guidelines.orange.com/en/web/design/textual-content/))
- [ ] **Not color-only**: Don't rely on syntax color alone to convey meaning

---

## Testing Checklist

### Zoom & Reflow Testing

- [ ] Zoom to 200%; confirm code remains legible and long lines scroll rather than clip

### Contrast Testing

- [ ] Check code text and any syntax-highlight colors meet ≥4.5:1

### Structure Testing

- [ ] Confirm inline and block code expose `<code>`/`<pre>` semantics to assistive tech

Resources: [Orange Accessibility Testing Guide](https://a11y-guidelines.orange.com/en/web/testing/)

---

## Key WCAG Criteria

- **1.4.3 Contrast (Minimum)** (AA): Code text meets ≥4.5:1 contrast
- **1.4.4 Resize Text** (AA): Code resizes to 200% without loss of content
- **1.4.10 Reflow** (AA): Long code scrolls within its block without breaking the page
- **1.3.1 Info and Relationships** (A): Code semantics conveyed programmatically
- **1.4.1 Use of Color** (A): Syntax meaning not conveyed by color alone

For complete reference: [Orange Accessibility Guidelines](https://a11y-guidelines.orange.com/en/web/)

---

## Additional Resources

- [Orange Accessibility Guidelines - Typography](https://a11y-guidelines.orange.com/en/web/design/typography/)
- [W3C WAI - Content Structure](https://www.w3.org/WAI/tutorials/page-structure/)
- [WCAG 2.2 Understanding Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)
- [Orange Design System - Accessibility & Sustainability](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability)

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Jun 16, 2026 | 1.0.0 | <ul><li>Component creation</ul> | Maxime Tonnerre<br>Jérôme Regnier |
