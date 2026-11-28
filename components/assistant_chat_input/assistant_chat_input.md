---
id: assistant-chat-input
category: Control
family: Chat input
---

# Assistant chat input

An assistant chat input is a UI element designed for interacting with AI assistants through a conversational interface.

# Guideline

<img src="images/hero_image_assistant_chat_input.png" alt="hero_image_assistant_chat_input" width="864">

## Anatomy

<img src="images/assistant_chat_input@anatomy_img.png" alt="assistant_chat_input@anatomy_img" width="864">

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Container | The whole component: it holds the notice, the input, its bottom actions and its supporting text. | No |
| 2 | Legal text container | Holds the AI legal notice above the input. | Yes |
| 3 | Legal text | Editable notice with relevant information about the assistant. | Yes |
| 4 | Chat input container | Surface of the input: it groups the text area and the bottom actions and carries the state styling. | No |
| 5 | Slot | Holds custom content inside the input. | Yes |
| 6 | Text input container | Holds the label and the entered text or placeholder. | No |
| 7 | Label text | Indicates the function of the input. It can be hidden in compact layouts. | Yes |
| 8 | Bottom actions | Holds the leading and trailing actions, including the send action. | No |
| 9 | Divider | The visible divider of the chat input surface. | No |
| 10 | Helper text container | Holds the supporting text below the input. | Yes |
| 11 | Helper text | Gives additional information about the input, such as the remaining characters. | Yes |
| 12 | Helper link | Links to additional help when the helper text is not sufficient. | Yes |

## Definition

An assistant chat input is a UI element designed for interacting with AI assistants through a conversational interface.

The assistant chat input combines a dedicated text entry area with multiple contextual actions, such as voice input, audio recording, and additional options, allowing users to interact with the AI through multiple input methods and functionalities.

## Outlined

<!-- zh-row -->

**`False`** An input with a subtle background fill and un visible bottom border, creating a softer and more contained look. Best suited for dense layouts or to enhance visibility.

**`True`** A minimalist input with a transparent background and a visible stroke outlining the field.  
This style may be interesting for contexts other than form pages:  
  • When inputs need to feel lightweight and unobtrusive  
  • In a header (search field)  
  • In a selection/filtering feature in a product catalog

<img src="images/assistant_chat_input@outlined_img.png" alt="assistant_chat_input@outlined_img" width="433">

## Rounded corner

<!-- zh-row -->

Even though in Figma this rendering option is available and editable from the properties of each input component, the configuration of this rendering option is actually transversal across the entire product/service in which the component is used.  
It is therefore impossible to have one input component set to Rounded corner=True and another set to Rounded corner=False within the same product/service.

**`False`** The square rendering corresponds to Orange's historical style. It conveys the brand's sense of seriousness, robustness and utility-driven. It remains the default style for our digital interface components.

**`True`** The rounded rendering offers flexibility without sacrificing the attribution to the brand. It helps anchoring the service in a reality where the visual codes of the mobile area tends to rub off on all interfaces. Use rounded corners for a softer, more approachable, friendly and tactile feel.

This option is technically not available for all brand themes  
Here’s the list of rounded corners availability by brand theme

| Brand theme | Status |
|---|---|
| Orange | ✅ Available |
| Orange Compact | ✅ Available |
| Sosh | ❌ Unavailable |
| Wireframe | ❌ Unavailable |

<img src="images/assistant_chat_input@rounded_corner_img.png" alt="assistant_chat_input@rounded_corner_img" width="433">

## Input status

<!-- zh-row -->

**`Empty`** The Empty state indicates that the text area is blank with no content or placeholder, a neutral starting point.

<img src="images/assistant_chat_input@input_status_empty_img.png" alt="assistant_chat_input@input_status_empty_img" width="433">

<!-- zh-row -->

**`Empty (Placeholder)`** The Empty with Placeholder state provides a hint or guidance inside the field to suggest expected input.

<img src="images/assistant_chat_input@input_status_empty_placeholder_img.png" alt="assistant_chat_input@input_status_empty_placeholder_img" width="433">

<!-- zh-row -->

**`Filled`** The Filled state shows that the user has entered valid content into the field, replacing any placeholder.

<img src="images/assistant_chat_input@input_status_filled_img.png" alt="assistant_chat_input@input_status_filled_img" width="433">

## Error

<!-- zh-row -->

The Error status indicates that the user input does not meet validation rules, for example, in this specific case, if the number of characters entered by the user exceeds the allowed limit. It provides immediate visual feedback, typically through a red border, error icon, and a clear, accessible error message positioned below the input (mandatory).

This state helps users quickly identify and correct mistakes by explaining what went wrong and, when possible, how to fix it.  
The input remains editable, encouraging users to revise their input without starting over.

&nbsp;

### ⚠️ Error message vs helper text / link
If a helper text accompanies the text input, it is replaced by the error message. However, a helper link must not be replaced and should remain positioned below the error message.

<img src="images/assistant_chat_input@error_img.png" alt="assistant_chat_input@error_img" width="433">

## AI legal notice

<!-- zh-row -->

**`True`** Displays an editable notice above the input. Use it to communicate relevant information about the assistant.

**`False`** Hides the notice and removes its space above the input.

Keep the copy concise: the supplied notice is a single-line, truncated text layer. Longer legal information should be available elsewhere in the experience. The notice text is not generated by the component.

<img src="images/assistant_chat_input@ai_legal_notice_img.png" alt="assistant_chat_input@ai_legal_notice_img" width="433">

## Other boolean options

<!-- zh-row -->

**`Scrolled`** Represents the state in which the field contains more text than its visible height can display and that internal scrolling is available.  
This allows users to navigate through the overflowing text without expanding the text area beyond the maximum planned height of 240px, allowing the display of about 10 lines of text. It is particularly useful when preserving space is important, or when the text area is embedded within a fixed-height container.

**`Helper text`** Supporting text conveys additional information about the input field, such as how it will be used. It should ideally only take up a single line, though may wrap to multiple lines if required, and be either persistently visible or visible only on focus.

**`Helper link`** If the helper text is not sufficient (It can also be displayed on its own without helper text), it's possible to offer the user an additional help link (the link can be external or open a modal).

<img src="images/assistant_chat_input@other_boolean_options_img.png" alt="assistant_chat_input@other_boolean_options_img" width="433">

## Character counter

<!-- zh-row -->

### Character limit not exceeded
The character counter, located in the helper text area, displays in real time (with each keystroke) the number of characters the user can still enter before reaching the field’s allowed limit.

⚠️ It is impossible to provide a recommendation for the maximum number of characters, as this depends too specifically on the constraints (or lack thereof) of each project.  
If the count cannot be added and the text should be changed to "XXX characters maximum."

• **Character limit exceeded**  
If the user exceeds the set limit, the field enters an error state, but input is not blocked. The character counter then shows the user, still in real time, how many characters have been entered beyond the field’s allowed limit.

The user must reduce the number of characters entered for the text area to exit the error state.  
In the case where the maximum number of characters is 180, for example: When the input is at 180 char filled in the helper text changes ""You have 0/180 characters left".

<img src="images/assistant_chat_input@character_counter_img.png" alt="assistant_chat_input@character_counter_img" width="433">

## Bottom actions

<!-- zh-row -->

### Leading actions / Trailing actions
The "Bottom actions" section consists of two independent groups. The group at the beginning ("Leading actions") contains, by default, icon buttons for additional customizable options, as well as a component slot. The group at the end ("Trailing actions") contains the "send" action button, which is not customizable and must never be hidden.

&nbsp;

### Leading and trailing groups
The Bottom actions instance contains leading and trailing action groups. Each group can be shown or hidden independently.

&nbsp;

### Action 1 / Action 2 / Action 3
Show or hide each primary action independently. The default options provided can be customized on a per-project basis.

<img src="images/assistant_chat_input@bottom_actions_leading_actions_trailing_actions_img.png" alt="assistant_chat_input@bottom_actions_leading_actions_trailing_actions_img" width="433">

<!-- zh-row -->

### Slot
A dedicated slot is provided within the "Bottom actions" area to accommodate custom content. This is distinct from the content slot associated with the input field.  
This slot is disabled by default. It is not a "content-slot" property located at the root of the chat input component. Any custom content inserted into this slot will appear between the action groups.

<img src="images/assistant_chat_input@bottom_actions_slot_img.png" alt="assistant_chat_input@bottom_actions_slot_img" width="433">

<!-- zh-row -->

### Trail action
The final "send" action button cannot be customized and must never be hidden, for accessibility reasons.

&nbsp;

### Individual trailing actions
The final "send" action button cannot be customized and must never be hidden, in order to meet accessibility requirements.

<img src="images/assistant_chat_input@bottom_actions_send_only_img.png" alt="assistant_chat_input@bottom_actions_send_only_img" width="433">

Configuration shown here is made through the nested Bottom actions instance. Keep the sending action identifiable and remove actions that have no useful function in the conversation.

## Behavior by entered line count

<!-- zh-row -->

### Default display
By default, the height of the input text container is set to 60px, which allows 1 lines of text to be displayed without expanding the component.  
This height helps distinguish the field from other text inputs, prevents discouraging users with an overly large field, and keeps the layout compact at the start of a form.

• **Auto-resize (automatic expansion)**  
Above 1 lines of text, the field automatically increases in height as the user types their comment.  
This behavior is not mandatory. It is possible to enable or disable the component’s expansion depending on the page layout. In a mobile chat-type use case, for example, the height of the text area must remain fixed even if the text entered by the user exceeds 3 lines.

• **Vertical scrollbar**  
If expansion is disabled or the maximum height is reached at 240px, corresponding to about 10 lines of text, an internal scrollbar appears allowing the user to scroll through the overflowing text.  
This choice prevents breaking the layout but has the drawback, on mobile, of creating a scroll within a scroll (text area scroll inside a page scroll).

&nbsp;

### ⚠️ Old web browsers
The automatic expansion of the text area’s height based on the number of lines entered by the user is not a behavior supported by older web browsers. To address this issue, we have planned an alternative behavior for the component, which in this case has a fixed height of 144px (corresponding to about 6 lines of text), whether it is filled in or not. The selection of the appropriate expected behavior for the component is done automatically based on the version of the user’s web browser.

<img src="images/assistant_chat_input@behavior_by_entered_line_count_img.png" alt="assistant_chat_input@behavior_by_entered_line_count_img" width="433">

## Label (can it be hidden?)

<!-- zh-row -->

Indicates the function of an input field. Why hide the label for an input field? In certain user interface contexts—particularly when space is limited or the field is part of a compact layout (such as a chat input)—visually hiding the label can help maintain a clean, uncluttered interface. However, this practice should only be adopted if:  
The function of the input field remains clear, either through placeholder text or a contextual icon (e.g., a "send" icon for a chat input).  
The label remains accessible to screen readers (via `aria-label`, `aria-labelledby`, or text that is visually hidden).  
When a chat input appears in an interface that includes other possible interactions, the label must be displayed.

Hiding a label is a design choice that must balance visual simplicity and clarity of intent, without compromising inclusiveness or form guidance.

<img src="images/assistant_chat_input@label_can_it_be_hidden_img.png" alt="assistant_chat_input@label_can_it_be_hidden_img" width="433">

## Truncated input area

<!-- zh-row -->

**When losing focus, the truncation behavior of the input area differs depending on the technical environment. It’s important to respect the native behaviors designed to handle truncation:**

• On web, by default (even if the project retains control over this setting), if the text volume exceeds the visible width of the field, the input displays the end of the text (bottom-aligned) and the beginning of the text becomes invisible (masked on the top).  
There should be no visual truncation indicator (...).  
This choice is intentional because, for many fields, showing the end often makes it easier to identify the value (file names, paths, emails).  
• On Android, by default (even if the project retains control over this setting), the behavior is the same as on the web.  
• On iOS, by default (even if the project retains control over this setting), the behavior is the same as on the web.

⚠️ In all cases: the entire text must remain accessible when the field regains focus:  
• Either by refocusing the field, the text becomes horizontally scrollable again (the blinking cursor is visible).  
• Or via a tooltip on hover in certain desktop contexts.

<img src="images/assistant_chat_input@truncated_input_area_img.png" alt="assistant_chat_input@truncated_input_area_img" width="433">

## Multiline and responsiveness

<!-- zh-row -->

### Multiline
This component allows multi-line text editing. Further details are available in the “Behavior by entered line count” section.

&nbsp;

### Max-width vs full-width
For greater flexibility, this component doesn’t have a default max-width. To avoid exceeding a width that would degrade readability and the perception of a compact interactive element, we recommend applying a max-width of around 640px.  
For mobile or tablet use (or if the component is positioned inside a specific container), it is possible to set this component to use the full available width (of the screen or the container).  
Please note that this behavior is not the default rule; it may be preferred if the template allows it (to improve user comfort or for better page structure/hierarchy).

&nbsp;

### User zoom in/out
The behavior of the text during user zoom in/out must follow a fundamental principle: the text must remain readable, accessible, and must never break the structure or lose information.  
However, “Text input” components present an exception regarding the loss of textual information following the activation of user zoom in, since text truncation (label, placeholder, input text) is exceptionally allowed and enabled.  
  • The text must always scale proportionally with user zoom. Text resizing must never be blocked.  
  • Zooming must never cause text to be truncated or hidden. The component must expand vertically to allow line wrapping.  
  • The component’s height and width must be flexible, never fixed, in order to automatically adapt its dimensions according to the level of zoom.  
  • In order to preserve the minimun interactive area during user zoom out, this component have a min-width of 240px and a min-height of 92px.  
  • Even if, the component has a max-height or a max-width for resizing control purposes, technically, during user zoom in, these limitations are not fixed but must be scalable in order to adapt to the user’s zoom level.  
  • As the error icon is functional, user zoom in/out doesn’t affect the size of the icons.  
  • The behaviors of the button (layout: icon only) component during user zoom are available in the corresponding documentation.  
**Learn more about the behavior of the button component.**

<img src="images/assistant_chat_input@multiline_and_responsiveness_img.png" alt="assistant_chat_input@multiline_and_responsiveness_img" width="433">

## Rich text

<!-- zh-row -->

### Strong text
  • Strong text can be used sparingly to highlight key information within the content. Text is allowed using the corresponding "Strong" token (e.g. Label/Large/Strong or Label/Medium/Strong) depending on the selected text style.  
  • No other text styles or custom font weights should be used.

• **⚠️ Underline text and Hyperlinks**  
  • Underlined text must not be applied manually (e.g. in helper text), as it is commonly associated with hyperlinks and may mislead users.  
  • If a link is required, the dedicated helper link component must be used (e.g. **Writing guidelines**).

<img src="images/assistant_chat_input@rich_text_img.png" alt="assistant_chat_input@rich_text_img" width="433">

## Slot spacing customization

Padding within customizable slots is optional and can be adjusted or removed according to layout needs. Designers should use semantic spacing tokens when customizing these values.

Any mandatory spacing must remain outside the slots, within their parent containers. Customizing slot padding must not affect the layout or accessibility of the surrounding actions.

# Specs

## Layout and spacing

### Error: False, State: Enabled

<img src="images/assistant_chat_input@spec_layout_spacing_error_false_state_enabled_01.png" alt="assistant_chat_input@spec_layout_spacing_error_false_state_enabled_01" width="864">

<img src="images/assistant_chat_input@spec_layout_spacing_error_false_state_enabled_02.png" alt="assistant_chat_input@spec_layout_spacing_error_false_state_enabled_02" width="864">

<img src="images/assistant_chat_input@spec_layout_spacing_error_false_state_enabled_03.png" alt="assistant_chat_input@spec_layout_spacing_error_false_state_enabled_03" width="864">

<img src="images/assistant_chat_input@spec_layout_spacing_error_false_state_enabled_04.png" alt="assistant_chat_input@spec_layout_spacing_error_false_state_enabled_04" width="864">

<img src="images/assistant_chat_input@spec_layout_spacing_error_false_state_enabled_05.png" alt="assistant_chat_input@spec_layout_spacing_error_false_state_enabled_05" width="864">

<img src="images/assistant_chat_input@spec_layout_spacing_error_false_state_enabled_06.png" alt="assistant_chat_input@spec_layout_spacing_error_false_state_enabled_06" width="864">

<img src="images/assistant_chat_input@spec_layout_spacing_error_false_state_enabled_07.png" alt="assistant_chat_input@spec_layout_spacing_error_false_state_enabled_07" width="864">

### Error: False, State: Focus

<img src="images/assistant_chat_input@spec_layout_spacing_error_false_state_focus_01.png" alt="assistant_chat_input@spec_layout_spacing_error_false_state_focus_01" width="864">

<img src="images/assistant_chat_input@spec_layout_spacing_error_false_state_focus_02.png" alt="assistant_chat_input@spec_layout_spacing_error_false_state_focus_02" width="864">

<img src="images/assistant_chat_input@spec_layout_spacing_error_false_state_focus_03.png" alt="assistant_chat_input@spec_layout_spacing_error_false_state_focus_03" width="864">

### Error: False, State: Loading

<img src="images/assistant_chat_input@spec_layout_spacing_error_false_state_loading_01.png" alt="assistant_chat_input@spec_layout_spacing_error_false_state_loading_01" width="864">

<img src="images/assistant_chat_input@spec_layout_spacing_error_false_state_loading_02.png" alt="assistant_chat_input@spec_layout_spacing_error_false_state_loading_02" width="864">

### Error: False, State: Read only

<img src="images/assistant_chat_input@spec_layout_spacing_error_false_state_read_only_01.png" alt="assistant_chat_input@spec_layout_spacing_error_false_state_read_only_01" width="864">

### Error: True, State: Enabled

<img src="images/assistant_chat_input@spec_layout_spacing_error_true_state_enabled_01.png" alt="assistant_chat_input@spec_layout_spacing_error_true_state_enabled_01" width="864">

<img src="images/assistant_chat_input@spec_layout_spacing_error_true_state_enabled_02.png" alt="assistant_chat_input@spec_layout_spacing_error_true_state_enabled_02" width="864">

## States

<!-- zh-row -->

**`Enabled`** Neutral appearance, whether empty or filled.  
It allows users to click, focus, and type freely without restrictions.

<img src="images/assistant_chat_input@states_enabled_img.png" alt="assistant_chat_input@states_enabled_img" width="433">

<!-- zh-row -->

**`Hover`** Slight visual contrast or border color change.

<img src="images/assistant_chat_input@states_hover_img.png" alt="assistant_chat_input@states_hover_img" width="433">

<!-- zh-row -->

**`Focus`** The text area is focused and ready to receive user input.  
It visually highlights the field to indicate that it's currently editable and interactive. This state typically appears after a user clicks or taps into the field.

<img src="images/assistant_chat_input@states_focus_img.png" alt="assistant_chat_input@states_focus_img" width="433">

<!-- zh-row -->

**`Loading`** The Loading state indicates that the system is processing or retrieving data related to the text area.  
A progress indicator appears to inform the user that an action is in progress. During this state, the input may be temporarily disabled to prevent further interaction.

<img src="images/assistant_chat_input@states_loading_img.png" alt="assistant_chat_input@states_loading_img" width="433">

<!-- zh-row -->

**`Read only`** Text visible but not editable (often with a muted or different background).

<img src="images/assistant_chat_input@states_read_only_img.png" alt="assistant_chat_input@states_read_only_img" width="433">

<!-- zh-row -->

**`Disabled`** The field is non-interactive and grayed out to indicate it cannot be changed. The helper text is muted.

<img src="images/assistant_chat_input@states_disabled_img.png" alt="assistant_chat_input@states_disabled_img" width="433">

<!-- zh-row -->

**`Skeleton`** Improves the perceived loading time by providing a visual cue of where field will appear once fully loaded.  
Uses the "Skeleton" component, variant “Security marge=False”.

<img src="images/assistant_chat_input@states_skeleton_img.png" alt="assistant_chat_input@states_skeleton_img" width="433">

# Accessibility

Work is in progress to deliver this content.

# Develop

## Developer documentation

| Platform | Developer documentation |
|---|---|
| OUDS Web | Not available yet |
| OUDS Android | Not available yet |
| OUDS iOS | Not available yet |
| OUDS Flutter | Not available yet |

# Changelog

## Availability

| Platform | Resource | Status | Version |
|---|---|---|---|
| Figma | [Assistant chat input component](https://r.orange.fr/r/S-ouds-design-assistant-chat-input) | Early Access | 1.0.0 |
| OUDS Web (former Boosted) | Not available yet | To do | – |
| OUDS Android - Jetpack Compose | Not available yet | To do | – |
| OUDS iOS - Swift | Not available yet | To do | – |
| OUDS Flutter | Not available yet | To do | – |

## Design changelog

| Date | Number | Notes |
|------|--------|-------|
| Nov 10, 2026 | - | <ul><li>Documentation update: Slot spacing customization<li>Added guidelines clarifying that padding within customizable slots is optional and can be modified or removed using semantic spacing tokens. Mandatory spacing must remain outside the slots to preserve the component's layout and accessibility.</ul> |
| Nov 5, 2026 | 1.0.0 | **Version 2.8 of the design tokens is required for the development of this update.**<ul><li>Component creation</ul> |
| May 4, 2026 | 0.1 | <ul><li>Draft</ul> |
