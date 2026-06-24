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

## Mandatory field indication

**If all fields are mandatory (several fields present):**
1. Display the message "All fields are mandatory." at the top.
2. Do not use an asterisk (*) at the end of each field label, nor the word "mandatory."

**If not all fields are mandatory (and there are several fields present):**
1. Display the message "All fields marked with an * are mandatory." at the top.
2. Use an asterisk (*) at the end of each mandatory field label.
   **⚠️ Important:**
   * In Figma, the asterisk must be entered manually by designers in the label text. UI rendering of the asterisk: **font-weight-bold + color-content-negative (red)**.
   * Technically, for web/iOS/Android, the asterisk is positioned in a dedicated container after the label text. Spacing between label and asterisk: 4px
3. Either the technology allows a 'required' attribute to be managed on the fields (usually in Web), in which case any asterisks must be hidden from users using assistive technologies, Or the technology does not allow the mandatory nature of the field to be indicated. In this case, the asterisk must be vocalised as well as a 'mandatory' mention. Please refer to the technical documentations for more information.
4. Depending on the use case, an 'optional' label can be added to non-mandatory fields.

**Indication of mandatory status for a group of control items:**
When a group of control items (Radio Button, Checkbox, or Switch item) is mandatory, the indication of requirement must be carried only by the group title.
The asterisk (*) must be placed at the end of the group title and must not be repeated in the labels of the individual items.
This rule avoids visual redundancy, clarifies that the requirement applies to the group rather than each option, and improves information hierarchy and form readability.

**If there is only one field in the form, or if the mandatory nature is obvious (such as login/password), no mention is necessary since the fields are essential to the form's functionality.**

---

## Multiline and responsiveness

**Multiline**
This component allows multi-line text editing. Although the number of lines is not technically limited, it is recommended not to exceed 2 lines of text. In its "Text + icon" variant, if the label spans multiple lines, the label remains centred.

**Max-width vs full-width**
For greater flexibility, this component doesn't have a default max-width. To avoid exceeding a width that would degrade readability and the perception of a compact interactive element, we recommend applying **a max-width of around 480px.**
For mobile or tablet use (or if the component is positioned inside a specific container), it is possible to set this component to use the full available width (of the screen or the container).
Please note that this behavior is not the default rule; it may be preferred if the template allows it (to improve user comfort or for better page structure/hierarchy).

**User zoom in/out**
The behavior of the text during user zoom in/out must follow a fundamental principle: the text must remain readable, accessible, and must never break the structure or lose information.
* The text must always scale proportionally with user zoom. Text resizing must never be blocked.
* Zooming must never cause text to be truncated or hidden. The component must expand vertically to allow line wrapping.
* The component's height and width must be flexible, never fixed, in order to automatically adapt its dimensions according to the level of zoom.
* In order to preserve the minimun interactive area during user zoom out, this component have a min-width **of 160px** and a min-height **of 52px**.
* Even if, the component has a max-height or a max-width for resizing control purposes, technically, during user zoom in, these limitations are not fixed but must be scalable in order to adapt to the user's zoom level.
* As the control item and error icon are functional, they must follow the same rules as text.
* In order to preserve the same display rendering as the component's error state, even if the icons is purely decorative, the icons follow the same rules as the text.

---

## Technical layout adjustments

Even though, in Figma, the component structure is unique (for easier use by designers), technically the versions differ in order to respect best practices for each environment (paradigm shift between the web "Container" vs. the native "Edge-to-Edge"):

**Web (mobile, tablet, and desktop)**
The component is contained within the browser window and has "safety margins." It therefore cannot appear in the area corresponding to the margin grid.
The component has internal padding-inline, and its display position must be between several columns (which varies depending on the number of containers used on a horizontal row).

**Native app (Android, iOS, Flutter)**
The display position of the component corresponds to the entire screen display area (edge to edge).
Its internal padding-inline is therefore replaced by the grid-margin tokens.

For a card-type display (Outlined=True), no adaptation is made; the component structure remains the same between web and native.

---

## Rich text

**Strong text**
* Strong text can be used sparingly to highlight key information within the content. Text is allowed using the corresponding "Strong" token (e.g. Label/Medium/Strong).
* No other text styles or custom font weights should be used.

**⚠️ Underline text**
* Underlined text must not be applied manually (e.g. in error message), as it is commonly associated with hyperlinks and may mislead users.

---