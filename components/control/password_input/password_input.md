# Guideline

## Intro

A password input securely captures confidential user credentials with character masking and optional visibility toggle for improved usability.

---

## Definition

A password input is a form field specifically designed to securely capture a user's confidential password. It masks the characters as they are typed, typically replacing them with dots, in order to protect the input from being read by others nearby.

While the primary goal is to enhance privacy and security, the field may also include usability features such as a "show/hide password" toggle and helper text to guide password creation.

---

## Best for

✅ Account login and authentication flows requiring secure credential entry

✅ New account registration where users create passwords for the first time

✅ Password change or reset journeys within account settings

✅ Multi-factor authentication setups requiring PIN or passcode entry

✅ Sensitive data entry in banking, healthcare, or enterprise applications

✅ Mobile-first interfaces where touch typing increases error likelihood

✅ Forms requiring confirmation of user identity before proceeding

✅ E-commerce checkout flows with saved payment authentication

✅ Admin or back-office systems with elevated security requirements

✅ Self-service portals where users manage their own account security

---

## Anatomy

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Label | Identifies the input field's purpose and provides accessible name | N |
| 2 | Input container | Houses the input area and associated interactive elements | N |
| 3 | Input area | Zone where users type their password characters | N |
| 4 | Character masking | Visual dots or asterisks replacing typed characters for privacy | N |
| 5 | Show/hide toggle | Button allowing users to reveal or conceal password characters | Y |
| 6 | Leading icon | Visual indicator of field purpose (e.g., lock icon) | Y |
| 7 | Helper text | Supporting guidance about password requirements or usage | Y |
| 8 | Error message | Validation feedback when input fails requirements | Y |

---

## Outlined

**`False`** An input with a subtle background fill and un visible bottom border, creating a softer and more contained look. Best suited for dense layouts or to enhance visibility.

**`True`** A minimalist input with a transparent background and a visible stroke outlining the field. This style may be interesting for contexts other than form pages:
• When inputs need to feel lightweight and unobtrusive
• In a header (search field)
• In a selection/filtering feature in a product catalog

### Do & don'ts

✅ **Do:** Use the outlined style in lightweight contexts such as headers, filters, or search interfaces where minimal visual weight improves the experience.  
❌ **Don't:** Mix outlined and filled styles inconsistently within the same form—choose one style and apply it uniformly.

✅ **Do:** Select the filled (non-outlined) variant for standard form pages to ensure sufficient visual prominence and discoverability.  
❌ **Don't:** Use the outlined style in dense forms where users need strong visual boundaries to distinguish multiple adjacent fields.

✅ **Do:** Ensure both outlined and filled variants maintain the same functional behaviors including focus states and error handling.  
❌ **Don't:** Reduce the touch target size when using the outlined style—maintain minimum 44×44px interactive areas.

✅ **Do:** Test both style variants for adequate contrast against their background contexts in light and dark modes.  
❌ **Don't:** Assume the outlined style will work on busy backgrounds without verifying stroke visibility meets 3:1 contrast ratio.

✅ **Do:** Apply the outlined style when aligning with brand guidelines that favor a modern, minimal aesthetic.  
❌ **Don't:** Choose style variants based solely on personal preference—align with established design system patterns.

---

## Rounded corner

**`False`** For a square finish.

**`True`** For a finish with rounded corner. To be favored in more emotional, immersive contexts or those tied to specific visual identities. For standard or business-oriented journeys, keep the default corners. This evolution addresses the need for flexibility in adapting the design to certain brand contexts.

### Do & don'ts

✅ **Do:** Use rounded corners in consumer-facing, lifestyle, or emotionally-driven brand experiences where softness supports the visual identity.  
❌ **Don't:** Apply rounded corners to enterprise or B2B applications where sharp corners better convey professionalism and precision.

✅ **Do:** Maintain consistent corner radius values across all form inputs within the same interface to create visual harmony.  
❌ **Don't:** Mix rounded and square inputs within the same form or page layout without intentional design rationale.

✅ **Do:** Coordinate password input corner styles with adjacent buttons and other form elements for cohesive component grouping.  
❌ **Don't:** Use extreme border-radius values that distort the input's proportions or reduce usable input area.

✅ **Do:** Consider rounded corners for mobile interfaces where softer shapes often feel more touch-friendly and approachable.  
❌ **Don't:** Override established platform conventions—follow iOS or Android native patterns where appropriate.

✅ **Do:** Document your corner radius decision in design tokens to ensure consistency across the design system.  
❌ **Don't:** Make corner style decisions in isolation—ensure they align with the broader component library and brand guidelines.

---

## Input status

**`Empty`** The Empty state indicates that the password input is blank with no content or placeholder, a neutral starting point.

**`Empty (Placeholder)`** The Empty with Placeholder state provides a hint or guidance inside the field to suggest expected input.

**`Filled`** The Filled state shows that the user has entered valid content into the field, replacing any placeholder.

### Do & don'ts

✅ **Do:** Use placeholder text sparingly and only for supplementary hints—never as a replacement for visible labels.  
❌ **Don't:** Put essential information like password requirements in placeholder text as it disappears once users start typing.

✅ **Do:** Ensure placeholder text has sufficient contrast (4.5:1 minimum) against the input background for readability.  
❌ **Don't:** Use placeholder text that could be mistaken for actual input, such as sample passwords or realistic credential formats.

✅ **Do:** Provide clear visual distinction between empty, placeholder, and filled states through typography weight or color changes.  
❌ **Don't:** Rely solely on placeholder presence to indicate whether a field has been interacted with—use proper state management.

✅ **Do:** Consider keeping helper text visible outside the input rather than using placeholders for password format guidance.  
❌ **Don't:** Use overly long placeholder text that gets truncated and loses meaning on smaller viewports.

✅ **Do:** Test that the filled state visually masks characters appropriately while maintaining consistent input height.  
❌ **Don't:** Allow the input to resize or shift layout when transitioning between empty and filled states.

---

## Error

The Error status indicates that the user input does not meet validation rules or expected formatting. It provides immediate visual feedback, typically through a red border, error icon, and a clear, accessible error message positioned below the input (mandatory).

This state helps users quickly identify and correct mistakes by explaining what went wrong and, when possible, how to fix it. The input remains editable, encouraging users to revise their input without starting over.

**Error message vs helper text** The error message is not the same element as the helper text, it is independent. If a helper text accompanies the text input, it is replaced by the error message. The helper text must not be displayed simultaneously.

### Do & don'ts

✅ **Do:** Write error messages that specifically explain what went wrong and provide actionable guidance on how to fix it.  
❌ **Don't:** Use generic error messages like "Invalid input" that leave users guessing about the actual problem.

✅ **Do:** Associate error messages programmatically with the input using `aria-describedby` so screen readers announce them.  
❌ **Don't:** Display error messages only through color changes—always include text descriptions for accessibility.

✅ **Do:** Show error validation inline and in real-time where appropriate to help users correct mistakes before submission.  
❌ **Don't:** Wait until form submission to reveal all errors, creating frustrating back-and-forth correction cycles.

✅ **Do:** Maintain the error state until the user has successfully corrected the input and it passes validation.  
❌ **Don't:** Clear error states automatically on focus or blur without verifying the input now meets requirements.

✅ **Do:** Use error iconography consistently alongside text to provide redundant visual cues beyond color alone.  
❌ **Don't:** Display both helper text and error message simultaneously—replace helper text with the error message.

---

## Leading icon

Helps indicate the purpose of the input (magnifying glass for search, envelope for email, phone device for phone number). Only use a leading icon if it adds clear functional or contextual value.

### Do & don'ts

✅ **Do:** Use universally recognized icons like a lock or key symbol that clearly communicate the password field's purpose.  
❌ **Don't:** Add decorative icons that don't contribute meaningful context or could confuse users about the field's function.

✅ **Do:** Ensure leading icons are marked as decorative (`aria-hidden="true"`) when the label already provides sufficient context.  
❌ **Don't:** Rely on the icon alone to communicate field purpose—always pair with a visible text label.

✅ **Do:** Maintain consistent icon sizing and alignment across all form inputs for visual coherence.  
❌ **Don't:** Use leading icons that visually compete with or obscure the show/hide toggle button on the trailing side.

✅ **Do:** Choose icon colors that meet 3:1 contrast requirements against the input background.  
❌ **Don't:** Use brand-colored icons that may fail contrast in certain themes or modes (light/dark).

✅ **Do:** Test that leading icons don't reduce the usable typing area or create cramped layouts on narrow viewports.  
❌ **Don't:** Include leading icons by default—only add them when they provide genuine functional value.

---

## Label

Describes the purpose of the input. Why hide a password input label?

In some UI contexts, especially when space is limited or when the input is part of a compact layout (search bars, filters, inline forms), visually hiding the label can help maintain a clean and uncluttered interface.

However, hiding the label should only be done if:
• The purpose of the input remains clear thanks to a placeholder or contextual icon.
• The label is still accessible to screen readers (using aria-label, aria-labelledby, or visually hidden text).

Hiding a label is a design choice that must balance visual simplicity and clarity of intent, without compromising inclusiveness or form guidance.

### Do & don'ts

✅ **Do:** Always provide a programmatically associated label for every password input, even when visually hidden.  
❌ **Don't:** Omit labels entirely—screen reader users depend on them to understand the field's purpose.

✅ **Do:** Use visually hidden CSS techniques (`.sr-only`) to maintain accessibility when hiding labels for visual design reasons.  
❌ **Don't:** Use `display: none` or `visibility: hidden` to hide labels as these remove them from the accessibility tree.

✅ **Do:** Write labels that clearly describe the expected input, such as "Password" or "Current password" for clarity.  
❌ **Don't:** Use vague labels like "Enter here" or overly technical labels that don't help users understand what's required.

✅ **Do:** Position visible labels consistently above or beside inputs according to your design system's established patterns.  
❌ **Don't:** Hide labels in contexts where users might not understand the field's purpose from context alone.

✅ **Do:** Ensure labels remain visible in error states to help users understand which field requires attention.  
❌ **Don't:** Rely on placeholder text as a label substitute—placeholders disappear when users begin typing.

---

## Other boolean options

**Prefix** A visual or textual element placed before the user's input. A prefix is not common and is discouraged in a Password Input component. Here are illustrative examples of very specific cases where:
• "corp-" Company password enforcing a prefix
• "temp-" Temporary password during a testing phase
• "dev-" For test accounts
• "eu-, us-, prod-, stage-" To encode a target environment
• "test@" Used in the context of automated or predictable tests
• "admin-" Pattern used to define an admin password

**Helper text** Supporting text conveys additional information about the input field, such as how it will be used. It should ideally only take up a single line, though may wrap to multiple lines if required, and be either persistently visible or visible only on focus.

### Do & don'ts

✅ **Do:** Use helper text to communicate password requirements upfront (e.g., minimum length, required character types).  
❌ **Don't:** Hide critical password requirements in tooltips or only reveal them after validation failures.

✅ **Do:** Keep helper text concise—ideally one line—while still providing actionable guidance.  
❌ **Don't:** Overload helper text with every possible requirement, making it overwhelming to read.

✅ **Do:** Connect helper text programmatically to the input via `aria-describedby` for screen reader accessibility.  
❌ **Don't:** Position helper text far from the input where the visual association becomes unclear.

✅ **Do:** Reserve prefixes for very specific enterprise or system contexts where they're genuinely required by backend systems.  
❌ **Don't:** Use prefixes in consumer-facing password fields as they add unnecessary complexity and confusion.

✅ **Do:** Display password strength indicators or requirement checklists as helper content to guide secure password creation.  
❌ **Don't:** Show helper text and error messages simultaneously—error messages should replace helper text when active.

---

# Specs

## States

**`Enabled`** Neutral appearance, whether empty or filled. It allows users to click, focus, and type freely without restrictions.

**`Hover`** Slight visual contrast or border color change.

**`Focus`** The password input is focused and ready to receive user input. It visually highlights the field to indicate that it's currently editable and interactive. This state typically appears after a user clicks or taps into the field.

**`Loading`** The Loading state indicates that the system is processing or retrieving data related to the password input. A progress indicator appears to inform the user that an action is in progress. During this state, the input may be temporarily disabled to prevent further interaction.

**`Read only`** Text visible but not editable (often with a muted or different background).

**`Disabled`** The field is non-interactive and grayed out to indicate it cannot be changed. The helper text is muted.

**`Skeleton`** Improves the perceived loading time by providing a visual cue of where field will appear once fully loaded. Uses the "Skeleton" component, variant "Security marge=False".

---

## Layout and spacing

🚧 Content to be added

---

# Accessibility

## Accessibility intro

Password inputs must meet WCAG 2.2 Level AA requirements with particular attention to secure, accessible show/hide functionality and clear error communication. For comprehensive accessibility guidance, see the [Orange Unified Design System Accessibility Overview](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability).

---

## Accessibility Challenges

Password inputs present unique accessibility challenges because they must balance security (character masking) with usability (allowing users to verify their input). The show/hide toggle requires careful implementation to communicate state changes without inadvertently exposing passwords to nearby listeners, while error messages and password requirements must be programmatically associated for assistive technology users.

### Key Challenges
- Masked characters prevent users from visually verifying input accuracy
- Show/hide toggle state must be clearly communicated to screen readers without reading the password aloud
- Password requirements need programmatic association with the input field
- Error messages must be announced without disrupting user flow

### Critical Success Factors
1. Implement show/hide toggle with proper `aria-pressed` or `role="switch"` with `aria-checked`
2. Connect password requirements via `aria-describedby` for screen reader announcement
3. Ensure visible focus indicator with ≥3:1 contrast on all interactive elements
4. Provide clear, specific error messages that explain both the problem and solution

---

## Design Requirements

### Structure & Labels
- [ ] **Visible label**: Always provide a visible text label; if hidden, use visually-hidden CSS with `aria-label` or `aria-labelledby`
- [ ] **Programmatic association**: Label connected via `for`/`id` pairing ([Orange: Form labels](https://a11y-guidelines.orange.com/en/web/develop/forms/))
- [ ] **Helper text connection**: Password requirements linked via `aria-describedby` on the input element

### Visual Design
- [ ] **Focus indicator**: 2px solid outline with ≥3:1 contrast against adjacent colors
- [ ] **Toggle button contrast**: Show/hide icon or text meets 3:1 contrast against background ([Color contrast](https://a11y-guidelines.orange.com/en/web/design/colors-and-contrasts/))
- [ ] **Error styling**: Red border with error icon; never rely on color alone to indicate errors

### Content
- [ ] **Error messages**: ❌ "Invalid password" / ✅ "Password must be at least 8 characters"
- [ ] **Toggle labels**: Use clear text ("Show password" / "Hide password") or accessible icon with `aria-label`

---

## Testing Checklist

### Screen Reader Testing
- [ ] Test with NVDA (Windows), JAWS (Windows), VoiceOver (macOS/iOS), TalkBack (Android)
- [ ] Verify label announced on focus, requirements read via `aria-describedby`, toggle state communicated, errors announced

### Keyboard Testing
- [ ] Tab navigates to input and toggle button, Enter/Space activates toggle, focus visible throughout
- [ ] Verify show/hide functionality works via keyboard without mouse interaction

### Paste Testing
- [ ] Paste functionality works correctly—never block paste in password fields

Resources: [Orange Accessibility Testing Guide](https://a11y-guidelines.orange.com/en/web/toolbox/)

---

## Key WCAG Criteria

- **1.3.1 Info and Relationships** (A): Label, helper text, and error messages programmatically associated with input
- **2.1.1 Keyboard** (A): All functionality including show/hide toggle operable via keyboard
- **2.4.7 Focus Visible** (AA): Clear focus indicator on input field and toggle button with ≥3:1 contrast
- **3.3.1 Error Identification** (A): Errors identified in text and associated with input via `aria-describedby`
- **4.1.2 Name, Role, Value** (A): Toggle button has accessible name and communicates pressed/checked state

For complete reference: [Orange Accessibility Guidelines - Forms](https://a11y-guidelines.orange.com/en/web/components-examples/)

---

## Additional Resources

- [Orange Accessibility Guidelines - Form Examples](https://a11y-guidelines.orange.com/en/web/components-examples/)
- [GOV.UK Design System - Password Input](https://design-system.service.gov.uk/components/password-input/)
- [WCAG 2.2 Understanding Docs - Input Purposes](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html)
- [Orange Design System - Accessibility & Sustainability](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability)

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Sep 30, 2025 | 1.2.0 | • The name of the "Style" variant has been replaced to "Outlined" with true/false variant | Hamza Amarir |
| Jul 29, 2025 | 1.1.0 | • Several design token updates: [Component tokens changelog 1.5.0](https://www.figma.com/design/Co2t6wHMf4GB9NJVGs2Hes/-OUDS-Core-Lib--Design-tokens?m=auto&node-id=9280-2568&t=HLVB4jOd35DWr8Bj-1) | Maxime Tonnerre |
| Jun 30, 2025 | 1.0.0 | • Component creation | Maxime Tonnerre |

---