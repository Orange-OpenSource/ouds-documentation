**If all fields are mandatory (several fields present):**
1. Display the message "All fields are mandatory." at the top.
2. Do not use an asterisk (*) at the end of each field label, nor the word "mandatory."
UI rendering of the asterisk: font-weight-bold + color-content-negative (red).

**If not all fields are mandatory (several fields present):**
1. Display the message "All fields marked with an * are mandatory." at the top.
2. Use an asterisk (*) at the end of each mandatory field label (the word "mandatory" is read aloud instead of the visible asterisk at the end of the label).
UI rendering of the asterisk: font-weight-bold + color-content-negative (red).
3. Use the mention "(optional)" at the end of each optional field label. Note that this rule is not systematic—it remains an option, to be used if needed.

**If there is only one field in the form, or if the mandatory nature is obvious (such as login/password), no mention is necessary since the fields are essential to the form's functionality.**

### Do & don'ts

✅ **Do:** Clearly indicate mandatory fields using a consistent pattern throughout the entire form or application

❌ **Don't:** Mix different mandatory field indicators (asterisks, labels, colors) inconsistently within the same interface

✅ **Do:** Place the asterisk immediately after the label text with no space, making the association clear

❌ **Don't:** Use asterisks without providing a legend explaining their meaning to users who may not understand the convention

✅ **Do:** Ensure screen readers announce "mandatory" or "required" when asterisks are present using `aria-required` or similar attributes

❌ **Don't:** Rely solely on red color to indicate mandatory fields, as color-blind users cannot perceive the distinction

✅ **Do:** Display a summary message at the form top explaining the mandatory field convention before users encounter fields

❌ **Don't:** Mark all fields as mandatory when some are truly optional, reducing trust and increasing abandonment

✅ **Do:** Use "(optional)" labels sparingly and only when the optionality needs emphasis for clarity

❌ **Don't:** Override WCAG guidance by making critical fields appear optional or hiding required field indicators

✅ **Do:** Test mandatory field patterns with users who rely on assistive technology to ensure clear communication

❌ **Don't:** Use mandatory field indicators on single-field forms where the requirement is obvious from context