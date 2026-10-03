**Multiline**
This component doesn't allows multi-line text editing.

**Max-width**
For greater flexibility, this component doesn't have a max-width.

**User zoom in/out**
The behavior of the text during user zoom in/out must follow a fundamental principle: the text must remain readable, accessible, and must never break the structure or lose information.
- The text must always scale proportionally with user zoom. Text resizing must never be blocked.
- Except for the name of page n-1, which is never truncated, and for this specific component, zooming may cause text to be truncated or hidden. The component must expand vertically to allow line wrapping.
- The component's height and width must be flexible, never fixed, in order to automatically adapt its dimensions according to the level of zoom.
- In order to preserve the minimun interactive area during user zoom out or during page name truncation, each link have a min-width and a min-height of 44px.
- Even if, the component has a max-height or a max-width for resizing control purposes, technically, during user zoom in, these limitations are not fixed but must be scalable in order to adapt to the user's zoom level.
- Even with user zoom in/out, this component does not allow multi-line text editing. As a result, the component may end up with horizontal scrolling if the total width of the non-truncatable labels exceeds the width of the container or the page.
- As the chevron icon is functional, it must follow the same rules as text.