✅ **Do:** Display error messages immediately below the select input, using clear language that explains how to fix the issue

❌ **Don't:** Rely on color alone to indicate errors; always include an icon and descriptive text for accessibility

✅ **Do:** Use `aria-describedby` to programmatically associate error messages with the select input for screen readers

❌ **Don't:** Show generic error messages like "Invalid selection" that don't help users understand what went wrong

✅ **Do:** Trigger validation after the user interacts with the field or attempts to submit the form, not while typing

❌ **Don't:** Display error states prematurely before users have had a chance to complete their selection

✅ **Do:** Ensure error icons have at least 3:1 contrast ratio and error text meets WCAG AA standards

❌ **Don't:** Hide error messages on focus or hover, preventing users from reading them while correcting mistakes

✅ **Do:** Provide specific guidance in error messages, such as "Please select a shipping method to continue"

❌ **Don't:** Use technical jargon or system codes in error messages that users cannot understand