**Multiline**
This component allows multi-line text editing. In standalone use, although the number of lines is not technically limited, it is recommended not to exceed one line of text.
In its "Next" variant, if the label spans multiple lines, the chevron icon remains aligned at the bottom.
In its "Text + icon" and "Previous" variants, if the label spans multiple lines, the icon remains vertically centred.

**Max-width vs full-width**
The max-width is applied at the label level and depends on the max-width value assigned to the typographic reference used.
Since the navigation indicator's position always remains close to the last letter of the text label (Layout=Next), it is not possible to use the "Link" component in a full-width context. The component cannot adapt to the parent container (or to the screen in a mobile context, for example) and occupy the full available width.
In a full-width context, you should prioritize using the "Navigation list item" component (for "Next" or "Previous" layout).

**User zoom in/out**
The behavior of the text during user zoom in/out must follow a fundamental principle: the text must remain readable, accessible, and must never break the structure or lose information.
- The text must always scale proportionally with user zoom. Text resizing must never be blocked.
- Zooming must never cause text to be truncated or hidden. The component must expand vertically to allow line wrapping.
- The component's height and width must be flexible, never fixed, in order to automatically adapt its dimensions according to the level of zoom.
- In order to preserve the minimun interactive area during user zoom out, this component have:
  - Default size: a min-width and a min-height **of 48px**
  - Small size: a min-width and a min-height **of 44px**
- Even if, the component has a max-height or a max-width for resizing control purposes, technically, during user zoom in, these limitations are not fixed but must be scalable in order to adapt to the user's zoom level.
- As the chevron icon is functional, it must follow the same rules as text.
- In its "Text + icon" variant, user zoom in/out doesn't affect the size of the icons; they remain fixed in size (decorative use).
