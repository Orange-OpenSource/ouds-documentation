# TEXT INPUT - Version, Definition & Properties

---

### Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Sep 30, 2025 | 1.3.0 | • The name of the "Style" variant has been replaced to "Outlined" with true/false variant | Hamza Amarir |
| Sep 25, 2025 | 1.2.0 | • Several design token updates: [Component tokens changelog 1.5.0](https://www.figma.com/design/Co2t6wHMf4GB9NJVGs2Hes/-OUDS-Core-Lib--Design-tokens?m=auto&node-id=9280-2568&t=HLVB4jOd35DWr8Bj-1) | Maxime Tonnerre |
| Jul 29, 2025 | 1.1.0 | • Several design token updates: [Component tokens changelog 1.5.0](https://www.figma.com/design/Co2t6wHMf4GB9NJVGs2Hes/-OUDS-Core-Lib--Design-tokens?m=auto&node-id=9280-2568&t=HLVB4jOd35DWr8Bj-1) | Maxime Tonnerre |
| Jun 30, 2025 | 1.0.0 | • Component creation | Maxime Tonnerre |

---

### Definition

A text input is a user interface component that allows users to enter, edit, or select single-line textual data. It's one of the most fundamental form elements used to capture user input such as names, emails, passwords, or search queries.

It provides a visual and interactive affordance for text entry while supporting labels, placeholders, icons, helper messages, and validation feedback.

---

### Properties

| property name | type |
|---------------|------|
| Outlined | 'True' \| 'False' |
| Rounded corner | 'False' \| 'True' |
| Input status | 'Empty' \| 'Empty (Placeholder)' \| 'Filled' |
| State | 'Enabled' \| 'Hover' \| 'Focus' \| 'Loading' \| 'Read only' \| 'Disabled' \| 'Skeleton' |
| Error | 'False' \| 'True' |
| Leading icon | 'False' \| 'True' |
| Trailing action | 'False' \| 'True' |
| ⚠️ Label | boolean |
| ✏️ Label | text |
| ✏️ Placeholder | text |
| ✏️ Input text | text |
| Autocompletion | boolean |
| ✏️ Autocompletion | text |
| Prefix | boolean |
| Suffix | boolean |
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

**Trailing action** Off

**⚠️ Label** On

**Autocompletion** Off

**Prefix** Off

**Suffix** Off

**Helper text** Off

**Helper link** Off

---

### Outlined

**`False`** An input with a subtle background fill and un visible bottom border, creating a softer and more contained look. Best suited for dense layouts or to enhance visibility.

**`True`** A minimalist input with a transparent background and a visible stroke outlining the field.

This style may be interesting for contexts other than form pages:
• When inputs need to feel lightweight and unobtrusive
• In a header (search field)
• In a selection/filtering feature in a product catalog

---

### Rounded corner

**`False`** For a square finish.

**`True`** For a finish with rounded corner.

To be favored in more emotional, immersive contexts or those tied to specific visual identities. For standard or business-oriented journeys, keep the default corners. This evolution addresses the need for flexibility in adapting the design to certain brand contexts.

---

### Input status

**`Empty`** The Empty state indicates that the text input is blank with no content or placeholder, a neutral starting point.

**`Empty (Placeholder)`** The Empty with Placeholder state provides a hint or guidance inside the field to suggest expected input.

**`Filled`** The Filled state shows that the user has entered valid content into the field, replacing any placeholder.

---

### States

**`Enabled`** Neutral appearance, whether empty or filled.

It allows users to click, focus, and type freely without restrictions.

**`Hover`** Slight visual contrast or border color change.

**`Focus`** The text input is focused and ready to receive user input.

It visually highlights the field to indicate that it's currently editable and interactive. This state typically appears after a user clicks or taps into the field.

**`Loading`** The Loading state indicates that the system is processing or retrieving data related to the text input.

A progress indicator appears to inform the user that an action is in progress. During this state, the input may be temporarily disabled to prevent further interaction.

**`Read only`** Text visible but not editable (often with a muted or different background).

**`Disabled`** The field is non-interactive and grayed out to indicate it cannot be changed. The helper text is muted.

**`Skeleton`** Improves the perceived loading time by providing a visual cue of where field will appear once fully loaded.

Uses the "Skeleton" component, variant "Security marge=False".

---

### Error

The Error status indicates that the user input does not meet validation rules or expected formatting. It provides immediate visual feedback, typically through a red border, error icon, and a clear, accessible error message positioned below the input (mandatory).

This state helps users quickly identify and correct mistakes by explaining what went wrong and, when possible, how to fix it.

The input remains editable, encouraging users to revise their input without starting over.

**⚠️ Error message vs helper text / link**

The error message is not the same element as the helper text, it is independent. If a helper text accompanies the text input, it is replaced by the error message. The helper text must not be displayed simultaneously. However, a helper link must not be replaced and should remain positioned below the error message.

---

### Leading icon

Helps indicate the purpose of the input (magnifying glass for search, envelope for email, phone device for phone number). Only use a leading icon if it adds clear functional or contextual value.

---

### Trailing action

Used to provide actions related to the field: clear input, toggle password visibility, open a date picker, etc. Can also indicate status or feedback (error checkmark, loading spinner).

---

### Other boolean options

**Autocompletion** Provides suggested values as the user types. Displays inline text predictions within the input field and/or a dropdown menu of predictive options to speed up input and reduce errors.

**Prefix** A visual or textual element placed before the user's input.

Commonly used to indicate expected formatting like a country code, a unit...

**Suffix** An element placed after the user's input, often used to display a currency or a unit (kg, %, cm...).

**Helper text** Supporting text conveys additional information about the input field, such as how it will be used. It should ideally only take up a single line, though may wrap to multiple lines if required, and be either persistently visible or visible only on focus.

**Helper link** If the helper text is not sufficient (It can also be displayed on its own without helper text), it's possible to offer the user an additional help link (the link can be external or open a modal).

---