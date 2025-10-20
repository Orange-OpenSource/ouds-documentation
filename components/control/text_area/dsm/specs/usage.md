## Usage

### Label visibility and accessibility
**Do:** Always ensure labels are accessible to screen readers using `aria-label`, `aria-labelledby`, or visually hidden text when the visible label is hidden for design purposes.

**Don't:** Hide labels without providing alternative accessible labeling, as this creates confusion for users relying on assistive technologies.

### Character limit guidance
**Do:** Display character limits proactively with real-time counters to help users stay within constraints before reaching an error state.

**Don't:** Block user input when character limits are exceeded; instead, show the excess count and allow users to edit their content back within limits.

### Error message clarity
**Do:** Replace helper text with clear, actionable error messages that explain what went wrong and how to fix it, while preserving helper links below the error.

**Don't:** Stack error messages on top of helper text or remove helper links when errors occur, as this removes important contextual information.

### Resize behavior consistency
**Do:** Use automatic expansion from 3 to 10 lines with internal scrolling at maximum height to maintain consistent layout across the interface.

**Don't:** Allow manual resize handles that can break responsive layouts or create inconsistent component behavior across the design system.

---