I'll generate the design system documentation for the PIN Code Input component using the uploaded document as the primary source and the Figma link as supplementary reference.

Let me first fetch the Figma data to see if there are any visual assets or additional context:Let me get a screenshot to see the visual examples:Perfect! Now I have both the source documentation and visual references. Let me generate the complete documentation:

---

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

---

# Specs

## Properties

### Initial Config

| Property | Default Value | Notes |
|----------|---------------|-------|
| Outlined | False | Uses filled style with background; set to True for transparent background with stroke outline |
| Rounded corner | False | Square corners by default; set to True for rounded corners in emotional or brand-specific contexts |
| Length | 6 | Standard 6-digit code; change to 4 for simple PINs or 8 for enhanced security scenarios |
| Error | False | Normal state by default; set to True to display validation errors with red styling and error message |
| Helper text | False | Hidden by default; enable to show supporting text about code format or source below the input fields |

### Property Details

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

### Length

**`4`** Four individual input fields for simple 4-digit PINs or quick verification codes.

**`6`** Six individual input fields for standard authentication codes, commonly used for SMS or email verification.

**`8`** Eight individual input fields for enhanced security scenarios requiring longer codes.

---

### Error

The Error status indicates that the user input does not meet validation rules or expected formatting. It provides immediate visual feedback, typically through a red border, error icon, and a clear, accessible error message positioned below the input (mandatory).

This state helps users quickly identify and correct mistakes by explaining what went wrong and, when possible, how to fix it. The input remains editable, encouraging users to revise their input without starting over.

The error state must be triggered by an explicit validation (submission, API response), and not in real time with each keystroke. This can occur either because the entered code does not match the expected code, because the user entered an expired or already used code, or finally if the maximum number of attempts has been exceeded.

⚠️ **Alert:** In the context of a PIN code input, in addition to the input's "Error" UI rendering, it is essential to also include an "Alert" component (also in its "Error" status) in the interface.

---

### Helper text

**Helper text** Supporting text conveys additional information about the input field, such as how it will be used. It should ideally only take up a single line, though may wrap to multiple lines if required, and be either persistently visible or visible only on focus.

---

# Accessibility

### Keyboard Support

1. Press `Tab` to focus the first empty input field in the sequence; press `Shift+Tab` to move focus backward through fields.
2. Type a numeric digit (0-9) to fill the current field and automatically advance focus to the next empty field.
3. Press `Backspace` to clear the current field and move focus to the previous field if the current field is empty.
4. Press arrow keys (`ArrowLeft`, `ArrowRight`) to manually navigate between input fields without deleting content.
5. Provide a visible focus indicator with outline or border ≥2px and contrast ≥3:1 on the currently active input field.
6. Press `Enter` to submit the complete code once all fields are filled (if auto-submit is not enabled).

---

### Screen Reader Experience

1. Use semantic `<input type="text" inputmode="numeric">` elements for each digit field with `maxlength="1"`.
2. Provide a group label using `role="group"` with `aria-labelledby` pointing to the main label text (e.g., "Enter 6-digit verification code").
3. Announce the field position and total count using `aria-label` on each input (e.g., "Digit 1 of 6", "Digit 2 of 6").
4. Apply `aria-invalid="true"` to all input fields when in error state and link error message using `aria-describedby`.
5. Announce error messages immediately using `aria-live="assertive"` and provide specific feedback about what went wrong (incorrect code, expired, attempts exceeded).
6. Announce successful code entry using `aria-live="polite"` when validation passes and next action is available.

---

### Touch & Mobile

1. Provide touch targets ≥44×44px for each input field with spacing ≥8px between fields to prevent accidental touches.
2. Trigger numeric keyboard automatically using `inputmode="numeric"` or `type="tel"` to optimize for digit entry on mobile devices.
3. Support auto-advance between fields on digit entry to reduce the need for manual navigation taps.
4. Ensure the entire component remains visible when the mobile keyboard appears; adjust viewport scroll if necessary.
5. Support both portrait and landscape orientations without loss of functionality or field visibility.

---

### Visual Accessibility

1. Ensure text and digit content have contrast ≥4.5:1 against background; labels and helper text must meet the same ratio.
2. Ensure input field borders, focus indicators, and error state borders have contrast ≥3:1 against adjacent surfaces.
3. Do not rely on color alone to convey error state; include error icon and descriptive error message text below the fields.
4. Support text resizing up to 200% without loss of content, functionality, or horizontal scrolling (reflow must pass).
5. Respect `prefers-reduced-motion` and avoid auto-advance animations or transitions that rely on motion to convey state changes.

---

### Error Handling

1. Apply `aria-invalid="true"` to all input fields in the group when the complete code fails validation.
2. Link the error message to all inputs using `aria-describedby` with a stable ID referencing the error text element.
3. Announce errors immediately via `aria-live="assertive"` after validation fails and return focus to the first input field for correction.
4. Provide specific, actionable error messages: "Incorrect code. Please try again" or "Code expired. Request a new code" instead of generic "Error".
5. Announce success state using `aria-live="polite"` when the correct code is entered and describe the next step in the flow.
6. Clear all fields or maintain entered values based on security requirements when displaying errors; document this behavior clearly.

---

### Testing Checklist

**Quick Tests (≤5 minutes)**

1. Complete digit entry using keyboard only with visible focus moving sequentially; `Backspace` navigates backward correctly.
2. Screen reader announces each field position ("Digit 1 of 6"), group label, and error messages immediately upon validation failure.
3. Zoom to 200%: all input fields remain visible and functional without horizontal scrolling; layout reflows appropriately.
4. High-contrast mode: focus indicators, field borders, and error states remain clearly visible with ≥3:1 contrast.
5. On touch device: numeric keyboard opens automatically; targets are ≥44×44px; auto-advance works between fields.

**Common Issues to Avoid**

1. Missing group label or individual field position announcements for screen reader users.
2. Color-only error indication without accompanying error icon or descriptive error message text.
3. Missing `aria-invalid="true"` or `aria-describedby` linking error message to input fields in error state.
4. Insufficient contrast (<3:1) for focus indicators or error state borders against background.
5. Focus trap within digit fields preventing users from navigating to submit button or other page elements.
6. Auto-advance not working or moving focus before users can correct a mistyped digit.