Describes the purpose of the input. Why hide a phone number input label?

In some UI contexts, especially when space is limited or when the input is part of a compact layout (search bars, filters, inline forms), visually hiding the label can help maintain a clean and uncluttered interface.

However, hiding the label should only be done if:
• The purpose of the input remains clear thanks to a placeholder or contextual icon.
• The label is still accessible to screen readers (using aria-label, aria-labelledby, or visually hidden text).

Hiding a label is a design choice that must balance visual simplicity and clarity of intent, without compromising inclusiveness or form guidance.

### Do & don'ts

✅ **Do:** Always provide a programmatically associated label, even when visually hidden.  
❌ **Don't:** Remove labels entirely from the DOM—always include them for assistive technology.

✅ **Do:** Use the `<label>` element with `for` attribute pointing to the input's `id` for proper association.  
❌ **Don't:** Rely solely on `aria-label` when a visible label would benefit all users.

✅ **Do:** Keep labels concise and descriptive: "Phone number" or "Mobile phone" is sufficient.  
❌ **Don't:** Use overly verbose labels like "Please enter your telephone number here."

✅ **Do:** Position visible labels consistently—above the input is the most scannable placement.  
❌ **Don't:** Place labels inside the input as placeholder text that disappears on focus.

✅ **Do:** Consider all users before hiding labels—cognitive disabilities benefit from persistent visible labels.  
❌ **Don't:** Hide labels purely for aesthetic reasons without validating usability impact.