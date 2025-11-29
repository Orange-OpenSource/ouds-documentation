# Guideline

## Intro

A phone number input captures and validates telephone numbers with integrated country selection, dial code display, and format-aware validation.

---

## Definition

A phone number input is a form field specifically designed to capture and validate telephone numbers, often in international format. It typically integrates a country selector, allowing users to choose their country and automatically apply the corresponding dialing code (such as +33 for France).

The dialing code is usually displayed as a non-editable prefix within the field to guide the user and ensure consistent formatting. The component include real-time formatting or masking to improve readability during input, and validation rules tailored to the number structure of the selected country.

---

## Best for

✅ Account registration requiring phone verification or two-factor authentication

✅ International e-commerce checkout with multi-country shipping addresses

✅ Appointment booking systems needing SMS confirmation capabilities

✅ Customer contact forms for service or support inquiries

✅ Emergency contact collection in healthcare or safety applications

✅ Delivery tracking systems requiring real-time SMS notifications

✅ Travel and hospitality booking with international guest profiles

✅ Financial services requiring phone-based identity verification

✅ B2B lead capture forms with international prospect databases

✅ Mobile-first applications where phone is the primary identifier

---

## Anatomy

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Label | Identifies the field's purpose for users and assistive technologies | N |
| 2 | Country selector | Displays country flag and enables selection of country/dial code | Y |
| 3 | Dial code prefix | Shows read-only country dialing code (e.g., +33) | Y |
| 4 | Input field | Primary area where users enter phone number digits | N |
| 5 | Leading icon | Visual indicator reinforcing the phone input context | Y |
| 6 | Helper text | Provides additional guidance on expected format or usage | Y |
| 7 | Error message | Displays validation feedback when input is invalid | Y |
| 8 | Container | Wraps all elements with appropriate styling (outlined/filled) | N |

---

## Outlined

**`False`** An input with a subtle background fill and un visible bottom border, creating a softer and more contained look. Best suited for dense layouts or to enhance visibility.

**`True`** A minimalist input with a transparent background and a visible stroke outlining the field.

This style may be interesting for contexts other than form pages:
• When inputs need to feel lightweight and unobtrusive
• In a header (search field)
• In a selection/filtering feature in a product catalog

### Do & don'ts

✅ **Do:** Use outlined style on light backgrounds where the stroke provides sufficient visual boundary and contrast.  
❌ **Don't:** Use outlined style on busy or patterned backgrounds where the thin border may become visually lost.

✅ **Do:** Apply filled style in dense form layouts where multiple inputs need clear visual separation.  
❌ **Don't:** Mix outlined and filled styles inconsistently within the same form section.

✅ **Do:** Consider outlined style for inline or embedded inputs that should feel integrated with surrounding content.  
❌ **Don't:** Use outlined style for critical data entry where maximum visibility is required.

✅ **Do:** Maintain consistent style choice across all phone number inputs within the same user flow.  
❌ **Don't:** Switch between outlined and filled based solely on aesthetic preference without considering usability.

✅ **Do:** Test both styles for sufficient contrast ratios (minimum 3:1) against their backgrounds.  
❌ **Don't:** Assume one style works universally across all themes (light/dark mode).

---

## Rounded corner

**`False`** The input field is rectangular with sharp corners, creating a clean and structured appearance. This style is well-suited for form-based interfaces and professional, formal layouts, where clarity and alignment are key.

**`True`** The input field features rounded corners, giving it a softer and more modern look. This style works well in consumer-facing applications or interfaces with a friendly, approachable tone.

### Do & don'ts

✅ **Do:** Use sharp corners for enterprise, financial, or government applications requiring a professional appearance.  
❌ **Don't:** Apply rounded corners inconsistently across form elements within the same interface.

✅ **Do:** Choose rounded corners for consumer-facing apps targeting a friendly, approachable brand personality.  
❌ **Don't:** Use excessively large border radii that distort the input's proportions or obscure content.

✅ **Do:** Align corner radius with your design system's global border-radius tokens for consistency.  
❌ **Don't:** Mix sharp and rounded inputs in the same form without clear visual hierarchy justification.

✅ **Do:** Consider how corner style affects touch target perception on mobile devices.  
❌ **Don't:** Let corner style choice override accessibility requirements like focus indicator visibility.

✅ **Do:** Test rounded corners at various input widths to ensure visual harmony across breakpoints.  
❌ **Don't:** Assume rounded corners automatically improve usability—test with real users.

---

## Input status

**`Empty`** The field is empty. The placeholder text is not visible: the label is displayed instead and remains visible when the user starts typing.

**`Empty (Placeholder)`** The field is empty. The placeholder text is displayed in lieu of the label as an additional way to provide a contextual hint.

**`Filled`** The field has been filled out by the user.

### Do & don'ts

✅ **Do:** Always display a visible label that persists when the user begins typing for accessibility compliance.  
❌ **Don't:** Rely solely on placeholder text as the only means of identifying the input's purpose.

✅ **Do:** Use placeholder text to show example formats like "06 12 34 56 78" only as supplementary guidance.  
❌ **Don't:** Use placeholder text that disappears as the only instruction for complex format requirements.

✅ **Do:** Ensure filled state maintains clear visual distinction from empty state for at-a-glance scanning.  
❌ **Don't:** Allow placeholder text color to pass as valid input text, confusing users about field completion.

✅ **Do:** Design empty state to clearly invite interaction with appropriate visual affordances.  
❌ **Don't:** Display placeholder text that could be mistaken for pre-filled user data.

✅ **Do:** Preserve user-entered data through page refreshes and navigation when appropriate.  
❌ **Don't:** Clear filled fields unexpectedly without user action or clear warning.

---

## Error

**`False`** The input is in a standard state, with no validation issues. It is ready for users to fill out without errors.

**`True`** The input has detected a validation error. An error message provides guidance to the user about what needs to be corrected. Error handling can be done either when the user navigates away from the field (on blur) or upon submission (when the user submits the form).

### Do & don'ts

✅ **Do:** Provide specific, actionable error messages explaining exactly what needs correction (e.g., "Phone number must be 10 digits").  
❌ **Don't:** Display generic errors like "Invalid input" that don't help users understand the problem.

✅ **Do:** Validate on blur for immediate feedback while avoiding interruption during active typing.  
❌ **Don't:** Trigger validation errors while the user is still actively entering their phone number.

✅ **Do:** Use both color and iconography to indicate error state, never relying on color alone.  
❌ **Don't:** Use only red color to indicate errors—this fails users with color vision deficiencies.

✅ **Do:** Associate error messages programmatically with inputs using `aria-describedby` for screen readers.  
❌ **Don't:** Position error messages far from the input field where association is unclear.

✅ **Do:** Clear error state immediately when the user corrects the input and validation passes.  
❌ **Don't:** Retain error styling after the user has successfully corrected the issue.

---

## Leading icon

**`Leading icon`** When enabled, it is possible to display an icon on the left of the input text.

### Do & don'ts

✅ **Do:** Use a recognizable phone icon that reinforces the input's purpose at a glance.  
❌ **Don't:** Use decorative or ambiguous icons that don't clearly relate to phone number entry.

✅ **Do:** Ensure the icon has sufficient contrast and size (minimum 16×16px) for visibility.  
❌ **Don't:** Make the icon interactive unless it has a clear, documented function.

✅ **Do:** Maintain consistent icon placement and sizing across all form inputs in your interface.  
❌ **Don't:** Use icons inconsistently—some inputs with icons, others without, in the same form.

✅ **Do:** Consider omitting the icon when the country selector flag already provides visual context.  
❌ **Don't:** Stack multiple icons (leading icon + flag) creating visual clutter.

✅ **Do:** Test icon visibility across all component states (enabled, disabled, error, focus).  
❌ **Don't:** Allow icon color to conflict with or obscure error/success state indicators.

---

## Country selector

**`Country selector`** When enabled, it is possible to display a country selector with its flag. Country selector is displayed as a secondary button with only an icon (flag) and a chevron.

### Do & don'ts

✅ **Do:** Default the country selector to the user's detected geolocation when available.  
❌ **Don't:** Force users to manually select a country when their location can be automatically detected.

✅ **Do:** Provide a searchable dropdown for the country list—there are nearly 200 countries.  
❌ **Don't:** Display countries only as a scrollable list without search capability.

✅ **Do:** Show both country name and dial code in the dropdown for clarity (e.g., "France (+33)").  
❌ **Don't:** Display only country codes in the selector, requiring users to memorize codes.

✅ **Do:** Preserve the entered phone number if the user changes the country selection.  
❌ **Don't:** Clear the phone number field when users switch countries, forcing re-entry.

✅ **Do:** Make the chevron indicator clearly visible to signal the selector is interactive.  
❌ **Don't:** Use a flag alone without affordance indicators—users may not recognize it as clickable.

---

## Label

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

---

## Other boolean options

**Dial code** When enabled, it is possible to display the country dial code value. The dial code is read-only and cannot be edited directly by the user.

**Helper text** When enabled, a helper text appears below the input field to provide additional context or tips on how to fill out the field. Useful for offering suggestions or clarifying expected input formats (e.g., "Please enter a phone number in international format").

### Do & don'ts

✅ **Do:** Display the dial code as clearly non-editable with visual distinction from the input area.  
❌ **Don't:** Allow users to accidentally select or attempt to edit the dial code prefix.

✅ **Do:** Use helper text to clarify format expectations before errors occur.  
❌ **Don't:** Display helper text that duplicates information already visible in the placeholder.

✅ **Do:** Keep helper text brief—one line maximum—to avoid overwhelming the form layout.  
❌ **Don't:** Use helper text for critical instructions that should be in the label.

✅ **Do:** Ensure helper text meets minimum contrast requirements (4.5:1 for normal text).  
❌ **Don't:** Use very light gray helper text that becomes illegible for users with low vision.

✅ **Do:** Replace helper text with error messages when validation fails, then restore after correction.  
❌ **Don't:** Display both helper text and error messages simultaneously, creating visual clutter.

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

✅ **Do:** Mark optional fields with "(optional)" rather than marking every required field with asterisks.  
❌ **Don't:** Use asterisks without explaining their meaning—provide a legend at form start.

✅ **Do:** Announce "mandatory" or "required" to screen readers instead of the visual asterisk symbol.  
❌ **Don't:** Rely solely on visual asterisks for required field indication—use `aria-required="true"`.

✅ **Do:** Position the mandatory field explanation at the top of the form before users encounter fields.  
❌ **Don't:** Place required field explanations at the bottom of forms where users discover them too late.

✅ **Do:** Use consistent mandatory indication patterns across all forms in your application.  
❌ **Don't:** Mix different required field indication methods within the same form or application.

✅ **Do:** Consider marking optional fields instead when most fields are required—reduces visual noise.  
❌ **Don't:** Over-mark forms with asterisks when all fields are required—state this once at the top.

---

# Specs

## States

**`Enabled`** The default state when the user can interact with the text input. The field is ready to accept input when the user clicks or taps on it.

**`Hover`** Triggered when the user hovers the cursor over the input. This state provides visual feedback, signaling that the field can be interacted with.

**`Focus`** Activated when the user clicks or taps into the input, indicating that the field is currently selected and ready for input. This state is critical for accessibility, as it shows exactly where the user's focus is within the form.

**`Loading`** The component displays a loading indicator to inform the user that a process is underway, such as validating the input. The input remains disabled during this time.

**`Read only`** The input contains data but is not editable. This state is useful for displaying pre-filled data that the user shouldn't alter, like information pulled from a database or data confirmed in a previous step.

**`Disabled`** The input is inactive and cannot be interacted with. This state indicates that the field is currently unavailable, such as in cases where a required previous action has not been completed.

**`Skeleton`** A placeholder state to indicate that content is loading or being fetched. Useful in maintaining the layout structure while the actual data is being retrieved, providing a smooth user experience during initial page loads.

---

## Layout and spacing

🚧 Content to be added

---

# Accessibility

## Accessibility intro

The Phone Number Input component must meet WCAG 2.2 Level AA compliance to ensure all users can successfully enter phone numbers regardless of ability. For comprehensive accessibility guidance, see the [Orange Unified Design System Accessibility Overview](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability).

---

## Accessibility Challenges

Phone number inputs present unique accessibility challenges due to their multi-part nature, combining a country selector, dial code prefix, and number input within a single component. International format variations and real-time formatting add complexity for assistive technology users.

### Key Challenges
- Multiple interactive elements (country selector, input field) require clear focus management and logical tab order
- Dial code changes must be announced to screen readers when country selection changes
- Input masking and formatting can interfere with screen reader announcements and braille displays
- Validation messages for country-specific number formats need clear, programmatic association

### Critical Success Factors
1. Group related elements with `fieldset` and `legend` or `role="group"` with `aria-labelledby`
2. Ensure country selector changes announce the new dial code via `aria-live` regions
3. Provide clear labels distinguishing country selector from phone number input
4. Associate all error messages with inputs using `aria-describedby`

---

## Design Requirements

### Structure & Labels
- [ ] **Visible label**: Persistent label text "Phone number" associated via `<label for="">` ([Orange label guidelines](https://a11y-guidelines.orange.com/en/web/components-examples/forms/))
- [ ] **Input type**: Use `type="tel"` and `autocomplete="tel"` for proper keyboard and autofill ([WCAG 1.3.5](https://www.w3.org/WAI/WCAG21/Understanding/identify-input-purpose.html))
- [ ] **Group labeling**: Wrap country selector and input in `role="group"` with descriptive `aria-label`

### Visual Design
- [ ] **Focus indicator**: Visible focus ring with ≥3:1 contrast ratio on all interactive elements ([Orange focus guidelines](https://a11y-guidelines.orange.com/en/web/design/colors-and-contrasts/))
- [ ] **Error styling**: Red border + error icon + text message, never color alone
- [ ] **Touch targets**: Minimum 44×44px for country selector button on mobile

### Content
- [ ] **Error messages**: ❌ "Invalid" / ✅ "Enter a 10-digit phone number" ([Orange error guidelines](https://a11y-guidelines.orange.com/en/web/components-examples/forms/))
- [ ] **Country list**: Include both country name and code for screen reader clarity

---

## Testing Checklist

### Screen Reader Testing
- [ ] Test with NVDA (Windows), JAWS (Windows), VoiceOver (macOS/iOS), TalkBack (Android)
- [ ] Verify: label announced on focus, country change announces new dial code, error messages read with input

### Keyboard Testing
- [ ] Tab navigates to country selector then input field in logical order, Enter/Space opens country dropdown
- [ ] Arrow keys navigate country list, Escape closes dropdown, focus indicator visible (≥3:1 contrast) throughout

### Country Selector Testing
- [ ] Verify country search is keyboard accessible, selection updates dial code and announces change

Resources: [Orange Accessibility Testing Guide](https://a11y-guidelines.orange.com/en/web/toolbox/)

---

## Key WCAG Criteria

- **1.3.1 Info and Relationships** (A): Use semantic HTML grouping for country selector + input field association
- **1.3.5 Identify Input Purpose** (AA): Include `autocomplete="tel"` for browser/assistive technology recognition
- **2.1.1 Keyboard** (A): All functionality operable via keyboard including country selector dropdown
- **3.3.1 Error Identification** (A): Errors identified in text, associated with input via `aria-describedby`
- **4.1.2 Name, Role, Value** (A): Country selector button has accessible name, expanded state communicated

For complete reference: [Orange Accessibility Guidelines - Form Components](https://a11y-guidelines.orange.com/en/web/components-examples/forms/)

---

## Additional Resources

- [Orange Accessibility Guidelines - Forms](https://a11y-guidelines.orange.com/en/web/components-examples/forms/)
- [GOV.UK Design System - Phone Numbers Pattern](https://design-system.service.gov.uk/patterns/phone-numbers/)
- [W3C WAI - Labeling Controls Tutorial](https://www.w3.org/WAI/tutorials/forms/labels/)
- [WCAG 2.2 Understanding 3.3.2 Labels or Instructions](https://www.w3.org/WAI/WCAG21/Understanding/labels-or-instructions.html)

---

# Changelog

| Date | Number | Notes |
|------|--------|-------|
| Sep 30, 2025 | 1.2.0 | • The name of the "Style" variant has been replaced to "Outlined" with true/false variant |
| Jul 29, 2025 | 1.1.0 | • Several design token updates: [Component tokens changelog 1.5.0](https://www.figma.com/design/Co2t6wHMf4GB9NJVGs2Hes/-OUDS-Core-Lib--Design-tokens?m=auto&node-id=9280-2568&t=HLVB4jOd35DWr8Bj-1) |
| Jun 30, 2025 | 1.0.0 | • Component creation |

---