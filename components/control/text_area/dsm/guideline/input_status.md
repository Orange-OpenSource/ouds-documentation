**`Empty`** The Empty state indicates that the text area is blank with no content or placeholder, a neutral starting point.

**`Empty (Placeholder)`** The Empty with Placeholder state provides a hint or guidance inside the field to suggest expected input.

**`Filled`** The Filled state shows that the user has entered valid content into the field, replacing any placeholder.

**Do & don'ts**

✅ **Do:** Provide clear placeholder text that demonstrates the expected format or gives a concrete example

❌ **Don't:** Use placeholder text as a replacement for labels, as it disappears when users begin typing

✅ **Do:** Keep placeholder text concise and specific to help users understand what to enter without overwhelming them

❌ **Don't:** Leave text areas in the empty state without any guidance if the expected input isn't immediately obvious

✅ **Do:** Ensure placeholder text has sufficient contrast (at least 4.5:1) while still being distinguishable from entered text

❌ **Don't:** Include critical instructions only in placeholder text, as it's not accessible to all users and disappears during interaction

✅ **Do:** Use the filled state to provide clear visual feedback that user input has been successfully captured

❌ **Don't:** Rely solely on filled state to indicate valid input; combine with other feedback mechanisms for complex validation

✅ **Do:** Consider progressive disclosure where empty fields show just enough information to get started

❌ **Don't:** Make placeholder text so verbose that it becomes distracting or reduces the perceived simplicity of the form