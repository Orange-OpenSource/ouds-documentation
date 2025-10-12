# Specs

## Properties

### Initial Config

| Property | Default Value | Notes |
|----------|---------------|-------|
| Outlined | False | Filled style with background fill and bottom border |
| Rounded corner | False | Square corners for standard contexts |
| Input status | Empty | Neutral starting state with no content |
| State | Enabled | Interactive and ready for user input |
| Error | False | No validation errors present |
| Scrolled | False | No overflow requiring scroll |
| Label | True (visible) | Label displayed by default |
| Helper text | False | No helper text shown by default |
| Helper link | False | No additional help link provided |

---

### Outlined

**`False`**

An input with a subtle background fill and visible bottom border, creating a softer and more contained look. Best suited for dense layouts or to enhance visibility.

**`True`**

A minimalist input with a transparent background and a visible stroke outlining the field. This style may be interesting for contexts other than form pages:
- When inputs need to feel lightweight and unobtrusive
- In a header (search field)
- In a selection/filtering feature in a product catalog

---

### Rounded Corner

**`False`**

For a square finish.

**`True`**

For a finish with rounded corner. To be favored in more emotional, immersive contexts or those tied to specific visual identities. For standard or business-oriented journeys, keep the default corners. This evolution addresses the need for flexibility in adapting the design to certain brand contexts.

---

### Input Status

**`Empty`**

The Empty state indicates that the text area is blank with no content or placeholder, a neutral starting point.

**`Empty (Placeholder)`**

The Empty with Placeholder state provides a hint or guidance inside the field to suggest expected input.

**`Filled`**

The Filled state shows that the user has entered valid content into the field, replacing any placeholder.

---

### State

**`Enabled`**

Neutral appearance, whether empty or filled. It allows users to click, focus, and type freely without restrictions.

**`Hover`**

Slight visual contrast or border color change.

**`Focus`**

The text area is focused and ready to receive user input. It visually highlights the field to indicate that it's currently editable and interactive. This state typically appears after a user clicks or taps into the field.

**`Loading`**

The Loading state indicates that the system is processing or retrieving data related to the text area. A progress indicator appears to inform the user that an action is in progress. During this state, the input may be temporarily disabled to prevent further interaction.

**`Read only`**

Text visible but not editable (often with a muted or different background).

**`Disabled`**

The field is non-interactive and grayed out to indicate it cannot be changed. The helper text is muted.

**`Skeleton`**

Improves the perceived loading time by providing a visual cue of where field will appear once fully loaded. Uses the "Skeleton" component, variant "Security marge=False".

---

### Error

**`False`**

No validation errors present. The text area displays in its normal state.

**`True`**

The Error status indicates that the user input does not meet validation rules, for example, in this specific case, if the number of characters entered by the user exceeds the allowed limit. It provides immediate visual feedback, typically through a red border, error icon, and a clear, accessible error message positioned below the input.

This state helps users quickly identify and correct mistakes by explaining what went wrong and, when possible, how to fix it. The input remains editable, encouraging users to revise their input without starting over.

⚠️ **Error message vs helper text / link**

If a helper text accompanies the text input, it is replaced by the error message. However, a helper link must not be replaced and should remain positioned below the error message.

---

### Scrolled

**`False`**

No overflow present. All text content is visible within the current field height.

**`True`**

Represents the state in which the field contains more text than its visible height can display and that internal scrolling is available. This allows users to navigate through the overflowing text without expanding the text area beyond the maximum planned height of 240px, allowing the display of about 10 lines of text. It is particularly useful when preserving space is important, or when the text area is embedded within a fixed-height container.

---

### Label Visibility

**Visible (default)**

The label is displayed above the text area, clearly identifying the field's purpose.

**Hidden**

In some UI contexts, especially when space is limited or when the input is part of a compact layout (search bars, filters, inline forms), visually hiding the label can help maintain a clean and uncluttered interface.

However, hiding the label should only be done if:
- The purpose of the input remains clear thanks to a placeholder or contextual icon.
- The label is still accessible to screen readers (using aria-label, aria-labelledby, or visually hidden text).

Hiding a label is a design choice that must balance visual simplicity and clarity of intent, without compromising inclusiveness or form guidance.

---

### Helper Text

**`False`**

No helper text is displayed below the input field.

**`True`**

Supporting text conveys additional information about the input field, such as how it will be used. It should ideally only take up a single line, though may wrap to multiple lines if required, and be either persistently visible or visible only on focus.

---

### Helper Link

**`False`**

No additional help link is provided.

**`True`**

If the helper text is not sufficient (It can also be displayed on its own without helper text), it's possible to offer the user an additional help link (the link can be external or open a modal).

---

### Behavior by Entered Line Count

**Default display**

By default, the height of the input text container is set to 72px, which allows 3 lines of text to be displayed without expanding the component. This height helps distinguish the field from other text inputs, prevents discouraging users with an overly large field, and keeps the layout compact at the start of a form.

**Auto-resize (automatic expansion)**

Above 3 lines of text, the field automatically increases in height as the user types their content.

**Vertical scrollbar**

If expansion is disabled or the maximum height is reached at 240px, corresponding to about 10 lines of text, an internal scrollbar appears allowing the user to scroll through the overflowing text. This choice prevents breaking the layout but has the drawback, on mobile, of creating a scroll within a scroll (text area scroll inside a page scroll).

⚠️ **No manual resize (by the user)**

On both desktop and mobile, we have chosen to disable manual resizing to avoid behaviors inconsistent with the design system.

---

### Character Counter

**Character limit not exceeded**

The character counter, located in the helper text area, displays in real time (with each keystroke) the number of characters the user can still enter before reaching the field's allowed limit.

⚠️ It is impossible to provide a recommendation for the maximum number of characters, as this depends too specifically on the constraints (or lack thereof) of each project.

**Character limit exceeded**

If the user exceeds the set limit, the field enters an error state, but input is not blocked. The character counter then shows the user, still in real time, how many characters have been entered beyond the field's allowed limit.

The user must reduce the number of characters entered for the text area to exit the error state.

---

## Usage

### Provide clear labels and helper text
**Do:** Always include a descriptive label that clearly identifies the purpose of the text area. Use helper text to provide additional guidance about expected content, format, or character limits.

**Don't:** Rely solely on placeholder text to communicate the field's purpose, as it disappears when users begin typing and may not be accessible to all users.

### Set appropriate character limits
**Do:** Define character limits based on actual content requirements and display them with a real-time counter to help users stay within bounds while maintaining flexibility for editing.

**Don't:** Set arbitrarily restrictive character limits that force users to compress their thoughts unnaturally, or block input when limits are exceeded without allowing users to edit their content.

### Maintain consistent field heights
**Do:** Allow the text area to auto-resize from the default 3-line height up to the maximum 10-line height, providing visual feedback about content length while preserving layout integrity.

**Don't:** Allow unlimited vertical expansion that breaks page layout, or disable auto-resize entirely forcing users to scroll within a tiny field from the first line of text.

### Handle errors constructively
**Do:** Provide specific, actionable error messages that explain what went wrong and how to fix it. Keep the field editable so users can make corrections without starting over.

**Don't:** Display vague error messages like "Invalid input" without explanation, or disable the field entirely when errors occur, forcing users to clear and re-enter all their content.