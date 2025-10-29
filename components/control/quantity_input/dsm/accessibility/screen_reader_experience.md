## Screen Reader Experience

1. Use semantic `<input type="number">` element with appropriate `role` if necessary (default role is sufficient).
2. Provide `aria-label` or `aria-labelledby` to associate the input with its visible label text.
3. Use `aria-describedby` to link the input to helper text and error messages with stable IDs.
4. Apply `aria-invalid="true"` when the input contains an invalid value and link error text via `aria-describedby`.
5. Announce value changes via `aria-live="polite"` when increment/decrement buttons are used, stating "Quantity set to [value]".
6. Ensure increment and decrement buttons have accessible names like "Increase quantity" and "Decrease quantity" via `aria-label`.
7. If min/max constraints exist, communicate them via `aria-valuemin`, `aria-valuemax`, and `aria-valuenow` attributes.
8. Group the input with its label and buttons using `role="group"` or `<fieldset>` with `<legend>` for complex layouts.
9. Ensure all state changes (enabled, disabled, read-only, error) are programmatically determinable via ARIA attributes.