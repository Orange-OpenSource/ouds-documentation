An error is used to provide real-time feedback when the select input is in an invalid state:

**Examples of invalid states:**
• Required field left empty
• Incorrect value format (invalid email, phone number, postal code)
• Value that does not meet the established criteria (password not secure enough, text too short or too long)

**Accessibility for error indication:**
• Color alone is not sufficient: WCAG requires that color not be the only means of conveying information. Therefore, an icon and explicit text must accompany the error color.
• Assistive technologies need contextual error messages: when a user submits a form or leaves a field, screen readers need to receive clear textual information about the error. Use the aria-describedby attribute to associate error messages with the corresponding select input element.
• Error text is not just an ornament: WCAG guidelines require that error messages be sufficiently precise and descriptive.

**`False`** The select input is in its neutral or valid state.

**`True`** The user sees an error message detailing the nature of the problem, and the component is visually marked (e.g., with a specific color or icon) to draw attention to the error.