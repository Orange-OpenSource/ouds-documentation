### Error

In the Error state, the quantity input displays a clear indication that the user has entered an invalid value or that the entered value does not meet the required constraints (e.g., exceeds maximum stock, falls below the minimum quantity, or contains non-numeric characters). Depending on the context, the error may be triggered in two scenarios: when the input is empty (no value entered yet) or when the input is filled (a value has been entered but is invalid).

**Empty state error:**
• Triggered when the input is required, but the user attempts to submit the form or proceed without entering a value.
• Use the ✏️ Error empty text property to display a custom error message such as "This field is required" or "Please enter a quantity."
• The focus is typically on encouraging the user to provide a value before proceeding.

**Filled state error:**
• Triggered when the user has entered a value that does not meet validation criteria, such as exceeding the maximum allowed quantity, falling below the minimum, or entering invalid characters (e.g., letters or special symbols).
• Use the ✏️ Error filled text property to display a specific error message such as "Quantity must be between 1 and 99" or "Only numeric values are allowed."
• The focus is on correcting the invalid input without erasing the user's entry immediately (unless necessary for real-time validation).

For both cases, the component should:
• Display the error message below the input field in a distinct color (typically red) to clearly indicate the issue.
• Highlight the input field with an error border or background color to draw the user's attention to the invalid state.
• Provide actionable and specific guidance to help the user correct the issue quickly (e.g., "Enter a number between 1 and 10").

Good error messages are concise, specific, and solution-oriented, helping users understand what went wrong and how to fix it.