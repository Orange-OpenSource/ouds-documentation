### Error Handling

1. Apply `aria-invalid="true"` to all input fields in the group when the complete code fails validation.
2. Link the error message to all inputs using `aria-describedby` with a stable ID referencing the error text element.
3. Announce errors immediately via `aria-live="assertive"` after validation fails and return focus to the first input field for correction.
4. Provide specific, actionable error messages: "Incorrect code. Please try again" or "Code expired. Request a new code" instead of generic "Error".
5. Announce success state using `aria-live="polite"` when the correct code is entered and describe the next step in the flow.
6. Clear all fields or maintain entered values based on security requirements when displaying errors; document this behavior clearly.