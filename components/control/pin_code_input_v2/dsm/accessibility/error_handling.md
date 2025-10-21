### Error Handling

1. Apply `aria-invalid="true"` to all digit boxes when the error state is active (submission with incomplete or incorrect entry).
2. Link error text to the group using `aria-describedby` with a stable ID (e.g., `id="pin-error"`); ensure each box references this ID.
3. Announce error messages immediately upon submission using `aria-live="assertive"`; message content must match displayed text.
4. Provide specific error messages: "Please enter the verification code." (empty case) or "Verification failed. Check and enter the correct code." (incorrect case).
5. Upon successful resubmission, remove `aria-invalid` and announce success with `aria-live="polite"` (e.g., "Code accepted"); return focus to the next logical element or first digit box for retry.