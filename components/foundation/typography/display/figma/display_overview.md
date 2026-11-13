## Definition

Display styles are intended for high-impact content such as landing pages, marketing campaigns, and key messages. Their large type sizes help capture attention and establish strong visual emphasis.
Variants automatically adapt across breakpoints to maintain a consistent visual hierarchy on every screen size.
Use them sparingly to preserve their impact and effectiveness.

---

## Size

**`Large`** The largest Display size, intended for maximum visual impact. Use it for hero sections, key messages, and high-priority content that requires immediate attention.

**`Medium`** A prominent Display size that provides strong emphasis while maintaining a more balanced visual presence. Suitable for major content areas and featured messages.

**`Small`** The most compact Display size, offering visual impact in space-constrained layouts. Use it when a display style is needed without overwhelming surrounding content.

---

## Multiline and responsiveness

**`Multiline`** This component allows multi-line text editing. The number of lines is not limited.

**Max-width vs full-width**
This component has a default max-width.
For the “Display large” variant, the global max-width token will be: size-max-width-display-large
For the “Display medium” variant, the global max-width token will be: size-max-width-display-medium
For the “Display small” variant, the global max-width token will be: size-max-width-display-small

**User zoom in/out**
The behavior of the text during user zoom in/out must follow a fundamental principle: the text must remain readable, accessible, and must never break the structure or lose information.
  • The text must always scale proportionally with user zoom. Text resizing must never be blocked.
  • Zooming must never cause text to be truncated or hidden. The component must expand vertically to allow line wrapping.
  • The component’s height and width must be flexible, never fixed, in order to automatically adapt its dimensions according to the level of zoom.
  • Even if, the component has a max-height or a max-width for resizing control purposes, technically, during user zoom in, these limitations are not fixed but must be scalable in order to adapt to the user’s zoom level.
