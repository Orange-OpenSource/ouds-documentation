### Screen Reader Experience

1. Use semantic `<input type="text" inputmode="numeric">` elements for each digit field with `maxlength="1"`.
2. Provide a group label using `role="group"` with `aria-labelledby` pointing to the main label text (e.g., "Enter 6-digit verification code").
3. Announce the field position and total count using `aria-label` on each input (e.g., "Digit 1 of 6", "Digit 2 of 6").
4. Apply `aria-invalid="true"` to all input fields when in error state and link error message using `aria-describedby`.
5. Announce error messages immediately using `aria-live="assertive"` and provide specific feedback about what went wrong (incorrect code, expired, attempts exceeded).
6. Announce successful code entry using `aria-live="polite"` when validation passes and next action is available.