## Future update! The version 2.5.0 is currently being designed; it will be released in an upcoming release.



---

## Definition

A checkbox is a UI element that enables users to select multiple options from a set of mutually non-exclusive choices. The checkbox, that lacks an additional icon asset or text label, offers greater flexibility when designing other components that incorporate a checkbox.

---

## State

**`Enabled`** The status of the checkbox before a user has interacted with it, or other content affects it.

**`Hover`** When a user places a pointing device over a checkbox, but has not yet taken action on it.

**`Focus`** When a user selects a checkbox via keyboard or voice command, but has not yet taken action on it.
Mirrors the "Hover" state but includes an additional border.

**`Pressed`** An intermediate state that communicates a user has taken action on a checkbox, and that it is in the process of navigating to a destination, triggering logic, or transmitting data.

**`Read only`** The checkbox is displayed in a specific state (selected or unselected), but the user cannot modify it.

**`Disabled`** Used to indicate an option that cannot be selected.

**`Skeleton`** Improves the perceived loading time by providing a visual cue of where checkbox will appear once fully loaded.
Uses the "Skeleton" component, variant “Security marge=True”.

---

## Selection status

**`Unselected`** By default, a checkbox is often in this state.
This state indicates that the user has not selected the associated option.

**`Selected`** Indicates that the user has selected the option.
This often corresponds to an action or validation.

**`Indeterminate`** Often used when the checkbox represents a partial selection. For example, in a nested (hierarchical) list, a parent checkbox can be indeterminate if some but not all sub-options are checked.
This is not a state the user directly selects but is calculated by the system.

---

## Error

**`False`** Used when the checkbox is unchecked but required.
Example: user must agree to terms, but didn’t check the box.

**`True`** Used when the checkbox is checked but still invalid.
Example: the selection conflicts with another field or fails validation.
