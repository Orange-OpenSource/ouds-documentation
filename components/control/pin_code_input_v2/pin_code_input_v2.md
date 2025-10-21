# Guideline

## Intro

A fixed-length numeric input component for capturing short authentication codes, presenting individual digit boxes to improve readability and accuracy during PIN entry.

---

## What is it

A PIN code input is a specialized form field used to capture short, fixed-length numeric codes, typically for authentication or confirmation purposes, such as a 4, 6 or 8-digit personal identification number (PIN).

It is often presented as a series of individual input fields or boxes, each representing a single digit, to enhance readability and encourage accurate input.

This component must support smooth keyboard navigation (automatic focus shift, backspace handling), secure input masking if needed. It is commonly used in sensitive flows like login, verification, or transaction confirmation.

---

## Anatomy

| # | Element | Purpose |
|---|---------|---------|
| 1 | Digit input box | Individual field for a single numeric character; provides clear visual separation between digits |
| 2 | Focus indicator | Highlights the currently active input box; guides user through sequential entry |
| 3 | Fill/outline container | Defines the visual boundary of each digit box using background fill or stroke |
| 4 | Helper text | Displays guidance (digit count) or context below the input row |
| 5 | Error message | Shows validation feedback when PIN entry fails; appears below helper text |

---

## Usage & Guidance

**When should I use outlined vs. filled style for PIN entry?**
Use filled (default) for standard form pages and dense layouts where visibility matters. Switch to outlined for lightweight contexts like header search fields, filtering features, or non-form scenarios where transparency reduces visual weight.  
*See also:* Specs → [Outlined](#outlined), Accessibility → [Visual Accessibility](#visual-accessibility)

**How does auto-advance work when entering digits?**
Focus automatically shifts to the next empty box after typing a valid digit, enabling rapid sequential entry without Tab key presses. Backspace moves focus to the previous box and clears its value, supporting quick corrections during the flow.  
*See also:* Specs → [Length](#length), Accessibility → [Keyboard Support](#keyboard-support)

**When does the error state appear and what triggers it?**
Error activates upon form submission when fields are incomplete or verification fails. Empty case shows "Please enter the verification code."; incorrect entry shows "Verification failed. Check and enter the correct code." Users can retype immediately; successful resubmission clears the error.  
*See also:* Specs → [Error](#error), Accessibility → [Error Handling](#error-handling)

**How should PIN input behave on mobile devices?**
Trigger numeric keyboard using `inputmode="numeric"` to streamline digit entry. Ensure each box meets 44×44px minimum touch target with 8px spacing, and support both portrait and landscape orientations without breaking the layout.  
*See also:* Specs → [Initial settings](#initial-settings), Accessibility → [Touch & Mobile](#touch--mobile)

---

## Screen Variants

**Desktop**  
Standard 6-digit layout with auto-advance focus and visible keyboard indicators. Each box sized for comfortable mouse/keyboard interaction with clear focus rings.

**Tablet**  
Slightly larger touch targets (44×44px minimum) to accommodate finger input. Numeric keyboard triggered automatically; layout adapts to portrait/landscape without loss of functionality.

**Mobile**  
Full numeric keyboard on focus with `inputmode="numeric"`. Touch targets meet 48×48px preferred size; boxes stack or scale responsively to fit narrow viewports while maintaining readability.

---

# Specs

## Properties

### Initial Config

| Property | Default Value | Notes |
|----------|---------------|-------|
| Outlined | False | Filled style provides better visibility in dense layouts; outlined reduces visual weight for non-form contexts. |
| Rounded corner | False | Square corners suit standard/business flows; rounded corners offer flexibility for brand-specific or emotional contexts. |
| Length | 6 | Six digits balances security and usability; adjust to 4 or 8 based on system requirements. |
| Error | False | Error state applies to all boxes simultaneously and cannot be assigned individually. |
| Helper text | Off | When enabled, displays the expected digit count (4, 6, or 8) to guide user input. |

---

### Property Details (from source)

### Outlined

**`False`** An input with a subtle background fill and un visible bottom border, creating a softer and more contained look. Best suited for dense layouts or to enhance visibility.

**`True`** A minimalist input with a transparent background and a visible stroke outlining the field. This style may be interesting for contexts other than form pages:
• When inputs need to feel lightweight and unobtrusive
• In a header (search field)
• In a selection/filtering feature in a product catalog

---

### Rounded corner

**`False`** For a square finish.

**`True`** For a finish with rounded corner. To be favored in more emotional, immersive contexts or those tied to specific visual identities. For standard or business-oriented journeys, keep the default corners. This evolution addresses the need for flexibility in adapting the design to certain brand contexts.

---

### Error

The default helper text informs the user about the number of digits required. The error state doesn't replace the helper message; instead, it adds a relevant error message beneath the helper text.

Error state applies to all digit inputs simultaneously and cannot be assigned individually.

**False behavior (no error detected)** The user hasn't submitted the form yet, or the form has been submitted and validated successfully. The component displays either in its default state or, if provided, includes a helper text to guide the user.

**True behavior (error detected)** The form was submitted with an invalid PIN code entry. For example, when the user submits without filling all required digits or enters incorrect digits during verification. The component displays two possible error message:
• Empty case: "Please enter the verification code."
• Filled case: "Verification failed. Check and enter the correct code."

⚠️ While the error state is active, the user can type again in the field. Upon resubmission, if validation is successful (True to False), the error state must be removed by resetting it to its default state. When the error state is active, the helper text remains visible without any changes.

---

### Other boolean options

**Helper text** Offers optional instructional text beneath the PIN code, such as a message indicating the expected number of digits (4, 6, or 8). By default, this text is displayed to inform the user about the required input.

---

### Length

| Property Value | Notes |
|----------------|-------|
| 4 | Four-digit PIN for quick authentication scenarios (e.g., app unlock, simple verification). |
| 6 | Six-digit PIN balances security and usability (default); common for two-factor authentication flows. |
| 8 | Eight-digit PIN for high-security contexts (e.g., transaction confirmation, sensitive account access). |

---

**Source Notes**

* Derived from: [Figma Component](https://www.figma.com/design/QtOWrH1m3RHOAkfyy0XFil/-OUDS-Lib--Components?node-id=67312-34672), uploaded designer document (pin_code_input_properties.md)
* Conflicts noted: None.

---

# Accessibility

### Keyboard Support

1. **`Tab`** moves focus forward through each digit box in left-to-right order; **`Shift+Tab`** moves focus backward.
2. Typing a valid digit (0–9) automatically advances focus to the next empty box; typing in the last box keeps focus on that box.
3. **`Backspace`** deletes the current digit and moves focus to the previous box; pressing Backspace in an empty box moves to the previous box without deleting.
4. **`Enter`** submits the form when all required digits are filled; focus remains on the last box if submission fails.
5. Provide a visible focus indicator with outline/border ≥2px and contrast ≥3:1 around the active digit box.
6. Arrow keys (**`ArrowLeft`**, **`ArrowRight`**) may optionally navigate between boxes; document this behavior if implemented.

---

### Screen Reader Experience

1. Use `<input type="text" inputmode="numeric" maxlength="1">` for each digit box to enforce single-character numeric entry.
2. Label the entire group using `role="group"` with `aria-labelledby` pointing to a heading (e.g., "Enter 6-digit verification code").
3. Each digit box must have a programmatic label such as `aria-label="Digit 1 of 6"` to indicate position in the sequence.
4. Apply `aria-invalid="true"` to all digit boxes when the error state is active; link error text using `aria-describedby` with a stable ID.
5. Announce error messages immediately upon submission failure using `aria-live="assertive"`; announce success states with `aria-live="polite"`.
6. When focus auto-advances, screen readers announce the new box label (e.g., "Digit 2 of 6") without additional interruption.

---

### Touch & Mobile

1. Provide touch targets ≥44×44px (48×48 preferred) for each digit box with spacing ≥8px between boxes.
2. Trigger numeric keyboard automatically using `inputmode="numeric"` to streamline digit entry on mobile devices.
3. Support both portrait and landscape orientations; boxes must reflow or scale responsively without loss of functionality.
4. Ensure visible focus indicators remain perceivable on touch devices (outline ≥2px, contrast ≥3:1) when using external keyboards.

---

### Visual Accessibility

1. Ensure digit box borders, focus indicators, and error outlines have contrast ≥3:1 against adjacent colors.
2. Error state must include both color change (e.g., red border) and a text message below the component; do not rely on color alone.
3. Helper text and error messages must have text contrast ≥4.5:1; large text (≥18pt or ≥14pt bold) requires ≥3:1.
4. Support text resizing up to 200%; boxes and text must reflow without horizontal scrolling or content loss (WCAG 2.1 Reflow).
5. Respect `prefers-reduced-motion` for focus transitions and auto-advance animations; reduce or eliminate motion when requested.

---

### Error Handling

1. Apply `aria-invalid="true"` to all digit boxes when the error state is active (submission with incomplete or incorrect entry).
2. Link error text to the group using `aria-describedby` with a stable ID (e.g., `id="pin-error"`); ensure each box references this ID.
3. Announce error messages immediately upon submission using `aria-live="assertive"`; message content must match displayed text.
4. Provide specific error messages: "Please enter the verification code." (empty case) or "Verification failed. Check and enter the correct code." (incorrect case).
5. Upon successful resubmission, remove `aria-invalid` and announce success with `aria-live="polite"` (e.g., "Code accepted"); return focus to the next logical element or first digit box for retry.

---

### Testing Checklist

**Quick Tests (≤5 minutes)**

1. Complete digit entry using keyboard only: Tab through boxes, type digits, Backspace to correct, Enter to submit; verify visible focus indicators (≥2px, ≥3:1 contrast).
2. Screen reader announces group label ("Enter 6-digit verification code"), individual box labels ("Digit 1 of 6"), and error messages immediately upon submission failure.
3. Zoom to 200%: digit boxes reflow without horizontal scrolling; all text and controls remain readable and functional.
4. High-contrast mode: focus indicators, error borders, and state cues remain perceivable with ≥3:1 contrast.
5. Touch device: numeric keyboard opens on focus; each box meets 44×44px; layout adapts to portrait/landscape without breaking.

**Common Issues to Avoid**

1. Missing `aria-labelledby` on the group or `aria-label` on individual digit boxes.
2. Error state indicated by color change only without accompanying text message or `aria-invalid`.
3. Focus indicator contrast <3:1 or outline <2px width.
4. Auto-advance not announced by screen readers or causing focus to skip boxes.
5. Missing `inputmode="numeric"` on mobile, forcing users to switch keyboard layouts manually.