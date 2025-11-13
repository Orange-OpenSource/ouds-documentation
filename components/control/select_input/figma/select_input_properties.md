# Select Input - Definition & Properties

---

### Definition

A select input is a form component that allows users to choose one (or sometimes multiple) options from a predefined list. It is typically rendered as a dropdown menu that displays available choices when interacted with, either by click or keyboard navigation.

This component is used when the number of choices is limited and known in advance and when users should select from controlled or standardized values

---

### Properties

| property name | type |
|---------------|------|
| Outlined | 'False' \| 'True' |
| Rounded corner | 'False' \| 'True' |
| Input status | 'Empty' \| 'Filled' |
| State | 'Enabled' \| 'Hover' \| 'Focus' \| 'Expanded' \| 'Loading' \| 'Read only' \| 'Disabled' \| 'Skeleton' |
| Error | 'False' \| 'True' |
| Leading icon | 'False' \| 'True' |
| ⚠️ Label | boolean |
| ✏️ Label | text |
| ✏️ Input text | text |
| Combobox | boolean |
| Autocompletion | boolean |
| ✏️ Autocompletion | text |
| Helper text | boolean |
| ✏️ Helper text | text |
| ✏️ Error empty text | text |
| ✏️ Error filled text | text |
| Helper link | boolean |

---

### Initial settings

**Outlined** Off

**Rounded corner** Off

**Input status** Empty

**State** Enabled

**Error** Off

**Leading icon** Off

**⚠️ Label** On

**Combobox** Off

**Autocompletion** Off

**Helper text** Off

**Helper link** Off

---

### Outlined

**`False`** An input with a subtle background fill and un visible bottom border.

**`True`** A minimalist input with a transparent background and visible stroke.

This style may be interesting for contexts other than form pages:
• When inputs need to feel lightweight and unobtrusive
• In a header (search field)
• In a selection/filtering feature in a product catalog

---

### Rounded corner

**`False`** A subtle and minimal style (neutral input border)

**`True`** A soft, friendly style, a bit more playful and approachable

---

### Input status

**`Empty`** By default, a select input is open with label, no input text, dropdown closed, and no helper text displayed below.

**`Filled`** The input text is the option selected by the user from the dropdown menu.

---

### State

**`Enabled`** Default state: the input is ready for interaction.

**`Hover`** When the user hovers over the input field (without the dropdown being opened), the appearance of the element changes slightly to indicate interactivity.

**`Focus`** When the user clicks or tabs into the input field (without opening the dropdown), the field gains focus and applies specific visual styles.

**`Expanded`** When the user opens the dropdown menu to view options.

**`Loading`** Indicates that options are being loaded asynchronously.

**`Read only`** When the select input is in a read-only state, its value is visible, but the user cannot interact with it or change the selection.

**`Disabled`** The input cannot be interacted with (non clickable, can't receive focus, no hover effect) and its appearance indicates unavailability.

**`Skeleton`** Displays a placeholder UI while content is loading.

---

### Error

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

### Leading icon

Conveys the nature or purpose of the select input field at a glance.

---

### Helper text

Information displayed below the select input field to provide guidance or context to the user (explanatory text, tips, additional details, guidance on the expected format).

**Examples of helper text:**
• Indicate the maximum character limit for a text field: "You have 180 characters remaining."
• Offer tips on format requirements: "Your password must contain at least 8 characters, including a number and a special character."

**Helper text on error:**
• When in error state, helper text becomes error text.

Helper text is used to provide additional information at the right time, without overcrowding the interface.

Helper text is different from placeholder text:
• Helper text remains visible before, during, and after text entry.
• Placeholder text disappears when typing.

---
