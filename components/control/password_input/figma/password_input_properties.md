# Password Input - Definition & Properties

---

### Definition

A password input is a form field specifically designed to securely capture a user's confidential password. It masks the characters as they are typed, typically replacing them with dots, in order to protect the input from being read by others nearby.

While the primary goal is to enhance privacy and security, the field may also include usability features such as a "show/hide password" toggle and helper text to guide password creation.

---

### Properties

| property name | type |
|---------------|------|
| Outlined | 'False' \| 'True' |
| Rounded corner | 'False' \| 'True' |
| Input status | 'Empty' \| 'Empty (Placeholder)' \| 'Filled' |
| State | 'Enabled' \| 'Hover' \| 'Focus' \| 'Loading' \| 'Read only' \| 'Disabled' \| 'Skeleton' |
| Error | 'False' \| 'True' |
| Leading icon | 'False' \| 'True' |
| Hidden password | 'True' \| 'False' |
| ⚠️ Label | boolean |
| ✏️ Label | text |
| ✏️ Placeholder | text |
| Prefix | boolean |
| ✏️ Prefix | text |
| ✏️ Input text | text |
| ✏️ Hidden input text | text |
| Helper text | boolean |
| ✏️ Helper text | text |
| ✏️ Error empty text | text |
| ✏️ Error filled text | text |

---

### Initial settings

**Outlined** Off

**Rounded corner** Off

**Input status** Empty

**State** Enabled

**Error** Off

**Leading icon** Off

**Hidden password** On

**⚠️ Label** On

**Prefix** Off

**Helper text** Off

---

### Outlined

**`False`** An input with a subtle background fill and un visible bottom border, creating a softer and more contained look. Best suited for dense layouts or to enhance visibility.

**`True`** A minimalist input with a transparent background and a visible stroke outlining the field. This style may be interesting for contexts other than form pages:
• When inputs need to feel lightweight and unobtrusive
• In a header (search field)
• In a selection/filtering feature in a product catalog

---

### Rounded corner

**`False`** For a square finish.

**`True`** For a finish with rounded corner. To be favored in more emotional, immersive contexts or those tied to specific visual identities. For standard or business-oriented journeys, keep the default corners. This evolution addresses the need for flexibility in adapting the design to certain brand contexts.

---

### Input status

**`Empty`** The Empty state indicates that the password input is blank with no content or placeholder, a neutral starting point.

**`Empty (Placeholder)`** The Empty with Placeholder state provides a hint or guidance inside the field to suggest expected input.

**`Filled`** The Filled state shows that the user has entered valid content into the field, replacing any placeholder.

---

### State

**`Enabled`** Neutral appearance, whether empty or filled. It allows users to click, focus, and type freely without restrictions.

**`Hover`** Slight visual contrast or border color change.

**`Focus`** The password input is focused and ready to receive user input. It visually highlights the field to indicate that it's currently editable and interactive. This state typically appears after a user clicks or taps into the field.

**`Loading`** The Loading state indicates that the system is processing or retrieving data related to the password input. A progress indicator appears to inform the user that an action is in progress. During this state, the input may be temporarily disabled to prevent further interaction.

**`Read only`** Text visible but not editable (often with a muted or different background).

**`Disabled`** The field is non-interactive and grayed out to indicate it cannot be changed. The helper text is muted.

**`Skeleton`** Improves the perceived loading time by providing a visual cue of where field will appear once fully loaded. Uses the "Skeleton" component, variant "Security marge=False".

---

### Error

The Error status indicates that the user input does not meet validation rules or expected formatting. It provides immediate visual feedback, typically through a red border, error icon, and a clear, accessible error message positioned below the input (mandatory).

This state helps users quickly identify and correct mistakes by explaining what went wrong and, when possible, how to fix it. The input remains editable, encouraging users to revise their input without starting over.

**⚠️ Error message vs helper text** The error message is not the same element as the helper text, it is independent. If a helper text accompanies the text input, it is replaced by the error message. The helper text must not be displayed simultaneously.

---

### Leading icon

Helps indicate the purpose of the input (magnifying glass for search, envelope for email, phone device for phone number). Only use a leading icon if it adds clear functional or contextual value.

---

### Other boolean options

**Prefix** A visual or textual element placed before the user's input. A prefix is not common and is discouraged in a Password Input component. Here are illustrative examples of very specific cases where:
• "corp-" Company password enforcing a prefix
• "temp-" Temporary password during a testing phase
• "dev-" For test accounts
• "eu-, us-, prod-, stage-" To encode a target environment
• "test@" Used in the context of automated or predictable tests
• "admin-" Pattern used to define an admin password

**Helper text** Supporting text conveys additional information about the input field, such as how it will be used. It should ideally only take up a single line, though may wrap to multiple lines if required, and be either persistently visible or visible only on focus.

---
