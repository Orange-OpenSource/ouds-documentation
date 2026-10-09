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

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Jun 16, 2026 | 1.0.0 | <ul><li>Component creation</ul> | Maxime Tonnerre<br>Jérôme Regnier |
