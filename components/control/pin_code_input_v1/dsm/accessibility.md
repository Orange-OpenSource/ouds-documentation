# Accessibility

## Keyboard Support

1. `Tab` moves focus to the first empty digit box or the first box if all are empty.
2. `Shift+Tab` moves focus backward from the component to the previous focusable element.
3. Arrow keys (`Left`/`Right`) navigate between digit boxes without deleting content.
4. `Backspace` deletes the current digit and moves focus to the previous box.
5. `Delete` removes the current digit and keeps focus on the same box.
6. `Enter` submits the form when all required digits are filled.
7. Number keys (`0`-`9`) enter digits and automatically advance focus to the next box.
8. Provide a visible focus indicator: outline or border ≥2px with contrast ≥3:1 against the background.
9. Focus order moves left-to-right through digit boxes, then to submit button or next form element.
10. Pasted content auto-distributes across boxes without breaking focus management.

---

## Screen Reader Experience

1. Use semantic `<input type="text" inputmode="numeric">` elements for each digit box.
2. Provide a group label via `<fieldset>` and `<legend>` or `role="group"` with `aria-labelledby` (e.g., "Enter 6-digit verification code").
3. Announce helper text using `aria-describedby` referencing the helper text ID.
4. Apply `aria-invalid="true"` to all digit inputs when in error state.
5. Link error messages to inputs using `aria-describedby` with a stable error ID.
6. Announce "digit 1 of 6", "digit 2 of 6" using `aria-label` on each input for positional context.
7. Use `aria-live="polite"` on the error message container to announce validation results on submission.
8. Ensure the current digit box value is announced when focus moves between boxes.

---

## Touch & Mobile

1. Provide touch targets ≥44×44px for each digit box with ≥8px spacing between boxes.
2. Use `inputmode="numeric"` to trigger the numeric keyboard on mobile devices.
3. Support paste gestures: long-press to paste full codes, auto-distributing digits across all boxes.
4. Ensure tap targets don't overlap; provide clear visual separation between digit boxes.
5. Support both portrait and landscape orientations without loss of functionality or layout breaking.

---

## Visual Accessibility

1. Ensure text contrast ≥4.5:1 for digit values and helper text; large text ≥3:1.
2. Ensure digit box borders and focus indicators have contrast ≥3:1 against the background.
3. Do not rely on color alone for error state; add error icons or text indicators below the component.
4. Support text resizing up to 200% without loss of content or functionality; digit boxes must reflow gracefully.
5. Respect `prefers-reduced-motion` for any animations related to focus transitions or error state changes.

---

## Error Handling

1. Apply `aria-invalid="true"` to all digit inputs when validation fails.
2. Link error text to inputs using `aria-describedby` with a stable error message ID.
3. Announce errors via `aria-live="polite"` immediately after form submission with validation failure.
4. Provide specific error messages: "Please enter the verification code" (empty) or "Verification failed. Check and enter the correct code" (incorrect).
5. Return focus to the first digit box after error announcement to enable immediate correction.
6. Remove `aria-invalid="false"` and clear error messages when user begins re-entry or validation succeeds.
7. Maintain helper text visibility even when error state is active; stack error message below helper text.

---

## Testing Checklist

### Quick Tests (≤5 minutes)

1. Keyboard-only: Tab to first box, type digits with auto-advance, use Backspace to correct, submit with Enter; visible focus indicators appear throughout.
2. Screen reader: Group label announces "Enter 6-digit verification code", each box announces "digit X of 6", error message reads "Verification failed. Check and enter the correct code" on submission.
3. Zoom to 200%: Digit boxes reflow without overlapping; all text and spacing remain readable and functional.
4. High-contrast/dark mode: Focus indicators, digit box borders, and error states remain perceivable with ≥3:1 contrast.
5. Touch device: Each digit box meets 44×44px target size; numeric keyboard opens automatically; paste from SMS distributes digits correctly.

### Common Issues to Avoid

1. Missing `aria-invalid` or `aria-describedby` on digit inputs when error state is active.
2. Color-only error indication without accompanying text or icon.
3. Focus indicator contrast <3:1 or missing visible focus on keyboard navigation.
4. Paste functionality not working or requiring manual digit-by-digit entry.
5. Error messages not announced by screen readers or missing specific guidance on correction.