# Guideline

## Intro 👈🤖

A button is an interactive element that triggers actions or events, enabling users to submit forms, navigate, or initiate workflows.

---

## Definition

A button is a fundamental interactive UI element that allows users to trigger an action or event within an interface, such as submitting a form, opening a dialog, or navigating to another page. Visually, it's typically styled to stand out as clickable, using shape, color, and label to convey its purpose.

---

## Best for 👈🤔

✅ Submitting form data or completing a transaction flow

✅ Primary call-to-action requiring immediate user attention

✅ Confirming or canceling actions in modal dialogs

✅ Triggering navigation to a new screen or page section

✅ Initiating file uploads, downloads, or data exports

✅ Executing destructive actions with confirmation (delete, remove)

✅ Toggling states or settings within compact interfaces

✅ Launching external applications or opening new browser windows

✅ Saving user progress or draft content

✅ Adding or removing items from lists, carts, or collections

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Container | Defines the interactive boundary and visual shape of the button | N |
| 2 | Text label | Communicates the action the button performs | Y |
| 3 | Leading icon | Provides visual context or reinforces the action meaning | Y |
| 4 | Loading indicator | Indicates an ongoing process after button activation | Y |
| 5 | Focus ring | Shows keyboard focus state for accessibility | N |
| 6 | Border | Defines button boundaries, especially for outline variants | Y |

---

## Appearance

**`Default`** Default buttons are used for actions which are not mandatory or essential for the user. Often screens will include multiple Outline buttons alongside one of the Full button.

**`Strong`** The Strong button on the page should be singular and prominent, ideally limited to one per view. It should be reserved for the most critical action, such as "Buy," "Save," "Submit," etc.

**`Brand`** A brand primary color alternative to the Strong button.
To be used sparingly for high-value specific actions or to visually anchor a brand moment. Do not use it as the default primary button in your interfaces.

**`Minimal`** Minimal buttons are commonly used for actions that are considered less crucial. They can be used independently or together with a strong button.

**`Negative`** Negative buttons should be used sparingly to warn of a destructive action, for example, delete or remove, typically resulting in the opening of a confirmation dialog.

---

## appearance_do_&_dont 👈🤔

✅ **Do:** Use only one Strong or Brand button per view to establish a clear visual hierarchy and guide users to the primary action.  
❌ **Don't:** Place multiple high-emphasis buttons together, which confuses users about which action is most important.

✅ **Do:** Reserve Negative buttons exclusively for destructive actions like "Delete" or "Remove" that require user awareness of consequences.  
❌ **Don't:** Use Negative styling for cancel actions or secondary dismissals that aren't truly destructive.

✅ **Do:** Pair Default (outline) buttons with Strong buttons to create clear primary/secondary action relationships.  
❌ **Don't:** Use Minimal buttons for important actions that users might miss due to low visual prominence.

✅ **Do:** Use Brand buttons sparingly for specific brand moments or high-value marketing actions to maintain their impact.  
❌ **Don't:** Use Brand buttons as the default primary throughout the interface, which dilutes brand emphasis.

✅ **Do:** Match button appearance to action importance—Strong for primary, Default for secondary, Minimal for tertiary.  
❌ **Don't:** Mix visual hierarchies inconsistently across similar workflows, creating unpredictable user experiences.

---

## Layouts

**`Text only`** This is the default layout of the component.

**`Text + icon`** This option includes functionality to choose any Solaris icon.
Its use must be restricted and remain specific to certain clearly identified contexts (e.g., the use of an icon within a "Play" button is standard in the context of TV or video streaming).

**`Icon only`** Typically utilized in business or back-office interfaces, it is rarely standalone (usually part of a group of elements).

---

## layouts_do_&_dont 👈🤔

✅ **Do:** Use Text only as the default layout, as text labels provide the clearest communication of button actions.  
❌ **Don't:** Default to icon-only buttons when space allows for text labels, sacrificing clarity for aesthetics.

✅ **Do:** Provide an accessible name via `aria-label` for icon-only buttons and include tooltips to explain the action on hover/focus.  
❌ **Don't:** Use icon-only buttons without accessible labels, making them incomprehensible to screen reader users.

✅ **Do:** Place icons before text labels (leading position) to maintain reading flow and visual consistency.  
❌ **Don't:** Position icons after text unless specifically indicating direction (e.g., "Next →") or external links.

✅ **Do:** Use icons that universally reinforce the action meaning, such as a trash icon for delete or download icon for download.  
❌ **Don't:** Add decorative icons that don't enhance understanding of the button's purpose.

✅ **Do:** Reserve icon-only buttons for well-established, universally recognized actions like close (×), settings (⚙), or search (🔍).  
❌ **Don't:** Use icon-only buttons for complex or ambiguous actions that require text explanation.

---

## Rounded corner

**`False`** For a square finish.

**`True`** For a finish with rounded corner.
To be favored in more emotional, immersive contexts or those tied to specific visual identities. For standard or business-oriented journeys, keep the default corners. This evolution addresses the need for flexibility in adapting the design to certain brand contexts.

---

## rounded_corner_do_&_dont 👈🤔

✅ **Do:** Use square corners (False) for standard business interfaces and professional applications to maintain a clean, structured appearance.  
❌ **Don't:** Mix rounded and square buttons inconsistently within the same interface or workflow.

✅ **Do:** Apply rounded corners (True) consistently across all buttons within emotional, lifestyle, or brand-focused experiences.  
❌ **Don't:** Use rounded corners arbitrarily without considering the overall visual identity and context.

✅ **Do:** Consider rounded corners for consumer-facing, mobile-first, or entertainment-focused applications where a softer aesthetic is appropriate.  
❌ **Don't:** Switch between corner styles mid-journey, creating visual inconsistency and confusion.

✅ **Do:** Align rounded corner usage with the broader design system and component library styling conventions.  
❌ **Don't:** Override global corner radius settings for individual buttons without design system approval.

✅ **Do:** Test rounded corner buttons to ensure touch targets remain sufficient (minimum 48×48dp) for mobile interactions.  
❌ **Don't:** Apply extreme border radius values that distort button proportions or reduce usable tap areas.

---

## Specific component: On colored bg

This variant ensures a sufficiently high level of accessibility when the component is used on a background that is "out of control".

**To invert color**
• In light mode: For a black finish
• In dark mode: For a white finish

---

## specific_component_on_colored_bg_do_&_dont 👈🤔

✅ **Do:** Use the "On colored bg" variant when placing buttons over images, gradients, or brand-colored backgrounds where contrast cannot be guaranteed.  
❌ **Don't:** Use standard button variants on unpredictable backgrounds where they may fail contrast requirements.

✅ **Do:** Apply inverted colors consistently—black finish in light mode and white finish in dark mode—to ensure WCAG 2.1 AA compliance.  
❌ **Don't:** Mix inverted and non-inverted buttons on the same colored background, creating visual inconsistency.

✅ **Do:** Test button contrast against all possible background variations, including images with varying light and dark areas.  
❌ **Don't:** Assume a single static color variant will work across dynamic or user-generated background content.

✅ **Do:** Consider adding subtle shadows or overlays behind buttons on complex backgrounds to improve legibility.  
❌ **Don't:** Rely solely on color inversion when background complexity requires additional visual separation techniques.

✅ **Do:** Verify that focus states and hover states also maintain sufficient contrast on colored backgrounds.  
❌ **Don't:** Forget to test interactive states, which may reveal contrast issues not visible in the enabled state.

---

# Specs

## States

**`Enabled`** The status of the button before a user has interacted with it, or other content affects it.

**`Hover`** When a user places a pointing device over a button, but has not yet taken action on it.

**`Focus`** When a user selects a button via keyboard or voice command, but has not yet taken action on it.
Mirrors the "Hover" state but includes an additional border.

**`Pressed`** An intermediate state that communicates a user has taken action on a button, and that it is in the process of navigating to a destination, triggering logic, or transmitting data.

**`Loading`** A button is fetching data from another internal or external resource.
Uses the "Loading indicator" component.

**`Disabled`** Used to indicate a button that cannot be selected.

**`Skeleton`** Improves the perceived loading time by providing a visual cue of where button will appear once fully loaded.
Uses the "Skeleton" component, variant "Security marge=False".

---

## Layout and spacing

🚧 Content to be added

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Oct 10, 2025 | 3.2.0 | The specific component "On colored bg" has been split into two distinct components: <ul><li>A public version offering traditional management of dark and light modes <li>A private version (allowing the core team to nest the component with other components) offering customized mode management with four possible configurations: <ul><li>Always in light mode <li>Always in dark mode <li>Light to dark mode <li>Dark to light mode </ul><li>Consequently, for the private version, the name of the "Inverted color" variant has been replaced to "Mode control".</ul> | Maxime Tonnerre |
| Sep 28, 2025 | 3.1.0 | <ul><li>Brand variant: New background and content color tokens added for hover/pressed/loading/focus states <li>The name of the "Hierarchy" variant has been replaced to "Appearance"</ul> | Maxime Tonnerre |
| Jul 24, 2025 | 3.0.0 | <ul><li>New hierarchical variant: Brand → [Component tokens changelog 1.4.0](https://www.figma.com/design/Co2t6wHMf4GB9NJVGs2Hes/-OUDS-Core-Lib--Design-tokens?m=auto&node-id=9280-2568&t=HLVB4jOd35DWr8Bj-1) <li>Rounded corner property is now available → [Component tokens changelog 1.4.0](https://www.figma.com/design/Co2t6wHMf4GB9NJVGs2Hes/-OUDS-Core-Lib--Design-tokens?m=auto&node-id=9280-2568&t=HLVB4jOd35DWr8Bj-1) <li>Minimal variant: Color and width border tokens removed <li>Minimal variant: Color background tokens removed in the enabled state <li>Minimal variant: Color background tokens removed in the loading state <li>Minimal variant: Color background tokens removed in the disabled state</ul> | Maxime Tonnerre |
| Jul 21, 2025 | 2.1.0 | <ul><li>Several design token updates: [Component tokens changelog 1.3.0](https://www.figma.com/design/Co2t6wHMf4GB9NJVGs2Hes/-OUDS-Core-Lib--Design-tokens?m=auto&node-id=9280-2568&t=HLVB4jOd35DWr8Bj-1) <li>Button: Expanded: The chevron is also present in the 'icon only' variant. The gap between these 2 elements is defined by a design token: ouds-action-button-space-column-gap-icon-chevron→ouds-space-column-gap-2xs</ul> | Maxime Tonnerre |
| Apr 19, 2025 | 2.0.0 | <ul><li>Creation of "On colored bg" variant</ul> | Maxime Tonnerre |
| Dec 5, 2024 | 1.0.0 | <ul><li>Component creation</ul> | Maxime Tonnerre |
