# Quantity Input - Behavior

---

### Keyboard input disabled

In the vast majority of modern UX/UI cases, a quantity input should be editable on focus. However, there are a few specific rare cases where direct editing by keyboard input might be disabled:
• Highly guided or controlled usage→product configuration with mandatory steps
• Risk of critical error→specific or technical values
• Strict touch context→mobile app with simplified UI, no keyboard
• Deliberate product decision→to enforce navigation or a business constraint

In this specific context, it is therefore recommended to prefill the input by default.

---

### Keyboard input + increment/decrement controls enabled

In the context of an editable quantity input, if the field is focused and already filled by the user, then clicking the + (increase) or – (decrease) buttons must follow a smooth and predictable behavior according to the following UX rules.

When clicking + or – during editing:
• The value is automatically validated
• The action is applied to that value (+1 or –1)
• The field is visually updated with the new value
• The cursor is moved to the end of the field (optional)
• The field remains focused

Absolutely to avoid:
• Losing the currently typed value if partially entered
• Requiring defocus for the buttons to work
• Failing to parse/validate the value before incrementing

Specific error focus state:
If the value in the field is invalid (empty or non-numeric), clicking + or – may:
• Either fill in a default value (1)
• Or display a temporary blocking error ("Please enter a number")

---

### ⚠️ Label

Describes the purpose of the input. Why hide a quantity input label?
In some UI contexts, especially when space is limited or when the input is part of a compact layout (search bars, filters, inline forms), visually hiding the label can help maintain a clean and uncluttered interface.
However, hiding the label should only be done if:
• The purpose of the input remains clear thanks to a placeholder or contextual icon.
• The label is still accessible to screen readers (using aria-label, aria-labelledby, or visually hidden text).

Hiding a label is a design choice that must balance visual simplicity and clarity of intent, without compromising inclusiveness or form guidance.

---
