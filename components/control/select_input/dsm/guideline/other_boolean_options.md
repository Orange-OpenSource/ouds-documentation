**`Helper text`** Supporting text conveys additional information about the input field, such as how it will be used. It should ideally only take up a single line, though may wrap to multiple lines if required, and be either persistently visible or visible only on focus.

**`Helper link`** If the helper text is not sufficient (It can also be displayed on its own without helper text), it's possible to offer the user an additional help link (the link can be external or open a modal).

### Do & don'ts

✅ **Do:** Use helper text to provide essential context that helps users understand what to select or why

❌ **Don't:** Repeat information already stated in the label; helper text should add new, valuable guidance

✅ **Do:** Keep helper text concise (one sentence) to maintain readability and reduce cognitive load

❌ **Don't:** Use helper text for critical instructions that users might miss; include essential information in labels

✅ **Do:** Position helper text consistently between the input and any error messages in the vertical stack

❌ **Don't:** Hide helper text on focus or interaction when users may need it most

✅ **Do:** Use helper links when additional explanation is needed without cluttering the form interface

❌ **Don't:** Open helper links in new tabs without warning, as it disrupts the user's workflow

✅ **Do:** Ensure helper text is programmatically associated with the input using `aria-describedby`

❌ **Don't:** Style helper links identically to regular text, making them invisible to users who need extra guidance

✅ **Do:** Write helper text in plain language that all users can understand regardless of technical expertise

❌ **Don't:** Use helper text as a substitute for proper field labeling or clear option descriptions