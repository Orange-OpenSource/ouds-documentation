# Guideline

## Intro

A password input securely captures confidential passwords while masking characters to protect privacy from nearby observers.

---

## Description

A password input is a form field specifically designed to securely capture a user's confidential password. It masks the characters as they are typed, typically replacing them with dots, in order to protect the input from being read by others nearby.

While the primary goal is to enhance privacy and security, the field may also include usability features such as a "show/hide password" toggle and helper text to guide password creation.

---

## Anatomy

| # | Element | Purpose |
|---|---------|---------|
| 1 | Label | Identifies the field purpose and maintains accessibility |
| 2 | Leading icon | Provides visual context for password entry (optional) |
| 3 | Input container | Houses prefix, masked password text, and placeholder |
| 4 | Password visibility toggle | Allows users to reveal or hide password characters |
| 5 | Helper text | Provides guidance on password requirements or constraints |

---

## Usage & Guidance

### Best for

✅ User authentication and login scenarios
✅ Account creation requiring new password input
✅ Password change or reset flows
✅ Secure credential management interfaces

---

### ⚠️ Label

Describes the purpose of the input. Why hide a password input label?

In some UI contexts, especially when space is limited or when the input is part of a compact layout (search bars, filters, inline forms), visually hiding the label can help maintain a clean and uncluttered interface.

However, hiding the label should only be done if:
• The purpose of the input remains clear thanks to a placeholder or contextual icon.
• The label is still accessible to screen readers (using aria-label, aria-labelledby, or visually hidden text).

Hiding a label is a design choice that must balance visual simplicity and clarity of intent, without compromising inclusiveness or form guidance.

---

### How should I display labels and helper text for a login password field?

Use "Password" as the label with no helper text, since users already know their password and don't need creation guidance.

### What should the error state look like when a password is incorrect during login?

Display a red border with an error message stating "Incorrect password. Please try again" below the field, with the password cleared for re-entry.

### What's the visual difference between a new password field and a confirmation password field?

Use "Create password" for the first field and "Confirm password" for the second, both with identical styling and helper text showing requirements only on the first field.

---

## Screen Sizes

### Desktop

Password inputs maintain full width within their container with ample padding for comfortable interaction.

### Tablet

Components adapt to tablet viewports by maintaining their desktop sizing. Labels and helper text retain their desktop proportions for readability across various tablet orientations.

### Mobile

On mobile devices, password inputs expand to full container width with increased touch target sizes for the visibility toggle (minimum 44x44px). Helper text may wrap to multiple lines when needed, and mobile keyboards automatically configure for password entry with appropriate character access.

---

# Specs

## Properties

### Initial Config

| Property | Default Value | Notes |
|----------|---------------|-------|
| Outlined | Off | Controls whether the input has a visible stroke border or subtle background fill with bottom border |
| Rounded corner | Off | Determines if corners are square (standard) or rounded (for emotional/branded contexts) |
| Input status | Empty | Indicates whether the field contains no content, placeholder text, or filled user input |
| State | Enabled | Defines the current interaction state including enabled, hover, focus, loading, read-only, disabled, or skeleton |
| Error | Off | Controls visibility of error styling and error message below the field |
| Leading icon | Off | Determines whether a contextual icon appears at the start of the input field |
| Hidden password | On | Controls whether password characters are masked with dots or displayed as plain text |
| ⚠️ Label | On | Boolean control for label visibility (should remain on for accessibility unless context is unmistakable) |
| Helper text | Off | Controls whether supporting text appears below the input field |
| Prefix | Off | Determines whether a fixed text prefix appears before user input (rare use cases only) |

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

### Input status

**`Empty`** The Empty state indicates that the password input is blank with no content or placeholder, a neutral starting point.

**`Empty (Placeholder)`** The Empty with Placeholder state provides a hint or guidance inside the field to suggest expected input.

**`Filled`** The Filled state shows that the user has entered valid content into the field, replacing any placeholder.

---

### State

**`Enabled`** Neutral appearance, whether empty or filled. It allows users to click, focus, and type freely without restrictions.

**`Hover`** Slight visual contrast or border color change.

**`Focus`** The password input is focused and ready to receive user input. It visually highlights the field to indicate that it's currently editable and interactive. This state typically appears after a user clicks or taps into the field.

**`Loading`** The Loading state indicates that the system is processing or retrieving data related to the password input. A progress indicator appears to inform the user that an action is in progress. During this state, the input may be temporarily disabled to prevent further interaction.

**`Read only`** Text visible but not editable (often with a muted or different background).

**`Disabled`** The field is non-interactive and grayed out to indicate it cannot be changed. The helper text is muted.

**`Skeleton`** Improves the perceived loading time by providing a visual cue of where field will appear once fully loaded. Uses the "Skeleton" component, variant "Security marge=False".

---

### Error

The Error status indicates that the user input does not meet validation rules or expected formatting. It provides immediate visual feedback, typically through a red border, error icon, and a clear, accessible error message positioned below the input (mandatory).

This state helps users quickly identify and correct mistakes by explaining what went wrong and, when possible, how to fix it. The input remains editable, encouraging users to revise their input without starting over.

**⚠️ Error message vs helper text** The error message is not the same element as the helper text, it is independent. If a helper text accompanies the text input, it is replaced by the error message. The helper text must not be displayed simultaneously.

---

### Leading icon

Helps indicate the purpose of the input (magnifying glass for search, envelope for email, phone device for phone number). Only use a leading icon if it adds clear functional or contextual value.

---

### Other boolean options

**Prefix** A visual or textual element placed before the user's input. A prefix is not common and is discouraged in a Password Input component. Here are illustrative examples of very specific cases where:
• "corp-" Company password enforcing a prefix
• "temp-" Temporary password during a testing phase
• "dev-" For test accounts
• "eu-, us-, prod-, stage-" To encode a target environment
• "test@" Used in the context of automated or predictable tests
• "admin-" Pattern used to define an admin password

**Helper text** Supporting text conveys additional information about the input field, such as how it will be used. It should ideally only take up a single line, though may wrap to multiple lines if required, and be either persistently visible or visible only on focus.

---

# Accessibility

## Accessibility intro

Password inputs must meet WCAG 2.2 Level AA standards for secure credential entry with proper labeling, keyboard navigation, and assistive technology support. For comprehensive accessibility guidance, see the [Orange Unified Design System Accessibility Overview](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability).

---

## Accessibility Challenges

Password inputs present unique accessibility challenges because they mask characters by design, creating tension between security and usability. Users with visual impairments, cognitive disabilities, or motor control issues face heightened difficulty when they cannot see what they've typed, cannot easily toggle visibility, or cannot understand why their password was rejected. The critical success factors involve maintaining security while ensuring all users can successfully enter, verify, and manage their passwords through clear labeling, keyboard access, and informative feedback.

### Key Challenges
- **Character masking** prevents visual verification of input, increasing error risk for users with visual or cognitive impairments
- **Password visibility toggles** must be discoverable and operable by all users regardless of input method
- **Error messages** need to provide specific, actionable guidance without exposing security vulnerabilities
- **Password requirements** must be communicated clearly before users attempt entry

### Critical Success Factors
1. Provide visible, programmatic labels that persist and clearly identify the field as password entry (WCAG 3.3.2)
2. Ensure password visibility toggle buttons are keyboard-accessible with clear announced states (WCAG 2.1.1, 4.1.2)
3. Deliver specific, non-technical error messages that guide users toward correct password format (WCAG 3.3.1, 3.3.3)
4. Support password manager integration and paste functionality for users who rely on assistive tools (WCAG 2.1.1)

---

## Design Requirements

### Structure & Labels
- [ ] **Persistent label**: Visible label remains above or beside the field at all times, programmatically associated via `for`/`id` attributes ([Orange: Labels](https://a11y-guidelines.orange.com/en/web/components-examples/forms/))
- [ ] **Password visibility toggle**: Trailing button with clear icon states (eye/eye-slash) and `aria-label` describing current state (e.g., "Show password" or "Hide password")
- [ ] **Helper text association**: Use `aria-describedby` to link helper text explaining password requirements to the input field ([Orange: Forms](https://a11y-guidelines.orange.com/en/web/components-examples/forms/))

### Visual Design
- [ ] **Focus indicator contrast**: Visible focus ring with minimum 3:1 contrast ratio against adjacent colors, never relying on color alone (WCAG 2.4.7, 1.4.11)
- [ ] **Error state contrast**: Error border and error icon meet 3:1 contrast minimum, with error text meeting 4.5:1 contrast against background (WCAG 1.4.3)
- [ ] **Touch target size**: Password visibility toggle button minimum 44×44px for touch interfaces, 24×24px for desktop with adequate spacing (WCAG 2.5.5)

### Content
- [ ] **Error specificity**: ❌ "Invalid password" / ✅ "Password must be 8-20 characters with at least one number" ([Orange: Error Messages](https://a11y-guidelines.orange.com/en/web/components-examples/forms/))
- [ ] **Helper text timing**: Display password requirements before users begin typing, not only on validation failure

---

## Testing Checklist

### Screen Reader Testing
- [ ] Test with NVDA (Windows), JAWS (Windows), VoiceOver (macOS/iOS), TalkBack (Android) to verify label announces field as "password", helper text reads before entry, error messages announce on validation failure, visibility toggle state changes announce clearly
- [ ] Verify password characters announce as "dot" or "bullet" when masked, actual characters when visible, paste operations announce success

### Keyboard Testing
- [ ] Tab reaches password field and visibility toggle in logical order, Enter submits form from password field, Space activates visibility toggle button, focus remains visible with ≥3:1 contrast throughout
- [ ] Test paste functionality (Ctrl/Cmd+V) works correctly, auto-fill from password managers functions without keyboard traps

### Paste Testing
- [ ] Paste password text correctly fills field, screen reader announces paste success and character count/validation

Resources: [Orange Accessibility Testing Guide](https://a11y-guidelines.orange.com/en/web/test/)

---

## Key WCAG Criteria

- **2.1.1 Keyboard** (A): All password field interactions including typing, visibility toggle, and paste operations work via keyboard without timing requirements
- **2.4.7 Focus Visible** (AA): Visible focus indicator with ≥3:1 contrast appears on password field and visibility toggle button
- **3.3.1 Error Identification** (A): Password validation errors identified in text with specific guidance, associated with input via `aria-describedby`
- **3.3.2 Labels or Instructions** (A): Visible label and helper text provided for password field, available to assistive technology via proper HTML and ARIA
- **4.1.2 Name, Role, Value** (A): Password input uses `type="password"`, visibility toggle communicates state changes, error states update `aria-invalid` attribute

For complete reference: [Orange Accessibility Guidelines - Form Components](https://a11y-guidelines.orange.com/en/web/components-examples/forms/)

---

## Additional Resources

- [Orange Accessibility Guidelines - Forms](https://a11y-guidelines.orange.com/en/web/components-examples/forms/)
- [WCAG 2.2 Understanding Docs - 3.3.1 Error Identification](https://www.w3.org/WAI/WCAG22/Understanding/error-identification.html)
- [WCAG 2.2 Understanding Docs - 3.3.2 Labels or Instructions](https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions.html)
- [Orange Design System - Accessibility & Sustainability](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability)
- [W3C - Accessible Authentication](https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html)
