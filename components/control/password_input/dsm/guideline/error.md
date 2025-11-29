The Error status indicates that the user input does not meet validation rules or expected formatting. It provides immediate visual feedback, typically through a red border, error icon, and a clear, accessible error message positioned below the input (mandatory).

This state helps users quickly identify and correct mistakes by explaining what went wrong and, when possible, how to fix it. The input remains editable, encouraging users to revise their input without starting over.

**Error message vs helper text** The error message is not the same element as the helper text, it is independent. If a helper text accompanies the text input, it is replaced by the error message. The helper text must not be displayed simultaneously.

### Do & don'ts

✅ **Do:** Write error messages that specifically explain what went wrong and provide actionable guidance on how to fix it.  
❌ **Don't:** Use generic error messages like "Invalid input" that leave users guessing about the actual problem.

✅ **Do:** Associate error messages programmatically with the input using `aria-describedby` so screen readers announce them.  
❌ **Don't:** Display error messages only through color changes—always include text descriptions for accessibility.

✅ **Do:** Show error validation inline and in real-time where appropriate to help users correct mistakes before submission.  
❌ **Don't:** Wait until form submission to reveal all errors, creating frustrating back-and-forth correction cycles.

✅ **Do:** Maintain the error state until the user has successfully corrected the input and it passes validation.  
❌ **Don't:** Clear error states automatically on focus or blur without verifying the input now meets requirements.

✅ **Do:** Use error iconography consistently alongside text to provide redundant visual cues beyond color alone.  
❌ **Don't:** Display both helper text and error message simultaneously—replace helper text with the error message.