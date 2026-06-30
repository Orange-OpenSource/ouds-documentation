# Guideline

## Intro 👈🤖

Body is the workhorse text style for paragraphs and everyday content, tuned for comfortable, readable reading across every screen size.

---

## Definition

Body styles are designed for everyday text content such as paragraphs, descriptions, and informational messages. They prioritize readability and provide a comfortable reading experience across all screen sizes. Multiple size options allow content importance to be expressed while maintaining consistency.
Their typography automatically scales across breakpoints to support responsive layouts.

---

## Best for 👈🤔

✅ Paragraphs and running text in articles, descriptions, and help content

✅ Informational and instructional messages

✅ Card and list descriptions beneath a heading or label

✅ Form helper text and supporting explanations

✅ Introductory or lead paragraphs using the Large size

✅ Dense or secondary content using the Small size

✅ Emphasizing key words or sentences with the Moderate or Strong weight

✅ Long-form reading where comfort and rhythm matter

✅ Responsive layouts that must stay readable across breakpoints

✅ Any default text that isn't a heading, label, or code

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Font family | Theme `body` font-family token defining the typeface | N |
| 2 | Font size | Type size per variant — Large 16px, Medium 14px, Small 12px | N |
| 3 | Line height | Reading-optimized vertical rhythm per size | N |
| 4 | Letter spacing | Subtle positive tracking that aids legibility at text sizes | N |
| 5 | Font weight | Emphasis axis — Default, Moderate, Strong | N |
| 6 | Responsive scaling | Automatic adaptation across breakpoints | N |

---

## Size

**`Large`** The most prominent body text size, ideal for introductory paragraphs, highlighted content, or situations where enhanced readability is desired.

**`Medium`** The default body text size, providing an optimal balance between readability, information density, and visual hierarchy across most use cases.

**`Small`** A compact body text size intended for supporting information, secondary content, and dense layouts where space efficiency is important.

---

## size_do_&_dont 👈🤔

✅ **Do:** Use Medium as the default for most running text and descriptions.  
❌ **Don't:** Default to Large or Small for body copy without a clear hierarchy reason.

✅ **Do:** Use Large for introductory or lead paragraphs that deserve more presence.  
❌ **Don't:** Set long articles entirely in Large, tiring the reader.

✅ **Do:** Reserve Small for supporting, secondary, or dense content.  
❌ **Don't:** Use Small for primary reading content or critical instructions.

✅ **Do:** Keep a comfortable line length and let body text reflow responsively.  
❌ **Don't:** Constrain body text to fixed widths or sizes that hurt readability.

✅ **Do:** Maintain a consistent body size within the same content block.  
❌ **Don't:** Mix multiple body sizes in one paragraph, creating a ragged rhythm.

---

## Weight

**`Default`** The default weight provides the standard level of typographic emphasis for Body and Label styles. It is designed for optimal readability and neutral hierarchy, making it the baseline for most interface content. Use it whenever no additional emphasis is required.

**`Moderate`** Moderate weight increases visual presence while remaining balanced and readable. It is used to reinforce hierarchy within Body and Label typography without introducing strong emphasis. Suitable for highlighting important information or improving scanability.

**`Strong`** Strong weight provides the highest level of emphasis for Body and Label styles. It is intended for critical information, key actions, or elements that must stand out within dense content. Use it sparingly to preserve its impact and avoid visual overload.

---

## weight_do_&_dont 👈🤔

✅ **Do:** Use Default weight for the vast majority of body content.  
❌ **Don't:** Set whole paragraphs in Strong, which removes all emphasis contrast.

✅ **Do:** Use Moderate to gently reinforce hierarchy or improve scanability.  
❌ **Don't:** Reach for Strong when Moderate already provides enough emphasis.

✅ **Do:** Reserve Strong for critical information or key in-line emphasis.  
❌ **Don't:** Scatter Strong across the page, causing visual overload.

✅ **Do:** Pair weight changes with meaning, not decoration.  
❌ **Don't:** Use weight as the only signal for something that needs a semantic element.

✅ **Do:** Keep weight usage consistent for similar content across the product.  
❌ **Don't:** Switch weights arbitrarily between equivalent pieces of content.

---

# Specs

## States

🚧 Not applicable — Body is a non-interactive typography style and has no interactive states.

---

## Layout and spacing

🚧 Content to be added

---

# Accessibility 👈🤖

## Accessibility intro

Body styles must meet WCAG 2.2 Level AA, staying legible, resizable, and reflowable so everyone can read content comfortably. For comprehensive guidance, see the [Orange Unified Design System Accessibility Overview](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability).

---

## Accessibility Challenges

Body text is where most reading happens, so contrast, resizing, spacing, and reflow matter most here. Weight must convey emphasis without becoming the only signal of meaning, and small sizes must remain legible.

### Key Challenges

- Maintaining ≥4.5:1 contrast for normal-size body text on all backgrounds
- Supporting text resize and user text-spacing without loss of content
- Allowing reflow to a single column without horizontal scrolling
- Keeping Small body text legible and not the carrier of critical information

### Critical Success Factors

1. Use relative units so body text scales with user and browser settings
2. Keep ≥4.5:1 contrast for normal text (≥3:1 only where text qualifies as large)
3. Respect user text-spacing overrides without clipping or overlap
4. Don't rely on weight or color alone to convey meaning

---

## Design Requirements

### Structure & Labels

- [ ] **Semantic text**: Use real paragraph/list elements rather than styled generic containers ([Structure guidance](https://a11y-guidelines.orange.com/en/web/develop/page-structure/))
- [ ] **Meaningful emphasis**: Pair Strong/Moderate with `<strong>`/`<em>` when emphasis is semantic
- [ ] **Reading order**: Keep DOM order matching visual reading order

### Visual Design

- [ ] **Contrast**: Meet ≥4.5:1 for normal-size body text ([Contrast guidance](https://a11y-guidelines.orange.com/en/web/design/color-and-contrast/))
- [ ] **Text spacing**: Survive user text-spacing adjustments without loss of content
- [ ] **Resize**: Use relative units so text scales to 200%

### Content

- [ ] **Readable length**: Keep comfortable line lengths for sustained reading
- [ ] **Not weight-only**: ❌ Weight as sole meaning / ✅ Weight plus semantics ([Content guidance](https://a11y-guidelines.orange.com/en/web/design/textual-content/))

---

## Testing Checklist

### Zoom & Reflow Testing

- [ ] Zoom to 200%/400%; confirm no clipping, loss, or horizontal scroll
- [ ] Apply WCAG text-spacing overrides; confirm content remains intact

### Contrast Testing

- [ ] Check Default/Moderate/Strong body text contrast on every background

### Structure Testing

- [ ] Confirm emphasis maps to semantic elements where it carries meaning

Resources: [Orange Accessibility Testing Guide](https://a11y-guidelines.orange.com/en/web/testing/)

---

## Key WCAG Criteria

- **1.4.3 Contrast (Minimum)** (AA): Normal-size body text meets ≥4.5:1 contrast
- **1.4.4 Resize Text** (AA): Body text resizes to 200% without loss of content
- **1.4.12 Text Spacing** (AA): No loss of content when users adjust text spacing
- **1.4.10 Reflow** (AA): Content reflows to a single column without horizontal scrolling
- **1.3.1 Info and Relationships** (A): Emphasis and structure conveyed programmatically

For complete reference: [Orange Accessibility Guidelines](https://a11y-guidelines.orange.com/en/web/)

---

## Additional Resources

- [Orange Accessibility Guidelines - Typography](https://a11y-guidelines.orange.com/en/web/design/typography/)
- [W3C WAI - Text Spacing](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html)
- [WCAG 2.2 Understanding Resize Text](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html)
- [Orange Design System - Accessibility & Sustainability](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability)

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Jun 16, 2026 | 1.0.0 | <ul><li>Component creation</ul> | Maxime Tonnerre<br>Jérôme Regnier |
