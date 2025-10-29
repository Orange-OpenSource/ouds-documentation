# Quantity input - COMPLETE DOCUMENTATION

---

### Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Sep 30, 2025 | 1.2.0 | • For the property "Actions placement", the name of the variant "Right" is replaced by "Trailing" (RTL consideration)<br>• The name of the "Style" variant has been replaced to "Outlined" with true/false variant | Hamza Amarir |
| Jul 29, 2025 | 1.1.0 | • Several design token updates: [Component tokens changelog 1.5.0](https://www.figma.com/design/Co2t6wHMf4GB9NJVGs2Hes/-OUDS-Core-Lib--Design-tokens?m=auto&node-id=9280-2568&t=HLVB4jOd35DWr8Bj-1) | Maxime Tonnerre |
| Jun 30, 2025 | 1.0.0 | • Component creation | Maxime Tonnerre |

---

### Definition

A quantity input is a form component that allows users to specify a numerical value representing a quantity, often used in contexts like shopping carts, inventory management, or booking systems. It typically combines a numeric text field with increment and decrement controls (such as "+" and "–" buttons) to make adjustments easy and precise. The component must enforce valid input ranges (minimum of 1), prevent invalid characters, and support keyboard input, stepper controls, and assistive technologies.

---

### Properties

| property name | type |
|---------------|------|
| Outlined | 'False' \| 'True' |
| Rounded corner | 'False' \| 'True' |
| Actions placement | 'Trailing' \| 'Split' |
| Input status | 'Empty' \| 'Empty (Placeholder)' \| 'Filled' |
| State | 'Enabled' \| 'Hover' \| 'Focus' \| 'Loading' \| 'Read only' \| 'Disabled' \| 'Skeleton' |
| Error | 'False' \| 'True' |
| Leading icon | 'False' \| 'True' |
| ⚠️ Label | boolean |
| ✏️ Label | text |
| ✏️ Placeholder | text |
| ✏️ Input text | text |
| Suffix | boolean |
| Helper text | boolean |
| ✏️ Helper text | text |
| ✏️ Error empty text | text |
| ✏️ Error filled text | text |

---

### Initial settings

**Outlined** Off

**Rounded corner** Off

**Actions placement** Trailing

**Input status** Empty

**State** Enabled

**Error** Off

**Leading icon** Off

**⚠️ Label** On

**Suffix** Off

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

**`Empty`** The input has not been interacted with yet, and no value (not even a placeholder) is displayed. Only the label is visible.

**`Empty (Placeholder)`** The input has not been interacted with yet and displays a placeholder text to guide the user on what to enter. The placeholder appears in a lighter color and disappears when the user starts typing.

**`Filled`** The input contains a value that has been entered by the user or pre-filled by the system. The filled state is the result of user interaction or a default value provided by the application.

---

### Actions placement

**`Trailing`** The increment and decrement action buttons are positioned on the trailing side (right in LTR languages, left in RTL languages) of the input field, both one above the other. This creates a condensed vertical layout that is consistent with the overall spatial hierarchy of the input field and keeps the entire component compact within a single inline flow.

**`Split`** The decrement button is positioned on the leading side (left in LTR languages, right in RTL languages), while the increment button is on the trailing side. This creates a horizontal arrangement that visually balances the input field. This layout visually resembles physical controls or product detail pages.

---

### States

**`Enabled`** The component is interactive and ready for use. Users can type in the input or use the increment/decrement buttons.

**`Hover`** The visual appearance of the input field changes when the user hovers their mouse over it, indicating interactivity.

**`Focus`** The input field is currently selected and active, ready to receive keyboard input. A visible focus indicator (such as a border or outline) makes it clear which element is active.

**`Loading`** The component displays a loading indicator while data is being fetched or processed (e.g., updating inventory or verifying constraints in real time). Users cannot interact with the input until the loading process is complete.

**`Read only`** The input displays a value that the user cannot modify. This is useful when the quantity is set by the system or determined by external factors. Users can view the value but cannot interact with the increment, decrement, or input field.

**`Disabled`** The input is not currently available for interaction, often due to contextual constraints (e.g., an item is out of stock, or the maximum allowable quantity has been reached). The component appears grayed out and does not respond to user actions.

**`Skeleton`** The component displays a placeholder animation (skeleton screen) while waiting for content to load. This provides a visual cue that data is being fetched and helps reduce perceived wait time.

---

### ⚠️ Specific focus state rules

In the Focus state, the border of the input field becomes thicker (2px instead of 1px). If the border were centered on the edge of the input, half of its thickness (0.5px inward and 0.5px outward) would increase the overall size of the component and could cause layout shifts or alignment issues with surrounding content.

To prevent this, the 2px border must expand inward rather than extending outward. This ensures:
• The component's outer dimensions remain constant, avoiding layout shifts.
• Visual consistency and alignment with adjacent elements.

**Practical implementation:**
• Use CSS techniques like box-sizing: border-box to ensure the border grows inward.
• Alternatively, create a pseudo-element (::before or ::after) positioned inside the component to simulate the thicker border without altering the component's box model.
• Avoid using outline, which may expand outward and cause unwanted misalignment, unless implemented with a negative offset.

---

### Error

In the Error state, the quantity input displays a clear indication that the user has entered an invalid value or that the entered value does not meet the required constraints (e.g., exceeds maximum stock, falls below the minimum quantity, or contains non-numeric characters). Depending on the context, the error may be triggered in two scenarios: when the input is empty (no value entered yet) or when the input is filled (a value has been entered but is invalid).

**Empty state error:**
• Triggered when the input is required, but the user attempts to submit the form or proceed without entering a value.
• Use the ✏️ Error empty text property to display a custom error message such as "This field is required" or "Please enter a quantity."
• The focus is typically on encouraging the user to provide a value before proceeding.

**Filled state error:**
• Triggered when the user has entered a value that does not meet validation criteria, such as exceeding the maximum allowed quantity, falling below the minimum, or entering invalid characters (e.g., letters or special symbols).
• Use the ✏️ Error filled text property to display a specific error message such as "Quantity must be between 1 and 99" or "Only numeric values are allowed."
• The focus is on correcting the invalid input without erasing the user's entry immediately (unless necessary for real-time validation).

---

### Error (continued)

For both cases, the component should:
• Display the error message below the input field in a distinct color (typically red) to clearly indicate the issue.
• Highlight the input field with an error border or background color to draw the user's attention to the invalid state.
• Provide actionable and specific guidance to help the user correct the issue quickly (e.g., "Enter a number between 1 and 10").

Good error messages are concise, specific, and solution-oriented, helping users understand what went wrong and how to fix it.

---

### Leading icon

This boolean property allows an icon to be displayed on the left side (leading side) of the input field, providing an additional visual cue or contextual indicator for the user.

When set to true, a decorative or functional icon appears at the start of the input. This could represent a category (such as a cart icon for a shopping cart), a unit type (such as a currency symbol for monetary input), or any other relevant visual hint that helps the user understand the context or purpose of the input field.

The leading icon does not replace the label but serves as a supplementary visual cue to reinforce the input's meaning or to make the interface more intuitive and visually engaging.

---

### Label

Label is a required element that describes the purpose of the input field. It provides users with clear context about what information or value they are expected to enter.

**⚠️ Label (boolean property)**

Determines whether the label is visible in the component. When set to true, the label is displayed and provides users with clear guidance on what to enter. When set to false, the label is hidden, though this is not recommended from an accessibility standpoint. Even if the label is visually hidden, it should remain present in the code for screen readers and assistive technologies to ensure that all users understand the purpose of the input.

**✏️ Label (text property - editable)**

Allows you to customize the text content of the label. By default, the label may read something like "Quantity" or "Number of items," but you can edit it to match your specific use case, such as "Select quantity," "Number of tickets," or "How many items?". Providing a clear and descriptive label helps users understand exactly what they are expected to input, improving usability and accessibility.

---

### Other boolean options

**Suffix** Allows an optional suffix (such as a unit indicator like "kg," "pcs," or "items") to be displayed after the input field. This provides additional context to the user about the unit or type of value being entered.

**Helper text** Determines whether additional explanatory text is displayed below the input field. When enabled, the Helper text can provide extra guidance, tips, or clarification to help users understand how to use the input correctly (e.g., "Minimum quantity is 1" or "Select the number of items you wish to purchase").

---

✅ Complete English content extracted - Format transformed to standard template