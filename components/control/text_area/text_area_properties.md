# Properties

## Text area

| property name | type |
|--------------|------|
| Outlined | 'False' \| 'True' |
| Rounded corner | 'False' \| 'True' |
| Input status | 'Empty' \| 'Empty (Placeholder)' \| 'Filled' |
| State | 'Enabled' \| 'Hover' \| 'Focus' \| 'Loading' \| 'Read only' \| 'Disabled' \| 'Skeleton' |
| Error | 'False' \| 'True' |
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

---

### Outlined

`**False**` An input with a subtle background fill and un visible bottom border, creating a softer and more contained look. Best suited for dense layouts or to enhance visibility.

`**True**` A minimalist input with a transparent background and a visible stroke outlining the field. This style may be interesting for contexts other than form pages:
- When inputs need to feel lightweight and unobtrusive
- In a header (search field)
- In a selection/filtering feature in a product catalog

---

### Rounded corner

`**False**` For a square finish.

`**True**` For a finish with rounded corner. To be favored in more emotional, immersive contexts or those tied to specific visual identities. For standard or business-oriented journeys, keep the default corners. This evolution addresses the need for flexibility in adapting the design to certain brand contexts.

---

### Input status

`**Empty**` The Empty state indicates that the text area is blank with no content or placeholder, a neutral starting point.

`**Empty (Placeholder)**` The Empty with Placeholder state provides a hint or guidance inside the field to suggest expected input.

`**Filled**` The Filled state shows that the user has entered valid content into the field, replacing any placeholder.

---

### State

`**Enabled**` Neutral appearance, whether empty or filled. It allows users to click, focus, and type freely without restrictions.

`**Hover**` Slight visual contrast or border color change.

`**Focus**` The text area is focused and ready to receive user input. It visually highlights the field to indicate that it's currently editable and interactive. This state typically appears after a user clicks or taps into the field.

`**Loading**` The Loading state indicates that the system is processing or retrieving data related to the text area. A progress indicator appears to inform the user that an action is in progress. During this state, the input may be temporarily disabled to prevent further interaction.

`**Read only**` Text visible but not editable (often with a muted or different background).

`**Disabled**` The field is non-interactive and grayed out to indicate it cannot be changed. The helper text is muted.

`**Skeleton**` Improves the perceived loading time by providing a visual cue of where field will appear once fully loaded. Uses the "Skeleton" component, variant "Security marge=False".

---

### Error

The Error status indicates that the user input does not meet validation rules, for example, in this specific case, if the number of characters entered by the user exceeds the allowed limit. It provides immediate visual feedback, typically through a red border, error icon, and a clear, accessible error message positioned below the input.

This state helps users quickly identify and correct mistakes by explaining what went wrong and, when possible, how to fix it. The input remains editable, encouraging users to revise their input without starting over.

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

### Scrolled

When the text area content exceeds the visible height, a vertical scrollbar appears to allow users to navigate through the text. The scrolled state provides clear feedback that additional content is available beyond what is immediately visible.

---

### Helper text

Helper text provides additional guidance, context, or instructions to help users understand what information is expected in the text area. It appears below the input field and is typically used to:
- Clarify the format or type of information required
- Provide examples
- Explain any constraints or limitations

---

### Helper link

A helper link is an actionable text element positioned below the text area that provides users with access to additional information, external resources, or related actions. Unlike helper text, which is purely informational, a helper link is interactive and allows users to navigate to another page, open a modal, or trigger a specific action.

---

### Behavior for content lines

The text area component adapts its height behavior based on the amount of content entered:

**1. Fixed height < 3 lines**
For inputs with minimal content (up to 3 lines), the text area maintains a fixed height, providing a compact and consistent layout.

**2. Auto-expansion from 4 to 10 lines**
When the content grows beyond 3 lines, the text area automatically expands to accommodate up to 10 lines. This progressive expansion ensures that users can see their input without needing to scroll, maintaining readability and a smooth user experience.

**3. Internal scroll > 10 lines**
Once the content exceeds 10 lines, the text area stops expanding and activates an internal scroll. This prevents the component from occupying excessive vertical space while still allowing users to navigate through their text comfortably.

---

### Additional considerations

**Characters remaining / Characters too many**

The component can display character count feedback to help users stay within defined limits:
- **Characters remaining**: Shows how many characters are still available before reaching the maximum limit
- **Characters too many**: Indicates when the user has exceeded the allowed character count, typically triggering an error state