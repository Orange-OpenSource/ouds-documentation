## Definition

Body styles are designed for everyday text content such as paragraphs, descriptions, and informational messages. They prioritize readability and provide a comfortable reading experience across all screen sizes. Multiple size options allow content importance to be expressed while maintaining consistency.
Their typography automatically scales across breakpoints to support responsive layouts.

---

## Size

**`Large`** The most prominent body text size, ideal for introductory paragraphs, highlighted content, or situations where enhanced readability is desired.

**`Medium`** The default body text size, providing an optimal balance between readability, information density, and visual hierarchy across most use cases.

**`Small`** A compact body text size intended for supporting information, secondary content, and dense layouts where space efficiency is important.

---

## Weight

**`Default`** The default weight provides the standard level of typographic emphasis for Body and Label styles. It is designed for optimal readability and neutral hierarchy, making it the baseline for most interface content. Use it whenever no additional emphasis is required.

**`Moderate`** Moderate weight increases visual presence while remaining balanced and readable. It is used to reinforce hierarchy within Body and Label typography without introducing strong emphasis. Suitable for highlighting important information or improving scanability.

**`Strong`** Strong weight provides the highest level of emphasis for Body and Label styles. It is intended for critical information, key actions, or elements that must stand out within dense content. Use it sparingly to preserve its impact and avoid visual overload.

---

## Multiline and responsiveness

**`Multiline`** This component allows multi-line text editing. The number of lines is not limited.

**Max-width vs full-width**
This component has a default max-width.
For the “Body large” variant, the global max-width token will be: size-max-width-body-large
For the “Body medium” variant, the global max-width token will be: size-max-width-body-medium
For the “Body small” variant, the global max-width token will be: size-max-width-body-small

**User zoom in/out**
The behavior of the text during user zoom in/out must follow a fundamental principle: the text must remain readable, accessible, and must never break the structure or lose information.
  • The text must always scale proportionally with user zoom. Text resizing must never be blocked.
  • Zooming must never cause text to be truncated or hidden. The component must expand vertically to allow line wrapping.
  • The component’s height and width must be flexible, never fixed, in order to automatically adapt its dimensions according to the level of zoom.
  • Even if, the component has a max-height or a max-width for resizing control purposes, technically, during user zoom in, these limitations are not fixed but must be scalable in order to adapt to the user’s zoom level.
