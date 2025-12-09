# Guideline

## Intro 👈🤖

A badge count is a non-interactive visual indicator that displays numeric values to communicate quantities or notification counts.

---

## Definition

🚧 Missing from source: Definition section in badge_count_overview.md

---

## Best for 👈🤔

✅ Displaying unread notification counts on navigation icons or menu items

✅ Showing the number of items in a shopping cart or basket

✅ Indicating active filter counts in search or data table interfaces

✅ Communicating pending task or action quantities requiring user attention

✅ Displaying unread message counts in messaging or email applications

✅ Showing the number of updates or alerts in system status indicators

✅ Indicating quantities in tabbed interfaces where counts provide useful context

✅ Communicating real-time count changes for collaborative or dynamic content

✅ Displaying error or warning counts that need user acknowledgment

✅ Showing selection counts in multi-select or batch operation interfaces

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Container | Pill-shaped background that holds the count value and provides visual emphasis through status color | N |
| 2 | Count label | Numeric text displaying the quantity value, centered within the container | N |
| 3 | Status color | Background color indicating semantic meaning: Neutral, Accent, Positive, Info, Warning, or Negative | N |
| 4 | Padding | Horizontal spacing ensuring consistent internal layout regardless of digit count | N |
| 5 | Border radius | Pill shape (2000px radius) creating the characteristic rounded appearance | N |

---

🚧 Missing from source: badge_count_overview.md file required (no additional sections found to inject)

---

# Specs

## States

🚧 Missing from source: States section in badge_count_overview.md

Based on Figma component data, the Badge Count supports the following states:

**Enabled state**: The badge displays with full status color styling and readable count text. The contrast ratio between content and background meets the 4.5:1 minimum requirement.

**Disabled state**: The badge displays with a muted background color (`color-action-disabled`) and reduced contrast text (`color-content-on-action-disabled`), indicating the associated element or feature is unavailable.

---

## Layout and spacing

🚧 Content to be added

---

# Accessibility 👈🤖

## Accessibility intro

Badge Count components must meet WCAG 2.2 Level AA standards for color contrast, status communication, and assistive technology compatibility. For comprehensive accessibility guidance, see the [Orange Unified Design System Accessibility Overview](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability).

---

## Accessibility Challenges

Badge counts present unique accessibility challenges because they are non-interactive visual indicators that communicate dynamic numeric information. Users must be able to perceive badge updates through multiple channels, and screen reader users need equivalent access to count changes without requiring focus navigation to the badge element.

### Key Challenges
- Color-only status differentiation may exclude users with color vision deficiencies
- Dynamic count updates may not be announced to screen reader users
- Small text size within badges can impact readability for users with low vision
- Non-interactive nature means standard focus-based announcement patterns don't apply

### Critical Success Factors
1. Maintain 4.5:1 minimum contrast ratio between count text and background (WCAG 1.4.3)
2. Provide programmatic context through `aria-label` or adjacent text for screen readers
3. Use ARIA live regions to announce count changes when updates occur dynamically
4. Ensure status meaning is conveyed through more than color alone

---

## Design Requirements

### Structure & Labels
- [ ] **Accessible context**: Provide descriptive text via `aria-label` or visually hidden text (e.g., "5 unread messages" not just "5") ([Orange labeling guidelines](https://a11y-guidelines.orange.com/en/web/develop/textual-content/))
- [ ] **Non-interactive element**: Badge should not receive keyboard focus as it is purely informational (WCAG 2.4.3)
- [ ] **Semantic association**: Position badge adjacent to its related element so context is clear to all users

### Visual Design
- [ ] **Text contrast**: Minimum 4.5:1 contrast ratio between count and background color ([Orange contrast guidelines](https://a11y-guidelines.orange.com/en/web/design/colors-and-contrasts/))
- [ ] **Color independence**: Don't rely solely on color to convey status; combine with text labels or icons when critical
- [ ] **Minimum size**: Ensure count text meets minimum 12px font size for readability

### Content
- [ ] **Meaningful counts**: ❌ "5" / ✅ "5 notifications" (via accessible label) ([Orange content guidelines](https://a11y-guidelines.orange.com/en/web/develop/textual-content/))
- [ ] **Truncation clarity**: Use "99+" pattern for large numbers with accessible full count available

---

## Testing Checklist

### Screen Reader Testing
- [ ] Test with NVDA (Windows), JAWS (Windows), VoiceOver (macOS/iOS), TalkBack (Android)
- [ ] Verify badge context announced correctly, count values read accurately, status meaning communicated

### Keyboard Testing
- [ ] Confirm badge does not receive focus (non-interactive)
- [ ] Verify associated interactive element (icon, button) is keyboard accessible and announces badge context

### Live Region Testing
- [ ] Verify count changes announced via `aria-live="polite"` when updates occur dynamically
- [ ] Confirm announcements don't interrupt critical user tasks

Resources: [Orange Accessibility Testing Guide](https://a11y-guidelines.orange.com/en/web/test/)

---

## Key WCAG Criteria

- **1.4.3 Contrast (Minimum)** (AA): Count text must have 4.5:1 contrast ratio against badge background
- **1.4.1 Use of Color** (A): Status information conveyed by color must also be available through text or context
- **4.1.3 Status Messages** (AA): Dynamic count updates must be programmatically announced without receiving focus
- **1.1.1 Non-text Content** (A): Provide accessible name describing the badge's purpose and count context
- **2.4.3 Focus Order** (A): Badge should not appear in keyboard focus sequence as non-interactive element

For complete reference: [Orange Accessibility Guidelines - Component Examples](https://a11y-guidelines.orange.com/en/web/components-examples/)

---

## Additional Resources

- [Orange Accessibility Guidelines - Colors and Contrasts](https://a11y-guidelines.orange.com/en/web/design/colors-and-contrasts/)
- [WCAG 2.2 Understanding Status Messages (4.1.3)](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html)
- [W3C ARIA Live Regions](https://www.w3.org/WAI/WCAG21/Techniques/aria/ARIA19)
- [Orange Design System - Accessibility & Sustainability](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability)

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Oct 14, 2025 | 1.2.0 | • The component now has two states: Enabled and Disabled. • Documentation has been updated and published in Zeroeight, with use case examples provided for every state. • The colors and background tokens for the functional states of the positive and info statuses have been changed. • The minimum required contrast ratio has been corrected from 3:1 to 4.5:1 between content (count) and background for Enable state. For the "Status neutral" variant: • The content token "color-content-on-status-neutral-emphasized" has been replaced by the token "color-content-inverse" • The surface token "color-surface-status-neutral-emphasized" has been replaced by the token "color-surface-inverse-high" | Anton Astafev |
| Jun 16, 2025 | 1.1.0 | • "Accent" variant added | Maxime Tonnerre |
| Mai 9, 2025 | 1.0.0 | • Component creation | Anton Astafev |