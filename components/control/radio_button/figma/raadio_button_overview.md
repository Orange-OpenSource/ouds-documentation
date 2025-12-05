## Definition

A radio button is a user interface element that allows users to select a single option from a set of mutually exclusive choices, typically displayed as a circular input with a label that becomes filled when selected.

This component family is available in two variants:
• **Radio-button:** In this template, the component does not display any text or icon. This layout provides greater flexibility when creating other components that require a radio-button to be displayed.
• **Radio-button item:** In this template, the component displays multiple additional text elements and icon assets.

---

## State

**`Enabled`** The default active state where the radio button is functional and selectable. It may show an unselected or selected style, with a label and helper text visible.

**`Hover`** When a user places a pointing device over a radio button, but has not yet taken action on it. This includes a subtle visual indicator (highlighted background or color change) to show interactivity.

**`Focus`** When a user selects a radio button via keyboard or voice command, but has not yet taken action on it. Mirrors the "Hover" state but includes an additional border.

**`Pressed`** An intermediate state that communicates a user has taken action on a radio button, and that it is in the process of navigating to a destination, triggering logic, or transmitting data.

**`Read only`** The radio button is displayed in a specific state (selected or unselected), but the user cannot modify it with a label and helper text visible.

**`Disabled`** The radio button is non-interactive and grayed out to indicate it cannot be selected or changed. The label and helper text are  muted.

**`Skeleton`** Improves the perceived loading time by providing a visual cue of where radio button will appear once fully loaded. Uses the "Skeleton" component, variant "Security marge=True".

---

## Selected

Typically, a radio button has two main states: Selected and Unselected.

**`False`** The radio button is unselected. Used by default or when the user chooses another option in the group.

**`True`** The radio button is selected. Indicates the user's current active choice within the group.

---

## Error

**`False`** The field is required but not selected. Example: the "I accept the terms" checkbox is not checked — user action is required.

**`True`** The field is selected but still invalid. Example: the user selects "Subscribe to newsletter" but doesn't provide an email — logical condition not met.

---

## Outlined

**`False`** This is the default layout of the component.

**`True`** Outlined radio buttons are designed to stand out and draw the user's attention. They are often used to emphasize significant or impactful options that require careful consideration in the interface.

---

## Reverse

**`False`** This is the default layout of the component. From left to right, the order of the elements is as follows: radio button / text / icon.

**`True`** As its name suggests, this layout is the reversed mirror of the "Default" template. From left to right, the order of the elements is as follows: icon / text / radio button. This variant is necessary for RTL mode and certain mobile use cases.

---

## Other boolean options

**`Extra label`** It is possible to display or hide strong accompanying text for the main label.

**`Description`** It is possible to display or hide accompanying text for the main label.

**`Icon`** It is possible to display or hide an icon. If displayed, this option includes functionality to choose any Solaris icon.

**`Divider`** It is possible to display or hide a dividing element (line).

**`Error message`** In the context where the component is in its "Error" true option, the error message can be displayed.

---