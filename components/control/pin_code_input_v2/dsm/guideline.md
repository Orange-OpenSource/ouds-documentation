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