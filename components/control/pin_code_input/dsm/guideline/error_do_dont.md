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