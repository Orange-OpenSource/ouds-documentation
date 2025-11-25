Describes the purpose of the input. Why hide a text area label?

In some UI contexts, especially when space is limited or when the input is part of a compact layout (search bars, filters, inline forms), visually hiding the label can help maintain a clean and uncluttered interface.

However, hiding the label should only be done if:
• The purpose of the input remains clear thanks to a placeholder or contextual icon.
• The label is still accessible to screen readers (using aria-label, aria-labelledby, or visually hidden text).

Hiding a label is a design choice that must balance visual simplicity and clarity of intent, without compromising inclusiveness or form guidance.

**Do & don'ts**

✅ **Do:** Always provide a label for every text area, making it visible by default for maximum accessibility and usability

❌ **Don't:** Hide labels unless there's a compelling reason and you can guarantee the purpose remains absolutely clear to all users

✅ **Do:** Position labels above text areas rather than to the side, as top-aligned labels work better with longer text and responsive layouts

❌ **Don't:** Use placeholder text as a substitute for labels, as placeholders are not accessible to all users and disappear during interaction

✅ **Do:** Keep labels short, direct, and written in sentence case without punctuation at the end

❌ **Don't:** Use vague labels like "Comments" when more specific labels like "Additional details about your request" would be clearer

✅ **Do:** When hiding labels visually, ensure they remain accessible using `aria-label`, `aria-labelledby`, or visually-hidden CSS techniques

❌ **Don't:** Rely solely on icons or context to convey the purpose of a text area without providing an accessible label

✅ **Do:** Align labels consistently across your form to create a predictable and scannable layout

❌ **Don't:** Add colons or other punctuation after labels, as modern design systems favor cleaner label presentation

✅ **Do:** Ensure labels are visually and programmatically associated with their corresponding text areas

❌ **Don't:** Place labels far from their text areas, as this makes forms harder to complete and increases cognitive load