✅ **Do:** Validate checkbox selections on form submission, not when the user moves away from the field.
❌ **Don't:** Use inline validation on blur—wait until the user attempts to proceed.

✅ **Do:** Communicate errors through multiple channels—color, icon, and descriptive text message.
❌ **Don't:** Rely solely on color to indicate errors as this fails accessibility requirements.

✅ **Do:** Use `aria-describedby` to associate error messages with checkboxes for screen reader users.
❌ **Don't:** Disable the submit button when checkboxes are incomplete—show validation errors instead.

✅ **Do:** Provide specific, actionable error messages like "Select if you agree to the terms of service."
❌ **Don't:** Use vague messages like "This field is required" without explaining what action is needed.

✅ **Do:** Add visually hidden "Error:" prefix before error messages for screen reader announcement.
❌ **Don't:** Use native HTML5 validation—implement custom validation with `novalidate` on form elements.