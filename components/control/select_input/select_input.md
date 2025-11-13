# Guideline

## Intro 👈🤖

A dropdown menu component that allows users to choose one option from a predefined list of standardized values.

---

## Description

A select input is a form component that allows users to choose one (or sometimes multiple) options from a predefined list. It is typically rendered as a dropdown menu that displays available choices when interacted with, either by click or keyboard navigation.

This component is used when the number of choices is limited and known in advance and when users should select from controlled or standardized values.

---

## Anatomy 👈🤖

| # | Element | Purpose |
|---|---------|---------|
| 1 | Label | Identifies the purpose and content expected in the select field |
| 2 | Leading icon (optional) | Provides visual context about the input field's purpose or category |
| 3 | Input field | Contains the selected option text or placeholder, indicating the current selection state |
| 4 | Dropdown indicator | Shows that additional options are available and indicates the expanded/collapsed state |
| 5 | Helper text (optional) | Provides additional guidance, format requirements, or contextual information |
| 6 | Error text (conditional) | Replaces helper text to display specific validation error messages |
| 7 | Dropdown menu | Displays the list of available options when expanded |
| 8 | Option items | Individual selectable choices within the dropdown menu |

---

## Usage & Guidance

### Best for 👈🤔

✅ Selecting from a predefined list of 5-15 standardized options (countries, languages, categories)
✅ Form fields requiring controlled vocabulary to ensure data consistency
✅ Situations where users need to see all available options before choosing
✅ Single-selection scenarios where radio buttons would take too much space
✅ Filter controls in product catalogs, search interfaces, or data tables
✅ Settings and configuration screens with multiple discrete choices
✅ Mobile interfaces where dropdown behavior is native and familiar
✅ Location selection (city, region, timezone) where options are predefined
✅ Date components (month, year selection) within date pickers
✅ Status or category assignment in forms and workflows

---

### ⚠️ Label

Describes the purpose of the input. Why hide a select input label?
In some UI contexts, especially when space is limited or when the input is part of a compact layout (filters, inline forms), visually hiding the label can help maintain a clean and uncluttered interface.
However, hiding the label should only be done if:
• The purpose of the input remains clear thanks to a contextual icon.
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

### Context before selection 👈🤔

✅ **Do:** Provide clear labels and helper text explaining what users are selecting and why it matters for their task flow  
❌ **Don't:** Launch users directly into selection without explaining the consequences or purpose of their choice

### Default selection strategy 👈🤔

✅ **Do:** Pre-select the most common or safest option when there's a clear default choice that applies to most users  
❌ **Don't:** Force users to make a selection when no reasonable default exists or when the choice is critical to user intent

### Option organization 👈🤔

✅ **Do:** Order options logically (alphabetically, by popularity, or by task frequency) to reduce cognitive load and scanning time  
❌ **Don't:** Present options in random order or bury the most likely selections deep in long lists

### Error messaging clarity 👈🤔

✅ **Do:** Display specific, actionable error messages that explain what went wrong and how to fix it immediately below the field  
❌ **Don't:** Show generic "invalid selection" messages that leave users confused about what action to take next

### Loading state communication 👈🤔

✅ **Do:** Show loading indicators when options are being fetched asynchronously, with estimated wait time if known  
❌ **Don't:** Display an empty dropdown or frozen interface that makes users wonder if the component is broken

### Placeholder text usage 👈🤔

✅ **Do:** Use placeholder text like "Select an option" to indicate the field's purpose when no selection has been made  
❌ **Don't:** Use placeholders as a replacement for labels or include critical instructions that disappear once an option is selected

### Option label length 👈🤔

✅ **Do:** Keep option labels concise and scannable, ideally under 40 characters, to enable quick decision-making  
❌ **Don't:** Write lengthy option descriptions that require horizontal scrolling or make the dropdown menu difficult to navigate

### Search functionality threshold 👈🤔

✅ **Do:** Add search/filter capability (combobox) when the list exceeds 15 options to improve findability and reduce scrolling  
❌ **Don't:** Force users to scroll through 50+ options without any search or filtering mechanism

### Mobile consideration 👈🤔

✅ **Do:** Test that native mobile pickers work smoothly and that touch targets for the dropdown indicator are at least 44×44px  
❌ **Don't:** Implement custom dropdowns on mobile that override the native OS picker behavior users expect

### Read-only vs disabled distinction 👈🤔

✅ **Do:** Use read-only state to display a selection that users need to see but cannot change in the current context  
❌ **Don't:** Use disabled state when the value is relevant information—disabled implies unavailability, not immutability

---

### How should I configure a select input for country selection in a shipping form? 👈🤔

The label should read "Country" with an asterisk if mandatory, the helper text "Select your shipping destination" appears below, and options are ordered alphabetically starting with common countries.

### What does the error state look like when a user submits without making a selection? 👈🤔

The input field displays a red border with an error icon, and the text "Please select a country" replaces the helper text below the field.

### How do I display a select input with a leading icon for currency selection? 👈🤔

The currency icon (💰) appears on the left side of the input field, followed by the label "Currency" above and the selected option "USD - US Dollar" inside the field with a dropdown indicator on the right.

### What should the loading state look like when options are being fetched from an API? 👈🤔

The input field displays a loading spinner inside where the dropdown indicator normally appears, with the helper text "Loading available options..." below the field.

### How should I configure a select input for a filter in a product catalog? 👈🤔

The label reads "Sort by" positioned above the field, with options like "Price: Low to High" and "Newest First" in the dropdown, and no helper text needed for this compact filter context.

### What's the visual difference between an empty and filled select input? 👈🤔

The empty state shows placeholder text "Select an option" in a lighter gray color, while the filled state displays the selected option text "Option Name" in standard text color.

### How do I show a select input in read-only state displaying a user's previously saved selection? 👈🤔

The field displays the selected value "Premium Plan" with reduced opacity, no dropdown indicator, and a read-only visual treatment indicating the value is locked for this view.

### What should the expanded state look like when the dropdown menu is open? 👈🤔

The dropdown menu appears below the input field with all options visible (or scrollable if many), the currently selected option is highlighted, and the dropdown indicator points upward to indicate the open state.

### How should I configure a select input with helper text explaining format requirements? 👈🤔

The label "Time zone" appears above the field, with helper text below reading "Select the time zone for scheduled notifications" in a secondary text color to provide context.

### What does the hover state look like before a user opens the dropdown? 👈🤔

The input field's background changes slightly in color or shows a subtle border highlight, and the cursor changes to a pointer, indicating the field is interactive and ready to expand.

---

## Screen Sizes

### Desktop 👈🤖

Select inputs display at their full intended width (typically 280-360px), with dropdown menus expanding below the field to show all options clearly with adequate touch targets and readable text at standard sizes.

### Tablet 👈🤖

Select inputs maintain similar proportions to desktop with slightly larger touch targets (minimum 44px height), and dropdown menus may use native OS pickers on tablets for better touch interaction.

### Mobile 👈🤖

Select inputs trigger native mobile pickers when tapped, providing the familiar OS-specific selection interface with large touch targets and optimized scrolling behavior for single-hand operation.

---

# Specs

## Properties

### Initial Config

| Property | Default Value | Notes |
|----------|---------------|-------|
| Outlined | False | Uses subtle background fill with visible bottom border by default |
| Rounded corner | False | Standard neutral input border styling with minimal corner radius |
| Input status | Empty | Field is empty with label visible, dropdown closed, and no helper text displayed |
| State | Enabled | Component is interactive and ready for user selection |
| Error | False | No validation error is present, component displays in neutral state |
| Leading icon | False | No icon is displayed on the left side of the input field |
| ⚠️ Label | True | Label is visible above the input field by default |
| Combobox | False | Standard select without search/filter functionality |
| Autocompletion | False | No autocompletion or type-ahead behavior is enabled |
| Helper text | False | No helper text is displayed below the input field initially |
| Helper link | False | No link is included in the helper text area |

---

### Outlined

**`False`** An input with a subtle background fill and visible bottom border.

**`True`** A minimalist input with a transparent background and visible stroke.

This style may be interesting for contexts other than form pages:
• When inputs need to feel lightweight and unobtrusive
• In a header (search field)
• In a selection/filtering feature in a product catalog

---

### Rounded corner

**`False`** A subtle and minimal style (neutral input border)

**`True`** A soft, friendly style, a bit more playful and approachable

---

### Input status

**`Empty`** By default, a select input is open with label, no input text, dropdown closed, and no helper text displayed below.

**`Filled`** The input text is the option selected by the user from the dropdown menu.

---

### State

**`Enabled`** Default state: the input is ready for interaction.

**`Hover`** When the user hovers over the input field (without the dropdown being opened), the appearance of the element changes slightly to indicate interactivity.

**`Focus`** When the user clicks or tabs into the input field (without opening the dropdown), the field gains focus and applies specific visual styles.

**`Expanded`** When the user opens the dropdown menu to view options.

**`Loading`** Indicates that options are being loaded asynchronously.

**`Read only`** When the select input is in a read-only state, its value is visible, but the user cannot interact with it or change the selection.

**`Disabled`** The input cannot be interacted with (non clickable, can't receive focus, no hover effect) and its appearance indicates unavailability.

**`Skeleton`** Displays a placeholder UI while content is loading.

---

### Error

An error is used to provide real-time feedback when the select input is in an invalid state:

**Examples of invalid states:**
• Required field left empty
• Incorrect value format (invalid email, phone number, postal code)
• Value that does not meet the established criteria (password not secure enough, text too short or too long)

**Accessibility for error indication:**
• Color alone is not sufficient: WCAG requires that color not be the only means of conveying information. Therefore, an icon and explicit text must accompany the error color.
• Assistive technologies need contextual error messages: when a user submits a form or leaves a field, screen readers need to receive clear textual information about the error. Use the aria-describedby attribute to associate error messages with the corresponding select input element.
• Error text is not just an ornament: WCAG guidelines require that error messages be sufficiently precise and descriptive.

**`False`** The select input is in its neutral or valid state.

**`True`** The user sees an error message detailing the nature of the problem, and the component is visually marked (e.g., with a specific color or icon) to draw attention to the error.

---

### Leading icon

Conveys the nature or purpose of the select input field at a glance.

---

### Helper text

Information displayed below the select input field to provide guidance or context to the user (explanatory text, tips, additional details, guidance on the expected format).

**Examples of helper text:**
• Indicate the maximum character limit for a text field: "You have 180 characters remaining."
• Offer tips on format requirements: "Your password must contain at least 8 characters, including a number and a special character."

**Helper text on error:**
• When in error state, helper text becomes error text.

Helper text is used to provide additional information at the right time, without overcrowding the interface.

Helper text is different from placeholder text:
• Helper text remains visible before, during, and after text entry.
• Placeholder text disappears when typing.

---

# Accessibility 👈🤖

## Accessibility intro

Select inputs must meet WCAG 2.2 Level AA requirements for keyboard navigation, screen reader compatibility, and clear error identification. For comprehensive accessibility guidance, see the [Orange Unified Design System Accessibility Overview](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability).

---

## Accessibility Challenges

Select inputs present unique accessibility challenges because they rely heavily on visual affordances (dropdown indicators, option lists) that may not be apparent to screen reader users or keyboard-only users. The interaction model—clicking to expand, scrolling through options, and selecting—requires careful implementation to ensure users can independently navigate, understand available choices, and make selections without visual reference. Additionally, the dynamic nature of dropdown state changes, loading states, and error feedback must be communicated clearly to assistive technologies.

### Key Challenges
- **Hidden options until interaction**: Users may not know what choices are available without activating the dropdown, requiring clear labeling and instructions
- **State communication**: Expanded/collapsed states, loading indicators, and selected values must be announced to screen readers dynamically
- **Keyboard navigation complexity**: Users must be able to open the dropdown, navigate options with arrow keys, select with Enter/Space, and close with Escape
- **Error identification**: Validation errors must be associated with the select input and announced clearly, with color not being the only indicator

### Critical Success Factors
1. **Proper ARIA roles and attributes**: Use `role="combobox"`, `aria-expanded`, `aria-activedescendant`, and `aria-describedby` to communicate state and associations (WCAG 4.1.2)
2. **Keyboard-accessible interaction model**: Ensure Tab navigation, Arrow key option selection, Enter/Space to select, and Escape to close work reliably (WCAG 2.1.1)
3. **Visible focus indicators**: Provide clear focus styles with ≥3:1 contrast ratio on both the input field and dropdown options (WCAG 2.4.7)
4. **Clear error association**: Link error messages to the input using `aria-describedby` and provide text-based error identification, not just color (WCAG 3.3.1, 3.3.2)

---

## Design Requirements

### Structure & Labels
- [ ] **Visible persistent label**: Provide a clear label above or beside the select input that remains visible when the dropdown is expanded or an option is selected ([Orange Forms Guidelines](https://a11y-guidelines.orange.com/en/web/components-examples/forms/))
- [ ] **Helper text association**: Use `aria-describedby` to link helper text and error messages to the select input so screen readers announce them when the field receives focus ([Orange Forms Guidelines](https://a11y-guidelines.orange.com/en/web/components-examples/forms/))
- [ ] **Mandatory field indication**: Use asterisk (*) with bold red styling at the end of labels for required fields, and ensure "mandatory" is read by screen readers via `aria-required="true"` ([Orange Forms Guidelines](https://a11y-guidelines.orange.com/en/web/components-examples/forms/))

### Visual Design
- [ ] **Minimum touch target size**: Ensure the select input and dropdown options have touch targets of at least 44×44px on mobile and 24×24px on desktop ([Orange Touch Targets](https://a11y-guidelines.orange.com/en/web/design/accessible-design/#touch-targets))
- [ ] **Focus indicator contrast**: Provide a visible focus indicator with ≥3:1 contrast ratio against the background on the input field and each option in the dropdown ([WCAG 2.4.7 Focus Visible](https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html))
- [ ] **Error state visual treatment**: Use red border, error icon, and error text together—never rely on color alone to indicate errors ([WCAG 1.4.1 Use of Color](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html))

### Content
- [ ] **Concise option labels**: ❌ "This is the option that allows you to select the premium version of our service with additional features" / ✅ "Premium Plan" ([Orange Content Guidelines](https://a11y-guidelines.orange.com/en/web/design/accessible-design/#content))
- [ ] **Specific error messages**: ❌ "Invalid selection" / ✅ "Please select a shipping country to continue" with clear recovery guidance ([WCAG 3.3.1 Error Identification](https://www.w3.org/WAI/WCAG22/Understanding/error-identification.html))

---

## Testing Checklist

### Screen Reader Testing
- [ ] Test with NVDA (Windows), JAWS (Windows), VoiceOver (macOS/iOS), TalkBack (Android) to verify label announced, expanded/collapsed states communicated, selected option read aloud, error messages spoken
- [ ] Verify arrow key navigation announces each option clearly as focus moves, selected option is indicated, and dropdown closure is announced

### Keyboard Testing
- [ ] Tab to select input, Enter/Space opens dropdown, Arrow keys navigate options and announce them, Enter/Space selects highlighted option, Escape closes dropdown without selection, Tab moves focus away
- [ ] Verify focus visible with ≥3:1 contrast on input field and all dropdown options

### Mouse/Touch Testing
- [ ] Click to open dropdown works, click outside closes dropdown, click on option selects it, touch targets on mobile are ≥44×44px

Resources: [Orange Accessibility Testing Guide](https://a11y-guidelines.orange.com/en/web/test/)

---

## Key WCAG Criteria

- **2.1.1 Keyboard** (A): All select input functionality (open dropdown, navigate options, select, close) is operable via keyboard without timing requirements
- **2.4.7 Focus Visible** (AA): Visible focus indicator with ≥3:1 contrast on the input field and each dropdown option
- **3.3.1 Error Identification** (A): Errors identified in text (not just color) and associated with the select input via `aria-describedby`
- **3.3.2 Labels or Instructions** (A): Clear labels provided for select inputs and announced by assistive technologies
- **4.1.2 Name, Role, Value** (A): Correct semantic HTML (`<select>` or custom implementation with `role="combobox"`) and ARIA attributes (`aria-expanded`, `aria-activedescendant`) communicate state changes

For complete reference: [Orange Accessibility Guidelines - WCAG Criteria](https://a11y-guidelines.orange.com/en/web/components-examples/)

---

## Additional Resources

- [Orange Accessibility Guidelines - Forms Examples](https://a11y-guidelines.orange.com/en/web/components-examples/forms/)
- [WCAG 2.2 Understanding Docs - 4.1.2 Name, Role, Value](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html)
- [WCAG 2.2 Understanding Docs - 2.1.1 Keyboard](https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html)
- [Orange Design System - Accessibility & Sustainability](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability)
- [W3C ARIA Authoring Practices - Combobox Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/)