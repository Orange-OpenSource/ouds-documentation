**`Empty`** The field is empty. The placeholder text is not visible: the label is displayed instead and remains visible when the user starts typing.

**`Empty (Placeholder)`** The field is empty. The placeholder text is displayed in lieu of the label as an additional way to provide a contextual hint.

**`Filled`** The field has been filled out by the user.

### Do & don'ts

✅ **Do:** Always display a visible label that persists when the user begins typing for accessibility compliance.  
❌ **Don't:** Rely solely on placeholder text as the only means of identifying the input's purpose.

✅ **Do:** Use placeholder text to show example formats like "06 12 34 56 78" only as supplementary guidance.  
❌ **Don't:** Use placeholder text that disappears as the only instruction for complex format requirements.

✅ **Do:** Ensure filled state maintains clear visual distinction from empty state for at-a-glance scanning.  
❌ **Don't:** Allow placeholder text color to pass as valid input text, confusing users about field completion.

✅ **Do:** Design empty state to clearly invite interaction with appropriate visual affordances.  
❌ **Don't:** Display placeholder text that could be mistaken for pre-filled user data.

✅ **Do:** Preserve user-entered data through page refreshes and navigation when appropriate.  
❌ **Don't:** Clear filled fields unexpectedly without user action or clear warning.