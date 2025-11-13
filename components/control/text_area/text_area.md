# Guideline

## Intro 👈🤖

A multi-line input component for longer text entries like comments, messages, or descriptions that auto-expands as users type.

---

## Description

A text area is a multi-line text area component that allows users to enter and edit longer blocks of text, such as comments, messages, or descriptions. Unlike a standard text area, which is limited to a single line, the text area can expand vertically and offers more space for content entry.

It typically includes features like a visible label, placeholder text, character limits, and optional resize behavior. The text area is ideal for open-ended responses where users need to express detailed information.

---

## Anatomy 👈🤖

| # | Element | Purpose |
|---|---------|---------|
| 1 | Label text | Describes the purpose of the input field and provides context for users |
| 2 | Input text container | Main area where users enter and view their text content, auto-expands vertically |
| 3 | Placeholder text | Provides guidance on expected input when field is empty |
| 4 | Helper text / Character counter | Displays real-time character count and remaining limit, or provides additional guidance |
| 5 | Helper link | Optional link for additional assistance or information (external or modal) |
| 6 | Error message | Replaces helper text when validation fails, explains issue and correction steps |
| 7 | Scrollbar | Appears when content exceeds maximum height of 240px (approximately 10 lines) |

---

## Usage & Guidance

### Best for 👈🤔

✅ Open-ended feedback, detailed comments, or lengthy descriptions requiring multiple sentences  
✅ User-generated content where character count matters (reviews, testimonials, reports)  
✅ Form fields requiring more than one line of text input  
✅ Contexts where users need to see and edit multiple lines of text simultaneously  
✅ Situations where placeholder guidance improves input quality and reduces errors  
✅ Mobile-first designs where auto-expansion prevents layout disruption  
✅ Workflows where character limits are enforced to maintain data consistency  
✅ Scenarios requiring helper text or links to assist users during entry  
✅ Contexts where read-only or disabled states communicate system processing  
✅ Applications where loading states indicate background validation or data retrieval

---

### ⚠️ Label

Describes the purpose of the input. Why hide a text area label?

In some UI contexts, especially when space is limited or when the input is part of a compact layout (search bars, filters, inline forms), visually hiding the label can help maintain a clean and uncluttered interface.

However, hiding the label should only be done if:
• The purpose of the input remains clear thanks to a placeholder or contextual icon.
• The label is still accessible to screen readers (using aria-label, aria-labelledby, or visually hidden text).

Hiding a label is a design choice that must balance visual simplicity and clarity of intent, without compromising inclusiveness or form guidance.

---

### Behavior by entered line count

• **Default display**
By default, the height of **the input text container is set to 72px, which allows 3 lines of text** to be displayed without expanding the component. This height helps distinguish the field from other text inputs, prevents discouraging users with an overly large field, and keeps the layout compact at the start of a form.

• **Auto-resize (automatic expansion)**
Above 3 lines of text, the field automatically increases in height as the user types their comment.

• **Vertical scrollbar**
If expansion is disabled or **the maximum height is reached at 240px, corresponding to about 10 lines of text**, an internal scrollbar appears allowing the user to scroll through the overflowing text. This choice prevents breaking the layout but has the drawback, on mobile, of creating a scroll within a scroll (text area scroll inside a page scroll).

**⚠️ No manual resize (by the user)**
On both desktop and mobile, we have chosen to disable manual resizing to avoid behaviors inconsistent with the design system.

---

### Character counter

• **Character limit not exceeded**
The character counter, located in the helper text area, displays in real time (with each keystroke) the number of characters the user can still enter before reaching the field's allowed limit.

⚠️ It is impossible to provide a recommendation for the maximum number of characters, as this depends too specifically on the constraints (or lack thereof) of each project.

• **Character limit exceeded**
If the user exceeds the set limit, the field enters an error state, but input is not blocked. The character counter then shows the user, still in real time, how many characters have been entered beyond the field's allowed limit.

The user must reduce the number of characters entered for the text area to exit the error state.

---

### Label clarity drives completion 👈🤔

✅ **Do:** Use specific, action-oriented labels that explain what information is needed ("Describe your technical issue" rather than "Comments")  
❌ **Don't:** Use generic labels like "Text" or "Input" that leave users guessing about expected content type or format

---

### Position helper text for scanning efficiency 👈🤔

✅ **Do:** Place character counters and formatting hints below the input where users naturally look after typing  
❌ **Don't:** Position critical guidance above the input or far from the field, forcing users to scroll or search for context

---

### Placeholder text guides without replacing labels 👈🤔

✅ **Do:** Use placeholder text to show format examples ("Minimum 50 characters for detailed feedback") that disappear on focus  
❌ **Don't:** Rely on placeholder text alone without a persistent label, as placeholders vanish when users begin typing

---

### Error messages explain and guide recovery 👈🤔

✅ **Do:** Replace helper text with specific error messages that explain what went wrong and how to fix it ("Exceeds limit by 45 characters—please shorten your response")  
❌ **Don't:** Show vague errors like "Invalid input" without indicating the issue or next steps for correction

---

### Helper links reduce interruption 👈🤔

✅ **Do:** Provide optional helper links for complex input requirements that open modals or external guides without losing user progress  
❌ **Don't:** Interrupt the user's flow by opening help pages in the same window or removing them from the form context

---

### Character limits maintain consistency 👈🤔

✅ **Do:** Communicate character limits clearly before users begin typing, showing real-time countdown as they approach the limit  
❌ **Don't:** Block input abruptly at the limit without warning, or allow unlimited entry that later causes validation failures

---

### Auto-expansion preserves context 👈🤔

✅ **Do:** Let the field expand automatically up to 10 lines so users can see their full text while typing without scrolling  
❌ **Don't:** Force users into a tiny 2-3 line box from the start, hiding content and making editing difficult

---

### Read-only states communicate processing 👈🤔

✅ **Do:** Use read-only state when displaying pre-filled content that users should review but not modify during a workflow step  
❌ **Don't:** Use disabled state for content that's temporarily locked, as it suggests the field is permanently unavailable

---

### Loading states reduce uncertainty 👈🤔

✅ **Do:** Show loading indicators when the system validates input or fetches suggested content, reassuring users that processing is underway  
❌ **Don't:** Leave the field in a silent enabled state during background operations, causing users to wonder if their action registered

---

### Scrolling inside inputs creates friction on mobile 👈🤔

✅ **Do:** Consider maximum heights carefully for mobile layouts where nested scrolling (page scroll + input scroll) degrades usability  
❌ **Don't:** Set aggressive height limits on mobile that force frequent internal scrolling while the page itself is scrollable

---

### How should I configure labels and helper text for user feedback collection? 👈🤔

Use a specific label like "Share your experience" with helper text showing character requirements ("Minimum 50 characters") and a real-time counter below the input.

---

### What should the error state look like when a character limit is exceeded? 👈🤔

Display a red border, error icon, and message below the input stating "Exceeds limit by [X] characters—please shorten your response" while showing the exact overage count.

---

### How do I display helper links for complex input requirements? 👈🤔

Position the helper link below the helper text or error message with underlined text like "See formatting guidelines" that opens a modal without leaving the form.

---

### What's the visual difference between enabled and read-only states for pre-filled content? 👈🤔

Read-only state shows content with a muted background and no cursor interaction, while enabled state has standard background color and accepts focus and editing.

---

### How should I configure the field for short feedback versus detailed descriptions? 👈🤔

For short feedback (under 3 lines), use default 72px height; for detailed descriptions, let auto-expansion work up to 240px with visible scrollbar when limit is reached.

---

### What does the loading state look like when validating input? 👈🤔

Show a progress indicator inside the trailing container area (right side of input) while the field remains enabled but visually indicates processing is underway.

---

### How do I show placeholder guidance for format expectations? 👈🤔

Display placeholder text like "Describe your issue in detail (minimum 20 words)" that disappears on focus, with persistent label above and helper text below.

---

### What's the visual layout when both character counter and helper link are present? 👈🤔

Character counter appears in helper text position below input, followed by helper link on the next line, both left-aligned within the input container's padding.

---

### How should I configure the disabled state for temporarily locked fields? 👈🤔

Show grayed-out background, muted text, and disabled cursor with helper text also muted to indicate the field cannot currently accept input.

---

### What does the skeleton loading state look like before content loads? 👈🤔

Display animated skeleton placeholder matching the input's dimensions (label, 72px text container, helper text areas) using the OUDS Skeleton component with security margin disabled.

---

## Screen Sizes

### Desktop 👈🤖

Text area displays at full width within its container, defaulting to 72px height (3 lines) and expanding up to 240px as users type. Character counters and helper links are easily readable with standard 14px font size and 20px line height.

### Tablet 👈🤖

Maintains desktop behavior with full-width display and auto-expansion, though nested scrolling within the input may occur more frequently as vertical space becomes constrained. Touch targets for helper links meet minimum 44px height requirements.

### Mobile 👈🤖

Auto-expansion is critical to prevent immediate scrollbar appearance in constrained vertical space. Character counters remain visible below input, and users should be aware of potential scroll-within-scroll friction when content exceeds 240px on smaller screens.

---

# Specs

## Properties

### Initial Config

| Property | Default Value | Notes |
|----------|---------------|-------|
| Outlined | False | Standard filled style with subtle background and bottom border for form contexts |
| Rounded corner | False | Square corners maintain consistency with standard business-oriented journeys |
| Input status | Empty | Field starts blank without placeholder text visible by default |
| State | Enabled | Interactive and ready to receive user input without restrictions |
| Error | False | Field begins in valid state without error styling or messages |
| Scrolled | False | Scrollbar hidden until content exceeds maximum height of 240px |
| Label | True | Visible label provides context and accessibility for all users |
| Helper text | False | Character counter or guidance text disabled by default |
| Helper link | False | Optional assistance link hidden unless explicitly enabled |

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

### States

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

### Other boolean options

**Scrolled** Represents the state in which the field contains more text than its visible height can display and that internal scrolling is available. This allows users to navigate through the overflowing text without expanding the text area beyond **the maximum planned height of 240px, allowing the display of about 10 lines of text**. It is particularly useful when preserving space is important, or when the text area is embedded within a fixed-height container.

**Helper text** Supporting text conveys additional information about the input field, such as how it will be used. It should ideally only take up a single line, though may wrap to multiple lines if required, and be either persistently visible or visible only on focus.

**Helper link** If the helper text is not sufficient (It can also be displayed on its own without helper text), it's possible to offer the user an additional help link (the link can be external or open a modal).

---

# Accessibility 👈🤖

## Accessibility intro

Text area components must meet WCAG 2.2 Level AA standards for keyboard operability, label associations, error identification, and focus visibility to ensure all users can enter multi-line text effectively. For comprehensive accessibility guidance, see the [Orange Unified Design System Accessibility Overview](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability).

---

## Accessibility Challenges

Multi-line text inputs present unique accessibility challenges due to their dynamic height behavior, character counting requirements, and complex state management across typing, validation, and error recovery phases. Users relying on assistive technology need real-time feedback about character limits, validation states, and content overflow without losing context or position within longer text entries.

### Key Challenges
- Real-time character counter updates must announce changes to screen readers without interrupting typing flow
- Auto-expansion behavior can cause unexpected screen reader position loss or focus disruption
- Scrollable content within the input creates nested navigation complexity for keyboard and screen reader users
- Error messages must clearly associate with the field while preserving helper text context when both are present

### Critical Success Factors
1. Semantic HTML with proper `<textarea>` element and explicit label associations via `for`/`id` or `aria-labelledby` (WCAG 4.1.2)
2. Live region announcements for character counter changes using `aria-live="polite"` to avoid interrupting user input
3. Error identification with `aria-describedby` linking to error messages and `aria-invalid="true"` on validation failure (WCAG 3.3.1, 4.1.2)
4. Focus indicator with minimum 3:1 contrast ratio that remains visible during all interactions (WCAG 2.4.7)

---

## Design Requirements

### Structure & Labels
- [ ] **Persistent visible label**: Label must remain visible at all times, not hidden inside placeholder text ([Orange Forms Guidelines](https://a11y-guidelines.orange.com/en/web/components-examples/forms/))
- [ ] **Programmatic label association**: Use `<label for="id">` with matching `id` on `<textarea>`, or `aria-labelledby` pointing to label element ID
- [ ] **Character counter as live region**: Wrap counter in element with `aria-live="polite"` to announce updates without interrupting typing

### Visual Design
- [ ] **Focus indicator contrast**: Focus outline must have ≥3:1 contrast against adjacent colors, typically 2px solid with sufficient color difference ([Orange Focus Visible](https://a11y-guidelines.orange.com/en/web/components-examples/keyboard-navigation/))
- [ ] **Error state color + icon + text**: Never rely on color alone; combine red border with error icon and descriptive message below input ([Orange Color Contrast](https://a11y-guidelines.orange.com/en/web/components-examples/colors-and-contrasts/))
- [ ] **Text contrast in all states**: Input text ≥4.5:1, placeholder text ≥4.5:1, helper text ≥4.5:1 against backgrounds

### Content
- [ ] **Specific error messages**: ❌ "Invalid input" / ✅ "Exceeds limit by 45 characters—please shorten your response" ([Orange Error Messages](https://a11y-guidelines.orange.com/en/web/components-examples/error-messages/))
- [ ] **Helper text describes limits**: Communicate character limits, format requirements, and expectations before users begin typing

---

## Testing Checklist

### Screen Reader Testing
- [ ] Test with NVDA (Windows), JAWS (Windows), VoiceOver (macOS/iOS), TalkBack (Android)
- [ ] Verify label announced on focus, character counter updates spoken via live region, error messages read when `aria-invalid="true"` set, placeholder text announced when field empty

### Keyboard Testing
- [ ] Tab navigates to field, Enter creates new line (not submit), all functionality keyboard-accessible without mouse
- [ ] Focus indicator visible (≥3:1 contrast) throughout interaction including auto-expansion

### Character Counter Testing
- [ ] Counter updates announce via `aria-live="polite"` without interrupting typing flow
- [ ] When limit exceeded, error message replaces helper text and announces via `aria-describedby`

Resources: [Orange Accessibility Testing Guide](https://a11y-guidelines.orange.com/en/web/test/)

---

## Key WCAG Criteria

- **2.1.1 Keyboard** (A): All functionality including text entry, scrolling overflow content, and accessing helper links must work via keyboard alone
- **2.4.7 Focus Visible** (AA): Focus indicator with ≥3:1 contrast visible on `<textarea>`, helper links, and all interactive elements
- **3.3.1 Error Identification** (A): Errors identified in text via error message and associated with input via `aria-describedby`, with `aria-invalid="true"` set
- **3.3.2 Labels or Instructions** (A): Visible persistent label provided, with helper text clarifying character limits and format requirements
- **4.1.2 Name, Role, Value** (A): Semantic `<textarea>` element with proper label association, `aria-invalid`, `aria-describedby` for error/helper text, live region for counter updates

For complete reference: [Orange Accessibility Guidelines - Form Examples](https://a11y-guidelines.orange.com/en/web/components-examples/forms/)

---

## Additional Resources

- [Orange Accessibility Guidelines - Forms](https://a11y-guidelines.orange.com/en/web/components-examples/forms/)
- [Orange Accessibility Guidelines - Error Messages](https://a11y-guidelines.orange.com/en/web/components-examples/error-messages/)
- [WCAG 2.2 Understanding - 4.1.2 Name, Role, Value](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html)
- [WCAG 2.2 Understanding - 3.3.1 Error Identification](https://www.w3.org/WAI/WCAG22/Understanding/error-identification.html)
- [Orange Design System - Accessibility & Sustainability](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability)