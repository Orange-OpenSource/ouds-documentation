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