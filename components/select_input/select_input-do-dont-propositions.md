# Select input — do & don't propositions

AI-generated propositions that no one has validated yet. They are not part of the documentation ([select_input.md](select_input.md)) and are not shown on zeroheight. Once a designer validates one, it moves into the full file.

## Outlined — do & don't

✅ **Do:** Use outlined style for inputs in non-form contexts like toolbars, headers, or filters where visual weight needs to be minimal

❌ **Don't:** Mix outlined and filled styles inconsistently within the same form or interface section

✅ **Do:** Choose outlined style when the input sits on colored or textured backgrounds where filled inputs might clash

❌ **Don't:** Use outlined style as the default for long multi-field forms where filled inputs provide better visual structure

✅ **Do:** Ensure outlined inputs maintain sufficient contrast ratios (3:1 minimum) against their background in all states

❌ **Don't:** Rely solely on the border to convey interactive affordance without proper focus indicators

✅ **Do:** Test outlined inputs with users who have low vision to ensure the borders are perceivable in all states

❌ **Don't:** Use outlined style when multiple inputs are stacked vertically without sufficient spacing, as borders may visually merge

✅ **Do:** Apply outlined style consistently across filtering and search interfaces for cohesive visual language

❌ **Don't:** Use outlined inputs in contexts where users expect traditional form styling, causing confusion

## Input status — do & don't

✅ **Do:** Use clear placeholder text in empty states to guide users on what type of selection is expected

❌ **Don't:** Leave empty states completely blank without labels or placeholders, causing user confusion

✅ **Do:** Provide meaningful placeholder text that describes the category of choices (e.g., "Select country")

❌ **Don't:** Use the first option as a placeholder disguised as a selectable value

✅ **Do:** Ensure filled states clearly display the full selected value or truncate gracefully with ellipsis

❌ **Don't:** Allow selected text to overflow outside the input container without proper truncation

✅ **Do:** Differentiate empty and filled states visually to help users quickly identify which fields need attention

❌ **Don't:** Use identical styling for empty and filled states that makes form progress unclear

✅ **Do:** Announce input status changes to screen readers when selections are made or cleared

❌ **Don't:** Remove the label when the input is filled, forcing users to remember what they selected

## Error — do & don't

✅ **Do:** Display error messages immediately below the select input, using clear language that explains how to fix the issue

❌ **Don't:** Rely on color alone to indicate errors; always include an icon and descriptive text for accessibility

✅ **Do:** Use `aria-describedby` to programmatically associate error messages with the select input for screen readers

❌ **Don't:** Show generic error messages like "Invalid selection" that don't help users understand what went wrong

✅ **Do:** Trigger validation after the user interacts with the field or attempts to submit the form, not while typing

❌ **Don't:** Display error states prematurely before users have had a chance to complete their selection

✅ **Do:** Ensure error icons have at least 3:1 contrast ratio and error text meets WCAG AA standards

❌ **Don't:** Hide error messages on focus or hover, preventing users from reading them while correcting mistakes

✅ **Do:** Provide specific guidance in error messages, such as "Please select a shipping method to continue"

❌ **Don't:** Use technical jargon or system codes in error messages that users cannot understand

## Leading icon — do & don't

✅ **Do:** Use universally recognizable icons that clearly represent the input's purpose (e.g., location pin for country selection)

❌ **Don't:** Add decorative icons that don't enhance understanding or serve a functional purpose

✅ **Do:** Ensure leading icons have proper color contrast (3:1 minimum) against their background in all states

❌ **Don't:** Use leading icons inconsistently across similar input types, creating confusion about their meaning

✅ **Do:** Size leading icons appropriately (16-24px) to maintain visual balance with text and remain perceivable

❌ **Don't:** Rely solely on icon color to convey state changes; use additional visual indicators for accessibility

✅ **Do:** Test icon comprehension with users to verify they understand the icon's meaning without text labels

❌ **Don't:** Place leading icons so close to the input text that they interfere with readability or cause visual clutter

✅ **Do:** Make leading icons purely visual and exclude them from the accessibility tree unless they convey unique information

❌ **Don't:** Use overly complex or detailed icons that become unclear when rendered at small sizes

## Label — do & don't

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

## Other boolean options — do & don't

✅ **Do:** Use helper text to provide essential context that helps users understand what to select or why

❌ **Don't:** Repeat information already stated in the label; helper text should add new, valuable guidance

✅ **Do:** Keep helper text concise (one sentence) to maintain readability and reduce cognitive load

❌ **Don't:** Use helper text for critical instructions that users might miss; include essential information in labels

✅ **Do:** Position helper text consistently between the input and any error messages in the vertical stack

❌ **Don't:** Hide helper text on focus or interaction when users may need it most

✅ **Do:** Use helper links when additional explanation is needed without cluttering the form interface

❌ **Don't:** Open helper links in new tabs without warning, as it disrupts the user's workflow

✅ **Do:** Ensure helper text is programmatically associated with the input using `aria-describedby`

❌ **Don't:** Style helper links identically to regular text, making them invisible to users who need extra guidance

✅ **Do:** Write helper text in plain language that all users can understand regardless of technical expertise

❌ **Don't:** Use helper text as a substitute for proper field labeling or clear option descriptions

## Mandatory field indication — do & don't

✅ **Do:** Clearly indicate mandatory fields using a consistent pattern throughout the entire form or application

❌ **Don't:** Mix different mandatory field indicators (asterisks, labels, colors) inconsistently within the same interface

✅ **Do:** Place the asterisk immediately after the label text with no space, making the association clear

❌ **Don't:** Use asterisks without providing a legend explaining their meaning to users who may not understand the convention

✅ **Do:** Ensure screen readers announce "mandatory" or "required" when asterisks are present using `aria-required` or similar attributes

❌ **Don't:** Rely solely on red color to indicate mandatory fields, as color-blind users cannot perceive the distinction

✅ **Do:** Display a summary message at the form top explaining the mandatory field convention before users encounter fields

❌ **Don't:** Mark all fields as mandatory when some are truly optional, reducing trust and increasing abandonment

✅ **Do:** Use "(optional)" labels sparingly and only when the optionality needs emphasis for clarity

❌ **Don't:** Override WCAG guidance by making critical fields appear optional or hiding required field indicators

✅ **Do:** Test mandatory field patterns with users who rely on assistive technology to ensure clear communication

❌ **Don't:** Use mandatory field indicators on single-field forms where the requirement is obvious from context
