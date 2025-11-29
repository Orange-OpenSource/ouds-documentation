The Error status indicates that the user input does not meet validation rules or expected formatting. It provides immediate visual feedback, typically through a red border, error icon, and a clear, accessible error message positioned below the input (mandatory).

This state helps users quickly identify and correct mistakes by explaining what went wrong and, when possible, how to fix it. The input remains editable, encouraging users to revise their input without starting over.

If the input is filled, an "error" status is triggered by the entry of a value that is too small, too large, or non-numeric.

**⚠️ Error message vs helper text** The error message is not the same element as the helper text, it is independent. If a helper text accompanies the text input, it is replaced by the error message. The helper text must not be displayed simultaneously.

### Do & don'ts

✅ **Do:** Position error messages directly below the input field with consistent spacing for easy scanning  
❌ **Don't:** Display error messages in tooltips or modals that obscure the input or disappear unexpectedly

✅ **Do:** Write specific, actionable error messages like "Quantity must be between 1 and 99"  
❌ **Don't:** Use generic messages like "Invalid input" that don't help users understand how to fix the issue

✅ **Do:** Replace helper text with error messages to avoid cognitive overload—one message at a time  
❌ **Don't:** Show both helper text and error messages simultaneously, creating visual clutter and confusion

✅ **Do:** Use `aria-invalid="true"` and `aria-errormessage` to programmatically associate errors with the input  
❌ **Don't:** Rely solely on color to communicate errors—ensure text and icons provide redundant cues

✅ **Do:** Allow users to continue editing the input while the error state is displayed  
❌ **Don't:** Disable the input in error state, preventing users from making corrections