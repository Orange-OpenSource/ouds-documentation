## Definition

A checkbox component is a user interface element used to allow the user to selection-control or deselection-control an option. It is commonly used in forms, web interfaces, or applications to capture multiple or single choices.

This component family is available in two variants:
• **Checkbox:** In this template, the component does not display any text or icon. This layout provides greater flexibility when creating other components that require a checkbox to be displayed.
• **Checkbox item:** In this template, the component displays multiple additional text elements and icon assets.

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
Uses the "Skeleton" component, variant "Security marge=True".

---

## Selection status

**`Selected`** Indicates that the user has selected the option.
This often corresponds to an action or validation.

**`Unselected`** By default, a checkbox is often in this state.
This state indicates that the user has not selected the associated option.

**`Indeterminate`** Often used when the checkbox represents a partial selection. For example, in a nested (hierarchical) list, a parent checkbox can be indeterminate if some but not all sub-options are checked.
This is not a state the user directly selects but is calculated by the system.

---

## Error

**`False`** Used when the checkbox is unchecked but required.
Example: user must agree to terms, but didn't check the box.

**`True`** Used when the checkbox is checked but still invalid.
Example: the selection conflicts with another field or fails validation.

---

## Reverse

**`False`** This is the default layout of the component.
From left to right, the order of the elements is as follows: checkbox / text / icon.

**`True`** As its name suggests, this layout is the reversed mirror of the "Default" template.
From left to right, the order of the elements is as follows: icon / text / checkbox. This variant is necessary for RTL mode and certain mobile use cases.

---

## Other boolean options

**`Description`** It is possible to display or hide accompanying text for the main label.

**`Icon`** It is possible to display or hide an icon. If displayed, this option includes functionality to choose any Solaris icon.

**`Divider`** It is possible to display or hide a dividing element (line).

**`Error message`** In the context where the component is in its "Error" true option, the error message can be displayed.

---