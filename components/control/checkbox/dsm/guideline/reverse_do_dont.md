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