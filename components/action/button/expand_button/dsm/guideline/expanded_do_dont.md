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