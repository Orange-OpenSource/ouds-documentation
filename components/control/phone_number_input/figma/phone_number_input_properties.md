# Phone number input - Definition & Properties

---

### Definition

A phone number input is a form field specifically designed to capture and validate telephone numbers, often in international format. It typically integrates a country selector, allowing users to choose their country and automatically apply the corresponding dialing code (such as +33 for France).

The dialing code is usually displayed as a non-editable prefix within the field to guide the user and ensure consistent formatting. The component include real-time formatting or masking to improve readability during input, and validation rules tailored to the number structure of the selected country.

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
| Country selector | 'False' \| 'True' |
| ⚠️ Label | boolean |
| ✏️ Label | text |
| Dial code | boolean |
| ✏️ Dial code | text |
| ✏️ Placeholder | text |
| ✏️ Input text | text |
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

**Country selector** On

**⚠️ Label** On

**Dial code** On

**Helper text** Off

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

**`False`** The input field is rectangular with sharp corners, creating a clean and structured appearance. This style is well-suited for form-based interfaces and professional, formal layouts, where clarity and alignment are key.

**`True`** The input field features rounded corners, giving it a softer and more modern look. This style works well in consumer-facing applications or interfaces with a friendly, approachable tone.

---

### Input status

**`Empty`** The field is empty. The placeholder text is not visible: the label is displayed instead and remains visible when the user starts typing.

**`Empty (Placeholder)`** The field is empty. The placeholder text is displayed in lieu of the label as an additional way to provide a contextual hint.

**`Filled`** The field has been filled out by the user.

---

### State

**`Enabled`** The default state when the user can interact with the text input. The field is ready to accept input when the user clicks or taps on it.

**`Hover`** Triggered when the user hovers the cursor over the input. This state provides visual feedback, signaling that the field can be interacted with.

**`Focus`** Activated when the user clicks or taps into the input, indicating that the field is currently selected and ready for input. This state is critical for accessibility, as it shows exactly where the user's focus is within the form.

**`Loading`** The component displays a loading indicator to inform the user that a process is underway, such as validating the input. The input remains disabled during this time.

**`Read only`** The input contains data but is not editable. This state is useful for displaying pre-filled data that the user shouldn't alter, like information pulled from a database or data confirmed in a previous step.

**`Disabled`** The input is inactive and cannot be interacted with. This state indicates that the field is currently unavailable, such as in cases where a required previous action has not been completed.

**`Skeleton`** A placeholder state to indicate that content is loading or being fetched. Useful in maintaining the layout structure while the actual data is being retrieved, providing a smooth user experience during initial page loads.

---

### Error

**`False`** The input is in a standard state, with no validation issues. It is ready for users to fill out without errors.

**`True`** The input has detected a validation error. An error message provides guidance to the user about what needs to be corrected. Error handling can be done either when the user navigates away from the field (on blur) or upon submission (when the user submits the form).

---

### Leading icon

**`Leading icon`** When enabled, it is possible to display an icon on the left of the input text.

---

### Country selector

**`Country selector`** When enabled, it is possible to display a country selector with its flag. Country selector is displayed as a secondary button with only an icon (flag) and a chevron.

---

### Other boolean options

**Dial code** When enabled, it is possible to display the country dial code value. The dial code is read-only and cannot be edited directly by the user.

**Helper text** When enabled, a helper text appears below the input field to provide additional context or tips on how to fill out the field. Useful for offering suggestions or clarifying expected input formats (e.g., "Please enter a phone number in international format").

---

### Accessibility

**Associating labels with text fields** Labels must be provided to give textual description of the input field.
With rare exceptions, each text area field should have a label. It is essential that the purpose and expected input remains clear to the user. Even for phone number inputs where some of the elements can stay implicit, such as the country flag, labels remain important.

**Keyboard navigation** The phone number input must be fully navigable via keyboard, including the input field and the country selector. Tabbing through form elements should move the focus logically from one field to the next, ensuring all interactive elements are accessible. Focus states must be visually distinct and meet accessibility contrast standards.

**Country selection and autofill support** When integrating the country selector, ensure that autocomplete attributes are used correctly to allow browsers and assistive technologies to autofill fields accurately. Example: use autocomplete="tel-national" for the phone number field. Consider providing clear labels for both the country code and the phone number to maintain context.

**ARIA labels and instructions** Provide appropriate ARIA labels for elements like the country selector or dialcode. For example, the flag icon may not be immediately understood by screen readers without a clear label. Use aria-label to clarify the purpose of each component. For instance: aria-label="Select Country" for the country button.

**Error handling and validation** When validation errors occur, use aria-invalid="true" and aria-describedby to clearly communicate what went wrong and how to fix it. Ensure that error messages are announced immediately by screen readers, so users can correct issues without having to navigate away from the field.

**Complex input structures** Phone number inputs often combine multiple elements (e.g., flag, dial code, input field). Test with screen readers to ensure users understand each element's purpose and relationship to the other components. Use fieldset and legend when grouping multiple input components together, to make the relationships clear.

**Voice input** Users may prefer to fill out the field using voice commands, especially for phone numbers. Ensure that the input field supports dictation tools and that the input format doesn't interfere with voice-to-text recognition.