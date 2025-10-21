### Screen Reader Experience

1. Use semantic `<input type="text" inputmode="numeric">` elements for each digit box; group all boxes in a `<fieldset>` or `role="group"` with an accessible label (e.g., "Enter 6-digit verification code").
2. Provide `aria-label` or `aria-labelledby` on the group describing the purpose (e.g., "PIN code input, 6 digits required").
3. Apply `aria-invalid="true"` and `aria-describedby` linking to helper/error text when validation fails; announce error via `aria-live="assertive"` immediately upon submission failure.
4. Announce digit count in helper text initially (e.g., "Enter 6-digit code"); when error appears, append error message while preserving helper text (e.g., "Verification failed. Check and enter the correct code. Enter 6-digit code.").
5. Announce "Digit 1 of 6", "Digit 2 of 6", etc., as focus moves between boxes using `aria-label` or visual labels read by screen readers.