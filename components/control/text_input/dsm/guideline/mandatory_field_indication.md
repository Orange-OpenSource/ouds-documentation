In standard use cases, such as an account creation form, where most fields are mandatory, it's advisable to indicate optional fields rather than adding an asterisk (*) to every mandatory field. This reduces visual clutter while maintaining clarity.

However, in forms with a balanced mix or where mandatory fields are less common, it's preferable to explicitly mark required fields with an asterisk. In such cases, a clear and accessible indication must be placed at the top of the form to inform users (e.g., "All fields marked with an * are mandatory"). This indication should be:
• Accessible to screen readers (e.g., using visually hidden text or aria-describedby).
• Visually positioned near the form's heading or in a notice zone (banner).
• Semantically tied to the form using a role="status" or aria-live region to be announced on load or when dynamic fields appear.

### Do & don'ts

✅ **Do:** Choose one pattern consistently—either mark optional fields or required fields, not both.  
❌ **Don't:** Mark every field with an asterisk when most fields are required—mark the exceptions instead.

✅ **Do:** Include a legend at the top of forms explaining what the asterisk (*) means if you use one.  
❌ **Don't:** Assume users understand that asterisks indicate required fields without an explanation.

✅ **Do:** Use the HTML `required` attribute to enable native browser validation and assistive technology support.  
❌ **Don't:** Rely solely on visual asterisks—ensure required status is programmatically communicated.

✅ **Do:** Consider your form's majority case: mark the minority (optional fields in required-heavy forms, or vice versa).  
❌ **Don't:** Use color alone to distinguish required from optional fields—provide text or symbol indicators.

✅ **Do:** Test your required field indication with screen readers to ensure it's properly announced.  
❌ **Don't:** Add "(required)" labels that duplicate information already conveyed by asterisks and legends.