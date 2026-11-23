# Checkbox — do & don't propositions

AI-generated propositions that no one has validated yet. They are not part of the documentation ([checkbox.md](checkbox.md)) and are not shown on zeroheight. Once a designer validates one, it moves into the full file.

## Selection status — do & don't

✅ **Do:** Use indeterminate state only for parent-child hierarchies where some children are selected.  
❌ **Don't:** Allow users to manually set a checkbox to indeterminate state—it should be system-calculated only.

✅ **Do:** Automatically update parent checkbox state when children change (all selected → checked, none → unchecked, some → indeterminate).  
❌ **Don't:** Pre-select checkboxes by default as this increases the chance users will miss the question.

✅ **Do:** Use `aria-checked="mixed"` for indeterminate state to communicate status to assistive technologies.  
❌ **Don't:** Treat indeterminate as a third value—it is presentational only and doesn't affect submitted data.

✅ **Do:** Order options logically—alphabetically, most-to-least common, or by workflow sequence.  
❌ **Don't:** Confuse users by mixing checkboxes and radio buttons in the same option group.

✅ **Do:** Add hint text like "Select all that apply" to clarify multiple selections are allowed.  
❌ **Don't:** Assume the visual difference between checkboxes and radios is obvious to all users.

## Error — do & don't

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

## Reverse — do & don't

✅ **Do:** Position checkboxes to the left of labels in LTR contexts for easier scanning and discovery.  
❌ **Don't:** Hardcode left/right positioning—use logical CSS properties that respond to text direction.

✅ **Do:** Use the reverse layout for RTL languages where checkbox should appear on the right side.  
❌ **Don't:** Mix checkbox positions (left and right of label) within the same interface or form.

✅ **Do:** Test checkbox groups thoroughly in RTL mode to verify proper label alignment and reading order.  
❌ **Don't:** Assume checkbox-to-label visual relationships will automatically reverse correctly.

✅ **Do:** Use logical properties like `marginStart` and `marginEnd` instead of physical `margin-left/right`.  
❌ **Don't:** Forget to verify indeterminate and error states display correctly in reverse/RTL layout.

✅ **Do:** Consider mobile use cases where reverse layout may improve thumb reachability on large screens.  
❌ **Don't:** Use reverse layout inconsistently—apply it systematically based on language direction or device context.

## Other boolean options — do & don't

✅ **Do:** Use description text to explain accepted values or provide additional context for complex options.  
❌ **Don't:** Include links within description text—screen readers may not announce them as interactive.

✅ **Do:** Keep descriptions to a single short sentence without full stops for scannability.  
❌ **Don't:** Truncate checkbox labels with ellipsis—allow text to wrap to a second line instead.

✅ **Do:** Use dividers to create logical groupings or implement "none of the above" exclusive options.  
❌ **Don't:** Overuse dividers—they should separate meaningful groups, not every individual option.

✅ **Do:** Use icons sparingly to reinforce label meaning when visual distinction adds genuine value.  
❌ **Don't:** Add icons purely for decoration—they should serve a clear communicative purpose.

✅ **Do:** Display error messages immediately below the affected checkbox using consistent positioning.  
❌ **Don't:** Hide error messages until form submission if real-time feedback would help users.
