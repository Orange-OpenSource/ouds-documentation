### Error Handling

1. Apply `aria-invalid="true"` to all digit input boxes when the error state is active (Error = True).
2. Link error text to the input group using `aria-describedby` with a stable ID (e.g., `id="pin-code-error"`); include both helper and error text IDs in `aria-describedby` (e.g., `aria-describedby="pin-code-helper pin-code-error"`).
3. Announce error message via `aria-live="assertive"` immediately upon failed submission; return focus to the first digit box for correction.
4. Display specific error messages: "Please enter the verification code." (empty case) or "Verification failed. Check and enter the correct code." (incorrect case).
5. Remove error state (reset `aria-invalid="false"` and clear error text) upon successful resubmission; announce success via `aria-live="polite"` (e.g., "Code verified successfully.").