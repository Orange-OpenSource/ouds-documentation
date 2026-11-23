# Button — do & don't propositions

AI-generated propositions that no one has validated yet. They are not part of the documentation ([button.md](button.md)) and are not shown on zeroheight. Once a designer validates one, it moves into the full file.

## When to use

✅ To trigger actions that change system state or initiate a process

✅ For primary and secondary call-to-actions that require visual emphasis and explicit interaction

✅ For confirming intent, managing states, scenario-based navigation, and destructive actions

✅ Use a button when an immediate system response is expected, rather than simple navigation via a link

## Appearance — do & don't

✅ **Do:** Use only one Strong or Brand button per view to establish a clear visual hierarchy and guide users to the primary action.  
❌ **Don't:** Place multiple high-emphasis buttons together, which confuses users about which action is most important.

✅ **Do:** Reserve Negative buttons exclusively for destructive actions like "Delete" or "Remove" that require user awareness of consequences.  
❌ **Don't:** Use Negative styling for cancel actions or secondary dismissals that aren't truly destructive.

✅ **Do:** Pair Default (outline) buttons with Strong buttons to create clear primary/secondary action relationships.  
❌ **Don't:** Use Minimal buttons for important actions that users might miss due to low visual prominence.

✅ **Do:** Use Brand buttons sparingly for specific brand moments or high-value marketing actions to maintain their impact.  
❌ **Don't:** Use Brand buttons as the default primary throughout the interface, which dilutes brand emphasis.

✅ **Do:** Match button appearance to action importance—Strong for primary, Default for secondary, Minimal for tertiary.  
❌ **Don't:** Mix visual hierarchies inconsistently across similar workflows, creating unpredictable user experiences.

## Layouts — do & don't

✅ **Do:** Use Text only as the default layout, as text labels provide the clearest communication of button actions.  
❌ **Don't:** Default to icon-only buttons when space allows for text labels, sacrificing clarity for aesthetics.

✅ **Do:** Provide an accessible name via `aria-label` for icon-only buttons and include tooltips to explain the action on hover/focus.  
❌ **Don't:** Use icon-only buttons without accessible labels, making them incomprehensible to screen reader users.

✅ **Do:** Place icons before text labels (leading position) to maintain reading flow and visual consistency.  
❌ **Don't:** Position icons after text unless specifically indicating direction (e.g., "Next →") or external links.

✅ **Do:** Use icons that universally reinforce the action meaning, such as a trash icon for delete or download icon for download.  
❌ **Don't:** Add decorative icons that don't enhance understanding of the button's purpose.

✅ **Do:** Reserve icon-only buttons for well-established, universally recognized actions like close (×), settings (⚙), or search (🔍).  
❌ **Don't:** Use icon-only buttons for complex or ambiguous actions that require text explanation.

## Rounded corner — do & don't

✅ **Do:** Use square corners (False) for standard business interfaces and professional applications to maintain a clean, structured appearance.  
❌ **Don't:** Mix rounded and square buttons inconsistently within the same interface or workflow.

✅ **Do:** Apply rounded corners (True) consistently across all buttons within emotional, lifestyle, or brand-focused experiences.  
❌ **Don't:** Use rounded corners arbitrarily without considering the overall visual identity and context.

✅ **Do:** Consider rounded corners for consumer-facing, mobile-first, or entertainment-focused applications where a softer aesthetic is appropriate.  
❌ **Don't:** Switch between corner styles mid-journey, creating visual inconsistency and confusion.

✅ **Do:** Align rounded corner usage with the broader design system and component library styling conventions.  
❌ **Don't:** Override global corner radius settings for individual buttons without design system approval.

✅ **Do:** Test rounded corner buttons to ensure touch targets remain sufficient (minimum 48×48dp) for mobile interactions.  
❌ **Don't:** Apply extreme border radius values that distort button proportions or reduce usable tap areas.

## Specific component: On colored bg — do & don't

✅ **Do:** Use the "On colored bg" variant when placing buttons over images, gradients, or brand-colored backgrounds where contrast cannot be guaranteed.  
❌ **Don't:** Use standard button variants on unpredictable backgrounds where they may fail contrast requirements.

✅ **Do:** Apply inverted colors consistently—black finish in light mode and white finish in dark mode—to ensure WCAG 2.1 AA compliance.  
❌ **Don't:** Mix inverted and non-inverted buttons on the same colored background, creating visual inconsistency.

✅ **Do:** Test button contrast against all possible background variations, including images with varying light and dark areas.  
❌ **Don't:** Assume a single static color variant will work across dynamic or user-generated background content.

✅ **Do:** Consider adding subtle shadows or overlays behind buttons on complex backgrounds to improve legibility.  
❌ **Don't:** Rely solely on color inversion when background complexity requires additional visual separation techniques.

✅ **Do:** Verify that focus states and hover states also maintain sufficient contrast on colored backgrounds.  
❌ **Don't:** Forget to test interactive states, which may reveal contrast issues not visible in the enabled state.
