---
id: quantity-input
category: Control
family: None
---

# Quantity input

A quantity input is a UI element that lets users specify a numerical value representing a quantity.

# Guideline

<img src="images/hero_image_quantity_input.png" alt="hero_image_quantity_input" width="864">

## When to use

✅ When users need to specify a numeric quantity within a limited range

✅ For scenarios with incremental increase or decrease controls

✅ In e-commerce, ordering, or settings where precision matters

✅ When direct input and + / − controls are both acceptable

## Anatomy

<img src="images/quantity_input@anatomy_img.png" alt="quantity_input@anatomy_img" width="864">

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Label | Tells users what information to enter | No |
| 2 | Container | Holds and aligns all parts of the field (label, value, icons, etc.). | No |
| 3 | Decrement action | Decreases the quantity value by one increment. | No |
| 4 | Divider | Shows separation. | No |
| 5 | Increment action | Increases the quantity value by one increment. | Yes |
| 6 | Divider | The visible divider for the non-outlined style. | Yes |
| 7 | Helper text | Supplementary text displayed below the input field providing guidance or requirements. | Yes |
| 8 | Leading icon | Provides a visual cue about the field type. | Yes |
| 9 | Label | Moves above the input when focused or filled, so the field stays identifiable. | No |
| 10 | Text cursor | Indicates where the next character will be inserted while typing. | No |
| 11 | Placeholder | Shows an example or hint when the field is empty and focused. | No |
| 12 | Loading indicator | Shows progress while validation or authentication is in progress. | Yes |
| 13 | Outlined container | Alternative visual style using a full border. | Yes |
| 14 | Error icon | Highlights the field’s error state to improve visibility and feedback | Yes |
| 15 | Error text | Explains what’s wrong and how to fix it when validation fails. | Yes |

## Definition

A quantity input is a UI element that lets users specify a numerical value representing a quantity.

The quantity input typically combines a numeric text field with increment and decrement controls (like “+” and “–” buttons) for easy and precise adjustments. It enforces valid input ranges (minimum of one), prevents invalid characters, and supports keyboard input, stepper controls, and assistive technologies.

## Outlined

<!-- zh-row -->

**`False`** An input with a subtle background fill and un visible bottom border, creating a softer and more contained look. Best suited for dense layouts or to enhance visibility.

**`True`** A minimalist input with a transparent background and a visible stroke outlining the field. This style may be interesting for contexts other than form pages:
* When inputs need to feel lightweight and unobtrusive
* In a header (search field)
* In a selection/filtering feature in a product catalog

<img src="images/quantity_input@outlined_img.png" alt="quantity_input@outlined_img" width="433">

## Rounded corner

<!-- zh-row -->

Even though in Figma this rendering option is available and editable from the properties of each input component, the configuration of this rendering option is actually transversal across the entire product/service in which the component is used. It is therefore impossible to have one input component set to Rounded corner=True and another set to Rounded corner=False within the same product/service.

**`False`** The square rendering corresponds to Orange's historical style. It conveys the brand's sense of seriousness, robustness and utility-driven. It remains the default style for our digital interface components.

**`True`** The rounded rendering offers flexibility without sacrificing the attribution to the brand. It helps anchoring the service in a reality where the visual codes of the mobile area tends to rub off on all interfaces. Use rounded corners for a softer, more approachable, friendly and tactile feel.

This option is technically not available for all brand themes. Here's the list of rounded corners availability by brand theme:

| Brand theme | Status |
|---|---|
| Orange | ✅ Available |
| Orange Compact | ✅ Available |
| Sosh | ❌ Unavailable |
| Wireframe | ❌ Unavailable |

<img src="images/quantity_input@rounded_corner_img.png" alt="quantity_input@rounded_corner_img" width="433">

## Input status

<!-- zh-row -->

### Input status

**`Empty`** The Empty state indicates that the quantity input is blank with no content or placeholder, a neutral starting point.

**`Empty (Placeholder)`** The Empty with Placeholder state provides a hint or guidance inside the field to suggest expected input.

**`Filled`** The Filled state shows that the user has entered valid content into the field, replacing any placeholder.

<img src="images/quantity_input@input_status_img.png" alt="quantity_input@input_status_img" width="433">

## Actions placement

<!-- zh-row -->

**`Trailing`** It places both the increment and decrement buttons on the right side of the input field, either stacked vertically or positioned side by side. This layout is compact and visually streamlined, making it ideal for dense interfaces or mobile views.

**`Split`** It positions the decrement button to the left of the input and the increment button to the right. It provides a more balanced and intuitive interaction model, especially in use cases like e-commerce where users frequently adjust quantities.

<img src="images/quantity_input@actions_placement_img.png" alt="quantity_input@actions_placement_img" width="433">

## Specific focus state rules

<!-- zh-row -->

### Keyboard input disabled

In the vast majority of modern UX/UI cases, a quantity input should be editable on focus. However, there are a few specific rare cases where direct editing by keyboard input might be disabled:
* Highly guided or controlled usage→product configuration with mandatory steps
* Risk of critical error→specific or technical values
* Strict touch context→mobile app with simplified UI, no keyboard
* Deliberate product decision→to enforce navigation or a business constraint

In this specific context, it is therefore recommended to prefill the input by default.

<img src="images/quantity_input@specific_focus_state_rules_focus_img.png" alt="quantity_input@specific_focus_state_rules_focus_img" width="433">

<!-- zh-row -->

### Keyboard input + increment/decrement controls enabled

In the context of an editable quantity input, if the field is focused and already filled by the user, then clicking the + (increase) or – (decrease) buttons must follow a smooth and predictable behavior according to the following UX rules.

**When clicking + or – during editing:**
* The value is automatically validated
* The action is applied to that value (+1 or –1)
* The field is visually updated with the new value
* The cursor is moved to the end of the field (optional)
* The field remains focused

**Absolutely to avoid:**
* Losing the currently typed value if partially entered
* Requiring defocus for the buttons to work
* Failing to parse/validate the value before incrementing

**Specific error focus state:**  
If the value in the field is invalid (empty or non-numeric), clicking + or – may:
* Either fill in a default value (1)
* Or display a temporary blocking error ("Please enter a number")

<img src="images/quantity_input@specific_focus_state_rules_steps_img.png" alt="quantity_input@specific_focus_state_rules_steps_img" width="433">

## Error

<!-- zh-row -->

The Error status indicates that the user input does not meet validation rules or expected formatting. It provides immediate visual feedback, typically through a red border, error icon, and a clear, accessible error message positioned below the input (mandatory).

This state helps users quickly identify and correct mistakes by explaining what went wrong and, when possible, how to fix it. The input remains editable, encouraging users to revise their input without starting over.

If the input is filled, an "error" status is triggered by the entry of a value that is too small, too large, or non-numeric.

**⚠️ Error message vs helper text** The error message is not the same element as the helper text, it is independent. If a helper text accompanies the text input, it is replaced by the error message. The helper text must not be displayed simultaneously.

<img src="images/quantity_input@error_img.png" alt="quantity_input@error_img" width="433">

## Leading icon

<!-- zh-row -->

Helps indicate the purpose of the input (magnifying glass for search, envelope for email, phone device for phone number). Only use a leading icon if it adds clear functional or contextual value.

<img src="images/quantity_input@leading_icon_img.png" alt="quantity_input@leading_icon_img" width="433">

## Other boolean options

<!-- zh-row -->

**`Suffix`** An element placed after the user's input, often used to display a currency or a unit (kg, %, cm…).

**`Helper text`** Supporting text conveys additional information about the input field, such as how it will be used. It should ideally only take up a single line, though may wrap to multiple lines if required, and be either persistently visible or visible only on focus.

<img src="images/quantity_input@other_boolean_options_img.png" alt="quantity_input@other_boolean_options_img" width="433">

## ⚠️ Label (can it be hidden?)

<!-- zh-row -->

Describes the purpose of the input. Why hide a quantity input label?

In some UI contexts, especially when space is limited or when the input is part of a compact layout (search bars, filters, inline forms), visually hiding the label can help maintain a clean and uncluttered interface.  
However, hiding the label should only be done if:
* The purpose of the input remains clear thanks to a placeholder or contextual icon.
* The label is still accessible to screen readers (using aria-label, aria-labelledby, or visually hidden text).

Hiding a label is a design choice that must balance visual simplicity and clarity of intent, without compromising inclusiveness or form guidance.

<img src="images/quantity_input@label_img.png" alt="quantity_input@label_img" width="433">

## Mandatory field indication

<!-- zh-row -->

**If all fields are mandatory (several fields present):**
1. Display the message "All fields are mandatory." at the top.
2. Do not use an asterisk (*) at the end of each field label, nor the word "mandatory."

**If not all fields are mandatory (and there are several fields present):**
1. Display the message "All fields marked with an * are mandatory." at the top.
2. Use an asterisk (*) at the end of each mandatory field label.  
   **⚠️ Important:**
   * In Figma, the asterisk must be entered manually by designers in the label text. UI rendering of the asterisk: **font-weight-bold** + **color-content-negative (red)**.
   * Technically, for web/iOS/Android, the asterisk is positioned in a dedicated container after the label text. Spacing between label and asterisk: Empty state → 4px / Other states (reduced label) → 3px. If the label is truncated due to a large amount of text, the asterisk must remain visible at the end of the field.
3. Either the technology allows a 'required' attribute to be managed on the fields (usually in Web), in which case any asterisks must be hidden from users using assistive technologies, or the technology does not allow the mandatory nature of the field to be indicated. In this case, the asterisk must be vocalised as well as a 'mandatory' mention. Please refer to the technical documentations for more information.
4. Depending on the use case, an 'optional' label can be added to non-mandatory fields.

**If there is only one field in the form, or if the mandatory nature is obvious (such as login/password), no mention is necessary since the fields are essential to the form's functionality.**

<img src="images/quantity_input@mandatory_field_indication_img.png" alt="quantity_input@mandatory_field_indication_img" width="433">

<img src="images/quantity_input@mandatory_field_indication_img2.png" alt="quantity_input@mandatory_field_indication_img2" width="433">

## truncated input area

<!-- zh-row -->

**When losing focus, the truncation behavior of the input area differs depending on the technical environment. It's important to respect the native behaviors designed to handle truncation:**

* On web, by default (even if the project retains control over this setting), if the text volume exceeds the visible width of the field, the input displays the end of the text (right-aligned) and the beginning of the text becomes invisible (masked on the left). There should be no visual truncation indicator (...). This choice is intentional because, for many fields, showing the end often makes it easier to identify the value (file names, paths, emails).
* On Android, by default (even if the project retains control over this setting), the behavior is the same as on the web.
* On iOS, it is the opposite: the input area truncates the value on the right with a visual truncation indicator (...).

**⚠️ In all cases:** the entire text must remain accessible when the field regains focus:

* Either by refocusing the field, the text becomes horizontally scrollable again (the blinking cursor is visible).
* Or via a tooltip on hover in certain desktop contexts.

<img src="images/quantity_input@truncated_input_area_img.png" alt="quantity_input@truncated_input_area_img" width="433">

## Multiline and responsiveness

<!-- zh-row -->

### Multiline

In its "Empty" state (without a placeholder) and with its "Actions placement=Trailing", the label of this component allows two lines of text editing. However, it is recommended not to exceed one line of text.

Apart from the case described above, this component doesn't allow multi-line text editing (whether for the label, placeholder or input).

As a result, and in order to maintain a consistent and uniform height across multiple components, the presence of an excessive amount of text (in the label, placeholder, or input) will cause the text to be truncated so that only a single line remains visible for each element.

Additionally, allowing multi-line text editing would create confusion with the "Text area" component.

&nbsp;

### Max-width vs full-width

For greater flexibility, this component doesn't have a default max-width. To avoid exceeding a width that would degrade readability and the perception of a compact interactive element, we recommend applying **a max-width of around 320px.**

For mobile or tablet use (or if the component is positioned inside a specific container), it is possible to set this component to use the full available width (of the screen or the container).

Please note that this behavior is not the default rule; it may be preferred if the template allows it (to improve user comfort or for better page structure/hierarchy).

&nbsp;

### User zoom in/out

The behavior of the text during user zoom in/out must follow a fundamental principle: the text must remain readable, accessible, and must never break the structure or lose information.

However, "Text input" components present an exception regarding the loss of textual information following the activation of user zoom in, since text truncation (label, placeholder, input text) is exceptionally allowed and enabled.

* The text must always scale proportionally with user zoom. Text resizing must never be blocked.
* The component's height and width must be flexible, never fixed, in order to automatically adapt its dimensions according to the level of zoom.
* In order to preserve the minimun interactive area during user zoom out, this component have a min-width **of 200px** and a min-height **of 60px**.
* Even if, the component has a max-height or a max-width for resizing control purposes, technically, during user zoom in, these limitations are not fixed but must be scalable in order to adapt to the user's zoom level.
* In its "Leading icon" variant, user zoom in/out doesn't affect the size of the icons; they remain fixed in size (decorative use).
* As the error icon is functional, it must follow the same rules as text.
* The behaviors of the quantity button increase/decrease component during user zoom are available in the button (Layout: icon only) documentation. [Learn more about the behavior of the button component.](https://www.figma.com/design/QtOWrH1m3RHOAkfyy0XFil?node-id=92394-14049)

<img src="images/quantity_input@multiline_and_responsiveness_img.png" alt="quantity_input@multiline_and_responsiveness_img" width="433">

## Rich text

<!-- zh-row -->

### Strong text
* Strong text can be used sparingly to highlight key information within the content. Text is allowed using the corresponding "Strong" token (e.g. Label/Medium/Strong) depending on the selected text style.
* No other text styles or custom font weights should be used.

&nbsp;

### ⚠️ Underline text
* Underlined text must not be applied manually (e.g. in helper text), as it is commonly associated with hyperlinks and may mislead users.

<img src="images/quantity_input@rich_text_img.png" alt="quantity_input@rich_text_img" width="433">

# Specs

## Layout and spacing

<img src="images/quantity_input@specs_layout_spacing.png" alt="quantity_input@specs_layout_spacing" width="864">

## States

<!-- zh-row -->

**`Enabled`** Neutral appearance, whether empty or filled. It allows users to click, focus, and type freely without restrictions.

<img src="images/quantity_input@states_enabled_img.png" alt="quantity_input@states_enabled_img" width="433">

<!-- zh-row -->

**`Hover`** Slight visual contrast or border color change.

<img src="images/quantity_input@states_hover_img.png" alt="quantity_input@states_hover_img" width="433">

<!-- zh-row -->

**`Focus`** The quantity input is focused and ready to receive user input. It visually highlights the field to indicate that it's currently editable and interactive. This state typically appears after a user clicks or taps into the field.

<img src="images/quantity_input@states_focus_img.png" alt="quantity_input@states_focus_img" width="433">

<!-- zh-row -->

**`Loading`** The Loading state indicates that the system is processing or retrieving data related to the quantity input. A progress indicator appears to inform the user that an action is in progress. During this state, the input may be temporarily disabled to prevent further interaction.

<img src="images/quantity_input@states_loading_img.png" alt="quantity_input@states_loading_img" width="433">

<!-- zh-row -->

**`Read only`** Text visible but not editable (often with a muted or different background).

<img src="images/quantity_input@states_read_only_img.png" alt="quantity_input@states_read_only_img" width="433">

<!-- zh-row -->

**`Disabled`** The field is non-interactive and grayed out to indicate it cannot be changed. The helper text is muted.

<img src="images/quantity_input@states_disabled_img.png" alt="quantity_input@states_disabled_img" width="433">

<!-- zh-row -->

**`Skeleton`** Improves the perceived loading time by providing a visual cue of where field will appear once fully loaded. Uses the "Skeleton" component, variant "Security marge=False".

<img src="images/quantity_input@states_skeleton_img.png" alt="quantity_input@states_skeleton_img" width="433">

# Accessibility

Work is in progress to deliver this content.

# Develop

## Developer documentation

| Platform | Developer documentation |
|---|---|
| OUDS Web | Not available yet |
| OUDS Android | Not available yet |
| OUDS iOS | Not available yet |
| OUDS Flutter | Not available yet |

# Changelog

## Availability

| Platform | Resource | Status | Version |
|---|---|---|---|
| Figma | [Quantity input component](https://r.orange.fr/r/S-ouds-design-quantity-input) | Early Access | 1.3.1 |
| OUDS Web (former Boosted) | Not available yet | To do | – |
| OUDS Android - Jetpack Compose | Not available yet | To do | – |
| OUDS iOS - Swift | Not available yet | To do | – |
| OUDS Flutter | Not available yet | To do | – |

## Design changelog

| Date | Number | Notes |
|------|--------|-------|
| May 22, 2026 | 1.3.1 | **Version 2.6 of the design tokens is required for the development of this update.**<br>For "Loading" state:<ul><li>Loading state button was updated<ul><li>Absolute positioning has been removed and replaced with Auto Layout.<ul><li>The container now uses: ouds/button/space/inset/icon-only-default</li></ul></li><li>Inside the container, the Circular Progress Indicator uses: ouds/button/space/inset/progress-indicator-only-default</li></ul></li></ul> |
| Apr 22, 2026 | 1.3.0 | <ul><li>The input text reference changes from a regular weight (font-weight-label-default) to a medium weight (font-weight-label-moderate).</li><li>Removal of the component's max-width to avoid blocking certain layouts and to provide greater flexibility of use. The max-width values remain available in the design documentation.</li><li>Add spacing tokens between the label and the asterisk:<ul><li>control-text-input-space-column-gap-📄_label-asterisk</li><li>control-text-input-space-column-gap-📄_label-small-asterisk</li></ul></li></ul> |
| Apr 8, 2026 | - | • Documentation writing: Rich text |
| Mar 16, 2026 | - | Documentation writing:<ul><li>Rounded corners brand theme availability</li><li>Mandatory field indication</li><li>Truncated input area</li><li>Multiline and responsiveness</li></ul> |
| Jan 21, 2026 | - | • Documentation writing: Rounded corners update |
| Jan 6, 2026 | - | <ul><li>Documentation writing: Definition update</ul> |
| Sep 30, 2025 | 1.2.0 | • For the property "Actions placement", the name of the variant "Right" is replaced by "Trailing" (RTL consideration)<br>• The name of the "Style" variant has been replaced to "Outlined" with true/false variant |
| Jul 29, 2025 | 1.1.0 | • Several design token updates: [Component tokens changelog 1.5.0](https://www.figma.com/design/Co2t6wHMf4GB9NJVGs2Hes/-OUDS-Core-Lib--Design-tokens?m=auto&node-id=9280-2568&t=HLVB4jOd35DWr8Bj-1) |
| Jun 30, 2025 | 1.0.0 | • Component creation |
