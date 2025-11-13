# Guideline

## Intro 👈🤖

A single-line text input field for capturing user information like names, emails, or search queries.

---

## Description

A text input is a user interface component that allows users to enter, edit, or select single-line textual data. It's one of the most fundamental form elements used to capture user input such as names, emails, passwords, or search queries.

It provides a visual and interactive affordance for text entry while supporting labels, placeholders, icons, helper messages, and validation feedback.

---

## Anatomy 👈🤖

| # | Element | Purpose |
|---|---------|---------|
| 1 | Label | Identifies the input's purpose and guides user entry |
| 2 | Input field | Container for text entry with background and border |
| 3 | Placeholder | Provides example or hint text within empty field |
| 4 | Leading icon | Optional icon at start indicating input type or function |
| 5 | Trailing action | Optional button/icon at end for actions like clear or submit |
| 6 | Helper text | Supplementary guidance below field explaining format or requirements |
| 7 | Error message | Validation feedback replacing helper text when errors occur |
| 8 | Prefix/Suffix | Fixed text/symbol before or after user input (combined) |

---

## Usage & Guidance

### Best for 👈🤔

✅ Single-line text data entry (names, addresses, email)  
✅ Search functionality with real-time filtering  
✅ Form fields requiring validation feedback  
✅ Inputs needing contextual icons (search, password visibility)  
✅ Fields with standard character limits (under 100 characters)  
✅ Data with specific format requirements (phone, date)  
✅ Inputs requiring clear/reset functionality  
✅ Login credentials and authentication fields  
✅ URL or link entry  
✅ Numeric inputs with fixed units or symbols

---

### ⚠️ Label

Describes the purpose of the input. Why hide a text input label?

In some UI contexts, especially when space is limited or when the input is part of a compact layout (search bars, filters, inline forms), visually hiding the label can help maintain a clean and uncluttered interface.

However, hiding the label should only be done if:
• The purpose of the input remains clear thanks to a placeholder or contextual icon.
• The label is still accessible to screen readers (using aria-label, aria-labelledby, or visually hidden text).

Hiding a label is a design choice that must balance visual simplicity and clarity of intent, without compromising inclusiveness or form guidance.

---

### ⚠️ Mandatory field indication

**If all fields are mandatory (several fields present):**
1. Display the message "All fields are mandatory." at the top.
2. Do not use an asterisk (*) at the end of each field label, nor the word "mandatory."
UI rendering of the asterisk: font-weight-bold + color-content-negative (red).

**If not all fields are mandatory (several fields present):**
1. Display the message "All fields marked with an * are mandatory." at the top.
2. Use an asterisk (*) at the end of each mandatory field label (the word "mandatory" is read aloud instead of the visible asterisk at the end of the label).
UI rendering of the asterisk: font-weight-bold + color-content-negative (red).
3. Use the mention "(optional)" at the end of each optional field label. Note that this rule is not systematic—it remains an option, to be used if needed.

**If there is only one field in the form, or if the mandatory nature is obvious (such as login/password), no mention is necessary since the fields are essential to the form's functionality.**

---

### Label clarity matters most 👈🤔

✅ **Do:** Write labels that clearly describe what data is needed without requiring placeholder text to understand the purpose  
❌ **Don't:** Rely solely on placeholder text to communicate the field's purpose, as placeholders disappear on focus and aren't always accessible

### Keep helper text concise and actionable 👈🤔

✅ **Do:** Use helper text to provide format examples or requirements that help users succeed ("Use format: +33 6 12 34 56 78")  
❌ **Don't:** Write long instructional paragraphs in helper text or repeat information already in the label

### Match error messages to actual problems 👈🤔

✅ **Do:** Provide specific error messages that tell users exactly what's wrong and how to fix it ("Email must include @ symbol")  
❌ **Don't:** Use generic error messages like "Invalid input" that leave users guessing what went wrong

### Use leading icons for clarity, not decoration 👈🤔

✅ **Do:** Add leading icons that reinforce the input type and help users scan forms quickly (search icon for search, lock for password)  
❌ **Don't:** Use decorative icons that don't add meaning or icons that conflict with the label's message

### Position trailing actions where they're expected 👈🤔

✅ **Do:** Place clear/reset actions on the trailing side where users naturally look when they've finished typing  
❌ **Don't:** Add multiple trailing icons that crowd the field or create confusion about which action to take

### Consider the full user journey 👈🤔

✅ **Do:** Show helpful contextual information before errors occur, like character counters approaching limits or format hints while typing  
❌ **Don't:** Wait until validation fails to inform users about requirements they could have met during entry

### Make success states clear and brief 👈🤔

✅ **Do:** Provide quick visual confirmation when validation passes, then let users move forward without distraction  
❌ **Don't:** Keep success messages visible so long that they slow down the user's progress through the form

### Group related fields logically 👈🤔

✅ **Do:** Place related text inputs together with clear section headings and ensure adequate spacing between unrelated groups  
❌ **Don't:** Mix unrelated inputs together or create visual ambiguity about which fields belong to which section

---

### How should I display an empty text input with placeholder text? 👈🤔

Show the label above the field, placeholder text inside using secondary color, and helper text below to guide format expectations.

### How should I configure a text input with a search icon and clear button? 👈🤔

Place a search icon as the leading element and a clear/close icon as the trailing action, with a descriptive label and placeholder for the search context.

### What should the error state look like when validation fails? 👈🤔

Display red border, error icon, and replace helper text with a specific error message explaining what's wrong and how to fix it.

### How do I show a text input in focus state during typing? 👈🤔

Apply prominent border highlight, maintain visible label, hide placeholder text, and show any real-time validation feedback in helper text area.

### How should I display a disabled text input that users cannot edit? 👈🤔

Use reduced opacity for the entire field, gray out text and borders, maintain label visibility, and include disabled cursor behavior.

### How do I configure prefix or suffix for currency or unit inputs? 👈🤔

Place fixed text (like "$" or "kg") as prefix before the input area or suffix after, ensuring it remains static while users type their values.

### What should the loading state look like during validation or data fetch? 👈🤔

Display a loading spinner in the trailing area, keep the field in focus appearance, and maintain any entered text visible during processing.

### How should I handle a text input in read-only mode? 👈🤔

Show the field with filled content but reduced visual emphasis, no focus outline on click, and potentially different background color to indicate non-editable state.

### How do I display a text input with both helper text and character counter? 👈🤔

Position helper text on the left side below the field and character count on the right, both in secondary text style with appropriate spacing.

### What's the correct layout for a text input with required field indication? 👈🤔

Place red asterisk (*) immediately after the label text, maintain proper spacing, and include "All fields marked with an * are mandatory" message at form top.

---

## Screen Sizes

### Desktop 👈🤖
Text inputs display at full width within their container with comfortable touch targets and clear spacing for labels, helper text, and error messages.

### Tablet 👈🤖
Inputs maintain similar layout to desktop but may adjust width to fit multi-column forms, ensuring touch targets remain accessible and icons stay proportional.

### Mobile 👈🤖
Text inputs stack vertically at full width to maximize typing area, with increased touch target sizes for icons and appropriately sized fonts for readability on smaller screens.

---

# Specs

## Properties

### Initial Config

| Property | Default Value | Notes |
|----------|---------------|-------|
| Outlined | False | Uses filled style with background and bottom border by default |
| Rounded corner | False | Square corners are standard unless context requires rounded appearance |
| Input status | Empty | Field starts empty without placeholder unless explicitly configured |
| State | Enabled | Interactive and ready for user input in default state |
| Error | False | No validation error displayed initially |
| Leading icon | False | No icon shown at start of field unless needed for context |
| Trailing action | False | No action button or icon at end unless functionality required |
| ⚠️ Label | True | Label is visible by default for accessibility and clarity |
| Autocompletion | False | Browser autocomplete disabled unless explicitly enabled |
| Prefix | False | No fixed text before input area unless needed for currency/units |
| Suffix | False | No fixed text after input area unless needed for units/domains |
| Helper text | False | No supplementary guidance shown unless needed for format hints |
| Helper link | False | No clickable help link included unless additional resources needed |

---

### Outlined

**`False`** An input with a subtle background fill and un visible bottom border, creating a softer and more contained look. Best suited for dense layouts or to enhance visibility.

**`True`** A minimalist input with a transparent background and a visible stroke outlining the field. This style may be interesting for contexts other than form pages:
• When inputs need to feel lightweight and unobtrusive
• In a header (search field)
• In a selection/filtering feature in a product catalog

---

### Rounded corner

**`False`** An input without rounded corner.

**`True`** An input with a rounded corner. This style may be interesting for contexts other than form pages:
• When inputs need to feel lightweight and unobtrusive
• In a header (search field)
• In a selection/filtering feature in a product catalog

---

### Input status

**`Empty`** An empty input field state with no user-entered content and no placeholder text. Represents the initial state when a form first loads.

**`Empty (Placeholder)`** An empty field displaying placeholder text to guide users on the expected input format or purpose. The placeholder disappears when the user starts typing.

**`Filled`** A field containing user-entered text or pre-populated data. This state indicates that the field has been successfully engaged with and contains information.

---

### State

**`Enabled`** The default interactive state where users can click into the field and begin typing. The field responds to hover, focus, and input events. This represents a fully functional, ready-to-use state.

**`Hover`** The appearance of the input when the cursor is positioned over the field but hasn't clicked yet. Provides visual feedback that the field is interactive and can be selected. Typically shows subtle styling changes like border color shifts.

**`Focus`** The active editing state when a user has clicked into the field and can type. The field displays a prominent focus indicator (like a border highlight) to show it's currently selected. This state receives all keyboard input.

**`Loading`** The state shown when the system is processing input-related actions, such as validating data, fetching autocomplete suggestions, or performing real-time checks. Usually displays a loading spinner or progress indicator while preserving the field's content.

**`Read only`** A view-only state displaying static information that users cannot modify. The field appears with reduced visual emphasis to indicate its non-editable nature. Useful for displaying confirmation details or information that shouldn't be changed.

**`Disabled`** An inactive state where the field is visible but completely non-interactive. Typically shown in greyed-out styling to clearly communicate unavailability. Used when a field is not applicable to the current workflow or lacks necessary permissions.

**`Skeleton`** A loading placeholder state displayed before actual content loads. Shows an animated shimmer or gradient effect as a temporary visual while waiting for field initialization or data retrieval. Part of the skeleton loading pattern for perceived performance.

---

### Error

**`False`** The field is in a valid state with no validation errors. Displays the standard appearance without any error indicators or messaging. Used when input meets all requirements or hasn't been validated yet.

**`True`** The validation error state showing that the input doesn't meet requirements. Displays error styling (typically red borders), error messages explaining the issue, and potentially error icons. Used after validation fails to guide users toward correct input. Error messages should be clear, specific, and actionable to help users fix the issue.

---

### Leading icon

**`False`** The input field displays without a leading icon, showing only the text container and label. This is the default configuration for most basic input fields.

**`True`** The input includes a functional icon positioned at the start of the field, before the user's text entry area. Leading icons help users quickly identify the input's purpose (like a search icon for search fields or a lock for password inputs).

---

### Trailing action

**`False`** The input displays without any trailing action button or icon. This is the standard configuration where the field ends with just the text entry area.

**`True`** The input includes an interactive element (button or icon) positioned at the end of the field, after the text entry area. Common trailing actions include clear/reset buttons, password visibility toggles, or submit/search buttons.

---

### Other boolean options

**⚠️ Label** Describes the purpose of the input. Includes a warning symbol to indicate this is an important field property with accessibility implications.

**Autocompletion** Enables or disables autocomplete suggestions that appear as the user types, offering relevant options based on past inputs or system data.

**Prefix** Adds a fixed text or symbol before the user's input value (like currency symbols "$" or units "kg"). The prefix remains static while the user types.

**Suffix** Adds a fixed text or symbol after the user's input value (like domain extensions ".com" or percentage symbols "%"). The suffix remains static while the user types.

**Helper text** Displays supplementary guidance below the input field to clarify expected format, provide examples, or offer contextual help. This text supports users in completing the field correctly.

**Helper link** Provides a clickable link below the input field that directs users to additional information, documentation, or assistance related to filling out the field.

---

# Accessibility 👈🤖

## Accessibility intro

Text inputs must meet WCAG 2.2 Level AA requirements for keyboard operability, clear labeling, visible focus indicators, and accessible error messaging. For comprehensive accessibility guidance, see the [Orange Unified Design System Accessibility Overview](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability).

---

## Accessibility Challenges

Text inputs present accessibility challenges because they require clear purpose identification, keyboard navigation, visible focus indication, meaningful error communication, and proper state announcements for users who cannot see visual cues or use a mouse.

### Key Challenges
- Labels must remain visible and programmatically associated with inputs to communicate purpose
- Error messages need both visual and programmatic connection to failed inputs for screen reader users
- Focus indicators must maintain sufficient contrast across all states and themes
- Dynamic content changes (loading, error states) require live region announcements

### Critical Success Factors
1. Visible and persistent labels with proper `for`/`id` associations (WCAG 3.3.2)
2. Error messages linked via `aria-describedby` and identified in text (WCAG 3.3.1)
3. Focus visible with ≥3:1 contrast ratio against background (WCAG 2.4.7)
4. All functionality keyboard-accessible without timing requirements (WCAG 2.1.1)

---

## Design Requirements

### Structure & Labels
- [ ] **Visible label required**: Always display label text above or beside input, never rely solely on placeholder ([Orange Forms Guidelines](https://a11y-guidelines.orange.com/en/web/components-examples/forms/))
- [ ] **Label association**: Ensure label `for` attribute matches input `id` for screen reader connection
- [ ] **Required field indication**: Use both asterisk (*) and explanatory text at form top for mandatory fields

### Visual Design
- [ ] **Focus indicator contrast**: Focus outline must have ≥3:1 contrast ratio against background ([Orange Focus Visible](https://a11y-guidelines.orange.com/en/web/design/focus-visible/))
- [ ] **Error state distinction**: Red error borders alone insufficient—include error icon and text message
- [ ] **Touch target size**: Minimum 44×44px touch target for mobile including icons and trailing actions

### Content
- [ ] **Clear error messages**: ❌ "Invalid input" / ✅ "Email must include @ symbol" ([Orange Error Messages](https://a11y-guidelines.orange.com/en/web/components-examples/forms/))
- [ ] **Helper text clarity**: Provide format examples in helper text before validation, not just error messages after

---

## Testing Checklist

### Screen Reader Testing
- [ ] Test with NVDA (Windows), JAWS (Windows), VoiceOver (macOS/iOS), TalkBack (Android) to verify labels announced correctly, error messages read when present, helper text available, state changes communicated
- [ ] Verify placeholder text does not replace label announcements and required field status is indicated

### Keyboard Testing
- [ ] Tab navigation focuses input, Enter submits form (if applicable), Escape clears focus—all functionality keyboard-accessible
- [ ] Verify focus visible with ≥3:1 contrast across all states (enabled, hover, error)

### Paste Testing
- [ ] Paste functionality works correctly and announces changes to screen readers when content is pasted

Resources: [Orange Accessibility Testing Guide](https://a11y-guidelines.orange.com/en/web/test/)

---

## Key WCAG Criteria

- **2.1.1 Keyboard** (A): All text input functionality operable via keyboard without timing requirements, including focus, typing, clearing, and form submission
- **2.4.7 Focus Visible** (AA): Visible focus indicator with ≥3:1 contrast ratio maintained across all input states and color schemes
- **3.3.1 Error Identification** (A): Errors identified in text and associated with specific inputs via `aria-describedby` referencing error message ID
- **3.3.2 Labels or Instructions** (A): Visible labels provided for all inputs with programmatic association via `for`/`id` attributes, never hidden or replaced by placeholders
- **4.1.2 Name, Role, Value** (A): Semantic `<input>` elements with correct `type` attributes and ARIA attributes (`aria-invalid`, `aria-describedby`, `aria-required`) communicate state changes

For complete reference: [Orange Accessibility Guidelines - Forms](https://a11y-guidelines.orange.com/en/web/components-examples/forms/)

---

## Additional Resources

- [Orange Accessibility Guidelines - Forms Examples](https://a11y-guidelines.orange.com/en/web/components-examples/forms/)
- [WCAG 2.2 Understanding Docs - Input Purpose](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html)
- [Orange Design System - Accessibility & Sustainability](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability)
- [Orange Focus Visible Guidelines](https://a11y-guidelines.orange.com/en/web/design/focus-visible/)
- [Orange Error Message Guidelines](https://a11y-guidelines.orange.com/en/web/components-examples/forms/)