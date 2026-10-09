# Guideline

## Intro 👈🤖

A select input lets users choose a single option from a predefined list displayed in a dropdown menu.

---

## Definition

A select input is a form component that allows users to choose one (or sometimes multiple) options from a predefined list. It is typically rendered as a dropdown menu that displays available choices when interacted with, either by click or keyboard navigation.

This component is used when the number of choices is limited and known in advance and when users should select from controlled or standardized values

---

## Best for

✅ Selecting from 5-15 predefined options in a form

✅ Choosing standardized values where custom input is not needed

✅ Space-constrained interfaces where radio buttons would create clutter

✅ Sorting or filtering content by a single criterion

✅ Mobile-optimized forms leveraging native device selectors

✅ Data entry requiring controlled, validated selections

✅ Settings panels with multiple configuration options

✅ Forms where all options need not be immediately visible

✅ Location, date format, or category selection

✅ Small-screen interfaces requiring compact input controls

---

## Anatomy

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Label | Identifies the purpose of the select input | N |
| 2 | Input container | Clickable area that triggers the dropdown menu | N |
| 3 | Selected value | Displays the currently chosen option or placeholder text | N |
| 4 | Chevron icon | Visual indicator that the field opens a dropdown | N |
| 5 | Helper text | Provides additional guidance about the selection | Y |
| 6 | Error message | Communicates validation issues to the user | Y |
| 7 | Leading icon | Conveys the input's purpose or category at a glance | Y |
| 8 | Helper link | Offers additional help when helper text is insufficient | Y |

---

## Outlined

**`False`** An input with a subtle background fill and un visible bottom border.

**`True`** A minimalist input with a transparent background and visible stroke.

This style may be interesting for contexts other than form pages:
• When inputs need to feel lightweight and unobtrusive
• In a header (search field)
• In a selection/filtering feature in a product catalog

### Do & don'ts

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

---

## Rounded corner

**`False`** A subtle and minimal style (neutral input border)

**`True`** A soft, friendly style, a bit more playful and approachable

### Do & don'ts

✅ **Do:** Use rounded corners consistently across all form inputs in the same interface to maintain visual harmony

❌ **Don't:** Mix sharp and rounded corners arbitrarily within a single form, creating visual inconsistency

✅ **Do:** Choose rounded corners when designing for consumer-facing products where friendliness enhances user comfort

❌ **Don't:** Use extreme border radius values that compromise the rectangular nature of form inputs

✅ **Do:** Consider accessibility by ensuring rounded corners don't interfere with touch target size on mobile devices

❌ **Don't:** Apply rounded corners only to select inputs when other form controls remain sharp-edged

✅ **Do:** Test rounded corners with your brand guidelines to ensure they align with overall design language

❌ **Don't:** Use rounded corners in highly formal or technical interfaces where neutrality is required

✅ **Do:** Maintain consistent corner radius values across different input sizes for visual coherence

❌ **Don't:** Round corners so aggressively that the input resembles a pill shape, reducing form recognition

---

## Input status

**`Empty`** By default, a select input is open with label, no input text, dropdown closed, and no helper text displayed below.

**`Filled`** The input text is the option selected by the user from the dropdown menu.

### Do & don'ts

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

---

## Error

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

### Do & don'ts

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

---

## Leading icon

Conveys the nature or purpose of the select input field at a glance.

### Do & don'ts

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

---

## Label

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

---

## Other boolean options

**`Helper text`** Supporting text conveys additional information about the input field, such as how it will be used. It should ideally only take up a single line, though may wrap to multiple lines if required, and be either persistently visible or visible only on focus.

**`Helper link`** If the helper text is not sufficient (It can also be displayed on its own without helper text), it's possible to offer the user an additional help link (the link can be external or open a modal).

### Do & don'ts

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

---

## Mandatory field indication

**If all fields are mandatory (several fields present):**
1. Display the message "All fields are mandatory." at the top.
2. Do not use an asterisk (*) at the end of each field label, nor the word "mandatory."
UI rendering of the asterisk: font-weight-bold + color-content-negative (red).

**If not all fields are mandatory (several fields present):**
1. Display the message "All fields marked with an * are mandatory." at the top.
2. Use an asterisk (*) at the end of each mandatory field label (the word "mandatory" is read aloud instead of the visible asterisk at the end of the label).
UI rendering of the asterisk: font-weight-bold + color-content-negative (red).
3. Use the mention "(optional)" at the end of each optional field label. Note that this rule is not systematic—it remains an option, to be used if needed.

**If there is only one field in the form, or if the mandatory nature is obvious (such as login/password), no mention is necessary since the fields are essential to the form's functionality.**

### Do & don'ts

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

---

# Specs

## States

**`Enabled`** Default state: the input is ready for interaction.

**`Hover`** When the user hovers over the input field (without the dropdown being opened), the appearance of the element changes slightly to indicate interactivity.

**`Focus`** When the user clicks or tabs into the input field (without opening the dropdown), the field gains focus and applies specific visual styles.

**`Expanded`** When the user opens the dropdown menu to view options.

**`Loading`** Indicates that options are being loaded asynchronously.

**`Read only`** When the select input is in a read-only state, its value is visible, but the user cannot interact with it or change the selection.

**`Disabled`** The input cannot be interacted with (non clickable, can't receive focus, no hover effect) and its appearance indicates unavailability.

**`Skeleton`** Displays a placeholder UI while content is loading.

---

## Layout and spacing

🚧 Content to be added

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Nov ??, 2025 | 1.3.0 | • Scope: Trailing action=False / State=Loading → Replacement of the button component (loading state) with a "Trailing container" frame containing the circular progress indicator component | Maxime Tonnerre |
| Sep 30, 2025 | 1.2.0 | • The name of the "Style" variant has been replaced to "Outlined" with true/false variant | Hamza Amarir |
| Jul 29, 2025 | 1.1.0 | • Several design token updates: [Component tokens changelog 1.5.0](https://www.figma.com/design/Co2t6wHMf4GB9NJVGs2Hes/-OUDS-Core-Lib--Design-tokens?m=auto&node-id=9280-2568&t=HLVB4jOd35DWr8Bj-1) | Maxime Tonnerre |
| Jun 30, 2025 | 1.0.0 | • Component creation | Maxime Tonnerre |

---