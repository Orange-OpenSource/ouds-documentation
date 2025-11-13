# Guideline

## Intro 👈🤖

A PIN Code Input captures short, fixed-length numeric codes through individual digit fields for secure authentication or verification flows.

---

## Description

A PIN code input is a specialized form field used to capture short, fixed-length numeric codes, typically for authentication or confirmation purposes, such as a 4, 6 or 8-digit personal identification number (PIN).

It is often presented as a series of individual input fields or boxes, each representing a single digit, to enhance readability and encourage accurate input.

This component must support smooth keyboard navigation (automatic focus shift, backspace handling), secure input masking if needed. It is commonly used in sensitive flows like login, verification, or transaction confirmation.

---

## Anatomy 👈🤖

| # | Element | Purpose |
|---|---------|---------|
| 1 | PIN code container | Groups all digit input fields in a horizontal row with consistent spacing |
| 2 | Digit input field | Individual field for a single numeric character, displays entered digit as masked bullet or visible number |
| 3 | Focus indicator | Visual border highlighting the currently active digit input field |
| 4 | Placeholder | Dash or hyphen displayed in empty digit fields to indicate expected input |
| 5 | Helper text | Supporting message below inputs providing context (e.g., "Enter the 6-digit code sent to your phone") |
| 6 | Error message | Red text below inputs explaining validation failure when error state is triggered |
| 7 | Error indicator (combined) | Red border and background tint on digit fields when validation fails |

---

## Usage & Guidance

### Best for 👈🤔

✅ SMS or email verification codes requiring 4, 6, or 8 digits
✅ Two-factor authentication flows with time-sensitive codes
✅ Transaction confirmation PINs for financial operations
✅ Password reset verification with numeric codes
✅ Account login requiring fixed-length numeric credentials
✅ Device pairing or setup requiring numeric confirmation
✅ Parental control or age verification requiring PIN entry
✅ Secure document access with fixed-length numeric keys
✅ One-time passwords (OTP) sent via SMS or authenticator apps
✅ Registration completion with email verification codes

---

### Behaviour and interactions

**Visible or Accessible Label**
• The input must have a clear and unique label, either visible on screen or provided through aria-label or aria-labelledby.
• Never rely solely on a placeholder to describe the field – placeholders do not replace labels, especially for screen reader users.

**Clear separation of country selector, dial code, and input field**
• The country selector must be keyboard-navigable (e.g., <button> or <select>) and properly labelled (e.g., aria-label="Select country").
• If the dial code (e.g., +33) is displayed as a prefix, it should be readable by assistive technologies, with a clear semantic role (e.g., non-editable text, not focusable if decorative).
• Ensure the visual and semantic reading order is coherent (e.g., "Select country, France, plus thirty-three, phone number").

**Input formatting and guidance**
• If a mask is used for formatting (e.g., (0X) XX XX XX XX), it must not interfere with keyboard navigation or screen reader output.
• Provide clear instructions if a specific format is required, both visually and via aria-describedby.

**Clear and accessible error feedback**
• In case of errors (e.g., incomplete number, invalid format), display a clear, visible error message, linked to the field via aria-describedby.
• Do not rely on color alone to indicate errors – combine text, icon, and visual state changes.

**Smooth keyboard navigation**
• All interactive elements (input field, country selector, etc.) must be fully keyboard-accessible in a logical order (e.g., using Tab and arrow keys).
• Follow native interaction patterns (e.g., use arrow keys to navigate country list, Escape to close dropdown, etc.).

**Logical screen reader announcements**
• Ensure screen readers announce elements in a clear and logical order: field label, selected country, dial code, and then the input field.
• Avoid complex composite fields that may not be well supported by assistive technologies. Prefer either a single field or clearly separated elements with appropriate ARIA roles.

**Responsive and readable at all scales**
• The component must remain readable and functional at all screen sizes, including zoom (up to 200%, per WCAG 2.2 AA) or in compact interfaces.
• Related elements (label, icons, helper text, error messages) must remain visible, legible, and non-overlapping.
• All field elements must remain functional under zoom: input, focus, keyboard interactions, visibility of states (error, helper, etc.).
• No element (e.g., error message, action icon) should be truncated, hidden, or inaccessible due to zoom.
• On mobile, pinch-to-zoom must be allowed (avoid meta tags like user-scalable=no).
• Prefer column-based or flex-wrap layouts to prevent horizontal breaking.
• Icons and interactive elements must scale with text during zoom.
• Ensure touch targets remain large enough: at least 44x44 px in final display, regardless of scale.

---

### Provide context before the input 👈🤔

✅ **Do:** Display clear instructions above the input explaining where the code was sent (e.g., "Enter the 6-digit code sent to +33 6 12 34 56 78") and how long it remains valid  
❌ **Don't:** Show the PIN input without explaining the code source, expected format, or expiration time, leaving users uncertain about what to enter

### Show resend options for time-sensitive codes 👈🤔

✅ **Do:** Include a countdown timer with helper text like "Code expires in 2:30" and a "Resend code" link that becomes active after expiration  
❌ **Don't:** Hide resend functionality or fail to indicate when users can request a new code if the first one expires or doesn't arrive

### Display clear error messages for validation failures 👈🤔

✅ **Do:** Show specific error text like "Incorrect code. 2 attempts remaining." or "This code has expired. Request a new one." with error state styling on inputs  
❌ **Don't:** Display generic "Invalid code" errors without explaining the specific problem (wrong code, expired, already used, max attempts) or next steps

### Position the input within the verification flow 👈🤔

✅ **Do:** Place the PIN input as the final step after phone number entry, clearly separated from previous fields with its own heading and context  
❌ **Don't:** Combine the PIN input with other form fields or show it before establishing where the code was sent, creating confusion about the input sequence

### Handle successful verification gracefully 👈🤔

✅ **Do:** Show immediate success feedback (green borders, checkmarks) and automatically proceed to the next screen after successful code entry  
❌ **Don't:** Leave users waiting without confirmation after entering a correct code or require manual submission after all digits are filled

### Accommodate different code lengths clearly 👈🤔

✅ **Do:** Configure digit field quantity (4, 6, or 8) to match the exact code length your system sends, making it visually obvious how many digits are expected  
❌ **Don't:** Use a generic text field for code entry or display more/fewer fields than the actual code length, causing user uncertainty

### Consider security vs. usability for masking 👈🤔

✅ **Do:** Mask digits as bullets (●) by default for sensitive contexts like banking PINs, while allowing temporary visibility on mobile keyboards  
❌ **Don't:** Show unmasked digits in high-security contexts or mask verification codes that users may need to reference from another device

### Support paste functionality for codes 👈🤔

✅ **Do:** Allow users to paste complete codes (e.g., from SMS messages) that auto-populate all digit fields correctly  
❌ **Don't:** Disable paste or fail to handle pasted codes, forcing manual digit-by-digit entry even when codes are copied from messages

### Indicate code expiration timing 👈🤔

✅ **Do:** Display countdown timers or expiration timestamps (e.g., "Valid for 5 minutes" or "Expires at 14:32") so users know urgency  
❌ **Don't:** Send time-sensitive codes without indicating expiration, leading to confusion when codes fail after unknown time periods

### Provide alternative verification methods 👈🤔

✅ **Do:** Include fallback options like "Didn't receive a code? Try email verification" or "Call me instead" for users with SMS delivery issues  
❌ **Don't:** Trap users in a single verification path without alternatives when codes fail to arrive or phone numbers are inaccessible

---

### How should I configure the PIN input for SMS verification codes? 👈🤔

Use 6 digit fields with a visible label like "Verification code" and helper text stating "Enter the 6-digit code sent to +33 6 12 34 56 78" with a countdown timer.

### What should the error state look like when a user enters an incorrect code? 👈🤔

Display red borders on all digit fields, show an error icon, and include specific error text below like "Incorrect code. 2 attempts remaining."

### How do I display a 4-digit PIN input for transaction confirmation? 👈🤔

Configure 4 digit fields with masked bullets (●), a clear label like "Transaction PIN", and helper text such as "Enter your 4-digit PIN to confirm this payment."

### What's the visual configuration for an 8-digit PIN with expired code error? 👈🤔

Show 8 empty digit fields with red error borders and error message "This code has expired. Request a new code to continue."

### How should I show a resend option for time-sensitive verification? 👈🤔

Include helper text with countdown timer "Code expires in 2:30" and a disabled "Resend code" link that becomes active after expiration.

### What should the success state look like after correct code entry? 👈🤔

Display green borders on filled digit fields with checkmarks and brief success message "Code verified" before auto-advancing to next screen.

### How do I configure helper text for email verification vs. SMS? 👈🤔

For email: "Enter the 6-digit code sent to user@example.com"; for SMS: "Enter the 6-digit code sent to +33 6 12 34 56 78".

### What's the layout for partially filled PIN input during entry? 👈🤔

Show first two fields with masked bullets (●), third field with blinking cursor and darker background (focus state), remaining fields with placeholder dashes (-).

### How should I display maximum attempts exceeded error? 👈🤔

Show all digit fields with red error state, error icon, and message "Maximum attempts exceeded. Request a new verification code."

### What's the configuration for first-use PIN creation vs. verification? 👈🤔

Creation: "Create your 6-digit PIN" with helper text "Choose a PIN you'll remember"; Verification: "Enter PIN" with helper text "Enter the PIN you just created".

---

## Screen Sizes

### Desktop 👈🤖
The PIN code input displays horizontally with individual digit fields sized 56px wide × 60px tall, with 12px gaps between fields. Helper text and error messages appear below with full width, maintaining clear readability without wrapping.

### Tablet 👈🤖
Layout remains horizontal but digit fields scale to minimum 44px width while maintaining touch-friendly 60px height. Spacing between fields adjusts to 10-12px to fit viewport while preserving clear separation.

### Mobile 👈🤖
Digit fields use minimum 44px × 60px dimensions to meet touch target requirements. On narrow screens (320px-360px), 8-digit PINs may reduce field width slightly (44px minimum) or wrap helper text, but maintain full keyboard accessibility and paste support.

---

# Specs

## Properties

### Initial Config

| Property | Default Value | Notes |
|----------|---------------|-------|
| Outlined | False | Controls whether digit fields use subtle background (False) or transparent with visible stroke (True) |
| Rounded corner | False | Determines square corners (False) or rounded corners (True) for digit field containers |
| Length | 6 | Sets the number of individual digit input fields (4, 6, or 8) |
| Error | False | Toggles error state styling with red borders, background tint, and error message display |
| Helper text | False | Shows or hides supporting text below the PIN input fields |

---

### Outlined

**`False`** An input with a subtle background fill and visible bottom border, creating a softer and more contained look. Best suited for dense layouts or to enhance visibility.

**`True`** A minimalist input with a transparent background and a visible stroke outlining the field.
This style may be interesting for contexts other than form pages:
• When inputs need to feel lightweight and unobtrusive
• In a header (search field)
• In a selection/filtering feature in a product catalog

---

### Rounded corner

**`False`** For a square finish.

**`True`** For a finish with rounded corner.
To be favored in more emotional, immersive contexts or those tied to specific visual identities. For standard or business-oriented journeys, keep the default corners. This evolution addresses the need for flexibility in adapting the design to certain brand contexts.

---

### Error

The Error status indicates that the user input does not meet validation rules or expected formatting. It provides immediate visual feedback, typically through a red border, error icon, and a clear, accessible error message positioned below the input (mandatory).

This state helps users quickly identify and correct mistakes by explaining what went wrong and, when possible, how to fix it.
The input remains editable, encouraging users to revise their input without starting over.

The error state must be triggered by an explicit validation (submission, API response), and not in real time with each keystroke. This can occur either because the entered code does not match the expected code, because the user entered an expired or already used code, or finally if the maximum number of attempts has been exceeded.

⚠️ **Alert:** In the context of a PIN code input, in addition to the input's "Error" UI rendering, it is essential to also include an "Alert" component (also in its "Error" status) in the interface.

---

### Other boolean options

**Helper text** Supporting text conveys additional information about the input field, such as how it will be used. It should ideally only take up a single line, though may wrap to multiple lines if required, and be either persistently visible or visible only on focus.

---

# Accessibility 👈🤖

## Accessibility intro

The PIN Code Input must meet WCAG 2.2 Level AA requirements for keyboard navigation, screen reader announcements, focus visibility, error identification, and paste support. For comprehensive accessibility guidance, see the [Orange Unified Design System Accessibility Overview](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability).

---

## Accessibility Challenges

PIN code inputs present unique accessibility challenges because they fragment a single conceptual value across multiple visual fields, requiring careful coordination of keyboard navigation, screen reader announcements, and state management. Users relying on assistive technology must understand the relationship between individual digit fields while maintaining awareness of the complete code entry process.

### Key Challenges
- **Fragmented input model** - Multiple individual fields must behave as a cohesive single input for screen readers
- **Auto-advance behavior** - Automatic focus shifting between fields can confuse users if not properly announced
- **Paste operation complexity** - Pasted codes must correctly distribute across fields and announce the result
- **Error state ambiguity** - Validation failures must clearly indicate which attempt failed and remaining attempts

### Critical Success Factors
1. **Semantic grouping with fieldset/legend** ensuring screen readers announce the complete input purpose (2.4.6 Headings and Labels)
2. **Individual field labeling** with aria-label describing position (e.g., "Digit 1 of 6") so users track progress (4.1.2 Name, Role, Value)
3. **Coordinated ARIA live regions** announcing auto-advance, paste results, and validation outcomes without interrupting input flow (4.1.3 Status Messages)
4. **Error recovery guidance** providing specific failure reasons and clear next steps in associated error messages (3.3.3 Error Suggestion)

---

## Design Requirements

### Structure & Labels
- [ ] **Fieldset/legend wrapper**: Wrap all digit fields in `<fieldset>` with `<legend>` describing the complete input (e.g., "Enter 6-digit verification code") ([Orange Form Guidelines](https://a11y-guidelines.orange.com/en/web/components-examples/forms/))
- [ ] **Individual field labels**: Each digit field needs `aria-label="Digit [n] of [total]"` so screen readers announce position context
- [ ] **Helper text association**: Link helper text to the first digit field using `aria-describedby` to provide code source context

### Visual Design
- [ ] **Focus indicators**: Minimum 3:1 contrast ratio against background on focused digit field with 2px border thickness ([Orange Focus Indicators](https://a11y-guidelines.orange.com/en/web/components-examples/accessible-forms/#focus-indicator))
- [ ] **Error state contrast**: Red error borders (#CC0000) and error text must meet 4.5:1 contrast against white background
- [ ] **Touch target sizing**: Digit fields minimum 44×44px on mobile to meet touch accessibility requirements

### Content
- [ ] **Error message specificity**: ❌ "Invalid code" / ✅ "Incorrect code. 2 attempts remaining. Request new code if needed." ([Orange Error Messages](https://a11y-guidelines.orange.com/en/web/components-examples/forms/#error-messages))
- [ ] **Helper text clarity**: Include code source and expiration (e.g., "Enter 6-digit code sent to +33 6 12 34 56 78. Valid for 5 minutes.")

---

## Testing Checklist

### Screen Reader Testing
- [ ] Test with NVDA (Windows), JAWS (Windows), VoiceOver (macOS/iOS), TalkBack (Android) to verify fieldset/legend announces on entry, individual digit positions read correctly, auto-advance announces "Moved to digit [n]", paste operations announce "Code entered", error messages read with field context
- [ ] Verify masking announces as "Digit entered" not revealing actual values, empty fields announce with placeholder, focus changes don't interrupt announcement queue

### Keyboard Testing
- [ ] Tab enters first field, Arrow keys/Tab move between fields, Number keys enter digits with auto-advance, Backspace deletes and moves to previous field, paste (Ctrl+V/Cmd+V) fills all fields, Enter submits when complete, Escape clears all fields, focus visible with ≥3:1 contrast
- [ ] Verify no keyboard traps, all functionality operable without mouse, focus order matches visual layout

### Paste Testing
- [ ] Paste 6-digit code into first field distributes correctly across all fields, announces "6-digit code entered" to screen readers
- [ ] Paste partial code (3 digits) fills only first 3 fields, leaves remaining empty with correct focus position

Resources: [Orange Accessibility Testing Guide](https://a11y-guidelines.orange.com/en/web/test/)

---

## Key WCAG Criteria

- **2.1.1 Keyboard** (A): All digit field navigation, auto-advance, backspace, and paste operations operable via keyboard without timing requirements
- **2.4.7 Focus Visible** (AA): Visible focus indicator with ≥3:1 contrast on the currently active digit input field
- **3.3.1 Error Identification** (A): Validation errors identified in text below fields, associated via `aria-describedby`, explaining specific failure reason
- **3.3.3 Error Suggestion** (AA): Error messages provide guidance (e.g., "Request new code" when expired, "2 attempts remaining" when incorrect)
- **4.1.2 Name, Role, Value** (A): Each digit field has accessible name via `aria-label`, fieldset/legend provides group context, state changes (filled, error) programmatically announced

For complete reference: [Orange Accessibility Guidelines - Form Components](https://a11y-guidelines.orange.com/en/web/components-examples/forms/)

---

## Additional Resources

- [Orange Accessibility Guidelines - Form Examples](https://a11y-guidelines.orange.com/en/web/components-examples/forms/)
- [Orange Accessibility Guidelines - Keyboard Navigation](https://a11y-guidelines.orange.com/en/web/components-examples/keyboard/)
- [WCAG 2.2 Understanding 3.3.1 Error Identification](https://www.w3.org/WAI/WCAG22/Understanding/error-identification.html)
- [WCAG 2.2 Understanding 4.1.2 Name, Role, Value](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html)
- [Orange Design System - Accessibility & Sustainability](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability)

---
