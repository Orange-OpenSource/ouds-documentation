# Guideline

## Intro 👈🤖

A suggestion chip is a compact, interactive element that presents contextual recommendations or predictive options to streamline user input and selection.

---

## Definition

A suggestion chip is a compact UI element used to present recommended or predictive options based on user input or context. Often found in search bars, forms, or messaging interfaces, suggestion chips help users quickly select from relevant suggestions. They are typically non-selected by default and can be tapped or clicked to apply the suggestion, streamlining user input and enhancing usability.

---

## Best for 👈🤔

✅ Presenting dynamic search suggestions or autocomplete options in search interfaces

✅ Offering quick reply options in messaging or chat applications

✅ Displaying contextual recommendations based on user input or behavior

✅ Providing predictive text or phrase completions in form fields

✅ Surfacing recently used or frequently selected options for quick access

✅ Narrowing user intent by presenting filtered or categorized suggestions

✅ Enabling quick selection of predefined responses in customer support interfaces

✅ Facilitating voice assistant or conversational UI interactions with suggested actions

✅ Streamlining mobile input where typing is cumbersome or time-consuming

✅ Guiding users toward relevant content discovery through contextual nudges

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Container | Defines the chip boundary with rounded corners and provides interactive touch/click target | N |
| 2 | Label text | Displays the suggestion content with centered alignment for readability | Y |
| 3 | Leading icon | Reinforces the suggestion meaning or category with a visual symbol | Y |
| 4 | Border | Indicates chip boundaries and communicates interaction states through color and width changes | N |
| 5 | Interactive area | Extends the minimum touch target (48px height) for accessibility compliance | N |
| 6 | Focus indicator | Triple contrasting border that indicates keyboard focus for accessibility | N |

---

## Layouts

**`Text + icon`** Combines text with an icon to enhance clarity and recognition. Ideal when a visual cue helps reinforce the filter's meaning.

**`Text only`** Displays only text, offering a clean and minimalistic look. Best suited for category-based filters that do not require additional visual elements.

**`Icon only`** Uses only an icon, making it a compact option for limited space. Works well with universally recognized symbols, such as a heart for favorites or a checkmark for selection.

---

## layouts_do_&_dont 👈🤔

✅ **Do:** Use text + icon layout when icons add meaningful context to help users quickly identify suggestions  
❌ **Don't:** Add decorative icons that don't reinforce the suggestion's meaning or purpose

✅ **Do:** Use text-only layout for simple, self-explanatory suggestions that don't need visual reinforcement  
❌ **Don't:** Default to text + icon when the label alone clearly communicates the suggestion

✅ **Do:** Reserve icon-only layout for universally recognized symbols that users can identify without labels  
❌ **Don't:** Use icon-only chips with ambiguous or unfamiliar icons that require text explanation

✅ **Do:** Maintain consistent layout patterns within a single chip set for visual coherence  
❌ **Don't:** Mix different layouts arbitrarily within the same suggestion chip group

✅ **Do:** Consider the context and user familiarity when selecting the appropriate layout variant  
❌ **Don't:** Choose layouts based solely on aesthetic preference without considering usability

---

# Specs

## States

**`Enabled`** The chip is active and available for interaction. It is displayed in its standard style without additional effects.

**`Hover`** The appearance of the chip changes when the cursor hovers over it. This includes a color change for the border and the chip's content.

**`Pressed`** The active state when the chip is being pressed. Accompanied by a color change in the content and border.

**`Disabled`** The chip is unavailable for interaction. It is visually represented with a muted color change in the content and border (reduced brightness and contrast).

**`Focus`** The state when the chip receives focus (e.g., during keyboard navigation). It features a triple contrasting border to indicate the active element.

**`Skeleton`** Displays a placeholder chip while the content is loading. It appears as a semi-transparent gray block without content.

---

## Layout and spacing

🚧 Content to be added

---

# Accessibility 👈🤖

## Accessibility intro

Suggestion chips must meet WCAG 2.2 Level AA requirements for interactive controls, ensuring all users can perceive, navigate, and activate suggestions regardless of input method or assistive technology. For comprehensive accessibility guidance, see the [Orange Unified Design System Accessibility Overview](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability).

---

## Accessibility Challenges

Suggestion chips present unique accessibility challenges because they function as dynamic, contextual controls that appear based on user input. They must communicate their purpose, availability, and interaction patterns to all users while maintaining a compact visual footprint.

### Key Challenges
- Ensuring chips are discoverable and announced when they dynamically appear
- Communicating the suggestion's purpose and action clearly to screen reader users
- Providing sufficient touch targets and focus indicators within compact dimensions
- Managing focus when suggestions are dismissed or new suggestions appear

### Critical Success Factors
1. Each chip must have an accessible name that clearly describes its action (WCAG 4.1.2)
2. Keyboard users must be able to navigate and activate all chips (WCAG 2.1.1)
3. Focus indicators must be clearly visible with ≥3:1 contrast ratio (WCAG 2.4.7)
4. Dynamic suggestion updates should be announced to screen readers appropriately

---

## Design Requirements

### Structure & Labels
- [ ] **Accessible name**: Ensure each chip has a clear, descriptive label via visible text or `aria-label`
- [ ] **Semantic role**: Use `role="button"` for actionable chips or native `<button>` element ([Semantic HTML](https://a11y-guidelines.orange.com/en/web/develop/semantic-html/))
- [ ] **Chip sets**: Group related chips with `role="group"` and provide an accessible group label

### Visual Design
- [ ] **Focus indicator**: Triple contrasting border with ≥3:1 contrast against background ([Focus visibility](https://a11y-guidelines.orange.com/en/web/design/focus-visible/))
- [ ] **Color contrast**: Label text must have ≥4.5:1 contrast in all states ([Color contrast](https://a11y-guidelines.orange.com/en/web/design/colors-and-contrasts/))
- [ ] **Touch target**: Maintain 48px minimum interactive area for mobile accessibility

### Content
- [ ] **Clear labels**: ❌ "Opt1" / ✅ "Search nearby restaurants" ([Clear content](https://a11y-guidelines.orange.com/en/web/design/editorial-content/))
- [ ] **Concise text**: Keep labels between 1-5 words for quick scanning and comprehension

---

## Testing Checklist

### Screen Reader Testing
- [ ] Test with NVDA (Windows), JAWS (Windows), VoiceOver (macOS/iOS), TalkBack (Android)
- [ ] Verify chip labels announced, role communicated as button, dynamic updates spoken

### Keyboard Testing
- [ ] Tab navigation reaches all chips, Arrow keys navigate within chip sets
- [ ] Enter/Space activates chip, focus indicator visible (≥3:1 contrast)

Resources: [Orange Accessibility Testing Guide](https://a11y-guidelines.orange.com/en/web/testing/)

---

## Key WCAG Criteria

- **2.1.1 Keyboard** (A): All chip functionality operable via keyboard without timing requirements
- **2.4.7 Focus Visible** (AA): Visible focus indicator with ≥3:1 contrast on all interactive chips
- **4.1.2 Name, Role, Value** (A): Chips expose accessible name and button role to assistive technology
- **1.4.3 Contrast (Minimum)** (AA): Text and icons maintain ≥4.5:1 contrast in all states
- **2.5.5 Target Size (Enhanced)** (AAA): Interactive area meets 48×48px minimum for touch accessibility

For complete reference: [Orange Accessibility Guidelines - Interactive Components](https://a11y-guidelines.orange.com/en/web/components-examples/)

---

## Additional Resources

- [Orange Accessibility Guidelines - Buttons and Interactive Elements](https://a11y-guidelines.orange.com/en/web/components-examples/)
- [WCAG 2.2 Understanding 2.1.1 Keyboard](https://www.w3.org/WAI/WCAG22/Understanding/keyboard)
- [W3C ARIA Authoring Practices - Button Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/button/)
- [Orange Design System - Accessibility & Sustainability](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability)

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Nov 12, 2025 | 1.4.0 | • Label text with bold replaced by medium. | Anton Astafev |
| Jul 21, 2025 | 1.3.0 | • The name of the family to which this component belongs is changing: Input → Control. As a result, the token naming convention is being updated. • Several design token updates: [Component tokens changelog 1.3.0](https://www.figma.com/design/Co2t6wHMf4GB9NJVGs2Hes/-OUDS-Core-Lib--Design-tokens?m=auto&node-id=9280-2568&t=HLVB4jOd35DWr8Bj-1) | Maxime Tonnerre |
| Jul 2, 2025 | 1.2.0 | • Modification of the typographic alignment "Label text", the alignment is now centered. | Maxime Tonnerre |
| Jun 13, 2025 | 1.1.0 | • Modification of the minimum height of the frame containing the component to increase the interactive area (48px). Component token: $ouds-input-chip-size-min-height-interactive-area • Modification of the semantic token corresponding to the inline padding used when displaying an icon. Component token: $ouds-input-chip-space-padding-inline-icon Semantic token: $ouds-space-padding-inline-sm • Modification of the typographic alignment of the "Content" frame, the alignment is now centered. | Maxime Tonnerre |
| Apr 9, 2025 | 1.0.0 | • Component creation | Anton Astafev |