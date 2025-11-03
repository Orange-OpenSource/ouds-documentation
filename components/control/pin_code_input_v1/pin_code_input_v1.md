# Guideline

## Intro

A specialized numeric input capturing fixed-length codes for authentication or verification using individual digit boxes for clarity.

---

## What is it

A PIN code input is a specialized form field used to capture short, fixed-length numeric codes, typically for authentication or confirmation purposes, such as a 4, 6 or 8-digit personal identification number (PIN).

It is often presented as a series of individual input fields or boxes, each representing a single digit, to enhance readability and encourage accurate input.

This component must support smooth keyboard navigation (automatic focus shift, backspace handling), secure input masking if needed. It is commonly used in sensitive flows like login, verification, or transaction confirmation.

---

## Anatomy

| # | Element | Purpose |
|---|---------|---------|
| 1 | Digit input box | Individual field for a single numeric character |
| 2 | Focus indicator | Visual cue showing the currently active input |
| 3 | Error indicator | Visual state applied to all boxes when validation fails |
| 4 | Helper text | Instructional message showing expected digit count |

---

## Usage & Guidance

### Good fit when

✅ Fixed-length numeric input required (4, 6, or 8 digits)  
✅ Authentication, verification, or transaction confirmation flows  
✅ Mobile-first contexts requiring paste/SMS autofill support

### Fast checklist

**Minimize user effort (Must)**  
✅ **Do:** Auto-advance focus after each digit entry to reduce manual tabbing  
❌ **Don't:** Force users to manually tab between boxes, slowing the flow

**Guide with context (Should)**  
✅ **Do:** Show helper text indicating expected digit count before first interaction  
❌ **Don't:** Wait until error submission to explain format requirements

**Surface errors immediately (Must)**  
✅ **Do:** Validate on submission and display specific error messages with next steps  
❌ **Don't:** Show generic "Error" without indicating whether the issue is empty or incorrect input

**Support paste workflows (Should)**  
✅ **Do:** Allow pasting full codes from SMS/email, auto-distributing digits across boxes  
❌ **Don't:** Require manual digit-by-digit entry when users have codes ready to paste

**Maintain visual hierarchy (Optional)**  
✅ **Do:** Use outlined style sparingly in headers or filters to reduce visual weight  
❌ **Don't:** Mix filled and outlined styles within the same form section

**See also:** [Properties](#properties) · [Keyboard Support](#keyboard-support) · [Error Handling](#error-handling)

### Core Flows

**SMS verification entry**  
User receives code → focuses first box → types/pastes digits → auto-advances → submits → receives validation feedback

**Transaction confirmation**  
User initiates transaction → PIN prompt appears → enters memorized code → backspaces to correct typos → submits → proceeds or sees error

---

## Screen Variants

### Desktop  
Standard box sizing with hover states; keyboard navigation is primary interaction method with full Tab/Shift+Tab support.

### Tablet  
Similar to desktop with slightly larger touch targets; numeric keyboard appears on focus.

### Mobile  
Optimized for thumb reach with 44×44px minimum touch targets; numeric keyboard auto-opens with `inputmode="numeric"`; paste support critical for SMS autofill.

---

# Specs

## Properties

### Initial Config

| Property | Default Value | Notes |
|----------|---------------|-------|
| Outlined | `False` | Filled style with subtle background provides better visibility in standard forms. |
| Rounded corner | `False` | Square corners maintain consistency with business-oriented interfaces. |
| Length | `6` | Six digits balance security and usability for most verification scenarios. |
| Error | `False` | Component starts in default state; error appears only after validation. |
| Helper text | `Off` | Optional instructional text can be enabled to guide users on expected format. |

### Property Details

#### Outlined

**`False`** An input with a subtle background fill and un visible bottom border, creating a softer and more contained look. Best suited for dense layouts or to enhance visibility.

**`True`** A minimalist input with a transparent background and a visible stroke outlining the field. This style may be interesting for contexts other than form pages:
• When inputs need to feel lightweight and unobtrusive
• In a header (search field)
• In a selection/filtering feature in a product catalog

---

#### Rounded corner

**`False`** For a square finish.

**`True`** For a finish with rounded corner. To be favored in more emotional, immersive contexts or those tied to specific visual identities. For standard or business-oriented journeys, keep the default corners. This evolution addresses the need for flexibility in adapting the design to certain brand contexts.

---

#### Length

| property name | type |
|---------------|------|
| Length | '4' \| '6' \| '8' |

Determines the number of individual digit input boxes displayed. Choose based on security requirements and user context.

---

#### Error

The default helper text informs the user about the number of digits required. The error state doesn't replace the helper message; instead, it adds a relevant error message beneath the helper text.

Error state applies to all digit inputs simultaneously and cannot be assigned individually.

**False behavior (no error detected)** The user hasn't submitted the form yet, or the form has been submitted and validated successfully. The component displays either in its default state or, if provided, includes a helper text to guide the user.

**True behavior (error detected)** The form was submitted with an invalid PIN code entry. For example, when the user submits without filling all required digits or enters incorrect digits during verification. The component displays two possible error message:
• Empty case: "Please enter the verification code."
• Filled case: "Verification failed. Check and enter the correct code."

⚠️ While the error state is active, the user can type again in the field. Upon resubmission, if validation is successful (True to False), the error state must be removed by resetting it to its default state. When the error state is active, the helper text remains visible without any changes.

---

#### Helper text

**Helper text** Offers optional instructional text beneath the PIN code, such as a message indicating the expected number of digits (4, 6, or 8). By default, this text is displayed to inform the user about the required input.

---

# Accessibility

## Keyboard Support

1. `Tab` moves focus to the first empty digit box or the first box if all are empty.
2. `Shift+Tab` moves focus backward from the component to the previous focusable element.
3. Arrow keys (`Left`/`Right`) navigate between digit boxes without deleting content.
4. `Backspace` deletes the current digit and moves focus to the previous box.
5. `Delete` removes the current digit and keeps focus on the same box.
6. `Enter` submits the form when all required digits are filled.
7. Number keys (`0`-`9`) enter digits and automatically advance focus to the next box.
8. Provide a visible focus indicator: outline or border ≥2px with contrast ≥3:1 against the background.
9. Focus order moves left-to-right through digit boxes, then to submit button or next form element.
10. Pasted content auto-distributes across boxes without breaking focus management.

---

## Screen Reader Experience

1. Use semantic `<input type="text" inputmode="numeric">` elements for each digit box.
2. Provide a group label via `<fieldset>` and `<legend>` or `role="group"` with `aria-labelledby` (e.g., "Enter 6-digit verification code").
3. Announce helper text using `aria-describedby` referencing the helper text ID.
4. Apply `aria-invalid="true"` to all digit inputs when in error state.
5. Link error messages to inputs using `aria-describedby` with a stable error ID.
6. Announce "digit 1 of 6", "digit 2 of 6" using `aria-label` on each input for positional context.
7. Use `aria-live="polite"` on the error message container to announce validation results on submission.
8. Ensure the current digit box value is announced when focus moves between boxes.

---

## Touch & Mobile

1. Provide touch targets ≥44×44px for each digit box with ≥8px spacing between boxes.
2. Use `inputmode="numeric"` to trigger the numeric keyboard on mobile devices.
3. Support paste gestures: long-press to paste full codes, auto-distributing digits across all boxes.
4. Ensure tap targets don't overlap; provide clear visual separation between digit boxes.
5. Support both portrait and landscape orientations without loss of functionality or layout breaking.

---

## Visual Accessibility

1. Ensure text contrast ≥4.5:1 for digit values and helper text; large text ≥3:1.
2. Ensure digit box borders and focus indicators have contrast ≥3:1 against the background.
3. Do not rely on color alone for error state; add error icons or text indicators below the component.
4. Support text resizing up to 200% without loss of content or functionality; digit boxes must reflow gracefully.
5. Respect `prefers-reduced-motion` for any animations related to focus transitions or error state changes.

---

## Error Handling

1. Apply `aria-invalid="true"` to all digit inputs when validation fails.
2. Link error text to inputs using `aria-describedby` with a stable error message ID.
3. Announce errors via `aria-live="polite"` immediately after form submission with validation failure.
4. Provide specific error messages: "Please enter the verification code" (empty) or "Verification failed. Check and enter the correct code" (incorrect).
5. Return focus to the first digit box after error announcement to enable immediate correction.
6. Remove `aria-invalid="false"` and clear error messages when user begins re-entry or validation succeeds.
7. Maintain helper text visibility even when error state is active; stack error message below helper text.

---

## Testing Checklist

### Quick Tests (≤5 minutes)

1. Keyboard-only: Tab to first box, type digits with auto-advance, use Backspace to correct, submit with Enter; visible focus indicators appear throughout.
2. Screen reader: Group label announces "Enter 6-digit verification code", each box announces "digit X of 6", error message reads "Verification failed. Check and enter the correct code" on submission.
3. Zoom to 200%: Digit boxes reflow without overlapping; all text and spacing remain readable and functional.
4. High-contrast/dark mode: Focus indicators, digit box borders, and error states remain perceivable with ≥3:1 contrast.
5. Touch device: Each digit box meets 44×44px target size; numeric keyboard opens automatically; paste from SMS distributes digits correctly.

### Common Issues to Avoid

1. Missing `aria-invalid` or `aria-describedby` on digit inputs when error state is active.
2. Color-only error indication without accompanying text or icon.
3. Focus indicator contrast <3:1 or missing visible focus on keyboard navigation.
4. Paste functionality not working or requiring manual digit-by-digit entry.
5. Error messages not announced by screen readers or missing specific guidance on correction.