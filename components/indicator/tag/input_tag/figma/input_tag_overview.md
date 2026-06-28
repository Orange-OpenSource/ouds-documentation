## Definition

An input tag is a UI element that renders an entered value as a tag, allowing it to display brief information like a label, keyword, or category. The input tag allows users to type and submit values (typically by pressing enter, comma, or tab), transforming each value into a tag.

---

## States

**`Enabled`** The default state of the Input tag. The tag is fully interactive, allowing users to read the label and remove the tag if needed.

**`Hover`** Displayed when a user hovers the cursor over the tag. Visual cues (such as a highlighted border) indicate that the tag is interactive and can be removed.

**`Pressed`** Shown when the tag is actively being clicked or tapped. The tag appears pressed or highlighted, providing feedback that the action is being performed.

**`Disabled`** Indicates that the tag is non-interactive. The tag appears faded or greyed out, and users cannot interact with it or remove it.

**`Focus`** Appears when the tag is focused, typically via keyboard navigation or screen reader. A distinct outline or highlight indicates that the tag is in focus, supporting accessibility.

**`Skeleton`** A placeholder state displayed while content is loading. The tag appears as a simplified, greyed-out shape without label text, indicating to users that tags will soon be available.

---

## Multiline and responsiveness

**Multiline**
This component doesn't allows multi-line text editing. This is a design recommendation, technically, and for several reasons (responsive behavior, user zoom, etc.), multiline remains possible.

**Max-width vs full-width**
For greater flexibility, this component doesn't have a default max-width. To avoid exceeding a width that would degrade readability and the perception of a compact interactive element, we recommend applying **a max-width of around 240px.**
It is not possible to set this component to use the full available width (of the screen or the container).

**User zoom in/out**
The behavior of the text during user zoom in/out must follow a fundamental principle: the text must remain readable, accessible, and must never break the structure or lose information.
- The text must always scale proportionally with user zoom. Text resizing must never be blocked.
- Zooming must never cause text to be truncated or hidden. The component must expand vertically to allow line wrapping.
- The component's height and width must be flexible, never fixed, in order to automatically adapt its dimensions according to the level of zoom.
- In order to preserve the minimun interactive area during user zoom out, this component have a min-width and a min-height.
- Even if, the component has a max-height or a max-width for resizing control purposes, technically, during user zoom in, these limitations are not fixed but must be scalable in order to adapt to the user's zoom level.
- As the close icon is functional, it must follow the same rules as text.
