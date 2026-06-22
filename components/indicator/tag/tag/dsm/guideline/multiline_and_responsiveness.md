**Multiline**
This component doesn't allows multi-line text editing. This is a design recommendation, technically, and for several reasons (responsive behavior, user zoom, etc.), multiline remains possible.

**Max-width vs full-width**
For greater flexibility, this component doesn't have a default max-width. To avoid exceeding a width that would degrade readability and the perception of a compact interactive element, we recommend applying **a max-width of around 200px.**
- In its "Rounded corner=True", it's not possible to set this component to use the full available width (of the screen or the container).
- In its "Rounded corner=False", it's possible to set this component to use the full available width (of the screen or the container). As a result, the component's background will stretch across the entire available surface, but the text must be limited to its number of characters.

**User zoom in/out**
The behavior of the text during user zoom in/out must follow a fundamental principle: the text must remain readable, accessible, and must never break the structure or lose information.
- The text must always scale proportionally with user zoom. Text resizing must never be blocked.
- Zooming must never cause text to be truncated or hidden. The component must expand vertically to allow line wrapping.
- The component's height and width must be flexible, never fixed, in order to automatically adapt its dimensions according to the level of zoom.
- In order to preserve the minimun visible area during user zoom out, this component have:
  - Default size: a min-width **of 48px** and a min-height **of 32px**
  - Small size: a min-width **of 44px** and a min-height **of 24px**
- Even if, the component has a max-height or a max-width for resizing control purposes, technically, during user zoom in, these limitations are not fixed but must be scalable in order to adapt to the user's zoom level.
- Icons, bullets or loader must always scale proportionally with user zoom. Icon resizing must never be blocked.
