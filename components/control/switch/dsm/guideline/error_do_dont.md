✅ **Do:** Display error messages directly below the switch with clear, actionable text explaining how to resolve the issue.  
❌ **Don't:** Use generic error messages like "Invalid selection" without specifying what the user should do.

✅ **Do:** Use a distinct error color (typically red) for the divider and icon to draw attention to the validation issue.  
❌ **Don't:** Rely solely on color to indicate errors—include an icon and text for accessibility.

✅ **Do:** Provide different error messages for selected and unselected states when the context requires clarification.  
❌ **Don't:** Show the same error message regardless of the switch state if the required action differs.

✅ **Do:** Associate error messages with the switch using `aria-describedby` for screen reader accessibility.  
❌ **Don't:** Position error messages far from the switch where users may not notice them.

✅ **Do:** Clear the error state immediately when the user corrects the issue by toggling the switch.  
❌ **Don't:** Require users to perform additional actions (like clicking a "validate" button) to clear error states.