# Guideline

## Intro 👈🤖

Expand button toggles content visibility, enabling users to progressively reveal or collapse sections while reducing visual clutter.

---

## Definition

Expand button is a control that toggles content visibility, allowing users to expand or collapse sections. It reduces visual clutter by showing only key information and providing access to more details when needed.

---

## Best for 👈🤔

✅ FAQ sections where questions can be expanded to reveal answers

✅ Collapsible panels that hide advanced or secondary options

✅ Mobile interfaces where screen space is limited

✅ Progressive disclosure of product details or specifications

✅ Settings menus with expandable advanced options

✅ Filtering panels with collapsible category groups

✅ Checkout flows revealing additional payment or shipping details

✅ Data tables with expandable row details

✅ Navigation menus with collapsible sub-sections

✅ Form sections that reveal conditional fields based on context

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Container | Houses all button elements and defines interactive hit area | N |
| 2 | Label | Descriptive text indicating the expandable content or action | Y |
| 3 | Icon | Visual indicator (chevron) showing expand/collapse direction | N |
| 4 | Background | Visual surface providing hierarchy and state feedback | N |
| 5 | Border | Defines button boundaries; varies by appearance variant | Y |
| 6 | Focus ring | Visible outline indicating keyboard focus for accessibility | N |
| 7 | Loading indicator | Spinner replacing icon during async content loading | Y |

---

## Appearance

**`Default`** Default expand buttons are used for standard interactions where expanding or collapsing content does not require strong emphasis. They provide a balanced and neutral look suitable for most layouts.
Use case: Expanding FAQ sections or showing additional text in articles.

**`Strong`** The Strong expand button is prominent and visually emphasized, reserved for the most important expandable sections where visibility and clarity are critical.
Use case: Expanding a key section in a form, such as "Payment details" in a checkout process.

**`Brand`** The Brand expand button uses the brand's primary color as an alternative to the Strong button. It should be used sparingly to anchor a branded moment or highlight a special section.
Use case: Expanding promotional or branded content blocks.

**`Minimal`** Minimal expand buttons are lightweight and understated, best for secondary or less critical expandable areas. They reduce visual noise and integrate seamlessly with simple layouts.
Use case: Expanding advanced options in a settings menu or filters in a search panel.

---

## appearance_do_&_dont 👈🤔

✅ **Do:** Use Default appearance for most standard expand/collapse interactions to maintain visual consistency across the interface.  
❌ **Don't:** Use Strong or Brand variants for every expandable section, as this diminishes their visual impact and importance.

✅ **Do:** Reserve Strong appearance for critical or high-priority expandable content that users must notice, such as payment details or important warnings.  
❌ **Don't:** Mix multiple high-emphasis variants (Strong and Brand) in the same view, creating visual competition.

✅ **Do:** Use Minimal appearance for secondary or nested expandable content to create clear visual hierarchy.  
❌ **Don't:** Use Minimal variant for primary actions or important content that users might overlook.

✅ **Do:** Apply Brand appearance sparingly for promotional content or branded moments that align with marketing campaigns.  
❌ **Don't:** Use Brand appearance throughout an interface, diluting brand emphasis and creating visual noise.

✅ **Do:** Maintain consistent appearance choices within the same context or component group.  
❌ **Don't:** Randomly alternate between appearance variants without a clear hierarchical purpose.

---

## Expanded

**`False`** The Expanded = false state indicates that the content controlled by the button is currently hidden or collapsed. The button should visually suggest that more information is available (e.g., with a downward chevron).
Use case: Default state in FAQs, dropdowns, or collapsible panels before the user interacts with them.

**`True`** The Expanded = true state indicates that the content has been revealed or expanded. The button should update its visual affordance to show that the section is open (e.g., with an upward chevron) and that it can be collapsed again.
Use case: Active state when a user expands details, advanced options, or additional filters in a panel.

---

## expanded_do_&_dont 👈🤔

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

---

## Icon only

**`False`** The Icon only = false state displays both a text label and an icon. This version provides greater clarity and is recommended when users may need additional context to understand the button's action.
Use case: Expanding or collapsing sections in forms or settings, where descriptive text improves usability.

**`True`** The Icon only = true state displays only the icon without a visible label. It creates a more compact appearance, suitable for space-constrained layouts or when the icon meaning is universally understood. For accessibility, always provide an alternative text label via aria-label or a tooltip.
Use case: Expanding or collapsing filters, toolbars, or mobile panels where space is limited.

---

## icon_only_do_&_dont 👈🤔

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

---

## Rounded corner

**`False`** For a square finish.

**`True`** For a finish with rounded corner.
To be favored in more emotional, immersive contexts or those tied to specific visual identities. For standard or business-oriented journeys, keep the default corners. This evolution addresses the need for flexibility in adapting the design to certain brand contexts.

---

## rounded_corner_do_&_dont 👈🤔

✅ **Do:** Use square corners (False) for standard business interfaces and professional contexts.  
❌ **Don't:** Apply rounded corners inconsistently across similar components in the same interface.

✅ **Do:** Apply rounded corners for immersive, emotional, or brand-focused experiences where softer aesthetics align with the design direction.  
❌ **Don't:** Mix square and rounded corner styles on the same page without a clear design rationale.

✅ **Do:** Maintain consistent corner radius with other interactive elements (buttons, cards) in the same context.  
❌ **Don't:** Use rounded expand buttons alongside square standard buttons, creating visual inconsistency.

✅ **Do:** Consider the overall design language and brand guidelines when choosing corner style.  
❌ **Don't:** Default to rounded corners just because they look "modern" without considering brand alignment.

✅ **Do:** Document corner radius choices in your design system to ensure team consistency.  
❌ **Don't:** Let individual designers choose corner styles ad-hoc without design system governance.

---

# Specs

## States

**`Enabled`** The default state of the Expand button when it is available for interaction.
Use case: A collapsed section ready to be expanded by the user.

**`Hover`** The state when a user places the pointer over the Expand button without activating it. Provides a visual cue that the element is interactive.
Use case: Highlighting that a FAQ or dropdown section can be opened.

**`Focus`** The state when the button is selected via keyboard or voice command but not yet activated. Usually shows an outline or border to ensure accessibility.
Use case: Allowing users with keyboard navigation to expand or collapse sections clearly.

**`Pressed`** A transient state indicating that the user has clicked or tapped the Expand button and the action is being executed.
Use case: User presses the button to reveal advanced options in a form.

**`Loading`** Used when expanding content requires fetching or processing data before it is displayed. The button shows a loading indicator.
Use case: Expanding a collapsible panel that loads additional product details from the server.

**`Disabled`** Indicates that the Expand button cannot be interacted with, for example when expansion is not allowed or content is unavailable.
Use case: Expand option disabled for sections restricted to certain user roles.

**`Skeleton`** A placeholder state that represents the Expand button before it is fully loaded. Improves perceived performance by showing the button will appear soon.
Use case: During initial page load when collapsible components are still being fetched.

---

## Layout and spacing

🚧 Content to be added

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Sep 28, 2025 | 3.1.0 | <ul><li>Brand variant: New background and content color tokens added for hover/pressed/loading/focus states <li>The name of the "Hierarchy" variant has been replaced to "Appearance"</ul> | Maxime Tonnerre |
| Jul 24, 2025 | 3.0.0 | <ul><li>New hierarchical variant: Brand → [Component tokens changelog 1.4.0](https://www.figma.com/design/Co2t6wHMf4GB9NJVGs2Hes/-OUDS-Core-Lib--Design-tokens?m=auto&node-id=9280-2568&t=HLVB4jOd35DWr8Bj-1) <li>Rounded corner property is now available → [Component tokens changelog 1.4.0](https://www.figma.com/design/Co2t6wHMf4GB9NJVGs2Hes/-OUDS-Core-Lib--Design-tokens?m=auto&node-id=9280-2568&t=HLVB4jOd35DWr8Bj-1) <li>Minimal variant: Color and width border tokens removed <li>Minimal variant: Color background tokens removed in the enabled state <li>Minimal variant: Color background tokens removed in the loading state <li>Minimal variant: Color background tokens removed in the disabled state</ul> | Maxime Tonnerre |
| Jul 21, 2025 | 2.1.0 | <ul><li>Several design token updates: [Component tokens changelog 1.3.0](https://www.figma.com/design/Co2t6wHMf4GB9NJVGs2Hes/-OUDS-Core-Lib--Design-tokens?m=auto&node-id=9280-2568&t=HLVB4jOd35DWr8Bj-1) <li>Button: Expanded: The chevron is also present in the 'icon only' variant. The gap between these 2 elements is defined by a design token: ouds-action-button-space-column-gap-icon-chevron→ouds-space-column-gap-2xs</ul> | Maxime Tonnerre |
| Apr 19, 2025 | 2.0.0 | <ul><li>Creation of "On colored bg" variant</ul> | Maxime Tonnerre |
| Dec 5, 2024 | 1.0.0 | <ul><li>Component creation</ul> | Maxime Tonnerre |