A Navigation button must provide clear navigation between pages, remain accessible to all users, and communicate both the action and the current position within a sequence. Following these guidelines ensures compliance with WCAG 2.1 standards and a consistent user experience.

**Semantics and Structure**
Always use the semantic HTML `<button>` or `<a>` element for pagination controls. This ensures native accessibility and correct behavior with assistive technologies.
If non-semantic elements are used, apply the appropriate ARIA role (e.g., `role="button"` or `role="link"`).
Manage proper keyboard navigation across all pagination elements.

**Accessible Text**
Each Navigation button must provide clear and descriptive text or an accessible name ("Next page", "Previous page", "Page 3").
For Icon only variants, always provide a text alternative via:
* The `aria-label` attribute (e.g., `aria-label="Next page"`), or
* Hidden screen reader text (using `.sr-only`).

**Visible Focus**
Navigation buttons must display a clear and visible focus state when navigated via keyboard (outline or highlight).
Never disable or remove the native browser focus indicator without providing an accessible alternative.

**Screen Reader Compatibility**
Ensure that pagination communicates the user's current location within a sequence. Use attributes such as:
* `aria-current="page"` for the active page,
* `aria-disabled="true"` for unavailable navigation buttons ("Previous" on the first page). This helps screen reader users understand context.

**Keyboard Navigation**
Navigation buttons must be fully operable with a keyboard.
* Use Tab to move between pagination controls.
* Use Enter or Space to activate the selected button. Ensure logical order so that navigation flows consistently (from "Previous" to numbered pages to "Next").

**Animation and Feedback**
While pagination typically changes the page instantly, provide smooth transitions or loading states when content requires time to render.
Indicate clearly when new content is being loaded (loading spinner or skeleton state).

**Best Practices**
* Keep pagination simple and predictable; avoid unnecessary variations.
* Clearly distinguish the active page from inactive buttons.
* Use Disabled states for unavailable actions ("Next" on the last page).
* For long lists, consider combining pagination with additional navigation ("Jump to page").
