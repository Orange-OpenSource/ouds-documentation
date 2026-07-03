# Guideline

## Intro 👈🤖

Label is the compact, fixed-size text style for component content — buttons, fields, badges — kept consistent and predictable across every breakpoint.

---

## Definition

Label styles are intended for compact interface elements such as buttons, form fields, badges, and other small components. Unlike other typography categories, they are not responsive and maintain a fixed size across all breakpoints. This ensures visual consistency and predictable behavior within space-constrained UI elements. Labels should be preferred whenever content is displayed within small components.

---

## Best for 👈🤔

✅ Button and call-to-action text

✅ Form field labels, placeholders, and helper microcopy

✅ Badge, tag, and chip text

✅ Tabs, menu items, and navigation labels

✅ Table headers and compact data cells

✅ Tooltips and small contextual hints

✅ Status and metadata text inside components

✅ Any text rendered within a space-constrained UI component

✅ Contexts needing a fixed size that won't reflow with breakpoints

✅ Emphasizing a component label with the Moderate or Strong weight

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Font family | Theme `label` font-family token defining the typeface | N |
| 2 | Font size | Fixed type size per variant — Xlarge 18px, Large 16px, Medium 14px, Small 12px | N |
| 3 | Line height | Compact vertical rhythm suited to component layouts | N |
| 4 | Letter spacing | Tracking tuned for short, dense labels | N |
| 5 | Font weight | Emphasis axis — Default, Moderate, Strong | N |
| 6 | Fixed sizing | Non-responsive — size stays constant across breakpoints | N |

---

## Size

**`Xlarge`** The largest label size, intended for prominent UI controls and interface elements that require increased visibility and emphasis.

**`Large`** A highly readable label size suitable for key interactive components and larger interface patterns. It provides strong clarity while maintaining compactness.

**`Medium`** The default label size, designed for most interface components and controls. It offers a balanced combination of readability and space efficiency.

**`Small`** The most compact label size, optimized for dense interfaces and small UI components. Use it when space is limited while preserving legibility.

---

## size_do_&_dont 👈🤔

✅ **Do:** Use Medium as the default label size for most components and controls.  
❌ **Don't:** Default to Xlarge or Small without a clear emphasis or density reason.

✅ **Do:** Use Xlarge or Large for prominent controls that need extra visibility.  
❌ **Don't:** Scale labels up so far that they read like body or heading text.

✅ **Do:** Reserve Small for dense interfaces while preserving legibility.  
❌ **Don't:** Shrink labels below a legible size just to fit more in.

✅ **Do:** Rely on the fixed sizing to keep component text predictable across breakpoints.  
❌ **Don't:** Expect labels to scale responsively like Heading or Body styles.

✅ **Do:** Keep label sizes consistent for the same component type across the product.  
❌ **Don't:** Mix label sizes arbitrarily within a single component.

---

## Weight

**`Default`** The default weight provides the standard level of typographic emphasis for Body and Label styles. It is designed for optimal readability and neutral hierarchy, making it the baseline for most interface content. Use it whenever no additional emphasis is required.

**`Moderate`** Moderate weight increases visual presence while remaining balanced and readable. It is used to reinforce hierarchy within Body and Label typography without introducing strong emphasis. Suitable for highlighting important information or improving scanability.

**`Strong`** Strong weight provides the highest level of emphasis for Body and Label styles. It is intended for critical information, key actions, or elements that must stand out within dense content. Use it sparingly to preserve its impact and avoid visual overload.

---

## weight_do_&_dont 👈🤔

✅ **Do:** Use Default weight for most component labels.  
❌ **Don't:** Set every label in Strong, removing emphasis contrast across the UI.

✅ **Do:** Use Moderate to reinforce a label's importance without shouting.  
❌ **Don't:** Use Strong where Moderate already provides enough emphasis.

✅ **Do:** Reserve Strong for primary actions or labels that must stand out.  
❌ **Don't:** Overuse Strong across many controls, causing visual overload.

✅ **Do:** Match weight to the component's role and importance.  
❌ **Don't:** Use weight as the sole means of conveying state or meaning.

✅ **Do:** Keep weight consistent for equivalent controls across the product.  
❌ **Don't:** Vary weight arbitrarily between identical component types.

---

# Specs

## States

🚧 Not applicable — Label is a non-interactive typography style and has no interactive states.

---

## Layout and spacing

🚧 Content to be added

---

# Accessibility 👈🤖

## Accessibility intro

Label styles must meet WCAG 2.2 Level AA. Because labels are fixed-size and live inside components, contrast, accessible naming, and resilience to user text-spacing matter most. For comprehensive guidance, see the [Orange Unified Design System Accessibility Overview](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability).

---

## Accessibility Challenges

Labels are small and fixed, so legibility and contrast are critical, especially at the Small size. As component text, a label often provides the accessible name for a control, and it must remain intact when users increase text spacing or zoom.

### Key Challenges

- Maintaining ≥4.5:1 contrast at small, fixed label sizes
- Ensuring labels provide or reinforce a control's accessible name
- Surviving user zoom and text-spacing without clipping inside components
- Not conveying meaning through weight or color alone

### Critical Success Factors

1. Keep ≥4.5:1 contrast for label text (≥3:1 only where it qualifies as large)
2. Associate labels with their control so they form the accessible name
3. Allow component layouts to grow so zoomed/spaced labels aren't clipped
4. Pair emphasis with semantics, not weight or color alone

---

## Design Requirements

### Structure & Labels

- [ ] **Programmatic association**: Tie field labels to inputs via `<label for>`/`aria-labelledby` ([Forms guidance](https://a11y-guidelines.orange.com/en/web/develop/forms/))
- [ ] **Accessible name**: Ensure button/chip labels expose a clear accessible name
- [ ] **No truncation of meaning**: Don't hide essential label text behind ellipsis only

### Visual Design

- [ ] **Contrast**: Meet ≥4.5:1 for label text, including at the Small size ([Contrast guidance](https://a11y-guidelines.orange.com/en/web/design/color-and-contrast/))
- [ ] **No clipping**: Let containers grow when text is zoomed or spaced
- [ ] **Not color/weight-only**: Don't signal state through color or weight alone

### Content

- [ ] **Concise & clear**: ❌ "OK" for everything / ✅ specific action labels ([Content guidance](https://a11y-guidelines.orange.com/en/web/design/textual-content/))
- [ ] **Consistent terms**: Use consistent labels for the same action across the product

---

## Testing Checklist

### Zoom & Spacing Testing

- [ ] Zoom to 200% and apply text-spacing overrides; confirm labels aren't clipped in their components

### Contrast Testing

- [ ] Check Default/Moderate/Strong label contrast at every size, especially Small

### Screen Reader Testing

- [ ] Confirm labels provide or reinforce the accessible name of their control

Resources: [Orange Accessibility Testing Guide](https://a11y-guidelines.orange.com/en/web/testing/)

---

## Key WCAG Criteria

- **1.4.3 Contrast (Minimum)** (AA): Label text meets ≥4.5:1 contrast at its size
- **2.4.6 Headings and Labels** (AA): Labels describe topic or purpose
- **1.3.1 Info and Relationships** (A): Label–control associations conveyed programmatically
- **1.4.4 Resize Text** (AA): Labels remain usable when text is resized to 200%
- **1.4.12 Text Spacing** (AA): No loss of content when users adjust text spacing

For complete reference: [Orange Accessibility Guidelines](https://a11y-guidelines.orange.com/en/web/)

---

## Additional Resources

- [Orange Accessibility Guidelines - Forms](https://a11y-guidelines.orange.com/en/web/develop/forms/)
- [W3C WAI - Labels](https://www.w3.org/WAI/tutorials/forms/labels/)
- [WCAG 2.2 Understanding Headings and Labels](https://www.w3.org/WAI/WCAG22/Understanding/headings-and-labels.html)
- [Orange Design System - Accessibility & Sustainability](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability)

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Jun 16, 2026 | 1.0.0 | <ul><li>Component creation</ul> | Maxime Tonnerre<br>Jérôme Regnier |
