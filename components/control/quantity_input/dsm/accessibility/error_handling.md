## Error Handling

1. Apply `aria-invalid="true"` to the input field when it contains an invalid value.
2. Link error messages to the input using `aria-describedby` with a stable, unique ID.
3. Announce errors immediately via `aria-live="assertive"` when validation fails, and return focus to the input field.
4. Provide specific, actionable error messages such as "Quantity must be between 1 and 99" instead of generic "Error" messages.
5. Announce success states when appropriate (e.g., "Quantity updated successfully") and describe next steps if needed.
6. Display error messages visually below the input in a distinct color (red) and with sufficient contrast.
7. Preserve user input when displaying errors; do not clear the field unless necessary for security or validation reasons.