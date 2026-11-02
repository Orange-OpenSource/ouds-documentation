# Guideline

## Intro 👈🤖

🚧 Content to be added

---

## Definition

A chat input is a UI element that allows users to compose a message in a conversation. It combines a text entry area, configurable bottom actions and optional supporting messages or a helper link.

This overview documents the supplied draft: its visual variants and editable content. Message submission, validation, character counting and suggestion logic must be implemented by the product.

Chat input does not expose Voice input, AI legal notice or a content slot at its root. The microphone is an action icon, not a voice-input mode. A slot is available only inside the nested Bottom actions component.

---

## Best for 👈🤔

✅ Composing a message in a conversation

✅ Quick, iterative exchanges rather than multi-step data entry

✅ Support and customer-service conversations

✅ Messages that can run over several lines

✅ Conversations that need extra actions next to the send action

✅ The bottom of a conversation view, on mobile and on desktop

✅ Messages with a character limit that need live feedback

✅ Messaging between users or with a team inside a product

✅ Compact layouts where the label can be hidden without losing clarity

✅ Conversations that need supporting text or a helper link, such as writing guidelines

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Chat input | The whole component: it holds the input, its bottom actions and its supporting text. | N |
| 2 | Chat input container | Surface of the input: it groups the text area and the bottom actions and carries the state styling. | N |
| 3 | Text input container | Holds the label and the entered text or placeholder. | N |
| 4 | Label text | Indicates the function of the input. It can be hidden in compact layouts. | Y |
| 5 | Bottom actions | Holds the leading and trailing actions, including the send action. | N |
| 6 | Helper text container | Holds the supporting text below the input. | Y |
| 7 | Helper text | Gives additional information about the input, such as the remaining characters. | Y |
| 8 | Helper link | Links to additional help when the helper text is not sufficient. | Y |

---

## Outlined

**`False`** An input with a subtle background fill and un visible bottom border, creating a softer and more contained look. Best suited for dense layouts or to enhance visibility.

**`True`** A minimalist input with a transparent background and a visible stroke outlining the field.  
This style may be interesting for contexts other than form pages:  
  • When inputs need to feel lightweight and unobtrusive  
  • In a header (search field)  
  • In a selection/filtering feature in a product catalog

---

## outlined_do_&_dont 👈🤔

✅ **Do:** Use Outlined False for a contained look in dense layouts or when the input needs more visibility  
❌ **Don't:** Place it on a surface where its fill no longer stands out

✅ **Do:** Use Outlined True when the input has to feel lightweight and unobtrusive  
❌ **Don't:** Use Outlined to signal that one input matters more than another

✅ **Do:** Keep the same style for every chat input of a product  
❌ **Don't:** Switch styles from one screen of a conversation to another

✅ **Do:** Check that Focus and Error stay visible in the style you choose  
❌ **Don't:** Rely on the border color alone to communicate an error

✅ **Do:** Choose the style according to the surface around the input  
❌ **Don't:** Combine both styles in the same view

---

## Rounded corner

Even though in Figma this rendering option is available and editable from the properties of each input component, the configuration of this rendering option is actually transversal across the entire product/service in which the component is used.  
It is therefore impossible to have one input component set to Rounded corner=True and another set to Rounded corner=False within the same product/service.

**`False`** The square rendering corresponds to Orange's historical style. It conveys the brand's sense of seriousness, robustness and utility-driven. It remains the default style for our digital interface components.

**`True`** The rounded rendering offers flexibility without sacrificing the attribution to the brand. It helps anchoring the service in a reality where the visual codes of the mobile area tends to rub off on all interfaces. Use rounded corners for a softer, more approachable, friendly and tactile feel.

This option is technically not available for all brand themes  
Here’s the list of rounded corners availability by brand theme

| Brand theme | Status |
|---|---|
| Orange | Available |
| Orange Compact | Available |
| Sosh | Unavailable |
| Wireframe | Unavailable |

---

## rounded_corner_do_&_dont 👈🤔

✅ **Do:** Apply one corner treatment to all the inputs of a product or service  
❌ **Don't:** Mix rounded and square inputs in the same product or service

✅ **Do:** Use rounded corners only with the themes that support them: Orange and Orange Compact  
❌ **Don't:** Expect rounded corners on the Sosh and Wireframe themes

✅ **Do:** Let the brand theme decide the corner treatment  
❌ **Don't:** Change the corners of one input to give it more emphasis

✅ **Do:** Keep the same corner treatment in every state of the input  
❌ **Don't:** Switch between rounded and square when the state changes

✅ **Do:** Use the same treatment as the other controls placed next to the input  
❌ **Don't:** Combine a rounded input with square controls in one row

---

## Input status

**`Empty`** The Empty state indicates that the text area is blank with no content or placeholder, a neutral starting point.

**`Empty (Placeholder)`** The Empty with Placeholder state provides a hint or guidance inside the field to suggest expected input.

**`Filled`** The Filled state shows that the user has entered valid content into the field, replacing any placeholder.

---

## input_status_do_&_dont 👈🤔

✅ **Do:** Write clear, contextual placeholder text  
❌ **Don't:** Use the placeholder as the only explanation of what the input does

✅ **Do:** Replace the placeholder as soon as the user types  
❌ **Don't:** Keep the hint visible next to the entered text

✅ **Do:** Keep the placeholder short enough to fit on one line  
❌ **Don't:** Put long instructions in the placeholder

✅ **Do:** Prevent the submission of an empty message in the product logic  
❌ **Don't:** Let users send an empty message

✅ **Do:** Make entered text clearly different from placeholder text  
❌ **Don't:** Style entered text like a hint

---

## Error

The Error status indicates that the user input does not meet validation rules, for example, in this specific case, if the number of characters entered by the user exceeds the allowed limit. It provides immediate visual feedback, typically through a red border, error icon, and a clear, accessible error message positioned below the input (mandatory).

This state helps users quickly identify and correct mistakes by explaining what went wrong and, when possible, how to fix it.  
The input remains editable, encouraging users to revise their input without starting over.

**⚠️ Error message vs helper text / link**  
If a helper text accompanies the text input, it is replaced by the error message. However, a helper link must not be replaced and should remain positioned below the error message.

---

## error_do_&_dont 👈🤔

✅ **Do:** Show a clear error message below the input that explains the problem and how to fix it  
❌ **Don't:** Show only a red border

✅ **Do:** Combine color with the error icon and the error text  
❌ **Don't:** Rely on color alone to show the error

✅ **Do:** Keep the input editable so that users can correct their message  
❌ **Don't:** Clear what the user has typed

✅ **Do:** Replace the helper text with the error message  
❌ **Don't:** Show the helper text and the error message at the same time

✅ **Do:** Keep the helper link below the error message  
❌ **Don't:** Replace the helper link with the error message

---

## Other boolean options

**`Scrolled`** Represents the state in which the field contains more text than its visible height can display and that internal scrolling is available.  
This allows users to navigate through the overflowing text without expanding the text area beyond the maximum planned height of 240px, allowing the display of about 10 lines of text. It is particularly useful when preserving space is important, or when the text area is embedded within a fixed-height container.

**`Helper text`** Supporting text conveys additional information about the input field, such as how it will be used. It should ideally only take up a single line, though may wrap to multiple lines if required, and be either persistently visible or visible only on focus.

**`Helper link`** If the helper text is not sufficient (It can also be displayed on its own without helper text), it's possible to offer the user an additional help link (the link can be external or open a modal).

---

## other_boolean_options_do_&_dont 👈🤔

✅ **Do:** Use Scrolled when the text exceeds the maximum height of the input  
❌ **Don't:** Let the input grow beyond its maximum height

✅ **Do:** Keep the helper text short, ideally on a single line  
❌ **Don't:** Use helper text for long instructions

✅ **Do:** Offer a helper link when the helper text is not sufficient  
❌ **Don't:** Add several links below the input

✅ **Do:** Make sure that opening the help does not lose the message being written  
❌ **Don't:** Send the user away from a conversation with no way back

✅ **Do:** Show helper text or a helper link only when they help the conversation  
❌ **Don't:** Display them on every input by default

---

## Character counter

**Character limit not exceeded**  
The character counter, located in the helper text area, displays in real time (with each keystroke) the number of characters the user can still enter before reaching the field’s allowed limit.

⚠️ It is impossible to provide a recommendation for the maximum number of characters, as this depends too specifically on the constraints (or lack thereof) of each project.  
If the count cannot be added and the text should be changed to "XXX characters maximum."

• **Character limit exceeded**  
If the user exceeds the set limit, the field enters an error state, but input is not blocked. The character counter then shows the user, still in real time, how many characters have been entered beyond the field’s allowed limit.

The user must reduce the number of characters entered for the text area to exit the error state.  
In the case where the maximum number of characters is 180, for example: When the input is at 180 char filled in the helper text changes ""You have 0/180 characters left".

---

## character_counter_do_&_dont 👈🤔

✅ **Do:** Show the remaining characters in real time  
❌ **Don't:** Reveal the limit only after the user tries to send

✅ **Do:** Let users keep typing past the limit and show how far they have gone over  
❌ **Don't:** Block input when the limit is reached

✅ **Do:** Set the limit according to the constraints of the project  
❌ **Don't:** Copy a limit from another product without checking it

✅ **Do:** Use the "XXX characters maximum" text when the count cannot be added  
❌ **Don't:** Display a counter that does not update

✅ **Do:** Leave the error state as soon as the text is back within the limit  
❌ **Don't:** Keep the error displayed once the text fits

---

## Bottom actions

**Leading actions / Trailing actions**  
The "Bottom actions" section consists of two independent groups. The group at the beginning ("Leading actions") contains, by default, icon buttons for additional customizable options, as well as a component slot. The group at the end ("Trailing actions") contains the "send" action button, which is not customizable and must never be hidden.

**Leading and trailing groups**  
The Bottom actions instance contains leading and trailing action groups. Each group can be shown or hidden independently.

**Action 1 / Action 2 / Action 3**  
Show or hide each primary action independently. The default options provided can be customized on a per-project basis.

**Slot**  
A dedicated slot is provided within the "Bottom actions" area to accommodate custom content. This is distinct from the content slot associated with the input field.  
This slot is disabled by default. It is not a "content-slot" property located at the root of the chat input component. Any custom content inserted into this slot will appear between the action groups.

**Trail action**  
The final "send" action button cannot be customized and must never be hidden, for accessibility reasons.

**Individual trailing actions**  
The final "send" action button cannot be customized and must never be hidden, in order to meet accessibility requirements.

Configuration shown here is made through the nested Bottom actions instance. Keep the sending action identifiable and remove actions that have no useful function in the conversation.

---

## bottom_actions_do_&_dont 👈🤔

✅ **Do:** Keep the send action identifiable and always visible  
❌ **Don't:** Hide the send action

✅ **Do:** Remove the actions that have no useful function in the conversation  
❌ **Don't:** Fill all the action places by default

✅ **Do:** Give every icon-only action an accessible name  
❌ **Don't:** Use ambiguous icons without a name

✅ **Do:** Use the slot of the bottom actions for custom content between the action groups  
❌ **Don't:** Confuse it with a content slot of the input area

✅ **Do:** Use specific, verb-based labels so that users understand the outcome  
❌ **Don't:** Use generic labels such as "OK"

---

## Behavior by entered line count

**Default display**  
By default, the height of the input text container is set to 60px, which allows 1 lines of text to be displayed without expanding the component.  
This height helps distinguish the field from other text inputs, prevents discouraging users with an overly large field, and keeps the layout compact at the start of a form.

• **Auto-resize (automatic expansion)**  
Above 1 lines of text, the field automatically increases in height as the user types their comment.  
This behavior is not mandatory. It is possible to enable or disable the component’s expansion depending on the page layout. In a mobile chat-type use case, for example, the height of the text area must remain fixed even if the text entered by the user exceeds 3 lines.

• **Vertical scrollbar**  
If expansion is disabled or the maximum height is reached at 240px, corresponding to about 10 lines of text, an internal scrollbar appears allowing the user to scroll through the overflowing text.  
This choice prevents breaking the layout but has the drawback, on mobile, of creating a scroll within a scroll (text area scroll inside a page scroll).

**⚠️ Old web browsers**  
The automatic expansion of the text area’s height based on the number of lines entered by the user is not a behavior supported by older web browsers. To address this issue, we have planned an alternative behavior for the component, which in this case has a fixed height of 144px (corresponding to about 6 lines of text), whether it is filled in or not. The selection of the appropriate expected behavior for the component is done automatically based on the version of the user’s web browser.

---

## behavior_by_entered_line_count_do_&_dont 👈🤔

✅ **Do:** Start with a compact input that grows as the user types  
❌ **Don't:** Start with a large empty field

✅ **Do:** Switch to internal scrolling once the maximum height is reached  
❌ **Don't:** Let the input push the conversation off the screen

✅ **Do:** Keep a fixed height when the page layout requires it  
❌ **Don't:** Enable expansion in a layout that cannot absorb it

✅ **Do:** Check the scroll inside a scroll on mobile  
❌ **Don't:** Assume that a nested scroll is comfortable on small screens

✅ **Do:** Rely on the planned fixed height for older web browsers  
❌ **Don't:** Depend on automatic expansion in every browser

---

## ⚠️ Label (can it be hidden?)

Indicates the function of an input field. Why hide the label for an input field? In certain user interface contexts—particularly when space is limited or the field is part of a compact layout (such as a chat input)—visually hiding the label can help maintain a clean, uncluttered interface. However, this practice should only be adopted if:  
The function of the input field remains clear, either through placeholder text or a contextual icon (e.g., a "send" icon for a chat input).  
The label remains accessible to screen readers (via `aria-label`, `aria-labelledby`, or text that is visually hidden).  
When a chat input appears in an interface that includes other possible interactions, the label must be displayed.

Hiding a label is a design choice that must balance visual simplicity and clarity of intent, without compromising inclusiveness or form guidance.

---

## label_can_it_be_hidden_do_&_dont 👈🤔

✅ **Do:** Keep the function clear through placeholder text or a contextual icon when the label is hidden  
❌ **Don't:** Hide the label without replacing its meaning

✅ **Do:** Keep the label available to screen readers  
❌ **Don't:** Remove the label from the accessibility tree

✅ **Do:** Display the label when the interface includes other possible interactions  
❌ **Don't:** Hide it in a layout with several controls

✅ **Do:** Hide the label only when space is limited or the layout is compact  
❌ **Don't:** Hide it for visual preference alone

✅ **Do:** Write a short label in sentence case, without a colon  
❌ **Don't:** Use a long phrase as a label

---

## ⚠️ Truncated input area

**When losing focus, the truncation behavior of the input area differs depending on the technical environment. It’s important to respect the native behaviors designed to handle truncation:**

• On web, by default (even if the project retains control over this setting), if the text volume exceeds the visible width of the field, the input displays the end of the text (bottom-aligned) and the beginning of the text becomes invisible (masked on the top).  
There should be no visual truncation indicator (...).  
This choice is intentional because, for many fields, showing the end often makes it easier to identify the value (file names, paths, emails).  
• On Android, by default (even if the project retains control over this setting), the behavior is the same as on the web.  
• On iOS, by default (even if the project retains control over this setting), the behavior is the same as on the web.

⚠️ In all cases: the entire text must remain accessible when the field regains focus:  
• Either by refocusing the field, the text becomes horizontally scrollable again (the blinking cursor is visible).  
• Or via a tooltip on hover in certain desktop contexts.

---

## truncated_input_area_do_&_dont 👈🤔

✅ **Do:** Respect the native truncation behavior of each environment  
❌ **Don't:** Override it with a custom behavior

✅ **Do:** Show the end of the text when the input loses focus  
❌ **Don't:** Add a visual truncation indicator (...)

✅ **Do:** Keep the entire text accessible when the input regains focus  
❌ **Don't:** Make part of the text unreachable

✅ **Do:** Offer a tooltip on hover in desktop contexts when it helps  
❌ **Don't:** Rely on a tooltip on touch screens

✅ **Do:** Test truncation with long messages  
❌ **Don't:** Assume that the visible text is enough to identify the message

---

## Multiline and responsiveness

**Multiline**  
This component allows multi-line text editing. Further details are available in the “Behavior by entered line count” section.

**Max-width vs full-width**  
For greater flexibility, this component doesn’t have a default max-width. To avoid exceeding a width that would degrade readability and the perception of a compact interactive element, we recommend applying a max-width of around 640px.  
For mobile or tablet use (or if the component is positioned inside a specific container), it is possible to set this component to use the full available width (of the screen or the container).  
Please note that this behavior is not the default rule; it may be preferred if the template allows it (to improve user comfort or for better page structure/hierarchy).

**User zoom in/out**  
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

---

## multiline_and_responsiveness_do_&_dont 👈🤔

✅ **Do:** Apply a max-width of around 640px  
❌ **Don't:** Stretch the input across a very wide screen

✅ **Do:** Use the full available width on mobile or inside a specific container when the template allows it  
❌ **Don't:** Make full width the default rule

✅ **Do:** Let the text scale proportionally with user zoom  
❌ **Don't:** Block text resizing

✅ **Do:** Keep the height and width flexible so the input adapts to the zoom level  
❌ **Don't:** Fix the dimensions of the input

✅ **Do:** Preserve the minimum interactive area when the user zooms out  
❌ **Don't:** Let the input shrink below its minimum size

---

## Rich text

**Strong text**  
  • Strong text can be used sparingly to highlight key information within the content. Text is allowed using the corresponding "Strong" token (e.g. Label/Large/Strong or Label/Medium/Strong) depending on the selected text style.  
  • No other text styles or custom font weights should be used.

• **⚠️ Underline text and Hyperlinks**  
  • Underlined text must not be applied manually (e.g. in helper text), as it is commonly associated with hyperlinks and may mislead users.  
  • If a link is required, the dedicated helper link component must be used (e.g. **Writing guidelines**).

---

## rich_text_do_&_dont 👈🤔

✅ **Do:** Use the matching Strong token sparingly to highlight key information  
❌ **Don't:** Use other text styles or custom font weights

✅ **Do:** Use the dedicated helper link component when a link is required  
❌ **Don't:** Underline text manually

✅ **Do:** Reserve strong text for short, key information such as a character count  
❌ **Don't:** Set a whole sentence in strong text

✅ **Do:** Choose the Strong token that matches the selected text style  
❌ **Don't:** Mix Strong tokens from different text styles in one message

✅ **Do:** Keep supporting text simple  
❌ **Don't:** Add hyperlinks inside the helper text

---

# Specs

## States

**`Enabled`** Neutral appearance, whether empty or filled.  
It allows users to click, focus, and type freely without restrictions.

**`Hover`** Slight visual contrast or border color change.

**`Focus`** The text area is focused and ready to receive user input.  
It visually highlights the field to indicate that it's currently editable and interactive. This state typically appears after a user clicks or taps into the field.

**`Loading`** The Loading state indicates that the system is processing or retrieving data related to the text area.  
A progress indicator appears to inform the user that an action is in progress. During this state, the input may be temporarily disabled to prevent further interaction.

**`Read only`** Text visible but not editable (often with a muted or different background).

**`Disabled`** The field is non-interactive and grayed out to indicate it cannot be changed. The helper text is muted.

**`Skeleton`** Improves the perceived loading time by providing a visual cue of where field will appear once fully loaded.  
Uses the "Skeleton" component, variant “Security marge=False”.

---

## Layout and spacing

### Error: False, State: Enabled

- Chat input: Empty — `chat_input@spec_layout_spacing_error_false_state_enabled_01`
- Chat input container — `chat_input@spec_layout_spacing_error_false_state_enabled_02`
- Text input container — `chat_input@spec_layout_spacing_error_false_state_enabled_03`
- Text container — `chat_input@spec_layout_spacing_error_false_state_enabled_04`
- Label text container — `chat_input@spec_layout_spacing_error_false_state_enabled_05`
- Helper text container — `chat_input@spec_layout_spacing_error_false_state_enabled_06`

### Error: False, State: Focus

- Text container — `chat_input@spec_layout_spacing_error_false_state_focus_01`
- Input container — `chat_input@spec_layout_spacing_error_false_state_focus_02`
- Input container — `chat_input@spec_layout_spacing_error_false_state_focus_03`

### Error: False, State: Loading

- Trailing container — `chat_input@spec_layout_spacing_error_false_state_loading_01`
- Progress indicator container — `chat_input@spec_layout_spacing_error_false_state_loading_02`

### Error: True, State: Enabled

- Text input container — `chat_input@spec_layout_spacing_error_true_state_enabled_01`
- Error text container — `chat_input@spec_layout_spacing_error_true_state_enabled_02`

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Oct 30, 2026 | 1.0.0 | **Version 2.8 of the design tokens is required for the development of this update.**<ul><li>Component creation</ul> | Jérôme Regnier<br>Maxime Tonnerre |
| May 4, 2026 | 0.1 | <ul><li>Draft</ul> | Jérôme Regnier<br>Maxime Tonnerre |
