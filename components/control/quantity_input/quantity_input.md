# Guideline

## Intro

A quantity input lets users specify a numerical value using a text field with increment and decrement controls for easy adjustments.

---

## What is it

A quantity input is a form component that allows users to specify a numerical value representing a quantity, often used in contexts like shopping carts, inventory management, or booking systems. It typically combines a numeric text field with increment and decrement controls (such as "+" and "−" buttons) to make adjustments easy and precise. The component must enforce valid input ranges (minimum of 1), prevent invalid characters, and support keyboard input, stepper controls, and assistive technologies.

---

## Anatomy

| # | Element | Purpose |
|---|---------|---------|
| 1 | Label | Describes the purpose of the input field and provides context for users |
| 2 | Input field | Text field where users can type the numerical quantity value directly |
| 3 | Increment button | Button (+) that increases the quantity value by one unit |
| 4 | Decrement button | Button (−) that decreases the quantity value by one unit |
| 5 | Leading icon (optional) | Visual indicator that appears before the input to provide additional context |


---

## Usage & Guidance

### How should I configure labels and helper text for a shopping cart quantity?
Display a clear label like "Quantity" above the input, with optional helper text below showing constraints such as "Minimum quantity is 1" or "Select the number of items you wish to purchase."

### What should the error state look like when a quantity exceeds stock limits?
The input displays a red border with an error message below stating the specific issue, such as "Quantity must be between 1 and 99" or "Only 5 items available in stock."

### How do trailing vs. split button layouts differ visually?
Trailing layout places both increment and decrement buttons vertically stacked on the right side, while split layout positions the decrement button on the left and increment button on the right, flanking the input field horizontally.

### What's the visual difference between outlined and filled variants?
Filled variant shows a subtle background with a bottom border for contained layouts, while outlined variant displays a transparent background with a visible stroke around the entire field for lightweight contexts.

---

## Screen Variants

### Desktop
The component displays at full size with clear clickable buttons and comfortable spacing for mouse interactions. Labels and helper text are fully visible with adequate spacing between elements.

### Tablet
The component maintains similar sizing to desktop but may adjust spacing slightly to accommodate touch targets. All interactive elements remain easily accessible with finger input.

### Mobile
The component prioritizes touch-friendly targets with minimum 44×44px button sizes. The numeric keyboard automatically appears when users tap the input field for efficient mobile entry.

---

# Specs

## Properties

### Initial Config

| Property | Default Value | Notes |
|----------|---------------|-------|
| Outlined | False | Uses filled style with background and bottom border by default |
| Rounded corner | False | Square corners are standard for business contexts |
| Actions placement | Trailing | Buttons stacked vertically on the right side |
| Input status | Empty | No value displayed initially |
| State | Enabled | Interactive and ready for user input |
| Error | False | No validation errors present |
| Leading icon | False | No icon displayed before the input by default |

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

# Accessibility

## Keyboard Support

1. `Tab` moves focus to the quantity input field; `Shift+Tab` moves focus backward to the previous focusable element.
2. Arrow keys (`Up`/`Down`) increment or decrement the value by one unit when the input has focus.
3. `Enter` key submits the form if the input is part of a form, or triggers the associated action.
4. `Escape` key clears focus from the input field if no other action is defined.
5. Increment and decrement buttons must be keyboard-accessible and activated with `Enter` or `Space`.
6. Focus order follows left-to-right, top-to-bottom sequence: label → input field → increment/decrement buttons.
7. Provide a visible focus indicator with outline or border ≥2px and contrast ≥3:1 around the active element.
8. Ensure focus is not trapped within the component; users must be able to move focus forward and backward freely.

---

## Screen Reader Experience

1. Use semantic `<input type="number">` element with appropriate `role` if necessary (default role is sufficient).
2. Provide `aria-label` or `aria-labelledby` to associate the input with its visible label text.
3. Use `aria-describedby` to link the input to helper text and error messages with stable IDs.
4. Apply `aria-invalid="true"` when the input contains an invalid value and link error text via `aria-describedby`.
5. Announce value changes via `aria-live="polite"` when increment/decrement buttons are used, stating "Quantity set to [value]".
6. Ensure increment and decrement buttons have accessible names like "Increase quantity" and "Decrease quantity" via `aria-label`.
7. If min/max constraints exist, communicate them via `aria-valuemin`, `aria-valuemax`, and `aria-valuenow` attributes.
8. Group the input with its label and buttons using `role="group"` or `<fieldset>` with `<legend>` for complex layouts.
9. Ensure all state changes (enabled, disabled, read-only, error) are programmatically determinable via ARIA attributes.

---

## Touch & Mobile

1. Ensure increment and decrement buttons meet minimum touch target size of 44×44px (48×48px preferred).
2. Provide spacing of ≥8px between buttons and other interactive elements to prevent accidental taps.
3. Use `inputmode="numeric"` to trigger the numeric keyboard on mobile devices for efficient entry.
4. Support both portrait and landscape orientations without loss of functionality or content reflow issues.
5. Consider larger button sizes and spacing on mobile to accommodate finger-based interactions.

---

## Visual Accessibility

1. Ensure text contrast ≥4.5:1 for label, input text, and helper text; large text contrast ≥3:1.
2. Ensure UI components (buttons, borders, focus indicators) have contrast ≥3:1 against adjacent colors.
3. Do not rely solely on color to convey error state; include text messages, icons, or border thickness changes.
4. Support text resizing up to 200% (browser zoom) without loss of content or functionality; content must reflow properly.
5. Respect `prefers-reduced-motion` by avoiding or minimizing animations for value changes and state transitions.
6. Ensure focus indicators are clearly visible and maintain ≥3:1 contrast against the background.

---

## Error Handling

1. Apply `aria-invalid="true"` to the input field when it contains an invalid value.
2. Link error messages to the input using `aria-describedby` with a stable, unique ID.
3. Announce errors immediately via `aria-live="assertive"` when validation fails, and return focus to the input field.
4. Provide specific, actionable error messages such as "Quantity must be between 1 and 99" instead of generic "Error" messages.
5. Announce success states when appropriate (e.g., "Quantity updated successfully") and describe next steps if needed.
6. Display error messages visually below the input in a distinct color (red) and with sufficient contrast.
7. Preserve user input when displaying errors; do not clear the field unless necessary for security or validation reasons.

---

## Testing Checklist

**Quick Tests (≤5 minutes)**

1. Navigate the component using only the keyboard (`Tab`, `Shift+Tab`, arrow keys) with visible focus indicators at all times.
2. Use a screen reader to verify labels, helper text, and error messages are announced correctly and immediately.
3. Zoom the page to 200% and confirm the layout reflows without content loss, overlap, or horizontal scrolling.
4. Enable high-contrast mode or dark mode and verify focus indicators, borders, and text remain perceivable.
5. On a touch device, confirm buttons meet 44×44px minimum size and the numeric keyboard appears when tapping the input.

**Common Issues to Avoid**

1. Using color alone to indicate error state without accompanying text, icons, or border changes.
2. Missing `aria-invalid` and `aria-describedby` attributes on inputs with validation errors.
3. Focus indicators with insufficient contrast (<3:1) or missing entirely.
4. Buttons or interactive elements smaller than 44×44px on mobile devices.
5. Error messages not linked to inputs programmatically, causing screen readers to miss announcements.
