### Screen Reader Experience

1. Use `<input type="text" inputmode="numeric">` for each digit field with `maxlength="1"` to accept single numeric characters.
2. Provide a group label using `role="group"` with `aria-labelledby` referencing a label like "Enter 6-digit verification code."
3. Link helper text to the input group using `aria-describedby` so context is announced when focus enters the group.
4. Apply `aria-invalid="true"` to all digit fields when in error state and link error message via `aria-describedby`.
5. Announce error messages immediately using `aria-live="assertive"` when validation fails, stating the specific issue and retry instructions.