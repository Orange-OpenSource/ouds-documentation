## Definition

The Code style is dedicated to technical content such as code snippets, commands, system values, and identifiers. It uses a monospace typeface to preserve character alignment and improve readability of structured content. Available in a single size, it provides a consistent presentation of technical information throughout the product. Its use should be limited to content that requires an accurate code-like representation.

---

## Multiline and responsiveness

**`Multiline`** This component allows multi-line text editing. The number of lines is not limited.

**Max-width vs full-width**
This component has no maximum width by default.

**User zoom in/out**
The behavior of the text during user zoom in/out must follow a fundamental principle: the text must remain readable, accessible, and must never break the structure or lose information.
  • The text must always scale proportionally with user zoom. Text resizing must never be blocked.
  • Zooming must never cause text to be truncated or hidden. The component must expand vertically to allow line wrapping.
  • The component’s height and width must be flexible, never fixed, in order to automatically adapt its dimensions according to the level of zoom.
  • Even if, the component has a max-height or a max-width for resizing control purposes, technically, during user zoom in, these limitations are not fixed but must be scalable in order to adapt to the user’s zoom level.
