Describes the purpose of the input. Why hide a password input label?

In some UI contexts, especially when space is limited or when the input is part of a compact layout (search bars, filters, inline forms), visually hiding the label can help maintain a clean and uncluttered interface.

However, hiding the label should only be done if:
• The purpose of the input remains clear thanks to a placeholder or contextual icon.
• The label is still accessible to screen readers (using aria-label, aria-labelledby, or visually hidden text).

Hiding a label is a design choice that must balance visual simplicity and clarity of intent, without compromising inclusiveness or form guidance.

### Do & don'ts

✅ **Do:** Always provide a programmatically associated label for every password input, even when visually hidden.  
❌ **Don't:** Omit labels entirely—screen reader users depend on them to understand the field's purpose.

✅ **Do:** Use visually hidden CSS techniques (`.sr-only`) to maintain accessibility when hiding labels for visual design reasons.  
❌ **Don't:** Use `display: none` or `visibility: hidden` to hide labels as these remove them from the accessibility tree.

✅ **Do:** Write labels that clearly describe the expected input, such as "Password" or "Current password" for clarity.  
❌ **Don't:** Use vague labels like "Enter here" or overly technical labels that don't help users understand what's required.

✅ **Do:** Position visible labels consistently above or beside inputs according to your design system's established patterns.  
❌ **Don't:** Hide labels in contexts where users might not understand the field's purpose from context alone.

✅ **Do:** Ensure labels remain visible in error states to help users understand which field requires attention.  
❌ **Don't:** Rely on placeholder text as a label substitute—placeholders disappear when users begin typing.