# Text Input - Definition & Properties

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

**`True`** A minimalist input with a transparent background and a visible stroke outlining the field. This style may be interesting for contexts other than form pages:
• When inputs need to feel lightweight and unobtrusive
• In a header (search field)
• In a selection/filtering feature in a product catalog

---

### Rounded corner

**`False`** An input without rounded corner.

**`True`** An input with a rounded corner. This style may be interesting for contexts other than form pages:
• When inputs need to feel lightweight and unobtrusive
• In a header (search field)
• In a selection/filtering feature in a product catalog

---

### Input status

**`Empty`** An empty input field state with no user-entered content and no placeholder text. Represents the initial state when a form first loads.

**`Empty (Placeholder)`** An empty field displaying placeholder text to guide users on the expected input format or purpose. The placeholder disappears when the user starts typing.

**`Filled`** A field containing user-entered text or pre-populated data. This state indicates that the field has been successfully engaged with and contains information.

---

### State

**`Enabled`** The default interactive state where users can click into the field and begin typing. The field responds to hover, focus, and input events. This represents a fully functional, ready-to-use state.

**`Hover`** The appearance of the input when the cursor is positioned over the field but hasn't clicked yet. Provides visual feedback that the field is interactive and can be selected. Typically shows subtle styling changes like border color shifts.

**`Focus`** The active editing state when a user has clicked into the field and can type. The field displays a prominent focus indicator (like a border highlight) to show it's currently selected. This state receives all keyboard input.

**`Loading`** The state shown when the system is processing input-related actions, such as validating data, fetching autocomplete suggestions, or performing real-time checks. Usually displays a loading spinner or progress indicator while preserving the field's content.

**`Read only`** A view-only state displaying static information that users cannot modify. The field appears with reduced visual emphasis to indicate its non-editable nature. Useful for displaying confirmation details or information that shouldn't be changed.

**`Disabled`** An inactive state where the field is visible but completely non-interactive. Typically shown in greyed-out styling to clearly communicate unavailability. Used when a field is not applicable to the current workflow or lacks necessary permissions.

**`Skeleton`** A loading placeholder state displayed before actual content loads. Shows an animated shimmer or gradient effect as a temporary visual while waiting for field initialization or data retrieval. Part of the skeleton loading pattern for perceived performance.

---

### Error

**`False`** The field is in a valid state with no validation errors. Displays the standard appearance without any error indicators or messaging. Used when input meets all requirements or hasn't been validated yet.

**`True`** The validation error state showing that the input doesn't meet requirements. Displays error styling (typically red borders), error messages explaining the issue, and potentially error icons. Used after validation fails to guide users toward correct input. Error messages should be clear, specific, and actionable to help users fix the issue.

---

### Leading icon

**`False`** The input field displays without a leading icon, showing only the text container and label. This is the default configuration for most basic input fields.

**`True`** The input includes a functional icon positioned at the start of the field, before the user's text entry area. Leading icons help users quickly identify the input's purpose (like a search icon for search fields or a lock for password inputs).

---

### Trailing action

**`False`** The input displays without any trailing action button or icon. This is the standard configuration where the field ends with just the text entry area.

**`True`** The input includes an interactive element (button or icon) positioned at the end of the field, after the text entry area. Common trailing actions include clear/reset buttons, password visibility toggles, or submit/search buttons.

---

### Other boolean options

**⚠️ Label** Describes the purpose of the input. Includes a warning symbol to indicate this is an important field property with accessibility implications.

**Autocompletion** Enables or disables autocomplete suggestions that appear as the user types, offering relevant options based on past inputs or system data.

**Prefix** Adds a fixed text or symbol before the user's input value (like currency symbols "$" or units "kg"). The prefix remains static while the user types.

**Suffix** Adds a fixed text or symbol after the user's input value (like domain extensions ".com" or percentage symbols "%"). The suffix remains static while the user types.

**Helper text** Displays supplementary guidance below the input field to clarify expected format, provide examples, or offer contextual help. This text supports users in completing the field correctly.

**Helper link** Provides a clickable link below the input field that directs users to additional information, documentation, or assistance related to filling out the field.

---