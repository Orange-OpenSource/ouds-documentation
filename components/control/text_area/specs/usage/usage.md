## Usage

### Label Visibility and Clarity
**Do:** Always provide a clear, descriptive label that explains the purpose of the text area, even if it's visually hidden for compact layouts, ensuring screen readers can access it via aria-label or aria-labelledby.

**Don't:** Hide the label without providing alternative accessible text or rely solely on placeholder text to convey the field's purpose, as placeholders disappear when users start typing.

---

### Character Limit Communication
**Do:** Set appropriate character limits based on content requirements and display the real-time character counter in the helper text area to provide continuous feedback as users type.

**Don't:** Block user input when the character limit is exceeded; instead, enter an error state that clearly shows how many characters need to be removed while keeping the content editable.

---

### Helper Text and Error Messages
**Do:** Use helper text to provide guidance on expected content format or usage, and replace it with clear, actionable error messages that explain what went wrong and how to fix it when validation fails.

**Don't:** Display both helper text and error messages simultaneously, or remove helper links when showing error messages—keep helper links positioned below the error message for additional support.

---

### Height and Scrolling Behavior
**Do:** Allow the text area to expand automatically from the default 3-line height (72px) up to the maximum 10-line height (240px), then introduce a scrollbar for overflow content to maintain layout consistency.

**Don't:** Enable manual resizing by users or allow unlimited vertical expansion that could break the layout, especially in mobile contexts where scroll-within-scroll can create confusing interactions.