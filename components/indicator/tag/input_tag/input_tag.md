# Guideline

## Intro 👈🤖

Input tag allows users to enter and manage multiple values as removable tags within a text input field.

---

## Definition

A Input tag is a component that allows users to enter multiple values, each represented as a tag. As users type and submit values (usually by pressing enter, comma, or tab), each value is transformed into a Tag. Input tags are often used for adding labels, categories, or participants.

---

## Best for 👈🤔

✅ Adding multiple email recipients in a compose or sharing interface

✅ Creating user-defined labels, categories, or keywords for content organization

✅ Selecting multiple participants, assignees, or collaborators from a list

✅ Building custom filters or search criteria with multiple terms

✅ Tagging content with metadata for categorization and discoverability

✅ Managing skill sets, interests, or attributes in profile forms

✅ Creating comma-separated lists that benefit from visual token representation

✅ Situations where users need to easily add and remove multiple discrete values

✅ Forms requiring multiple selections from an open-ended set of options

✅ Interfaces where entered values need clear visual distinction from pending input

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Container | Provides the visual boundary with rounded pill shape and holds all tag elements | N |
| 2 | Label text | Displays the user-entered value as readable text within the tag | N |
| 3 | Close icon | Enables users to remove the tag by clicking or tapping | N |
| 4 | Border | Indicates the tag boundary and changes appearance based on state | N |
| 5 | Background | Provides visual distinction and changes color based on interaction state | N |
| 6 | Focus ring | Indicates keyboard focus state for accessibility compliance | Y |

---

# Specs

## States

**`Enabled`** The default state of the Input tag. The tag is fully interactive, allowing users to read the label and remove the tag if needed.

**`Hover`** Displayed when a user hovers the cursor over the tag. Visual cues (such as a highlighted border) indicate that the tag is interactive and can be removed.

**`Pressed`** Shown when the tag is actively being clicked or tapped. The tag appears pressed or highlighted, providing feedback that the action is being performed.

**`Disabled`** Indicates that the tag is non-interactive. The tag appears faded or greyed out, and users cannot interact with it or remove it.

**`Focus`** Appears when the tag is focused, typically via keyboard navigation or screen reader. A distinct outline or highlight indicates that the tag is in focus, supporting accessibility.

**`Skeleton`** A placeholder state displayed while content is loading. The tag appears as a simplified, greyed-out shape without label text, indicating to users that tags will soon be available.

---

## Layout and spacing

🚧 Content to be added

---

# Accessibility 👈🤖

## Accessibility intro

Input tag components must meet WCAG 2.2 Level AA standards to ensure all users can add, view, and remove tags effectively using keyboard, mouse, or assistive technologies. For comprehensive accessibility guidance, see the [Orange Unified Design System Accessibility Overview](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability).

---

## Accessibility Challenges

Input tags present unique accessibility challenges because they combine text input functionality with multiple interactive elements (individual tags with remove actions) in a single component. Users must be able to navigate between tags, understand each tag's content, and remove specific tags—all while managing the overall input field.

### Key Challenges

- Multiple focusable elements within a single input container require clear navigation patterns
- Remove actions must be discoverable and operable without mouse interaction
- State changes (adding/removing tags) must be announced to screen reader users
- Visual distinction between tags and pending input text must be perceivable

### Critical Success Factors

1. Implement `role="listbox"` or `role="group"` for the tag container with proper ARIA labeling (WCAG 4.1.2)
2. Ensure each tag has `role="option"` with accessible remove button (`aria-label="Remove [tag name]"`)
3. Provide keyboard navigation using Arrow keys between tags and Tab to exit the component
4. Announce tag additions and removals to assistive technologies via live regions

---

## Design Requirements

### Structure & Labels

- [ ] **Container role**: Use `role="group"` or `role="listbox"` with `aria-label` describing the input purpose
- [ ] **Tag identification**: Each tag uses `role="option"` with accessible name from label text
- [ ] **Remove button**: Close icon has `aria-label="Remove [tag name]"` ([Orange ARIA guidelines](https://a11y-guidelines.orange.com/en/web/develop/textual-content/))

### Visual Design

- [ ] **Focus indicator**: 3:1 minimum contrast ratio with ≥2px visible border ([Focus visibility](https://a11y-guidelines.orange.com/en/web/design/focus-visibility/))
- [ ] **State differentiation**: Enabled, hover, pressed, disabled states visually distinct with sufficient contrast
- [ ] **Text contrast**: Label text meets 4.5:1 contrast ratio against background

### Content

- [ ] **Concise labels**: ❌ "Click here to remove this particular tag item" / ✅ "Remove Marketing" ([Clear labels](https://a11y-guidelines.orange.com/en/web/design/content/))
- [ ] **Consistent terminology**: Use same remove action label pattern across all tags

---

## Testing Checklist

### Screen Reader Testing

- [ ] Test with NVDA (Windows), JAWS (Windows), VoiceOver (macOS/iOS), TalkBack (Android)
- [ ] Verify tag labels announced, remove button purpose clear, state changes (add/remove) spoken via live region

### Keyboard Testing

- [ ] Tab enters component, Arrow keys navigate between tags, Tab exits to next element
- [ ] Backspace/Delete removes focused tag, Enter/Space activates remove button, focus indicator visible (≥3:1 contrast)

### Functional Testing

- [ ] Verify disabled state prevents all interaction and is announced as "disabled" or "unavailable"

Resources: [Orange Accessibility Testing Guide](https://a11y-guidelines.orange.com/en/web/test/)

---

## Key WCAG Criteria

- **2.1.1 Keyboard** (A): All tag interactions (focus, navigate, remove) operable via keyboard without timing requirements
- **2.4.7 Focus Visible** (AA): Visible focus indicator with ≥3:1 contrast on each tag and remove button
- **4.1.2 Name, Role, Value** (A): Tags use proper ARIA roles, names include label text, states communicated programmatically
- **1.4.3 Contrast (Minimum)** (AA): Label text maintains 4.5:1 contrast ratio in all states
- **4.1.3 Status Messages** (AA): Tag additions and removals announced without moving focus via `aria-live` region

For complete reference: [Orange Accessibility Guidelines - Components](https://a11y-guidelines.orange.com/en/web/components-examples/)

---

## Additional Resources

- [Orange Accessibility Guidelines - Form Components](https://a11y-guidelines.orange.com/en/web/components-examples/)
- [WCAG 2.2 Understanding - Name, Role, Value](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html)
- [WAI-ARIA Authoring Practices - Listbox Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/listbox/)
- [Orange Design System - Accessibility & Sustainability](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability)

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Nov 12, 2025 | 1.2.0 | • Label text with bold replaced by medium | Anton Astafev |
| Jul 21, 2025 | 1.1.0 | • Several design token updates: [Component tokens changelog 1.3.0](https://www.figma.com/design/Co2t6wHMf4GB9NJVGs2Hes/-OUDS-Core-Lib--Design-tokens?m=auto&node-id=9280-2568&t=HLVB4jOd35DWr8Bj-1) | Maxime Tonnerre |
| Mai 20, 2025 | 1.0.0 | • Component creation | Anton Astafev |