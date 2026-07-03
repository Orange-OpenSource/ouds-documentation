## Definition

A filter chip is a UI element that enables users to select or deselect options within a series, commonly used to capture filtering decisions. The filter chip allows users to refine content by selecting or deselecting options. It can be toggled 'On' or 'Off' to adjust the displayed results, and selected filter chips remain visually distinct to show which filters are active.

---

## Selected

**`True`** Visually distinct to indicate an active filter.
Changes in color and includes a tick mark to signify selection.

**`False`** Maintains a neutral appearance, indicating an available filter option.

---

## Layouts

**`Text only`** Displays only text, offering a clean and minimalistic look.
Best suited for category-based filters that do not require additional visual elements.

**`Text + icon`** Combines text with an icon to enhance clarity and recognition.
Ideal when a visual cue helps reinforce the filter's meaning.

**`Icon only`** Uses only an icon, making it a compact option for limited space.
Works well with universally recognized symbols, such as a heart for favorites or a checkmark for selection.

---

## States

**`Enabled`** The chip is active and available for interaction.
It is displayed in its standard style without additional effects.

**`Hover`** The appearance of the chip changes when the cursor hovers over it.
This includes a color change for the border and the chip's content.

**`Pressed`** The active state when the chip is being pressed.
Accompanied by a color change in the content and border.

**`Disabled`** The chip is unavailable for interaction.
It is visually represented with a muted color change in the content and border (reduced brightness and contrast).

**`Focus`** The state when the chip receives focus (during keyboard navigation).
It features a triple contrasting border to indicate the active element.

**`Skeleton`** Displays a placeholder chip while the content is loading.
It appears as a semi-transparent gray block without content.

---

## Multiline and responsiveness

**Multiline**
This component doesn't allows multi-line text editing. This is a design recommendation, technically, and for several reasons (responsive behavior, user zoom, etc.), multiline remains possible.

**Max-width vs full-width**
For greater flexibility, this component doesn't have a default max-width. To avoid exceeding a width that would degrade readability and the perception of a compact interactive element, we recommend applying **a max-width of around 240px.**
It is not possible to set this component to use the full available width (of the screen or the container).

**User zoom in/out**
The behavior of the text during user zoom in/out must follow a fundamental principle: the text must remain readable, accessible, and must never break the structure or lose information.
* The text must always scale proportionally with user zoom. Text resizing must never be blocked.
* Zooming must never cause text to be truncated or hidden. The component must expand vertically to allow line wrapping.
* The component's height and width must be flexible, never fixed, in order to automatically adapt its dimensions according to the level of zoom.
* In order to preserve the minimun interactive area during user zoom out, this component have a min-width **of 52px** and a min-height **of 48px**.
* Even if, the component has a max-height or a max-width for resizing control purposes, technically, during user zoom in, these limitations are not fixed but must be scalable in order to adapt to the user's zoom level.
* As the tick icon is functional, it must follow the same rules as text.
* In its "Text + icon" variant, user zoom in/out doesn't affect the size of the icons; they remain fixed in size (decorative use).
* As the text is missing, in its "Icon only" variant, the icons follow the same rules as the text.
