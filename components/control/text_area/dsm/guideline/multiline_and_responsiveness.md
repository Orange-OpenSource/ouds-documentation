• **Multiline**
This component allows multi-line text editing. Further details are available in the "Behavior by entered line count" section.

• **Max-width vs full-width**
For greater flexibility, this component doesn't have a default max-width. To avoid exceeding a width that would degrade readability and the perception of a compact interactive element, we recommend applying **a max-width of around 640px.**
For mobile or tablet use (or if the component is positioned inside a specific container), it is possible to set this component to use the full available width (of the screen or the container). Please note that this behavior is not the default rule; it may be preferred if the template allows it (to improve user comfort or for better page structure/hierarchy).

• **User zoom in/out**
The behavior of the text during user zoom in/out must follow a fundamental principle: the text must remain readable, accessible, and must never break the structure or lose information. However, "Text input" components present an exception regarding the loss of textual information following the activation of user zoom in, since text truncation (label, placeholder, input text) is exceptionally allowed and enabled.

  - The text must always scale proportionally with user zoom. Text resizing must never be blocked.
  - Zooming must never cause text to be truncated or hidden. The component must expand vertically to allow line wrapping.
  - The component's height and width must be flexible, never fixed, in order to automatically adapt its dimensions according to the level of zoom.
  - In order to preserve the minimum interactive area during user zoom out, this component has a min-width **of 240px** and a min-height **of 92px**.
  - Even if the component has a max-height or a max-width for resizing control purposes, technically, during user zoom in, these limitations are not fixed but must be scalable in order to adapt to the user's zoom level.
  - In its "Leading icon" variant, user zoom in/out doesn't affect the size of the icons; they remain fixed in size (decorative use).
  - As the error icon is functional, it must follow the same rules as text.
  - The behaviors of the button (layout: icon only) component during user zoom are available in the corresponding documentation.
