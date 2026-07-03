The Error status indicates that the user input does not meet validation rules or expected formatting. It provides immediate visual feedback, typically through a red border, error icon, and a clear, accessible error message positioned below the input (mandatory).

This state helps users quickly identify and correct mistakes by explaining what went wrong and, when possible, how to fix it.

The input remains editable, encouraging users to revise their input without starting over.

In the context of the select field, if the user has correctly selected a value but an error message still appears, it often means that: the option has been deleted, blocked, or is invalid / the option does not comply with a business rule / the option is incompatible with the user's profile / the option is obsolete or expired / inconsistency with another value in the form / too many choices, limit exceeded / server issue or value rejected on the backend.

**⚠️ Error message vs helper text / link**

The error message is not the same element as the helper text, it is independent. If a helper text accompanies the text input, it is replaced by the error message. The helper text must not be displayed simultaneously. However, a helper link must not be replaced and should remain positioned below the error message.
