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

**Feedback and comment forms**  
Text areas are commonly used in feedback forms, survey responses, and comment sections where users need to provide detailed opinions or explanations.

**Message composition**  
Used in messaging interfaces, email clients, and chat applications where users compose multi-line messages with character limits.

**Profile and settings descriptions**  
Applied in user profile pages and account settings where users enter biographical information, company descriptions, or extended personal details.

---

## Screen Variants

**Desktop**  
Text areas display with a default height of 72px (3 lines) and auto-expand up to 240px (10 lines) with clear visual indicators and ample space for helper text and character counts.

**Tablet**  
Similar behavior to desktop with adjusted touch targets and slightly modified spacing to accommodate touch interactions while maintaining readability.

**Mobile**  
Maintains the same height constraints but requires careful consideration of the scroll-within-scroll behavior when internal scrolling is active within the page scroll.

---