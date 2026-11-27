# Switch — do & don't propositions

AI-generated propositions that no one has validated yet. They are not part of the documentation ([switch.md](switch.md)) and are not shown on zeroheight. Once a designer validates one, it moves into the full file.

## When to use

✅ When toggling a binary on/off state

✅ For immediate actions that take effect as soon as the control is changed

✅ When the control represents a system or feature state, not a choice among options

✅ For settings that can be changed frequently without confirmation

## Selected — do & don't

✅ **Do:** Use distinct visual cues (color, position, icon) to clearly differentiate between on and off states.  
❌ **Don't:** Rely solely on color to indicate the selected state—users with color blindness may not perceive the difference.

✅ **Do:** Position the cursor to the right of the track for "on" and left for "off" to match user expectations.  
❌ **Don't:** Invert the cursor position convention as this creates confusion about which state is active.

✅ **Do:** Apply the action immediately when the user toggles the switch without requiring a separate save action.  
❌ **Don't:** Use switches for actions that require confirmation or have significant consequences.

✅ **Do:** Display a checkmark icon inside the cursor when selected to reinforce the active state visually.  
❌ **Don't:** Add animation that delays the visual feedback of state change beyond 200ms.

✅ **Do:** Ensure the default state (usually off) makes sense for first-time users and respects privacy.  
❌ **Don't:** Pre-select switches in ways that may trick users into enabling unwanted features.

## Error — do & don't

✅ **Do:** Display error messages directly below the switch with clear, actionable text explaining how to resolve the issue.  
❌ **Don't:** Use generic error messages like "Invalid selection" without specifying what the user should do.

✅ **Do:** Use a distinct error color (typically red) for the divider and icon to draw attention to the validation issue.  
❌ **Don't:** Rely solely on color to indicate errors—include an icon and text for accessibility.

✅ **Do:** Provide different error messages for selected and unselected states when the context requires clarification.  
❌ **Don't:** Show the same error message regardless of the switch state if the required action differs.

✅ **Do:** Associate error messages with the switch using `aria-describedby` for screen reader accessibility.  
❌ **Don't:** Position error messages far from the switch where users may not notice them.

✅ **Do:** Clear the error state immediately when the user corrects the issue by toggling the switch.  
❌ **Don't:** Require users to perform additional actions (like clicking a "validate" button) to clear error states.

## Reverse — do & don't

✅ **Do:** Use the reverse layout consistently throughout RTL (right-to-left) language interfaces.  
❌ **Don't:** Mix default and reverse layouts inconsistently within the same screen or context.

✅ **Do:** Apply the reverse layout when the switch control needs to be the primary visual anchor on the left.  
❌ **Don't:** Use reverse layout arbitrarily—always have a clear UX rationale for the choice.

✅ **Do:** Maintain the same touch target size and spacing in both default and reverse layouts.  
❌ **Don't:** Reduce interactive area when switching layouts as this affects accessibility.

✅ **Do:** Test both layouts with screen readers to ensure announcement order remains logical.  
❌ **Don't:** Assume visual order matches reading order—verify with assistive technologies.

✅ **Do:** Use reverse layout on mobile when the switch is the primary action and needs immediate thumb access.  
❌ **Don't:** Switch between layouts based on screen size without considering consistency.

## Other boolean options — do & don't

✅ **Do:** Include description text when the label alone doesn't provide enough context for users to make informed decisions.  
❌ **Don't:** Add description text that merely repeats the label or provides no additional value.

✅ **Do:** Use icons that clearly represent the category or type of setting being controlled.  
❌ **Don't:** Use decorative icons that don't add meaning or could be confused with interactive elements.

✅ **Do:** Use dividers to visually group related switch items and improve scanability in long lists.  
❌ **Don't:** Add dividers between every switch item when they create visual noise without aiding comprehension.

✅ **Do:** Display error messages only when the switch state genuinely conflicts with system or form requirements.  
❌ **Don't:** Show error messages for optional switches that have valid states in both on and off positions.

✅ **Do:** Keep description text concise—ideally one line—to maintain visual hierarchy.  
❌ **Don't:** Use description text as a substitute for proper documentation or help content.

## State — do & don't

✅ **Do:** Use the disabled state only when the switch will become available based on another condition or user action.  
❌ **Don't:** Disable switches without providing context about why or how to enable them.

✅ **Do:** Ensure the focus state has a visible indicator with at least 3:1 contrast ratio against adjacent colors.  
❌ **Don't:** Remove the default focus outline without providing an equally prominent custom indicator.

✅ **Do:** Use skeleton states during initial page load to indicate where interactive content will appear.  
❌ **Don't:** Display skeleton states for more than a few seconds as users may perceive this as broken functionality.

✅ **Do:** Make the read-only state visually distinct from disabled to communicate that the value is intentionally locked.  
❌ **Don't:** Use read-only when disabled would be more appropriate—read-only implies the value is meaningful and intentional.

✅ **Do:** Provide visual feedback during the pressed state to confirm the user's action was registered.  
❌ **Don't:** Allow the pressed state to persist longer than necessary as it may confuse users about the actual toggle state.
