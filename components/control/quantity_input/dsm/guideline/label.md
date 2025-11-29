Describes the purpose of the input. Why hide a quantity input label?
In some UI contexts, especially when space is limited or when the input is part of a compact layout (search bars, filters, inline forms), visually hiding the label can help maintain a clean and uncluttered interface.
However, hiding the label should only be done if:
• The purpose of the input remains clear thanks to a placeholder or contextual icon.
• The label is still accessible to screen readers (using aria-label, aria-labelledby, or visually hidden text).

Hiding a label is a design choice that must balance visual simplicity and clarity of intent, without compromising inclusiveness or form guidance.

### Do & don'ts

✅ **Do:** Always provide a programmatic label using `<label>`, `aria-label`, or `aria-labelledby`  
❌ **Don't:** Rely solely on placeholder text as a label substitute—it disappears when users type

✅ **Do:** Use visually hidden labels (CSS technique) when visual context makes the purpose obvious  
❌ **Don't:** Remove labels entirely from the DOM, breaking accessibility for screen reader users

✅ **Do:** Keep labels concise and descriptive: "Quantity" or "Number of guests" rather than lengthy instructions  
❌ **Don't:** Use vague labels like "Enter value" that don't clarify what the number represents

✅ **Do:** Position visible labels consistently—typically above the input or inline to its left  
❌ **Don't:** Place labels in unexpected positions that break users' scanning patterns

✅ **Do:** Include context in the label when multiple quantity inputs appear together (e.g., "Adults," "Children")  
❌ **Don't:** Use identical generic labels for multiple inputs, forcing users to infer meaning from position alone