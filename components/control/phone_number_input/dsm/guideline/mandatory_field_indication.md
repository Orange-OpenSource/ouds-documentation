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

✅ **Do:** Mark optional fields with "(optional)" rather than marking every required field with asterisks.  
❌ **Don't:** Use asterisks without explaining their meaning—provide a legend at form start.

✅ **Do:** Announce "mandatory" or "required" to screen readers instead of the visual asterisk symbol.  
❌ **Don't:** Rely solely on visual asterisks for required field indication—use `aria-required="true"`.

✅ **Do:** Position the mandatory field explanation at the top of the form before users encounter fields.  
❌ **Don't:** Place required field explanations at the bottom of forms where users discover them too late.

✅ **Do:** Use consistent mandatory indication patterns across all forms in your application.  
❌ **Don't:** Mix different required field indication methods within the same form or application.

✅ **Do:** Consider marking optional fields instead when most fields are required—reduces visual noise.  
❌ **Don't:** Over-mark forms with asterisks when all fields are required—state this once at the top.