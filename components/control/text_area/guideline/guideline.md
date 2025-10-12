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