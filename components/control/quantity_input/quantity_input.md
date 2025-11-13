# Guideline

## Intro 👈🤖

A Quantity Input lets users select numeric values through buttons or keyboard input for shopping carts and inventory.

---

## Description

A quantity input is a form component that allows users to specify a numerical value representing a quantity, often used in contexts like shopping carts, inventory management, or booking systems. It typically combines a numeric text field with increment and decrement controls (such as "+" and "−" buttons) to make adjustments easy and precise. The component must enforce valid input ranges (minimum of 1), prevent invalid characters, and support keyboard input, stepper controls, and assistive technologies.

---

## Anatomy 👈🤖

| # | Element | Purpose |
|---|---------|---------|
| 1 | Container | Provides the structural frame and background for all input elements |
| 2 | Label text | Identifies the purpose and expected input for the field |
| 3 | Leading icon (optional) | Provides visual context or categorization for the input type |
| 4 | Input field / Placeholder | Displays entered numeric value or guidance text when empty |
| 5 | Suffix (optional) | Shows the unit of measurement or context (e.g., "pcs", "kg") |
| 6 | Increment button (+) | Increases the numeric value by one unit on click |
| 7 | Decrement button (−) | Decreases the numeric value by one unit on click |
| 8 | Helper / Error text | Offers guidance or displays validation feedback below the input |

---

## Usage & Guidance

### Best for 👈🤔

✅ E-commerce cart quantity adjustments where users select how many items to purchase  
✅ Inventory or stock management interfaces requiring precise numeric entry  
✅ Booking systems for tickets, seats, or room reservations with specific counts  
✅ Recipe builders or measurement tools needing unit-based quantity input  
✅ Form fields with numeric constraints (min 1, max 99) and touchscreen optimization  
✅ Settings panels requiring numeric configuration values  
✅ Product configurators where users specify item quantities  
✅ Order forms with multiple line items each requiring quantity selection  
✅ Mobile-first contexts where stepper buttons simplify numeric entry  
✅ Situations requiring paste or autofill support for numeric values

---

### Keyboard input disabled

In the vast majority of modern UX/UI cases, a quantity input should be editable on focus. However, there are a few specific rare cases where direct editing by keyboard input might be disabled:
• Highly guided or controlled usage→product configuration with mandatory steps
• Risk of critical error→specific or technical values
• Strict touch context→mobile app with simplified UI, no keyboard
• Deliberate product decision→to enforce navigation or a business constraint

In this specific context, it is therefore recommended to prefill the input by default.

---

### Keyboard input + increment/decrement controls enabled

In the context of an editable quantity input, if the field is focused and already filled by the user, then clicking the + (increase) or – (decrease) buttons must follow a smooth and predictable behavior according to the following UX rules.

When clicking + or – during editing:
• The value is automatically validated
• The action is applied to that value (+1 or –1)
• The field is visually updated with the new value
• The cursor is moved to the end of the field (optional)
• The field remains focused

Absolutely to avoid:
• Losing the currently typed value if partially entered
• Requiring defocus for the buttons to work
• Failing to parse/validate the value before incrementing

Specific error focus state:
If the value in the field is invalid (empty or non-numeric), clicking + or – may:
• Either fill in a default value (1)
• Or display a temporary blocking error ("Please enter a number")

---

### ⚠️ Label

Describes the purpose of the input. Why hide a quantity input label?
In some UI contexts, especially when space is limited or when the input is part of a compact layout (search bars, filters, inline forms), visually hiding the label can help maintain a clean and uncluttered interface.
However, hiding the label should only be done if:
• The purpose of the input remains clear thanks to a placeholder or contextual icon.
• The label is still accessible to screen readers (using aria-label, aria-labelledby, or visually hidden text).

Hiding a label is a design choice that must balance visual simplicity and clarity of intent, without compromising inclusiveness or form guidance.

---

### Context placement 👈🤔

✅ **Do:** Place quantity inputs directly adjacent to product images and names in cart interfaces for immediate visual association  
❌ **Don't:** Isolate quantity controls far from the items they modify, forcing users to scan back and forth

### Default values and prefilling 👈🤔

✅ **Do:** Default to quantity "1" for most shopping scenarios so users can immediately add to cart without extra clicks  
❌ **Don't:** Start with empty or "0" values that require users to increment before taking action

### Unit clarity in labels 👈🤔

✅ **Do:** Use suffix text (like "pcs", "kg", "units") when the measurement unit isn't obvious from context  
❌ **Don't:** Leave unit ambiguity that forces users to guess whether they're selecting items, boxes, or cases

### Validation timing and feedback 👈🤔

✅ **Do:** Provide immediate inline validation as users type or click increment buttons, showing allowed ranges  
❌ **Don't:** Wait until form submission to reveal that quantities are outside acceptable bounds

### Mobile-first stepper sizing 👈🤔

✅ **Do:** Make increment and decrement buttons large enough (44×44px minimum) for reliable touch interaction on mobile  
❌ **Don't:** Use tiny stepper controls that cause frequent mis-taps and user frustration

### Error recovery guidance 👈🤔

✅ **Do:** Show helper text like "Min: 1, Max: 99" proactively to prevent errors before they occur  
❌ **Don't:** Display only error messages after mistakes, missing the opportunity to guide users correctly first

### Label hierarchy and scannability 👈🤔

✅ **Do:** Use clear, specific labels like "Number of tickets:" rather than generic "Quantity:" when context matters  
❌ **Don't:** Use identical labels for multiple quantity inputs in the same form, reducing differentiation

### Keyboard workflow efficiency 👈🤔

✅ **Do:** Support arrow keys (↑↓) for incrementing values and allow direct numeric typing for power users  
❌ **Don't:** Force all users through button clicks when keyboard input would be faster for larger value changes

### Visual feedback on interaction 👈🤔

✅ **Do:** Provide hover and active states on stepper buttons so users receive immediate feedback before clicking  
❌ **Don't:** Use static buttons with no visual response, leaving users uncertain if they've clicked successfully

### Integration with product flows 👈🤔

✅ **Do:** Position quantity selectors before "Add to Cart" or purchase buttons in the natural reading order  
❌ **Don't:** Place quantity controls after action buttons, disrupting the expected user flow sequence

---

### How should I configure the quantity input for e-commerce cart items with units? 👈🤔

Display the label "Quantity:", input field with the current value, suffix showing units like "pcs", and increment/decrement buttons on the right side.

### What does the empty state with placeholder look like? 👈🤔

Show placeholder text "Enter a number" in muted color within the input field, with stepper buttons enabled and helper text below explaining valid ranges.

### How should I display error state when value exceeds maximum? 👈🤔

Replace helper text with error message in red (e.g., "Maximum quantity is 99"), add error icon, and apply red border or underline to the input container.

### What's the visual difference between trailing and split button placement? 👈🤔

Trailing placement groups both + and − buttons together on the right side; split placement positions the − button on the left, input in center, and + button on the right.

### How do I show the loading state during quantity validation? 👈🤔

Display a progress indicator within the input area while keeping the field value visible but temporarily disabled until validation completes.

### What should the disabled state look like when items are out of stock? 👈🤔

Apply muted background and text colors to the entire component, gray out stepper buttons, and add helper text like "Currently unavailable".

### How should I configure the read-only state for confirmed orders? 👈🤔

Display the quantity value with no stepper buttons, use muted colors, and change label to past tense like "Ordered quantity:".

### What does the focus state look like during keyboard input? 👈🤔

Show prominent focus border around the input container, highlight the input field text, and ensure stepper buttons remain accessible.

### How do I display helper text for range constraints? 👈🤔

Position text like "Please enter a number between 1 and 99" below the input in muted color, aligned with the field's left edge.

### What's the hover state appearance for stepper buttons? 👈🤔

Apply subtle background color change and increase visual contrast on the button being hovered to indicate interactivity.

---

## Screen Sizes

### Desktop 👈🤖
The quantity input displays with comfortable spacing and full visibility of labels, input field, and stepper buttons. Desktop supports keyboard input workflows including arrow keys for incrementing and Tab navigation between fields.

### Tablet 👈🤖
Component maintains similar layout to desktop but with slightly adjusted touch target sizes to accommodate finger interaction while preserving the trailing or split button placement options.

### Mobile 👈🤖
Stepper buttons are enlarged to meet 44×44px minimum touch target requirements. Split button placement becomes more prominent as it provides better thumb-zone accessibility on smaller screens.

---

# Specs

## Properties

### Initial Config

| Property | Default Value | Notes |
|----------|---------------|-------|
| Outlined | False | Uses filled background style by default for standard form contexts |
| Rounded corner | False | Maintains square corners unless brand identity requires softer edges |
| Actions placement | Trailing | Groups increment/decrement buttons together on the right side |
| Input status | Empty | Starts with no value entered, ready for user input |
| State | Enabled | Component is interactive and ready for user input immediately |
| Error | False | No validation errors present initially |
| Leading icon | False | Icon is optional and hidden by default unless context requires it |
| ⚠️ Label | True | Label is displayed by default for accessibility and clarity |
| ✏️ Label | "Quantity:" | Default label text can be customized based on context |
| ✏️ Placeholder | "Enter a number" | Provides hint when field is empty |
| ✏️ Input text | Empty | No default numeric value in the field |
| Suffix | False | Unit text (like "pcs") is optional |
| Helper text | False | Supporting text is optional |
| ✏️ Helper text | "Please enter a number between 1 and 99." | Default guidance message when helper text is enabled |
| ✏️ Error empty text | Customizable | Error message shown when empty field is submitted |
| ✏️ Error filled text | Customizable | Error message shown when invalid value is entered |

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

### Input status

**`Empty`** The Empty state indicates that the quantity input is blank with no content or placeholder, a neutral starting point.

**`Empty (Placeholder)`** The Empty with Placeholder state provides a hint or guidance inside the field to suggest expected input.

**`Filled`** The Filled state shows that the user has entered valid content into the field, replacing any placeholder.

---

### Actions placement

**`Trailing`** It places both the increment and decrement buttons on the right side of the input field, either stacked vertically or positioned side by side. This layout is compact and visually streamlined, making it ideal for dense interfaces or mobile views.

**`Split`** It positions the decrement button to the left of the input and the increment button to the right. It provides a more balanced and intuitive interaction model, especially in use cases like e-commerce where users frequently adjust quantities.

---

### State

**`Enabled`** Neutral appearance, whether empty or filled. It allows users to click, focus, and type freely without restrictions.

**`Hover`** Slight visual contrast or border color change.

**`Focus`** The quantity input is focused and ready to receive user input. It visually highlights the field to indicate that it's currently editable and interactive. This state typically appears after a user clicks or taps into the field.

**`Loading`** The Loading state indicates that the system is processing or retrieving data related to the quantity input. A progress indicator appears to inform the user that an action is in progress. During this state, the input may be temporarily disabled to prevent further interaction.

**`Read only`** Text visible but not editable (often with a muted or different background).

**`Disabled`** The field is non-interactive and grayed out to indicate it cannot be changed. The helper text is muted.

**`Skeleton`** Improves the perceived loading time by providing a visual cue of where field will appear once fully loaded. Uses the "Skeleton" component, variant "Security marge=False".

---

### Error

The Error status indicates that the user input does not meet validation rules or expected formatting. It provides immediate visual feedback, typically through a red border, error icon, and a clear, accessible error message positioned below the input (mandatory).

This state helps users quickly identify and correct mistakes by explaining what went wrong and, when possible, how to fix it. The input remains editable, encouraging users to revise their input without starting over.

If the input is filled, an "error" status is triggered by the entry of a value that is too small, too large, or non-numeric.

**⚠️ Error message vs helper text** The error message is not the same element as the helper text, it is independent. If a helper text accompanies the text input, it is replaced by the error message. The helper text must not be displayed simultaneously.

---

### Leading icon

Helps indicate the purpose of the input (magnifying glass for search, envelope for email, phone device for phone number). Only use a leading icon if it adds clear functional or contextual value.

---

### Suffix and Helper text

**Suffix** An element placed after the user's input, often used to display a currency or a unit (kg, %, cm…).

**Helper text** Supporting text conveys additional information about the input field, such as how it will be used. It should ideally only take up a single line, though may wrap to multiple lines if required, and be either persistently visible or visible only on focus.

---

# Accessibility 👈🤖

## Accessibility intro

Quantity inputs must meet WCAG 2.2 Level AA standards to ensure all users can adjust numeric values effectively. For comprehensive accessibility guidance, see the [Orange Unified Design System Accessibility Overview](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability).

---

## Accessibility Challenges

Quantity inputs present unique accessibility challenges because they combine text input with button controls, requiring coordination between keyboard, screen reader, and mouse interactions. Users must understand both the current value and the allowed range, while assistive technology must announce value changes caused by button clicks.

### Key Challenges
- Screen readers must announce both the label and current value when focus moves to the input field
- Button clicks that change values need immediate announcement of the new value to screen readers
- Keyboard users require efficient methods to increment values without relying solely on mouse clicks
- Error states must be programmatically associated with the input so assistive technology can announce them

### Critical Success Factors
1. Labels must be programmatically associated with inputs using `for`/`id` or `aria-labelledby`
2. Live regions (`aria-live`) must announce value changes when users click increment/decrement buttons
3. All functionality must be keyboard accessible (Tab, Enter, Arrow keys for incrementing)
4. Error messages must use `aria-describedby` to link validation feedback to the input field

---

## Design Requirements

### Structure & Labels
- [ ] **Label association**: Every quantity input must have a visible label programmatically linked via `<label for="input-id">` or `aria-labelledby`
- [ ] **Button labels**: Increment (+) and decrement (−) buttons must have accessible names like "Increase quantity" and "Decrease quantity"
- [ ] **Value announcement**: Current value and allowed range should be conveyed through `aria-valuemin`, `aria-valuemax`, `aria-valuenow` attributes

### Visual Design
- [ ] **Focus indicators**: Focus borders must have ≥3:1 contrast ratio against adjacent colors ([Orange A11y: Focus](https://a11y-guidelines.orange.com/en/web/develop/focus/))
- [ ] **Touch targets**: Increment and decrement buttons must be ≥44×44px on mobile for reliable touch interaction
- [ ] **Color contrast**: All text (labels, values, helper text) must meet ≥4.5:1 contrast for normal text, ≥3:1 for large text

### Content
- [ ] **Error messages**: ❌ "Invalid" / ✅ "Please enter a number between 1 and 99" ([Orange A11y: Forms](https://a11y-guidelines.orange.com/en/web/develop/forms/))
- [ ] **Helper text clarity**: Proactively communicate constraints like "Min: 1, Max: 99" before errors occur

---

## Testing Checklist

### Screen Reader Testing
- [ ] Test with NVDA (Windows), JAWS (Windows), VoiceOver (macOS/iOS), TalkBack (Android)
- [ ] Verify label and current value announced when focusing input, button actions announce new values via `aria-live`, error messages read via `aria-describedby`

### Keyboard Testing
- [ ] Tab navigation moves between inputs and buttons, focus visible with ≥3:1 contrast, Enter/Space activate buttons, Arrow ↑↓ keys increment values in input field
- [ ] All functionality accessible without mouse, Escape clears focus if applicable

### Paste Testing
- [ ] Pasting numeric values into the field works correctly and triggers validation
- [ ] Screen readers announce changes after paste operations

Resources: [Orange Accessibility Testing Guide - Forms](https://a11y-guidelines.orange.com/en/web/test/forms/)

---

## Key WCAG Criteria

- **2.1.1 Keyboard** (A): All increment, decrement, and input functionality operable via keyboard without timing requirements
- **2.4.7 Focus Visible** (AA): Visible focus indicator with ≥3:1 contrast on input field and stepper buttons
- **3.3.1 Error Identification** (A): Validation errors identified in text and programmatically associated with inputs via `aria-describedby`
- **3.3.2 Labels or Instructions** (A): Labels provided for quantity inputs and available to assistive technology via proper HTML association
- **4.1.2 Name, Role, Value** (A): Correct semantic HTML (`<input type="number">`, `<button>`) and ARIA attributes (`aria-valuenow`, `aria-live`) communicate state changes

For complete reference: [Orange Accessibility Guidelines - Forms & Inputs](https://a11y-guidelines.orange.com/en/web/components-examples/forms/)

---

## Additional Resources

- [Orange Accessibility Guidelines - Form Examples](https://a11y-guidelines.orange.com/en/web/components-examples/forms/)
- [WCAG 2.2 Understanding - Input Modalities](https://www.w3.org/WAI/WCAG22/Understanding/input-modalities)
- [Orange Design System - Accessibility & Sustainability](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability)
- [ARIA: spinbutton role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/spinbutton_role)
- [W3C ARIA Authoring Practices - Spinbutton](https://www.w3.org/WAI/ARIA/apg/patterns/spinbutton/)