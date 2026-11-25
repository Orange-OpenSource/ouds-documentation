---
id: radio-button
category: Control
family: None
---

# Radio button

A radio button is a UI element that allows users to select a single option from a set of mutually exclusive choices.

# Guideline

<img src="images/hero_image_radio_button_item.png" alt="hero_image_radio_button_item" width="864">

## Anatomy

<img src="images/radio_button@anatomy_img.png" alt="radio_button@anatomy_img" width="864">

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Radio button indicator | Indicates the selection state of a radio option (selected or unselected). | No |
| 2 | Label | Primary text that describes the selectable option. | No |
| 3 | Extra label | Secondary label used to highlight critical or contextual information. | Yes |
| 4 | Description | Provides additional guidance or explanatory text for the option. | Yes |
| 5 | Icon | Solaris icon representing the option. | Yes |
| 6 | Divider | Visual separator used when multiple radio options are displayed in a list. | Yes |
| 7 | Error text | Displays validation or error messaging related to the radio option. | Yes |
| 8 | Error icon | Visual indicator that reinforces the error state of the option. | No |
| 9 | Outline | Outline indicating. | Yes |

## Definition

A **radio button** is a UI element that allows users to select a single option from a set of mutually exclusive choices.

The radio button, that lacks an additional icon asset or text label, provides greater flexibility when designing other components that incorporate a radio button.

A **radio button item** is a UI element shaped like a row, that allows users to select a single option from a set of mutually exclusive choices.

Unlike the radio button, the radio button item accommodates a broader range of contexts by enabling the toggling of visibility of additional text labels and icon assets.

## Selected

|  |
|

Typically, a radio button has two main states: Selected and Unselected.

<!-- zh-row -->

**`False`** The radio button is unselected. Used by default or when the user chooses another option in the group.

**`True`** The radio button is selected. Indicates the user's current active choice within the group.

<img src="images/radio_button@selected_img.png" alt="radio_button@selected_img" width="433">

## Error

<!-- zh-row -->

**`False`** The field is required but not selected. Example: the "I accept the terms" checkbox is not checked — user action is required.

**`True`** The field is selected but still invalid. Example: the user selects "Subscribe to newsletter" but doesn't provide an email — logical condition not met.

<img src="images/radio_button@error_img.png" alt="radio_button@error_img" width="433">

**Do:** Write specific, actionable error messages that tell users exactly what went wrong and how to fix it

**Don't:** Use generic error messages like "Invalid input" or "Error"—they don't help users understand the problem

## Outlined

<!-- zh-row -->

**`False`** This is the default layout of the component.

**`True`** Outlined radio buttons are designed to stand out and draw the user's attention. They are often used to emphasize significant or impactful options that require careful consideration in the interface.

<img src="images/radio_button@outlined_img.png" alt="radio_button@outlined_img" width="433">

## Reverse

<!-- zh-row -->

**`False`** This is the default layout of the component. From left to right, the order of the elements is as follows: radio button / text / icon.

**`True`** As its name suggests, this layout is the reversed mirror of the "Default" template. From left to right, the order of the elements is as follows: icon / text / radio button. This variant is necessary for RTL mode and certain mobile use cases.

<img src="images/radio_button@reverse_img.png" alt="radio_button@reverse_img" width="433">

## Other boolean options

<!-- zh-row -->

**`Extra label`** It is possible to display or hide strong accompanying text for the main label.

**`Description`** It is possible to display or hide accompanying text for the main label.

**`Icon`** It is possible to display or hide an icon. If displayed, this option includes functionality to choose any Solaris icon.

**`Divider`** It is possible to display or hide a dividing element (line).

**`Error message`** In the context where the component is in its "Error" true option, the error message can be displayed.

<img src="images/radio_button@other_boolean_options_img.png" alt="radio_button@other_boolean_options_img" width="433">

## Mandatory field indication

<!-- zh-row -->

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

<img src="images/radio_button@mandatory_field_indication_img.png" alt="radio_button@mandatory_field_indication_img" width="433">

<img src="images/radio_button@mandatory_field_indication_img2.png" alt="radio_button@mandatory_field_indication_img2" width="433">

## Multiline and responsiveness

<!-- zh-row -->

### Multiline
This component allows multi-line text editing. Although the number of lines is not technically limited, it is recommended not to exceed 2 lines of text. In its "Text + icon" variant, if the label spans multiple lines, the label remains centred.

&nbsp;

### Max-width vs full-width
For greater flexibility, this component doesn't have a default max-width. To avoid exceeding a width that would degrade readability and the perception of a compact interactive element, we recommend applying **a max-width of around 480px.**  
For mobile or tablet use (or if the component is positioned inside a specific container), it is possible to set this component to use the full available width (of the screen or the container).  
Please note that this behavior is not the default rule; it may be preferred if the template allows it (to improve user comfort or for better page structure/hierarchy).

&nbsp;

### User zoom in/out
The behavior of the text during user zoom in/out must follow a fundamental principle: the text must remain readable, accessible, and must never break the structure or lose information.
* The text must always scale proportionally with user zoom. Text resizing must never be blocked.
* Zooming must never cause text to be truncated or hidden. The component must expand vertically to allow line wrapping.
* The component's height and width must be flexible, never fixed, in order to automatically adapt its dimensions according to the level of zoom.
* In order to preserve the minimun interactive area during user zoom out, this component have a min-width **of 160px** and a min-height **of 52px**.
* Even if, the component has a max-height or a max-width for resizing control purposes, technically, during user zoom in, these limitations are not fixed but must be scalable in order to adapt to the user's zoom level.
* As the control item and error icon are functional, they must follow the same rules as text.
* In order to preserve the same display rendering as the component's error state, even if the icons is purely decorative, the icons follow the same rules as the text.

<img src="images/radio_button@multiline_and_responsiveness_img.png" alt="radio_button@multiline_and_responsiveness_img" width="433">

## Technical layout adjustments

<!-- zh-row -->

Even though, in Figma, the component structure is unique (for easier use by designers), technically the versions differ in order to respect best practices for each environment (paradigm shift between the web "Container" vs. the native "Edge-to-Edge"):

&nbsp;

### Web (mobile, tablet, and desktop)
The component is contained within the browser window and has "safety margins." It therefore cannot appear in the area corresponding to the margin grid.  
The component has internal padding-inline, and its display position must be between several columns (which varies depending on the number of containers used on a horizontal row).

&nbsp;

### Native app (Android, iOS, Flutter)
The display position of the component corresponds to the entire screen display area (edge to edge).  
Its internal padding-inline is therefore replaced by the grid-margin tokens.

<img src="images/radio_button@technical_layout_adjustments_img.png" alt="radio_button@technical_layout_adjustments_img" width="433">

<!-- zh-row -->

For a card-type display (Outlined=True), no adaptation is made; the component structure remains the same between web and native.

<img src="images/radio_button@technical_layout_adjustments_img2.png" alt="radio_button@technical_layout_adjustments_img2" width="433">

## Rich text

<!-- zh-row -->

### Strong text
* Strong text can be used sparingly to highlight key information within the content. Text is allowed using the corresponding "Strong" token (e.g. Label/Medium/Strong).
* No other text styles or custom font weights should be used.

&nbsp;

### ⚠️ Underline text
* Underlined text must not be applied manually (e.g. in error message), as it is commonly associated with hyperlinks and may mislead users.

<img src="images/radio_button@rich_text_img.png" alt="radio_button@rich_text_img" width="433">

# Specs

## Layout and spacing

<img src="images/radio_button@specs_layout_spacing_img.png" alt="radio_button@specs_layout_spacing_img" width="864">

## States

<!-- zh-row -->

**`Enabled`** The default active state where the radio button is functional and selectable. It may show an unselected or selected style, with a label and helper text visible.

**`Hover`** When a user places a pointing device over a radio button, but has not yet taken action on it. This includes a subtle visual indicator (highlighted background or color change) to show interactivity.

**`Focus`** When a user selects a radio button via keyboard or voice command, but has not yet taken action on it. Mirrors the "Hover" state but includes an additional border.

**`Pressed`** An intermediate state that communicates a user has taken action on a radio button, and that it is in the process of navigating to a destination, triggering logic, or transmitting data.

**`Read only`** The radio button is displayed in a specific state (selected or unselected), but the user cannot modify it with a label and helper text visible.

**`Disabled`** The radio button is non-interactive and grayed out to indicate it cannot be selected or changed. The label and helper text are  muted.

**`Skeleton`** Improves the perceived loading time by providing a visual cue of where radio button will appear once fully loaded. Uses the "Skeleton" component, variant "Security marge=True".

<img src="images/radio_button@state_img.png" alt="radio_button@state_img" width="433">

# Accessibility

Work is in progress to deliver this content.

# Develop

## OUDS Web

[Components/RadioButtons › Radio Buttons 0](https://web.unified-design-system.orange.com/storybook/?path=/story/components-radiobuttons--radio-buttons-0)

[Components/RadioButtons › Radio Buttons 15](https://web.unified-design-system.orange.com/storybook/?path=/story/components-radiobuttons--radio-buttons-15)

## Developer Documentation

| Platform | Developer documentation |
|---|---|
| OUDS Web | [S-ouds-web-radio-button](https://r.orange.fr/r/S-ouds-web-radio-button) |
| OUDS Android | [S-ouds-android-radio-button](https://r.orange.fr/r/S-ouds-android-radio-button) |
| OUDS iOS | [S-ouds-ios-radio-button](https://r.orange.fr/r/S-ouds-ios-radio-button) |
| OUDS Flutter | [S-ouds-flutter-radio-button](https://r.orange.fr/r/S-ouds-flutter-radio-button) |

# Changelog

## Availability

| Platform | Resource | Status | Version |
|---|---|---|---|
| Figma | [Radio button component](https://r.orange.fr/r/S-ouds-design-radio-button) | Live | 1.4.0 |
| OUDS Web (former Boosted) | [Web dev documentation](https://r.orange.fr/r/S-ouds-web-radio-button) | Live | 1.4.0 |
| OUDS Android - Jetpack Compose | [Android dev documentation](https://r.orange.fr/r/S-ouds-android-radio-button) | Live | 1.4.0 |
| OUDS iOS - Swift | [iOS dev documentation](https://r.orange.fr/r/S-ouds-ios-radio-button) | Live | 1.4.0 |
| OUDS Flutter | [Flutter dev documentation](https://r.orange.fr/r/S-ouds-flutter-radio-button) | Live | 1.4.0 |

## Design changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Apr 8, 2026 | - | <ul><li>Documentation writing: Rich text</ul> | Anton Astafev |
| Mar 16, 2026 | - | <ul><li>Documentation writing:<ul><li>Mandatory field indication<li>Multiline and responsiveness<li>Technical layout adjustments</ul></ul> | Maxime Tonnerre |
| Jan 6, 2026 | - | <ul><li>Documentation writing: Definition update</ul> | Cyriaque Billard |
| Nov 7, 2025 | 1.4.0 | <ul><li>A new Read-only variant has been added for the .Radiobutton.Indicator component, supporting two boolean variants — Selected = True/False. This variant introduces two new color tokens: <ul><li>ouds/color/action/read-only-primary — used for the indicator (shape) <li>ouds/color/action/read-only-secondary — used for the stroke</ul> <li>The new Read-only variant has been integrated into the Read-only variant of both the Radio button and Radio button Item components. <li>We replaced the token in Error text container ouds-control-text-input-space-padding-block-top-helper-text with ouds-control-control-item-space-padding-block-top-error-text. <li>"Helper text" is now called "Description". <li>"Additional label" is now called "Extra label".</ul> | Anton Astafev |
| Oct 20, 2025 | 1.3.0 | <ul><li>The Radio button item has been split into two boolean variants: → Error = True/False → Selected = True/False <li>The divider color is now functional in the Error state — it changes dynamically according to the component status. <li>The icon in the Error state is fixed to .Component/alert/important; its color changes together with the divider depending on the component's status. → The new token $control-control-item-size-error-icon is used for the icon size. → The new token $control-text-input-space-padding-inline-error-icon is used for the error icon container. 🆕 Both tokens are now available in the latest release of the Token Library 2.1.0. <li>Added Error text (from the Input component) — it follows the same padding-inline as control-item (16px) and uses → $control-text-input-space-padding-block-top-helper-text for block padding. By default, the Error text adapts automatically to match the component status: → Selected → displays the corresponding default error message for the selected state. → Unselected → displays the corresponding default error message for the unselected state. <li>The "Read only" state has been updated to replace control items (in their disabled states) — both selected and unselected — with the Tag → Text only → Muted component: → Positive with label "Selected" if selected = True → Negative with label "Unselected" if selected = False <li>Harmonisation of spacing across the control-item family We've unified sizing tokens across the entire control-item family (previously they were defined per component) to align spacing with other control items such as Text input. Replacement note: instead of the single token padding inset 12, use the following tokens: → ouds/_control/control-item/space/padding-inline → 16 → ouds/_control/control-item/space/padding-block → 12 Additionally, for the control-item family: → ouds/_control/control-item/space/column-gap → 12 → ouds/_control/control-item/size/max-width → 480</ul> | Anton Astafev |
| Sep 19, 2025 | 1.2.0 | <ul><li>In the initial settings, the 'Divider' variant is now hidden.</ul> | Maxime Tonnerre |
| Jul 21, 2025 | 1.1.0 | <ul><li>The name of the family to which this component belongs is changing: Input → Control. As a result, the token naming convention is being updated. <li>Following the renaming of the 'Control' category, the name of the token sub-family 'control-item' is now becoming 'item'."</ul> | Maxime Tonnerre |
| Jan 22, 2025 | 1.0.0 | <ul><li>Component creation</ul> | Maxime Tonnerre |
