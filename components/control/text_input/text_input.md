# Guideline

## Intro 👈🤖

A text input enables users to enter or edit single-line text such as names, emails, passwords, or search queries.

---

## Description

A text input is a user interface component that allows users to enter, edit, or select single-line textual data. It's one of the most fundamental form elements used to capture user input such as names, emails, passwords, or search queries.

It provides a visual and interactive affordance for text entry while supporting labels, placeholders, icons, helper messages, and validation feedback.

---

## Anatomy 👈🤖

| # | Element | Purpose |
|---|---------|---------|
| 1 | Label | Identifies the input's purpose; can be hidden visually but must remain accessible |
| 2 | Input field | Container where users type, edit, or view text content |
| 3 | Placeholder | Optional hint text suggesting expected input format or example |
| 4 | Leading icon | Optional visual indicator of input purpose (search, email, phone) |
| 5 | Trailing action | Optional interactive element (clear, visibility toggle, picker trigger) |
| 6 | Helper text/Error message | Supporting guidance or validation feedback below the field |
| 7 | Prefix/Suffix (combined) | Optional formatting indicators (country code, currency, units) |
| 8 | Autocompletion | Optional predictive suggestions appearing inline or in dropdown |

---

## Usage & Guidance

### Best for 👈🤔

✅ Single-line text entry such as names, emails, phone numbers, or search terms  
✅ Fields requiring format indicators like currency codes, units, or country prefixes  
✅ Inputs benefiting from autocompletion to reduce typing and errors  
✅ Forms where inline validation provides immediate feedback on correctness  
✅ Password fields with visibility toggle for security and usability balance  
✅ Search bars in headers or toolbars requiring lightweight, unobtrusive appearance  
✅ Read-only fields displaying non-editable information within form context  
✅ Filter controls in product catalogs or data tables needing compact design  
✅ Loading states where data retrieval requires temporary input prevention  
✅ Skeleton loading to improve perceived performance before content appears

---

### ⚠️ Label

Describes the purpose of the input. Why hide a text input label?

In some UI contexts, especially when space is limited or when the input is part of a compact layout (search bars, filters, inline forms), visually hiding the label can help maintain a clean and uncluttered interface.

However, hiding the label should only be done if:
• The purpose of the input remains clear thanks to a placeholder or contextual icon.
• The label is still accessible to screen readers (using aria-label, aria-labelledby, or visually hidden text).

Hiding a label is a design choice that must balance visual simplicity and clarity of intent, without compromising inclusiveness or form guidance.

---

### Clear purpose through labeling 👈🤔

✅ **Do:** Write labels that clearly describe what information users should provide, keeping them visible unless context makes purpose obvious  
❌ **Don't:** Hide labels in complex forms or rely solely on placeholders, which disappear on input and harm accessibility

### Strategic icon usage 👈🤔

✅ **Do:** Add leading icons only when they reinforce field purpose (magnifying glass for search, envelope for email)  
❌ **Don't:** Use decorative icons that add no functional value or create visual clutter in dense form layouts

### Helper text timing 👈🤔

✅ **Do:** Display helper text persistently when users need format guidance before typing, or show on focus for secondary tips  
❌ **Don't:** Replace critical formatting instructions with error messages after submission—guide users proactively

### Error message clarity 👈🤔

✅ **Do:** Write error messages that explain what's wrong and how to fix it, replacing helper text but keeping helper links visible  
❌ **Don't:** Show generic errors like "Invalid input" or display helper text simultaneously with error messages

### Trailing action purpose 👈🤔

✅ **Do:** Provide functional trailing actions like clear input, password toggle, or date picker that directly support data entry  
❌ **Don't:** Add trailing elements that don't perform actions or create confusion about field interactivity

### Placeholder as enhancement 👈🤔

✅ **Do:** Use placeholders to show input format examples (555-123-4567) while keeping labels visible for field identity  
❌ **Don't:** Treat placeholders as label replacements or include critical instructions that vanish when users start typing

### Prefix and suffix context 👈🤔

✅ **Do:** Display prefixes/suffixes when formatting context is essential (currency codes, measurement units, country codes)  
❌ **Don't:** Add prefixes or suffixes that duplicate information already clear from label or create input confusion

### Loading state transparency 👈🤔

✅ **Do:** Show loading indicators when processing takes more than a moment, preventing user interaction during data retrieval  
❌ **Don't:** Leave fields enabled during loading or fail to communicate that system processing is occurring

### Read-only vs disabled distinction 👈🤔

✅ **Do:** Use read-only for reference data users need to see but can't change; use disabled for truly unavailable fields  
❌ **Don't:** Disable fields containing important information users need to read or copy

### Autocompletion value 👈🤔

✅ **Do:** Implement autocompletion for predictable inputs like addresses, emails, or common search terms to speed entry  
❌ **Don't:** Add autocompletion to creative fields requiring unique input or when suggestions would confuse rather than help

---

### How should I configure a text input for email address entry? 👈🤔

Display a label "Email address," an optional leading envelope icon, a placeholder showing format (name@example.com), and helper text noting "We'll use this for account recovery."

### What should the error state look like when an email format is invalid? 👈🤔

Show red border, error icon as trailing element, and error message "Enter a valid email address like name@example.com" replacing helper text below the field.

### How do I display a text input with autocompletion for address entry? 👈🤔

Include a label "Street address," show placeholder "Start typing your address," and display dropdown suggestions as user types with matching text highlighted in each option.

### How should I configure a password input with visibility toggle? 👈🤔

Show label "Password," use password masking (•••), add eye icon as trailing action to toggle visibility, and include helper text "At least 8 characters with one number."

### What does a loading state look like while validating user input? 👈🤔

Display normal field appearance with loading spinner as trailing element, prevent editing, and show helper text "Checking availability..." below the field.

### How do I configure a search input for a header navigation? 👈🤔

Use outlined variant with transparent background, magnifying glass leading icon, placeholder "Search products," and optional clear button as trailing action when filled.

### How should I display a currency amount input with prefix? 👈🤔

Show label "Amount," dollar sign prefix before input area, placeholder "0.00," and optional helper text "Minimum $10.00" below the field.

### What's the visual difference between read-only and disabled states? 👈🤔

Read-only shows normal text color with muted background and no cursor change; disabled uses grayed-out text, muted background, and grayed helper text.

### How do I configure a phone number input with country code prefix? 👈🤔

Display label "Phone number," country code prefix "+1" before input area, placeholder "555-123-4567," and optional helper text "We'll only contact you about your order."

### How should skeleton loading appear for a form with multiple text inputs? 👈🤔

Show gray animated placeholder rectangles matching input field dimensions with label positions above, maintaining form layout structure before actual content loads.

---

## Screen Sizes

### Desktop 👈🤖

Text inputs display at full width within their container or with fixed maximum widths appropriate to expected content length (narrower for zip codes, wider for addresses). Labels appear above fields with helper text below, and all interactive states maintain clear visual affordances at standard mouse pointer sizes.

### Tablet 👈🤖

Text inputs adapt to available space, typically using full-width layouts in portrait orientation while potentially using side-by-side layouts in landscape for shorter fields. Touch targets for trailing actions increase slightly, and on-screen keyboards appear automatically on focus without obscuring the field.

### Mobile 👈🤖

Text inputs use full-width layouts to maximize touch targets and readability, with increased padding for finger-friendly interaction. Labels remain above fields, helper text appears below, and the mobile keyboard optimizes to input type (email, number, URL) while the viewport adjusts to keep the focused field visible above the keyboard.

---

# Specs

## Properties

### Initial Config

| Property | Default Value | Notes |
|----------|---------------|-------|
| Outlined | False | Subtle background with bottom border creates contained appearance; True provides transparent background with stroke outline |
| Rounded corner | False | Square corners for standard contexts; True for brand-specific or emotional contexts |
| Input status | Empty | Neutral starting state with no content or placeholder text |
| State | Enabled | Field is interactive and ready for user input |
| Error | False | No validation error present; True displays error styling and message |
| Leading icon | False | No icon displayed before input area |
| Trailing action | False | No interactive element after input area |
| ⚠️ Label | True (boolean) | Label is displayed by default; hide only when context makes purpose obvious |
| Autocompletion | False | Predictive suggestions disabled by default |
| Prefix | False | No formatting element before user input |
| Suffix | False | No formatting element after user input |
| Helper text | False | Supporting guidance text not displayed by default |
| Helper link | False | Additional help link not displayed by default |

---

### Outlined

**`False`** An input with a subtle background fill and visible bottom border, creating a softer and more contained look. Best suited for dense layouts or to enhance visibility.

**`True`** A minimalist input with a transparent background and a visible stroke outlining the field.

This style may be interesting for contexts other than form pages:
• When inputs need to feel lightweight and unobtrusive
• In a header (search field)
• In a selection/filtering feature in a product catalog

---

### Rounded corner

**`False`** For a square finish.

**`True`** For a finish with rounded corner.

To be favored in more emotional, immersive contexts or those tied to specific visual identities. For standard or business-oriented journeys, keep the default corners. This evolution addresses the need for flexibility in adapting the design to certain brand contexts.

---

### Input status

**`Empty`** The Empty state indicates that the text input is blank with no content or placeholder, a neutral starting point.

**`Empty (Placeholder)`** The Empty with Placeholder state provides a hint or guidance inside the field to suggest expected input.

**`Filled`** The Filled state shows that the user has entered valid content into the field, replacing any placeholder.

---

### States

**`Enabled`** Neutral appearance, whether empty or filled.

It allows users to click, focus, and type freely without restrictions.

**`Hover`** Slight visual contrast or border color change.

**`Focus`** The text input is focused and ready to receive user input.

It visually highlights the field to indicate that it's currently editable and interactive. This state typically appears after a user clicks or taps into the field.

**`Loading`** The Loading state indicates that the system is processing or retrieving data related to the text input.

A progress indicator appears to inform the user that an action is in progress. During this state, the input may be temporarily disabled to prevent further interaction.

**`Read only`** Text visible but not editable (often with a muted or different background).

**`Disabled`** The field is non-interactive and grayed out to indicate it cannot be changed. The helper text is muted.

**`Skeleton`** Improves the perceived loading time by providing a visual cue of where field will appear once fully loaded.

Uses the "Skeleton" component, variant "Security marge=False".

---

### Error

The Error status indicates that the user input does not meet validation rules or expected formatting. It provides immediate visual feedback, typically through a red border, error icon, and a clear, accessible error message positioned below the input (mandatory).

This state helps users quickly identify and correct mistakes by explaining what went wrong and, when possible, how to fix it.

The input remains editable, encouraging users to revise their input without starting over.

**⚠️ Error message vs helper text / link**

The error message is not the same element as the helper text, it is independent. If a helper text accompanies the text input, it is replaced by the error message. The helper text must not be displayed simultaneously. However, a helper link must not be replaced and should remain positioned below the error message.

---

### Leading icon

Helps indicate the purpose of the input (magnifying glass for search, envelope for email, phone device for phone number). Only use a leading icon if it adds clear functional or contextual value.

---

### Trailing action

Used to provide actions related to the field: clear input, toggle password visibility, open a date picker, etc. Can also indicate status or feedback (error checkmark, loading spinner).

---

### Other boolean options

**Autocompletion** Provides suggested values as the user types. Displays inline text predictions within the input field and/or a dropdown menu of predictive options to speed up input and reduce errors.

**Prefix** A visual or textual element placed before the user's input.

Commonly used to indicate expected formatting like a country code, a unit...

**Suffix** An element placed after the user's input, often used to display a currency or a unit (kg, %, cm...).

**Helper text** Supporting text conveys additional information about the input field, such as how it will be used. It should ideally only take up a single line, though may wrap to multiple lines if required, and be either persistently visible or visible only on focus.

**Helper link** If the helper text is not sufficient (It can also be displayed on its own without helper text), it's possible to offer the user an additional help link (the link can be external or open a modal).

---

# Accessibility 👈🤖

## Accessibility intro

Text inputs must ensure WCAG 2.2 Level AA compliance through proper labeling, keyboard operability, clear error identification, and sufficient contrast for all states. For comprehensive accessibility guidance, see the [Orange Unified Design System Accessibility Overview](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability).

---

## Accessibility Challenges

Text inputs are deceptively complex from an accessibility perspective because they combine multiple interactive elements (field, icons, buttons), dynamic states (empty, filled, error, loading), and critical form semantics that must be correctly communicated to assistive technologies. The challenge intensifies when labels are hidden, errors appear dynamically, or autocompletion introduces live updates that screen readers must announce appropriately.

### Key Challenges
- **Label visibility vs. accessibility**: Hidden labels require correct ARIA implementation to remain discoverable by screen readers
- **Dynamic error communication**: Error messages must be programmatically associated and announced immediately without disrupting user flow
- **Multi-element coordination**: Leading icons, trailing actions, prefixes, and suffixes must not confuse assistive technology navigation
- **State change announcements**: Loading, validation, and autocompletion updates must be communicated via live regions without overwhelming users

### Critical Success Factors
1. **Proper labeling structure** with visible or ARIA-labeled alternatives that clearly identify field purpose (WCAG 3.3.2)
2. **Explicit error association** using `aria-describedby` to link validation messages and `aria-invalid` to mark error state (WCAG 3.3.1)
3. **Keyboard operability** for all interactive elements including trailing actions and autocompletion selection (WCAG 2.1.1)
4. **Focus visibility** with ≥3:1 contrast focus indicators on all states (WCAG 2.4.7)

---

## Design Requirements

### Structure & Labels
- [ ] **Label association**: Every text input must have a label element properly associated via `for`/`id` or contain label text ([Orange Forms Guidelines](https://a11y-guidelines.orange.com/en/web/components-examples/forms/))
- [ ] **Hidden label accessibility**: When labels are visually hidden, provide `aria-label` or `aria-labelledby` referencing visually-hidden text ([Orange ARIA Guidelines](https://a11y-guidelines.orange.com/en/web/components-examples/accessible-hiding/))
- [ ] **Helper text linkage**: Connect helper text and error messages to input using `aria-describedby` for screen reader announcement

### Visual Design
- [ ] **Focus indicator contrast**: Focus state border/outline must have ≥3:1 contrast against adjacent colors ([Orange Color Contrast](https://a11y-guidelines.orange.com/en/web/design/colors-and-contrasts/))
- [ ] **Text contrast ratios**: Input text ≥4.5:1, placeholder text ≥4.5:1, disabled text ≥3:1 against backgrounds
- [ ] **Interactive target size**: Touch/click targets for trailing actions and icons must be ≥44×44 CSS pixels on mobile

### Content
- [ ] **Error message quality**: ❌ "Invalid" / ✅ "Enter a valid email address like name@example.com" ([Orange Error Messages](https://a11y-guidelines.orange.com/en/web/components-examples/forms/))
- [ ] **Placeholder limitations**: Placeholders show examples only; critical instructions belong in labels or helper text

---

## Testing Checklist

### Screen Reader Testing
- [ ] Test with NVDA (Windows), JAWS (Windows), VoiceOver (macOS/iOS), TalkBack (Android) verifying label announcement, current value reading, state communication, helper text/error message reading, and autocompletion option announcement
- [ ] Verify hidden labels are announced, error states trigger immediate notification, and loading states communicate processing

### Keyboard Testing
- [ ] Tab reaches input, focus visible (≥3:1), trailing actions keyboard-accessible (Tab or arrow keys), autocompletion navigable (arrow keys), selection via Enter/Space
- [ ] Verify no keyboard traps, Escape clears autocompletion, and all functionality operable without mouse

### Paste Testing
- [ ] Paste via Ctrl+V/Cmd+V works correctly, pasted content announced to screen readers, validation triggered appropriately

Resources: [Orange Accessibility Testing Guide](https://a11y-guidelines.orange.com/en/web/toolbox/methods-and-test-tools/)

---

## Key WCAG Criteria

- **2.1.1 Keyboard** (A): All input functionality, trailing actions, and autocompletion operable via keyboard without timing requirements
- **2.4.7 Focus Visible** (AA): Visible focus indicator with ≥3:1 contrast on input field and all interactive elements
- **3.3.1 Error Identification** (A): Errors identified in text, associated with inputs via `aria-describedby`, and marked with `aria-invalid="true"`
- **3.3.2 Labels or Instructions** (A): Labels provided for all inputs, visible or available via ARIA, with sufficient instructions for expected format
- **4.1.2 Name, Role, Value** (A): Correct semantic HTML (`<input>`, `<label>`) and ARIA attributes communicate states (error, loading, disabled) to assistive technology

For complete reference: [Orange Accessibility Guidelines - WCAG Criteria](https://a11y-guidelines.orange.com/en/web/components-examples/)

---

## Additional Resources

- [Orange Accessibility Guidelines - Forms Examples](https://a11y-guidelines.orange.com/en/web/components-examples/forms/)
- [Orange Accessibility Guidelines - Accessible Hiding](https://a11y-guidelines.orange.com/en/web/components-examples/accessible-hiding/)
- [WCAG 2.2 Understanding - Input Purpose](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html)
- [Orange Design System - Accessibility & Sustainability](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability)
- [Orange Color and Contrast Guidelines](https://a11y-guidelines.orange.com/en/web/design/colors-and-contrasts/)