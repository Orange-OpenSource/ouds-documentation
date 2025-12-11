The close (dismiss) button controls whether a user can remove the alert message from view.
Depending on the purpose of the alert, it may either be dismissible (True) or persistent (False).
Some alerts must remain visible to ensure users are aware of important information; others can be closed to reduce visual clutter.

**`False`** The alert does not include a close button, and therefore remains visible until the context changes (e.g., the issue is resolved, the page is refreshed, or the user completes a related task).
Example:
• The message is critical or mandatory (e.g., service disruption, required action) and must not be ignored.
• The alert reflects a state that the user must see for the duration of a task or journey. (A network outage notification that remains until connectivity is restored.)

**`True`** The alert includes a close button, allowing the user to dismiss it when they have acknowledged the message.
Example:
• The message is informational and does not require further action from the user.
• Allowing dismissal improves UX by reducing persistent visual noise.
For example, a tip "New feature launched" that the user may choose to hide.
Not all informational alerts must have close buttons, but this offers user control when appropriate.