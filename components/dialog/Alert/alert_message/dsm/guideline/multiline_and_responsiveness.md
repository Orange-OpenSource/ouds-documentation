**Multiline**
This component allows multi-line text editing. The number of lines is not limited.

**Max-width vs full-width**
For greater flexibility, this component doesn't have a default max-width. The max-width is applied to the text within the component.
As a result, if it is positioned across the full available width (of the screen or the container), the component's background will stretch across the entire available surface, but the text may be limited to its max-width if the display width is larger.

**User zoom in/out**
The behavior of the text during user zoom in/out must follow a fundamental principle: the text must remain readable, accessible, and must never break the structure or lose information.
* The text must always scale proportionally with user zoom. Text resizing must never be blocked.
* Zooming must never cause text to be truncated or hidden. The component must expand vertically to allow line wrapping.
* The component's height and width must be flexible, never fixed, in order to automatically adapt its dimensions according to the level of zoom.
* In order to preserve the minimun interactive area during user zoom out, this component have a min-width **of 160px** and a min-height **of 100px**.
* If the component doesn't contain any interactive elements, it's not necessary to maintain the minimum interactive area during user zooms out.
* Even if, the component has a max-height or a max-width for resizing control purposes, technically, during user zoom in, these limitations are not fixed but must be scalable in order to adapt to the user's zoom level.
* Icons must always scale proportionally with user zoom. Icon resizing must never be blocked.
* The behaviors of the other subcomponents during user zoom are available in the corresponding documentation.
