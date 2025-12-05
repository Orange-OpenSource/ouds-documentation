# Guideline

## Intro 👈🤖

Expand Link is a lightweight text control that reveals or collapses additional content through progressive disclosure.

---

## Definition

An Expand link is a lightweight control used to reveal or collapse additional content through a text link, rather than a button. It is best suited for inline contexts where minimal visual weight is required, keeping the layout clean while still allowing access to extended information.

---

## Best for 👈🤔

✅ Progressive disclosure of supplementary information without page navigation

✅ FAQ sections where questions reveal detailed answers inline

✅ Mobile-first interfaces where vertical space is limited

✅ Inline content expansion within paragraphs or compact layouts

✅ Reducing visual clutter while maintaining access to extended details

✅ Product descriptions with "Read more" functionality

✅ Help text or contextual hints that users can optionally view

✅ Nested information structures requiring lightweight toggle controls

✅ Information-dense dashboards where content density must be managed

✅ Form sections with optional additional fields or explanations

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Label | Text that describes the action or content to be revealed/collapsed | N |
| 2 | Chevron icon | Visual indicator showing expanded/collapsed state direction | N |
| 3 | Focus ring | Visible outline indicating keyboard focus for accessibility | N |
| 4 | Underline | Visual affordance on hover/focus indicating interactivity | Y |
| 5 | Container | Touch target area ensuring minimum interactive size | N |
| 6 | Skeleton placeholder | Loading state indicator while content loads | Y |

---

## Expanded

**`False`** State indicates that the content linked to the expand control is currently hidden. The link should suggest that additional information can be revealed.

**`True`** State indicates that the content has been revealed. The link updates visually to indicate that the section is open and can be collapsed again.

---

## expanded_do_&_dont 👈🤔

✅ **Do:** Use clear, action-oriented labels like "Show details" or "View more" that indicate what will be revealed  
❌ **Don't:** Use vague labels like "Click here" or "More" that don't describe the hidden content

✅ **Do:** Animate the chevron icon rotation to provide visual feedback of state change  
❌ **Don't:** Change the icon abruptly without transition, which can disorient users

✅ **Do:** Maintain the expanded state when users navigate away and return to preserve context  
❌ **Don't:** Automatically collapse content on page revisit, forcing users to re-expand

✅ **Do:** Position expanded content directly below the trigger for clear visual association  
❌ **Don't:** Display revealed content far from the trigger, breaking the spatial relationship

✅ **Do:** Allow multiple expand links to be open simultaneously for user flexibility  
❌ **Don't:** Force accordion behavior (auto-collapse) unless content relationships require it

---

## Sizes

**`Default`** This is the default size of the component.
This size is used for the vast majority of applications.

**`Small`** This size can be particularly useful in an information-dense interface or in the construction of a template or component requiring the use of small elements (in an "In-line alert" component, for example).

---

## sizes_do_&_dont 👈🤔

✅ **Do:** Use the default size for standalone expand links in primary content areas  
❌ **Don't:** Mix different sizes of expand links within the same visual grouping

✅ **Do:** Use the small size within compact components like alerts, cards, or data tables  
❌ **Don't:** Use small size when the expand link is the primary action on a page

✅ **Do:** Ensure touch targets meet minimum 44×44px requirements regardless of visual size  
❌ **Don't:** Reduce the interactive area below accessibility guidelines for small size

✅ **Do:** Scale font size proportionally with the size variant using design tokens  
❌ **Don't:** Override typography tokens with fixed pixel values

✅ **Do:** Maintain consistent chevron icon proportions relative to label text  
❌ **Don't:** Use oversized or undersized icons that create visual imbalance

---

## Specific component: On colored bg

This variant ensures a sufficiently high level of accessibility when the component is used on a background that is "out of control".

**To invert color**
• In light mode: For a black finish
• In dark mode: For a white finish

---

## specific_component:_on_colored_bg_do_&_dont 👈🤔

✅ **Do:** Use the "On colored bg" variant when placing expand links on colored, image, or gradient backgrounds  
❌ **Don't:** Use the standard variant on backgrounds where contrast cannot be guaranteed

✅ **Do:** Test color contrast ratios meet WCAG AA (4.5:1 for text) in both light and dark modes  
❌ **Don't:** Assume the inverted variant will work without verifying actual contrast values

✅ **Do:** Apply consistent inverted color treatment to all interactive states (hover, focus, pressed)  
❌ **Don't:** Mix standard and inverted color schemes within the same background context

✅ **Do:** Use design tokens for color management to ensure automatic theme switching  
❌ **Don't:** Hard-code color values that won't adapt to light/dark mode changes

✅ **Do:** Ensure focus indicators remain visible against the colored background  
❌ **Don't:** Allow focus rings to blend into backgrounds, making keyboard navigation invisible

---

# Specs

## States

**`Enabled`** The default state when the link is available for interaction and displayed with a clear label.

**`Hover`** The state when a user hovers over the link. Provides a visual cue that the element is interactive.

**`Focus`** The state when the link is selected via keyboard or voice commands. Typically shown with an outline or highlight to ensure accessibility.

**`Pressed`** A transient state indicating that the user has clicked the link and the action is being executed.

**`Disabled`** The state when the link is not available for interaction, such as when expanding or collapsing is not possible at the moment.

**`Skeleton`** A placeholder state that indicates where the link will appear once fully loaded. Improves perceived performance by showing upcoming interactivity.

---

## Layout and spacing

🚧 Content to be added

---

# Accessibility 👈🤖

## Accessibility intro

Expand Link must be fully operable via keyboard and communicate its expanded/collapsed state to assistive technologies per WCAG 2.2 AA requirements. For comprehensive accessibility guidance, see the [Orange Unified Design System Accessibility Overview](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability).

---

## Accessibility Challenges

Expand Link presents unique accessibility challenges because users must understand both the interactive nature of the control and the current state of the associated content. Screen reader users cannot see the chevron direction, so expanded/collapsed state must be programmatically communicated.

### Key Challenges
- Communicating binary expanded/collapsed state to non-visual users
- Ensuring keyboard operability with standard activation keys
- Maintaining visible focus indicators against varying backgrounds
- Preserving content relationships when content visibility changes

### Critical Success Factors
1. Use `aria-expanded` attribute reflecting true/false state (WCAG 4.1.2)
2. Implement `button` role for the interactive trigger element
3. Ensure minimum 44×44px touch target for mobile accessibility
4. Provide visible focus indicator with ≥3:1 contrast ratio (WCAG 2.4.7)

---

## Design Requirements

### Structure & Labels
- [ ] **Semantic role**: Use `<button>` element with `aria-expanded` attribute ([Orange - Interactive elements](https://a11y-guidelines.orange.com/en/web/develop/interactive-components/))
- [ ] **Programmatic relationship**: Connect trigger to content via `aria-controls` referencing content ID
- [ ] **Accessible name**: Label clearly describes action or content, available to assistive technology

### Visual Design
- [ ] **Focus indicator**: Visible ring with ≥3:1 contrast against adjacent colors ([Orange - Focus visibility](https://a11y-guidelines.orange.com/en/web/design/focus-visibility/))
- [ ] **State indication**: Chevron direction change provides visual expanded/collapsed feedback
- [ ] **Disabled state**: Reduced opacity (0.2-0.28) indicates non-interactive state

### Content
- [ ] **Label clarity**: ❌ "Click here" / ✅ "Show payment options" ([Orange - Link labeling](https://a11y-guidelines.orange.com/en/web/design/navigation/))
- [ ] **State announcement**: Screen readers announce "expanded" or "collapsed" with label

---

## Testing Checklist

### Screen Reader Testing
- [ ] Test with NVDA (Windows), JAWS (Windows), VoiceOver (macOS/iOS), TalkBack (Android)
- [ ] Verify label announced, expanded/collapsed state communicated, content accessible when revealed

### Keyboard Testing
- [ ] Tab navigates to control, Enter/Space toggles state, focus visible throughout
- [ ] Verify expanded content receives focus appropriately after reveal

Resources: [Orange Accessibility Testing Guide](https://a11y-guidelines.orange.com/en/web/test/)

---

## Key WCAG Criteria

- **2.1.1 Keyboard** (A): Expand Link operable via Enter and Space keys without timing requirements
- **2.4.7 Focus Visible** (AA): Focus ring visible with ≥3:1 contrast on all background variants
- **4.1.2 Name, Role, Value** (A): `aria-expanded` attribute reflects current state, button role identified
- **1.4.3 Contrast (Minimum)** (AA): Label text maintains 4.5:1 contrast in all states
- **2.5.5 Target Size** (AAA): Interactive area meets 44×44px minimum for touch accessibility

For complete reference: [Orange Accessibility Guidelines - Interactive Components](https://a11y-guidelines.orange.com/en/web/components-examples/)

---

## Additional Resources

- [W3C WAI-ARIA Disclosure Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/)
- [Orange Accessibility Guidelines - Interactive Components](https://a11y-guidelines.orange.com/en/web/develop/interactive-components/)
- [WCAG 2.2 Understanding 4.1.2 Name, Role, Value](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html)
- [Orange Design System - Accessibility & Sustainability](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability)

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Oct 10, 2025 | 2.3.0 | The specific component "On colored bg" has been split into two distinct components: • A public version offering traditional management of dark and light modes • A private version (allowing the core team to nest the component with other components) offering customized mode management with four possible configurations: ‣ Always in light mode ‣ Always in dark mode ‣ Light to dark mode ‣ Dark to light mode • Consequently, for the private version, the name of the "Inverted color" variant has been replaced to "Mode control". | Maxime Tonnerre |
| Sep 28, 2025 | 2.2.0 | • Add a leading icon and a hidden boolean property for multi-theme management • Add 2 new component tokens for managing the show/hide visibility of the icon: [Component tokens changelog 1.6.0](https://www.figma.com/design/Co2t6wHMf4GB9NJVGs2Hes/-OUDS-Core-Lib--Design-tokens?m=auto&node-id=9280-2568&t=HLVB4jOd35DWr8Bj-1) | Jérôme Regnier |
| Jul 21, 2025 | 2.1.0 | • Several design token updates: [Component tokens changelog 1.3.0](https://www.figma.com/design/Co2t6wHMf4GB9NJVGs2Hes/-OUDS-Core-Lib--Design-tokens?m=auto&node-id=9280-2568&t=HLVB4jOd35DWr8Bj-1) | Maxime Tonnerre |
| Apr 19, 2025 | 2.0.0 | • Creation of "On colored bg" variant | Maxime Tonnerre |
| Dec 3, 2024 | 1.0.0 | • Component creation | Maxime Tonnerre |