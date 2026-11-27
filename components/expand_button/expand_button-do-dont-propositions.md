# Expand button — do & don't propositions

AI-generated propositions that no one has validated yet. They are not part of the documentation ([expand_button.md](expand_button.md)) and are not shown on zeroheight. Once a designer validates one, it moves into the full file.

## When to use

✅ To expand or collapse additional content or details

✅ When saving space while preserving access to information

✅ For controlling hierarchical or progressively disclosed content

✅ When the action affects only content visibility, not data or system state

## Appearance — do & don't

✅ **Do:** Use Default appearance for most standard expand/collapse interactions to maintain visual consistency across the interface.  
❌ **Don't:** Use Strong or Brand variants for every expandable section, as this diminishes their visual impact and importance.

✅ **Do:** Reserve Strong appearance for critical or high-priority expandable content that users must notice, such as payment details or important warnings.  
❌ **Don't:** Mix multiple high-emphasis variants (Strong and Brand) in the same view, creating visual competition.

✅ **Do:** Use Minimal appearance for secondary or nested expandable content to create clear visual hierarchy.  
❌ **Don't:** Use Minimal variant for primary actions or important content that users might overlook.

✅ **Do:** Apply Brand appearance sparingly for promotional content or branded moments that align with marketing campaigns.  
❌ **Don't:** Use Brand appearance throughout an interface, diluting brand emphasis and creating visual noise.

✅ **Do:** Maintain consistent appearance choices within the same context or component group.  
❌ **Don't:** Randomly alternate between appearance variants without a clear hierarchical purpose.

## Expanded — do & don't

✅ **Do:** Use clear visual indicators (chevron rotation) to communicate expanded/collapsed state immediately.  
❌ **Don't:** Rely solely on content visibility to indicate state; always update the button's visual affordance.

✅ **Do:** Ensure the chevron icon rotates smoothly (down → up) to reinforce state change with visual continuity.  
❌ **Don't:** Use inconsistent icon directions or swap between different icon types for expand/collapse states.

✅ **Do:** Announce state changes to screen readers using `aria-expanded` attribute that updates dynamically.  
❌ **Don't:** Omit `aria-expanded` or fail to update it when the expanded state changes.

✅ **Do:** Consider starting critical content sections in an expanded state if users typically need that information.  
❌ **Don't:** Force users to expand every section when the majority would benefit from seeing content by default.

✅ **Do:** Preserve the user's expanded/collapsed state choices when they return to a page within the same session.  
❌ **Don't:** Reset all sections to collapsed state on every page load if users have expressed preferences.

## Icon only — do & don't

✅ **Do:** Always provide an accessible name via `aria-label` when using icon-only buttons.  
❌ **Don't:** Assume users will understand icon-only buttons without providing accessible text for screen readers.

✅ **Do:** Use icon-only buttons only when space is constrained and the icon's meaning is universally understood.  
❌ **Don't:** Default to icon-only for all expand buttons; prefer labeled buttons for better usability.

✅ **Do:** Provide a tooltip on hover/focus to help sighted users understand the icon-only button's purpose.  
❌ **Don't:** Rely solely on `aria-label` for tooltip functionality; use a visible tooltip for all users.

✅ **Do:** Ensure icon-only buttons meet minimum touch target size requirements (44×44px) for mobile accessibility.  
❌ **Don't:** Create icon-only buttons that are too small to tap accurately on touch devices.

✅ **Do:** Use descriptive `aria-label` text like "Expand filters" rather than just "Expand".  
❌ **Don't:** Use generic labels that don't provide context about what content will be expanded.

## Rounded corner — do & don't

✅ **Do:** Use square corners (False) for standard business interfaces and professional contexts.  
❌ **Don't:** Apply rounded corners inconsistently across similar components in the same interface.

✅ **Do:** Apply rounded corners for immersive, emotional, or brand-focused experiences where softer aesthetics align with the design direction.  
❌ **Don't:** Mix square and rounded corner styles on the same page without a clear design rationale.

✅ **Do:** Maintain consistent corner radius with other interactive elements (buttons, cards) in the same context.  
❌ **Don't:** Use rounded expand buttons alongside square standard buttons, creating visual inconsistency.

✅ **Do:** Consider the overall design language and brand guidelines when choosing corner style.  
❌ **Don't:** Default to rounded corners just because they look "modern" without considering brand alignment.

✅ **Do:** Document corner radius choices in your design system to ensure team consistency.  
❌ **Don't:** Let individual designers choose corner styles ad-hoc without design system governance.
