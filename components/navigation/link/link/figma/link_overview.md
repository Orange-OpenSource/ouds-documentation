## Definition

A link is a user interface element that allows navigation from one location to another, either within the same page, across different pages of a site (or application), or to an external resource.

Typically rendered as underlined or styled text, a link communicates its interactive nature visually and semantically. It should always lead to a valid destination and be clearly labeled to describe the target or purpose. Unlike a button, which triggers an action, a link's primary function is navigation.

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

## Sizes

**`Default`** This is the default size of the component.
This size is used for the vast majority of applications.

**`Small`** This size can be particularly useful in an information-dense interface or in the construction of a template or component requiring the use of small elements (in an "In-line alert" component, for example).

---

## Specific component: On colored bg

This variant ensures a sufficiently high level of accessibility when the component is used on a background that is "out of control".

**To invert color**
• In light mode: For a black finish
• In dark mode: For a white finish

---

## Expand variant (⛔️ Not supported ⛔️)

**Important! Following the design assessment ritual, the development of this subcomponent is on hold. A joint study with the future "Accordion" component will need to be conducted with the aim of unifying these two components.**

Similar to the "Button" component, a complementary "Expand" subcomponent is proposed.
This subcomponent adopts the layout and interaction states of the "Next" variant (text + chevron) with the following differences:
• Includes an "Active" state parameter for toggling between folded and unfolded states (boolean).
• The chevron icon for the folded state is "chevron down".
• The chevron icon for the unfolded state is "chevron up".

---