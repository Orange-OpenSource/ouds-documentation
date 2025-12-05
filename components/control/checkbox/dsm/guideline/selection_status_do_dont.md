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