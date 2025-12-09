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

---

## Specific component: On colored bg

This variant ensures a sufficiently high level of accessibility when the component is used on a background that is "out of control".

**To invert color**
• In light mode: For a black finish
• In dark mode: For a white finish

---
