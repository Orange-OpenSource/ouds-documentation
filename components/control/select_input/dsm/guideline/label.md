Describes the purpose of the input. Why hide a select input label?
In some UI contexts, especially when space is limited or when the input is part of a compact layout (filters, inline forms), visually hiding the label can help maintain a clean and uncluttered interface.
However, hiding the label should only be done if:
• The purpose of the input remains clear thanks to a contextual icon.
• The label is still accessible to screen readers (using aria-label, aria-labelledby, or visually hidden text).

Hiding a label is a design choice that must balance visual simplicity and clarity of intent, without compromising inclusiveness or form guidance.

### Do & don'ts

✅ **Do:** Always provide a label for every select input, either visibly or through `aria-label` for accessibility

❌ **Don't:** Hide labels visually without ensuring screen readers can still access label text

✅ **Do:** Write clear, concise labels that precisely describe what users should select (e.g., "Delivery method")

❌ **Don't:** Use vague labels like "Choose option" that don't indicate what type of selection is required

✅ **Do:** Position labels directly above or to the left of select inputs following standard form layout patterns

❌ **Don't:** Place labels far from their inputs, making it difficult for users to associate them

✅ **Do:** Keep labels short (3-5 words) to maintain scanability and reduce cognitive load

❌ **Don't:** Write labels as full sentences or questions when a brief phrase is sufficient

✅ **Do:** Use sentence case for labels (e.g., "Country of residence") rather than title case or all caps

❌ **Don't:** Include colons after labels; modern design patterns favor clean label text without punctuation

✅ **Do:** Ensure visually hidden labels still provide complete context for screen reader users

❌ **Don't:** Assume placeholder text can replace proper labels, as placeholders disappear when users interact with the field