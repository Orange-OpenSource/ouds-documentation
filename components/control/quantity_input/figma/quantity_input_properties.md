# Quantity Input - Definition & Properties

---

### Definition

A quantity input is a form component that allows users to specify a numerical value representing a quantity, often used in contexts like shopping carts, inventory management, or booking systems. It typically combines a numeric text field with increment and decrement controls (such as "+" and "–" buttons) to make adjustments easy and precise. The component must enforce valid input ranges (minimum of 1), prevent invalid characters, and support keyboard input, stepper controls, and assistive technologies.

---

### Properties

| property name | type |
|---------------|------|
| Outlined | 'False' \| 'True' |
| Rounded corner | 'False' \| 'True' |
| Actions placement | 'Trailing' \| 'Split' |
| Input status | 'Empty' \| 'Empty (Placeholder)' \| 'Filled' |
| State | 'Enabled' \| 'Hover' \| 'Focus' \| 'Loading' \| 'Read only' \| 'Disabled' \| 'Skeleton' |
| Error | 'False' \| 'True' |
| Leading icon | 'False' \| 'True' |
| ⚠️ Label | boolean |
| ✏️ Label | text |
| ✏️ Placeholder | text |
| ✏️ Input text | text |
| Suffix | boolean |
| Helper text | boolean |
| ✏️ Helper text | text |
| ✏️ Error empty text | text |
| ✏️ Error filled text | text |

---

### Initial settings

**Outlined** Off

**Rounded corner** Off

**Actions placement** Trailing

**Input status** Empty

**State** Enabled

**Error** Off

**Leading icon** Off

**⚠️ Label** On

**Suffix** Off

**Helper text** Off

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

**`Empty`** The Empty state indicates that the quantity input is blank with no content or placeholder, a neutral starting point.

**`Empty (Placeholder)`** The Empty with Placeholder state provides a hint or guidance inside the field to suggest expected input.

**`Filled`** The Filled state shows that the user has entered valid content into the field, replacing any placeholder.

---

### Actions placement

**`Trailing`** It places both the increment and decrement buttons on the right side of the input field, either stacked vertically or positioned side by side. This layout is compact and visually streamlined, making it ideal for dense interfaces or mobile views.

**`Split`** It positions the decrement button to the left of the input and the increment button to the right. It provides a more balanced and intuitive interaction model, especially in use cases like e-commerce where users frequently adjust quantities.

---

### State

**`Enabled`** Neutral appearance, whether empty or filled. It allows users to click, focus, and type freely without restrictions.

**`Hover`** Slight visual contrast or border color change.

**`Focus`** The quantity input is focused and ready to receive user input. It visually highlights the field to indicate that it's currently editable and interactive. This state typically appears after a user clicks or taps into the field.

**`Loading`** The Loading state indicates that the system is processing or retrieving data related to the quantity input. A progress indicator appears to inform the user that an action is in progress. During this state, the input may be temporarily disabled to prevent further interaction.

**`Read only`** Text visible but not editable (often with a muted or different background).

**`Disabled`** The field is non-interactive and grayed out to indicate it cannot be changed. The helper text is muted.

**`Skeleton`** Improves the perceived loading time by providing a visual cue of where field will appear once fully loaded. Uses the "Skeleton" component, variant "Security marge=False".

---

### Error

The Error status indicates that the user input does not meet validation rules or expected formatting. It provides immediate visual feedback, typically through a red border, error icon, and a clear, accessible error message positioned below the input (mandatory).

This state helps users quickly identify and correct mistakes by explaining what went wrong and, when possible, how to fix it. The input remains editable, encouraging users to revise their input without starting over.

If the input is filled, an "error" status is triggered by the entry of a value that is too small, too large, or non-numeric.

**⚠️ Error message vs helper text** The error message is not the same element as the helper text, it is independent. If a helper text accompanies the text input, it is replaced by the error message. The helper text must not be displayed simultaneously.

---

### Leading icon

Helps indicate the purpose of the input (magnifying glass for search, envelope for email, phone device for phone number). Only use a leading icon if it adds clear functional or contextual value.

---

### Suffix and Helper text

**Suffix** An element placed after the user's input, often used to display a currency or a unit (kg, %, cm…).

**Helper text** Supporting text conveys additional information about the input field, such as how it will be used. It should ideally only take up a single line, though may wrap to multiple lines if required, and be either persistently visible or visible only on focus.

---
