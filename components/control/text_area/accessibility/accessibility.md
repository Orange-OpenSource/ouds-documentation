### Keyboard navigation
The text area must be fully operable using keyboard controls. Users should be able to tab into the field, type content naturally, use arrow keys to navigate within text, and shift+tab to exit. The focus indicator must be clearly visible with sufficient contrast (minimum 3:1 ratio against adjacent colors) to show when the field is active. When an error occurs, focus should move to the error message or remain on the field with the error announced.


---


### Screen reader support
Implement proper semantic HTML using the `<textarea>` element with associated `<label>` elements connected via matching `for` and `id` attributes. The label must be programmatically associated even when visually hidden. Helper text should be associated using `aria-describedby`, and error messages should be linked with `aria-describedby` and announced using `aria-live="polite"` or `aria-live="assertive"` for critical errors. Character counter updates should be announced periodically, not on every keystroke to avoid overwhelming screen reader users.


---


### ARIA attributes and labels
Use `aria-label` or `aria-labelledby` when labels are visually hidden to ensure screen readers can identify the field's purpose. Apply `aria-required="true"` for mandatory fields. Use `aria-invalid="true"` when validation fails and `aria-describedby` to reference both helper text and error message IDs. For multi-part descriptions, include space-separated IDs in `aria-describedby` (e.g., `aria-describedby="helper-text-id error-message-id"`). The `aria-multiline="true"` attribute should be set to indicate the multi-line nature of the input.


---


### Error communication
Error messages must be clear, specific, and actionable, explaining both what went wrong and how to correct it. Errors should be communicated through multiple channels: visual styling (color, iconography), text content, and ARIA attributes. Never rely on color alone to indicate errors—always include an icon and text message. When character limits are exceeded, announce the overage amount and required reduction. Error states should not disable the field but should allow users to edit and correct their input immediately.


---


### Focus management
Maintain logical focus order within forms, ensuring the text area appears in the natural tab sequence. When users interact with helper links that open modals or external resources, manage focus appropriately—moving focus to the opened content and returning it to the text area upon closing. Avoid focus traps that prevent keyboard users from navigating away from the field.


---


### Touch target sizing
On mobile and tablet devices, ensure the entire text area input region meets minimum touch target size requirements of 44×44 pixels (iOS) or 48×48 pixels (Android). Interactive elements like helper links should be adequately spaced (minimum 8px separation) to prevent accidental activation. The scrollbar, when visible, should be thick enough for touch interaction without frustration.


---


### Color contrast requirements
All text within and around the text area must meet WCAG AA standards: 4.5:1 contrast ratio for normal text and 3:1 for large text (18pt or 14pt bold). This includes labels, input text, placeholder text, helper text, error messages, and character counters. In disabled states, ensure at least 3:1 contrast so users can still perceive the field's presence and label. Border colors and focus indicators must maintain 3:1 contrast against adjacent background colors.


---


### Component-specific accessibility concerns
The nested scroll pattern (scrollbar within the text area on a scrollable page) requires careful implementation to ensure screen reader users understand they're navigating within a bounded region. Consider using `role="textbox"` with `aria-multiline="true"` for custom implementations. The auto-resize behavior should not cause unexpected page reflows that disorient users. Loading states must be announced to screen readers using appropriate ARIA live regions. When the skeleton state is active, use `aria-busy="true"` or `aria-label="Loading"` to communicate the loading status to assistive technologies.