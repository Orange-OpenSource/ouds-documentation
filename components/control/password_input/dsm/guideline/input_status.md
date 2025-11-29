**`Empty`** The Empty state indicates that the password input is blank with no content or placeholder, a neutral starting point.

**`Empty (Placeholder)`** The Empty with Placeholder state provides a hint or guidance inside the field to suggest expected input.

**`Filled`** The Filled state shows that the user has entered valid content into the field, replacing any placeholder.

### Do & don'ts

✅ **Do:** Use placeholder text sparingly and only for supplementary hints—never as a replacement for visible labels.  
❌ **Don't:** Put essential information like password requirements in placeholder text as it disappears once users start typing.

✅ **Do:** Ensure placeholder text has sufficient contrast (4.5:1 minimum) against the input background for readability.  
❌ **Don't:** Use placeholder text that could be mistaken for actual input, such as sample passwords or realistic credential formats.

✅ **Do:** Provide clear visual distinction between empty, placeholder, and filled states through typography weight or color changes.  
❌ **Don't:** Rely solely on placeholder presence to indicate whether a field has been interacted with—use proper state management.

✅ **Do:** Consider keeping helper text visible outside the input rather than using placeholders for password format guidance.  
❌ **Don't:** Use overly long placeholder text that gets truncated and loses meaning on smaller viewports.

✅ **Do:** Test that the filled state visually masks characters appropriately while maintaining consistent input height.  
❌ **Don't:** Allow the input to resize or shift layout when transitioning between empty and filled states.