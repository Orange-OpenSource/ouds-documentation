✅ **Do:** Display error messages directly below the radio group with clear, actionable language like "Select an option"  
❌ **Don't:** Use generic error messages like "Invalid input" that don't explain what action is required

✅ **Do:** Use a distinct error color (typically red) for the indicator border and error message text  
❌ **Don't:** Rely solely on color to indicate errors—include text and icons for accessibility

✅ **Do:** Associate error messages programmatically with the radio group using `aria-describedby`  
❌ **Don't:** Place error messages far from the radio group where users may miss the connection

✅ **Do:** Clear error states immediately when the user makes a valid selection  
❌ **Don't:** Keep error indicators visible after the user has corrected the issue

✅ **Do:** Validate on blur or form submission rather than on every interaction to avoid premature errors  
❌ **Don't:** Show error states before the user has had a chance to interact with the radio group