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
| 5 | Error message | Specific feedback displayed when validation fails |

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