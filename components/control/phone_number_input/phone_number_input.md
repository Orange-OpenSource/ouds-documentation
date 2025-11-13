# Guideline

## Intro 👈🤖

A phone number input field with optional country selector, dial code prefix, and validation.

---

## Description

A phone number input is a form field specifically designed to capture and validate telephone numbers, often in international format. It typically integrates a country selector, allowing users to choose their country and automatically apply the corresponding dialing code (such as +33 for France).

The dialing code is usually displayed as a non-editable prefix within the field to guide the user and ensure consistent formatting. The component include real-time formatting or masking to improve readability during input, and validation rules tailored to the number structure of the selected country.

---

## Anatomy 👈🤖

| # | Element | Purpose |
|---|---------|---------|
| 1 | Label | Identifies the purpose and expected input format for the field |
| 2 | Country selector button | Optional clickable button displaying country flag and chevron icon for country selection |
| 3 | Dial code prefix | Read-only display of the selected country's telephone dialing code |
| 4 | Input field | Editable area where users enter their phone number digits |
| 5 | Placeholder/Input text | Guidance text (placeholder) or actual user-entered phone number |
| 6 | Leading icon | Optional icon displayed on the left side of the input field (combined with other visual elements) |
| 7 | Helper/Error text | Contextual guidance or validation feedback message below the field |

---

## Usage & Guidance

### Best for 👈🤔

✅ International phone number collection requiring country code selection  
✅ Contact forms where users may be from different regions or countries  
✅ Registration flows needing verified phone numbers for authentication  
✅ Account settings where users update their contact information  
✅ Forms supporting SMS verification or two-factor authentication  
✅ Business applications requiring standardized international format  
✅ E-commerce checkout flows collecting delivery contact numbers  
✅ Customer support forms needing callback phone numbers  
✅ Mobile-optimized forms where number pad keyboard is beneficial  
✅ Applications with autofill support for faster form completion

---

### ⚠️ Label

Describes the purpose of the input. Why hide a phone number input label?

In some UI contexts, especially when space is limited or when the input is part of a compact layout (search bars, filters, inline forms), visually hiding the label can help maintain a clean and uncluttered interface.

However, hiding the label should only be done if:
• The purpose of the input remains clear thanks to a placeholder or contextual icon.
• The label is still accessible to screen readers (using aria-label, aria-labelledby, or visually hidden text).

Hiding a label is a design choice that must balance visual simplicity and clarity of intent, without compromising inclusiveness or form guidance.

---

### ⚠️ Mandatory field indication

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

---

### Clear country context 👈🤔

✅ **Do:** Display the selected country flag and dial code prominently to confirm the user's country selection before they begin typing  
❌ **Don't:** Hide the country selector or use ambiguous icons that don't clearly indicate which country is currently selected

### Format guidance visibility 👈🤔

✅ **Do:** Provide example formatting in placeholder text or helper text showing expected number structure (e.g., "06 12 34 56 78")  
❌ **Don't:** Leave users guessing about whether to include spaces, dashes, or the full international format

### Validation timing 👈🤔

✅ **Do:** Validate phone number format on blur or form submission, allowing users to complete their entry before showing errors  
❌ **Don't:** Interrupt users with validation errors while they're still actively typing their phone number

### Country selector placement 👈🤔

✅ **Do:** Position the country selector at the start of the input so users set their country before entering digits  
❌ **Don't:** Bury the country selector in a separate field or require users to scroll to change their country after entering their number

### Autofill support 👈🤔

✅ **Do:** Use appropriate autocomplete attributes (`tel-national` or `tel`) to enable browser and password manager autofill  
❌ **Don't:** Disable autocomplete or use generic attributes that prevent browsers from recognizing the field as a phone number input

### Error message specificity 👈🤔

✅ **Do:** Explain exactly what's wrong with the entered number (e.g., "Phone number must be 10 digits for France")  
❌ **Don't:** Show vague messages like "Invalid input" that don't help users understand how to fix the error

### Default country selection 👈🤔

✅ **Do:** Pre-select the user's country based on their location or account settings to reduce friction  
❌ **Don't:** Always default to a single country regardless of user context, forcing international users to manually change it

### Mobile keyboard optimization 👈🤔

✅ **Do:** Trigger the numeric keyboard on mobile devices by setting appropriate input attributes for faster number entry  
❌ **Don't:** Use a text keyboard that requires users to switch to numbers manually

### Dial code editability 👈🤔

✅ **Do:** Keep the dial code read-only and automatically update it when users change their country selection  
❌ **Don't:** Allow users to manually edit the dial code, which can create validation conflicts with the selected country

### Helper text usage 👈🤔

✅ **Do:** Use helper text to clarify what format is expected or reassure users about privacy (e.g., "Used only for account verification")  
❌ **Don't:** Clutter the interface with redundant instructions when the field purpose and format are already clear from context

---

### How should I configure labels and helper text for international business registration? 👈🤔

Display "Business phone number" as the label with helper text "Include country code for international clients" along with the country selector and dial code prefix visible.

### What should the error state look like when a user enters an incomplete phone number? 👈🤔

Show red border around the input with error text below stating "Phone number is incomplete" or specify the exact digit requirement for the selected country.

### How do I display the country selector with dial code for mobile-first forms? 👈🤔

Show the country flag button followed by the read-only dial code (e.g., "+33") inside the input field at the start, with the editable number area immediately after.

### What configuration works best for SMS verification code delivery? 👈🤔

Use label "Mobile phone number" with helper text "We'll send a verification code to this number" and enable the country selector with dial code displayed.

### How should I show validation for numbers from different country formats? 👈🤔

Display country-specific error messages (e.g., "French numbers must be 10 digits" or "US numbers must be 10 digits") that reflect the selected country's format requirements.

### What's the best layout for combining leading icon with country selector? 👈🤔

Position the leading icon first, followed by the country selector button with flag, then dial code, then the number input area, maintaining clear visual separation between each element.

### How do I configure the read-only state for displaying saved contact numbers? 👈🤔

Show the complete phone number with country code in a read-only field with muted styling and disable both the input and country selector button.

### What helper text should I display for privacy-sensitive phone collection? 👈🤔

Include helper text like "Your number will not be shared with third parties" or "Used only for order updates" below the input field.

### How should the empty state with placeholder differ from the empty state without placeholder? 👈🤔

The empty state without placeholder shows only the label above the field, while the empty placeholder state displays hint text like "06 12 34 56 78" inside the input area.

### What configuration should I use for optional phone number fields? 👈🤔

Display the label followed by "(optional)" text and include helper text explaining why providing the number is beneficial (e.g., "Helps us contact you about your order").

---

## Screen Sizes

### Desktop 👈🤖

The full phone number input displays at 360px width minimum with all elements clearly visible, including country selector button, dial code, and input area with comfortable spacing for mouse interaction.

### Tablet 👈🤖

The component maintains its desktop layout at reduced width, ensuring country flag, dial code, and input field remain accessible, with touch-friendly target sizes for the country selector button.

### Mobile 👈🤖

The input scales to full viewport width with optimized touch targets for the country selector, automatically triggering numeric keyboard, and displaying one element per line if space is constrained.

---

# Specs

## Properties

### Initial Config

| Property | Default Value | Notes |
|----------|---------------|-------|
| Outlined | False | Filled background style with visible bottom border is the default presentation |
| Rounded corner | False | Rectangular corners are used by default for structured form interfaces |
| Input status | Empty | Field begins empty, ready to accept user input without placeholder text |
| State | Enabled | Component is active and interactive, ready for user input |
| Error | False | No validation errors are present in the initial state |
| Leading icon | False | No icon displayed at the start of the input by default |
| Country selector | True | Country selection button with flag is enabled by default for international support |
| ⚠️ Label | True | Label is displayed by default to identify the field purpose |
| Dial code | True | Country dialing code prefix is displayed by default as a read-only element |
| Helper text | False | No additional contextual help text is shown initially |

---

### Outlined

**`False`** An input with a subtle background fill and un visible bottom border, creating a softer and more contained look. Best suited for dense layouts or to enhance visibility.

**`True`** A minimalist input with a transparent background and a visible stroke outlining the field.

This style may be interesting for contexts other than form pages:
• When inputs need to feel lightweight and unobtrusive
• In a header (search field)
• In a selection/filtering feature in a product catalog

---

### Rounded corner

**`False`** The input field is rectangular with sharp corners, creating a clean and structured appearance. This style is well-suited for form-based interfaces and professional, formal layouts, where clarity and alignment are key.

**`True`** The input field features rounded corners, giving it a softer and more modern look. This style works well in consumer-facing applications or interfaces with a friendly, approachable tone.

---

### Input status

**`Empty`** The field is empty. The placeholder text is not visible: the label is displayed instead and remains visible when the user starts typing.

**`Empty (Placeholder)`** The field is empty. The placeholder text is displayed in lieu of the label as an additional way to provide a contextual hint.

**`Filled`** The field has been filled out by the user.

---

### State

**`Enabled`** The default state when the user can interact with the text input. The field is ready to accept input when the user clicks or taps on it.

**`Hover`** Triggered when the user hovers the cursor over the input. This state provides visual feedback, signaling that the field can be interacted with.

**`Focus`** Activated when the user clicks or taps into the input, indicating that the field is currently selected and ready for input. This state is critical for accessibility, as it shows exactly where the user's focus is within the form.

**`Loading`** The component displays a loading indicator to inform the user that a process is underway, such as validating the input. The input remains disabled during this time.

**`Read only`** The input contains data but is not editable. This state is useful for displaying pre-filled data that the user shouldn't alter, like information pulled from a database or data confirmed in a previous step.

**`Disabled`** The input is inactive and cannot be interacted with. This state indicates that the field is currently unavailable, such as in cases where a required previous action has not been completed.

**`Skeleton`** A placeholder state to indicate that content is loading or being fetched. Useful in maintaining the layout structure while the actual data is being retrieved, providing a smooth user experience during initial page loads.

---

### Error

**`False`** The input is in a standard state, with no validation issues. It is ready for users to fill out without errors.

**`True`** The input has detected a validation error. An error message provides guidance to the user about what needs to be corrected. Error handling can be done either when the user navigates away from the field (on blur) or upon submission (when the user submits the form).

---

### Leading icon

**`Leading icon`** When enabled, it is possible to display an icon on the left of the input text.

---

### Country selector

**`Country selector`** When enabled, it is possible to display a country selector with its flag. Country selector is displayed as a secondary button with only an icon (flag) and a chevron.

---

### Other boolean options

**Dial code** When enabled, it is possible to display the country dial code value. The dial code is read-only and cannot be edited directly by the user.

**Helper text** When enabled, a helper text appears below the input field to provide additional context or tips on how to fill out the field. Useful for offering suggestions or clarifying expected input formats (e.g., "Please enter a phone number in international format").

---

# Accessibility 👈🤖

## Accessibility intro

Phone number inputs with country selectors present unique accessibility challenges that require careful attention to WCAG 2.2 Level AA compliance, particularly around keyboard navigation, screen reader announcements, and the relationship between multiple interactive components. For comprehensive accessibility guidance, see the [Orange Unified Design System Accessibility Overview](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability).

---

## Accessibility Challenges

Phone number inputs combine multiple interactive elements (country selector button, dial code display, and number input field) that must work cohesively for users with disabilities. The relationship between the country selector and the input field must be clear, state changes must be announced properly, and validation feedback must be associated correctly with the appropriate field element.

### Key Challenges
- Multiple interactive components requiring coordinated keyboard navigation and focus management
- Country selector button state must be announced to screen readers with current selection
- Dial code changes must be communicated as live updates when country selection changes
- Error messages must associate correctly with the input despite multiple component parts

### Critical Success Factors
1. Proper semantic HTML structure with fieldset/legend grouping related elements (WCAG 1.3.1, 4.1.2)
2. Keyboard-accessible country selector with clear focus indicators (WCAG 2.1.1, 2.4.7)
3. Screen reader announcements for country selection changes and dial code updates (WCAG 4.1.3)
4. Error messages associated with input using `aria-describedby` (WCAG 3.3.1, 3.3.2)

---

## Design Requirements

### Structure & Labels
- [ ] **Visible label provided for input field**: Use `<label>` element with `for` attribute matching input `id` ([Orange Forms Guidelines](https://a11y-guidelines.orange.com/en/web/components-examples/forms/))
- [ ] **Country selector has accessible name**: Use `aria-label="Select country"` on country selector button
- [ ] **Helper text associated with input**: Use `aria-describedby` to link helper text element to input field

### Visual Design
- [ ] **Focus indicator visible and high contrast**: Minimum 3:1 contrast ratio for focus outline on all interactive elements ([Orange Focus Guidelines](https://a11y-guidelines.orange.com/en/web/design/focus/))
- [ ] **Error state uses color plus text**: Red border combined with error icon and descriptive text message ([Orange Color Guidelines](https://a11y-guidelines.orange.com/en/web/design/colors-and-contrasts/))
- [ ] **Dial code visually distinct from editable input**: Use different background or border treatment to show read-only nature

### Content
- [ ] **Error messages clear and actionable**: ❌ "Invalid" / ✅ "French phone numbers must be 10 digits" ([Orange Error Messages](https://a11y-guidelines.orange.com/en/web/components-examples/accessible-forms/))
- [ ] **Placeholder text not used as label replacement**: Placeholder provides format example only, label always present

---

## Testing Checklist

### Screen Reader Testing
- [ ] Test with NVDA (Windows), JAWS (Windows), VoiceOver (macOS/iOS), TalkBack (Android) to verify label announced, country selection changes spoken, dial code updates announced, error messages read
- [ ] Verify country selector announces current country, button role, expanded state when dropdown opens

### Keyboard Testing
- [ ] Tab moves focus between country selector and input field, Enter/Space opens country selector, Arrow keys navigate country list, Escape closes country selector, all functionality keyboard-accessible, focus indicator visible (≥3:1 contrast)
- [ ] Test that dial code updates don't disrupt focus position within input field

### Autocomplete Testing
- [ ] Verify `autocomplete="tel-national"` or `autocomplete="tel"` attribute enables browser autofill
- [ ] Test that autofilled values trigger appropriate validation and state changes

Resources: [Orange Accessibility Testing Guide](https://a11y-guidelines.orange.com/en/web/test/)

---

## Key WCAG Criteria

- **1.3.1 Info and Relationships** (A): Fieldset/legend groups related country selector and input elements to convey their relationship programmatically
- **2.1.1 Keyboard** (A): All functionality including country selector dropdown and input field is fully operable via keyboard
- **2.4.7 Focus Visible** (AA): Visible focus indicator with ≥3:1 contrast on country selector button and input field
- **3.3.1 Error Identification** (A): Validation errors identified in text and associated with input via `aria-describedby` or `aria-errormessage`
- **4.1.2 Name, Role, Value** (A): Country selector uses proper button role and `aria-expanded` attribute, input has accessible name and description

For complete reference: [Orange Accessibility Guidelines - Forms](https://a11y-guidelines.orange.com/en/web/components-examples/forms/)

---

## Additional Resources

- [Orange Accessibility Guidelines - Forms Examples](https://a11y-guidelines.orange.com/en/web/components-examples/forms/)
- [Orange Accessibility Guidelines - Accessible Forms](https://a11y-guidelines.orange.com/en/web/components-examples/accessible-forms/)
- [WCAG 2.2 Understanding - Info and Relationships](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships)
- [WCAG 2.2 Understanding - Keyboard](https://www.w3.org/WAI/WCAG22/Understanding/keyboard)
- [Orange Design System - Accessibility & Sustainability](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability)