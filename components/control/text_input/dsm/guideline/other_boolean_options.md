**`Autocompletion`** Provides suggested values as the user types. Displays inline text predictions within the input field and/or a dropdown menu of predictive options to speed up input and reduce errors.

**`Prefix`** A visual or textual element placed before the user's input. Commonly used to indicate expected formatting like a country code, a unit...

**`Suffix`** An element placed after the user's input, often used to display a currency or a unit (kg, %, cm…).

**`Helper text`** Supporting text conveys additional information about the input field, such as how it will be used. It should ideally only take up a single line, though may wrap to multiple lines if required, and be either persistently visible or visible only on focus.

**`Helper link`** If the helper text is not sufficient (It can also be displayed on its own without helper text), it's possible to offer the user an additional help link (the link can be external or open a modal).

### Do & don'ts

✅ **Do:** Use prefixes and suffixes to clarify expected format (€, kg, %) rather than relying on helper text alone.  
❌ **Don't:** Validate against users entering the prefix/suffix themselves—be forgiving if they duplicate it.

✅ **Do:** Keep helper text concise (ideally one line) and use full sentences with punctuation when appropriate.  
❌ **Don't:** Duplicate information already conveyed by the label or placeholder in helper text.

✅ **Do:** Use autocomplete to speed up input for predictable data like addresses, names, or common values.  
❌ **Don't:** Enable autocomplete for sensitive fields where suggestions could expose private information.

✅ **Do:** Make helper links visually distinct and clearly actionable, opening additional guidance when needed.  
❌ **Don't:** Hide essential information behind helper links—critical instructions should be immediately visible.

✅ **Do:** Mark prefixes and suffixes with `aria-hidden="true"` if they're purely decorative and don't need to be announced.  
❌ **Don't:** Add so many optional elements that the input becomes visually cluttered and overwhelming.