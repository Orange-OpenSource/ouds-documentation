# Accessibility

### Keyboard Support

1. `Tab` moves focus into the first empty digit box; `Shift+Tab` moves focus out to the previous form element.
2. Typing a valid numeric character (`0`–`9`) auto-advances focus to the next digit box (left→right); no auto-advance occurs on the last box.
3. `Backspace` clears the current digit and moves focus to the previous box; on the first box, Backspace clears the digit without moving focus.
4. `Arrow Left` / `Arrow Right` navigate between digit boxes without clearing content; wrap is not supported (focus stops at first/last box).
5. Provide a visible focus indicator with outline/border **≥2px** and contrast **≥3:1** against the background.

---

### Screen Reader Experience

1. Use semantic `<input type="text" inputmode="numeric">` elements for each digit box; group all boxes in a `<fieldset>` or `role="group"` with an accessible label (e.g., "Enter 6-digit verification code").
2. Provide `aria-label` or `aria-labelledby` on the group describing the purpose (e.g., "PIN code input, 6 digits required").
3. Apply `aria-invalid="true"` and `aria-describedby` linking to helper/error text when validation fails; announce error via `aria-live="assertive"` immediately upon submission failure.
4. Announce digit count in helper text initially (e.g., "Enter 6-digit code"); when error appears, append error message while preserving helper text (e.g., "Verification failed. Check and enter the correct code. Enter 6-digit code.").
5. Announce "Digit 1 of 6", "Digit 2 of 6", etc., as focus moves between boxes using `aria-label` or visual labels read by screen readers.

---

### Touch & Mobile

1. Provide touch targets **≥48×48px** for each digit box with spacing **≥8px** between adjacent boxes.
2. Trigger numeric keyboard using `inputmode="numeric"` on each input element; ensure `type="text"` to allow paste and SMS autofill.
3. Support paste gesture via long-press context menu; distribute pasted digits across all boxes automatically (e.g., pasting "123456" fills all six boxes in sequence).
4. Support both portrait and landscape orientations; ensure digit boxes remain visible and accessible without horizontal scroll at 100% zoom.

---

### Visual Accessibility

1. Ensure text contrast **≥4.5:1** for digit characters and helper/error text; large text (helper) requires **≥3:1**.
2. Ensure focus indicators and digit box borders have contrast **≥3:1** against the background.
3. Use both color and text to convey error state; apply red border + "Verification failed" message (do not rely on color alone).
4. Support text resizing up to **200%** without loss of content or functionality; digit boxes must reflow without horizontal scroll.
5. Respect `prefers-reduced-motion`; avoid animated transitions for focus movement or error appearance.

---

### Error Handling

1. Apply `aria-invalid="true"` to all digit input boxes when the error state is active (Error = True).
2. Link error text to the input group using `aria-describedby` with a stable ID (e.g., `id="pin-code-error"`); include both helper and error text IDs in `aria-describedby` (e.g., `aria-describedby="pin-code-helper pin-code-error"`).
3. Announce error message via `aria-live="assertive"` immediately upon failed submission; return focus to the first digit box for correction.
4. Display specific error messages: "Please enter the verification code." (empty case) or "Verification failed. Check and enter the correct code." (incorrect case).
5. Remove error state (reset `aria-invalid="false"` and clear error text) upon successful resubmission; announce success via `aria-live="polite"` (e.g., "Code verified successfully.").

---

### Testing Checklist

**Quick Tests (≤5 minutes)**

1. Keyboard-only: `Tab` into first box, type digits with auto-advance, use `Backspace` to correct, and submit; verify visible focus indicator ≥2px with ≥3:1 contrast.
2. Screen reader announces "Enter 6-digit verification code" on focus; error message "Verification failed. Check and enter the correct code." reads immediately after failed submission.
3. Zoom to **200%**: digit boxes reflow without horizontal scroll; spacing and focus indicators remain perceivable.
4. High-contrast/dark mode: focus indicators and error state remain visible with ≥3:1 contrast; red border alone is not the only error cue.
5. On a touch device: paste 6-digit code from SMS via long-press; verify numeric keyboard opens and all boxes populate correctly.

**Common Issues to Avoid**

1. Missing `aria-invalid="true"` on digit boxes when error state is active.
2. Replacing helper text entirely with error message (both must remain visible simultaneously).
3. Focus indicators with insufficient contrast (<3:1) against the background.
4. Blocking paste or failing to distribute pasted digits across all boxes.
5. Individual digit validation errors instead of unified group-level error state.