# Guideline

## Intro
A text area is a multi-line input component that allows users to enter and edit longer blocks of text with automatic expansion and optional scrolling.

---

## What is it
A text area is a multi-line text area component that allows users to enter and edit longer blocks of text, such as comments, messages, or descriptions. Unlike a standard text area, which is limited to a single line, the text area can expand vertically and offers more space for content entry.

It typically includes features like a visible label, placeholder text, character limits, and optional resize behavior. The text area is ideal for open-ended responses where users need to express detailed information.

---

## Anatomy

| # | Element | Purpose |
|---|---------|---------|
| 1 | Label | Identifies the purpose of the text area field |
| 2 | Input container | The expandable area where users enter multi-line text |
| 3 | Placeholder text | Provides guidance on expected input when the field is empty |
| 4 | Helper text | Displays supporting information or character count |
| 5 | Helper link | Offers additional help or guidance when needed |
| 6 | Error message | Communicates validation issues with the entered text |
| 7 | Scrollbar | Enables navigation through text that exceeds visible height |

---

## Key Features

**Multi-line text entry**

Allows users to input extended content across multiple lines, making it suitable for detailed responses, comments, and descriptions.

**Auto-resize capability**

Automatically expands vertically as users type, starting from 3 lines (72px) and growing up to 10 lines (240px) to accommodate content without manual adjustment.

**Character limit feedback**

Displays real-time character count in the helper text area, showing remaining or exceeded characters to help users stay within defined limits.

**Scrolling behavior**

When maximum height is reached, an internal scrollbar appears to allow navigation through overflowing text while maintaining a consistent layout.

**Multiple visual styles**

Offers both filled and outlined variants with optional rounded corners to adapt to different design contexts and brand requirements.

---

## When to Use

Use the Text Area component when you need to:

✅ Collect detailed, multi-line user input such as feedback, comments, descriptions, or messages.

✅ Allow users to express open-ended responses where single-line inputs would be too restrictive.

✅ Provide visible character limits with real-time feedback to help users stay within defined constraints.

✅ Accommodate variable content length with automatic expansion up to a defined maximum height.

✅ Display pre-filled content that users can review and edit in a read-only or enabled state.

---

## When not to Use

Avoid using this component when:

❌ A single-line text input would suffice for short, predictable responses like names, emails, or phone numbers.

❌ You need structured data entry that would be better served by specific input types like date pickers, dropdowns, or number fields.

❌ The expected input is so brief that a text area's vertical space would create unnecessary visual weight in the layout.

❌ You're building a rich text editor with formatting capabilities, which requires a more advanced component with toolbar controls.

❌ Space is extremely limited and a compact input solution is required, such as inline editing or search fields.

---

## Common Patterns

### Feedback and comment forms

Text areas are commonly used in feedback forms, survey responses, and comment sections where users need to provide detailed opinions or explanations.

### Message composition

Used in messaging interfaces, email clients, and chat applications where users compose multi-line messages with character limits.

### Profile and settings descriptions

Applied in user profile pages and account settings where users enter biographical information, company descriptions, or extended personal details.

---

## Screen Variants

### Desktop

Text areas display with a default height of 72px (3 lines) and auto-expand up to 240px (10 lines) with clear visual indicators and ample space for helper text and character counts.

### Tablet

Similar behavior to desktop with adjusted touch targets and slightly modified spacing to accommodate touch interactions while maintaining readability.

### Mobile
Maintains the same height constraints but requires careful consideration of the scroll-within-scroll behavior when internal scrolling is active within the page scroll.

---

# Specs

## Properties

### Initial Config

| Property | Default Value | Notes |
|----------|---------------|-------|
| Outlined | False | Filled style with subtle background |
| Rounded corner | False | Square corners for standard contexts |
| Input status | Empty | Blank field with no placeholder |
| State | Enabled | Fully interactive and editable |
| Error | False | No validation errors displayed |
| Scrolled | False | No internal scrolling active |
| ⚠️ Label | True | Label is visible by default |
| Helper text | False | No helper text displayed |
| Helper link | False | No helper link displayed |

---

### Outlined

**`False`** An input with a subtle background fill and un visible bottom border, creating a softer and more contained look. Best suited for dense layouts or to enhance visibility.

**`True`** A minimalist input with a transparent background and a visible stroke outlining the field. This style may be interesting for contexts other than form pages:
• When inputs need to feel lightweight and unobtrusive
• In a header (search field)
• In a selection/filtering feature in a product catalog

---

### Rounded corner

**`False`** For a square finish.

**`True`** For a finish with rounded corner. To be favored in more emotional, immersive contexts or those tied to specific visual identities. For standard or business-oriented journeys, keep the default corners. This evolution addresses the need for flexibility in adapting the design to certain brand contexts.

---

### Input status

**`Empty`** The Empty state indicates that the text area is blank with no content or placeholder, a neutral starting point.

**`Empty (Placeholder)`** The Empty with Placeholder state provides a hint or guidance inside the field to suggest expected input.

**`Filled`** The Filled state shows that the user has entered valid content into the field, replacing any placeholder.

---

### State

**`Enabled`** Neutral appearance, whether empty or filled. It allows users to click, focus, and type freely without restrictions.

**`Hover`** Slight visual contrast or border color change.

**`Focus`** The text area is focused and ready to receive user input. It visually highlights the field to indicate that it's currently editable and interactive. This state typically appears after a user clicks or taps into the field.

**`Loading`** The Loading state indicates that the system is processing or retrieving data related to the text area. A progress indicator appears to inform the user that an action is in progress. During this state, the input may be temporarily disabled to prevent further interaction.

**`Read only`** Text visible but not editable (often with a muted or different background).

**`Disabled`** The field is non-interactive and grayed out to indicate it cannot be changed. The helper text is muted.

**`Skeleton`** Improves the perceived loading time by providing a visual cue of where field will appear once fully loaded. Uses the "Skeleton" component, variant "Security marge=False".

---

### Error

The Error status indicates that the user input does not meet validation rules, for example, in this specific case, if the number of characters entered by the user exceeds the allowed limit. It provides immediate visual feedback, typically through a red border, error icon, and a clear, accessible error message positioned below the input.

This state helps users quickly identify and correct mistakes by explaining what went wrong and, when possible, how to fix it. The input remains editable, encouraging users to revise their input without starting over.

**⚠️ Error message vs helper text / link** If a helper text accompanies the text input, it is replaced by the error message. However, a helper link must not be replaced and should remain positioned below the error message.

---

### Label

Describes the purpose of the input. Why hide a text area label? In some UI contexts, especially when space is limited or when the input is part of a compact layout (search bars, filters, inline forms), visually hiding the label can help maintain a clean and uncluttered interface.

However, hiding the label should only be done if:
• The purpose of the input remains clear thanks to a placeholder or contextual icon.
• The label is still accessible to screen readers (using aria-label, aria-labelledby, or visually hidden text).

Hiding a label is a design choice that must balance visual simplicity and clarity of intent, without compromising inclusiveness or form guidance.

---

### Input text

**Scrolled** Represents the state in which the field contains more text than its visible height can display and that internal scrolling is available. This allows users to navigate through the overflowing text without expanding the text area beyond **the maximum planned height of 240px, allowing the display of about 10 lines of text**. It is particularly useful when preserving space is important, or when the text area is embedded within a fixed-height container.

**Helper text** Supporting text conveys additional information about the input field, such as how it will be used. It should ideally only take up a single line, though may wrap to multiple lines if required, and be either persistently visible or visible only on focus.

**Helper link** If the helper text is not sufficient (It can also be displayed on its own without helper text), it's possible to offer the user an additional help link (the link can be external or open a modal).

---

### Display behavior

**Default display** By default, the height of **the input text container is set to 72px, which allows 3 lines of text** to be displayed without expanding the component. This height helps distinguish the field from other text inputs, prevents discouraging users with an overly large field, and keeps the layout compact at the start of a form.

**Auto-resize (automatic expansion)** Above 3 lines of text, the field automatically increases in height as the user types their comment.

**Vertical scrollbar** If expansion is disabled or **the maximum height is reached at 240px, corresponding to about 10 lines of text**, an internal scrollbar appears allowing the user to scroll through the overflowing text. This choice prevents breaking the layout but has the drawback, on mobile, of creating a scroll within a scroll (text area scroll inside a page scroll).

**⚠️ No manual resize (by the user)** On both desktop and mobile, we have chosen to disable manual resizing to avoid behaviors inconsistent with the design system.

---

### Character limit

**Character limit not exceeded** The character counter, located in the helper text area, displays in real time (with each keystroke) the number of characters the user can still enter before reaching the field's allowed limit.

⚠️ It is impossible to provide a recommendation for the maximum number of characters, as this depends too specifically on the constraints (or lack thereof) of each project.

**Character limit exceeded** If the user exceeds the set limit, the field enters an error state, but input is not blocked. The character counter then shows the user, still in real time, how many characters have been entered beyond the field's allowed limit.

The user must reduce the number of characters entered for the text area to exit the error state.

---

## Usage

### Label visibility and accessibility
**Do:** Always ensure labels are accessible to screen readers using `aria-label`, `aria-labelledby`, or visually hidden text when the visible label is hidden for design purposes.

**Don't:** Hide labels without providing alternative accessible labeling, as this creates confusion for users relying on assistive technologies.

### Character limit guidance
**Do:** Display character limits proactively with real-time counters to help users stay within constraints before reaching an error state.

**Don't:** Block user input when character limits are exceeded; instead, show the excess count and allow users to edit their content back within limits.

### Error message clarity
**Do:** Replace helper text with clear, actionable error messages that explain what went wrong and how to fix it, while preserving helper links below the error.

**Don't:** Stack error messages on top of helper text or remove helper links when errors occur, as this removes important contextual information.

### Resize behavior consistency
**Do:** Use automatic expansion from 3 to 10 lines with internal scrolling at maximum height to maintain consistent layout across the interface.

**Don't:** Allow manual resize handles that can break responsive layouts or create inconsistent component behavior across the design system.

---

# Accessibility

### Keyboard Navigation
Users must be able to navigate to the text area using the Tab key and enter it in the natural tab order of the form. Once focused, users should be able to type freely, with Enter creating new lines within the multi-line field. Shift+Tab should move focus backward. The focus indicator must have a minimum contrast ratio of 3:1 against the background. Arrow keys should navigate within the text content, and keyboard scrolling (Page Up/Page Down, Home/End) should work when internal scrolling is active.

---

### Screen Reader Support
The text area must use the semantic `<textarea>` HTML element to ensure proper identification by assistive technologies. Labels must be explicitly associated with the textarea using the `for` attribute matching the textarea's `id`, or by wrapping the textarea in a `<label>` element. Helper text should be associated using `aria-describedby` to provide context. Error messages must use `aria-describedby` or `aria-errormessage` to announce validation issues. Character count information should be announced dynamically using `aria-live="polite"` regions to inform users of remaining or exceeded characters without interrupting their input flow.

---

### ARIA Attributes
Required attributes include `aria-label` or `aria-labelledby` when labels are visually hidden, ensuring screen readers can identify the field's purpose. Use `aria-describedby` to reference helper text, character counters, and additional instructions. When errors occur, add `aria-invalid="true"` and associate error messages with `aria-describedby` or `aria-errormessage`. For character limits, use `aria-live="polite"` on the counter element to announce updates. If the textarea is required, include `aria-required="true"`. In read-only state, add `aria-readonly="true"`, and in disabled state, use the `disabled` attribute which implicitly communicates non-interactivity.

---

### Focus Management
When the text area receives focus, a clear visual indicator must appear with sufficient contrast (3:1 minimum). Focus should follow the natural document order unless programmatically managed for specific interactions. When validation errors occur, consider moving focus to the error message or maintaining it on the textarea with the error announced via `aria-live` regions. If the textarea is part of a modal or dialog, focus should be trapped within that container and restored to the triggering element when closed. Ensure focus is never lost during loading states, and that the loading indicator is announced appropriately.

---

### Error Handling
Error messages must be semantically associated with the textarea using `aria-describedby` or `aria-errormessage` so screen readers announce them when the field receives focus. The `aria-invalid="true"` attribute must be added to the textarea element when in an error state. Error messages should clearly explain what went wrong (e.g., "Character limit exceeded by 45 characters") and how to fix it. Visual indicators include a red border, error icon, and red error text meeting color contrast requirements. Error announcements should use `aria-live="assertive"` for immediate validation issues or `aria-live="polite"` for less urgent feedback. The textarea must remain editable during error states to allow correction.

---

### Touch Targets
The minimum touch target size for the text area should be at least 44x44 pixels to accommodate finger taps on mobile and tablet devices, following WCAG guidelines. Ensure adequate spacing (at least 8px) between the textarea and adjacent interactive elements to prevent accidental activation. The entire input container should be tappable to focus the field, not just the text within. Helper links and error messages below the textarea must also meet the 44x44px minimum touch target requirement with proper spacing.

---

### Color Contrast
All text within and around the text area must meet WCAG 2.1 AA contrast requirements: 4.5:1 for normal text (including labels, helper text, placeholder text, and input text) and 3:1 for large text. Error messages and error icons must maintain 4.5:1 contrast against their background. The focus indicator border must have at least 3:1 contrast against adjacent colors. In disabled state, text may have reduced contrast but should still be perceivable. Border colors, both in default and hover states, should meet 3:1 contrast for UI components. Ensure character counter text maintains 4.5:1 contrast in both normal and error states.

---

### Component-Specific Considerations
The auto-resize behavior from 3 to 10 lines must not cause unexpected scroll jumps or disorientation for users. Announce expansion behavior to screen reader users if it significantly changes the layout. The internal scrollbar that appears at maximum height creates a scroll-within-scroll situation, particularly problematic on mobile—ensure this is tested with screen readers and touch gestures. When the scrolled state is active, the scrollable region must be keyboard accessible and announced. Character limit feedback must be real-time but not overly verbose; use `aria-live="polite"` to balance immediacy with non-interruption. The skeleton loading state should include appropriate ARIA attributes (`aria-busy="true"` or `aria-live="polite"`) to inform users that content is loading. Ensure placeholder text is not relied upon as the sole labeling mechanism, as it disappears on input and may not be announced consistently.