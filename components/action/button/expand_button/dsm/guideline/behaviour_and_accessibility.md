An Expand button must clearly communicate its purpose, be accessible via keyboard and screen readers, and provide intuitive toggling between expanded and collapsed states. Following these guidelines ensures compliance with WCAG 2.1 standards and a consistent, inclusive user experience.

**Semantics and Structure**
Always use the semantic HTML `<button>` element for expand/collapse controls. This ensures native accessibility and correct support by assistive technologies.
If a non-semantic element is used, add the appropriate ARIA role (e.g., `role="button"`) and manage keyboard navigation properly.
Use the `aria-expanded` attribute to indicate the current state of the control (true = expanded, false = collapsed).

**Accessible Text**
The button must include a clear and descriptive label ("Expand details", "Collapse section").
For Icon only variants, provide a text alternative via:
* The `aria-label` attribute (e.g., `aria-label="Expand filters"`), or
* Hidden screen-reader text (using `.sr-only`). Avoid unlabeled or ambiguous expand buttons.

**Visible Focus**
The button must display a clear and visible focus indicator when navigated via keyboard (outline or highlight).
Never disable or remove the browser's native focus indicator without providing an accessible replacement.

**Screen Reader Compatibility**
Communicate the expand/collapse state to screen readers using `aria-expanded`.
If the control manages visibility of a specific region, use `aria-controls` to reference the content area.
This ensures that users of assistive technologies understand both the action and its effect.

**Keyboard Navigation**
Expand buttons must be fully operable using the keyboard:
* Use Tab to navigate to the button.
* Use Enter or Space to toggle between expanded and collapsed states. Ensure logical navigation order so users can seamlessly move through collapsible sections.

**Animation and Feedback**
Provide smooth transitions between expanded and collapsed states. This not only improves the user experience but also reinforces the action taken.
Keep animations short and subtle to avoid distracting from the content.

**Best Practices**
* Use Tab to navigate to the button.
* Ensure consistency: use the same iconography (chevrons, plus/minus) across the system.
* Avoid nesting too many expandable areas, as this can make navigation confusing.
* Always make the current state clear — users should instantly know whether a section is open or closed.
