# Guideline

## Intro 👈🤖

A Navigation button enables users to move between pages in multi-page interfaces like search results, product listings, or data tables.

---

## Definition

A Navigation button is a navigational UI element that allows users to move between different pages of content within a multi-page interface, such as lists, search results, or data tables. Typically arranged in a sequence, Navigation buttons indicate the user's current position and provide controls to access previous, next, or specific pages.

---

## Best for 👈🤔

✅ Multi-step form navigation where users move forward or backward through sequential steps

✅ Product catalog or search results pagination requiring next/previous page controls

✅ Data table navigation with large datasets split across multiple pages

✅ Article series or tutorial sequences where content flows linearly

✅ Carousel or slideshow controls for browsing visual content

✅ Checkout flow progression where users advance through purchasing steps

✅ FAQ or documentation pages with related content split into sections

✅ Mobile interfaces where compact icon-only navigation saves screen space

✅ Admin dashboards with paginated lists of records or entries

✅ Wizard-style interfaces guiding users through a defined sequence

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Container | Defines the button boundaries and touch/click target area | N |
| 2 | Label | Text indicating the navigation direction ("Next", "Previous") | Y |
| 3 | Icon | Directional arrow (chevron) reinforcing the navigation action | N |
| 4 | Background | Visual surface providing contrast and state feedback | N |
| 5 | Border | Defines button edges, varies by appearance variant | Y |
| 6 | Loading indicator | Spinner shown during content loading states | Y |
| 7 | Focus ring | Visual indicator for keyboard focus accessibility | N |

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

## appearance_do_&_dont 👈🤔

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

---

## Layouts

**`Next`** The Next layout button is used to move the user forward in a sequence of content, steps, or pages.
Use case: Navigating to the next page in a multi-step form, product catalog, or article series.

**`Previous`** The Previous layout button allows the user to return to the prior step, page, or section.
Use case: Going back to the previous step in a checkout flow or returning to the prior search results page.

---

## layouts_do_&_dont 👈🤔

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

---

## Icon only

**`False`** When Icon only is set to false, the button displays both an icon and a text label. This makes the action more explicit and accessible, especially for new users or in contexts where clarity is critical.
Use case: Using a "Next" button with both text and icon in a multi-step checkout flow to ensure the action is clearly understood.

**`True`** The Icon only Navigation button is used in layouts where space is limited or where a minimalist design is required. It relies solely on universally recognized icons (such as arrows) to indicate navigation actions without additional text. This variant should be applied selectively — for example in carousels, mobile navigation bars, or compact toolbars — where the context makes the meaning obvious. To ensure accessibility, it must always be paired with a hidden text label (via aria-label or tooltip) so that assistive technologies can convey the action clearly.

---

## icon_only_do_&_dont 👈🤔

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

---

## Rounded corner

**`False`** For a square finish.

**`True`** For a finish with rounded corner.
To be favored in more emotional, immersive contexts or those tied to specific visual identities. For standard or business-oriented journeys, keep the default corners. This evolution addresses the need for flexibility in adapting the design to certain brand contexts.

---

## rounded_corner_do_&_dont 👈🤔

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

---

## Specific component: On colored bg

This variant ensures a sufficiently high level of accessibility when the component is used on a background that is "out of control".

**To invert color**
• In light mode: For a black finish
• In dark mode: For a white finish

---

## specific_component_on_colored_bg_do_&_dont 👈🤔

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

---

# Specs

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

## Layout and spacing

🚧 Content to be added

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Oct 10, 2025 | 3.2.0 | New component name: Navigation button (vs Pagination button) The specific component "On colored bg" has been split into two distinct components: <ul><li>A public version offering traditional management of dark and light modes <li>A private version (allowing the core team to nest the component with other components) offering customized mode management with four possible configurations: <ul><li>Always in light mode <li>Always in dark mode <li>Light to dark mode <li>Dark to light mode </ul><li>Consequently, for the private version, the name of the "Inverted color" variant has been replaced to "Mode control".</ul> | Maxime Tonnerre |
| Sep 28, 2025 | 3.1.0 | <ul><li>Brand variant: New background and content color tokens added for hover/pressed/loading/focus states <li>The name of the "Hierarchy" variant has been replaced to "Appearance"</ul> | Maxime Tonnerre |
| Jul 24, 2025 | 3.0.0 | <ul><li>New hierarchical variant: Brand → [Component tokens changelog 1.4.0](https://www.figma.com/design/Co2t6wHMf4GB9NJVGs2Hes/-OUDS-Core-Lib--Design-tokens?m=auto&node-id=9280-2568&t=HLVB4jOd35DWr8Bj-1) <li>Rounded corner property is now available → [Component tokens changelog 1.4.0](https://www.figma.com/design/Co2t6wHMf4GB9NJVGs2Hes/-OUDS-Core-Lib--Design-tokens?m=auto&node-id=9280-2568&t=HLVB4jOd35DWr8Bj-1) <li>Minimal variant: Color and width border tokens removed <li>Minimal variant: Color background tokens removed in the enabled state <li>Minimal variant: Color background tokens removed in the loading state <li>Minimal variant: Color background tokens removed in the disabled state</ul> | Maxime Tonnerre |
| Jul 21, 2025 | 2.1.0 | <ul><li>Several design token updates: [Component tokens changelog 1.3.0](https://www.figma.com/design/Co2t6wHMf4GB9NJVGs2Hes/-OUDS-Core-Lib--Design-tokens?m=auto&node-id=9280-2568&t=HLVB4jOd35DWr8Bj-1) <li>Button: Expanded: The chevron is also present in the 'icon only' variant. The gap between these 2 elements is defined by a design token: ouds-action-button-space-column-gap-icon-chevron→ouds-space-column-gap-2xs</ul> | Maxime Tonnerre |
| Apr 19, 2025 | 2.0.0 | <ul><li>Creation of "On colored bg" variant</ul> | Maxime Tonnerre |
| Dec 5, 2024 | 1.0.0 | <ul><li>Component creation</ul> | Maxime Tonnerre |