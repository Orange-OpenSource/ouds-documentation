# Guideline

## Intro

Multi-line text area that allows users to enter detailed text like comments or feedback, with features for character limits, auto-expansion, and error validation.

---

## Definition

A text area is a multi-line text area component that allows users to enter and edit longer blocks of text, such as comments, messages, or descriptions. Unlike a standard text area, which is limited to a single line, the text area can expand vertically and offers more space for content entry.

It typically includes features like a visible label, placeholder text, character limits, and optional resize behavior. The text area is ideal for open-ended responses where users need to express detailed information.

---

## Best for

✅ Open-ended feedback collection requiring detailed responses

✅ Comment sections where multi-line explanations are expected

✅ Description fields in forms that need more than a single sentence

✅ Message composition requiring multiple paragraphs

✅ Long-form content entry like reviews or testimonials

✅ Support ticket submissions with detailed issue descriptions

✅ Notes or additional information fields in applications

✅ Text editing where users need to see multiple lines simultaneously

✅ Content requiring character limits with real-time counter feedback

✅ Mobile contexts where expandable fields improve usability

---

## Anatomy

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Label | Identifies the purpose of the text area for users | N |
| 2 | Input container | Multi-line text entry field with auto-resize capability | N |
| 3 | Placeholder text | Provides guidance on expected input format or content | Y |
| 4 | Helper text | Offers additional context or instructions for completion | Y |
| 5 | Helper link | Provides access to detailed help or external guidance | Y |
| 6 | Character counter | Shows remaining or exceeded character count in real-time | Y |
| 7 | Error message | Displays validation feedback when input rules are violated | Y |
| 8 | Trailing container | Holds loading indicator or action buttons when needed | Y |

---

## Outlined

**`False`** An input with a subtle background fill and un visible bottom border, creating a softer and more contained look. Best suited for dense layouts or to enhance visibility.

**`True`** A minimalist input with a transparent background and a visible stroke outlining the field. This style may be interesting for contexts other than form pages:
• When inputs need to feel lightweight and unobtrusive
• In a header (search field)
• In a selection/filtering feature in a product catalog

**Do & don'ts**

✅ **Do:** Use filled text areas in dense forms where multiple fields need clear visual separation and containment

❌ **Don't:** Mix outlined and filled styles within the same form context as it creates visual inconsistency

✅ **Do:** Choose outlined text areas for lightweight contexts like search fields or filtering interfaces where minimal visual weight is desired

❌ **Don't:** Use outlined text areas on backgrounds with poor contrast as the stroke may become difficult to perceive

✅ **Do:** Consider the overall page hierarchy when selecting outlined versus filled, ensuring text areas don't compete with primary actions

❌ **Don't:** Apply outlined style to all text areas by default without considering the specific use case and surrounding interface elements

✅ **Do:** Use filled text areas when the field needs to stand out as an important data collection point

❌ **Don't:** Switch between styles inconsistently across your application, as users expect predictable patterns

✅ **Do:** Test both styles with your target users to determine which provides better usability in your specific context

❌ **Don't:** Assume outlined text areas are always more modern or better; filled variants often provide clearer affordance for interaction

---

## Input status

**`Empty`** The Empty state indicates that the text area is blank with no content or placeholder, a neutral starting point.

**`Empty (Placeholder)`** The Empty with Placeholder state provides a hint or guidance inside the field to suggest expected input.

**`Filled`** The Filled state shows that the user has entered valid content into the field, replacing any placeholder.

**Do & don'ts**

✅ **Do:** Provide clear placeholder text that demonstrates the expected format or gives a concrete example

❌ **Don't:** Use placeholder text as a replacement for labels, as it disappears when users begin typing

✅ **Do:** Keep placeholder text concise and specific to help users understand what to enter without overwhelming them

❌ **Don't:** Leave text areas in the empty state without any guidance if the expected input isn't immediately obvious

✅ **Do:** Ensure placeholder text has sufficient contrast (at least 4.5:1) while still being distinguishable from entered text

❌ **Don't:** Include critical instructions only in placeholder text, as it's not accessible to all users and disappears during interaction

✅ **Do:** Use the filled state to provide clear visual feedback that user input has been successfully captured

❌ **Don't:** Rely solely on filled state to indicate valid input; combine with other feedback mechanisms for complex validation

✅ **Do:** Consider progressive disclosure where empty fields show just enough information to get started

❌ **Don't:** Make placeholder text so verbose that it becomes distracting or reduces the perceived simplicity of the form

---

## Error

The Error status indicates that the user input does not meet validation rules, for example, in this specific case, if the number of characters entered by the user exceeds the allowed limit. It provides immediate visual feedback, typically through a red border, error icon, and a clear, accessible error message positioned below the input (mandatory).

This state helps users quickly identify and correct mistakes by explaining what went wrong and, when possible, how to fix it. The input remains editable, encouraging users to revise their input without starting over.

**⚠️ Error message vs helper text / link** If a helper text accompanies the text input, it is replaced by the error message. However, a helper link must not be replaced and should remain positioned below the error message.

**Do & don'ts**

✅ **Do:** Display error messages immediately adjacent to the text area with clear visual indicators like red borders and error icons

❌ **Don't:** Show errors while users are still typing; wait for field blur or form submission to avoid premature interruption

✅ **Do:** Write error messages that explain what went wrong and provide specific guidance on how to fix it

❌ **Don't:** Use technical jargon or error codes in messages; keep language plain and user-friendly

✅ **Do:** Ensure error messages are programmatically associated with the text area using `aria-describedby` for screen reader accessibility

❌ **Don't:** Disable or remove the text area when displaying errors; users must be able to correct their input

✅ **Do:** Combine visual error indicators (color, icons) with text to support users who cannot perceive color alone

❌ **Don't:** Replace helper text permanently with error messages; restore helper text when the error is resolved

✅ **Do:** Keep error messages concise and actionable, focusing on what users need to do next

❌ **Don't:** Display multiple error messages simultaneously if they can be consolidated into a single, clear instruction

✅ **Do:** Maintain error states until users have successfully corrected the input and validation passes

❌ **Don't:** Clear error messages prematurely before users have had a chance to address the issue

---

## ⚠️ Label

Describes the purpose of the input. Why hide a text area label?

In some UI contexts, especially when space is limited or when the input is part of a compact layout (search bars, filters, inline forms), visually hiding the label can help maintain a clean and uncluttered interface.

However, hiding the label should only be done if:
• The purpose of the input remains clear thanks to a placeholder or contextual icon.
• The label is still accessible to screen readers (using aria-label, aria-labelledby, or visually hidden text).

Hiding a label is a design choice that must balance visual simplicity and clarity of intent, without compromising inclusiveness or form guidance.

**Do & don'ts**

✅ **Do:** Always provide a label for every text area, making it visible by default for maximum accessibility and usability

❌ **Don't:** Hide labels unless there's a compelling reason and you can guarantee the purpose remains absolutely clear to all users

✅ **Do:** Position labels above text areas rather than to the side, as top-aligned labels work better with longer text and responsive layouts

❌ **Don't:** Use placeholder text as a substitute for labels, as placeholders are not accessible to all users and disappear during interaction

✅ **Do:** Keep labels short, direct, and written in sentence case without punctuation at the end

❌ **Don't:** Use vague labels like "Comments" when more specific labels like "Additional details about your request" would be clearer

✅ **Do:** When hiding labels visually, ensure they remain accessible using `aria-label`, `aria-labelledby`, or visually-hidden CSS techniques

❌ **Don't:** Rely solely on icons or context to convey the purpose of a text area without providing an accessible label

✅ **Do:** Align labels consistently across your form to create a predictable and scannable layout

❌ **Don't:** Add colons or other punctuation after labels, as modern design systems favor cleaner label presentation

✅ **Do:** Ensure labels are visually and programmatically associated with their corresponding text areas

❌ **Don't:** Place labels far from their text areas, as this makes forms harder to complete and increases cognitive load

---

## Other boolean options

**Scrolled** Represents the state in which the field contains more text than its visible height can display and that internal scrolling is available. This allows users to navigate through the overflowing text without expanding the text area beyond **the maximum planned height of 240px, allowing the display of about 10 lines of text**. It is particularly useful when preserving space is important, or when the text area is embedded within a fixed-height container.

**Helper text** Supporting text conveys additional information about the input field, such as how it will be used. It should ideally only take up a single line, though may wrap to multiple lines if required, and be either persistently visible or visible only on focus.

**Helper link** If the helper text is not sufficient (It can also be displayed on its own without helper text), it's possible to offer the user an additional help link (the link can be external or open a modal).

**Do & don'ts**

✅ **Do:** Set a maximum height for text areas to prevent them from dominating the layout, using scrolling for overflow content

❌ **Don't:** Allow text areas to expand infinitely without constraint, as this disrupts page layout and creates poor mobile experiences

✅ **Do:** Use helper text to provide concise, actionable guidance that helps users understand what to enter

❌ **Don't:** Make helper text longer than 1-2 lines, as lengthy instructions reduce scannability and increase cognitive burden

✅ **Do:** Position helper text directly below the text area where users naturally look for additional context

❌ **Don't:** Place helper text above the text area or far from it, as this breaks the visual flow and reduces discoverability

✅ **Do:** Use helper links sparingly for detailed instructions that would overwhelm inline helper text

❌ **Don't:** Include links within helper text without clear indication, as screen readers may not announce them as interactive

✅ **Do:** Ensure scrolled text areas have sufficient contrast on scrollbars and clear visual indicators of scrollable content

❌ **Don't:** Hide scrollbars entirely, as users need visual confirmation that more content exists below

✅ **Do:** Test scrolling behavior on mobile devices to avoid nested scrolling issues where possible

❌ **Don't:** Create scroll-within-scroll situations on mobile, as they cause frustration and usability problems

✅ **Do:** Make helper text and helper links accessible via screen readers using proper semantic markup

❌ **Don't:** Convey critical information only through helper links, as users may miss or skip them

✅ **Do:** Display helper text persistently rather than only on focus, ensuring it's available when users need it most

❌ **Don't:** Rely on hover-only tooltips for essential information, as they're not accessible on touch devices or to keyboard users

---

## Behavior by entered line count

• **Default display**
By default, the height of **the input text container is set to 72px, which allows 3 lines of text** to be displayed without expanding the component. This height helps distinguish the field from other text inputs, prevents discouraging users with an overly large field, and keeps the layout compact at the start of a form.

• **Auto-resize (automatic expansion)**
Above 3 lines of text, the field automatically increases in height as the user types their comment.

• **Vertical scrollbar**
If expansion is disabled or **the maximum height is reached at 240px, corresponding to about 10 lines of text**, an internal scrollbar appears allowing the user to scroll through the overflowing text. This choice prevents breaking the layout but has the drawback, on mobile, of creating a scroll within a scroll (text area scroll inside a page scroll).

**⚠️ No manual resize (by the user)**
On both desktop and mobile, we have chosen to disable manual resizing to avoid behaviors inconsistent with the design system.

**Do & don'ts**

✅ **Do:** Start with a reasonable default height (3 lines) that signals multi-line input without overwhelming users

❌ **Don't:** Show a single-line height initially, as it fails to communicate that multi-line input is expected

✅ **Do:** Allow text areas to auto-expand as users type to show all content without requiring scrolling for most use cases

❌ **Don't:** Force users to scroll within small text areas when auto-expansion would provide a better experience

✅ **Do:** Set a maximum height to prevent text areas from consuming excessive screen space in long-form inputs

❌ **Don't:** Allow unlimited expansion on small screens, as it makes navigation and form completion difficult

✅ **Do:** Disable manual resize handles to maintain consistent layout and prevent users from breaking the design

❌ **Don't:** Allow users to resize text areas arbitrarily, especially on mobile, as it causes layout problems

✅ **Do:** Test auto-resize behavior across different devices to ensure smooth transitions without layout shifts

❌ **Don't:** Create jarring resize animations that distract users or cause content to jump unexpectedly

✅ **Do:** Provide clear visual feedback when maximum height is reached and scrolling becomes necessary

❌ **Don't:** Hide the fact that content has been truncated; make scrollability obvious with visible scrollbars

✅ **Do:** Consider the typical length of expected responses when setting default and maximum heights

❌ **Don't:** Use the same height settings for all text areas regardless of their purpose or expected content length

✅ **Do:** Ensure auto-resize respects container boundaries and doesn't break parent layout constraints

❌ **Don't:** Allow text areas to overflow their containers or overlap with adjacent content during expansion

---

## Character counter

• **Character limit not exceeded**
The character counter, located in the helper text area, displays in real time (with each keystroke) the number of characters the user can still enter before reaching the field's allowed limit.

⚠️ It is impossible to provide a recommendation for the maximum number of characters, as this depends too specifically on the constraints (or lack thereof) of each project.

• **Character limit exceeded**
If the user exceeds the set limit, the field enters an error state, but input is not blocked. The character counter then shows the user, still in real time, how many characters have been entered beyond the field's allowed limit.

The user must reduce the number of characters entered for the text area to exit the error state.

**Do & don'ts**

✅ **Do:** Display character counters in real-time to give users immediate feedback on remaining capacity

❌ **Don't:** Wait until form submission to inform users they've exceeded character limits

✅ **Do:** Position character counters in the helper text area where users naturally look for field-related information

❌ **Don't:** Place character counters in locations that are hard to notice or that interrupt the typing flow

✅ **Do:** Show "X characters remaining" format to help users gauge how much more they can write

❌ **Don't:** Only show total character count without indicating the limit, forcing users to do mental math

✅ **Do:** Transition to error state when limits are exceeded, using clear visual indicators like color change

❌ **Don't:** Block user input when the limit is reached; allow typing and show the overflow amount instead

✅ **Do:** Use clear, accessible language in character counters like "15 characters remaining" rather than just numbers

❌ **Don't:** Rely solely on color to communicate limit status; include text and icons for accessibility

✅ **Do:** Set character limits based on actual content requirements and database constraints, not arbitrary numbers

❌ **Don't:** Use unnecessarily restrictive character limits that frustrate users trying to provide complete information

✅ **Do:** Update character counter announcements for screen readers using ARIA live regions

❌ **Don't:** Make character counter changes completely silent to assistive technology users

✅ **Do:** Allow users to see and edit content that exceeds the limit so they can make informed decisions about what to cut

❌ **Don't:** Truncate or delete user content automatically when limits are exceeded

---

# Specs

## States

**`Enabled`** Neutral appearance, whether empty or filled. It allows users to click, focus, and type freely without restrictions.

**`Hover`** Slight visual contrast or border color change.

**`Focus`** The text area is focused and ready to receive user input. It visually highlights the field to indicate that it's currently editable and interactive. This state typically appears after a user clicks or taps into the field.

**`Loading`** The Loading state indicates that the system is processing or retrieving data related to the text area. A progress indicator appears to inform the user that an action is in progress. During this state, the input may be temporarily disabled to prevent further interaction.

**`Read only`** Text visible but not editable (often with a muted or different background).

**`Disabled`** The field is non-interactive and grayed out to indicate it cannot be changed. The helper text is muted.

**`Skeleton`** Improves the perceived loading time by providing a visual cue of where field will appear once fully loaded. Uses the "Skeleton" component, variant "Security marge=False".

---

## Layout and spacing

🚧 Content to be added

---

# Accessibility

## Accessibility intro

Text areas must comply with WCAG 2.2 Level AA standards to ensure all users can enter multi-line text regardless of ability. For comprehensive accessibility guidance, see the [Orange Unified Design System Accessibility Overview](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability).

---

## Accessibility Challenges

Text areas present unique accessibility challenges due to their multi-line nature, dynamic character counting, auto-resize behaviors, and complex validation states. Unlike single-line inputs, text areas must communicate content length, scrollability, and overflow conditions to all users. Screen reader users need clear indication of character limits, current count, and error states without overwhelming them with excessive announcements. Keyboard users require predictable navigation patterns, especially when text areas expand or trigger validation. The combination of labels, helper text, character counters, and error messages must be properly associated and announced in a logical sequence.

### Key Challenges
- Character counters updating in real-time must announce changes without overwhelming screen reader users
- Auto-resize behavior can cause unexpected focus and scroll position changes that disorient users
- Error states with exceeded character limits must be communicated clearly without blocking input
- Scrollable content within text areas creates nested scrolling challenges on mobile devices

### Critical Success Factors
1. **Clear structure**: Proper semantic HTML with associated labels, described-by relationships linking to helper text, character counters, and error messages (WCAG 3.3.2, 4.1.2)
2. **Visible focus indicators**: High-contrast focus outlines (≥3:1) that remain visible throughout interaction (WCAG 2.4.7)
3. **Real-time feedback**: Polite ARIA live regions for character counter updates that don't interrupt user flow (WCAG 4.1.3)
4. **Keyboard accessibility**: Full keyboard operability including Tab navigation, arrow keys for text editing, and Escape to exit without submission (WCAG 2.1.1)

---

## Design Requirements

### Structure & Labels
- [ ] **Visible labels required**: Every text area must have a permanently visible label positioned above the field, not just placeholder text ([Orange Forms Guidelines](https://a11y-guidelines.orange.com/en/web/develop/forms/))
- [ ] **Programmatic association**: Use `<label for="id">` pointing to text area's `id` attribute to create proper association for assistive technology
- [ ] **Helper text association**: Connect helper text using `aria-describedby` to ensure screen readers announce it when the field receives focus

### Visual Design
- [ ] **Focus indicators**: Provide visible focus state with ≥3:1 contrast ratio against adjacent colors, never remove or hide focus outlines ([WCAG 2.4.7](https://www.w3.org/WAI/WCAG22/Understanding/focus-visible))
- [ ] **Color contrast**: Ensure text and borders meet 4.5:1 for normal text, 3:1 for large text and UI components ([WCAG 1.4.3, 1.4.11](https://a11y-guidelines.orange.com/en/web/develop/forms/))
- [ ] **Clear boundaries**: Text area borders must be clearly visible with sufficient contrast to indicate the input region

### Content
- [ ] **Descriptive labels**: ❌ "Comments" / ✅ "Please describe the issue you experienced" ([Orange Forms Best Practices](https://a11y-guidelines.orange.com/en/web/develop/forms/))
- [ ] **Clear error messages**: Explain what went wrong and how to fix it without technical jargon, programmatically associated via `aria-describedby`

---

## Testing Checklist

### Screen Reader Testing
- [ ] Test with NVDA (Windows), JAWS (Windows), VoiceOver (macOS/iOS), TalkBack (Android)
- [ ] Verify label announced first, then helper text, current character count (if applicable), then field role and current value

### Keyboard Testing
- [ ] Tab focuses text area, Shift+Tab moves backwards, all functionality keyboard-accessible
- [ ] Focus indicator visible with ≥3:1 contrast throughout interaction, arrow keys navigate within text
- [ ] Enter key creates new lines within text area without submitting form, Escape exits field without clearing content

### Character Counter Testing
- [ ] Character counter updates appear in helper text region and announce via ARIA live region without interrupting typing
- [ ] Error state triggered when limit exceeded, communicated via visual indicators and screen reader announcement

Resources: [Orange Accessibility Testing Methods](https://a11y-guidelines.orange.com/en/web/test/)

---

## Key WCAG Criteria

- **2.1.1 Keyboard** (A): All text area functionality including focus, text entry, character counting, and error recovery operable via keyboard
- **2.4.7 Focus Visible** (AA): Visible focus indicator with ≥3:1 contrast when text area receives keyboard focus
- **3.3.1 Error Identification** (A): Character limit errors identified in text and associated with text area via `aria-describedby`
- **3.3.2 Labels or Instructions** (A): Labels provided for text areas with helper text for complex requirements, both accessible to assistive technology
- **4.1.2 Name, Role, Value** (A): Semantic `<textarea>` element with proper label association, helper text via `aria-describedby`, error state via `aria-invalid`, character counter updates via ARIA live regions

For complete reference: [Orange Accessibility Guidelines - Form Components](https://a11y-guidelines.orange.com/en/web/components-examples/)

---

## Additional Resources

- [Orange Accessibility Guidelines - Forms Development](https://a11y-guidelines.orange.com/en/web/develop/forms/)
- [WCAG 2.2 Understanding - Success Criterion 3.3.2 Labels or Instructions](https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions)
- [Orange Unified Design System - Accessibility & Sustainability](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability)
- [WAI-ARIA Authoring Practices - Text Area Pattern](https://www.w3.org/WAI/ARIA/apg/)
- [Orange Guidelines - Disabling HTML Elements Accessibly](https://a11y-guidelines.orange.com/en/articles/disable-elements/)

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Nov 10, 2025 | 1.2.0 | • Scope: Trailing action=False / State=Loading → Replacement of the button component (loading state) with a "Trailing container" frame containing the circular progress indicator component | Maxime Tonnerre |
| Sep 30, 2025 | 1.1.0 | • The name of the "Style" variant has been replaced to "Outlined" with true/false variant | Hamza Amarir |
| Jun 30, 2025 | 1.0.0 | • Component creation | Maxime Tonnerre |

---
