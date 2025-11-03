# Guideline

A multi-line input field that expands automatically as users type longer text, ideal for comments, messages, or detailed descriptions.

---

## What is it

A text area is a multi-line text area component that allows users to enter and edit longer blocks of text, such as comments, messages, or descriptions. Unlike a standard text area, which is limited to a single line, the text area can expand vertically and offers more space for content entry.

It typically includes features like a visible label, placeholder text, character limits, and optional resize behavior. The text area is ideal for open-ended responses where users need to express detailed information.

---

## Anatomy

| # | Element | Purpose |
|---|---------|---------|
| 1 | Label | Identifies the field's purpose and what input is expected |
| 2 | Input container | Multi-line text entry area with 72px default height (3 lines) |
| 3 | Placeholder text | Provides guidance on expected content format or examples |
| 4 | Character counter | Displays remaining/exceeded characters relative to limit in real-time |
| 5 | Helper text/Error message | Offers additional guidance or validation feedback below field |
| 6 | Helper link | Optional external or modal link for additional help resources |
| 7 | Scrollbar | Appears when content exceeds 240px maximum height (10 lines) |
| 8 | Border/Outline | Visual indicator of field state (enabled, focus, error) |

---

## Usage & Guidance

### Best for 👈👈👈

✅ Multi-sentence feedback requiring 3+ lines of text (reviews, comments, descriptions)  
✅ Open-ended questions where response length is unpredictable  
✅ Message composition interfaces (emails, chat, support tickets)  
✅ Form fields requiring detailed explanations or justifications  
✅ Content creation contexts (blog posts, notes, documentation)  
✅ User-generated descriptions that need character count monitoring  
✅ Contexts where auto-resize improves user experience without layout disruption  
✅ Mobile forms where vertical scroll management is critical  
✅ Read-only display of longer text blocks requiring scrolling  
✅ Situations where placeholder guidance helps format consistency

---

### ⚠️ Label

Describes the purpose of the input. Why hide a text area label?

In some UI contexts, especially when space is limited or when the input is part of a compact layout (search bars, filters, inline forms), visually hiding the label can help maintain a clean and uncluttered interface.

However, hiding the label should only be done if:
• The purpose of the input remains clear thanks to a placeholder or contextual icon.
• The label is still accessible to screen readers (using aria-label, aria-labelledby, or visually hidden text).

Hiding a label is a design choice that must balance visual simplicity and clarity of intent, without compromising inclusiveness or form guidance.

---

### Behavior on content size (height)

• **Default display** By default, the height of the input text container is set to 72px, which allows 3 lines of text to be displayed without expanding the component. This height helps distinguish the field from other text inputs, prevents discouraging users with an overly large field, and keeps the layout compact at the start of a form.

• **Auto-resize (automatic expansion)** Above 3 lines of text, the field automatically increases in height as the user types their comment.

• **Vertical scrollbar** If expansion is disabled or the maximum height is reached at 240px, corresponding to about 10 lines of text, an internal scrollbar appears allowing the user to scroll through the overflowing text. This choice prevents breaking the layout but has the drawback, on mobile, of creating a scroll within a scroll (text area scroll inside a page scroll).

**⚠️ No manual resize (by the user)** On both desktop and mobile, we have chosen to disable manual resizing to avoid behaviors inconsistent with the design system.

---

### Character count

• **Character limit not exceeded** The character counter, located in the helper text area, displays in real time (with each keystroke) the number of characters the user can still enter before reaching the field's allowed limit.

⚠️ It is impossible to provide a recommendation for the maximum number of characters, as this depends too specifically on the constraints (or lack thereof) of each project.

• **Character limit exceeded** If the user exceeds the set limit, the field enters an error state, but input is not blocked. The character counter then shows the user, still in real time, how many characters have been entered beyond the field's allowed limit.

The user must reduce the number of characters entered for the text area to exit the error state.

---

### Establish clear expectations upfront 👈👈👈

✅ **Do:** Use label + helper text combination to explain expected content length, format, and character limits before users start typing  
❌ **Don't:** Wait until error state to inform users about character limits or content requirements they should have known from the start

### Position context where users naturally look first 👈👈👈

✅ **Do:** Place essential guidance (character limits, format expectations) in helper text directly below the label where users scan before typing  
❌ **Don't:** Hide critical information in tooltips, modals, or helper links that require extra interaction to discover

### Design error recovery into the flow 👈👈👈

✅ **Do:** When character limit is exceeded, show "+23 characters over limit" and let users continue typing while they edit down  
❌ **Don't:** Block input at character limit or clear the field, forcing users to lose their work and start over

### Optimize vertical real estate strategically 👈👈👈

✅ **Do:** Use 72px default height (3 lines) for forms where vertical space is precious and most responses are brief  
❌ **Don't:** Start with expanded height in dense forms or mobile layouts where it pushes important content below the fold

### Adapt height behavior to content expectations 👈👈👈

✅ **Do:** Allow auto-expansion for feedback forms or messaging where users expect to write longer responses naturally  
❌ **Don't:** Force scrolling at 72px when the context signals to users they should write detailed, multi-paragraph responses

### Make scroll-within-scroll intentional 👈👈👈

✅ **Do:** Accept scroll-within-scroll on mobile only when maintaining layout stability is more important than scroll convenience (constrained dialogs, fixed-height cards)  
❌ **Don't:** Cap height at 240px on mobile forms without considering whether users would prefer page-level scrolling instead

### Signal read-only content appropriately 👈👈👈

✅ **Do:** Use read-only state with scrollbar for displaying user-submitted content, historical data, or system-generated text users need to reference  
❌ **Don't:** Use read-only text areas as a substitute for static text blocks or when there's no need for scrolling interaction

### Handle empty state meaningfully 👈👈👈

✅ **Do:** Use placeholder text that shows realistic examples: "Example: I noticed the checkout button didn't respond when I clicked it on mobile"  
❌ **Don't:** Write vague placeholders like "Enter text here" or "Type something" that don't help users understand what to write

### Preserve user content during validation 👈👈👈

✅ **Do:** Keep all user input visible when displaying error messages, allowing them to see and fix specific issues without re-entering text  
❌ **Don't:** Clear the field, truncate content, or hide text during error states, breaking the user's editing flow

### Coordinate helper text with validation timing 👈👈👈

✅ **Do:** Show persistent helper text for character limits but replace it with specific error messages only after users exceed the limit  
❌ **Don't:** Show both helper text and error message simultaneously, creating visual clutter and unclear hierarchy

---

### How should I configure labels and helper text for user feedback forms? 👈👈👈

Use a descriptive label like "What happened?" with helper text below showing the character limit: "Describe the issue you encountered (500 characters maximum)."

### What should the empty state look like when first displayed? 👈👈👈

Display the label, empty 72px container with placeholder text showing an example response format, and helper text with character limit if applicable.

### How do I show the character limit being exceeded? 👈👈👈

When exceeded, add red border and error icon to the container, replace helper text with red error message showing "+[X] characters over limit," and let the user continue editing.

### What's the visual difference between 72px default and expanded height states? 👈👈👈

Default shows 3 lines of text at 72px; after 3 lines, the container automatically grows vertically until reaching 240px maximum height.

### How should I display the scrollbar when maximum height is reached? 👈👈👈

At 240px height (approximately 10 lines), show a vertical scrollbar inside the text container, maintaining the fixed height while allowing content scrolling.

### What should the focus state look like during text entry? 👈👈👈

Apply focus styling (typically blue border or outline) to the container border, ensure the cursor is visible inside the field, and maintain any helper text or character counter below.

### How do I configure read-only display for system-generated content? 👈👈👈

Use read-only state with muted background color, display the full text content with scrollbar if needed, and show a label indicating the content source.

### What should the error state look like for validation failures beyond character limits? 👈👈👈

Apply red border and error icon, display specific error message below the field (e.g., "Please remove special characters"), and keep the user's input visible for correction.

### How should I display helper links alongside error messages? 👈👈👈

Position the helper link directly below the error message, maintaining its regular styling, so users can access additional help while seeing what went wrong.

### What's the correct configuration for mobile messaging interfaces? 👈👈👈

Use 72px default height with auto-expansion enabled, show character counter if there's a limit, and consider allowing expansion beyond 240px if message length is expected.

---

## Screen Sizes

### Desktop

Text areas maintain 72px default height and auto-expand vertically to 240px maximum. Wider viewports allow longer line lengths before wrapping, reducing vertical expansion needs. Scrollbars use standard desktop styling.

### Tablet

Similar behavior to desktop with moderate line lengths. Touch-friendly scrollbar sizing ensures usability. Auto-expansion works identically, preventing layout disruption in responsive forms.

### Mobile

Compact width causes more frequent line wrapping and faster vertical expansion. Scroll-within-scroll consideration is critical—balance layout stability against user scroll expectations. Touch targets for scrolling must meet minimum 44px requirements.

---

# Specs

## Properties

### Initial Config

| Property | Default Value | Notes |
|----------|---------------|-------|
| Outlined | False | Filled style with subtle background and bottom border is default for form contexts |
| Rounded corner | False | Square corners are default; rounded corners available for brand-specific emotional contexts |
| Input status | Empty | Field starts blank without placeholder unless placeholder text is explicitly configured |
| State | Enabled | Neutral appearance allowing immediate user interaction without restrictions |
| Error | False | Field begins in valid state; error status triggers only after validation failure |
| Scrolled | False | Scrollbar appears automatically only when content exceeds 240px maximum height |
| ⚠️ Label | True | Label is visible by default; hiding requires explicit choice with accessibility considerations |
| Helper text | False | Helper text is optional; enable when users need guidance about format or limits |
| Helper link | False | Additional help link is optional; use only when external resources or modals add value |

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

**⚠️ Error message vs helper text / link** If a helper text accompanies the text input, it is replaced by the error message. However, a helper link must not be replaced and should remain positioned below the error message.

---

### Scrolled

**`Scrolled`** Represents the state in which the field contains more text than its visible height can display and that internal scrolling is available. This allows users to navigate through the overflowing text without expanding the text area beyond the maximum planned height of 240px, allowing the display of about 10 lines of text. It is particularly useful when preserving space is important, or when the text area is embedded within a fixed-height container.

---

### Helper text

**Helper text** Supporting text conveys additional information about the input field, such as how it will be used. It should ideally only take up a single line, though may wrap to multiple lines if required, and be either persistently visible or visible only on focus.

---

### Helper link

**Helper link** If the helper text is not sufficient (It can also be displayed on its own without helper text), it's possible to offer the user an additional help link (the link can be external or open a modal).

---

# Accessibility

Text areas require WCAG 2.2 Level AA compliance to ensure users can enter longer-form content independently and efficiently. For comprehensive accessibility guidance, see the [Orange Unified Design System Accessibility Overview](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability).

---

## Accessibility Challenges

Multi-line text inputs present unique challenges: users must understand expected content length and format upfront, navigate multiple lines with keyboard and assistive technology, recover from character limit violations without losing work, and manage scroll-within-scroll interactions especially on mobile. Auto-expansion behavior and dynamic character counting must announce changes to screen readers in real-time without overwhelming users, while maintaining spatial awareness of cursor position across multiple lines.

### Key Challenges
- Auto-resize behavior changing field height dynamically may disorient screen reader users who lose spatial context
- Character counters updating in real-time require live region announcements without interrupting text composition flow
- Scroll-within-scroll on mobile creates navigation complexity for users relying on gestures or screen readers
- Error states appearing after character limit exceeded must preserve all user content while providing clear recovery path

### Critical Success Factors
1. Provide programmatically associated labels, helper text, and error messages using `aria-describedby` (WCAG 3.3.2, 4.1.2)
2. Announce character count changes and limit violations via live regions without disrupting composition flow (WCAG 4.1.3)
3. Ensure all functionality operates via keyboard including multi-line navigation, scrolling, and error correction (WCAG 2.1.1)
4. Maintain ≥3:1 contrast for focus indicators, error borders, and disabled text states (WCAG 2.4.7, 1.4.11)

---

## Design Requirements

### Structure & Labels
- [ ] **Programmatically associated label**: Connect visible label to `<textarea>` via `id` and `for` attribute, never omit even if visually hidden ([Orange A11y - Forms](https://a11y-guidelines.orange.com/en/web/components-examples/forms/))
- [ ] **Multi-ID aria-describedby**: Associate helper text, character counter, and error message using space-separated IDs so screen readers announce all context
- [ ] **Persistent label visibility**: Keep labels visible by default unless placeholder + context icon clearly convey purpose with hidden label still available to assistive technology

### Visual Design
- [ ] **Focus indicator contrast**: Ensure focus border or outline has ≥3:1 contrast against adjacent colors and ≥2px thickness ([Orange A11y - Focus Visibility](https://a11y-guidelines.orange.com/en/web/components-examples/keyboard-navigation/#focus-visibility))
- [ ] **Error state contrast**: Red error border and icon must meet ≥3:1 contrast against white background, error text ≥4.5:1 against background
- [ ] **Disabled state contrast**: Maintain ≥3:1 contrast for disabled text and borders to ensure visibility while signaling non-interactivity ([WCAG 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum))

### Content
- [ ] **Actionable error messages**: ❌ "Character limit exceeded" / ✅ "Please remove 23 characters. Consider shortening your response or splitting into multiple comments." ([Orange A11y - Error Messages](https://a11y-guidelines.orange.com/en/web/components-examples/forms/#error-messages))
- [ ] **Realistic placeholder examples**: Show specific format rather than generic hints: "Example: I clicked the submit button but received error code 502" vs "Enter description here"

---

## Testing Checklist

### Screen Reader Testing
- [ ] Test with NVDA (Windows), JAWS (Windows), VoiceOver (macOS/iOS), TalkBack (Android) to verify label announced, helper text read before user types, character counter updates announced via live region, error messages read immediately when triggered
- [ ] Verify auto-expansion height changes announced, scroll state communicated when scrollbar appears, read-only state indicated, disabled state clearly identified

### Keyboard Testing
- [ ] Tab focuses field (visible focus indicator ≥3:1 contrast), Enter creates new line within text area (not form submission), Arrow keys navigate between lines, Home/End move to line start/end, Ctrl+Home/End move to field start/end
- [ ] Verify Page Up/Down scroll content when scrollbar present, Escape clears focus from field, all interactions keyboard-accessible without mouse

### Paste Testing
- [ ] Paste long text (Ctrl+V/Cmd+V) updates character counter immediately and announces change to screen readers
- [ ] Verify paste triggering auto-expansion announces new height, paste exceeding character limit triggers error state with preserved content

Resources: [Orange Accessibility Testing Guide](https://a11y-guidelines.orange.com/en/web/test/)

---

## Key WCAG Criteria

- **2.1.1 Keyboard** (A): All text entry, scrolling, and error correction operable via keyboard without timing requirements; Enter key creates new lines rather than submitting forms
- **2.4.7 Focus Visible** (AA): Visible focus indicator with ≥3:1 contrast on text area border when focused, maintained during typing and scrolling
- **3.3.1 Error Identification** (A): Character limit violations and validation errors identified in text, associated via `aria-describedby`, with error icon and red border
- **3.3.2 Labels or Instructions** (A): Labels provided for all text areas, helper text explains character limits upfront, placeholder shows format examples
- **4.1.2 Name, Role, Value** (A): Correct `<textarea>` semantic HTML, `aria-describedby` links helper/error text, `aria-invalid="true"` set during error states
- **4.1.3 Status Messages** (AA): Character counter and limit violations announced via `aria-live="polite"` live region without interrupting typing flow

For complete reference: [Orange Accessibility Guidelines - Form Components](https://a11y-guidelines.orange.com/en/web/components-examples/forms/)

---

## Additional Resources

- [Orange Accessibility Guidelines - Forms](https://a11y-guidelines.orange.com/en/web/components-examples/forms/)
- [Orange Accessibility Guidelines - Error Messages](https://a11y-guidelines.orange.com/en/web/components-examples/forms/#error-messages)
- [WCAG 2.2 Understanding Docs - Keyboard](https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html)
- [WCAG 2.2 Understanding Docs - Status Messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html)
- [Orange Design System - Accessibility & Sustainability](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability)