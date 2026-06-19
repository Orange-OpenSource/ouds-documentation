## Definition

A select input is a form component that allows users to choose one (or sometimes multiple) options from a predefined list. It is typically rendered as a dropdown menu that displays available choices when interacted with, either by click or keyboard navigation.

This component is used when the number of choices is limited and known in advance and when users should select from controlled or standardized values

---

## Outlined

**`False`** An input with a subtle background fill and un visible bottom border.

**`True`** A minimalist input with a transparent background and visible stroke.

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

**`Empty`** By default, a select input is open with label, no input text, dropdown closed, and no helper text displayed below.

**`Filled`** The input text is the option selected by the user from the dropdown menu.

---

## States

**`Enabled`** Default state: the input is ready for interaction.

**`Hover`** When the user hovers over the input field (without the dropdown being opened), the appearance of the element changes slightly to indicate interactivity.

**`Focus`** When the user clicks or tabs into the input field (without opening the dropdown), the field gains focus and applies specific visual styles.

**`Expanded`** When the user opens the dropdown menu to view options.

**`Loading`** Indicates that options are being loaded asynchronously.

**`Read only`** When the select input is in a read-only state, its value is visible, but the user cannot interact with it or change the selection.

**`Disabled`** The input cannot be interacted with (non clickable, can't receive focus, no hover effect) and its appearance indicates unavailability.

**`Skeleton`** Displays a placeholder UI while content is loading.

---

## Error

An error is used to provide real-time feedback when the select input is in an invalid state:

**Examples of invalid states:**
• Required field left empty
• Incorrect value format (invalid email, phone number, postal code)
• Value that does not meet the established criteria (password not secure enough, text too short or too long)

**Accessibility for error indication:**
• Color alone is not sufficient: WCAG requires that color not be the only means of conveying information. Therefore, an icon and explicit text must accompany the error color.
• Assistive technologies need contextual error messages: when a user submits a form or leaves a field, screen readers need to receive clear textual information about the error. Use the aria-describedby attribute to associate error messages with the corresponding select input element.
• Error text is not just an ornament: WCAG guidelines require that error messages be sufficiently precise and descriptive.

**`False`** The select input is in its neutral or valid state.

**`True`** The user sees an error message detailing the nature of the problem, and the component is visually marked (e.g., with a specific color or icon) to draw attention to the error.

---

## Leading icon

Conveys the nature or purpose of the select input field at a glance.

---

## ⚠️ Label

Describes the purpose of the input. Why hide a select input label?
In some UI contexts, especially when space is limited or when the input is part of a compact layout (filters, inline forms), visually hiding the label can help maintain a clean and uncluttered interface.
However, hiding the label should only be done if:
• The purpose of the input remains clear thanks to a contextual icon.
• The label is still accessible to screen readers (using aria-label, aria-labelledby, or visually hidden text).

Hiding a label is a design choice that must balance visual simplicity and clarity of intent, without compromising inclusiveness or form guidance.

---

## Other boolean options

**`Helper text`** Supporting text conveys additional information about the input field, such as how it will be used. It should ideally only take up a single line, though may wrap to multiple lines if required, and be either persistently visible or visible only on focus.

**`Helper link`** If the helper text is not sufficient (It can also be displayed on its own without helper text), it's possible to offer the user an additional help link (the link can be external or open a modal).

---

## ⚠️ Mandatory field indication

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

---

## ⚠️ Truncated input area

**When losing focus, the truncation behavior of the input area differs depending on the technical environment. It's important to respect the native behaviors designed to handle truncation:**

For this component, if the text volume exceeds the visible width of the field, the input area truncates the value on the right with a visual truncation indicator (...).

**⚠️ In all cases:** the entire text must remain accessible when the field regains focus:

* Either by opening the dropdown (either by clicking on it or using the down arrow) in which the item is selected and thus seeing the text in its entirety.
* Or via a tooltip on hover in certain desktop contexts.

---

## Multiline and responsiveness

**Multiline**

In its "Empty" state, the label of this component allows two lines of text editing. However, it is recommended not to exceed one line of text.

Apart from the case described above, this component doesn't allow multi-line text editing (whether for the label or input).

As a result, and in order to maintain a consistent and uniform height across multiple components, the presence of an excessive amount of text (in the label or input) will cause the text to be truncated so that only a single line remains visible for each element.

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
* In order to preserve the minimun interactive area during user zoom out, this component have a min-width **of 96px** and a min-height **of 60px**.
* Even if, the component has a max-height or a max-width for resizing control purposes, technically, during user zoom in, these limitations are not fixed but must be scalable in order to adapt to the user's zoom level.
* In its "Leading icon" variant, user zoom in/out doesn't affect the size of the icons; they remain fixed in size (decorative use).
* As the chevron and error icon are functional, they must follow the same rules as text.

---

## Rich text

* **Strong text**
  * Strong text can be used sparingly to highlight key information within the content. Text is allowed using the corresponding "Strong" token (e.g. Label/Medium/Strong) depending on the selected text style.
  * No other text styles or custom font weights should be used.

* **⚠️ Underline text and Hyperlinks**
  * Underlined text must not be applied manually (e.g. in helper text), as it is commonly associated with hyperlinks and may mislead users.
  * If a link is required, the dedicated helper link component must be used (e.g. **Compare plans**).

---
