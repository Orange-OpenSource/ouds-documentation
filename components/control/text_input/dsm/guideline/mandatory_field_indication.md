In standard use cases, such as an account creation form, where most fields are mandatory, it's advisable to indicate optional fields rather than adding an asterisk (*) to every mandatory field. This reduces visual clutter while maintaining clarity.

However, in forms with a balanced mix or where mandatory fields are less common, it's preferable to explicitly mark required fields with an asterisk. In such cases, a clear and accessible indication must be placed at the top of the form to inform users (e.g., "All fields marked with an * are mandatory"). This indication should be:
• Accessible to screen readers (e.g., using visually hidden text or aria-describedby).
• Visually positioned near the form's heading or in a notice zone (banner).
• Semantically tied to the form using a role="status" or aria-live region to be announced on load or when dynamic fields appear.
