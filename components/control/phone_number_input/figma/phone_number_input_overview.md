## Definition

A phone number input is a form field specifically designed to capture and validate telephone numbers, often in international format. It typically integrates a country selector, allowing users to choose their country and automatically apply the corresponding dialing code (such as +33 for France).

The dialing code is usually displayed as a non-editable prefix within the field to guide the user and ensure consistent formatting. The component include real-time formatting or masking to improve readability during input, and validation rules tailored to the number structure of the selected country.

---

## Outlined

**`False`** An input with a subtle background fill and un visible bottom border, creating a softer and more contained look. Best suited for dense layouts or to enhance visibility.

**`True`** A minimalist input with a transparent background and a visible stroke outlining the field.

This style may be interesting for contexts other than form pages:
• When inputs need to feel lightweight and unobtrusive
• In a header (search field)
• In a selection/filtering feature in a product catalog

---

## Rounded corner

Even though in Figma this rendering option is available and editable from the properties of each input component, the configuration of this rendering option is actually transversal across the entire product/service in which the component is used. It is therefore impossible to have one input component set to Rounded corner=True and another set to Rounded corner=False within the same product/service.

**`False`** The square rendering corresponds to Orange's historical style. It conveys the brand's sense of seriousness, robustness and utility-driven. It remains the default style for our digital interface components.

**`True`** The rounded rendering offers flexibility without sacrificing the attribution to the brand. It helps anchoring the service in a reality where the visual codes of the mobile area tends to rub off on all interfaces. Use rounded corners for a softer, more approachable, friendly and tactile feel.

This option is technically not available for all brand themes. Here's the list of rounded corners availability by brand theme:

| Brand theme | Status |
|---|---|
| Orange | ✓ Available |
| Orange Compact | ✓ Available |
| Sosh | ⚠️ Unavailable |
| Wireframe | ⚠️ Unavailable |

---

## Input status

**`Empty`** The field is empty. The placeholder text is not visible: the label is displayed instead and remains visible when the user starts typing.

**`Empty (Placeholder)`** The field is empty. The placeholder text is displayed in lieu of the label as an additional way to provide a contextual hint.

**`Filled`** The field has been filled out by the user.

---

## States

**`Enabled`** The default state when the user can interact with the text input. The field is ready to accept input when the user clicks or taps on it.

**`Hover`** Triggered when the user hovers the cursor over the input. This state provides visual feedback, signaling that the field can be interacted with.

**`Focus`** Activated when the user clicks or taps into the input, indicating that the field is currently selected and ready for input. This state is critical for accessibility, as it shows exactly where the user's focus is within the form.

**`Loading`** The component displays a loading indicator to inform the user that a process is underway, such as validating the input. The input remains disabled during this time.

**`Read only`** The input contains data but is not editable. This state is useful for displaying pre-filled data that the user shouldn't alter, like information pulled from a database or data confirmed in a previous step.

**`Disabled`** The input is inactive and cannot be interacted with. This state indicates that the field is currently unavailable, such as in cases where a required previous action has not been completed.

**`Skeleton`** A placeholder state to indicate that content is loading or being fetched. Useful in maintaining the layout structure while the actual data is being retrieved, providing a smooth user experience during initial page loads.

---

## Error

**`False`** The input is in a standard state, with no validation issues. It is ready for users to fill out without errors.

**`True`** The input has detected a validation error. An error message provides guidance to the user about what needs to be corrected. Error handling can be done either when the user navigates away from the field (on blur) or upon submission (when the user submits the form).

---

## Leading icon

**`Leading icon`** When enabled, it is possible to display an icon on the left of the input text.

---

## Country selector

**`Country selector`** When enabled, it is possible to display a country selector with its flag. Country selector is displayed as a secondary button with only an icon (flag) and a chevron.

---

## ⚠️ Label (can it be hidden?)

Describes the purpose of the input. Why hide a phone number input label?

In some UI contexts, especially when space is limited or when the input is part of a compact layout (search bars, filters, inline forms), visually hiding the label can help maintain a clean and uncluttered interface.

However, hiding the label should only be done if:
• The purpose of the input remains clear thanks to a placeholder or contextual icon.
• The label is still accessible to screen readers (using aria-label, aria-labelledby, or visually hidden text).

Hiding a label is a design choice that must balance visual simplicity and clarity of intent, without compromising inclusiveness or form guidance.

---

## Other boolean options

**Dial code** When enabled, it is possible to display the country dial code value. The dial code is read-only and cannot be edited directly by the user.

**Helper text** When enabled, a helper text appears below the input field to provide additional context or tips on how to fill out the field. Useful for offering suggestions or clarifying expected input formats (e.g., "Please enter a phone number in international format").

---

## ⚠️ Mandatory field indication

**If all fields are mandatory (several fields present):**
1. Display the message "All fields are mandatory." at the top.
2. Do not use an asterisk (*) at the end of each field label, nor the word "mandatory."
   UI rendering of the asterisk: font-weight-bold + color-content-negative (red).

**If not all fields are mandatory (several fields present):**
1. Display the message "All fields marked with an * are mandatory." at the top.
2. Use an asterisk (*) at the end of each mandatory field label (the word "mandatory" is read aloud instead of the visible asterisk at the end of the label).
   UI rendering of the asterisk: font-weight-bold + color-content-negative (red).
3. Use the mention "(optional)" at the end of each optional field label. Note that this rule is not systematic—it remains an option, to be used if needed.

**If there is only one field in the form, or if the mandatory nature is obvious (such as login/password), no mention is necessary since the fields are essential to the form's functionality.**

---

## ⚠️ Truncated input area

**When losing focus, the truncation behavior of the input area differs depending on the technical environment. It's important to respect the native behaviors designed to handle truncation:**

* On web, by default (even if the project retains control over this setting), if the text volume exceeds the visible width of the field, the input displays the end of the text (right-aligned) and the beginning of the text becomes invisible (masked on the left). There should be no visual truncation indicator (...). This choice is intentional because, for many fields, showing the end often makes it easier to identify the value (file names, paths, emails).
* On Android, by default (even if the project retains control over this setting), the behavior is the same as on the web.
* On iOS, it is the opposite: the input area truncates the value on the right with a visual truncation indicator (...).

**⚠️ In all cases:** the entire text must remain accessible when the field regains focus:

* Either by refocusing the field, the text becomes horizontally scrollable again (the blinking cursor is visible).
* Or via a tooltip on hover in certain desktop contexts.

---

## Multiline and responsiveness

**Multiline**

In its "Empty" state (without a placeholder), the label of this component allows two lines of text editing. However, it is recommended not to exceed one line of text.

Apart from the case described above, this component doesn't allow multi-line text editing (whether for the label, placeholder or input).

As a result, and in order to maintain a consistent and uniform height across multiple components, the presence of an excessive amount of text (in the label, placeholder, or input) will cause the text to be truncated so that only a single line remains visible for each element.

Additionally, allowing multi-line text editing would create confusion with the "Text area" component.

**Max-width vs full-width**

For greater flexibility, this component doesn't have a default max-width. To avoid exceeding a width that would degrade readability and the perception of a compact interactive element, we recommend applying **a max-width of around 480px.**

For mobile or tablet use (or if the component is positioned inside a specific container), it is possible to set this component to use the full available width (of the screen or the container).

Please note that this behavior is not the default rule; it may be preferred if the template allows it (to improve user comfort or for better page structure/hierarchy).

**User zoom in/out**

The behavior of the text during user zoom in/out must follow a fundamental principle: the text must remain readable, accessible, and must never break the structure or lose information.

However, "Text input" components present an exception regarding the loss of textual information following the activation of user zoom, since text truncation (label, placeholder, input text) is exceptionally allowed and enabled.

* The text must always scale proportionally with user zoom. Text resizing must never be blocked.
* The component's height and width must be flexible, never fixed, in order to automatically adapt its dimensions according to the level of zoom.
* In order to preserve the minimun interactive area during user zoom out, this component have a min-width **of 240px** and a min-height **of 60px**.
* Even if, the component has a max-height or a max-width for resizing control purposes, technically, during user zoom in, these limitations are not fixed but must be scalable in order to adapt to the user's zoom level.
* In its "Leading icon" variant, user zoom in/out doesn't affect the size of the icons; they remain fixed in size (decorative use).
* As the country selector and error icon are functional, they must follow the same rules as text.

---

## Rich text

* **Strong text**
  * Strong text can be used sparingly to highlight key information within the content. Text is allowed using the corresponding "Strong" token (e.g. Label/Medium/Strong and Label/Large/Strong) depending on the selected text style.
  * No other text styles or custom font weights should be used.

* **⚠️ Underline text**
  * Underlined text must not be applied manually (e.g. in helper text), as it is commonly associated with hyperlinks and may mislead users.

---
