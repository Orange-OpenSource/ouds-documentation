# Guideline

## Intro
A text area is a multi-line input component that allows users to enter and edit longer blocks of text, such as comments, messages, or descriptions, with features like automatic expansion, character limits, and validation feedback.

---

## What is it
A text area is a multi-line text area component that allows users to enter and edit longer blocks of text, such as comments, messages, or descriptions. Unlike a standard text area, which is limited to a single line, the text area can expand vertically and offers more space for content entry.

It typically includes features like a visible label, placeholder text, character limits, and optional resize behavior. The text area is ideal for open-ended responses where users need to express detailed information.

---

## Anatomy

| # | Element | Purpose |
|---|---------|---------|
| 1 | Label | Identifies the purpose of the text area and guides user input |
| 2 | Input Container | Houses the text content and provides visual boundaries for the input area |
| 3 | Input Text | Displays the user-entered content across multiple lines |
| 4 | Placeholder Text | Provides guidance or example text when the field is empty |
| 5 | Character Counter | Shows remaining or exceeded character count in real-time |
| 6 | Helper Text | Offers additional context, instructions, or validation messages |
| 7 | Helper Link | Provides access to supplementary information or external help resources |
| 8 | Scrollbar | Enables navigation through content that exceeds the visible area |

---

## Key Features

**Multi-line Input Capability**
Unlike single-line text inputs, the text area supports multiple lines of text, making it ideal for longer content entries such as comments, descriptions, or messages.

**Automatic Height Expansion**
The component automatically expands vertically as users type beyond the initial 3-line display, accommodating growing content up to a maximum of 10 lines (240px) before introducing a scrollbar.

**Real-time Character Counter**
Provides immediate feedback on character usage, displaying remaining characters before reaching the limit and showing excess characters when the limit is exceeded, helping users stay within constraints.

**Flexible Visual Styles**
Offers both filled and outlined variants with optional rounded corners, allowing adaptation to different design contexts from dense forms to lightweight search interfaces.

**Comprehensive State Management**
Supports multiple interaction states including enabled, hover, focus, loading, read-only, disabled, and error states, with clear visual feedback for each condition.

---

## When to Use

✅ When users need to provide detailed, open-ended responses that require multiple sentences or paragraphs, such as feedback forms, comment sections, or message composition

✅ For collecting descriptions, explanations, or narratives where content length is unpredictable and may vary significantly between users

✅ When implementing forms that require validation with character limits, where real-time feedback on remaining characters improves user experience

✅ In scenarios where content may need to be reviewed or edited after initial entry, benefiting from the expanded viewing area

✅ When you need to differentiate longer text inputs from single-line fields in a form, making the interface more intuitive and reducing user confusion

---

## When not to Use

❌ For short, single-line inputs like names, email addresses, or search queries where a standard text input would be more appropriate and space-efficient

❌ In highly constrained mobile layouts where the expanded height could disrupt the overall page flow or create awkward scrolling experiences

❌ When collecting structured data that would be better served by specific input types like dropdowns, radio buttons, or formatted fields (phone numbers, dates)

❌ For extremely long-form content creation where a dedicated rich text editor with formatting capabilities would provide a better authoring experience

❌ In read-only contexts where content simply needs to be displayed rather than edited, where a standard text display would be more appropriate

---

## Common Patterns

**Feedback and Review Forms**
Text areas are commonly used in customer feedback forms, product reviews, or survey responses where users need to share detailed opinions or experiences. The automatic expansion feature allows users to write as much as they need without being constrained by a small initial field, while the character counter helps them stay within reasonable limits. The error state provides clear guidance when responses are too long, ensuring submissions meet system requirements.

**Comment and Discussion Threads**
In social platforms, support tickets, or collaborative tools, text areas facilitate conversation by providing space for thoughtful replies and detailed explanations. The multi-line format encourages more comprehensive responses than single-line inputs, while the scrollable behavior at maximum height keeps the interface manageable even in lengthy discussions. The helper text can guide tone or content expectations, improving communication quality.

**Form Applications and Submissions**
Application forms for jobs, grants, or registrations often require detailed text entries for questions like "Why are you interested?" or "Describe your experience." Text areas in these contexts provide the necessary space for thoughtful responses while the character counter ensures applicants meet minimum or maximum length requirements. The outlined variant can be used in lighter-weight filtering interfaces, while the filled variant works well in traditional form layouts where multiple fields are stacked vertically.

---

## Screen Variants

**Desktop**
On desktop screens, the text area displays with optimal spacing and typically shows the default 3-line height (72px) initially. The component can comfortably expand to the maximum height of 240px (approximately 10 lines) before introducing a scrollbar. The larger viewport allows for generous padding around the field, clear visibility of helper text and character counters, and easy mouse interaction with the scrollbar when content overflows. Labels, helper text, and error messages have ample space and remain fully visible without wrapping.

**Tablet**
For tablet devices, the text area maintains similar functionality to desktop but may require slightly adjusted spacing to optimize for touch interaction. The component should maintain adequate tap target sizes (minimum 44x44px for interactive elements), and the scrollbar should be touch-friendly with sufficient width for finger scrolling. Consider the orientation: in portrait mode, the text area might occupy more vertical screen space, while landscape mode provides more horizontal room. Helper text and character counters remain visible but may wrap to multiple lines if necessary.

**Mobile**
On mobile devices, the text area requires careful consideration of the limited screen real estate. The component should span the full width of the container with appropriate margins to prevent edge-to-edge placement. The initial 3-line height is maintained, but be aware that vertical expansion can quickly consume valuable screen space. When the maximum height is reached and scrolling is introduced, users may encounter a scroll-within-scroll situation (text area scrolling within page scrolling), which can be challenging. Ensure the keyboard doesn't obscure the field when focused, and consider using the system's native scrolling behavior. Labels may appear above the field, and helper text should remain concise to avoid excessive scrolling. Touch targets for any interactive elements (like helper links) must meet minimum size requirements for comfortable thumb interaction.

---

# Specs

## Properties

### Initial Config

| Property | Default Value | Notes |
|----------|---------------|-------|
| Outlined | False | Filled style with subtle background |
| Rounded corner | False | Square corners for standard contexts |
| Input status | Empty | Blank field with no content |
| State | Enabled | Fully interactive and editable |
| Error | False | No validation errors present |
| Scrolled | False | No overflow scrolling needed |
| ⚠️ Label | True | Label visible by default |
| Helper text | False | No helper text displayed |
| Helper link | False | No additional help link |

---

### Outlined

**`False`**
An input with a subtle background fill and un visible bottom border, creating a softer and more contained look. Best suited for dense layouts or to enhance visibility.

**`True`**
A minimalist input with a transparent background and a visible stroke outlining the field. This style may be interesting for contexts other than form pages:
• When inputs need to feel lightweight and unobtrusive
• In a header (search field)
• In a selection/filtering feature in a product catalog

---

### Rounded corner

**`False`**
For a square finish.

**`True`**
For a finish with rounded corner. To be favored in more emotional, immersive contexts or those tied to specific visual identities. For standard or business-oriented journeys, keep the default corners. This evolution addresses the need for flexibility in adapting the design to certain brand contexts.

---

### Input status

**`Empty`**
The Empty state indicates that the text area is blank with no content or placeholder, a neutral starting point.

**`Empty (Placeholder)`**
The Empty with Placeholder state provides a hint or guidance inside the field to suggest expected input.

**`Filled`**
The Filled state shows that the user has entered valid content into the field, replacing any placeholder.

---

### States

**`Enabled`**
Neutral appearance, whether empty or filled. It allows users to click, focus, and type freely without restrictions.

**`Hover`**
Slight visual contrast or border color change.

**`Focus`**
The text area is focused and ready to receive user input. It visually highlights the field to indicate that it's currently editable and interactive. This state typically appears after a user clicks or taps into the field.

**`Loading`**
The Loading state indicates that the system is processing or retrieving data related to the text area. A progress indicator appears to inform the user that an action is in progress. During this state, the input may be temporarily disabled to prevent further interaction.

**`Read only`**
Text visible but not editable (often with a muted or different background).

**`Disabled`**
The field is non-interactive and grayed out to indicate it cannot be changed. The helper text is muted.

**`Skeleton`**
Improves the perceived loading time by providing a visual cue of where field will appear once fully loaded. Uses the "Skeleton" component, variant "Security marge=False".

---

### Error

The Error status indicates that the user input does not meet validation rules, for example, in this specific case, if the number of characters entered by the user exceeds the allowed limit. It provides immediate visual feedback, typically through a red border, error icon, and a clear, accessible error message positioned below the input.

This state helps users quickly identify and correct mistakes by explaining what went wrong and, when possible, how to fix it. The input remains editable, encouraging users to revise their input without starting over.

⚠️ **Error message vs helper text / link**

If a helper text accompanies the text input, it is replaced by the error message. However, a helper link must not be replaced and should remain positioned below the error message.

---

### ⚠️ Label

Describes the purpose of the input. Why hide a text area label?

In some UI contexts, especially when space is limited or when the input is part of a compact layout (search bars, filters, inline forms), visually hiding the label can help maintain a clean and uncluttered interface.

However, hiding the label should only be done if:
• The purpose of the input remains clear thanks to a placeholder or contextual icon.
• The label is still accessible to screen readers (using aria-label, aria-labelledby, or visually hidden text).

Hiding a label is a design choice that must balance visual simplicity and clarity of intent, without compromising inclusiveness or form guidance.

---

### Other boolean options

**Scrolled**
Represents the state in which the field contains more text than its visible height can display and that internal scrolling is available. This allows users to navigate through the overflowing text without expanding the text area beyond **the maximum planned height of 240px, allowing the display of about 10 lines of text**. It is particularly useful when preserving space is important, or when the text area is embedded within a fixed-height container.

**Helper text**
Supporting text conveys additional information about the input field, such as how it will be used. It should ideally only take up a single line, though may wrap to multiple lines if required, and be either persistently visible or visible only on focus.

**Helper link**
If the helper text is not sufficient (It can also be displayed on its own without helper text), it's possible to offer the user an additional help link (the link can be external or open a modal).

---

### Behavior by entered line count

**Default display**
By default, the height of **the input text container is set to 72px, which allows 3 lines of text** to be displayed without expanding the component. This height helps distinguish the field from other text inputs, prevents discouraging users with an overly large field, and keeps the layout compact at the start of a form.

**Auto-resize (automatic expansion)**
Above 3 lines of text, the field automatically increases in height as the user types their comment.

**Vertical scrollbar**

If expansion is disabled or **the maximum height is reached at 240px, corresponding to about 10 lines of text**, an internal scrollbar appears allowing the user to scroll through the overflowing text. This choice prevents breaking the layout but has the drawback, on mobile, of creating a scroll within a scroll (text area scroll inside a page scroll).

⚠️ **No manual resize (by the user)**
On both desktop and mobile, we have chosen to disable manual resizing to avoid behaviors inconsistent with the design system.

---

### Character counter

**Character limit not exceeded**
The character counter, located in the helper text area, displays in real time (with each keystroke) the number of characters the user can still enter before reaching the field's allowed limit.

⚠️ It is impossible to provide a recommendation for the maximum number of characters, as this depends too specifically on the constraints (or lack thereof) of each project.

**Character limit exceeded**
If the user exceeds the set limit, the field enters an error state, but input is not blocked. The character counter then shows the user, still in real time, how many characters have been entered beyond the field's allowed limit.

The user must reduce the number of characters entered for the text area to exit the error state.

---

## Usage

### Label Visibility and Clarity
**Do:** Always provide a clear, descriptive label that explains the purpose of the text area, even if it's visually hidden for compact layouts, ensuring screen readers can access it via aria-label or aria-labelledby.

**Don't:** Hide the label without providing alternative accessible text or rely solely on placeholder text to convey the field's purpose, as placeholders disappear when users start typing.

---

### Character Limit Communication
**Do:** Set appropriate character limits based on content requirements and display the real-time character counter in the helper text area to provide continuous feedback as users type.

**Don't:** Block user input when the character limit is exceeded; instead, enter an error state that clearly shows how many characters need to be removed while keeping the content editable.

---

### Helper Text and Error Messages
**Do:** Use helper text to provide guidance on expected content format or usage, and replace it with clear, actionable error messages that explain what went wrong and how to fix it when validation fails.

**Don't:** Display both helper text and error messages simultaneously, or remove helper links when showing error messages—keep helper links positioned below the error message for additional support.

---

### Height and Scrolling Behavior
**Do:** Allow the text area to expand automatically from the default 3-line height (72px) up to the maximum 10-line height (240px), then introduce a scrollbar for overflow content to maintain layout consistency.

**Don't:** Enable manual resizing by users or allow unlimited vertical expansion that could break the layout, especially in mobile contexts where scroll-within-scroll can create confusing interactions.

---

# Accessibility

## Keyboard navigation
The text area must be fully operable using keyboard controls. Users should be able to tab into the field, type content naturally, use arrow keys to navigate within text, and shift+tab to exit. The focus indicator must be clearly visible with sufficient contrast (minimum 3:1 ratio against adjacent colors) to show when the field is active. When an error occurs, focus should move to the error message or remain on the field with the error announced.

---

## Screen reader support
Implement proper semantic HTML using the `<textarea>` element with associated `<label>` elements connected via matching `for` and `id` attributes. The label must be programmatically associated even when visually hidden. Helper text should be associated using `aria-describedby`, and error messages should be linked with `aria-describedby` and announced using `aria-live="polite"` or `aria-live="assertive"` for critical errors. Character counter updates should be announced periodically, not on every keystroke to avoid overwhelming screen reader users.

---

## ARIA attributes and labels
Use `aria-label` or `aria-labelledby` when labels are visually hidden to ensure screen readers can identify the field's purpose. Apply `aria-required="true"` for mandatory fields. Use `aria-invalid="true"` when validation fails and `aria-describedby` to reference both helper text and error message IDs. For multi-part descriptions, include space-separated IDs in `aria-describedby` (e.g., `aria-describedby="helper-text-id error-message-id"`). The `aria-multiline="true"` attribute should be set to indicate the multi-line nature of the input.

---

## Error communication
Error messages must be clear, specific, and actionable, explaining both what went wrong and how to correct it. Errors should be communicated through multiple channels: visual styling (color, iconography), text content, and ARIA attributes. Never rely on color alone to indicate errors—always include an icon and text message. When character limits are exceeded, announce the overage amount and required reduction. Error states should not disable the field but should allow users to edit and correct their input immediately.

---

## Focus management
Maintain logical focus order within forms, ensuring the text area appears in the natural tab sequence. When users interact with helper links that open modals or external resources, manage focus appropriately—moving focus to the opened content and returning it to the text area upon closing. Avoid focus traps that prevent keyboard users from navigating away from the field.

---

## Touch target sizing
On mobile and tablet devices, ensure the entire text area input region meets minimum touch target size requirements of 44×44 pixels (iOS) or 48×48 pixels (Android). Interactive elements like helper links should be adequately spaced (minimum 8px separation) to prevent accidental activation. The scrollbar, when visible, should be thick enough for touch interaction without frustration.

---

## Color contrast requirements
All text within and around the text area must meet WCAG AA standards: 4.5:1 contrast ratio for normal text and 3:1 for large text (18pt or 14pt bold). This includes labels, input text, placeholder text, helper text, error messages, and character counters. In disabled states, ensure at least 3:1 contrast so users can still perceive the field's presence and label. Border colors and focus indicators must maintain 3:1 contrast against adjacent background colors.

---

## Component-specific accessibility concerns
The nested scroll pattern (scrollbar within the text area on a scrollable page) requires careful implementation to ensure screen reader users understand they're navigating within a bounded region. Consider using `role="textbox"` with `aria-multiline="true"` for custom implementations. The auto-resize behavior should not cause unexpected page reflows that disorient users. Loading states must be announced to screen readers using appropriate ARIA live regions. When the skeleton state is active, use `aria-busy="true"` or `aria-label="Loading"` to communicate the loading status to assistive technologies.