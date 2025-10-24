# Guideline

## Intro

A PIN code input captures short, fixed-length numeric codes for authentication or confirmation using a series of individual digit fields.

---

## What is it

A PIN code input is a specialized form field used to capture short, fixed-length numeric codes, typically for authentication or confirmation purposes, such as a 4, 6 or 8-digit personal identification number (PIN).

---

## Anatomy

| # | Element | Purpose |
|---|---------|---------|
| 1 | Label | Identifies the purpose of the input field and provides context for what the user should enter |
| 2 | Input fields | Individual boxes for each digit, providing clear visual separation and encouraging accurate single-digit entry |
| 3 | Focus indicator | Highlights the currently active input field to guide user attention during digit entry |
| 4 | Error indicator | Visual marker (red border/icon) on input fields to signal invalid or rejected code entry |
| 5 | Helper text | Supporting guidance about the code format, expected length, or where to find the code |
| 6 | Error message | Specific text explaining what went wrong and how to correct the input |

---

## Usage & Guidance

**How should I configure labels and helper text for SMS verification codes?**  
Position a descriptive label above the input fields (e.g., "Enter verification code") and include helper text below showing the destination phone number or explaining the code source.

**What should the error state look like when a code is invalid?**  
Display red borders around all input fields, show an error icon, and provide a specific error message below explaining whether the code was incorrect, expired, or the maximum attempts were exceeded.

**How do I display different PIN lengths for various use cases?**  
Use 4 fields for simple PINs or quick verification, 6 fields for standard authentication codes (SMS/email), and 8 fields for enhanced security scenarios requiring longer codes.

**How should the component appear during active digit entry?**  
Highlight the current input field with a focus indicator, auto-advance to the next field after each digit is entered, and allow backspace to move to the previous field for corrections.

---

## Screen Variants

### Desktop  
Display input fields in a horizontal row with comfortable spacing between each digit box, allowing easy mouse or keyboard interaction with clear visual separation.

### Tablet  
Maintain the horizontal layout with slightly increased touch target sizes to accommodate finger input while preserving the visual clarity of individual digit fields.

### Mobile  
Present fields in a horizontal row with optimized touch targets (minimum 44×44px), automatically triggering the numeric keyboard and supporting auto-advance between fields for efficient one-handed entry.