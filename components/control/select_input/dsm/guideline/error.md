An error is used to provide real-time feedback when the select input is in an invalid state:

**Examples of invalid states:**
• Required field left empty
• Incorrect value format (invalid email, phone number, postal code)
• Value that does not meet the established criteria (password not secure enough, text too short or too long)

**Accessibility for error indication:**
• Color alone is not sufficient: WCAG requires that color not be the only means of conveying information. Therefore, an icon and explicit text must accompany the error color.
• Assistive technologies need contextual error messages: when a user submits a form or leaves a field, screen readers need to receive clear textual information about the error. Use the aria-describedby attribute to associate error messages with the corresponding select input element.
• Error text is not just an ornament: WCAG guidelines require that error messages be sufficiently precise and descriptive.

**`False`** The select input is in its neutral or valid state.

**`True`** The user sees an error message detailing the nature of the problem, and the component is visually marked (e.g., with a specific color or icon) to draw attention to the error.

### Do & don'ts

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