A button component must be clearly identifiable, easily navigable via keyboard, accessible to screen readers, and offer intuitive interaction for all users. Adopting these guidelines ensures compliance with WCAG 2.1 standards and an inclusive user experience.

**Semantics and Structure**
Ensure that each button has a clear and defined action.
Always use the HTML `<button>` element for buttons, as it is natively accessible and supported by assistive technologies (screen readers).
Avoid using `<div>` or `<span>` styled as buttons, unless absolutely necessary. In such cases:
* Add the appropriate ARIA role: `role="button"`.
* Manage keyboard navigation properly.

**Accessible Text**
The button's visible text should be clear and easy to understand ("Send" or "Add to Cart").
Avoid unlabeled or empty buttons.
If the button contains only an icon, provide a textual alternative using:
* The `aria-label` attribute (`aria-label="Search"`), or
* Hidden screen-reader text (using CSS techniques such as `.sr-only`).

**Visible Focus**
The button must display a clear and visible focus style when navigated to via keyboard (a border or highlight).
Never disable the browser's native focus state without providing an alternative.

**Screen Reader Compatibility**
The button's role is automatically detected when using the `<button>` element. If another element is used, add `role="button"`.
Provide additional context with `aria-label` or `aria-describedby` if the button's action is not clear from the visible text.
Use ARIA technologies to notify screen readers of changes if necessary (`aria-live`).

**Keyboard Navigation**
If the button serves a specific role (opening a menu), ensure interactions are intuitive and align with user expectations.
Users must be able to navigate to and activate the button using only the keyboard:
* Use the Tab key for navigation.
* Use Enter or Space for activation.
