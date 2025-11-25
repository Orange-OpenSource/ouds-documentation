The Error status indicates that the user input does not meet validation rules, for example, in this specific case, if the number of characters entered by the user exceeds the allowed limit. It provides immediate visual feedback, typically through a red border, error icon, and a clear, accessible error message positioned below the input (mandatory).

This state helps users quickly identify and correct mistakes by explaining what went wrong and, when possible, how to fix it. The input remains editable, encouraging users to revise their input without starting over.

**⚠️ Error message vs helper text / link** If a helper text accompanies the text input, it is replaced by the error message. However, a helper link must not be replaced and should remain positioned below the error message.

**Do & don'ts**

✅ **Do:** Display error messages immediately adjacent to the text area with clear visual indicators like red borders and error icons

❌ **Don't:** Show errors while users are still typing; wait for field blur or form submission to avoid premature interruption

✅ **Do:** Write error messages that explain what went wrong and provide specific guidance on how to fix it

❌ **Don't:** Use technical jargon or error codes in messages; keep language plain and user-friendly

✅ **Do:** Ensure error messages are programmatically associated with the text area using `aria-describedby` for screen reader accessibility

❌ **Don't:** Disable or remove the text area when displaying errors; users must be able to correct their input

✅ **Do:** Combine visual error indicators (color, icons) with text to support users who cannot perceive color alone

❌ **Don't:** Replace helper text permanently with error messages; restore helper text when the error is resolved

✅ **Do:** Keep error messages concise and actionable, focusing on what users need to do next

❌ **Don't:** Display multiple error messages simultaneously if they can be consolidated into a single, clear instruction

✅ **Do:** Maintain error states until users have successfully corrected the input and validation passes

❌ **Don't:** Clear error messages prematurely before users have had a chance to address the issue