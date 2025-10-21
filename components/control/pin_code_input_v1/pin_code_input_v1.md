# Guideline

## Intro

A specialized numeric input for capturing fixed-length security codes (4, 6, or 8 digits) used in authentication, verification, and transaction confirmation flows.

---

## What is it

A PIN code input is a specialized form field used to capture short, fixed-length numeric codes, typically for authentication or confirmation purposes, such as a 4, 6 or 8-digit personal identification number (PIN).

It is often presented as a series of individual input fields or boxes, each representing a single digit, to enhance readability and encourage accurate input.

This component must support smooth keyboard navigation (automatic focus shift, backspace handling), secure input masking if needed. It is commonly used in sensitive flows like login, verification, or transaction confirmation.

---

## Anatomy

| # | Element | Purpose |
|---|---------|---------|
| 1 | Digit container | Individual box representing one digit position in the PIN sequence |
| 2 | Input field | Active area accepting single numeric character input |
| 3 | Focus indicator | Visual cue showing the currently active digit position |
| 4 | Helper text | Instructional message displaying expected digit count (4, 6, or 8) |
| 5 | Error message | Validation feedback displayed when submission fails or input is incomplete |

---

## Usage & Guidance — Compact

### Use it if all 3 are true

* Fixed-length numeric input (4, 6, or 8 digits) is required
* Paste/SMS autofill support enhances user experience
* Security or verification context demands clear visual separation of digits

> Otherwise use a standard text input with `type="tel"` or `inputmode="numeric"` for variable-length codes.

### Top 5 Rules

**Auto-advance focus (Must)**

* ✅ **Do:** Move focus to the next digit automatically upon valid character entry
  *Reduces friction and matches user mental model of sequential entry.*
* ❌ **Don't:** Require manual Tab navigation between digit boxes
  *Forces unnecessary keystrokes and slows completion.*

**Backspace behavior (Must)**

* ✅ **Do:** Clear current digit and move focus to previous box on Backspace
  *Allows natural correction flow without losing position.*
* ❌ **Don't:** Delete current digit but leave focus in place
  *Breaks expected editing pattern and confuses users.*

**Paste support (Should)**

* ✅ **Do:** Accept full code via paste and distribute across digit boxes (e.g., from SMS)
  *Enables fast autofill and reduces manual entry errors.*
* ❌ **Don't:** Block paste or insert all digits into the first box only
  *Forces tedious retyping when autofill is available.*

**Unified error state (Must)**

* ✅ **Do:** Apply error styling to all digit boxes simultaneously with `aria-invalid="true"`
  *Communicates validation failure as a single cohesive event.*
* ❌ **Don't:** Highlight only the first empty or incorrect digit
  *Implies individual validation when the code is validated as a whole.*

**Helper text visibility (Should)**

* ✅ **Do:** Display digit count ("Enter 6-digit code") by default; append error below without replacing it
  *Preserves guidance while adding failure context.*
* ❌ **Don't:** Replace helper text entirely with error message
  *Removes the digit count reference users need for correction.*

*See also:* Specs → Initial Config, Accessibility → Error Handling, Accessibility → Keyboard Support

### Core Flows

* **First-time verification** — User receives SMS → Pastes code → All digits populate → Submits → **Success**
* **Manual retry after error** — User enters wrong code → Submits → Sees error → Clears via Backspace → Re-enters → **Success/Error**

---

## Screen Variants

**Desktop**  
Full-width digit boxes with visible spacing ≥16px between boxes; focus indicators at ≥2px stroke. Optimized for keyboard-first entry.

**Tablet**  
Balanced digit box sizing (48×48px minimum) supporting both touch and keyboard. Maintains spacing for fat-finger tolerance.

**Mobile**  
Touch targets at 48×48px minimum with ≥8px spacing. Triggers numeric keyboard via `inputmode="numeric"`. Paste button appears in context menu for SMS autofill.

---

# Specs

## Properties

### Initial Config

| Property | Default Value | Notes |
|----------|---------------|-------|
| Outlined | False | Uses filled style with subtle background; switch to True for lightweight transparent stroke style. |
| Rounded corner | False | Square corners by default; enable for brand-specific or emotional contexts. |
| Length | 6 | Supports 4, 6, or 8 digits; 6 is the most common verification code length. |
| Error | False | No error shown initially; switches to True after failed validation. |
| Helper text | True (visible by default) | Displays expected digit count message; remains visible when error appears. |

### Property Details (from source)

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

#### Error

The default helper text informs the user about the number of digits required. The error state doesn't replace the helper message; instead, it adds a relevant error message beneath the helper text.

Error state applies to all digit inputs simultaneously and cannot be assigned individually.

**False behavior (no error detected)** The user hasn't submitted the form yet, or the form has been submitted and validated successfully. The component displays either in its default state or, if provided, includes a helper text to guide the user.

**True behavior (error detected)** The form was submitted with an invalid PIN code entry. For example, when the user submits without filling all required digits or enters incorrect digits during verification. The component displays two possible error message:
• Empty case: "Please enter the verification code."
• Filled case: "Verification failed. Check and enter the correct code."

⚠️ While the error state is active, the user can type again in the field. Upon resubmission, if validation is successful (True to False), the error state must be removed by resetting it to its default state. When the error state is active, the helper text remains visible without any changes.

---

#### Other boolean options

**Helper text** Offers optional instructional text beneath the PIN code, such as a message indicating the expected number of digits (4, 6, or 8). By default, this text is displayed to inform the user about the required input.

---

**Source Notes**

* Derived from: Figma link (https://www.figma.com/design/QtOWrH1m3RHOAkfyy0XFil/-OUDS-Lib--Components?node-id=67312-34672), uploaded designer document (`pin_code_input_properties.md`)
* Conflicts noted: None.

---

# Accessibility

### Keyboard Support

1. `Tab` moves focus into the first empty digit box; `Shift+Tab` moves focus out to the previous form element.
2. Typing a valid numeric character (`0`–`9`) auto-advances focus to the next digit box (left→right); no auto-advance occurs on the last box.
3. `Backspace` clears the current digit and moves focus to the previous box; on the first box, Backspace clears the digit without moving focus.
4. `Arrow Left` / `Arrow Right` navigate between digit boxes without clearing content; wrap is not supported (focus stops at first/last box).
5. Provide a visible focus indicator with outline/border **≥2px** and contrast **≥3:1** against the background.

---

### Screen Reader Experience

1. Use semantic `<input type="text" inputmode="numeric">` elements for each digit box; group all boxes in a `<fieldset>` or `role="group"` with an accessible label (e.g., "Enter 6-digit verification code").
2. Provide `aria-label` or `aria-labelledby` on the group describing the purpose (e.g., "PIN code input, 6 digits required").
3. Apply `aria-invalid="true"` and `aria-describedby` linking to helper/error text when validation fails; announce error via `aria-live="assertive"` immediately upon submission failure.
4. Announce digit count in helper text initially (e.g., "Enter 6-digit code"); when error appears, append error message while preserving helper text (e.g., "Verification failed. Check and enter the correct code. Enter 6-digit code.").
5. Announce "Digit 1 of 6", "Digit 2 of 6", etc., as focus moves between boxes using `aria-label` or visual labels read by screen readers.

---

### Touch & Mobile

1. Provide touch targets **≥48×48px** for each digit box with spacing **≥8px** between adjacent boxes.
2. Trigger numeric keyboard using `inputmode="numeric"` on each input element; ensure `type="text"` to allow paste and SMS autofill.
3. Support paste gesture via long-press context menu; distribute pasted digits across all boxes automatically (e.g., pasting "123456" fills all six boxes in sequence).
4. Support both portrait and landscape orientations; ensure digit boxes remain visible and accessible without horizontal scroll at 100% zoom.

---

### Visual Accessibility

1. Ensure text contrast **≥4.5:1** for digit characters and helper/error text; large text (helper) requires **≥3:1**.
2. Ensure focus indicators and digit box borders have contrast **≥3:1** against the background.
3. Use both color and text to convey error state; apply red border + "Verification failed" message (do not rely on color alone).
4. Support text resizing up to **200%** without loss of content or functionality; digit boxes must reflow without horizontal scroll.
5. Respect `prefers-reduced-motion`; avoid animated transitions for focus movement or error appearance.

---

### Error Handling

1. Apply `aria-invalid="true"` to all digit input boxes when the error state is active (Error = True).
2. Link error text to the input group using `aria-describedby` with a stable ID (e.g., `id="pin-code-error"`); include both helper and error text IDs in `aria-describedby` (e.g., `aria-describedby="pin-code-helper pin-code-error"`).
3. Announce error message via `aria-live="assertive"` immediately upon failed submission; return focus to the first digit box for correction.
4. Display specific error messages: "Please enter the verification code." (empty case) or "Verification failed. Check and enter the correct code." (incorrect case).
5. Remove error state (reset `aria-invalid="false"` and clear error text) upon successful resubmission; announce success via `aria-live="polite"` (e.g., "Code verified successfully.").

---

### Testing Checklist

**Quick Tests (≤5 minutes)**

1. Keyboard-only: `Tab` into first box, type digits with auto-advance, use `Backspace` to correct, and submit; verify visible focus indicator ≥2px with ≥3:1 contrast.
2. Screen reader announces "Enter 6-digit verification code" on focus; error message "Verification failed. Check and enter the correct code." reads immediately after failed submission.
3. Zoom to **200%**: digit boxes reflow without horizontal scroll; spacing and focus indicators remain perceivable.
4. High-contrast/dark mode: focus indicators and error state remain visible with ≥3:1 contrast; red border alone is not the only error cue.
5. On a touch device: paste 6-digit code from SMS via long-press; verify numeric keyboard opens and all boxes populate correctly.

**Common Issues to Avoid**

1. Missing `aria-invalid="true"` on digit boxes when error state is active.
2. Replacing helper text entirely with error message (both must remain visible simultaneously).
3. Focus indicators with insufficient contrast (<3:1) against the background.
4. Blocking paste or failing to distribute pasted digits across all boxes.
5. Individual digit validation errors instead of unified group-level error state.