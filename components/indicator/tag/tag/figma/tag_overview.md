## Definition

A tag is a small element that shows short info like a label, keyword, or category.
It helps users quickly find, group, or understand content.

---

## States

Even though the Tag component is not interactive, it still includes several display states. This allows it to be flexible in different scenarios and ensures the user always sees the right visual feedback. The component supports four states: Enabled, Loading, Disabled, and Skeleton.

**`Enabled`** The default state of the tag, used to display the main information or status.

Use case:
• Displaying a ready status or category (e.g., Shipped, Active, New).

**`Loading`** A state where the tag shows a loader together with text.

Use case:
• Displaying status before API data is available. For example, while the system fetches the real value, the tag shows "Loading".
• Data updates or filtering. When a table or list is being updated (e.g., applying filters or refreshing data), the tag temporarily shows loading and is then replaced with the actual value.

**`Disabled`** A non-active state of the tag. It appears "dimmed" to indicate that it is unavailable or not relevant.

Use case:
• Used when a status is no longer valid (e.g., an order is canceled and the tag is no longer meaningful).
• When the tag is part of a status system but currently has no value to display.

**`Skeleton`** A placeholder state shown before the actual data is loaded.

Use case:
• Used to display the structure of the interface while waiting for data.
• Helps avoid abrupt interface changes and provides a smoother experience.

---

## Status

Tags have status depending on the context of the information they represent. Each state is designed to convey a specific meaning and ensure clarity in communication.

**Non fonctionnel**
Non-functional tags are used to display categories, default states, or to draw attention without carrying a specific functional meaning (unlike functional tags such as success, info, warning, and error).
Icons related to the tag's context can be used to enhance recognition.

**`Neutral`** Default or inactive state. Used for standard labels, categories, or when no specific status needs to be communicated.

**`Accent`** Used to draw attention to new features, recommendations, or content suggestions. Invites users to explore and engage with new offerings, creating an exciting and engaging experience.

**Fonctional**
Functional tags communicate specific statuses or system feedback (e.g., success, warning, error, information). Each tag must always be paired with its dedicated functional icon that matches the meaning of the tag.
**Other icons must not be used.**

**`Positive`** Indicates a successful or confirmed status, such as completed tasks or active states.
Always use the functional icon associated with success. ""

**`Warning`** Signals potential issues or actions that require user attention. Use with caution.
Always use the functional icon associated with warning. ""

**`Negative`** Communicates errors, failed actions, or negative outcomes.
Always use the functional icon associated with error. ""

**`Info`** Represents informational content, tips, or supportive context.
Always use the functional icon associated with information. ""

---

## Appearance

**`Muted`** A tag with a subtle, light, or semi-transparent background. Used for secondary or less prominent information. Muted tags blend more with the background, providing a softer visual emphasis compared to emphasized tags.

**`Emphasized`** A tag with a solid, high-contrast background. Used to draw strong attention to important labels or categories. Emphasized tags stand out prominently against the interface and are ideal for primary or high-priority information.

---

## Layouts

**`Text only`** A tag that displays only text. Used for simple labels, categories, or keywords without additional visual elements.

**`Text + Bullet`** A tag with a small indicator (bullet) alongside the text. Used to show status, presence, or activity next to the label.

**`Text + Icon`** A tag that includes an icon before the text. Used to visually reinforce the meaning of the tag, such as status, type, or action.

---

## Shape

**`Rounded corner=True`** A tag with fully rounded corners, creating a pill-shaped appearance. Rounded tags offer a softer and more approachable look, suitable for most modern interfaces.

**`Rounded corner=False`** A tag with sharp, square corners. Squared tags provide a more formal, structured, or technical feel. They are often used in business contexts to label promotions, offers, or important notices.

---

## Size

**`Default`** The standard tag size, using bold text to ensure strong visibility and readability.
Commonly used for promotional content, highlights, or key information, where emphasis and clarity are important.

**`Small`** A compact tag with medium text, designed for tables or complex components where space efficiency matters.
It helps maintain visual balance and prevents the interface from feeling overloaded with bold text.

---
