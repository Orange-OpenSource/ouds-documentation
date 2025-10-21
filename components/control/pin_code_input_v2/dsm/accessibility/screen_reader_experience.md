### Screen Reader Experience

1. Use `<input type="text" inputmode="numeric" maxlength="1">` for each digit box to enforce single-character numeric entry.
2. Label the entire group using `role="group"` with `aria-labelledby` pointing to a heading (e.g., "Enter 6-digit verification code").
3. Each digit box must have a programmatic label such as `aria-label="Digit 1 of 6"` to indicate position in the sequence.
4. Apply `aria-invalid="true"` to all digit boxes when the error state is active; link error text using `aria-describedby` with a stable ID.
5. Announce error messages immediately upon submission failure using `aria-live="assertive"`; announce success states with `aria-live="polite"`.
6. When focus auto-advances, screen readers announce the new box label (e.g., "Digit 2 of 6") without additional interruption.