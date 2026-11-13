## Definition

Heading styles are used to structure content and define the hierarchy of information within an interface.
Available in multiple sizes, they help users quickly understand the organization of a page or section.
Their size automatically adjusts across breakpoints to ensure optimal readability on all devices.
Headings serve as the primary entry point for visual navigation.

---

## Size

**`Xlarge`** The highest level of heading hierarchy, used to introduce major sections and establish clear content structure. It serves as the primary navigational anchor within a page or experience.

**`Large`** A high-emphasis heading used for important sections and content groupings. It helps organize information while maintaining strong visual hierarchy.

**`Medium`** A versatile heading size suitable for standard section titles and subsections. It provides a clear hierarchy while preserving content balance.

**`Small`** The most compact heading size, designed for minor sections and localized content organization. Use it where a heading is required within limited space.

---

## Marker

When enabled, a brand-colored marker is displayed below the heading large to enhance its visual emphasis and reinforce information hierarchy. This optional decorative element helps highlight important sections and improve content scanability. Use it selectively to maintain its impact and avoid visual clutter.

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

## Multiline and responsiveness

**`Multiline`** This component allows multi-line text editing. The number of lines is not limited.

**Max-width vs full-width**
This component has a default max-width.
For the “Heading xlarge” variant, the global max-width token will be: size-max-width-heading-xlarge
For the “Heading large” variant, the global max-width token will be: size-max-width-heading-large
For the “Heading medium” variant, the global max-width token will be: size-max-width-heading-medium
For the “Heading small” variant, the global max-width token will be: size-max-width-heading-small

**User zoom in/out**
The behavior of the text during user zoom in/out must follow a fundamental principle: the text must remain readable, accessible, and must never break the structure or lose information.
  • The text must always scale proportionally with user zoom. Text resizing must never be blocked.
  • Zooming must never cause text to be truncated or hidden. The component must expand vertically to allow line wrapping.
  • The component’s height and width must be flexible, never fixed, in order to automatically adapt its dimensions according to the level of zoom.
  • Even if, the component has a max-height or a max-width for resizing control purposes, technically, during user zoom in, these limitations are not fixed but must be scalable in order to adapt to the user’s zoom level.
  • As the marker isn’t functional, user zoom in/out doesn’t affect the size of the element; they remain fixed in size (decorative use).
