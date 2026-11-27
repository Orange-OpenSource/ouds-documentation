# Badge — do & don't propositions

AI-generated propositions that no one has validated yet. They are not part of the documentation ([badge.md](badge.md)) and are not shown on zeroheight. Once a designer validates one, it moves into the full file.

## Status — do & don't

✅ **Do:** Use semantic colors consistently—green for positive outcomes, red for errors, blue for informational content, yellow for warnings.  
❌ **Don't:** Use random colors that don't align with established semantic meanings in your design system.

✅ **Do:** Reserve negative (red) status for critical issues requiring immediate attention like errors or failures.  
❌ **Don't:** Overuse negative status badges, which desensitizes users to actual critical information.

✅ **Do:** Use neutral status for general labels that don't carry semantic weight or emotional connotation.  
❌ **Don't:** Use neutral badges when a specific status color would better communicate the intended meaning.

✅ **Do:** Apply accent status to highlight new features, discoveries, or promotional content that needs emphasis.  
❌ **Don't:** Use accent badges for system status information where functional colors (positive, warning, negative) are more appropriate.

✅ **Do:** Use info status for non-urgent informational context like "In Progress" or "Pending Review".  
❌ **Don't:** Use info badges for states that require user action—use warning or negative instead.

## Size — do & don't

✅ **Do:** Choose badge size proportional to the element it accompanies—use xsmall for icons, medium for standard UI components.  
❌ **Don't:** Use oversized badges that visually overpower the primary content they're meant to supplement.

✅ **Do:** Maintain consistent badge sizes within the same context or view for visual harmony.  
❌ **Don't:** Mix multiple badge sizes randomly within the same component or list.

✅ **Do:** Use larger badges (medium or large) when the badge conveys critical status information that must be noticed.  
❌ **Don't:** Use xsmall badges for important status information that users might easily miss.

✅ **Do:** Consider touch target requirements when badges appear in mobile or touch interfaces—ensure adequate size for accessibility.  
❌ **Don't:** Use xsmall badges as the only status indicator in touch-heavy interfaces without supporting context.

✅ **Do:** Scale badge size appropriately across responsive breakpoints while maintaining the fixed-size principle within each viewport.  
❌ **Don't:** Allow badges to dynamically resize based on interface scaling, which contradicts the component's design intent.

## State — do & don't

✅ **Do:** Use the enabled state when the badge conveys actionable or relevant status information that users need to see.  
❌ **Don't:** Display enabled badges for outdated or irrelevant status that no longer applies.

✅ **Do:** Apply the disabled state when the associated element or feature is unavailable or inactive.  
❌ **Don't:** Use disabled badges as the primary way to hide information—consider removing the badge entirely if not needed.

✅ **Do:** Maintain consistent visual distinction between enabled and disabled states across all status variants.  
❌ **Don't:** Allow disabled badges to have the same visual weight as enabled badges, causing confusion.

✅ **Do:** Use disabled badges to indicate temporarily unavailable statuses that may become active later.  
❌ **Don't:** Use disabled state for permanent conditions—choose appropriate enabled status colors instead.

✅ **Do:** Ensure disabled badges still meet minimum contrast requirements for accessibility.  
❌ **Don't:** Make disabled badges so faint that users cannot perceive them at all.
