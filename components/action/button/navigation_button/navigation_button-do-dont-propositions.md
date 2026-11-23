# Navigation button — do & don't propositions

AI-generated propositions that no one has validated yet. They are not part of the documentation ([navigation_button.md](navigation_button.md)) and are not shown on zeroheight. Once a designer validates one, it moves into the full file.

## When to use

✅ To move between pages, screens, or sections of the interface

✅ For navigation within navigational surfaces such as headers, sidebars, or menus

✅ When the action does not modify data, but changes context or route

✅ When a compact and predictable navigation control is required

## Appearance — do & don't

✅ **Do:** Use only one Strong or Brand variant per pagination group to indicate the active or primary action clearly.  
❌ **Don't:** Apply Strong or Brand appearance to all navigation buttons, which eliminates visual hierarchy and confuses users.

✅ **Do:** Reserve the Brand variant for high-value moments that align with marketing goals or brand emphasis.  
❌ **Don't:** Use the Brand variant as a default replacement for Strong, as it dilutes brand impact when overused.

✅ **Do:** Use Default appearance for standard next/previous controls that don't require special emphasis.  
❌ **Don't:** Mix multiple strong visual variants in a single navigation group, creating competing focal points.

✅ **Do:** Choose Minimal appearance for secondary contexts where pagination shouldn't dominate the interface.  
❌ **Don't:** Use Minimal variants in critical navigation flows where clear affordance is essential for task completion.

✅ **Do:** Maintain consistent appearance choices within a single pagination pattern or component instance.  
❌ **Don't:** Switch appearance variants dynamically based on hover or interaction states—appearance should remain stable.

## Layouts — do & don't

✅ **Do:** Position the Previous button on the left and Next button on the right following natural reading direction conventions.  
❌ **Don't:** Reverse the positions of Previous and Next buttons, which conflicts with established user expectations.

✅ **Do:** Ensure the Next button receives appropriate visual emphasis as the primary forward action in sequential flows.  
❌ **Don't:** Give Previous and Next buttons identical prominence when progression is the primary user goal.

✅ **Do:** Disable the Previous button on the first page and Next button on the last page rather than hiding them.  
❌ **Don't:** Hide navigation buttons entirely when unavailable, as users lose context about their position in the sequence.

✅ **Do:** Provide adequate spacing between Previous and Next buttons to prevent accidental clicks.  
❌ **Don't:** Place navigation buttons too close together, increasing the risk of user errors on touch devices.

✅ **Do:** Use consistent layout direction throughout the entire application or product experience.  
❌ **Don't:** Flip layout conventions between different sections, which creates cognitive dissonance for users.

## Icon only — do & don't

✅ **Do:** Always provide an accessible name via `aria-label` or visually hidden text for icon-only buttons.  
❌ **Don't:** Use icon-only buttons without accessible labels, which makes them meaningless to screen reader users.

✅ **Do:** Use icon-only variants only when the navigation context is abundantly clear from surrounding interface elements.  
❌ **Don't:** Default to icon-only in unfamiliar contexts where users may not understand the arrow's meaning.

✅ **Do:** Include tooltips on hover for icon-only buttons to provide additional context for sighted users.  
❌ **Don't:** Rely solely on tooltips for accessibility—they don't help keyboard or screen reader users effectively.

✅ **Do:** Prefer icon+label buttons for critical navigation actions like checkout progression or form submissions.  
❌ **Don't:** Use icon-only variants in high-stakes flows where misclicks could cause data loss or frustration.

✅ **Do:** Ensure icon-only buttons have adequate touch target size (minimum 44×44px) for mobile accessibility.  
❌ **Don't:** Reduce icon-only button size below recommended minimums, which creates usability barriers on touch devices.

## Rounded corner — do & don't

✅ **Do:** Use rounded corners consistently with other UI elements in the same interface for visual harmony.  
❌ **Don't:** Mix rounded and square navigation buttons within the same pagination component or page section.

✅ **Do:** Choose rounded corners for consumer-facing, lifestyle, or brand-forward experiences that benefit from softer aesthetics.  
❌ **Don't:** Apply rounded corners arbitrarily without considering whether they align with the overall design language.

✅ **Do:** Maintain square corners in business applications, enterprise tools, or data-heavy interfaces for a professional feel.  
❌ **Don't:** Use overly rounded corners in dense admin interfaces where they may appear out of place.

✅ **Do:** Apply the same corner radius value to all navigation buttons within a pagination group.  
❌ **Don't:** Vary corner radius between different button variants, creating visual inconsistency.

✅ **Do:** Consider the rounded corner setting as part of broader theming decisions that affect the entire design system.  
❌ **Don't:** Treat corner styling as a per-component decision that could fragment the user interface appearance.

## Specific component: On colored bg — do & don't

✅ **Do:** Use the inverted variant when placing navigation buttons on brand colors, images, or gradients.  
❌ **Don't:** Use standard navigation buttons on colored backgrounds where contrast requirements may not be met.

✅ **Do:** Test color contrast ratios meet WCAG 2.2 AA requirements (4.5:1 for text, 3:1 for UI components).  
❌ **Don't:** Assume the inverted variant automatically meets accessibility standards without verification.

✅ **Do:** Apply the inverted variant consistently to all navigation controls when used on the same colored background.  
❌ **Don't:** Mix inverted and standard variants on the same background, creating inconsistent visual treatment.

✅ **Do:** Use the appropriate inverted mode setting (light/dark) based on the current theme context.  
❌ **Don't:** Hardcode a specific inverted mode that doesn't adapt to system or user theme preferences.

✅ **Do:** Consider the inverted variant essential when backgrounds contain photography, patterns, or unpredictable colors.  
❌ **Don't:** Overlook the inverted variant when working with hero sections, banners, or promotional content areas.
