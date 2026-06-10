## Definition

A Navigation button is a navigational UI element that allows users to move between different pages of content within a multi-page interface, such as lists, search results, or data tables. Typically arranged in a sequence, Navigation buttons indicate the user's current position and provide controls to access previous, next, or specific pages.

---

## Appearance

**`Default`** Default Navigation buttons are used for navigation between pages that are not critical or emphasized. They typically represent inactive page states and support smooth movement across content.
Use case: Standard "next/previous" navigation in product listings or search results.

**`Strong`** The Strong Navigation button should be singular and prominent, reserved for highlighting the active page. It ensures the user always knows their current position within a sequence.
Use case: Highlighting the active page in long catalog navigation.

**`Brand`** A brand-colored alternative to the Strong Navigation button. It should be used sparingly for high-value navigation points or to visually anchor a brand moment. Avoid using it as the default for all pages.
Use case: Emphasizing a key page (e.g., a promotional offer) with the brand's primary color.

**`Minimal`** Minimal Navigation buttons are simplified and less emphasized, suitable when pagination is not the primary focus. They can be used independently or in combination with stronger buttons.
Use case: Secondary interfaces, such as blogs or FAQs, where pagination is less critical.

---

## Layouts

**`Next`** The Next layout button is used to move the user forward in a sequence of content, steps, or pages.
Use case: Navigating to the next page in a multi-step form, product catalog, or article series.

**`Previous`** The Previous layout button allows the user to return to the prior step, page, or section.
Use case: Going back to the previous step in a checkout flow or returning to the prior search results page.

---

## Icon only

**`False`** When Icon only is set to false, the button displays both an icon and a text label. This makes the action more explicit and accessible, especially for new users or in contexts where clarity is critical.
Use case: Using a "Next" button with both text and icon in a multi-step checkout flow to ensure the action is clearly understood.

**`True`** The Icon only Navigation button is used in layouts where space is limited or where a minimalist design is required. It relies solely on universally recognized icons (such as arrows) to indicate navigation actions without additional text. This variant should be applied selectively — for example in carousels, mobile navigation bars, or compact toolbars — where the context makes the meaning obvious. To ensure accessibility, it must always be paired with a hidden text label (via aria-label or tooltip) so that assistive technologies can convey the action clearly.

---

## States

**`Enabled`** The default state of the Navigation button when it is available for interaction. It represents a normal, ready-to-use navigation control.
Use case: Visible as the standard button for moving to the next or previous page.

**`Hover`** The state when a user places a pointing device over the Navigation button without yet clicking it. It provides a visual cue that the button is interactive.
Use case: Helps users identify the button as clickable when navigating with a mouse.

**`Focus`** The state when a Navigation button is selected via keyboard or voice command but not yet activated. It usually mirrors the hover style with an additional outline for clarity.
Use case: Ensures accessibility and visibility for keyboard or assistive technology users.

**`Pressed`** A transient state indicating that the user has taken action on the button and the navigation is in progress. It confirms the interaction before moving to the next page.
Use case: Shown briefly after clicking "Next" to indicate the command has been received.

**`Loading`** The state used when the Navigation button is fetching or processing data before displaying the next set of content. It uses a loading indicator to communicate progress.
Use case: Appears when moving between pages in a data-heavy table or search results.

**`Disabled`** Indicates that the Navigation button is not available for interaction, such as when the user is already on the first or last page.
Use case: "Previous" button disabled on the first page, or "Next" disabled on the last page.

**`Skeleton`** A placeholder state used while the Navigation button is still loading. It improves perceived performance by giving users a visual indication that the control will appear soon.
Use case: Displayed during initial page load or while waiting for navigation controls to render.

---

## Rounded corner

**`False`** For a square finish.

**`True`** For a finish with rounded corner.
To be favored in more emotional, immersive contexts or those tied to specific visual identities. For standard or business-oriented journeys, keep the default corners. This evolution addresses the need for flexibility in adapting the design to certain brand contexts.

**Brand theme availability**
This option is technically not available for all brand themes. Here's the list of rounded corners availability by brand theme:

| Brand theme | Availability |
|---|---|
| Orange | ✅ Available |
| Orange Compact | ✅ Available |
| Sosh | ❌ Unavailable |
| Wireframe | ❌ Unavailable |

---

## Specific component: On colored bg

This variant ensures a sufficiently high level of accessibility when the component is used on a background that is "out of control".

**To invert color**
• In light mode: For a black finish
• In dark mode: For a white finish

---

## Multiline and responsiveness

**Multiline**
This component allows multi-line text editing. Although the number of lines is not technically limited, it is recommended not to exceed one line of text.
Nevertheless, if the label spans multiple lines, the label remains horizontally centred and the chevron icon remains vertically centred.

**Max-width vs full-width**
For greater flexibility, this component doesn't have a default max-width. To avoid exceeding a width that would degrade readability and the perception of a compact interactive element, we recommend applying **a max-width of around 360px.**
The component can also naturally wrap within the parent container (or the screen in a mobile use context for exemple) and use the full available width.
Please note that this behavior is not the default rule; it may be preferred if the template allows it (to improve user comfort or for better page structure/hierarchy).

**User zoom in/out**
The behavior of the text during user zoom in/out must follow a fundamental principle: the text must remain readable, accessible, and must never break the structure or lose information.
* The text must always scale proportionally with user zoom. Text resizing must never be blocked.
* Zooming must never cause text to be truncated or hidden. The component must expand vertically to allow line wrapping.
* The component's height and width must be flexible, never fixed, in order to automatically adapt its dimensions according to the level of zoom.
* In order to preserve the minimun interactive area during user zoom out, this component have a min-width and a min-height **of 48px**.
* Even if, the component has a max-height or a max-width for resizing control purposes, technically, during user zoom in, these limitations are not fixed but must be scalable in order to adapt to the user's zoom level.
* As the chevron icon is functional, it must follow the same rules as text.

---

## Behaviour and accessibility

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

---
