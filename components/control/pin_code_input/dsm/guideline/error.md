The Error status indicates that the user input does not meet validation rules or expected formatting. It provides immediate visual feedback, typically through a red border, error icon, and a clear, accessible error message positioned below the input (mandatory).

This state helps users quickly identify and correct mistakes by explaining what went wrong and, when possible, how to fix it.
The input remains editable, encouraging users to revise their input without starting over.

The error state must be triggered by an explicit validation (submission, API response), and not in real time with each keystroke. This can occur either because the entered code does not match the expected code, because the user entered an expired or already used code, or finally if the maximum number of attempts has been exceeded.

**Alert:** In the context of a PIN code input, in addition to the input's "Error" UI rendering, it is essential to also include an "Alert" component (also in its "Error" status) in the interface.

### Do & don'ts

✅ **Do:** Display error messages only after explicit validation (form submission or API response), not during typing.  
❌ **Don't:** Show real-time error feedback on each keystroke, as this creates anxiety and interrupts the user's flow.

✅ **Do:** Provide specific, actionable error messages explaining what went wrong (e.g., "Incorrect code" or "Code expired").  
❌ **Don't:** Use vague error messages like "Error" or "Invalid input" that don't help users understand the problem.

✅ **Do:** Keep the input editable in error state so users can correct their entry without clearing all fields.  
❌ **Don't:** Clear all entered digits when an error occurs, forcing users to re-enter the entire code.

✅ **Do:** Use the Alert component in conjunction with the input's error state for important security messages.  
❌ **Don't:** Rely solely on the input field's visual error state without providing an accompanying error message.

✅ **Do:** Indicate remaining attempts clearly when account lockout is imminent (e.g., "2 attempts remaining").  
❌ **Don't:** Lock users out without warning or without providing clear recovery options after exceeding attempt limits.