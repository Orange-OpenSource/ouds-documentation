# Accessibility

### Keyboard Navigation
Users must be able to navigate to the text area using the Tab key and enter it in the natural tab order of the form. Once focused, users should be able to type freely, with Enter creating new lines within the multi-line field. Shift+Tab should move focus backward. The focus indicator must have a minimum contrast ratio of 3:1 against the background. Arrow keys should navigate within the text content, and keyboard scrolling (Page Up/Page Down, Home/End) should work when internal scrolling is active.

---

### Screen Reader Support
The text area must use the semantic `<textarea>` HTML element to ensure proper identification by assistive technologies. Labels must be explicitly associated with the textarea using the `for` attribute matching the textarea's `id`, or by wrapping the textarea in a `<label>` element. Helper text should be associated using `aria-describedby` to provide context. Error messages must use `aria-describedby` or `aria-errormessage` to announce validation issues. Character count information should be announced dynamically using `aria-live="polite"` regions to inform users of remaining or exceeded characters without interrupting their input flow.

---

### ARIA Attributes
Required attributes include `aria-label` or `aria-labelledby` when labels are visually hidden, ensuring screen readers can identify the field's purpose. Use `aria-describedby` to reference helper text, character counters, and additional instructions. When errors occur, add `aria-invalid="true"` and associate error messages with `aria-describedby` or `aria-errormessage`. For character limits, use `aria-live="polite"` on the counter element to announce updates. If the textarea is required, include `aria-required="true"`. In read-only state, add `aria-readonly="true"`, and in disabled state, use the `disabled` attribute which implicitly communicates non-interactivity.

---

### Focus Management
When the text area receives focus, a clear visual indicator must appear with sufficient contrast (3:1 minimum). Focus should follow the natural document order unless programmatically managed for specific interactions. When validation errors occur, consider moving focus to the error message or maintaining it on the textarea with the error announced via `aria-live` regions. If the textarea is part of a modal or dialog, focus should be trapped within that container and restored to the triggering element when closed. Ensure focus is never lost during loading states, and that the loading indicator is announced appropriately.

---

### Error Handling
Error messages must be semantically associated with the textarea using `aria-describedby` or `aria-errormessage` so screen readers announce them when the field receives focus. The `aria-invalid="true"` attribute must be added to the textarea element when in an error state. Error messages should clearly explain what went wrong (e.g., "Character limit exceeded by 45 characters") and how to fix it. Visual indicators include a red border, error icon, and red error text meeting color contrast requirements. Error announcements should use `aria-live="assertive"` for immediate validation issues or `aria-live="polite"` for less urgent feedback. The textarea must remain editable during error states to allow correction.

---

### Touch Targets
The minimum touch target size for the text area should be at least 44x44 pixels to accommodate finger taps on mobile and tablet devices, following WCAG guidelines. Ensure adequate spacing (at least 8px) between the textarea and adjacent interactive elements to prevent accidental activation. The entire input container should be tappable to focus the field, not just the text within. Helper links and error messages below the textarea must also meet the 44x44px minimum touch target requirement with proper spacing.

---

### Color Contrast
All text within and around the text area must meet WCAG 2.1 AA contrast requirements: 4.5:1 for normal text (including labels, helper text, placeholder text, and input text) and 3:1 for large text. Error messages and error icons must maintain 4.5:1 contrast against their background. The focus indicator border must have at least 3:1 contrast against adjacent colors. In disabled state, text may have reduced contrast but should still be perceivable. Border colors, both in default and hover states, should meet 3:1 contrast for UI components. Ensure character counter text maintains 4.5:1 contrast in both normal and error states.

---

### Component-Specific Considerations
The auto-resize behavior from 3 to 10 lines must not cause unexpected scroll jumps or disorientation for users. Announce expansion behavior to screen reader users if it significantly changes the layout. The internal scrollbar that appears at maximum height creates a scroll-within-scroll situation, particularly problematic on mobile—ensure this is tested with screen readers and touch gestures. When the scrolled state is active, the scrollable region must be keyboard accessible and announced. Character limit feedback must be real-time but not overly verbose; use `aria-live="polite"` to balance immediacy with non-interruption. The skeleton loading state should include appropriate ARIA attributes (`aria-busy="true"` or `aria-live="polite"`) to inform users that content is loading. Ensure placeholder text is not relied upon as the sole labeling mechanism, as it disappears on input and may not be announced consistently.