# Guideline

## Intro 👈🤖 

A text area allows users to enter multi-line text content like comments or descriptions with expandable height and character counting.

---

## What is it

A text area is a multi-line text area component that allows users to enter and edit longer blocks of text, such as comments, messages, or descriptions. Unlike a standard text area, which is limited to a single line, the text area can expand vertically and offers more space for content entry.

It typically includes features like a visible label, placeholder text, character limits, and optional resize behavior. The text area is ideal for open-ended responses where users need to express detailed information.

---

## Anatomy 👈🤖

| # | Element | Purpose |
|---|---------|---------|
| 1 | Label | Describes the purpose of the text area input |
| 2 | Input container | Multi-line text entry field with expandable height |
| 3 | Placeholder text | Provides hint or guidance about expected input |
| 4 | Character counter | Displays remaining/exceeded characters in real-time |
| 5 | Helper text | Supporting information about input requirements |
| 6 | Helper link | Optional link to additional help or guidance |
| 7 | Error message | Explains validation errors when limits are exceeded |
| 8 | Scrollbar | Appears when content exceeds maximum height |

---

## Usage & Guidance

<<<<<<< HEAD
### Best for
=======
### Best for 👈🤔
>>>>>>> 4c02f0f (content:update)

✅ Long-form feedback or comments requiring multiple sentences  
✅ Detailed descriptions of issues, problems, or requests  
✅ User-generated content like reviews, testimonials, or stories  

✅ Text content with character limits requiring real-time feedback  
✅ Forms where distinguishing multi-line from single-line inputs aids clarity  
✅ Contexts where auto-expanding fields improve user experience  
✅ Mobile interfaces where scrolling within text should be minimized

---

### ⚠️ Label

Describes the purpose of the input. Why hide a text area label?

In some UI contexts, especially when space is limited or when the input is part of a compact layout (search bars, filters, inline forms), visually hiding the label can help maintain a clean and uncluttered interface. However, hiding the label should only be done if:
• The purpose of the input remains clear thanks to a placeholder or contextual icon.
• The label is still accessible to screen readers (using aria-label, aria-labelledby, or visually hidden text).

Hiding a label is a design choice that must balance visual simplicity and clarity of intent, without compromising inclusiveness or form guidance.

---

### Behavior by entered line count

**Default display** By default, the height of the input text container is set to 72px, which allows 3 lines of text to be displayed without expanding the component. This height helps distinguish the field from other text inputs, prevents discouraging users with an overly large field, and keeps the layout compact at the start of a form.

**Auto-resize (automatic expansion)** Above 3 lines of text, the field automatically increases in height as the user types their comment.

**Vertical scrollbar** If expansion is disabled or the maximum height is reached at 240px, corresponding to about 10 lines of text, an internal scrollbar appears allowing the user to scroll through the overflowing text. This choice prevents breaking the layout but has the drawback, on mobile, of creating a scroll within a scroll (text area scroll inside a page scroll).

⚠️ **No manual resize (by the user)** On both desktop and mobile, we have chosen to disable manual resizing to avoid behaviors inconsistent with the design system.

---

### Character counter

**Character limit not exceeded** The character counter, located in the helper text area, displays in real time (with each keystroke) the number of characters the user can still enter before reaching the field's allowed limit.

⚠️ It is impossible to provide a recommendation for the maximum number of characters, as this depends too specifically on the constraints (or lack thereof) of each project.

**Character limit exceeded** If the user exceeds the set limit, the field enters an error state, but input is not blocked. The character counter then shows the user, still in real time, how many characters have been entered beyond the field's allowed limit.

The user must reduce the number of characters entered for the text area to exit the error state.

---

<<<<<<< HEAD
### Set realistic character limits based on user needs 
✅ **Do:** Analyze typical user responses and set limits that accommodate 95% of legitimate use cases without feeling restrictive  
❌ **Don't:** Impose arbitrary low limits that force users to edit natural language or remove helpful context

### Place critical guidance in the label, not just helper text
=======
### Set realistic character limits based on user needs 👈🤔

✅ **Do:** Analyze typical user responses and set limits that accommodate 95% of legitimate use cases without feeling restrictive  
❌ **Don't:** Impose arbitrary low limits that force users to edit natural language or remove helpful context

### Place critical guidance in the label, not just helper text 👈🤔
>>>>>>> 4c02f0f (content:update)

✅ **Do:** Include essential requirements directly in the label (e.g., "Describe your issue (max 500 characters)")  
❌ **Don't:** Hide character limits or important constraints only in helper text that users may overlook

<<<<<<< HEAD
### Show character count early to prevent late-stage frustration
=======
### Show character count early to prevent late-stage frustration 👈🤔
>>>>>>> 4c02f0f (content:update)

✅ **Do:** Display remaining characters from the first keystroke so users can self-regulate as they compose  
❌ **Don't:** Wait until users approach or exceed the limit to reveal counting, forcing unexpected editing

<<<<<<< HEAD
### Write error messages that guide recovery, not just state problems
=======
### Write error messages that guide recovery, not just state problems 👈🤔
>>>>>>> 4c02f0f (content:update)

✅ **Do:** Specify "Your comment exceeds the limit by 45 characters—please shorten to submit"  
❌ **Don't:** Use vague errors like "Too many characters" without indicating how many to remove

### Use helper links sparingly and only when additional context is essential 👈🤔

✅ **Do:** Link to detailed formatting guidelines, content policies, or examples when users need more than a sentence of help  
❌ **Don't:** Add helper links for information that could fit in 1-2 lines of helper text

<<<<<<< HEAD
=======
### Position text areas after contextual information in forms 👈🤔

✅ **Do:** Place shorter fields (name, email) before the text area so users gather momentum before detailed writing  
❌ **Don't:** Start forms with large text areas before users understand what information is needed or why

### Preserve user content during validation errors 👈🤔

✅ **Do:** Keep all entered text visible when showing errors so users can edit rather than rewrite  
❌ **Don't:** Clear the field or hide content on error, forcing users to start over

### Adjust height constraints based on expected response length 👈🤔

✅ **Do:** Allow 5-7 visible lines for detailed feedback forms, 3-4 for brief comments  
❌ **Don't:** Use the same small initial height for all contexts regardless of typical response length
>>>>>>> 4c02f0f (content:update)

### Provide clear indication when scrolling is available 👈🤔

✅ **Do:** Ensure scrollbars are visible on overflow and consider subtle fade indicators at text boundaries  
❌ **Don't:** Hide scrollbars completely or provide no visual cue that more content exists beyond visible area

### Differentiate text areas from single-line inputs through sizing 👈🤔

✅ **Do:** Use noticeably taller initial height (72px vs. 40-48px for text inputs) to signal multi-line entry  
❌ **Don't:** Make text areas only slightly taller, causing users to miss the distinction and attempt single-line entry

---

### How should I configure labels and helper text for a support issue text area? 👈🤔

Use a clear label like "Describe your issue" with helper text showing character remaining count (e.g., "You have 180 characters remaining") positioned below the input field.

### What should the error state look like when users exceed the character limit? 👈🤔

Display a red border around the input, show a specific error message stating "You've exceeded the limit by X characters—please shorten to submit," and update the character counter to show the overage count.

### How do I visually distinguish between empty and filled states? 👈🤔

Empty state shows placeholder text in muted color (e.g., "Describe your issue in detail"), while filled state displays user-entered text in standard content color with the placeholder removed.

### What's the visual configuration for a text area with both helper text and helper link? 👈🤔

Position character counter helper text directly below the input, followed by a blue underlined helper link (e.g., "Content guidelines") on the next line, both indented to align with the input's left edge.

### How should focus state appear on the text area? 👈🤔

Apply a prominent border color change and focus ring around the entire input container to clearly indicate the field is active and ready for input.

### What does the loading state look like when content is being processed? 👈🤔

Display a loading spinner in the trailing container area on the right side of the input field while maintaining the input's filled or empty state appearance with text visible but non-interactive.

### How do I configure a read-only text area with existing content? 👈🤔

Show filled text in standard weight with a muted background color, no focus ring on interaction, and helper text indicating the field cannot be edited.

### What's the difference between a 3-line and 10-line text area layout? 👈🤔

The 3-line version shows initial height of 72px with no scrollbar, while the 10-line version displays maximum height of 240px with vertical scrollbar appearing when content exceeds this limit.

### How should I display a text area in outlined variant for search contexts? 👈🤔

Use transparent background with visible stroke border outlining the field, placeholder text centered, and minimal padding to create a lightweight appearance suitable for headers or filter panels.

### What does disabled state look like with placeholder text? 👈🤔

Show grayed-out placeholder text, muted background, no border emphasis, and cursor changes to not-allowed to indicate the field is non-interactive.

---

## Screen Sizes

### Desktop 👈🤖

Text areas display at their configured width (typically full-width within form containers) with minimum 72px height for 3 visible lines, expanding to maximum 240px with vertical scrollbar. Helper text and links appear below with adequate spacing.

### Tablet 👈🤖

Similar to desktop layout but may reduce horizontal padding slightly within form columns. Scrollbar behavior remains consistent to prevent double-scroll conflicts in constrained viewports.

### Mobile 👈🤖

Text areas occupy full container width with maintained 72-240px height range. Character counters stack cleanly below input. Be mindful that internal scrolling combined with page scrolling can create usability challenges on smaller screens.

---

# Specs

## Properties

### Initial Config

| Property | Default Value | Notes |
|----------|---------------|-------|
| Outlined | False | Standard filled appearance with bottom border is default; true provides outlined stroke style for lightweight contexts. |
| Rounded corner | False | Square corners are default for business contexts; true adds rounded corners for emotional or brand-specific interfaces. |
| Input status | Empty | Initial state showing no content or placeholder; can also start as Empty (Placeholder) or Filled based on context. |
| State | Enabled | Standard interactive state allowing user input; other states include Hover, Focus, Loading, Read only, Disabled, Skeleton. |
| Error | False | No validation error shown initially; true triggers red border and error message display when character limit is exceeded. |
| Scrolled | False | No internal scrolling initially; true indicates content exceeds visible height and scrollbar is available. |
| ⚠️ Label | True | Label is visible by default for accessibility; can be hidden only when purpose is clear through other UI context. |
| Helper text | False | Character counter and supporting text hidden by default; enable to show remaining character count or guidance. |
| Helper link | False | Additional help link hidden by default; enable when users need access to detailed guidelines or external resources. |

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

The Error status indicates that the user input does not meet validation rules, for example, in this specific case, if the number of characters entered by the user exceeds the allowed limit. It provides immediate visual feedback, typically through a red border, error icon, and a clear, accessible error message positioned below the input (mandatory).

This state helps users quickly identify and correct mistakes by explaining what went wrong and, when possible, how to fix it. The input remains editable, encouraging users to revise their input without starting over.

**Error message vs helper text / link** If a helper text accompanies the text input, it is replaced by the error message. However, a helper link must not be replaced and should remain positioned below the error message.

---

### Other boolean options

**Scrolled** Represents the state in which the field contains more text than its visible height can display and that internal scrolling is available. This allows users to navigate through the overflowing text without expanding the text area beyond the maximum planned height of 240px, allowing the display of about 10 lines of text. It is particularly useful when preserving space is important, or when the text area is embedded within a fixed-height container.

**Helper text** Supporting text conveys additional information about the input field, such as how it will be used. It should ideally only take up a single line, though may wrap to multiple lines if required, and be either persistently visible or visible only on focus.

**Helper link** If the helper text is not sufficient (It can also be displayed on its own without helper text), it's possible to offer the user an additional help link (the link can be external or open a modal).

---

# Accessibility 👈🤖

## Accessibility intro

The Text Area component must meet WCAG 2.2 Level AA requirements to ensure users can enter, edit, and review multi-line text content regardless of ability. For comprehensive accessibility guidance, see the [Orange Unified Design System Accessibility Overview](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability).

---

## Accessibility Challenges

Text areas present unique challenges because they combine multi-line text editing with dynamic features like auto-expansion, character counting, and scrolling—all of which must remain accessible to keyboard users, screen reader users, and users with motor or cognitive impairments. The real-time character counter and error state transitions require careful ARIA implementation to keep assistive technology users informed of changes.

### Key Challenges
- **State communication**: Screen readers must announce character count changes, error states, and scrolling availability without overwhelming users with excessive updates
- **Focus management**: Multi-line editing requires clear focus indicators that remain visible as content expands and scrolls
- **Error recovery**: Users must understand not just that an error occurred, but exactly how many characters to remove and where the error message is located
- **Double-scroll conflict**: On mobile, nested scrolling (text area within page) creates confusion for screen reader and switch control users

### Critical Success Factors
1. **Proper labeling and association** (WCAG 3.3.2, 1.3.1): Labels programmatically linked via `for`/`id`, helper text and errors associated using `aria-describedby`
2. **Live region announcements** (WCAG 4.1.3): Character counter and error messages use `aria-live="polite"` so screen readers announce changes without interrupting user typing
3. **Keyboard accessibility** (WCAG 2.1.1): All functionality—entering text, scrolling content, accessing helper links—operable via keyboard alone
4. **Clear focus indication** (WCAG 2.4.7): Focus ring maintains ≥3:1 contrast ratio against background at all times, including when content scrolls

---

## Design Requirements

### Structure & Labels
- [ ] **Label association**: Every text area has a visible `<label>` element programmatically linked using `for`/`id` attributes ([Orange Forms Guidelines](https://a11y-guidelines.orange.com/en/web/components-examples/forms/))
- [ ] **Helper text linking**: Character counter and helper text associated with input using `aria-describedby` attribute referencing their IDs
- [ ] **Error message connection**: Error messages must be associated via `aria-describedby` (in addition to label/helper text IDs) and announced when error state changes

### Visual Design
- [ ] **Focus indicator**: Focus ring has ≥3:1 contrast ratio against background color and remains visible when content scrolls ([Orange Focus Visibility](https://a11y-guidelines.orange.com/en/web/design/focus/))
- [ ] **Error state contrast**: Error borders, icons, and text meet ≥3:1 contrast ratio for non-text elements, ≥4.5:1 for error message text
- [ ] **Scrollbar visibility**: Scrollbars remain visible or use sufficient contrast (≥3:1) to indicate scrollable content

### Content
- [ ] **Error specificity**: ❌ "Too many characters" / ✅ "You've exceeded the limit by 45 characters—please shorten to submit" ([Orange Error Messages](https://a11y-guidelines.orange.com/en/web/components-examples/accessible-forms/))
- [ ] **Clear instructions**: Labels and helper text use plain language explaining expected input, character limits, and formatting requirements

---

## Testing Checklist

### Screen Reader Testing
- [ ] Test with NVDA (Windows), JAWS (Windows), VoiceOver (macOS/iOS), TalkBack (Android) to verify labels announced, character count updates spoken via live region, error messages read when triggered
- [ ] Verify scrollable content announced, focus remains on text area during expansion, helper link accessible and identified as link

### Keyboard Testing
- [ ] Tab navigation enters text area, focus visible ≥3:1 contrast, Enter creates new line (not submits form), all helper links reachable via Tab, Escape closes helper modals if present
- [ ] Verify scrolling works via arrow keys when content exceeds visible area

### Paste Testing
- [ ] Paste functionality works correctly, updates character counter immediately, triggers error state if limit exceeded, announces changes to screen readers

Resources: [Orange Accessibility Testing Guide](https://a11y-guidelines.orange.com/en/web/test/)

---

## Key WCAG Criteria

- **2.1.1 Keyboard** (A): All functionality—entering text, scrolling, accessing helper links, correcting errors—operable via keyboard without timing requirements
- **2.4.7 Focus Visible** (AA): Focus indicator has ≥3:1 contrast on text area border, remains visible during content scrolling and state changes
- **3.3.1 Error Identification** (A): Character limit errors identified in text (not just color) and associated with input via `aria-describedby`
- **3.3.2 Labels or Instructions** (A): Visible labels provided for all text areas, character limits stated in label or helper text, available to assistive technology
- **4.1.2 Name, Role, Value** (A): Semantic `<textarea>` element used, character counter uses `aria-live="polite"`, error states communicated via ARIA attributes

For complete reference: [Orange Accessibility Guidelines - Form Components](https://a11y-guidelines.orange.com/en/web/components-examples/forms/)

---

## Additional Resources

- [Orange Accessibility Guidelines - Forms](https://a11y-guidelines.orange.com/en/web/components-examples/forms/)
- [Orange Accessibility Guidelines - Accessible Form Examples](https://a11y-guidelines.orange.com/en/web/components-examples/accessible-forms/)
- [WCAG 2.2 Understanding Docs - Input Assistance](https://www.w3.org/WAI/WCAG22/Understanding/input-assistance)
- [Orange Design System - Accessibility & Sustainability](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability)
- [W3C ARIA Practices - Text Area Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/textarea/)
