I'll generate the design system documentation for the PIN code input component. Let me first fetch the Figma data from the provided link.Now let me compile the complete documentation using the uploaded designer document as the primary source:

# Guideline

## Intro

A PIN code input captures short, fixed-length numeric codes for authentication or confirmation through individual digit fields.

---

## What is it

A PIN code input is a specialized form field used to capture short, fixed-length numeric codes, typically for authentication or confirmation purposes, such as a 4, 6 or 8-digit personal identification number (PIN).

It is often presented as a series of individual input fields or boxes, each representing a single digit, to enhance readability and encourage accurate input.

This component must support smooth keyboard navigation (automatic focus shift, backspace handling), secure input masking if needed. It is commonly used in sensitive flows like login, verification, or transaction confirmation.

---

## Anatomy

| # | Element | Purpose |
|---|---------|---------|
| 1 | Input field container | Groups individual digit fields as a single interactive unit |
| 2 | Individual digit field | Displays and accepts a single numeric character |
| 3 | Field border/outline | Provides visual boundary and state indication (default, focused, error) |
| 4 | Helper text | Displays supporting information or instructions below the input |
| 5 | Error message | Shows validation feedback when code is incorrect or expired |

---

## Usage & Guidance

### How should I configure the input for a 6-digit SMS verification code?
Set Length to 6, enable Helper text with instructions like "Enter the code sent to your phone," and use the default non-outlined style with standard corners.

### What should the error state look like when a code is incorrect?
The input displays red borders on all digit fields, with an error message below stating the specific issue (e.g., "Invalid code. Please try again").

### How do I display a PIN input for transaction confirmation?
Use Length 4 for a transaction PIN, disable Helper text or provide context like "Enter your 4-digit transaction PIN," and pair with an Alert component for additional security messaging.

### What's the visual difference between 4-digit and 6-digit PIN layouts?
A 4-digit layout displays 4 individual fields in a row (212px wide), while a 6-digit layout shows 6 fields (324px wide), both maintaining consistent field spacing and sizing.

---

## Screen Variants

### Desktop  
Full-width digit fields with clear spacing, displaying horizontally in a single row with helper text underneath for optimal readability.

### Tablet  
Similar to desktop with proportional field sizing, maintaining horizontal layout and adequate touch target sizes for tablet interaction.

### Mobile  
Digit fields remain horizontally arranged but sized appropriately for mobile viewports, with numeric keyboard triggered automatically for efficient input.

---

# Specs

## Properties

### Initial Config

| Property | Default Value | Notes |
|----------|---------------|-------|
| Outlined | False | Non-outlined provides better visibility with background fill; outlined offers lighter appearance for non-form contexts |
| Rounded corner | False | Square corners are default for standard/business journeys; enable for brand-specific emotional contexts |
| Length | 6 | Common length for verification codes; adjust to 4 for PINs or 8 for enhanced security codes |
| Error | False | Enable to display error state with red border and error message after validation failure |
| Helper text | Off | Enable to provide supporting instructions or context below the input fields |

---

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

The Error status indicates that the user input does not meet validation rules or expected formatting. It provides immediate visual feedback, typically through a red border, error icon, and a clear, accessible error message positioned below the input (mandatory).

This state helps users quickly identify and correct mistakes by explaining what went wrong and, when possible, how to fix it. The input remains editable, encouraging users to revise their input without starting over.

The error state must be triggered by an explicit validation (submission, API response), and not in real time with each keystroke. This can occur either because the entered code does not match the expected code, because the user entered an expired or already used code, or finally if the maximum number of attempts has been exceeded.

⚠️ **Alert:** In the context of a PIN code input, in addition to the input's "Error" UI rendering, it is essential to also include an "Alert" component (also in its "Error" status) in the interface.

---

### Other boolean options

**Helper text** Supporting text conveys additional information about the input field, such as how it will be used. It should ideally only take up a single line, though may wrap to multiple lines if required, and be either persistently visible or visible only on focus.

---

# Accessibility

### Keyboard Support

1. `Tab` moves focus to the first empty digit field or the next field in the form; `Shift+Tab` moves backward.
2. Number keys (0-9) enter a digit in the focused field and automatically advance focus to the next empty field.
3. `Backspace` deletes the current digit and moves focus to the previous field; holding `Backspace` continues deleting backward.
4. Arrow keys (`Left`, `Right`) navigate between digit fields without changing values; `Home` jumps to first field, `End` to last field.
5. Each digit field receives a visible focus indicator with outline ≥2px and contrast ≥3:1 against the background.

---

### Screen Reader Experience

1. Use `<input type="text" inputmode="numeric">` for each digit field with `maxlength="1"` to accept single numeric characters.
2. Provide a group label using `role="group"` with `aria-labelledby` referencing a label like "Enter 6-digit verification code."
3. Link helper text to the input group using `aria-describedby` so context is announced when focus enters the group.
4. Apply `aria-invalid="true"` to all digit fields when in error state and link error message via `aria-describedby`.
5. Announce error messages immediately using `aria-live="assertive"` when validation fails, stating the specific issue and retry instructions.

---

### Touch & Mobile

1. Each digit field provides a touch target ≥44×44px with ≥8px spacing between fields for accurate tapping.
2. Use `inputmode="numeric"` to trigger the numeric keyboard on mobile devices, making digit entry faster.
3. Support both portrait and landscape orientations, maintaining field visibility and keyboard accessibility in both modes.
4. Ensure focus management works correctly with mobile keyboards, advancing to the next field after each digit entry.

---

### Visual Accessibility

1. Text and digit content maintain contrast ≥4.5:1 against backgrounds; error messages and icons meet ≥4.5:1 contrast.
2. Digit field borders and focus indicators maintain ≥3:1 contrast against adjacent colors.
3. Error states use red borders plus error icon and text message, not relying on color alone to convey the error.
4. Support text resizing to 200% without loss of functionality; digit fields reflow to maintain usability.
5. Respect `prefers-reduced-motion` by avoiding auto-advance animations if reduced motion is preferred.

---

### Error Handling

1. Apply `aria-invalid="true"` to all digit fields when the code fails validation.
2. Link the error message to all digit fields using `aria-describedby` with a stable ID for the error text container.
3. Announce errors via `aria-live="assertive"` immediately after validation, describing the specific issue (e.g., "Invalid code" or "Code expired").
4. Return focus to the first digit field after error announcement so users can immediately retry.
5. Clear `aria-invalid` and hide error messages once the user begins entering a new code.

---

### Testing Checklist

**Quick Tests (≤5 minutes)**

1. Navigate through all digit fields using only `Tab`, number keys, and `Backspace`; verify focus indicators are visible at ≥3:1 contrast.
2. With a screen reader, confirm the group label, helper text, and error messages are announced correctly when navigating fields.
3. Zoom to 200%: all digit fields, helper text, and error messages remain visible and functional without horizontal scrolling.
4. Enable high-contrast mode: verify field borders, focus indicators, and error states remain clearly distinguishable.
5. On a mobile device, confirm the numeric keyboard opens automatically and touch targets meet 44×44px.

**Common Issues to Avoid**

1. Missing `aria-invalid` or `aria-describedby` on digit fields when error state is active.
2. Error state conveyed only by red color without accompanying error text or icon.
3. Focus indicators with insufficient contrast (<3:1) making keyboard navigation difficult to track.
4. Auto-advance behavior that doesn't work correctly with screen readers or keyboard-only users.