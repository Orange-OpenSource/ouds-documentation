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