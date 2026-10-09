# Guideline

## Intro 👈🤖

A link is an interactive navigation element that directs users to another location within or outside the application.

---

## Definition

A link is a user interface element that allows navigation from one location to another, either within the same page, across different pages of a site (or application), or to an external resource.

Typically rendered as underlined or styled text, a link communicates its interactive nature visually and semantically. It should always lead to a valid destination and be clearly labeled to describe the target or purpose. Unlike a button, which triggers an action, a link's primary function is navigation.

---

## Best for 👈🤔

✅ In-page navigation to specific sections or anchors

✅ External navigation to related resources or documentation

✅ Breadcrumb trails showing hierarchical page structure

✅ Table of contents linking to document sections

✅ Footer navigation to legal pages, privacy policies, or site maps

✅ Inline references within body text requiring contextual navigation

✅ "Back" or "Next" sequential navigation patterns

✅ Search results listings with clickable titles

✅ Related content recommendations and cross-references

✅ Help documentation with contextual links to detailed topics

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Label text | Communicates the link destination or action to users | N |
| 2 | Chevron icon (Next/Back) | Indicates directional navigation context | Y |
| 3 | Custom icon (Text + icon) | Provides additional visual context for the link purpose | Y |
| 4 | Underline | Signals interactivity, especially for inline text links | Y |
| 5 | Focus ring | Indicates keyboard focus state for accessibility | N |
| 6 | Container | Defines the clickable touch/click target area | N |

---

## Layouts

**`Next`** Used in a standard navigation context. Positioned after the label, it features a "chevron right" icon, which is not customizable.

**`Back`** Used for "backward" navigation. Positioned before the label, it features a "chevron left" icon, which is not customizable.

**`Text only`** Can be used for navigation or actions within the same page. Whether placed in a text paragraph or as a standalone component, the interaction states remain consistent.

**`Text + icon`** This option includes functionality to choose any Solaris icon.
Used for navigation or actions within the same page.
• When embedded in a text paragraph, its interaction states are the same as the "Text Only" variant.
• When used as a standalone component (e.g., like the "Next" variant), it adopts the same interaction states as the "Next" and "Back" variants.
• Typically utilized in business or back-office interfaces, it is rarely standalone (usually part of a group of elements).

**`Visited`** Indicates to the user that the target URL has already been opened on the device.
• Take care, the visited variant is reserved for text links only and even more so in a specific context, such as: search results with suggested redirect links.

---

## layouts_do_&_dont 👈🤔

✅ **Do:** Use the "Next" layout for forward navigation in sequential flows like wizards or multi-step processes  
❌ **Don't:** Use chevron layouts for inline text links embedded within paragraphs

✅ **Do:** Reserve the "Visited" layout for contexts where tracking navigation history adds value, such as search results  
❌ **Don't:** Apply visited styles universally as they can create visual clutter and confusion

✅ **Do:** Match the "Text + icon" layout with icons that reinforce the link's destination or purpose  
❌ **Don't:** Use decorative icons that don't provide meaningful context about the link destination

✅ **Do:** Use "Text only" layout for inline links within body copy to maintain reading flow  
❌ **Don't:** Pair inline text links with icons as this disrupts the reading experience

✅ **Do:** Use "Back" layout consistently for returning to previous pages or steps in a flow  
❌ **Don't:** Mix "Back" and "Next" layouts inconsistently within the same navigation context

---

## Sizes

**`Default`** This is the default size of the component.
This size is used for the vast majority of applications.

**`Small`** This size can be particularly useful in an information-dense interface or in the construction of a template or component requiring the use of small elements (in an "In-line alert" component, for example).

---

## sizes_do_&_dont 👈🤔

✅ **Do:** Match inline link size to the surrounding body text size for visual consistency  
❌ **Don't:** Use mismatched link sizes that create jarring visual hierarchies within text blocks

✅ **Do:** Use the small size variant in dense interfaces like data tables, sidebars, or compact cards  
❌ **Don't:** Use small links as primary navigation elements where visibility is critical

✅ **Do:** Ensure small links maintain the minimum touch target size of 44×44px for mobile accessibility  
❌ **Don't:** Reduce link size below readable thresholds even in dense layouts

✅ **Do:** Use default size for standalone links that serve as primary navigation or calls-to-action  
❌ **Don't:** Mix multiple link sizes within the same navigation group or list

✅ **Do:** Consider the overall information density when selecting link size  
❌ **Don't:** Default to small size simply to fit more content on screen

---

## Specific component: On colored bg

This variant ensures a sufficiently high level of accessibility when the component is used on a background that is "out of control".

**To invert color**
• In light mode: For a black finish
• In dark mode: For a white finish

---

## specific_component:_on_colored_bg_do_&_dont 👈🤔

✅ **Do:** Use the "On colored bg" variant when placing links on brand colors, images, or gradients  
❌ **Don't:** Use standard link colors on colored backgrounds without checking contrast ratios

✅ **Do:** Test link visibility across all theme modes (light/dark) when using inverted color options  
❌ **Don't:** Assume one color configuration works for both light and dark modes

✅ **Do:** Ensure the inverted link color maintains a minimum 4.5:1 contrast ratio against the background  
❌ **Don't:** Use colored backgrounds that reduce link visibility below accessibility standards

✅ **Do:** Apply the "On colored bg" variant consistently across all link states (hover, focus, pressed)  
❌ **Don't:** Mix standard and inverted link variants on the same colored surface

✅ **Do:** Use black finish in light mode and white finish in dark mode for optimal readability  
❌ **Don't:** Invert colors arbitrarily without considering the overall visual hierarchy

---

## Expand variant (⛔️ Not supported ⛔️)

**Important! Following the design assessment ritual, the development of this subcomponent is on hold. A joint study with the future "Accordion" component will need to be conducted with the aim of unifying these two components.**

Similar to the "Button" component, a complementary "Expand" subcomponent is proposed.
This subcomponent adopts the layout and interaction states of the "Next" variant (text + chevron) with the following differences:
• Includes an "Active" state parameter for toggling between folded and unfolded states (boolean).
• The chevron icon for the folded state is "chevron down".
• The chevron icon for the unfolded state is "chevron up".

---

## expand_variant_do_&_dont 👈🤔

✅ **Do:** Wait for the unified Accordion component study before implementing expand functionality  
❌ **Don't:** Create custom expand link implementations that may conflict with future Accordion patterns

✅ **Do:** Use existing disclosure patterns like Accordion or Collapsible for expand/collapse functionality  
❌ **Don't:** Attempt to recreate expand behavior using the current Link component

✅ **Do:** Document any interim expand solutions with clear migration paths to future components  
❌ **Don't:** Ship expand link variations that lack proper ARIA attributes for accessibility

✅ **Do:** Consider using Button component for toggle actions until Expand variant is supported  
❌ **Don't:** Blur the distinction between navigation links and stateful toggle controls

✅ **Do:** Provide feedback to the design system team about expand/collapse use cases  
❌ **Don't:** Assume the current limitation will prevent all disclosure pattern implementations

---

# Specs

## States

**`Enabled`** The status of the link before a user has interacted with it, or other content affects it.
Depending on the layout, the underline may or may not appear in this state.
In cases without an underline, the orange chevron icon or a Solaris icon signals interactivity.

**`Hover`** When a user places a pointing device over a link, but has not yet taken action on it.
The underline appears, with UI codes consistent across all components.

**`Pressed`** An intermediate state that communicates a user has taken action on a link, and that it is in the process of navigating to a destination, triggering logic, or transmitting data.
The underline appears, with UI codes consistent across all components.

**`Disabled`** Used to indicate a link that cannot be selected.
Depending on the layout, the underline may or may not appear in this state.

**`Focus`** When a user selects a link via keyboard or voice command, but has not yet taken action on it.
Mirrors the "Hover" state but includes an additional border.

**`Skeleton`** Improves the perceived loading time by providing a visual cue of where link will appear once fully loaded.
Uses the "Skeleton" component, variant "Security marge=False".

---

## Layout and spacing

🚧 Content to be added

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Oct 10, 2025 | 2.2.0 | The specific component "On colored bg" has been split into two distinct components: • A public version offering traditional management of dark and light modes • A private version (allowing the core team to nest the component with other components) offering customized mode management with four possible configurations: • Always in light mode • Always in dark mode • Light to dark mode • Dark to light mode • Consequently, for the private version, the name of the "Inverted color" variant has been replaced to "Mode control". | Maxime Tonnerre |
| Jul 21, 2025 | 2.1.0 | • Several design token updates: [Component tokens changelog 1.3.0](https://www.figma.com/design/Co2t6wHMf4GB9NJVGs2Hes/-OUDS-Core-Lib--Design-tokens?m=auto&node-id=9280-2568&t=HLVB4jOd35DWr8Bj-1) | Maxime Tonnerre |
| Apr 19, 2025 | 2.0.0 | • Creation of "On colored bg" variant | Maxime Tonnerre |
| Dec 3, 2024 | 1.0.0 | • Component creation | Maxime Tonnerre |
