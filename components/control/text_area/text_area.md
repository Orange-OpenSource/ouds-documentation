Text_area_raw.md
# Guideline
## Intro
The text area allows users to input multi-line text for forms, comments, or longer messages. It supports expandable content and character limits.

## What is It?
A text area is a multi-line input field that accommodates larger amounts of free-form text. Unlike single-line inputs, it provides vertical space and can expand or scroll as content grows.

## Anatomy
Part | Description | Optional
--- | --- | ---
Label | Identifies the purpose of the field | Optional
Input container | The editable area where text is entered | Required
Placeholder text | Hint text displayed when empty | Optional
Input text | User-entered content | Optional
Helper text | Guidance or formatting instructions | Optional
Error message | Validation feedback when input is invalid | Optional
Helper link | Additional support resource | Optional
Character counter | Real-time count of characters entered vs limit | Optional

## Key Features
- **Multi-line input**: Supports longer text entries spanning multiple lines.
- **Auto-resize**: Expands vertically from 3 to approximately 10 lines as content grows.
- **Character limits**: Tracks and enforces maximum character counts with real-time feedback.
- **Validation feedback**: Displays clear error messages without blocking input.

## When to Use
- Collect detailed feedback, comments, or descriptions from users.
- Enable users to compose messages, reviews, or notes.
- Capture multi-line data in forms where single-line inputs are insufficient.

## When Not to Use
- Avoid for short, single-line entries; use a standard text input instead.
- Avoid when structured data formats (dropdowns, checkboxes) are more appropriate.
- Avoid for highly formatted text; consider a rich text editor.

## Common Patterns
**Feedback forms**  
Users provide detailed comments or suggestions in surveys, customer support, or product reviews. The text area auto-expands to accommodate longer responses.

**Message composition**  
Users write messages, notes, or descriptions in messaging apps, comment threads, or content management systems. Character counters help manage length constraints.

**Form fields for descriptions**  
Users enter job descriptions, project summaries, or biographical information in registration or profile forms. Helper text clarifies formatting requirements.

# Spec
## Properties → Initial Config
| property name | type |
| --- | --- |
| Outlined | 'False' | 'True' |
| Rounded corner | 'False' | 'True' |
| Input status | 'Empty' | 'Empty (Placeholder)' | 'Filled' |
| State | 'Enabled' | 'Hover' | 'Focus' | 'Loading' | 'Read only' | 'Disabled' | 'Skeleton' |
| Error | 'False' | 'True' |
| Scrolled | boolean |
| ⚠️ Label | boolean |
| ✏️ Label | text |
| ✏️ Placeholder | text |
| ✏️ Input text | text |
| Helper text | boolean |
| ✏️ Helper text | text |
| ✏️ Error empty text | text |
| ✏️ Error filled text | text |
| Helper link | boolean |

> Notes:
> - Default configuration: Outlined='False', Rounded corner='False', Input status='Empty (Placeholder)', State='Enabled', Error='False'.
> - Character counter appears in the helper text area when limits are enforced.

## Properties → Full (from properties_md verbatim)

### Outlined

**`False`**  
An input with a subtle background fill and un visible bottom border, creating a softer and more contained look. Best suited for dense layouts or to enhance visibility.

**`True`**  
A minimalist input with a transparent background and a visible stroke outlining the field.
This style may be interesting for contexts other than form pages:
- When inputs need to feel lightweight and unobtrusive
- In a header (search field)
- In a selection/filtering feature in a product catalog

---

### Rounded corner

**`False`**  
For a square finish.

**`True`**  
For a finish with rounded corner.
To be favored in more emotional, immersive contexts or those tied to specific visual identities. For standard or business-oriented journeys, keep the default corners. This evolution addresses the need for flexibility in adapting the design to certain brand contexts.

---

### Input status

**`Empty`**  
The Empty state indicates that the text area is blank with no content or placeholder, a neutral starting point.

**`Empty (Placeholder)`**  
The Empty with Placeholder state provides a hint or guidance inside the field to suggest expected input.

**`Filled`**  
The Filled state shows that the user has entered valid content into the field, replacing any placeholder.

---

### State

**`Enabled`**  
Neutral appearance, whether empty or filled.
It allows users to click, focus, and type freely without restrictions.

**`Hover`**  
Slight visual contrast or border color change.

**`Focus`**  
The text area is focused and ready to receive user input.
It visually highlights the field to indicate that it's currently editable and interactive. This state typically appears after a user clicks or taps into the field.

**`Loading`**  
The Loading state indicates that the system is processing or retrieving data related to the text area.
A progress indicator appears to inform the user that an action is in progress. During this state, the input may be temporarily disabled to prevent further interaction.

**`Read only`**  
Text visible but not editable (often with a muted or different background).

**`Disabled`**  
The field is non-interactive and grayed out to indicate it cannot be changed. The helper text is muted.

**`Skeleton`**  
Improves the perceived loading time by providing a visual cue of where field will appear once fully loaded.
Uses the "Skeleton" component, variant "Security marge=False".

---

### Error

The Error status indicates that the user input does not meet validation rules, for example, in this specific case, if the number of characters entered by the user exceeds the allowed limit. It provides immediate visual feedback, typically through a red border, error icon, and a clear, accessible error message positioned below the input.

This state helps users quickly identify and correct mistakes by explaining what went wrong and, when possible, how to fix it.
The input remains editable, encouraging users to revise their input without starting over.

**⚠️ Error message vs helper text / link**  
If a helper text accompanies the text input, it is replaced by the error message. However, a helper link must not be replaced and should remain positioned below the error message.

---

### ⚠️ Label

Describes the purpose of the input. Why hide a text area label?
In some UI contexts, especially when space is limited or when the input is part of a compact layout (search bars, filters, inline forms), visually hiding the label can help maintain a clean and uncluttered interface. However, hiding the label should only be done if:
- The purpose of the input remains clear thanks to a placeholder or contextual icon.
- The label is still accessible to screen readers (using aria-label, aria-labelledby, or visually hidden text).

Hiding a label is a design choice that must balance visual simplicity and clarity of intent, without compromising inclusiveness or form guidance.

---

### Other boolean options

**Scrolled**  
Represents the state in which the field contains more text than its visible height can display and that internal scrolling is available.
This allows users to navigate through the overflowing text without expanding the text area beyond the maximum planned height of 240px, allowing the display of about 10 lines of text. It is particularly useful when preserving space is important, or when the text area is embedded within a fixed-height container.

**Helper text**  
Supporting text conveys additional information about the input field, such as how it will be used. It should ideally only take up a single line, though may wrap to multiple lines if required, and be either persistently visible or visible only on focus.

**Helper link**  
If the helper text is not sufficient (It can also be displayed on its own without helper text), it's possible to offer the user an additional help link (the link can be external or open a modal).

---

### Behavior by entered line count

**Default display**  
By default, the height of the input text container is set to 72px, which allows 3 lines of text to be displayed without expanding the component.
This height helps distinguish the field from other text inputs, prevents discouraging users with an overly large field, and keeps the layout compact at the start of a form.

**Auto-resize (automatic expansion)**  
Above 3 lines of text, the field automatically increases in height as the user types their comment.

**Vertical scrollbar**  
If expansion is disabled or the maximum height is reached at 240px, corresponding to about 10 lines of text, an internal scrollbar appears allowing the user to scroll through the overflowing text.
This choice prevents breaking the layout but has the drawback, on mobile, of creating a scroll within a scroll (text area scroll inside a page scroll).

**⚠️ No manual resize (by the user)**  
On both desktop and mobile, we have chosen to disable manual resizing to avoid behaviors inconsistent with the design system.

---

### Character counter

**Character limit not exceeded**  
The character counter, located in the helper text area, displays in real time (with each keystroke) the number of characters the user can still enter before reaching the field's allowed limit.

**⚠️** It is impossible to provide a recommendation for the maximum number of characters, as this depends too specifically on the constraints (or lack thereof) of each project.

**Character limit exceeded**  
If the user exceeds the set limit, the field enters an error state, but input is not blocked. The character counter then shows the user, still in real time, how many characters have been entered beyond the field's allowed limit.

The user must reduce the number of characters entered for the text area to exit the error state.

## Best Practices (paired Do & Don't; max 4 pairs)
- **Do:** Use helper text to clarify expected input format or character limits.  
  **Don't:** Rely solely on placeholders for essential instructions; they disappear on input.

- **Do:** Display error messages that explain what went wrong and how to fix it.  
  **Don't:** Show generic error messages or block input entirely when validation fails.

- **Do:** Set appropriate character limits and display a real-time counter.  
  **Don't:** Allow the field to enter error state without informing the user of remaining characters.

- **Do:** Use labels to clearly identify the purpose of the text area for all users.  
  **Don't:** Hide labels unless the context is unambiguous and screen readers have alternative text.

# Accessibility
## Keyboard
- **Tab**: Moves focus into and out of the text area.
- **Enter**: Creates a new line within the text area.
- **Shift + Tab**: Moves focus backwards to the previous focusable element.
- **Esc**: (if applicable) Cancels editing or clears focus in modal contexts.

## Semantics
- Use `<textarea>` or `role="textbox"` with `aria-multiline="true"`.
- Associate labels via `<label for="id">` or `aria-labelledby`.
- Mark required fields with `aria-required="true"`.
- Indicate errors with `aria-invalid="true"` and `aria-describedby` pointing to error message ID.
- Announce character limits via `aria-describedby` or live regions.

## Focus & States
- Visible focus indicator with at least 3:1 contrast against adjacent colours.
- Error states conveyed via text and icon; not colour alone.
- Focus moves to the first error field on validation failure.

## Visual & Touch
- Text contrast at least 4.5:1 for normal text; 3:1 for large text (18pt+).
- Touch targets at least 44×44 px on mobile for tappable areas.
- Ensure error messages and helper text meet contrast requirements.

## Announcements
- On validation errors, move focus to the first invalid field and announce the error via `aria-live="assertive"` if focus does not move automatically.
- Character counter updates should use `aria-live="polite"` to avoid excessive interruptions.

## Assumptions & Gaps
- Default values for editable text properties (✏️ Label, ✏️ Placeholder, ✏️ Input text, ✏️ Helper text, ✏️ Error empty text, ✏️ Error filled text) are project-specific and not defined in the properties file.

## References
- Figma: https://www.figma.com/design/QtOWrH1m3RHOAkfyy0XFil/-OUDS-Lib--Components?node-id=66833-22057&t=kYliZr7uDSxt7IKA-4
- Source of truth for properties: text_area_properties.md