## Definition

An Expand filter chip is a compact UI component that combines the functionality of a filter chip with a dropdown menu. It allows users to apply a filter from a predefined list of options without leaving the current context. When activated, it reveals a dropdown containing selectable values, and the chip updates to reflect the selected filter. This component is useful for filters with multiple or dynamic options, offering both clarity and space efficiency in the interface.

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

**`Focus`** The state when the chip receives focus (e.g., during keyboard navigation).
It features a triple contrasting border to indicate the active element.

**`Skeleton`** Displays a placeholder chip while the content is loading.
It appears as a semi-transparent gray block without content.

---
