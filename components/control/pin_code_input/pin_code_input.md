# Guideline

## Intro

A PIN code input captures fixed-length numeric codes through individual digit fields, supporting authentication flows with automatic focus navigation and paste functionality.

---

## Definition

A PIN code input is a specialized form field used to capture short, fixed-length numeric codes, typically for authentication or confirmation purposes, such as a 4, 6 or 8-digit personal identification number (PIN).

It is often presented as a series of individual input fields or boxes, each representing a single digit, to enhance readability and encourage accurate input.

This component must support smooth keyboard navigation (automatic focus shift, backspace handling), secure input masking if needed. It is commonly used in sensitive flows like login, verification, or transaction confirmation.

---

## Best for

✅ Two-factor authentication (2FA) requiring a numeric verification code

✅ SMS or email one-time password (OTP) verification during account setup

✅ Transaction confirmation requiring a security PIN before completing payments

✅ Mobile-first flows where numeric keypad input is preferred

✅ Login verification when additional identity confirmation is needed

✅ Account recovery processes requiring code entry from email or SMS

✅ Session timeout re-authentication with a short verification code

✅ Secure actions requiring PIN confirmation (e.g., changing security settings)

✅ Time-sensitive code entry where codes expire within 30-60 seconds

✅ Device pairing or activation requiring numeric confirmation codes

---

## Anatomy

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | PIN code container | Groups all digit input fields as a cohesive unit | N |
| 2 | Digit input field | Individual input box accepting a single numeric character | N |
| 3 | Input border/underline | Visual boundary indicating the input area and state | N |
| 4 | Focus indicator | Highlights the currently active digit field | N |
| 5 | Error message | Displays validation feedback below the input group | Y |
| 6 | Helper text | Provides supporting instructions or context | Y |
| 7 | Separator | Visual divider between digit groups (e.g., 3-3 format) | Y |

---

## Outlined

**`False`** An input with a subtle background fill and un visible bottom border, creating a softer and more contained look. Best suited for dense layouts or to enhance visibility.

**`True`** A minimalist input with a transparent background and a visible stroke outlining the field.
This style may be interesting for contexts other than form pages:
• When inputs need to feel lightweight and unobtrusive
• In a header (search field)
• In a selection/filtering feature in a product catalog

### Do & don'ts

✅ **Do:** Use the filled (outlined=false) style in standard form contexts where the input needs prominence and clear boundaries.  
❌ **Don't:** Mix outlined and filled styles for PIN inputs within the same authentication flow.

✅ **Do:** Apply the outlined style consistently when multiple inputs appear in lightweight, non-form contexts like headers.  
❌ **Don't:** Use the outlined style in complex forms where it may reduce visual hierarchy and scannability.

✅ **Do:** Ensure both styles maintain sufficient contrast (≥3:1) against their background for accessibility compliance.  
❌ **Don't:** Choose a style based solely on aesthetics without considering the surrounding UI context and user expectations.

✅ **Do:** Consider the visual weight needed—use filled for emphasis in primary flows, outlined for secondary contexts.  
❌ **Don't:** Apply outlined style in high-security flows where users expect clear, prominent input fields.

✅ **Do:** Test both styles across light and dark themes to ensure consistent visibility and usability.  
❌ **Don't:** Assume one style works universally—validate with users in context before finalizing the choice.

---

## Rounded corner

**`False`** For a square finish.

**`True`** For a finish with rounded corner.
To be favored in more emotional, immersive contexts or those tied to specific visual identities. For standard or business-oriented journeys, keep the default corners. This evolution addresses the need for flexibility in adapting the design to certain brand contexts.

### Do & don'ts

✅ **Do:** Use square corners (rounded=false) for enterprise, banking, or professional application contexts.  
❌ **Don't:** Apply rounded corners in formal business flows unless explicitly aligned with brand guidelines.

✅ **Do:** Apply rounded corners consistently across all digit input fields when the rounded style is selected.  
❌ **Don't:** Mix rounded and square corners within the same PIN code input component.

✅ **Do:** Consider rounded corners for consumer-facing apps, entertainment, or lifestyle products seeking a friendlier aesthetic.  
❌ **Don't:** Use rounded corners as a default without considering whether they match the overall product design language.

✅ **Do:** Maintain the same corner radius across all input states (default, focus, error, disabled) for visual consistency.  
❌ **Don't:** Change corner styling between states, as this creates visual inconsistency and confusion.

✅ **Do:** Validate that rounded corners maintain sufficient touch target size (minimum 44×44px) on mobile devices.  
❌ **Don't:** Apply excessive border radius that makes individual digit fields appear as circles, reducing clarity.

---

## Error

The Error status indicates that the user input does not meet validation rules or expected formatting. It provides immediate visual feedback, typically through a red border, error icon, and a clear, accessible error message positioned below the input (mandatory).

This state helps users quickly identify and correct mistakes by explaining what went wrong and, when possible, how to fix it.
The input remains editable, encouraging users to revise their input without starting over.

The error state must be triggered by an explicit validation (submission, API response), and not in real time with each keystroke. This can occur either because the entered code does not match the expected code, because the user entered an expired or already used code, or finally if the maximum number of attempts has been exceeded.

**Alert:** In the context of a PIN code input, in addition to the input's "Error" UI rendering, it is essential to also include an "Alert" component (also in its "Error" status) in the interface.

### Do & don'ts

✅ **Do:** Display error messages only after explicit validation (form submission or API response), not during typing.  
❌ **Don't:** Show real-time error feedback on each keystroke, as this creates anxiety and interrupts the user's flow.

✅ **Do:** Provide specific, actionable error messages explaining what went wrong (e.g., "Incorrect code" or "Code expired").  
❌ **Don't:** Use vague error messages like "Error" or "Invalid input" that don't help users understand the problem.

✅ **Do:** Keep the input editable in error state so users can correct their entry without clearing all fields.  
❌ **Don't:** Clear all entered digits when an error occurs, forcing users to re-enter the entire code.

✅ **Do:** Use the Alert component in conjunction with the input's error state for important security messages.  
❌ **Don't:** Rely solely on the input field's visual error state without providing an accompanying error message.

✅ **Do:** Indicate remaining attempts clearly when account lockout is imminent (e.g., "2 attempts remaining").  
❌ **Don't:** Lock users out without warning or without providing clear recovery options after exceeding attempt limits.

---

## Other boolean options

**Helper text** Supporting text conveys additional information about the input field, such as how it will be used. It should ideally only take up a single line, though may wrap to multiple lines if required, and be either persistently visible or visible only on focus.

### Do & don'ts

✅ **Do:** Use helper text to provide context about code delivery (e.g., "Enter the 6-digit code sent to your phone").  
❌ **Don't:** Use helper text for information that should be in a label or that duplicates visible instructions elsewhere.

✅ **Do:** Keep helper text concise—ideally one line—to avoid cluttering the interface.  
❌ **Don't:** Write lengthy helper text that wraps multiple lines and competes with the primary input for attention.

✅ **Do:** Ensure helper text remains visible and readable in all states, including when the input is focused or in error.  
❌ **Don't:** Hide or obscure helper text when displaying error messages; show both when both are relevant.

✅ **Do:** Write helper text that adds value, such as timing information ("Code expires in 5 minutes") or delivery details.  
❌ **Don't:** Include placeholder-style hints in helper text that merely repeat the input's purpose without adding context.

✅ **Do:** Position helper text consistently below the input group across all instances of the PIN code input.  
❌ **Don't:** Place helper text in inconsistent locations that confuse users about which input it relates to.

---

# Specs

## States

🚧 Missing from source: States section in pin_code_input_overview.md

---

## Layout and spacing

🚧 Content to be added

---

# Changelog

| Date | Number | Notes |
|------|--------|-------|----------|
| Sep 30, 2025 | 1.2.0 | • The name of the "Style" variant has been replaced to "Outlined" with true/false variant | Hamza Amarir |
| Jul 29, 2025 | 1.1.0 | • Several design token updates: [Component tokens changelog 1.5.0](https://www.figma.com/design/Co2t6wHMf4GB9NJVGs2Hes/-OUDS-Core-Lib--Design-tokens?m=auto&node-id=9280-2568&t=HLVB4jOd35DWr8Bj-1) | Maxime Tonnerre |
| Jun 30, 2025 | 1.0.0 | • Component creation | Maxime Tonnerre |

---