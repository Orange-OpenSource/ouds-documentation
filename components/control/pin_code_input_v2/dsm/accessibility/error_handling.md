### Error Handling

1. Apply `aria-invalid="true"` to all digit fields when the code fails validation.
2. Link the error message to all digit fields using `aria-describedby` with a stable ID for the error text container.
3. Announce errors via `aria-live="assertive"` immediately after validation, describing the specific issue (e.g., "Invalid code" or "Code expired").
4. Return focus to the first digit field after error announcement so users can immediately retry.
5. Clear `aria-invalid` and hide error messages once the user begins entering a new code.