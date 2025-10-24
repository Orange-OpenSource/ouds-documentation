# Accessibility

### Keyboard Support

1. Press `Tab` to focus the first empty input field in the sequence; press `Shift+Tab` to move focus backward through fields.
2. Type a numeric digit (0-9) to fill the current field and automatically advance focus to the next empty field.
3. Press `Backspace` to clear the current field and move focus to the previous field if the current field is empty.
4. Press arrow keys (`ArrowLeft`, `ArrowRight`) to manually navigate between input fields without deleting content.
5. Provide a visible focus indicator with outline or border ≥2px and contrast ≥3:1 on the currently active input field.
6. Press `Enter` to submit the complete code once all fields are filled (if auto-submit is not enabled).

---

### Screen Reader Experience

1. Use semantic `<input type="text" inputmode="numeric">` elements for each digit field with `maxlength="1"`.
2. Provide a group label using `role="group"` with `aria-labelledby` pointing to the main label text (e.g., "Enter 6-digit verification code").
3. Announce the field position and total count using `aria-label` on each input (e.g., "Digit 1 of 6", "Digit 2 of 6").
4. Apply `aria-invalid="true"` to all input fields when in error state and link error message using `aria-describedby`.
5. Announce error messages immediately using `aria-live="assertive"` and provide specific feedback about what went wrong (incorrect code, expired, attempts exceeded).
6. Announce successful code entry using `aria-live="polite"` when validation passes and next action is available.

---

### Touch & Mobile

1. Provide touch targets ≥44×44px for each input field with spacing ≥8px between fields to prevent accidental touches.
2. Trigger numeric keyboard automatically using `inputmode="numeric"` or `type="tel"` to optimize for digit entry on mobile devices.
3. Support auto-advance between fields on digit entry to reduce the need for manual navigation taps.
4. Ensure the entire component remains visible when the mobile keyboard appears; adjust viewport scroll if necessary.
5. Support both portrait and landscape orientations without loss of functionality or field visibility.

---

### Visual Accessibility

1. Ensure text and digit content have contrast ≥4.5:1 against background; labels and helper text must meet the same ratio.
2. Ensure input field borders, focus indicators, and error state borders have contrast ≥3:1 against adjacent surfaces.
3. Do not rely on color alone to convey error state; include error icon and descriptive error message text below the fields.
4. Support text resizing up to 200% without loss of content, functionality, or horizontal scrolling (reflow must pass).
5. Respect `prefers-reduced-motion` and avoid auto-advance animations or transitions that rely on motion to convey state changes.

---

### Error Handling

1. Apply `aria-invalid="true"` to all input fields in the group when the complete code fails validation.
2. Link the error message to all inputs using `aria-describedby` with a stable ID referencing the error text element.
3. Announce errors immediately via `aria-live="assertive"` after validation fails and return focus to the first input field for correction.
4. Provide specific, actionable error messages: "Incorrect code. Please try again" or "Code expired. Request a new code" instead of generic "Error".
5. Announce success state using `aria-live="polite"` when the correct code is entered and describe the next step in the flow.
6. Clear all fields or maintain entered values based on security requirements when displaying errors; document this behavior clearly.

---

### Testing Checklist

**Quick Tests (≤5 minutes)**

1. Complete digit entry using keyboard only with visible focus moving sequentially; `Backspace` navigates backward correctly.
2. Screen reader announces each field position ("Digit 1 of 6"), group label, and error messages immediately upon validation failure.
3. Zoom to 200%: all input fields remain visible and functional without horizontal scrolling; layout reflows appropriately.
4. High-contrast mode: focus indicators, field borders, and error states remain clearly visible with ≥3:1 contrast.
5. On touch device: numeric keyboard opens automatically; targets are ≥44×44px; auto-advance works between fields.

**Common Issues to Avoid**

1. Missing group label or individual field position announcements for screen reader users.
2. Color-only error indication without accompanying error icon or descriptive error message text.
3. Missing `aria-invalid="true"` or `aria-describedby` linking error message to input fields in error state.
4. Insufficient contrast (<3:1) for focus indicators or error state borders against background.
5. Focus trap within digit fields preventing users from navigating to submit button or other page elements.
6. Auto-advance not working or moving focus before users can correct a mistyped digit.