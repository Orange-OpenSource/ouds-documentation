## Future update! The version 1.5.0 is currently being designed; it will be released in an upcoming release.



---

## Definition

A radio button is a UI element that allows users to select a single option from a set of mutually exclusive choices. The radio button, that lacks an additional icon asset or text label, provides greater flexibility when designing other components that incorporate a radio button.

---

## State

**`Enabled`** The default interactive state. The radio button can be either selected or unselected.

**`Hover`** When a user places a pointing device over a radio button, but has not yet taken action on it. This includes a subtle visual indicator (highlighted background or color change) to show interactivity.

**`Focus`** When a user selects a radio button via keyboard or voice command, but has not yet taken action on it.
Mirrors the "Hover" state but includes an additional border.

**`Pressed`** A temporary interaction state displayed while the user presses the radio button to select an option within its group.

**`Read only`** The radio button displays its current selection state, but the user cannot modify it.

**`Disabled`** The radio button cannot be selected or changed and is displayed using disabled-state styling.

**`Skeleton`** Improves the perceived loading time by providing a visual cue of where radio button will appear once fully loaded.
Uses the "Skeleton" component, variant “Security marge=True”.

---

## Selected

Typically, a radio button has two main states: Selected and Unselected.

**`False`** The radio button is unselected.
Used by default or when the user chooses another option in the group.

**`True`** The radio button is selected.
Indicates the user’s current active choice within the group.

---

## Error

**`False`** No validation error is displayed. The radio button may be selected or unselected.

**`True`** Applies the error appearance to the standalone radio button. Any associated validation message must be provided by the parent component or selection group.
