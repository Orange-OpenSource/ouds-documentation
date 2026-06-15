## Definition

A button is a fundamental interactive UI element that allows users to trigger an action or event within an interface, such as submitting a form, opening a dialog, or navigating to another page. Visually, it's typically styled to stand out as clickable, using shape, color, and label to convey its purpose.

---

## Appearance

**`Default`** Default buttons are used for actions which are not mandatory or essential for the user. Often screens will include multiple Outline buttons alongside one of the Full button.

**`Strong`** The Strong button on the page should be singular and prominent, ideally limited to one per view. It should be reserved for the most critical action, such as "Buy," "Save," "Submit," etc.

**`Brand`** A brand primary color alternative to the Strong button.
To be used sparingly for high-value specific actions or to visually anchor a brand moment. Do not use it as the default primary button in your interfaces.

**`Minimal`** Minimal buttons are commonly used for actions that are considered less crucial. They can be used independently or together with a strong button.

**`Negative`** Negative buttons should be used sparingly to warn of a destructive action, for example, delete or remove, typically resulting in the opening of a confirmation dialog.

---

## Layouts

**`Text only`** This is the default layout of the component.

**`Text + icon`** This option includes functionality to choose any Solaris icon.
Its use must be restricted and remain specific to certain clearly identified contexts (e.g., the use of an icon within a "Play" button is standard in the context of TV or video streaming).

**`Icon only`** Typically utilized in business or back-office interfaces, it is rarely standalone (usually part of a group of elements).

---

## States

**`Enabled`** The status of the button before a user has interacted with it, or other content affects it.

**`Hover`** When a user places a pointing device over a button, but has not yet taken action on it.

**`Focus`** When a user selects a button via keyboard or voice command, but has not yet taken action on it.
Mirrors the "Hover" state but includes an additional border.

**`Pressed`** An intermediate state that communicates a user has taken action on a button, and that it is in the process of navigating to a destination, triggering logic, or transmitting data.

**`Loading`** A button is fetching data from another internal or external resource.
Uses the "Loading indicator" component.

**`Disabled`** Used to indicate a button that cannot be selected.

**`Skeleton`** Improves the perceived loading time by providing a visual cue of where button will appear once fully loaded.
Uses the "Skeleton" component, variant "Security marge=False".

---

## Rounded corner

**`False`** For a square finish.

**`True`** For a finish with rounded corner.
To be favored in more emotional, immersive contexts or those tied to specific visual identities. For standard or business-oriented journeys, keep the default corners. This evolution addresses the need for flexibility in adapting the design to certain brand contexts.

**Brand theme availability**
This option is technically not available for all brand themes. Here's the list of rounded corners availability by brand theme:

| Brand theme | Availability |
|---|---|
| Orange | ✅ Available |
| Orange Compact | ✅ Available |
| Sosh | ❌ Unavailable |
| Wireframe | ❌ Unavailable |

---

## Specific component: On colored bg

This variant ensures a sufficiently high level of accessibility when the component is used on a background that is "out of control".

**To invert color**
• In light mode: For a black finish
• In dark mode: For a white finish

---

## Multiline and responsiveness

**Multiline**
This component allows multi-line text editing. Although the number of lines is not technically limited, it is recommended not to exceed one line of text.
In its "Text + icon" variant, if the label spans multiple lines, the label remains horizontally centred and the icon remains vertically centred.

**Max-width vs full-width**
For greater flexibility, this component doesn't have a default max-width. To avoid exceeding a width that would degrade readability and the perception of a compact interactive element, we recommend applying **a max-width of around 360px.**
The component can also naturally wrap within the parent container (or the screen in a mobile use context for exemple) and use the full available width.
Please note that this behavior is not the default rule; it may be preferred if the template allows it (to improve user comfort or for better page structure/hierarchy).

**User zoom in/out**
The behavior of the text during user zoom in/out must follow a fundamental principle: the text must remain readable, accessible, and must never break the structure or lose information.
* The text must always scale proportionally with user zoom. Text resizing must never be blocked.
* Zooming must never cause text to be truncated or hidden. The component must expand vertically to allow line wrapping.
* The component's height and width must be flexible, never fixed, in order to automatically adapt its dimensions according to the level of zoom.
* In order to preserve the minimun interactive area during user zoom out, this component have a min-width and a min-height **of 48px**.
* Even if, the component has a max-height or a max-width for resizing control purposes, technically, during user zoom in, these limitations are not fixed but must be scalable in order to adapt to the user's zoom level.
* In its "Text + icon" variant, user zoom in/out doesn't affect the size of the icons; they remain fixed in size (decorative use).
* As the text is missing, in its "Icon only" variant, the icons follow the same rules as the text.

---
