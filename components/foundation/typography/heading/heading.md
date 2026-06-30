# Guideline

## Intro 👈🤖

Heading styles structure content and signal hierarchy, giving users a clear, scannable entry point for navigating a page or section.

---

## Definition

Heading styles are used to structure content and define the hierarchy of information within an interface.
Available in multiple sizes, they help users quickly understand the organization of a page or section.
Their size automatically adjusts across breakpoints to ensure optimal readability on all devices.
Headings serve as the primary entry point for visual navigation.

---

## Best for 👈🤔

✅ Page titles and the main subject of a screen

✅ Section and subsection titles that group related content

✅ Card and panel titles within a layout

✅ Establishing a scannable hierarchy in long-form or dense pages

✅ Article and editorial headers above body copy

✅ Form section titles that separate groups of fields

✅ Dialog and sheet titles introducing a focused task

✅ Step or stage titles in a multi-step flow

✅ Anchoring navigation landmarks for assistive technology

✅ Emphasizing a key section with the optional Large-size marker

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Font family | Theme `heading` font-family token defining the typeface | N |
| 2 | Font weight | Weight applied to Heading styles (bold) | N |
| 3 | Font size | Type size per variant — Xlarge / Large / Medium / Small | N |
| 4 | Line height | Vertical rhythm paired to each size for readability | N |
| 5 | Letter spacing | Tracking adjustment tuned per size | N |
| 6 | Marker | Optional brand-colored accent below a Large heading | Y |
| 7 | Responsive scaling | Automatic size adaptation across breakpoints | N |

---

## Size

**`Xlarge`** The highest level of heading hierarchy, used to introduce major sections and establish clear content structure. It serves as the primary navigational anchor within a page or experience.

**`Large`** A high-emphasis heading used for important sections and content groupings. It helps organize information while maintaining strong visual hierarchy.

**`Medium`** A versatile heading size suitable for standard section titles and subsections. It provides a clear hierarchy while preserving content balance.

**`Small`** The most compact heading size, designed for minor sections and localized content organization. Use it where a heading is required within limited space.

---

## size_do_&_dont 👈🤔

✅ **Do:** Choose the heading size to express hierarchy, independently from the semantic heading level.  
❌ **Don't:** Pick a size just to make a lower-level heading look bigger, breaking the outline.

✅ **Do:** Use Xlarge as the single highest-level title that introduces a page or experience.  
❌ **Don't:** Repeat Xlarge across many sections, flattening the perceived hierarchy.

✅ **Do:** Step down through Large, Medium, and Small to nest subsections consistently.  
❌ **Don't:** Skip sizes arbitrarily, creating uneven jumps in visual hierarchy.

✅ **Do:** Let headings scale across breakpoints to keep hierarchy readable on every device.  
❌ **Don't:** Lock heading sizes to fixed pixels that break responsive readability.

✅ **Do:** Keep heading text concise so the hierarchy stays scannable.  
❌ **Don't:** Write sentence-length headings that dilute their structural role.

---

## Marker

When enabled, a brand-colored marker is displayed below the heading to enhance its visual emphasis and reinforce information hierarchy. This optional decorative element helps highlight important sections and improve content scanability. Use it selectively to maintain its impact and avoid visual clutter.

**`False`** The marker is not visible

**`True`** The marker is visible

**Brand theme availability**
This option is technically not available for all brand themes. Here's the list of marker availability by brand theme:

| Brand theme | Availability |
|---|---|
| Orange | ✅ Available |
| Orange Compact | ✅ Available |
| Sosh | ❌ Unavailable |
| Wireframe | ✅ Available |

**Sosh specifications**
The Sosh brand has chosen not to use a marker, instead relying on the "color-content-brand-secondary" color to highlight one or more important words in a heading.
A heading may also use just a single color token: "color-content-default" or "color-content-brand-secondary".

---

## marker_do_&_dont 👈🤔

✅ **Do:** Use the marker selectively to emphasize a key Large-size section heading.  
❌ **Don't:** Apply the marker to many headings at once, eroding its impact.

✅ **Do:** Treat the marker as decorative reinforcement, not a replacement for hierarchy.  
❌ **Don't:** Rely on the marker alone to convey a heading's importance to assistive tech.

✅ **Do:** Respect brand-theme availability — fall back gracefully where the marker is unavailable.  
❌ **Don't:** Force a marker on Sosh; use the brand-secondary color treatment instead.

✅ **Do:** On Sosh, highlight key words with `color-content-brand-secondary` as intended.  
❌ **Don't:** Recreate a marker visual on themes that deliberately omit it.

✅ **Do:** Keep enough surrounding space so the marker reads as an accent, not clutter.  
❌ **Don't:** Combine the marker with other heavy emphasis that competes for attention.

---

# Specs

## States

🚧 Not applicable — Heading is a non-interactive typography style and has no interactive states.

---

## Layout and spacing

🚧 Content to be added

---

# Accessibility 👈🤖

## Accessibility intro

Heading styles must meet WCAG 2.2 Level AA and, crucially, map to a correct semantic heading structure so everyone — including screen-reader users — can navigate by headings. For comprehensive guidance, see the [Orange Unified Design System Accessibility Overview](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability).

---

## Accessibility Challenges

Headings carry meaning beyond their appearance: assistive technology builds a navigable outline from heading levels, so visual size must not be confused with semantic level. The marker and color treatments must also remain perceivable without relying on color alone.

### Key Challenges

- Keeping semantic heading level independent from the chosen visual size
- Preserving a logical, non-skipping heading outline for screen-reader navigation
- Ensuring the marker and Sosh color emphasis don't rely on color alone
- Maintaining contrast and readability when headings scale across breakpoints

### Critical Success Factors

1. Map each heading to the correct `<h1>`–`<h6>` level for its place in the outline
2. Don't skip heading levels to achieve a particular visual size
3. Keep text contrast ≥4.5:1 (≥3:1 for large text) including marker/secondary colors
4. Allow headings to resize and reflow without loss of content

---

## Design Requirements

### Structure & Labels

- [ ] **Semantic level**: Use a real `<h1>`–`<h6>` element matching the outline ([Heading guidance](https://a11y-guidelines.orange.com/en/web/develop/page-structure/))
- [ ] **No level skipping**: Don't jump from `<h2>` to `<h4>` to obtain a size
- [ ] **One page title**: Reserve a single top-level heading per page

### Visual Design

- [ ] **Contrast**: Meet ≥4.5:1 (≥3:1 for large text) for heading and marker colors ([Contrast guidance](https://a11y-guidelines.orange.com/en/web/design/color-and-contrast/))
- [ ] **Not color-only**: Don't convey importance through the marker/secondary color alone
- [ ] **Resize**: Use relative units so headings scale to 200% without clipping

### Content

- [ ] **Descriptive**: ❌ "More" / ✅ "Mobile plans without commitment" ([Content guidance](https://a11y-guidelines.orange.com/en/web/design/textual-content/))
- [ ] **Concise**: Keep headings short so the outline stays scannable

---

## Testing Checklist

### Screen Reader Testing

- [ ] Navigate by headings (NVDA/JAWS/VoiceOver/TalkBack); confirm a logical, non-skipping outline
- [ ] Verify each heading level matches its place in the content hierarchy

### Zoom & Reflow Testing

- [ ] Zoom to 200%/400%; confirm no clipping, loss, or horizontal scroll

### Contrast Testing

- [ ] Check heading, marker, and Sosh secondary-color contrast on every background

Resources: [Orange Accessibility Testing Guide](https://a11y-guidelines.orange.com/en/web/testing/)

---

## Key WCAG Criteria

- **1.3.1 Info and Relationships** (A): Heading roles and levels exposed programmatically, not by size
- **2.4.6 Headings and Labels** (AA): Headings describe topic or purpose
- **1.4.3 Contrast (Minimum)** (AA): Heading and marker colors meet minimum contrast
- **1.4.4 Resize Text** (AA): Headings resize to 200% without loss of content
- **1.4.10 Reflow** (AA): Headings reflow to a single column without horizontal scrolling

For complete reference: [Orange Accessibility Guidelines](https://a11y-guidelines.orange.com/en/web/)

---

## Additional Resources

- [Orange Accessibility Guidelines - Typography](https://a11y-guidelines.orange.com/en/web/design/typography/)
- [W3C WAI - Headings](https://www.w3.org/WAI/tutorials/page-structure/headings/)
- [WCAG 2.2 Understanding Headings and Labels](https://www.w3.org/WAI/WCAG22/Understanding/headings-and-labels.html)
- [Orange Design System - Accessibility & Sustainability](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability)

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Jun 16, 2026 | 1.0.0 | <ul><li>Component creation</ul> | Maxime Tonnerre<br>Jérôme Regnier |
