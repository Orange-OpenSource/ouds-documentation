**`False`** The input is in a standard state, with no validation issues. It is ready for users to fill out without errors.

**`True`** The input has detected a validation error. An error message provides guidance to the user about what needs to be corrected. Error handling can be done either when the user navigates away from the field (on blur) or upon submission (when the user submits the form).

### Do & don'ts

✅ **Do:** Provide specific, actionable error messages explaining exactly what needs correction (e.g., "Phone number must be 10 digits").  
❌ **Don't:** Display generic errors like "Invalid input" that don't help users understand the problem.

✅ **Do:** Validate on blur for immediate feedback while avoiding interruption during active typing.  
❌ **Don't:** Trigger validation errors while the user is still actively entering their phone number.

✅ **Do:** Use both color and iconography to indicate error state, never relying on color alone.  
❌ **Don't:** Use only red color to indicate errors—this fails users with color vision deficiencies.

✅ **Do:** Associate error messages programmatically with inputs using `aria-describedby` for screen readers.  
❌ **Don't:** Position error messages far from the input field where association is unclear.

✅ **Do:** Clear error state immediately when the user corrects the input and validation passes.  
❌ **Don't:** Retain error styling after the user has successfully corrected the issue.