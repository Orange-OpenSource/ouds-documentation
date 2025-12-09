## Definition

A filter chip is a compact UI element used in a design system to represent a filter option that can be selected or deselected by the user. Filter chips allow users to refine content or data by applying one or more filters in a visually accessible and interactive way.

Purpose: Allows users to filter content by selecting or deselecting specific categories or attributes.
Behavior: Can be toggled on/off to refine displayed results. Selected chips remain visually distinct to indicate active filters.

---

## Selected

**`True`** Visually distinct to indicate an active filter.
Changes in color and includes a tick mark to signify selection.

**`False`** Maintains a neutral appearance, indicating an available filter option.

---

## Layouts

**`Text + icon`** Combines text with an icon to enhance clarity and recognition.
Ideal when a visual cue helps reinforce the filter's meaning.

**`Text only`** Displays only text, offering a clean and minimalistic look.
Best suited for category-based filters that do not require additional visual elements.

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

**`Focus`** The state when the chip receives focus (e.g., during keyboard navigation).
It features a triple contrasting border to indicate the active element.

**`Skeleton`** Displays a placeholder chip while the content is loading.
It appears as a semi-transparent gray block without content.

---