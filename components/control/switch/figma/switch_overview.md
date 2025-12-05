## Definition

A switch is a component that allows the user to toggle between two states, typically "on" and "off." It is often represented as a button or a slider that changes position or color to indicate the current state. Switches are used to enable or disable features, options, or settings in an intuitive and visual manner.

This component family is available in two variants:
• **Switch:** In this template, the component does not display any text or icon. This layout provides greater flexibility when creating other components that require a switch to be displayed.
• **Switch item:** In this template, the component displays multiple additional text elements and icon assets.

---

## State

**`Enabled`** The status of the switch before a user has interacted with it, or other content affects it.

**`Hover`** When a user places a pointing device over a switch, but has not yet taken action on it.

**`Focus`** When a user selects a switch via keyboard or voice command, but has not yet taken action on it. Mirrors the "Hover" state but includes an additional border.

**`Pressed`** An intermediate state that communicates a user has taken action on a switch, and that it is in the process of navigating to a destination, triggering logic, or transmitting data.

**`Read only`** The switch is displayed in a specific state (true or false), but the user cannot modify it.

**`Disabled`** Used to indicate an option that cannot be selected.

**`Skeleton`** Improves the perceived loading time by providing a visual cue of where switch will appear once fully loaded. Uses the "Skeleton" component, variant "Security marge=True".

---

## Selected

Typically, a switch has two main states: Selected and Unselected.

**`False`** The switch is off — the option or feature is disabled. Used as the default state before activation.

**`True`** The switch is on — the option or feature is enabled. Indicates that the setting or action is currently active.

---

## Error

**`False`** The switch is unselected or turned off, but this value is invalid. Used when a required action hasn't been completed or an active state is expected.

**`True`** The switch holds a value, but it does not meet logical or validation requirements. Used when the current state (on or off) causes a conflict or violates form rules.

---

## Reverse

**`False`** This is the default layout of the component. From left to right, the order of the elements is as follows: icon / text / switch.

**`True`** As its name suggests, this layout is the reversed mirror of the "Default" template. From left to right, the order of the elements is as follows: switch / text / icon. This variant is necessary for RTL mode and certain mobile use cases.

---

## Other boolean options

**`Description`** It is possible to display or hide accompanying text for the main label.

**`Icon`** It is possible to display or hide an icon. If displayed, this option includes functionality to choose any Solaris icon.

**`Divider`** It is possible to display or hide a dividing element (line).

**`Error message`** In the context where the component is in its "Error" true option, the error message can be displayed.

---

✅ Complete documentation extracted