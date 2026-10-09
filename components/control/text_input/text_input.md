# Guideline

## Intro 👈🤖

A text input allows users to enter and edit single-line textual data in forms, dialogs, and search interfaces.

---

## Definition

A text input is a user interface component that allows users to enter, edit, or select single-line textual data. It's one of the most fundamental form elements used to capture user input such as names, emails, passwords, or search queries.

It provides a visual and interactive affordance for text entry while supporting labels, placeholders, icons, helper messages, and validation feedback.

---

## Best for 👈🤔

✅ Capturing unique, free-form information that cannot be predicted (names, addresses, custom values)

✅ Collecting short, single-line responses where character count is relatively limited

✅ Email, username, or password entry with appropriate input types and validation

✅ Search queries requiring quick, single-line input with optional autocomplete

✅ Numeric entries when combined with appropriate input masks or validation (phone numbers, postal codes)

✅ Forms requiring inline validation feedback as users type or on blur

✅ Situations where prefixes or suffixes help clarify expected format (currency, units)

✅ Contexts needing leading icons to indicate input purpose (search, email, phone)

✅ Cases where trailing actions enhance efficiency (clear field, show/hide password)

✅ Mobile-first scenarios where appropriate keyboard types improve data entry accuracy

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Container | Provides visual boundaries and interactive area for the input field | N |
| 2 | Label | Describes the purpose of the input and what information is expected | N |
| 3 | Input text / Placeholder | Displays user-entered text or hint text guiding expected input format | N |
| 4 | Leading icon | Indicates input purpose or type (search, email, phone) | Y |
| 5 | Trailing action | Provides quick interactions (clear, show/hide password, dropdown) | Y |
| 6 | Helper text / Error message | Offers guidance on input requirements or displays validation feedback | Y |
| 7 | Prefix / Suffix | Displays fixed text or symbols indicating expected format (currency, units) | Y |

---

## Outlined

**`False`** An input with a subtle background fill and un visible bottom border, creating a softer and more contained look. Best suited for dense layouts or to enhance visibility.

**`True`** A minimalist input with a transparent background and a visible stroke outlining the field. This style may be interesting for contexts other than form pages:
• When inputs need to feel lightweight and unobtrusive
• In a header (search field)
• In a selection/filtering feature in a product catalog

### Do & don'ts

✅ **Do:** Use the filled style (Outlined=False) as the default for standard forms to provide clear visual boundaries and better scannability.  
❌ **Don't:** Mix filled and outlined styles randomly within the same form—maintain visual consistency throughout.

✅ **Do:** Choose the outlined style for search fields in headers or navigation areas where inputs should feel lightweight.  
❌ **Don't:** Use outlined inputs in dense forms where the lack of fill may reduce visibility and field recognition.

✅ **Do:** Consider the background context when choosing styles—outlined works better on light backgrounds with sufficient contrast.  
❌ **Don't:** Place outlined inputs on busy or patterned backgrounds where the subtle borders may be hard to perceive.

✅ **Do:** Apply the same input style consistently within a given context (all form fields, all search bars).  
❌ **Don't:** Switch between outlined and filled variants for adjacent inputs without a clear design rationale.

✅ **Do:** Test both styles with your target users to determine which provides better affordance in your specific context.  
❌ **Don't:** Assume one style is universally better—context, brand, and user needs should drive the decision.

---

## Rounded corner

**`False`** For a square finish.

**`True`** For a finish with rounded corner. To be favored in more emotional, immersive contexts or those tied to specific visual identities. For standard or business-oriented journeys, keep the default corners. This evolution addresses the need for flexibility in adapting the design to certain brand contexts.

### Do & don'ts

✅ **Do:** Use square corners as the default for business-oriented applications and standard enterprise forms.  
❌ **Don't:** Apply rounded corners inconsistently across different input fields within the same interface.

✅ **Do:** Consider rounded corners when the overall brand identity uses soft, approachable visual language.  
❌ **Don't:** Mix square and rounded corners on the same page unless they serve distinct semantic purposes.

✅ **Do:** Match the corner radius of text inputs with other interactive elements (buttons, cards) in the same context.  
❌ **Don't:** Use extremely large corner radii that distort the input proportions or reduce usable input area.

✅ **Do:** Apply rounded corners for consumer-facing, lifestyle, or entertainment products where warmth is desired.  
❌ **Don't:** Override established brand guidelines just for aesthetic preference—align with the design system.

✅ **Do:** Ensure the corner style choice is documented and applied systematically through design tokens.  
❌ **Don't:** Hardcode corner values individually—use design tokens to maintain consistency and enable theming.

---

## Input status

**`Empty`** The field is empty, showing only the label.

**`Empty (Placeholder)`** The field is empty but displays placeholder text to guide the user.

**`Filled`** The field contains user-entered text.

### Do & don'ts

✅ **Do:** Always provide a visible, persistent label for every text input—never rely solely on placeholder text.  
❌ **Don't:** Use placeholder text as a replacement for labels; it disappears when users start typing and harms accessibility.

✅ **Do:** Use placeholder text to provide format hints or examples (e.g., "e.g., john@example.com").  
❌ **Don't:** Put critical instructions in placeholder text—users cannot reference it once they've entered content.

✅ **Do:** Ensure filled inputs maintain clear visual distinction between the label and the entered value.  
❌ **Don't:** Use placeholder text color for entered values—maintain sufficient contrast for readability.

✅ **Do:** Design empty states to clearly invite interaction with appropriate visual affordances.  
❌ **Don't:** Make empty inputs appear disabled or non-interactive through overly subtle styling.

✅ **Do:** Consider pre-populating fields with known values when possible to save users time and reduce errors.  
❌ **Don't:** Auto-populate sensitive fields (like passwords) without explicit user consent and secure handling.

---

## Error

The Error status indicates that the user input does not meet validation rules or expected formatting. It provides immediate visual feedback, typically through a red border, error icon, and a clear, accessible error message positioned below the input (mandatory).

This state helps users quickly identify and correct mistakes by explaining what went wrong and, when possible, how to fix it. The input remains editable, encouraging users to revise their input without starting over.

**⚠️ Error message vs helper text / link** The error message is not the same element as the helper text, it is independent. If a helper text accompanies the text input, it is replaced by the error message. The helper text must not be displayed simultaneously. However, a helper link must not be replaced and should remain positioned below the error message.

### Do & don'ts

✅ **Do:** Write specific, actionable error messages that tell users exactly what went wrong and how to fix it.  
❌ **Don't:** Use generic error messages like "Invalid input" or "Error"—they don't help users understand the problem.

✅ **Do:** Use multiple visual cues for errors (color, icon, border, text) to support users who may not perceive color alone.  
❌ **Don't:** Rely solely on red color to indicate errors—colorblind users may miss the feedback entirely.

✅ **Do:** Associate error messages programmatically with inputs using `aria-describedby` for screen reader accessibility.  
❌ **Don't:** Display error messages in locations disconnected from the input field, making the association unclear.

✅ **Do:** Validate after form submission or when the user leaves the field—avoid interrupting users mid-typing.  
❌ **Don't:** Show errors while users are still typing, which can be disruptive and frustrating.

✅ **Do:** Phrase errors as helpful instructions (e.g., "Enter an email address") rather than accusations ("You entered invalid data").  
❌ **Don't:** Use technical jargon or codes in error messages—speak in user-friendly language.

---

## Leading icon

Helps indicate the purpose of the input (magnifying glass for search, envelope for email, phone device for phone number). Only use a leading icon if it adds clear functional or contextual value.

### Do & don'ts

✅ **Do:** Use universally recognized icons that clearly communicate the expected input type (magnifying glass for search).  
❌ **Don't:** Add decorative icons that don't provide functional or contextual value—they create visual noise.

✅ **Do:** Ensure leading icons have sufficient size (minimum 24dp) and contrast for easy recognition.  
❌ **Don't:** Use icons that compete visually with the input text or create crowding within the field.

✅ **Do:** Provide accessible names for icons using `aria-label` so screen readers can announce their purpose.  
❌ **Don't:** Assume icons alone convey meaning—always pair with labels for screen reader users.

✅ **Do:** Maintain consistent icon placement and sizing across all text inputs in your interface.  
❌ **Don't:** Vary icon styles (filled vs. outlined) inconsistently within the same form or context.

✅ **Do:** Consider whether the icon adds genuine value before including it—simpler is often better.  
❌ **Don't:** Overuse icons on every input; reserve them for cases where they meaningfully enhance comprehension.

---

## Trailing action

Provides direct, quick interaction within the input field (show/hide password, clear field, open dropdown). This action must enhance efficiency without cluttering the interface.

### Do & don'ts

✅ **Do:** Use clear buttons to let users quickly empty a filled input field, especially for search inputs.  
❌ **Don't:** Show clear buttons on empty inputs—they should only appear when there's content to clear.

✅ **Do:** Provide show/hide toggles for password fields so users can verify their input before submitting.  
❌ **Don't:** Make trailing actions too small to tap easily—maintain minimum touch target sizes (48dp).

✅ **Do:** Use descriptive `aria-label` attributes for trailing action buttons (e.g., "Show password", "Clear search").  
❌ **Don't:** Stack multiple trailing actions that create visual clutter or confusion about their functions.

✅ **Do:** Ensure trailing actions are keyboard accessible and receive visible focus indicators.  
❌ **Don't:** Place critical functionality only in trailing actions—provide alternative access methods.

✅ **Do:** Design trailing actions to be clearly distinct from the input content itself.  
❌ **Don't:** Use trailing actions for primary submit functions—reserve them for field-level utilities.

---

## ⚠️ Label

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

---

## Other boolean options

**`Autocompletion`** Provides suggested values as the user types. Displays inline text predictions within the input field and/or a dropdown menu of predictive options to speed up input and reduce errors.

**`Prefix`** A visual or textual element placed before the user's input. Commonly used to indicate expected formatting like a country code, a unit...

**`Suffix`** An element placed after the user's input, often used to display a currency or a unit (kg, %, cm…).

**`Helper text`** Supporting text conveys additional information about the input field, such as how it will be used. It should ideally only take up a single line, though may wrap to multiple lines if required, and be either persistently visible or visible only on focus.

**`Helper link`** If the helper text is not sufficient (It can also be displayed on its own without helper text), it's possible to offer the user an additional help link (the link can be external or open a modal).

### Do & don'ts

✅ **Do:** Use prefixes and suffixes to clarify expected format (€, kg, %) rather than relying on helper text alone.  
❌ **Don't:** Validate against users entering the prefix/suffix themselves—be forgiving if they duplicate it.

✅ **Do:** Keep helper text concise (ideally one line) and use full sentences with punctuation when appropriate.  
❌ **Don't:** Duplicate information already conveyed by the label or placeholder in helper text.

✅ **Do:** Use autocomplete to speed up input for predictable data like addresses, names, or common values.  
❌ **Don't:** Enable autocomplete for sensitive fields where suggestions could expose private information.

✅ **Do:** Make helper links visually distinct and clearly actionable, opening additional guidance when needed.  
❌ **Don't:** Hide essential information behind helper links—critical instructions should be immediately visible.

✅ **Do:** Mark prefixes and suffixes with `aria-hidden="true"` if they're purely decorative and don't need to be announced.  
❌ **Don't:** Add so many optional elements that the input becomes visually cluttered and overwhelming.

---

## ⚠️ Mandatory field indication

In standard use cases, such as an account creation form, where most fields are mandatory, it's advisable to indicate optional fields rather than adding an asterisk (*) to every mandatory field. This reduces visual clutter while maintaining clarity.

However, in forms with a balanced mix or where mandatory fields are less common, it's preferable to explicitly mark required fields with an asterisk. In such cases, a clear and accessible indication must be placed at the top of the form to inform users (e.g., "All fields marked with an * are mandatory"). This indication should be:
• Accessible to screen readers (e.g., using visually hidden text or aria-describedby).
• Visually positioned near the form's heading or in a notice zone (banner).
• Semantically tied to the form using a role="status" or aria-live region to be announced on load or when dynamic fields appear.

### Do & don'ts

✅ **Do:** Choose one pattern consistently—either mark optional fields or required fields, not both.  
❌ **Don't:** Mark every field with an asterisk when most fields are required—mark the exceptions instead.

✅ **Do:** Include a legend at the top of forms explaining what the asterisk (*) means if you use one.  
❌ **Don't:** Assume users understand that asterisks indicate required fields without an explanation.

✅ **Do:** Use the HTML `required` attribute to enable native browser validation and assistive technology support.  
❌ **Don't:** Rely solely on visual asterisks—ensure required status is programmatically communicated.

✅ **Do:** Consider your form's majority case: mark the minority (optional fields in required-heavy forms, or vice versa).  
❌ **Don't:** Use color alone to distinguish required from optional fields—provide text or symbol indicators.

✅ **Do:** Test your required field indication with screen readers to ensure it's properly announced.  
❌ **Don't:** Add "(required)" labels that duplicate information already conveyed by asterisks and legends.

---

# Specs

## States

**`Enabled`** Neutral appearance, whether empty or filled. It allows users to click, focus, and type freely without restrictions.

**`Hover`** Slight visual contrast or border color change.

**`Focus`** The text input is focused and ready to receive user input. It visually highlights the field to indicate that it's currently editable and interactive. This state typically appears after a user clicks or taps into the field.

**`Loading`** The Loading state indicates that the system is processing or retrieving data related to the text input. A progress indicator appears to inform the user that an action is in progress. During this state, the input may be temporarily disabled to prevent further interaction.

**`Read only`** Text visible but not editable (often with a muted or different background).

**`Disabled`** The field is non-interactive and grayed out to indicate it cannot be changed. The helper text is muted.

**`Skeleton`** Improves the perceived loading time by providing a visual cue of where field will appear once fully loaded. Uses the "Skeleton" component, variant "Security marge=False".

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