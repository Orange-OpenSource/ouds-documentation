The Error status indicates that the user input does not meet validation rules or expected formatting. It provides immediate visual feedback, typically through a red border, error icon, and a clear, accessible error message positioned below the input (mandatory).

This state helps users quickly identify and correct mistakes by explaining what went wrong and, when possible, how to fix it. The input remains editable, encouraging users to revise their input without starting over.

**⚠️ Error message vs helper text / link** The error message is not the same element as the helper text, it is independent. If a helper text accompanies the text input, it is replaced by the error message. The helper text must not be displayed simultaneously. However, a helper link must not be replaced and should remain positioned below the error message.

### Do & don'ts

✅ **Do:** Write specific, actionable error messages that tell users exactly what went wrong and how to fix it.  
❌ **Don't:** Use generic error messages like "Invalid input" or "Error"—they don't help users understand the problem.

✅ **Do:** Use multiple visual cues for errors (color, icon, border, text) to support users who may not perceive color alone.  
❌ **Don't:** Rely solely on red color to indicate errors—colorblind users may miss the feedback entirely.

✅ **Do:** Associate error messages programmatically with inputs using `aria-describedby` for screen reader accessibility.  
❌ **Don't:** Display error messages in locations disconnected from the input field, making the association unclear.

✅ **Do:** Validate after form submission or when the user leaves the field—avoid interrupting users mid-typing.  
❌ **Don't:** Show errors while users are still typing, which can be disruptive and frustrating.

✅ **Do:** Phrase errors as helpful instructions (e.g., "Enter an email address") rather than accusations ("You entered invalid data").  
❌ **Don't:** Use technical jargon or codes in error messages—speak in user-friendly language.