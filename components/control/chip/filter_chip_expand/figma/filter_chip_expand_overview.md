## Definition

A filter chip expand is a UI element that allows users to control the selection or deselection of a choice from a defined list of options, frequently used to capture filtering decisions. The filter chip expand feature is displayed through a dropdown with selectable values, making it ideal for filters with multiple or dynamic options while providing clarity and saving space in the interface.

---

## Selection Status

**`Selected`** Visually differentiated to show an active filter. The chip changes color and displays a tick and counter to indicate it has been selected.

**`Unselected`** Maintains a neutral appearance, indicating an available filter option.

---

## Expanded

The "Expanded" state allows the filter chip to be dynamically edited via a dropdown component.

**`True`** When a Filter chip is in the "Expanded" state, it:
 - Displays a contextual dropdown containing a menu or controls to modify the associated filter values.
 - Remains visually attached to the source chip (often below or overlapping).
 - Allows the user to select multiple options or apply a new value.
The component can remain in the "Expanded" state until a user action (click or key press) closes it. Chevron icon points up.

**`False`** The "Collapsed" state is the default or "resting" state of the filter chip, in which it simply displays a filter value, without any visible complex interaction. Chevron icon points down.

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
For greater flexibility, this component doesn't have a default max-width. To avoid exceeding a width that would degrade readability and the perception of a compact interactive element, we recommend applying **a max-width of around 200px.**
It is not possible to set this component to use the full available width (of the screen or the container).

**User zoom in/out**
The behavior of the text during user zoom in/out must follow a fundamental principle: the text must remain readable, accessible, and must never break the structure or lose information.
* The text must always scale proportionally with user zoom. Text resizing must never be blocked.
* Zooming must never cause text to be truncated or hidden. The component must expand vertically to allow line wrapping.
* The component's height and width must be flexible, never fixed, in order to automatically adapt its dimensions according to the level of zoom.
* In order to preserve the minimun interactive area during user zoom out, this component have a min-width **of 52px** and a min-height **of 48px**.
* Even if, the component has a max-height or a max-width for resizing control purposes, technically, during user zoom in, these limitations are not fixed but must be scalable in order to adapt to the user's zoom level.
* As the tick and the chevron icon are functional, they must follow the same rules as text.
* [Learn more about the behavior of the badge count component.](https://www.figma.com/design/QtOWrH1m3RHOAkfyy0XFil?node-id=92884-9275)
