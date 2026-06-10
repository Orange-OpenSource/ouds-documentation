**Multiline**
This component allows multi-line text editing. The number of lines is not limited.

**Max-width**
The max-width must be applied at the bullet list container level, not on individual list items. This ensures consistent alignment, readable line lengths, and a coherent vertical structure.
List items must naturally wrap within the parent container
The max-width value depends on the maximum width value assigned to the typographic reference used.
Since the component is standalone, it is up to the designer to manually add a max-width to the group of multiple bullet lists.
For the "body large" variant, the global max-width token will be: **size-max-width-body-large**
For the "body medium" variant, the global max-width token will be: **size-max-width-body-medium**

**User zoom in/out**
The behavior of the text during user zoom in/out must follow a fundamental principle: the text must remain readable, accessible, and must never break the structure or lose information.
* The text must always scale proportionally with user zoom. Text resizing must never be blocked.
* Zooming must never cause text to be truncated or hidden. The component must expand vertically to allow line wrapping.
* The component's height and width must be flexible, never fixed, in order to automatically adapt its dimensions according to the level of zoom.
* Even if, the component has a max-height or a max-width for resizing control purposes, technically, during user zoom in, these limitations are not fixed but must be scalable in order to adapt to the user's zoom level.
* In order to preserve the same display rendering, numbers, uppercase/lowercase letters, and bullet points follow the same rules as the text.
