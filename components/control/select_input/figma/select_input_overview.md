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

**`False`** A subtle and minimal style (neutral input border)

**`True`** A soft, friendly style, a bit more playful and approachable

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
UI rendering of the asterisk: font-weight-bold + color-content-negative (red).

**If not all fields are mandatory (several fields present):**
1. Display the message "All fields marked with an * are mandatory." at the top.
2. Use an asterisk (*) at the end of each mandatory field label (the word "mandatory" is read aloud instead of the visible asterisk at the end of the label).
UI rendering of the asterisk: font-weight-bold + color-content-negative (red).
3. Use the mention "(optional)" at the end of each optional field label. Note that this rule is not systematic—it remains an option, to be used if needed.

**If there is only one field in the form, or if the mandatory nature is obvious (such as login/password), no mention is necessary since the fields are essential to the form's functionality.**

---
