Describes the purpose of the input. Why hide a text input label?

In some UI contexts, especially when space is limited or when the input is part of a compact layout (search bars, filters, inline forms), visually hiding the label can help maintain a clean and uncluttered interface. However, hiding the label should only be done if:
• The purpose of the input remains clear thanks to a placeholder or contextual icon.
• The label is still accessible to screen readers (using aria-label, aria-labelledby, or visually hidden text).

Hiding a label is a design choice that must balance visual simplicity and clarity of intent, without compromising inclusiveness or form guidance.

### Do & don'ts

✅ **Do:** Always provide a label for every text input—make it visible by default for accessibility and usability.  
❌ **Don't:** Use placeholder text as the only label; it disappears on input and fails accessibility requirements.

✅ **Do:** Keep labels concise (1-3 words) and use sentence-case capitalization without colons.  
❌ **Don't:** Write labels as full sentences or questions when a short phrase suffices.

✅ **Do:** When visually hiding labels, use CSS techniques that keep them accessible to screen readers.  
❌ **Don't:** Use `display: none` or `visibility: hidden` to hide labels—these remove them from assistive technology.

✅ **Do:** Position labels above inputs (top-aligned) for better scannability and quicker form completion.  
❌ **Don't:** Rely on floating labels as the only label mechanism—they can cause accessibility issues when they shrink.

✅ **Do:** Ensure labels remain visible when the input is focused and after content is entered.  
❌ **Don't:** Allow labels to be obscured or overlapped by other interface elements.