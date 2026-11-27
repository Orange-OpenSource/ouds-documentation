## Definition

Label styles are intended for compact interface elements such as buttons, form fields, badges, and other small components. Unlike other typography categories, they are not responsive and maintain a fixed size across all breakpoints. This ensures visual consistency and predictable behavior within space-constrained UI elements. Labels should be preferred whenever content is displayed within small components.

---

## Size

**`Xlarge`** The largest label size, intended for prominent UI controls and interface elements that require increased visibility and emphasis.

**`Large`** A highly readable label size suitable for key interactive components and larger interface patterns. It provides strong clarity while maintaining compactness.

**`Medium`** The default label size, designed for most interface components and controls. It offers a balanced combination of readability and space efficiency.

**`Small`** The most compact label size, optimized for dense interfaces and small UI components. Use it when space is limited while preserving legibility.

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
For the “Label xlarge” variant, the global max-width token will be: size-max-width-label-xlarge
• For the “Label large” variant, the global max-width token will be: size-max-width-label-large
For the “Label medium” variant, the global max-width token will be: size-max-width-label-medium
For the “Label small” variant, the global max-width token will be: size-max-width-label-small

**User zoom in/out**
The behavior of the text during user zoom in/out must follow a fundamental principle: the text must remain readable, accessible, and must never break the structure or lose information.
  • The text must always scale proportionally with user zoom. Text resizing must never be blocked.
  • Zooming must never cause text to be truncated or hidden. The component must expand vertically to allow line wrapping.
  • The component’s height and width must be flexible, never fixed, in order to automatically adapt its dimensions according to the level of zoom.
  • Even if, the component has a max-height or a max-width for resizing control purposes, technically, during user zoom in, these limitations are not fixed but must be scalable in order to adapt to the user’s zoom level.
