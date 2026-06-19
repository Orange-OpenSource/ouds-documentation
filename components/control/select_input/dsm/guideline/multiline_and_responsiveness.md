**Multiline**

In its "Empty" state, the label of this component allows two lines of text editing. However, it is recommended not to exceed one line of text.

Apart from the case described above, this component doesn't allow multi-line text editing (whether for the label or input).

As a result, and in order to maintain a consistent and uniform height across multiple components, the presence of an excessive amount of text (in the label or input) will cause the text to be truncated so that only a single line remains visible for each element.

Additionally, allowing multi-line text editing would create confusion with the "Text area" component.

**Max-width vs full-width**

For greater flexibility, this component doesn't have a default max-width. To avoid exceeding a width that would degrade readability and the perception of a compact interactive element, we recommend applying **a max-width of around 480px.**

For mobile or tablet use (or if the component is positioned inside a specific container), it is possible to set this component to use the full available width (of the screen or the container).

Please note that this behavior is not the default rule; it may be preferred if the template allows it (to improve user comfort or for better page structure/hierarchy).

**User zoom in/out**

The behavior of the text during user zoom in/out must follow a fundamental principle: the text must remain readable, accessible, and must never break the structure or lose information.

However, "Text input" components present an exception regarding the loss of textual information following the activation of user zoom, since text truncation (label, placeholder, input text) is exceptionally allowed and enabled.

* The text must always scale proportionally with user zoom. Text resizing must never be blocked.
* The component's height and width must be flexible, never fixed, in order to automatically adapt its dimensions according to the level of zoom.
* In order to preserve the minimun interactive area during user zoom out, this component have a min-width **of 96px** and a min-height **of 60px**.
* Even if, the component has a max-height or a max-width for resizing control purposes, technically, during user zoom in, these limitations are not fixed but must be scalable in order to adapt to the user's zoom level.
* In its "Leading icon" variant, user zoom in/out doesn't affect the size of the icons; they remain fixed in size (decorative use).
* As the chevron and error icon are functional, they must follow the same rules as text.
