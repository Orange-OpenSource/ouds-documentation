# Guideline

## Intro

A quantity input enables users to specify numeric values through direct entry or increment/decrement controls, commonly used in e-commerce and booking flows.

---

## Definition

A quantity input is a form component that allows users to specify a numerical value representing a quantity, often used in contexts like shopping carts, inventory management, or booking systems. It typically combines a numeric text field with increment and decrement controls (such as "+" and "–" buttons) to make adjustments easy and precise. The component must enforce valid input ranges (minimum of 1), prevent invalid characters, and support keyboard input, stepper controls, and assistive technologies.

---

## Best for

✅ Shopping cart quantity adjustments where users modify item counts in small increments

✅ Booking systems requiring passenger, guest, or room counts within defined limits

✅ Inventory management interfaces for stock quantity updates

✅ Product configuration with limited numeric options (e.g., 1–10 items)

✅ Reservation systems specifying party size or number of tickets

✅ Form fields where values rarely exceed 20 and incremental changes are common

✅ Mobile-first interfaces where tap-based controls improve usability

✅ Contexts requiring validation feedback for out-of-range values

✅ Compact layouts needing space-efficient numeric input controls

✅ Scenarios where preventing invalid character entry improves data quality

---

## Anatomy

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Label | Describes the input's purpose and provides accessible identification | N |
| 2 | Input field | Displays current value and accepts direct keyboard entry | N |
| 3 | Increment button (+) | Increases value by one step when activated | N |
| 4 | Decrement button (–) | Decreases value by one step when activated | N |
| 5 | Leading icon | Provides visual context for the input's purpose | Y |
| 6 | Suffix | Displays units or currency after the value (kg, %, cm) | Y |
| 7 | Helper text | Offers additional guidance or context below the input | Y |
| 8 | Error message | Communicates validation failures with corrective guidance | Y |

---

## Outlined

**`False`** An input with a subtle background fill and un visible bottom border, creating a softer and more contained look. Best suited for dense layouts or to enhance visibility.

**`True`** A minimalist input with a transparent background and a visible stroke outlining the field. This style may be interesting for contexts other than form pages:
• When inputs need to feel lightweight and unobtrusive
• In a header (search field)
• In a selection/filtering feature in a product catalog

### Do & don'ts

✅ **Do:** Use the outlined variant for standalone inputs that need clear visual boundaries within content-heavy pages  
❌ **Don't:** Mix outlined and filled variants inconsistently within the same form or interface section

✅ **Do:** Apply the filled variant in dense form layouts where subtle background differentiation aids scanability  
❌ **Don't:** Use outlined style on dark backgrounds where the stroke may lack sufficient contrast

✅ **Do:** Consider the outlined variant for filter bars and search contexts where inputs appear inline with other controls  
❌ **Don't:** Default to outlined style without considering the overall visual density of the interface

✅ **Do:** Maintain consistent style choices across related quantity inputs within a single workflow  
❌ **Don't:** Switch between outlined and filled styles based solely on aesthetic preference without functional rationale

✅ **Do:** Test both variants with your actual content to determine which provides better visual hierarchy  
❌ **Don't:** Assume one style universally works better—context determines the optimal choice

---

## Rounded corner

**`False`** For a square finish.

**`True`** For a finish with rounded corner. To be favored in more emotional, immersive contexts or those tied to specific visual identities. For standard or business-oriented journeys, keep the default corners. This evolution addresses the need for flexibility in adapting the design to certain brand contexts.

### Do & don'ts

✅ **Do:** Use rounded corners consistently with other form elements in your design system to maintain visual harmony  
❌ **Don't:** Apply rounded corners to quantity inputs while using square corners on adjacent buttons or fields

✅ **Do:** Reserve rounded corners for consumer-facing or lifestyle brand interfaces where softer aesthetics align with brand identity  
❌ **Don't:** Use rounded corners in enterprise or data-heavy applications where sharp edges convey precision

✅ **Do:** Consider rounded corners for mobile interfaces where they may improve perceived touch targets  
❌ **Don't:** Assume rounded corners automatically improve usability—they are primarily a visual treatment

✅ **Do:** Document your corner radius choice in design tokens for consistent application across components  
❌ **Don't:** Mix corner radius values arbitrarily across different quantity input instances

✅ **Do:** Test rounded corner variants with your specific button placement (trailing vs. split) to ensure visual balance  
❌ **Don't:** Apply rounded corners without verifying they work well with increment/decrement button styling

---

### Input status

**`Empty`** The Empty state indicates that the quantity input is blank with no content or placeholder, a neutral starting point.

**`Empty (Placeholder)`** The Empty with Placeholder state provides a hint or guidance inside the field to suggest expected input.

**`Filled`** The Filled state shows that the user has entered valid content into the field, replacing any placeholder.

### Do & don'ts

✅ **Do:** Set a sensible default value (typically 1) to reduce user effort and prevent empty submission errors  
❌ **Don't:** Leave quantity inputs empty in e-commerce contexts where a zero value has no valid meaning

✅ **Do:** Use placeholder text to indicate expected format when the field can be empty (e.g., "Enter quantity")  
❌ **Don't:** Rely solely on placeholders for critical instructions—they disappear once users begin typing

✅ **Do:** Ensure filled state styling provides clear feedback that user input has been captured  
❌ **Don't:** Style filled and empty states identically, making it difficult to scan form completion status

✅ **Do:** Preserve entered values when users navigate away and return to the form  
❌ **Don't:** Reset quantity values unexpectedly, forcing users to re-enter their selections

✅ **Do:** Validate and display the filled state immediately when users type valid numbers  
❌ **Don't:** Delay visual confirmation of valid input, leaving users uncertain if their entry was accepted

---

## Actions placement

**`Trailing`** It places both the increment and decrement buttons on the right side of the input field, either stacked vertically or positioned side by side. This layout is compact and visually streamlined, making it ideal for dense interfaces or mobile views.

**`Split`** It positions the decrement button to the left of the input and the increment button to the right. It provides a more balanced and intuitive interaction model, especially in use cases like e-commerce where users frequently adjust quantities.

### Do & don'ts

✅ **Do:** Use split placement for e-commerce quantity selectors where users frequently adjust values in both directions  
❌ **Don't:** Use trailing placement when the decrease action is equally important as increase—split provides better balance

✅ **Do:** Apply trailing placement in compact table cells or data grids where horizontal space is limited  
❌ **Don't:** Force split placement in narrow containers where it causes the input field to become too small

✅ **Do:** Consider trailing placement for RTL (right-to-left) interfaces where it may provide more natural interaction  
❌ **Don't:** Ignore localization requirements when choosing button placement

✅ **Do:** Use split placement when touch targets need to be easily distinguishable for mobile users  
❌ **Don't:** Use trailing placement with stacked buttons if users struggle to tap the correct control

✅ **Do:** Test both placements with real users to determine which reduces errors in your specific context  
❌ **Don't:** Assume one placement universally outperforms the other without user research

---

## Specific focus state rules

**Keyboard input disabled**

In the vast majority of modern UX/UI cases, a quantity input should be editable on focus. However, there are a few specific rare cases where direct editing by keyboard input might be disabled:
• Highly guided or controlled usage→product configuration with mandatory steps
• Risk of critical error→specific or technical values
• Strict touch context→mobile app with simplified UI, no keyboard
• Deliberate product decision→to enforce navigation or a business constraint

In this specific context, it is therefore recommended to prefill the input by default.

**Keyboard input + increment/decrement controls enabled**

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

### Do & don'ts

✅ **Do:** Maintain focus on the input field when users interact with increment/decrement buttons  
❌ **Don't:** Move focus away from the quantity input after button clicks, disrupting keyboard navigation flow

✅ **Do:** Validate and apply the current value before incrementing or decrementing when the field is being edited  
❌ **Don't:** Ignore partially entered values—parse and validate them before applying the step change

✅ **Do:** Provide a clear focus indicator that encompasses the entire control (input + buttons) as a single unit  
❌ **Don't:** Show separate focus states for the input and buttons, confusing users about the component boundary

✅ **Do:** Support keyboard shortcuts (Arrow Up/Down) for incrementing and decrementing when the input has focus  
❌ **Don't:** Require users to tab to buttons separately when keyboard arrow controls can serve the same purpose

✅ **Do:** Handle edge cases gracefully—default to minimum value (1) when the field is empty and user clicks increment  
❌ **Don't:** Throw errors or behave unpredictably when users click buttons on an empty or invalid input

---

## Error

The Error status indicates that the user input does not meet validation rules or expected formatting. It provides immediate visual feedback, typically through a red border, error icon, and a clear, accessible error message positioned below the input (mandatory).

This state helps users quickly identify and correct mistakes by explaining what went wrong and, when possible, how to fix it. The input remains editable, encouraging users to revise their input without starting over.

If the input is filled, an "error" status is triggered by the entry of a value that is too small, too large, or non-numeric.

**Error message vs helper text** The error message is not the same element as the helper text, it is independent. If a helper text accompanies the text input, it is replaced by the error message. The helper text must not be displayed simultaneously.

### Do & don'ts

✅ **Do:** Position error messages directly below the input field with consistent spacing for easy scanning  
❌ **Don't:** Display error messages in tooltips or modals that obscure the input or disappear unexpectedly

✅ **Do:** Write specific, actionable error messages like "Quantity must be between 1 and 99"  
❌ **Don't:** Use generic messages like "Invalid input" that don't help users understand how to fix the issue

✅ **Do:** Replace helper text with error messages to avoid cognitive overload—one message at a time  
❌ **Don't:** Show both helper text and error messages simultaneously, creating visual clutter and confusion

✅ **Do:** Use `aria-invalid="true"` and `aria-errormessage` to programmatically associate errors with the input  
❌ **Don't:** Rely solely on color to communicate errors—ensure text and icons provide redundant cues

✅ **Do:** Allow users to continue editing the input while the error state is displayed  
❌ **Don't:** Disable the input in error state, preventing users from making corrections

---

## Leading icon

Helps indicate the purpose of the input (magnifying glass for search, envelope for email, phone device for phone number). Only use a leading icon if it adds clear functional or contextual value.

### Do & don'ts

✅ **Do:** Use leading icons that directly relate to the input's purpose (e.g., shopping cart icon for cart quantity)  
❌ **Don't:** Add decorative icons that don't enhance understanding of the input's function

✅ **Do:** Ensure leading icons maintain sufficient contrast and size for visibility at all supported sizes  
❌ **Don't:** Use icons so small or low-contrast that they become difficult to perceive

✅ **Do:** Hide leading icons from screen readers using `aria-hidden="true"` when the label provides sufficient context  
❌ **Don't:** Make leading icons focusable or interactive unless they serve an independent function

✅ **Do:** Consider omitting leading icons in compact layouts where space is at a premium  
❌ **Don't:** Force leading icons into every quantity input just for visual consistency

✅ **Do:** Test leading icon visibility across light and dark themes to ensure consistent recognition  
❌ **Don't:** Use icons that lose meaning or visibility when theme colors change

---

## Label

Describes the purpose of the input. Why hide a quantity input label?
In some UI contexts, especially when space is limited or when the input is part of a compact layout (search bars, filters, inline forms), visually hiding the label can help maintain a clean and uncluttered interface.
However, hiding the label should only be done if:
• The purpose of the input remains clear thanks to a placeholder or contextual icon.
• The label is still accessible to screen readers (using aria-label, aria-labelledby, or visually hidden text).

Hiding a label is a design choice that must balance visual simplicity and clarity of intent, without compromising inclusiveness or form guidance.

### Do & don'ts

✅ **Do:** Always provide a programmatic label using `<label>`, `aria-label`, or `aria-labelledby`  
❌ **Don't:** Rely solely on placeholder text as a label substitute—it disappears when users type

✅ **Do:** Use visually hidden labels (CSS technique) when visual context makes the purpose obvious  
❌ **Don't:** Remove labels entirely from the DOM, breaking accessibility for screen reader users

✅ **Do:** Keep labels concise and descriptive: "Quantity" or "Number of guests" rather than lengthy instructions  
❌ **Don't:** Use vague labels like "Enter value" that don't clarify what the number represents

✅ **Do:** Position visible labels consistently—typically above the input or inline to its left  
❌ **Don't:** Place labels in unexpected positions that break users' scanning patterns

✅ **Do:** Include context in the label when multiple quantity inputs appear together (e.g., "Adults," "Children")  
❌ **Don't:** Use identical generic labels for multiple inputs, forcing users to infer meaning from position alone

---

## Other boolean options

**`Suffix`** An element placed after the user's input, often used to display a currency or a unit (kg, %, cm…).

**`Helper text`** Supporting text conveys additional information about the input field, such as how it will be used. It should ideally only take up a single line, though may wrap to multiple lines if required, and be either persistently visible or visible only on focus.

### Do & don'ts

✅ **Do:** Use suffix for units of measurement (kg, cm, %) or currency symbols that clarify the value's meaning  
❌ **Don't:** Place units in the label or helper text when a suffix provides clearer inline context

✅ **Do:** Keep helper text brief and focused on a single piece of guidance (e.g., "Maximum 99 items")  
❌ **Don't:** Overload helper text with multiple instructions—prioritize the most critical information

✅ **Do:** Associate helper text with the input using `aria-describedby` for screen reader accessibility  
❌ **Don't:** Position helper text far from the input where the visual association becomes unclear

✅ **Do:** Show helper text persistently when the information is essential for correct input  
❌ **Don't:** Hide critical guidance behind focus states where users may miss it

✅ **Do:** Ensure suffix text maintains legibility and doesn't crowd the numeric value  
❌ **Don't:** Use long suffix text that causes truncation or makes the input feel cramped

---

# Specs

## States

**`Enabled`** Neutral appearance, whether empty or filled. It allows users to click, focus, and type freely without restrictions.

**`Hover`** Slight visual contrast or border color change.

**`Focus`** The quantity input is focused and ready to receive user input. It visually highlights the field to indicate that it's currently editable and interactive. This state typically appears after a user clicks or taps into the field.

**`Loading`** The Loading state indicates that the system is processing or retrieving data related to the quantity input. A progress indicator appears to inform the user that an action is in progress. During this state, the input may be temporarily disabled to prevent further interaction.

**`Read only`** Text visible but not editable (often with a muted or different background).

**`Disabled`** The field is non-interactive and grayed out to indicate it cannot be changed. The helper text is muted.

**`Skeleton`** Improves the perceived loading time by providing a visual cue of where field will appear once fully loaded. Uses the "Skeleton" component, variant "Security marge=False".

---

## Layout and spacing

🚧 Content to be added

---

# Accessibility

## Accessibility intro

The quantity input must meet WCAG 2.2 Level AA requirements, implementing the spinbutton pattern with proper ARIA attributes and keyboard support. For comprehensive accessibility guidance, see the [Orange Unified Design System Accessibility Overview](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability).

---

## Accessibility Challenges

Quantity inputs present unique accessibility challenges because they combine text input with button controls, requiring careful coordination of focus management, value announcements, and keyboard interactions. Users must be able to understand the current value, the allowed range, and receive feedback when values change—all through multiple input modalities.

### Key Challenges
- Coordinating focus between the text field and increment/decrement buttons
- Announcing value changes to screen readers without being overly verbose
- Supporting both direct keyboard entry and arrow key navigation
- Ensuring touch target sizes meet minimum requirements (44×44px) on mobile

### Critical Success Factors
1. Implement `role="spinbutton"` with `aria-valuenow`, `aria-valuemin`, and `aria-valuemax` (WCAG 4.1.2)
2. Provide visible focus indicators with ≥3:1 contrast ratio against adjacent colors (WCAG 2.4.7)
3. Ensure all functionality is operable via keyboard without timing requirements (WCAG 2.1.1)
4. Associate error messages programmatically using `aria-errormessage` and `aria-invalid` (WCAG 3.3.1)

---

## Design Requirements

### Structure & Labels
- [ ] **Programmatic label**: Associate visible label with input using `<label for="">` or `aria-labelledby` ([Orange labelling guidelines](https://a11y-guidelines.orange.com/en/web/develop/textual-content/#labelling-form-elements))
- [ ] **Spinbutton role**: Apply `role="spinbutton"` with `aria-valuenow`, `aria-valuemin`, `aria-valuemax` attributes
- [ ] **Button labels**: Provide accessible names for increment/decrement buttons ("Increase quantity", "Decrease quantity")

### Visual Design
- [ ] **Focus indicator**: Visible focus ring with ≥3:1 contrast, encompassing entire control group ([Orange focus guidelines](https://a11y-guidelines.orange.com/en/web/design/navigation-focus/#make-focus-visible))
- [ ] **Error styling**: Red border + icon + text message—never color alone
- [ ] **Touch targets**: Buttons meet 44×44px minimum touch target size on mobile

### Content
- [ ] **Error messages**: ❌ "Invalid" / ✅ "Enter a quantity between 1 and 99" ([Orange error guidelines](https://a11y-guidelines.orange.com/en/web/components-examples/forms/))
- [ ] **Value context**: Include units in `aria-valuetext` when helpful (e.g., "5 items")

---

## Testing Checklist

### Screen Reader Testing
- [ ] Test with NVDA (Windows), JAWS (Windows), VoiceOver (macOS/iOS), TalkBack (Android)
- [ ] Verify label announced on focus, current value read, min/max communicated, value changes announced

### Keyboard Testing
- [ ] Tab navigates to input, Arrow Up/Down adjust value, Home/End jump to min/max, Enter submits
- [ ] Focus indicator visible (≥3:1 contrast), buttons not in Tab order when arrows work

### Touch Testing
- [ ] Touch targets ≥44×44px, increment/decrement buttons easily distinguishable

Resources: [Orange Accessibility Testing Guide](https://a11y-guidelines.orange.com/en/web/test/)

---

## Key WCAG Criteria

- **2.1.1 Keyboard** (A): All functionality operable via keyboard including value adjustment with Arrow keys
- **2.4.7 Focus Visible** (AA): Clear focus indicator with ≥3:1 contrast on input field and buttons
- **3.3.1 Error Identification** (A): Errors identified in text and associated with input via `aria-errormessage`
- **3.3.2 Labels or Instructions** (A): Label provided and programmatically associated with input
- **4.1.2 Name, Role, Value** (A): Spinbutton role with `aria-valuenow`, `aria-valuemin`, `aria-valuemax` communicates state

For complete reference: [Orange Accessibility Guidelines - Forms](https://a11y-guidelines.orange.com/en/web/components-examples/forms/)

---

## Additional Resources

- [W3C WAI-ARIA Spinbutton Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/spinbutton/)
- [W3C Quantity Spin Button Example](https://www.w3.org/WAI/ARIA/apg/patterns/spinbutton/examples/quantity-spinbutton/)
- [Orange Accessibility Guidelines - Form Components](https://a11y-guidelines.orange.com/en/web/components-examples/)
- [MDN ARIA Spinbutton Role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/spinbutton_role)

---

# Changelog

| Date | Number | Notes |
|------|--------|-------|
| Sep 30, 2025 | 1.2.0 | • For the property "Actions placement", the name of the variant "Right" is replaced by "Trailing" (RTL consideration)<br>• The name of the "Style" variant has been replaced to "Outlined" with true/false variant |
| Jul 29, 2025 | 1.1.0 | • Several design token updates: [Component tokens changelog 1.5.0](https://www.figma.com/design/Co2t6wHMf4GB9NJVGs2Hes/-OUDS-Core-Lib--Design-tokens?m=auto&node-id=9280-2568&t=HLVB4jOd35DWr8Bj-1) |
| Jun 30, 2025 | 1.0.0 | • Component creation |

---