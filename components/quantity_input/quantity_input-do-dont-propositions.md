# Quantity input — do & don't propositions

AI-generated propositions that no one has validated yet. They are not part of the documentation ([quantity_input.md](quantity_input.md)) and are not shown on zeroheight. Once a designer validates one, it moves into the full file.

## Outlined — do & don't

/

## Actions placement — do & don't

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

## Specific focus state rules — do & don't

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

## Error — do & don't

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

## Leading icon — do & don't

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

## Other boolean options — do & don't

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

## Label — do & don't

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
