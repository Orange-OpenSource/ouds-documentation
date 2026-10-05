# Guideline

## Intro 👈🤖

An alert banner is a full-width message at the top of a page that communicates a global, system-level or service-wide state.

---

## Definition

The Alert banner is a messaging component used to communicate important information, system states, or service updates across an interface. It supports multiple semantic statuses, layouts, actions, and responsive behaviours to ensure consistent communication across products and platforms.

---

## Best for 👈🤔

✅ System-wide issues, such as a lost internet connection or a service outage

✅ Confirming that a global issue is resolved, such as a restored connection

✅ Announcing scheduled maintenance or an upcoming service disruption

✅ Account-level notices that apply across several screens or features

✅ Platform or service updates that do not require immediate action

✅ Persistent messages that must stay visible until the condition is resolved

✅ Promoting a service, an offer or a new feature across the experience

✅ General guidance, such as onboarding tips or account suggestions

✅ Global messages with a single follow-up action, such as View details

✅ Short messages centred below the header on wide desktop screens

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Container | The full-width surface that carries the status colour and sits in the page flow, below the header or navigation | N |
| 2 | Icon | Status icon for functional banners, or a contextual icon for Neutral and Accent banners | Y |
| 3 | Label | The main message, short enough to be understood at a glance | N |
| 4 | Description | Supplementary text that adds detail or guidance below the label (Start layout only) | Y |
| 5 | Action | A single text-only link-style action, placed trailing or at the bottom | Y |
| 6 | Close button | Lets users dismiss the banner when the message can be safely removed (Start layout only) | Y |

---

## Layout

The content layout defines how the banner’s icon, message, and action are positioned within the available screen width.
Choose the layout according to the viewport size and the relationship between the banner and the page grid.

**`Start`** The banner content follows the reference screen grid, with the icon, message, and action aligned to the page margins.
Recommended for mobile, tablet, and small desktop screens, where the available width is limited and the banner should use the space efficiently.
Use this layout when the banner needs to remain visually connected to the surrounding interface and aligned with the rest of the page content.

**`Center`** The banner content is grouped and centred within the available width. Recommended for wide desktop screens, where keeping the message and action in a compact central area improves readability and prevents elements from becoming visually disconnected.

Use this layout for short, focused messages with an optional single action. For longer content, multiple text levels, dismissible banners, or more flexible action positioning, use the Edge-to-edge layout.

The Center layout has a simplified structure:
• It does not support a close button.
• Content alignment is always centred.
• Unlike Edge-to-edge, it does not provide Top and Center alignment options.
• It does not include an Action layout setting. The action can only be shown or hidden.
• It does not support an additional description. Only the main label can be displayed.

⚠️ Layout: For the Center layout, set a suitable maximum content width for each breakpoint. The text and action must never touch or overflow the banner edges.

---

## layout_do_&_dont 👈🤔

✅ **Do:** Use the Start layout on mobile, tablet and small desktop screens, aligned with the page grid  
❌ **Don't:** Use the Center layout on narrow screens where the content cannot stay on one line

✅ **Do:** Use the Center layout for a short message with one optional action on wide desktop screens  
❌ **Don't:** Use the Center layout for a message that needs a description or a close button

✅ **Do:** Set a maximum content width for the Center layout at each breakpoint  
❌ **Don't:** Let the text or the action touch or overflow the banner edges

✅ **Do:** Switch to the Start layout when the content becomes longer or needs more flexible actions  
❌ **Don't:** Reduce the text size or truncate the message to keep the Center layout

✅ **Do:** Keep the same layout for the same banner across the pages of a journey  
❌ **Don't:** Mix Start and Center layouts for similar messages at the same breakpoint

---

## Alignment

**(for Layout=Start only)**

**`Top`** Recommended for mobile layouts or banners with longer content. Aligning the icon and action with the first line improves readability and keeps the interactive elements clearly connected to the beginning of the message.

**`Center`** Recommended for desktop layouts, compact banners, or short single-line messages. Vertically centring the icon, text, and action creates a balanced and compact composition.

---

## alignment_do_&_dont 👈🤔

✅ **Do:** Use Top alignment on mobile and for banners with long or multiline content  
❌ **Don't:** Centre the icon and the action next to a message that spans several lines

✅ **Do:** Use Center alignment for compact banners and short single-line messages on desktop  
❌ **Don't:** Use Top alignment on a single-line banner, where it looks unbalanced

✅ **Do:** Keep the icon and the action aligned with the first line of a multiline message  
❌ **Don't:** Let the close button drift to the vertical middle of a tall banner

✅ **Do:** Apply the same alignment to banners with the same content structure  
❌ **Don't:** Mix alignments between similar banners in the same product

✅ **Do:** Check the alignment again when translated or zoomed text wraps onto more lines  
❌ **Don't:** Assume a message that fits on one line in one language fits in every language

---

## Status

**Non-functional**
Non-functional banners communicate global or cross-screen information without representing a system status, error, confirmation, or warning.

They can appear across several screens to promote a service, highlight a new feature, or provide general guidance. Unlike functional banners, they are not triggered by a technical condition and do not require semantic status colours or icons.

**`Neutral`** Used for general guidance, service information, or contextual messages that apply across the experience without requiring immediate attention.
Neutral banners should remain informative and low priority. Use them for onboarding guidance, account suggestions, or general service notices that are not linked to a system event.

**`Accent`** Used to highlight promotional, featured, or brand-related content across the app or service.
Accent banners are suitable for campaigns, loyalty programmes, feature launches, and engagement messages. Use accent banners for promotional or featured content, not for urgent messages or system issues.

**Functional**
Functional banners behave as system banners. They communicate a global, high-priority state that affects the entire app, service, or user journey rather than a single field, component, or page section.

They usually appear automatically in response to a system condition, without the user triggering them directly. They may persist across screens and should remain visible until the condition is resolved, the information is no longer relevant, or the banner is dismissed when dismissal is permitted.

**`Negative`** Communicates a critical system issue that prevents the service or an essential feature from working correctly.
Use a negative banner for service outages, failed connections, unavailable functionality, or account-wide errors. The message should clearly explain the issue and, when possible, provide a recovery action.

**`Positive`** Confirms that a previously unavailable system, service, or connection is working again.
Use a positive banner when users need clear confirmation that a global issue has been resolved. It should not be used for minor confirmations related to a single action.

**`Info`** Communicates a relevant system-wide update that does not require immediate action.
Use an informational banner for service notices, platform changes, account-level information, or updates that apply across several screens or features.

**`Warning`** Communicates a potential system issue, upcoming disruption, or condition that may affect the service soon.
Use a warning banner when the system is still available but users should be informed or may need to prepare. The message should explain what may happen and when.

---

## status_do_&_dont 👈🤔

✅ **Do:** Match the status to the meaning of the message: Negative, Positive, Info or Warning  
❌ **Don't:** Choose a status for its colour or to draw more attention to the banner

✅ **Do:** Use Negative for critical system issues, such as an outage or a failed connection  
❌ **Don't:** Use a Negative banner for a field error or a problem limited to one page section

✅ **Do:** Use Positive to confirm that a global issue has been resolved  
❌ **Don't:** Use a Positive banner for a minor confirmation related to a single action

✅ **Do:** Use Neutral or Accent for guidance, promotions and featured content  
❌ **Don't:** Use an Accent banner for an urgent message or a system issue

✅ **Do:** Keep functional banners visible until the condition is resolved or no longer relevant  
❌ **Don't:** Show a functional banner without a technical condition that triggers it

---

## Action layout

**(for Layout=Start only)**
Alerts can be displayed with or without an action.
The placement of the action depends on the amount of content and the available screen space.
For action elements, we use the Link component with the “Text only” layout. This approach maintains visual consistency and aligns with our design system guidelines.

🔗 Link style used as a button: In this context, the link style is purely visual, it does not indicate navigation.
• Use <a> elements for navigation.
• Use <button> elements with the link visual style for in-app actions.

⚠️ Non-navigational usage: A link can be used to trigger an action rather than navigation (for example, opening a modal, revealing additional content, or executing a function). This pattern should only be applied when the link appearance is preferred, while ensuring the component remains accessible and its intent is clear.

**`None`** Used when the banner communicates a system state but no user action is required.
Suitable for messages that only inform users about the current state, such as a temporary service limitation or a restored connection.

**`Trailing`** Used when the action is positioned at the end of the message.
Recommended for wide layouts, short messages, and short CTAs that can remain on a single line. This layout keeps the banner compact and makes the action immediately visible.
Avoid the trailing layout when the message or CTA wraps onto several lines, as this may reduce readability and create an unbalanced layout.

**`Bottom`** Used when the action is positioned below the main message. The bottom layout gives the message and action enough room to wrap independently. It improves readability and prevents the CTA from competing with the main content for horizontal space.

**Recommended for:**
• mobile and narrow layouts;
• messages that span multiple lines;
• long or descriptive CTAs;
• translated content that may require more horizontal space.

---

## action_layout_do_&_dont 👈🤔

✅ **Do:** Use None when the banner only informs users about the current state  
❌ **Don't:** Add an action that does not help users understand or resolve the situation

✅ **Do:** Use Trailing for short messages and short actions that stay on a single line  
❌ **Don't:** Keep a trailing action when the message or the action wraps onto several lines

✅ **Do:** Use Bottom on mobile and for multiline messages or long action labels  
❌ **Don't:** Squeeze a long action label next to the message on a narrow screen

✅ **Do:** Use an <a> element for navigation and a <button> with the link style for in-app actions  
❌ **Don't:** Let the visual link style decide which semantic element is used

✅ **Do:** Write an action label that describes the result, such as View maintenance information  
❌ **Don't:** Use a vague label such as OK, Click here or Learn more

---

## Close button

**(for Layout=Start only)**
The close button determines whether users can dismiss the banner.
Use it only when the message can be safely removed after being acknowledged. Functional banners that communicate an active system issue or require user awareness should remain visible until the state changes.

**`False`** The banner does not include a close button and remains visible until the underlying issue is resolved.
Use this option for high-priority system states that users must remain aware of. For example, a No internet connection banner should not be dismissible and should disappear automatically only when connectivity is restored.

**`True`** The banner includes a close button and can be dismissed after the user has read the message.
Use this option for non-critical information that does not require action and can be safely hidden without affecting the user’s understanding of the current system state.

---

## close_button_do_&_dont 👈🤔

✅ **Do:** Add a close button when the message can be safely removed after it has been read  
❌ **Don't:** Let users dismiss a banner that reports an active system issue

✅ **Do:** Keep high-priority banners visible until the underlying condition is resolved  
❌ **Don't:** Hide a No internet connection banner before connectivity is restored

✅ **Do:** Give the close button a clear accessible name, such as Dismiss banner  
❌ **Don't:** Expose a technical icon name such as cross as the accessible name

✅ **Do:** Move focus to a logical element that remains on the page after dismissal  
❌ **Don't:** Let focus return to the top of the document when the banner closes

✅ **Do:** Keep a dismissed banner hidden for the rest of the journey unless its content changes  
❌ **Don't:** Show the same banner again right after the user dismissed it

---

## Icon

**(for Neutral and Accent only)**
Alert messages can include an icon to enhance recognition or remain icon-free when visual simplicity is preferred.
Icons help communicate context and tone but are optional for Non-functional alerts (Neutral and Accent).

**⚠️ Note:**
Functional alerts (Negative, Positive, Info, Warning) must always include a dedicated functional icon that reflects their semantic meaning. This ensures clarity, accessibility, and consistency across all user interfaces.

**`False`** The banner is displayed without an icon.
Use this option when the message is clear on its own or when a simpler visual treatment is preferred.

**`True`** The banner includes a contextual or decorative icon.
Use this option when the icon helps users understand the message more quickly or strengthens the banner’s visual identity.

---

## icon_do_&_dont 👈🤔

✅ **Do:** Always show the dedicated functional icon on Negative, Positive, Info and Warning banners  
❌ **Don't:** Remove or replace the functional icon of a banner that reports a system status

✅ **Do:** Add an icon to a Neutral or Accent banner when it helps users grasp the message faster  
❌ **Don't:** Add an icon to a Neutral or Accent banner only to fill the space

✅ **Do:** Choose an icon that matches the subject of the message  
❌ **Don't:** Use a status icon on a non-functional banner, where it implies a system state

✅ **Do:** Hide decorative icons from assistive technologies  
❌ **Don't:** Let screen readers announce icon names such as heart or gift

✅ **Do:** Repeat the meaning of the icon in the text of the banner  
❌ **Don't:** Rely on the icon alone to communicate the status

---

## Description

**(for Layout=Start only)**
Description is the optional supplementary text in an Alert Banner. Use only when additional detail or guidance is needed beyond the label. It should remain short, clear and scannable, helping the user understand what happened and what they can do next.

• If you can express the message fully in the label, omit body text.
• When body text is included, limit it to one or two short sentences. This aligns with practices from major design systems: for example, the Red Hat design system recommends 1-2 sentences for the message body. Red Hat design system
• Avoid long text blocks or “long-reads” within alerts — for detailed explanations, direct users to another view or modal. The ServiceNow “Horizon” system states that an alert message shows two lines by default, and if it exceeds two lines, provide a “Show More” link. Horizon Design System
• Use plain language consistent with Orange’s tone: friendly, clear, service-oriented. Avoid jargon or complex sentences. The US Web Design System emphasises “concise, human-readable language; avoid jargon and computer code.” U.S. Web Design System (USWDS)
• Provide next-step guidance if the alert requires user action: e.g., “Try again”, “Check your settings”, “Contact support”. If no action is required, the body text can simply explain the state.

**`False`** The banner displays the label only.
Use this option for short, self-explanatory messages that do not require additional context.

**`True`** The banner displays a label and a short description.
Use this option when users need more context about the issue, its impact, or the next step.

---

## description_do_&_dont 👈🤔

✅ **Do:** Add a description only when users need more context about the issue, its impact or the next step  
❌ **Don't:** Repeat the label in the description

✅ **Do:** Keep the description to one or two short sentences  
❌ **Don't:** Write long explanations inside the banner

✅ **Do:** Send users to another page, view or modal when a detailed explanation is needed  
❌ **Don't:** Stack several paragraphs or lists in a banner

✅ **Do:** Tell users what they can do next when the banner requires an action  
❌ **Don't:** Describe a problem without any guidance when a recovery step exists

✅ **Do:** Use plain, friendly and service-oriented language  
❌ **Don't:** Use jargon, error codes or technical terms users do not know

---

## Placement and Interaction

**Mobile reference design**
• Placement: Directly below the top app bar or page header and above the related page content.
• Width: Full available screen width.
• Layout: Use the Start layout to keep the icon, message and optional action aligned with the screen margins.
• Behaviour: The banner is part of the page layout and pushes the content down. It scrolls with the page and must not cover navigation or interactive elements.
• Use the Bottom action layout when the message or action requires multiple lines.

**Tablet reference design**
• Placement: Directly below the main navigation or page header.
• Width: Full available viewport or parent-container width.
• Layout: Use the Start layout by default. Align the inner content with the tablet grid.
• Behaviour: The banner pushes the page content down and scrolls with the page. It is not fixed or sticky by default.
• Use the Center layout only for short, focused messages that fit comfortably on one line.

**Desktop reference design**
• Placement: Directly below the global header or primary navigation and above the main page content.
• Width: The banner background spans the full viewport or product-container width.
• Layout: The Center layout is recommended for web when the banner contains a short message and an optional single action.
• Behaviour: The banner remains part of the document flow, pushes content down and scrolls with the page.
• Use the Start layout for longer messages, descriptions, close buttons or more complex actions.

**Desktop Large reference design**
• Placement: Directly below the global header or navigation.
• Layout: Use the Center layout for short global messages. Keep the inner content centred and constrained by a maximum text width.
• Behaviour: The banner scrolls with the page and must not remain fixed over the content by default.

Two width behaviours are supported:

**Edge to edge**
• The banner background spans the full viewport width.
• The inner content remains aligned with the page grid and uses a maximum text width. It must not stretch across the entire screen.

**Maximum width**
• The complete banner has a maximum width of 1920 px and remains centred in the viewport.
• When the viewport is wider than 1920 px, equal margins appear on both sides. The banner must not continue expanding beyond this width.
• Use this behaviour when the rest of the product already follows a centred (header content), maximum-width layout.

---

## placement_and_interaction_do_&_dont 👈🤔

✅ **Do:** Place the banner directly below the header or main navigation, above the page content  
❌ **Don't:** Place the banner in the middle of the page or inside a single section

✅ **Do:** Keep the banner in the page flow so that it pushes the content down  
❌ **Don't:** Overlay the banner on navigation, content or interactive elements

✅ **Do:** Let the banner scroll with the page by default  
❌ **Don't:** Fix the banner over the content without a clear need

✅ **Do:** Keep the inner content aligned with the page grid and within a maximum text width  
❌ **Don't:** Stretch the text across the whole width of a very wide screen

✅ **Do:** Use the maximum-width behaviour when the rest of the product follows a centred layout  
❌ **Don't:** Let the banner keep expanding beyond 1920 px in a product with a maximum width

---

## Multiline and responsiveness

**Multiline**
This component allows multi-line text editing. The number of lines is not limited.

**Max-width vs full-width**
For greater flexibility, this component doesn’t have a default max-width. The max-width is applied to the text within the component.
As a result, if it is positioned across the full available width (of the screen or the container), the component’s background will stretch across the entire available surface, but the text may be limited to its max-width if the display width is larger.

**User zoom in/out**
The behavior of the text during user zoom in/out must follow a fundamental principle: the text must remain readable, accessible, and must never break the structure or lose information.
• The text must always scale proportionally with user zoom. Text resizing must never be blocked.
• Zooming must never cause text to be truncated or hidden. The component must expand vertically to allow line wrapping.
• The component’s height and width must be flexible, never fixed, in order to automatically adapt its dimensions according to the level of zoom.
• In order to preserve the minimum interactive area during user zoom out, this component have a min-width of 160px and a min-height of 48px.
• If the component doesn’t contain any interactive elements, it’s not necessary to maintain the minimum interactive area during user zooms out.
• Even if, the component has a max-height or a max-width for resizing control purposes, technically, during user zoom in, these limitations are not fixed but must be scalable in order to adapt to the user’s zoom level.
• Icons must always scale proportionally with user zoom. Icon resizing must never be blocked.
• The behaviors of the other subcomponents during user zoom are available in the corresponding documentation.

---

## multiline_and_responsiveness_do_&_dont 👈🤔

✅ **Do:** Let the banner grow in height so the text can wrap onto several lines  
❌ **Don't:** Truncate the message or fix the height of the banner

✅ **Do:** Apply the max-width to the text while the background fills the available width  
❌ **Don't:** Stretch a line of text across the full width of a large screen

✅ **Do:** Let text and icons scale proportionally with user zoom  
❌ **Don't:** Block text resizing or keep icons at a fixed size

✅ **Do:** Keep the minimum interactive area when the banner contains an action or a close button  
❌ **Don't:** Let the action or the close button shrink below the minimum area at zoom out

✅ **Do:** Check the banner at 200% zoom and at a 320 px wide viewport  
❌ **Don't:** Assume a layout that works at the default size works at every zoom level

---

## Rich text

Rich text should be used sparingly to improve scanning and highlight the most important part of the message. It must never compensate for unclear writing.

**Layout=Start**

**Strong text**
• Strong text can be used sparingly in the label or description to highlight key information, such as a status, date, amount, or required step. Rich text must use the **Label/Medium/Strong** token only.
• No other text styles or custom font weights should be used.

**Underlined text** and **hyperlink**
• Underlined text must not be used for emphasis, as it is commonly associated with links.
• If a **hyperlink** is needed within the content, the typographic reference **Label/Medium/Underline** must be used.
• A separate Action can also be added outside the description when a more prominent or independent next step is needed.

**Layout=Center**

**Strong text**
• Strong text can be used sparingly in the label or description to highlight key information, such as a status, date, amount, or required step. Rich text must use the **Label/Large/Strong** token only.
• No other text styles or custom font weights should be used.

**Underlined text** and **hyperlink**
• Underlined text must not be used for emphasis, as it is commonly associated with links.
• If a **hyperlink** is needed within the content, the typographic reference **Label/Large/Underline** must be used.
• Use this action for an additional interaction, such as Close, View details, or Manage plan.

---

## rich_text_do_&_dont 👈🤔

✅ **Do:** Use strong text sparingly to highlight one key piece of information, such as a date or an amount  
❌ **Don't:** Bold several fragments or the whole message

✅ **Do:** Use the Label/Medium/Strong token in the Start layout and Label/Large/Strong in the Center layout  
❌ **Don't:** Apply other text styles or custom font weights

✅ **Do:** Underline only real hyperlinks, with the dedicated underline typographic reference  
❌ **Don't:** Underline text for emphasis

✅ **Do:** Add a separate action when a more prominent or independent next step is needed  
❌ **Don't:** Give an inline link and the separate action the same destination

✅ **Do:** Write a clear message first, then decide whether rich text helps scanning  
❌ **Don't:** Use rich text to compensate for unclear writing

---

# Specs

## States

🚧 Missing from source: States section in alert_banner_overview.md

---

## Layout and spacing

🚧 Content to be added

---

# Accessibility

## Accessibility

**Usage without vision**

The banner content, status and available actions are programmatically available to assistive technologies.
The accessible reading order should follow the logical content order:
Label → Description → Inline link → Action → Close button
Visual variants such as Top, Center, Trailing or Bottom must not change this programmatic order.
WCAG 2.1 — 1.3.1 Info and Relationships, Level A
WCAG 2.1 — 1.3.2 Meaningful Sequence, Level A

Functional banners that appear or update dynamically are announced without moving keyboard or screen reader focus to the banner. Use a polite announcement for routine information, positive confirmations and non-urgent warnings. Reserve assertive announcements for urgent failures that require immediate attention.
A Negative visual status does not automatically require an assertive announcement. Announcement priority depends on urgency, not colour.
WCAG 2.1 — 4.1.3 Status Messages, Level AA

Non-functional Neutral and Accent banners should not use a live region by default.
Promotional or contextual content should normally remain part of the page’s reading order. Announce it dynamically only when its appearance communicates a meaningful new change.
Design guidance supporting WCAG 2.1 — 4.1.3 Status Messages, Level AA

A persistent global banner should not be announced again on every page or screen transition when its content has not changed. Repeated announcements can interrupt navigation and create unnecessary screen reader noise. Announce the banner when it first appears or when its meaning changes.
Design guidance supporting WCAG 2.1 — 4.1.3 Status Messages, Level AA

The label and optional description are programmatically associated.
In the Edge-to-edge layout, assistive technologies should read the label followed by the description. In the Center layout, the complete message is provided by the label because this variant does not support a description.
WCAG 2.1 — 1.3.1 Info and Relationships, Level A

Functional icons are visually required for Negative, Positive, Info and Warning, but must not provide the only accessible indication of status.
When the status is already expressed in text, hide the icon from assistive technologies to avoid duplicate announcements. If an icon communicates unique information, provide an accessible text alternative and repeat the same meaning in the banner content.
WCAG 2.1 — 1.1.1 Non-text Content, Level A

Optional icons used in Neutral and Accent banners should be hidden from assistive technologies when they are decorative. Do not announce icon names such as “heart”, “gift” or “warning triangle” when they do not add information beyond the text.
WCAG 2.1 — 1.1.1 Non-text Content, Level A

Every interactive element exposes an accessible name, role and state.
The accessible name of an action or close button should include its visible label. Do not expose technical icon names such as “cross”, “chevron” or “link icon”.
WCAG 2.1 — 4.1.2 Name, Role, Value, Level A
WCAG 2.1 — 2.5.3 Label in Name, Level A

Use the correct semantic element for the action:
Use an <a> element when the action navigates to another destination.
Use a <button> element when the action performs an in-page or in-app operation.
The visual link style must not determine the semantic element.
WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

The close icon button has a clear accessible name, such as “Dismiss banner” or “Close notification”.
When additional context is useful, include the subject of the banner, for example “Dismiss 5G availability message”.
WCAG 2.1 — 2.4.6 Headings and Labels, Level AA
WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

When a focused close button removes the banner, focus moves to a logical element that remains on the page.
Do not allow focus to return unexpectedly to the beginning of the document or disappear into the page body.
WCAG 2.1 — 2.4.3 Focus Order, Level A

In the Loading state, the loading status is available as text and is not communicated by animation alone.
The loading indicator may be hidden from assistive technologies when the message already communicates the operation, for example “Activating your eSIM…”.
When loading completes, announce the meaningful result once. Do not repeatedly announce spinner updates or decorative progress changes.
WCAG 2.1 — 1.1.1 Non-text Content, Level A
WCAG 2.1 — 4.1.3 Status Messages, Level AA

If an action becomes unavailable during loading, its disabled or busy state is programmatically exposed.
Prevent repeated activation without unexpectedly moving focus away from the action.
WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

**Usage with limited vision**

Text has a minimum contrast ratio of 4.5:1, or 3:1 for large text.
This applies to the label, description, inline hyperlink and separate action across all statuses and themes.
WCAG 2.1 — 1.4.3 Contrast (Minimum), Level AA

Functional icons, the close button, focus indicators and other essential graphical controls have a minimum contrast ratio of 3:1 against adjacent colours.
WCAG 2.1 — 1.4.11 Non-text Contrast, Level AA

Keyboard focus remains clearly visible against both the banner background and the surrounding page.
Focus must remain distinguishable for all functional statuses, including high-contrast backgrounds such as Negative, Positive and Warning.
WCAG 2.1 — 2.4.7 Focus Visible, Level AA

Text can be resized to 200% without clipping, overlapping, hiding information or removing functionality.
Actions and the close button must remain available after text enlargement.
WCAG 2.1 — 1.4.4 Resize Text, Level AA

The banner reflows at a viewport width equivalent to 320 CSS px without horizontal scrolling or loss of content.
WCAG 2.1 — 1.4.10 Reflow, Level AA

Increased line height, paragraph spacing, letter spacing and word spacing do not clip or hide the label, description, link or action.
WCAG 2.1 — 1.4.12 Text Spacing, Level AA

The Center layout is used only when the label and optional action fit within the defined maximum content width.
Text and action must not touch or overflow the banner edges. When space becomes insufficient, use the Edge-to-edge layout rather than reducing text size or clipping content.
Design guidance supporting WCAG 2.1 — 1.4.10 Reflow, Level AA

The Edge-to-edge layout is recommended for mobile, tablet and narrow desktop screens.
The icon, text, action and close button should align with the reference screen grid and wrap without changing their logical reading order.
Design guidance supporting WCAG 2.1 — 1.3.2 Meaningful Sequence, Level A
WCAG 2.1 — 1.4.10 Reflow, Level AA

Use Top alignment when the message spans several lines.
Aligning the icon and action with the first line keeps the beginning of the message easier to identify at high zoom and on narrow screens.
Use Center alignment for short labels and compact desktop banners.
Design guidance supporting WCAG 2.1 — 1.4.10 Reflow, Level AA

Use the Bottom action layout for mobile screens, multi-line messages and long CTA labels.
The message and action must wrap independently without overlapping or forcing the action outside the visible banner area.
Design guidance supporting WCAG 2.1 — 1.4.10 Reflow, Level AA

The component supports both portrait and landscape orientation unless a specific orientation is essential to the service.
WCAG 2.1 — 1.3.4 Orientation, Level AA

Information remains visible in browser high-contrast or forced-colour modes.
Do not rely on background colour alone to preserve the banner boundary, status or visibility of controls.
Design guidance supporting WCAG 2.1 — 1.4.3 Contrast (Minimum), Level AA
WCAG 2.1 — 1.4.11 Non-text Contrast, Level AA

**Usage without perception of colour**

Colour is not used as the only way to communicate the banner status.
Functional Negative, Positive, Info and Warning banners combine: semantic colour, a dedicated functional icon, explicit text describing the status or its effect.
WCAG 2.1 — 1.4.1 Use of Color, Level A

Do not rely only on red, green, blue or yellow to communicate the result.
For example, use “Internet connection restored” rather than showing only a green banner with a check icon.
WCAG 2.1 — 1.4.1 Use of Color, Level A

Neutral and Accent banners remain understandable when their background colours cannot be distinguished.
The text itself must communicate whether the banner contains general guidance, promotional content or a featured offer.
WCAG 2.1 — 1.4.1 Use of Color, Level A

Links remain identifiable without relying only on colour.
Inline hyperlinks use the dedicated underline style. Underlining must not be applied to non-interactive text.
WCAG 2.1 — 1.4.1 Use of Color, Level A

Focus, hover, disabled and loading states are not communicated by colour alone.
Use a visible focus indicator, explicit loading text and programmatically exposed states.
WCAG 2.1 — 1.4.1 Use of Color, Level A
WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

The Loading state includes a meaningful text update.
A rotating spinner or changing colour cannot be the only indication that an operation is in progress.
WCAG 2.1 — 1.4.1 Use of Color, Level A
WCAG 2.1 — 4.1.3 Status Messages, Level AA

**Usage with limited manipulation or strength**

The action and close button can be operated using a keyboard.
Use standard activation keys and do not require pointer gestures, dragging, swiping or precise movement.
WCAG 2.1 — 2.1.1 Keyboard, Level A

Keyboard focus cannot become trapped inside the banner.
Users can move to and from the banner controls using the standard keyboard navigation mechanism.
WCAG 2.1 — 2.1.2 No Keyboard Trap, Level A

Interactive elements follow a logical focus order that matches the reading order.
Recommended order: Inline link → Separate action → Close button
Visual placement such as Trailing, Bottom, Top or Center must not reorder keyboard focus.
WCAG 2.1 — 2.4.3 Focus Order, Level A

Every keyboard-operable element has a visible focus indicator.
WCAG 2.1 — 2.4.7 Focus Visible, Level AA

Pointer actions complete on the up-event whenever possible, allowing users to cancel an accidental press before activation.
WCAG 2.1 — 2.5.2 Pointer Cancellation, Level A

The full visible action and close-button area is interactive.
Do not limit activation to a small icon path, a few letters of an underlined label or another visually hidden hit area.
Design guidance supporting WCAG 2.1 — 2.1.1 Keyboard, Level A

Provide a target size of at least 44 × 44 CSS px for the close button and separate action where possible.
WCAG 2.1 — 2.5.5 Target Size, Level AAA

Do not make the whole banner interactive when it also contains an independent action, inline link or close button.
Nested or overlapping interactive areas create ambiguous pointer and keyboard behaviour.
Design guidance supporting WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

The action remains stable while it is focused.
When loading starts, do not replace the focused action with a different control without preserving focus logically. Prevent duplicate submissions and expose the busy or disabled state programmatically.
WCAG 2.1 — 2.4.3 Focus Order, Level A
WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

A dismissible banner remains visible long enough for users to locate and operate the close button or action.
Alert banners should not disappear automatically. They should remain until the underlying state is resolved or the user explicitly dismisses them when dismissal is permitted.
WCAG 2.1 — 2.2.1 Timing Adjustable, Level A

High-priority functional banners are not dismissible when removing them would hide an unresolved condition.
For example, “No internet connection” remains visible and disappears automatically only when connectivity is restored.
Design guidance supporting cognitive and motor accessibility
When dismissal is allowed, the close action does not require simultaneous input, complex gestures or sustained pressure.
Design guidance supporting EN 301 549 — Usage with limited manipulation or strength

**Usage with limited cognition, language or learning**

The message uses short, direct and familiar language.
Avoid technical codes, unexplained abbreviations, vague system terminology and unnecessarily complex sentences.
Design guidance supporting cognitive accessibility

Each banner communicates one primary message.
Do not combine unrelated service updates, promotions and errors inside the same banner.
Design guidance supporting cognitive accessibility

Use a specific action label that describes the result of activation.
Prefer “Manage your plan”, “Retry connection” or “View affected services” over “OK”, “Click here” or “Learn more”.
WCAG 2.1 — 2.4.4 Link Purpose (In Context), Level A
WCAG 2.1 — 2.4.6 Headings and Labels, Level AA

Keep the description to one or two short sentences.
If detailed explanation is required, use the action or inline link to open another page, view or modal.
Design guidance supporting cognitive accessibility

The Center layout uses a short, self-contained label.
Because it does not support a description, do not use Center for messages that require detailed explanation, multiple steps or several links.
Design guidance supporting cognitive accessibility

Use rich text sparingly.
Highlight only one essential value or phrase with strong text whenever possible. Underline only interactive hyperlinks. Avoid combining several bold fragments, links and actions that compete for attention.
Design guidance supporting WCAG 2.1 — 1.3.1 Info and Relationships, Level A

In Edge-to-edge, rich text is used in the description.
A separate action may also be provided. When an inline link and a separate action are both present, they should serve different purposes and should not duplicate the same destination.
Design guidance supporting cognitive accessibility

In Center, rich text is used in the label.
Use the dedicated Action option for the additional interaction. Do not simulate an inline link inside the Center label.
Design guidance supporting cognitive accessibility

Errors are identified in text and include a recovery suggestion whenever one is available.
For example: “SIM activation failed. Check your network connection and try again.”
WCAG 2.1 — 3.3.1 Error Identification, Level A
WCAG 2.1 — 3.3.3 Error Suggestion, Level AA

Loading messages describe the operation in progress.
Prefer “Activating your eSIM…” over “Loading…” or a spinner without context.
When the operation completes, replace the loading message with a clear success or failure result.
WCAG 2.1 — 4.1.3 Status Messages, Level AA

Important or actionable banners remain visible until the user has had enough time to understand and respond.
Do not automatically dismiss errors, warnings, account restrictions or messages containing required actions.
WCAG 2.1 — 2.2.1 Timing Adjustable, Level A

Optional informational or promotional banners may include a close button.
When dismissed, they should not immediately reappear during the same journey unless the information has materially changed.
Design guidance supporting cognitive accessibility

Do not display several global banners at the same time unless each one is essential.
Prioritise messages and avoid overwhelming users with competing system states.
Design guidance supporting cognitive accessibility

Focusing or activating a banner control does not trigger an unexpected context change.
WCAG 2.1 — 3.2.1 On Focus, Level A
WCAG 2.1 — 3.2.2 On Input, Level A

**Usage without hearing and limited hearing**

The complete banner message is available visually and does not depend on sound.
Status, failure, warning, loading and completion information must remain understandable with audio disabled.
Design guidance supporting non-auditory access

Sound is never the only way to communicate connectivity loss, successful activation, a service interruption or another system state. Use visible text and the appropriate icon in addition to any optional sound or vibration.
Design guidance supporting non-auditory access

If an audio notification accompanies the banner, it communicates the same result as the visible message.
The audio must not introduce essential information that is missing from the label or description.
Design guidance supporting non-auditory access

**Minimize photosensitive seizure triggers**

Entrance and exit animations remain short and non-essential.
Avoid repeated bouncing, shaking, zooming or flashing transitions when the banner appears, updates or disappears.
Design guidance supporting motion accessibility

Respect the platform’s reduced-motion preference.
Replace movement with an immediate or simplified transition when reduced motion is enabled.
Design guidance supporting reduced-motion user preferences

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Aug 10, 2026 | 1.0.0 | **Version 2.7 of the design tokens is required for the development of this update.**<ul><li>Component creation</ul> | Anton Astafev |
