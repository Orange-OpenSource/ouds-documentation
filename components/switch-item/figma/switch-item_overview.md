## Future update! The version 1.7.0 is currently being designed; it will be released in an upcoming release.



---

## Definition

A switch item is a UI element that toggles between two states, typically "On" and "Off," and is used to enable or disable features, options, or settings. Unlike the switch, the switch item accommodates a broader range of contexts by enabling the toggling of visibility of additional text labels and icon assets.

---

## State

**`Enabled`** The status of the switch before a user has interacted with it, or other content affects it.

**`Hover`** When a user places a pointing device over a switch, but has not yet taken action on it.

**`Focus`** When a user selects a switch via keyboard or voice command, but has not yet taken action on it.
Mirrors the "Hover" state but includes an additional border.

**`Pressed`** A temporary interaction state displayed while the user presses the Switch item to change its current On/Off state.

**`Read only`** The switch is displayed in a specific state (true or false), but the user cannot modify it.

**`Disabled`** Used to indicate an option that cannot be selected.

**`Skeleton`** Improves the perceived loading time by providing a visual cue of where switch will appear once fully loaded.
Uses the "Skeleton" component, variant “Security marge=True”.

---

## Selected

Typically, a switch has two main states: Selected and Unselected.

**`False`** The switch is off, the option or feature is disabled.
Used as the default state before activation.

**`True`** The switch is on, the option or feature is enabled.
Indicates that the setting or action is currently active.

---

## Error

**`False`** No validation error is displayed. The Switch item may be either On or Off.

**`True`** Applies the error appearance to the Switch item when its current value does not meet validation requirements. If an error message is displayed, it must clearly explain the issue.

---

## Reverse

**`False`** This is the default layout of the component.
From left to right, the order of the elements is as follows: icon / text / switch.

**`True`** As its name suggests, this layout is the reversed mirror of the "Default" template.
From left to right, the order of the elements is as follows: switch / text / icon. This variant is necessary for RTL mode and certain mobile use cases.

---

## Other boolean options

**`Description`** It is possible to display or hide accompanying text for the main label.

**`Icon`** It is possible to display or hide an icon. If displayed, this option includes functionality to choose any Solaris icon.

**`Divider`** It is possible to display or hide a dividing element (line).

**`Error message`** In the context where the component is in its "Error" true option, the error message can be displayed.

---

## ⚠️ Mandatory field indication

**If all fields are mandatory (several fields present):**
• Display the message “All fields are mandatory.” at the top.
• Do not use an asterisk (*) at the end of each field label, nor the word “mandatory.”

**If not all fields are mandatory (and there are several fields present):**
• Display the message “All fields marked with an * are mandatory.” at the top.
• Use an asterisk (*) at the end of each mandatory field label.
**⚠️ Important:**
  • In Figma, the asterisk must be entered manually by designers in the label text.
UI rendering of the asterisk: font-weight-bold + color-content-negative (red).
  • Technically, for web/iOS/Android, the asterisk is positioned in a dedicated container after the label text.
Spacing between label and asterisk: 4px
• Either the technology allows a 'required' attribute to be managed on the fields (usually in Web), in which case any asterisks must be hidden from users using assistive technologies,
Or the technology does not allow the mandatory nature of the field to be indicated. In this case, the asterisk must be vocalised as well as a 'mandatory' mention.
Please refer to the technical documentations for more information.
• Depending on the use case, an 'optional' label can be added to non-mandatory fields.

**Indication of mandatory status for a group of control items:**
When a group of control items (Radio Button, Checkbox, or Switch item) is mandatory, the indication of requirement must be carried only by the group title.
The asterisk (*) must be placed at the end of the group title and must not be repeated in the labels of the individual items.
This rule avoids visual redundancy, clarifies that the requirement applies to the group rather than each option, and improves information hierarchy and form readability.

**If there is only one field in the form, or if the mandatory nature is obvious (such as login/password), no mention is necessary since the fields are essential to the form’s functionality.**

---

## Multiline and responsiveness

**`Multiline`** This component allows multi-line text editing. Although the number of lines is not technically limited, it is recommended not to exceed 2 lines of text. In its “Text + icon” variant, if the label spans multiple lines, the label remains centred.

**Max-width vs full-width**
For greater flexibility, this component doesn’t have a default max-width. To avoid exceeding a width that would degrade readability and the perception of a compact interactive element, we recommend applying a max-width of around 480px.
For mobile or tablet use (or if the component is positioned inside a specific container), it is possible to set this component to use the full available width (of the screen or the container).
Please note that this behavior is not the default rule; it may be preferred if the template allows it (to improve user comfort or for better page structure/hierarchy).

**User zoom in/out**
The behavior of the text during user zoom in/out must follow a fundamental principle: the text must remain readable, accessible, and must never break the structure or lose information.
  • The text must always scale proportionally with user zoom. Text resizing must never be blocked.
  • Zooming must never cause text to be truncated or hidden. The component must expand vertically to allow line wrapping.
  • The component’s height and width must be flexible, never fixed, in order to automatically adapt its dimensions according to the level of zoom.
  • In order to preserve the minimun interactive area during user zoom out, this component have a min-width of 160px and a min-height of 52px.
  • Even if, the component has a max-height or a max-width for resizing control purposes, technically, during user zoom in, these limitations are not fixed but must be scalable in order to adapt to the user’s zoom level.
  • As the control item and error icon are functional, they must follow the same rules as text.
  • In order to preserve the same display rendering as the component’s error state, even if the icons is purely decorative, the icons follow the same rules as the text.

---

## Technical layout adjustments

Even though, in Figma, the component structure is unique (for easier use by designers), technically the versions differ in order to respect best practices for each environment (paradigm shift between the web “Container” vs. the native “Edge-to-Edge”):

**Web (mobile, tablet, and desktop)**
The component is contained within the browser window and has “safety margins.” It therefore cannot appear in the area corresponding to the margin grid.
The component has internal padding-inline, and its display position must be between several columns (which varies depending on the number of containers used on a horizontal row).

**Native app (Android, iOS, Flutter)**
The display position of the component corresponds to the entire screen display area (edge to edge).
Its internal padding-inline is therefore replaced by the grid-margin tokens.

---

## Rich text

**`Strong text`**   • Strong text can be used sparingly to highlight key information within the content. Text is allowed using the corresponding "Strong" token (e.g. Label/Medium/Strong).
  • No other text styles or custom font weights should be used.

• ****⚠️ Underline text****
  • Underlined text must not be applied manually (e.g. in error message), as it is commonly associated with hyperlinks and may mislead users.

---

## Motion & Animation accessibility rules

In terms of animation, there are accessibility criteria to consider: “Animation from Interactions” and “Pause, Stop, Hide.”
These two main criteria address different issues:

**Pause, Stop, Hide - WCAG 2.2.2**
This concerns moving, blinking, scrolling, or automatically updating content.
The question to ask is: does the animation start automatically and meet the criterion’s conditions?
When a relevant animation lasts more than 5 seconds, users must be able to pause, stop, or hide it.
The two criteria should therefore be evaluated independently.

**Reduced Motion (Animation from Interactions) - WCAG 2.3.3**
This primarily concerns motion-based animations triggered by user interaction.
The question to ask is: is the movement essential to the functionality or to the information being conveyed?
If not, the animation should be removed, reduced, or replaced when the user has enabled Reduced Motion.

ℹ️ The reduced motion preference can be configured by the user at the operating system level and is available to websites through the CSS prefers-reduced-motion media feature.

Concrete application to the Switch:

**Pause, Stop, Hide**
The animation of a switch is triggered by a user action and therefore does not generally fall within the scope of this criterion.
If the state change triggers additional animation or automatically moving content that meets the conditions of the criterion, that content must be evaluated separately.

**Reduced Motion**
The animation applied when a switch changes state is generally not essential to its functionality or to understanding its state.
When Reduced Motion is enabled, the animation should therefore be removed or replaced with an instantaneous transition.
The state of the switch must remain clearly identifiable without relying on animation.
Default: animated state change
Reduced Motion: instantaneous state change
