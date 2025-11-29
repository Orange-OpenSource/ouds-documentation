**Dial code** When enabled, it is possible to display the country dial code value. The dial code is read-only and cannot be edited directly by the user.

**Helper text** When enabled, a helper text appears below the input field to provide additional context or tips on how to fill out the field. Useful for offering suggestions or clarifying expected input formats (e.g., "Please enter a phone number in international format").

### Do & don'ts

✅ **Do:** Display the dial code as clearly non-editable with visual distinction from the input area.  
❌ **Don't:** Allow users to accidentally select or attempt to edit the dial code prefix.

✅ **Do:** Use helper text to clarify format expectations before errors occur.  
❌ **Don't:** Display helper text that duplicates information already visible in the placeholder.

✅ **Do:** Keep helper text brief—one line maximum—to avoid overwhelming the form layout.  
❌ **Don't:** Use helper text for critical instructions that should be in the label.

✅ **Do:** Ensure helper text meets minimum contrast requirements (4.5:1 for normal text).  
❌ **Don't:** Use very light gray helper text that becomes illegible for users with low vision.

✅ **Do:** Replace helper text with error messages when validation fails, then restore after correction.  
❌ **Don't:** Display both helper text and error messages simultaneously, creating visual clutter.