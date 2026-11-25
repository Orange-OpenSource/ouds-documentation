---
id: password-input
category: Control
family: None
---

# Password input

A password input is a UI element designed to securely and confidentially capture a user’s password.

# Guideline

<img src="images/hero_image_password_input.png" alt="hero_image_password_input" width="864">

## When to use

✅ To capture confidential credentials that require character masking

✅ In authentication, registration, and password reset flows

✅ For data that should not be visible by default

## Anatomy

<img src="images/password_input@anatomy_img.png" alt="password_input@anatomy_img" width="864">

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Leading icon | Provides a visual cue about the field type (password). | Yes |
| 2 | Label | Tells users what information to enter. | Yes |
| 3 | Input container | Holds and aligns all parts of the field (label, value, icons, etc.). | No |
| 4 | Trailing action | Lets users toggle between hiding and showing the password. | No |
| 5 | Bottom border | The visible bottom border for the non-outlined style. | No |
| 6 | Helper text | Supplementary text displayed below the input field providing guidance or requirements. | Yes |
| 7 | Label | Moves above the input when focused or filled, so the field stays identifiable. | Yes |
| 8 | Prefix | Shows a static prefix before the value to provide context or format requirements (e.g., “DEV-”). | Yes |
| 9 | Input text | Shows the entered password as dots when hidden, or as text when revealed. | No |
| 10 | Text cursor | Indicates where the next character will be inserted while typing. | No |
| 11 | Loading indicator | Shows progress while validation or authentication is in progress. | Yes |
| 12 | Outlined container | Alternative visual style using a full border. | No |
| 13 | Error text | Explains what’s wrong and how to fix it when validation fails. | Yes |
| 14 | Error icon | Highlights the field’s error state to improve visibility and feedback. | Yes |

## Definition

A password input is a UI element designed to securely and confidentially capture a user’s password.

The password input feature enhances privacy by replacing characters with dots as they are typed. It also includes usability features like the option to show or hide the password and helper text to assist with password creation.

## Outlined

<!-- zh-row -->

**`False`** An input with a subtle background fill and un visible bottom border, creating a softer and more contained look. Best suited for dense layouts or to enhance visibility.

**`True`** A minimalist input with a transparent background and a visible stroke outlining the field. This style may be interesting for contexts other than form pages:
* When inputs need to feel lightweight and unobtrusive
* In a header (search field)
* In a selection/filtering feature in a product catalog

<img src="images/password_input@outlined_img.png" alt="password_input@outlined_img" width="433">

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

<img src="images/password_input@rounded_corner_img.png" alt="password_input@rounded_corner_img" width="433">

## Input status

<!-- zh-row -->

**`Empty`** The Empty state indicates that the password input is blank with no content or placeholder, a neutral starting point.

**`Empty (Placeholder)`** The Empty with Placeholder state provides a hint or guidance inside the field to suggest expected input.

**`Filled`** The Filled state shows that the user has entered valid content into the field, replacing any placeholder.

<img src="images/password_input@input_status_img.png" alt="password_input@input_status_img" width="433">

## Error

<!-- zh-row -->

The Error status indicates that the user input does not meet validation rules or expected formatting. It provides immediate visual feedback, typically through a red border, error icon, and a clear, accessible error message positioned below the input (mandatory).

This state helps users quickly identify and correct mistakes by explaining what went wrong and, when possible, how to fix it. The input remains editable, encouraging users to revise their input without starting over.

**Error message vs helper text** The error message is not the same element as the helper text, it is independent. If a helper text accompanies the text input, it is replaced by the error message. The helper text must not be displayed simultaneously.

<img src="images/password_input@error_img.png" alt="password_input@error_img" width="433">

**Do:** Write error messages that specifically explain what went wrong and provide actionable guidance on how to fix it

<img src="images/password_input@error_do_img.png" alt="password_input@error_do_img" width="416">

**Don't:** Use generic error messages like "Invalid input" that leave users guessing about the actual problem

<img src="images/password_input@error_dont_img.png" alt="password_input@error_dont_img" width="416">

## Leading icon

<!-- zh-row -->

Helps indicate the purpose of the input. Only use a leading icon if it adds clear functional or contextual value.

<img src="images/password_input@leading_icon_img.png" alt="password_input@leading_icon_img" width="433">

**Do:** Use universally recognized icons like a lock or key symbol that clearly communicate the password field's purpose

<img src="images/password_input@leading_icon_do_img.png" alt="password_input@leading_icon_do_img" width="416">

**Don't:** Add decorative icons that don't contribute meaningful context or could confuse users about the field's function

<img src="images/password_input@leading_icon_dont_img.png" alt="password_input@leading_icon_dont_img" width="416">

## Label

<!-- zh-row -->

Describes the purpose of the input. Why hide a password input label?

In some UI contexts, especially when space is limited or when the input is part of a compact layout (search bars, filters, inline forms), visually hiding the label can help maintain a clean and uncluttered interface. However, hiding the label should only be done if:
* The purpose of the input remains clear thanks to a placeholder or contextual icon.
* The label is still accessible to screen readers (using aria-label, aria-labelledby, or visually hidden text).

Hiding a label is a design choice that must balance visual simplicity and clarity of intent, without compromising inclusiveness or form guidance.

<img src="images/password_input@label_img.png" alt="password_input@label_img" width="433">

**Do:** Write labels that clearly describe the expected input, such as "Password" or "Current password" for clarity

<img src="images/password_input@label_do_img.png" alt="password_input@label_do_img" width="416">

**Don't:** Use vague labels like "Enter here" or overly technical labels that don't help users understand what's required

<img src="images/password_input@label_dont_img.png" alt="password_input@label_dont_img" width="416">

## Other boolean options

<!-- zh-row -->

**`Prefix`** - for Filled and Empty (Placeholder) Input states only A visual or textual element placed before the user's input. A prefix is not common and is discouraged in a Password Input component. Here are illustrative examples of very specific cases where:
* "corp-" Company password enforcing a prefix
* "temp-" Temporary password during a testing phase
*  "dev-" For test accounts
* "eu-, us-, prod-, stage-" To encode a target environment
* "test@" Used in the context of automated or predictable tests
* "admin-" Pattern used to define an admin password

**`Helper text`** Supporting text conveys additional information about the input field, such as how it will be used. It should ideally only take up a single line, though may wrap to multiple lines if required, and be either persistently visible or visible only on focus.

<img src="images/password_input@other_boolean_options_img.png" alt="password_input@other_boolean_options_img" width="433">

**Do:** Use helper text to communicate password requirements upfront (e.g., minimum length, required character types)

**Don't:** Hide critical password requirements in tooltips or only reveal them after validation failures

**Do:** Only reserve prefixes for very specific professional usage

<img src="images/password_input@other_boolean_options_do_img.png" alt="password_input@other_boolean_options_do_img" width="416">

**Don't:** Use prefixes in consumer-facing password fields as they add unnecessary complexity and confusion

<img src="images/password_input@other_boolean_options_dont_img.png" alt="password_input@other_boolean_options_dont_img" width="416">

## Mandatory field indication

<!-- zh-row -->

**If all fields are mandatory (several fields present):**
1. Display the message "All fields are mandatory." at the top.
2. Do not use an asterisk (*) at the end of each field label, nor the word "mandatory."

**If not all fields are mandatory (and there are several fields present):**
1. Display the message "All fields marked with an * are mandatory." at the top.
2. Use an asterisk (*) at the end of each mandatory field label.  
**⚠️ Important:**
* In Figma, the asterisk must be entered manually by designers in the label text.  
UI rendering of the asterisk: **font-weight-bold + color-content-negative (red)**.
* Technically, for web/iOS/Android, the asterisk is positioned in a dedicated container after the label text.  
Spacing between label and asterisk:  
Empty state → 4px  
Other states (reduced label) → 3px  
If the label is truncated due to a large amount of text, the asterisk must remain visible at the end of the field.
3. Either the technology allows a 'required' attribute to be managed on the fields (usually in Web), in which case any asterisks must be hidden from users using assistive technologies,  
Or the technology does not allow the mandatory nature of the field to be indicated. In this case, the asterisk must be vocalised as well as a 'mandatory' mention.  
Please refer to the technical documentations for more information.
4. Depending on the use case, an 'optional' label can be added to non-mandatory fields.

If there is only one field in the form, or if the mandatory nature is obvious (such as login/password), no mention is necessary since the fields are essential to the form's functionality.

<img src="images/password_input@mandatory_field_indication_img.png" alt="password_input@mandatory_field_indication_img" width="433">

<img src="images/password_input@mandatory_field_indication_img2.png" alt="password_input@mandatory_field_indication_img2" width="433">

## Truncated input area

<!-- zh-row -->

When losing focus, the truncation behavior of the input area differs depending on the technical environment. It's important to respect the native behaviors designed to handle truncation:

* On web, by default (even if the project retains control over this setting), if the text volume exceeds the visible width of the field, the input displays the end of the text (right-aligned) and the beginning of the text becomes invisible (masked on the left).  
There should be no visual truncation indicator (...).  
This choice is intentional because, for many fields, showing the end often makes it easier to identify the value (file names, paths, emails).
* On Android, by default (even if the project retains control over this setting), the behavior is the same as on the web.
* On iOS, it is the opposite: the input area truncates the value on the right with a visual truncation indicator (...).

**⚠️ In all cases:** the entire text must remain accessible when the field regains focus:
* Either by refocusing the field, the text becomes horizontally scrollable again (the blinking cursor is visible).
* Or via a tooltip on hover in certain desktop contexts.

<img src="images/password_input@truncated_input_area_img.png" alt="password_input@truncated_input_area_img" width="433">

## Multiline and responsiveness

<!-- zh-row -->

### Multiline
In its "Empty" state (without a placeholder), the label of this component allows two lines of text editing. However, it is recommended not to exceed one line of text.  
Apart from the case described above, this component doesn't allow multi-line text editing (whether for the label, placeholder or input).  
As a result, and in order to maintain a consistent and uniform height across multiple components, the presence of an excessive amount of text (in the label, placeholder, or input) will cause the text to be truncated so that only a single line remains visible for each element.  
Additionally, allowing multi-line text editing would create confusion with the "Text area" component.

&nbsp;

### Max-width vs full-width
For greater flexibility, this component doesn't have a default max-width. To avoid exceeding a width that would degrade readability and the perception of a compact interactive element, we recommend applying **a max-width of around 480px.**  
For mobile or tablet use (or if the component is positioned inside a specific container), it is possible to set this component to use the full available width (of the screen or the container).  
Please note that this behavior is not the default rule; it may be preferred if the template allows it (to improve user comfort or for better page structure/hierarchy).

&nbsp;

### User zoom in/out
The behavior of the text during user zoom in/out must follow a fundamental principle: the text must remain readable, accessible, and must never break the structure or lose information.  
However, "Text input" components present an exception regarding the loss of textual information following the activation of user zoom, since text truncation (label, placeholder, input text) is exceptionally allowed and enabled.
* The text must always scale proportionally with user zoom. Text resizing must never be blocked.
* The component's height and width must be flexible, never fixed, in order to automatically adapt its dimensions according to the level of zoom.
* In order to preserve the minimun interactive area during user zoom out, this component have a min-width **of 240px** and a min-height **of 60px**.
* Even if, the component has a max-height or a max-width for resizing control purposes, technically, during user zoom in, these limitations are not fixed but must be scalable in order to adapt to the user's zoom level.
* In its "Leading icon" variant, user zoom in/out doesn't affect the size of the icons; they remain fixed in size (decorative use).
* As the error icon is functional, it must follow the same rules as text.
* The behaviors of the button (layout: icon only) component during user zoom are available in the corresponding documentation. [Learn more about the behavior of the button component.](https://www.figma.com/design/QtOWrH1m3RHOAkfyy0XFil?node-id=92394-14049)

<img src="images/password_input@multiline_and_responsiveness_img.png" alt="password_input@multiline_and_responsiveness_img" width="433">

## Rich text

<!-- zh-row -->

### Strong text
* Strong text can be used sparingly to highlight key information within the content. Text is allowed using the corresponding "Strong" token (e.g. Label/Medium/Strong and Label/Large/Strong) depending on the selected text style.
* No other text styles or custom font weights should be used.

&nbsp;

### ⚠️ Underline text
* Underlined text must not be applied manually (e.g. in helper text), as it is commonly associated with hyperlinks and may mislead users.

<img src="images/password_input@rich_text_img.png" alt="password_input@rich_text_img" width="433">

# Specs

## Layout and spacing

<img src="images/password_input@spec_layout_spacing.png" alt="password_input@spec_layout_spacing" width="864">

## States

<!-- zh-row -->

**`Enabled`** Neutral appearance, whether empty or filled. It allows users to click, focus, and type freely without restrictions.

**`Hover`** Slight visual contrast or border color change.

**`Focus`** The password input is focused and ready to receive user input. It visually highlights the field to indicate that it's currently editable and interactive. This state typically appears after a user clicks or taps into the field.

**`Loading`** The Loading state indicates that the system is processing or retrieving data related to the password input. A progress indicator appears to inform the user that an action is in progress. During this state, the input may be temporarily disabled to prevent further interaction.

**`Read only`** Text visible but not editable (often with a muted or different background).

**`Disabled`** The field is non-interactive and grayed out to indicate it cannot be changed. The helper text is muted.

**`Skeleton`** Improves the perceived loading time by providing a visual cue of where field will appear once fully loaded. Uses the "Skeleton" component, variant "Security marge=False".

<img src="images/password_input@states_img.png" alt="password_input@states_img" width="433">

# Accessibility

Work is in progress to deliver this content.

# Develop

## OUDS-Web example

[Components/PasswordInput › Password Input 0](https://web.unified-design-system.orange.com/storybook/?path=/story/components-passwordinput--password-input-0)

## Developer documentation

| Platform | Developer documentation |
|---|---|
| OUDS Web | [S-ouds-web-password-input](https://r.orange.fr/r/S-ouds-web-password-input) |
| OUDS Android | [S-ouds-android-password-input](https://r.orange.fr/r/S-ouds-android-password-input) |
| OUDS iOS | [S-ouds-ios-password-input](https://r.orange.fr/r/S-ouds-ios-password-input) |
| OUDS Flutter | [S-ouds-flutter-password-input](https://r.orange.fr/r/S-ouds-flutter-password-input) |

# Changelog

## Availability

| Platform | Resource | Status | Version |
|---|---|---|---|
| Figma | [Password input component](https://r.orange.fr/r/S-ouds-design-password-input) | Live | 1.3.1 |
| OUDS Web (former Boosted) | [Web dev documentation](https://r.orange.fr/r/S-ouds-web-password-input) | Live | 1.3.0 |
| OUDS Android - Jetpack Compose | [Android dev documentation](https://r.orange.fr/r/S-ouds-android-password-input) | Live | 1.3.1 |
| OUDS iOS - Swift | [iOS dev documentation](https://r.orange.fr/r/S-ouds-ios-password-input) | Live | 1.3.1 |
| OUDS Flutter | [Flutter dev documentation](https://r.orange.fr/r/S-ouds-flutter-password-input) | Live | 1.3.1 |

## Design changelog

| Date | Number | Notes |
|------|--------|-------|
| May 22, 2026 | 1.3.1 | <ul><li>Version 2.6 of the design tokens is required for the development of this update.<li>For "Loading" state<ul><li>Loading state button was updated<ul><li>Absolute positioning has been removed and replaced with Auto Layout.<ul><li>The container now uses: ouds/button/space/inset/icon-only-default</ul><li>Inside the container, the Circular Progress Indicator uses: ouds/button/space/inset/progress-indicator-only-default</ul></ul></ul> |
| Apr 22, 2026 | 1.3.0 | <ul><li>The input text reference changes from a regular weight (font-weight-label-default) to a medium weight (font-weight-label-moderate).<li>Removal of the component's max-width to avoid blocking certain layouts and to provide greater flexibility of use. The max-width values remain available in the design documentation.<li>Add spacing tokens between the label and the asterisk:<ul><li>control-text-input-space-column-gap-📄_label-asterisk<li>control-text-input-space-column-gap-📄_label-small-asterisk</ul></ul> |
| Apr 8, 2026 | - | <ul><li>Documentation writing: Rich text</ul> |
| Mar 16, 2026 | - | <ul><li>Documentation writing:<ul><li>Rounded corners brand theme availability<li>Mandatory field indication<li>Truncated input area<li>Multiline and responsiveness</ul></ul> |
| Jan 21, 2026 | - | • Documentation writing: Rounded corners update | Cyriaque Billard |
| Jan 6, 2026 | - | <ul><li>Documentation writing: Definition update</ul> |
| Sep 30, 2025 | 1.2.0 | • The name of the "Style" variant has been replaced to "Outlined" with true/false variant |
| Jul 29, 2025 | 1.1.0 | • Several design token updates: [Component tokens changelog 1.5.0](https://www.figma.com/design/Co2t6wHMf4GB9NJVGs2Hes/-OUDS-Core-Lib--Design-tokens?m=auto&node-id=9280-2568&t=HLVB4jOd35DWr8Bj-1) |
| Jun 30, 2025 | 1.0.0 | • Component creation |
