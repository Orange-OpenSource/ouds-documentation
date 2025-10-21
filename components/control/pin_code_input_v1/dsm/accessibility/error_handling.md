## Error Handling

1. Apply `aria-invalid="true"` to all digit inputs when validation fails.
2. Link error text to inputs using `aria-describedby` with a stable error message ID.
3. Announce errors via `aria-live="polite"` immediately after form submission with validation failure.
4. Provide specific error messages: "Please enter the verification code" (empty) or "Verification failed. Check and enter the correct code" (incorrect).
5. Return focus to the first digit box after error announcement to enable immediate correction.
6. Remove `aria-invalid="false"` and clear error messages when user begins re-entry or validation succeeds.
7. Maintain helper text visibility even when error state is active; stack error message below helper text.