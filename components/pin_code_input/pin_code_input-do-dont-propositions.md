# PIN code input — do & don't propositions

AI-generated propositions that no one has validated yet. They are not part of the documentation ([pin_code_input.md](pin_code_input.md)) and are not shown on zeroheight. Once a designer validates one, it moves into the full file.

## Outlined — do & don't

✅ **Do:** Use the filled (outlined=false) style in standard form contexts where the input needs prominence and clear boundaries.  
❌ **Don't:** Mix outlined and filled styles for PIN inputs within the same authentication flow.

✅ **Do:** Apply the outlined style consistently when multiple inputs appear in lightweight, non-form contexts like headers.  
❌ **Don't:** Use the outlined style in complex forms where it may reduce visual hierarchy and scannability.

✅ **Do:** Ensure both styles maintain sufficient contrast (≥3:1) against their background for accessibility compliance.  
❌ **Don't:** Choose a style based solely on aesthetics without considering the surrounding UI context and user expectations.

✅ **Do:** Consider the visual weight needed—use filled for emphasis in primary flows, outlined for secondary contexts.  
❌ **Don't:** Apply outlined style in high-security flows where users expect clear, prominent input fields.

✅ **Do:** Test both styles across light and dark themes to ensure consistent visibility and usability.  
❌ **Don't:** Assume one style works universally—validate with users in context before finalizing the choice.

## Error — do & don't

✅ **Do:** Display error messages only after explicit validation (form submission or API response), not during typing.  
❌ **Don't:** Show real-time error feedback on each keystroke, as this creates anxiety and interrupts the user's flow.

✅ **Do:** Provide specific, actionable error messages explaining what went wrong (e.g., "Incorrect code" or "Code expired").  
❌ **Don't:** Use vague error messages like "Error" or "Invalid input" that don't help users understand the problem.

✅ **Do:** Keep the input editable in error state so users can correct their entry without clearing all fields.  
❌ **Don't:** Clear all entered characters when an error occurs, forcing users to re-enter the entire code.

✅ **Do:** Use the Alert component in conjunction with the input's error state for important security messages.  
❌ **Don't:** Rely solely on the input field's visual error state without providing an accompanying error message.

✅ **Do:** Indicate remaining attempts clearly when account lockout is imminent (e.g., "2 attempts remaining").  
❌ **Don't:** Lock users out without warning or without providing clear recovery options after exceeding attempt limits.

## Other boolean options — do & don't

✅ **Do:** Use helper text to provide context about code delivery (e.g., "Enter the 6-character code sent to your phone").  
❌ **Don't:** Use helper text for information that should be in a label or that duplicates visible instructions elsewhere.

✅ **Do:** Keep helper text concise—ideally one line—to avoid cluttering the interface.  
❌ **Don't:** Write lengthy helper text that wraps multiple lines and competes with the primary input for attention.

✅ **Do:** Ensure helper text remains visible and readable in all states, including when the input is focused or in error.  
❌ **Don't:** Hide or obscure helper text when displaying error messages; show both when both are relevant.

✅ **Do:** Write helper text that adds value, such as timing information ("Code expires in 5 minutes") or delivery details.  
❌ **Don't:** Include placeholder-style hints in helper text that merely repeat the input's purpose without adding context.

✅ **Do:** Position helper text consistently below the input group across all instances of the PIN code input.  
❌ **Don't:** Place helper text in inconsistent locations that confuse users about which input it relates to.
