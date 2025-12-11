# Guideline

## Intro 👈🤖

Badge Count is a compact numerical indicator that displays quantities like unread notifications, item counts, or pending actions on interface elements.

---

## Definition

The Badge is a small UI element used to highlight status, notifications, or categorization within an interface. It is often displayed as a label or indicator with a distinct background color and text.

**Usage:**
• Display numerical values (e.g., unread messages, notifications).

---

## Best for 👈🤔

✅ Displaying unread message or notification counts on navigation icons

✅ Showing item quantities in shopping carts or baskets

✅ Indicating pending tasks or action items requiring attention

✅ Communicating status counts on tabs or navigation items

✅ Highlighting new content arrivals in feeds or inboxes

✅ Representing active filter counts in data tables

✅ Showing selected item quantities in multi-select interfaces

✅ Displaying error or warning counts in system dashboards

✅ Indicating unprocessed queue items in workflow interfaces

✅ Communicating real-time count changes in collaborative tools

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Container | Pill-shaped background that holds the count value and provides visual emphasis through status-specific colors | N |
| 2 | Count text | Numeric value displayed within the container indicating quantity or amount | N |
| 3 | Status color | Background color that conveys semantic meaning (neutral, accent, positive, info, warning, negative) | N |
| 4 | Typography | Label font styling applied to the count text for readability at small sizes | N |
| 5 | Padding | Horizontal spacing within the container that ensures count text has adequate breathing room | N |
| 6 | Minimum width | Constraint ensuring the badge maintains a circular shape for single-digit counts | N |

---

## Status

Badges have seven states depending on the context of the information they represent. Each state is designed to convey a specific meaning and ensure clarity in communication.

**`Neutral`** Used for general labels without specific emphasis.

**`Accent`** Employed to highlight discovery or exploration-related content.

**`Positive`** Indicates success, completion, or approval.

**`Info`** Provides informational context without urgency.

**`Warning`** Negatives the user to potential risks or cautionary messages.

**`Negative`** Draws attention to important or critical information.
Often used for errors, restrictions, or urgent messages, but not exclusively for failures.

---

## status_do_&_dont 👈🤔

✅ **Do:** Use semantic status colors consistently throughout the application to establish clear visual language for users  
❌ **Don't:** Use red/negative status for non-critical information, as it creates unnecessary alarm and diminishes urgency perception

✅ **Do:** Reserve the Accent status for highlighting promotional or discovery-related counts that encourage exploration  
❌ **Don't:** Mix status meanings across contexts—a color should always represent the same semantic meaning

✅ **Do:** Use Neutral status as the default when the count doesn't require semantic emphasis or urgency  
❌ **Don't:** Overuse Warning or Negative statuses, as they lose impact when applied to non-urgent information

✅ **Do:** Apply Positive status to communicate successful completions, approvals, or beneficial counts  
❌ **Don't:** Use multiple different status colors in close proximity without clear contextual differentiation

✅ **Do:** Consider colorblind users by ensuring status meaning is conveyed through context, not color alone  
❌ **Don't:** Rely solely on status color to communicate critical information—pair with labels or icons when essential

---

## Size

**`Medium`** The default size, providing a balance between visibility and space efficiency, suitable for most use cases.

**`Large`** A prominent badge for drawing more attention, often used in dashboards or highlighted sections.

---

## size_do_&_dont 👈🤔

✅ **Do:** Use Medium size (16px) as the default for most interface contexts where badges appear alongside icons or text  
❌ **Don't:** Use Large size in compact layouts where it may crowd adjacent elements or disrupt visual hierarchy

✅ **Do:** Choose Large size (20px) for dashboards, cards, or areas where the count requires prominent visibility  
❌ **Don't:** Mix badge sizes inconsistently within the same component or navigation pattern

✅ **Do:** Ensure badge size is proportional to the parent element it's associated with (icons, buttons, avatars)  
❌ **Don't:** Use badges so small they become illegible or difficult to distinguish from decorative dots

✅ **Do:** Consider touch target requirements when badges are placed on interactive elements in mobile contexts  
❌ **Don't:** Increase badge size solely to draw attention—use status colors or positioning instead

✅ **Do:** Maintain consistent size selection across similar use cases throughout the application  
❌ **Don't:** Choose Large size for single-digit counts where Medium provides sufficient visibility

---

# Specs

## States

**`Enabled`** The active state of a badge. Includes all possible visual statuses that represent the current state of the system or element (e.g., success, warning, error, information, etc.). Used when the badge should attract attention and convey meaningful information.

**`Disabled`** The inactive state of a badge. Used to indicate that the user isn't allowed to interact with an element, or when the status is unavailable. It appears less prominent and serves as a secondary indication.
Badges with content keep the Enabled content but change their visual appearance.

---

## Layout and spacing

🚧 Content to be added

---

# Accessibility 👈🤖

## Accessibility intro

Badge Count components must meet WCAG 2.2 Level AA requirements for color contrast, non-text content identification, and status message communication. For comprehensive accessibility guidance, see the [Orange Unified Design System Accessibility Overview](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability).

---

## Accessibility Challenges

Badge counts present unique accessibility challenges because they convey dynamic numerical information through small visual indicators that must be perceivable by all users regardless of ability. The compact size, reliance on color for status meaning, and non-interactive nature require careful implementation to ensure screen reader users receive equivalent information.

### Key Challenges

- Small size makes meeting 4.5:1 contrast ratio critical for text legibility
- Status colors must not be the sole method of conveying semantic meaning
- Dynamic count updates need to be announced to assistive technology users
- Non-interactive nature means badges should not receive keyboard focus

### Critical Success Factors

1. Maintain 4.5:1 minimum contrast ratio between count text and background (WCAG 1.4.3)
2. Provide programmatic text alternatives via `aria-label` or visually hidden text
3. Use `aria-live` regions for dynamic count updates when contextually important
4. Ensure status meaning is conveyed through context, not color alone

---

## Design Requirements

### Structure & Labels

- [ ] **Accessible name**: Provide descriptive `aria-label` (e.g., "5 unread notifications") conveying count purpose ([Orange A11y - Accessible Name](https://a11y-guidelines.orange.com/en/web/develop/textual-content/))
- [ ] **Hidden text alternative**: Include visually hidden text for screen readers when badge is purely visual
- [ ] **Contextual association**: Ensure badge is programmatically associated with its parent element via proximity or `aria-describedby`

### Visual Design

- [ ] **Color contrast**: Minimum 4.5:1 ratio between count text and background color ([Orange A11y - Colors](https://a11y-guidelines.orange.com/en/web/design/colors-and-contrasts/))
- [ ] **Non-color identification**: Status meaning conveyed through context/labels, not color alone
- [ ] **Minimum size**: Ensure count text meets minimum target size for legibility

### Content

- [ ] **Meaningful counts**: ❌ "99+" without context / ✅ "99+ unread messages" with full context available
- [ ] **Truncation handling**: Provide full count value to assistive technology when visually truncated

---

## Testing Checklist

### Screen Reader Testing

- [ ] Test with NVDA (Windows), JAWS (Windows), VoiceOver (macOS/iOS), TalkBack (Android)
- [ ] Verify badge count and purpose are announced, status context communicated, dynamic updates spoken

### Keyboard Testing

- [ ] Confirm badge does not receive focus (non-interactive element)
- [ ] Verify parent interactive element announces badge information when focused

### Dynamic Updates Testing

- [ ] Verify `aria-live="polite"` announces count changes without interrupting user tasks
- [ ] Test that screen readers announce meaningful updates (e.g., "3 new notifications")

Resources: [Orange Accessibility Testing Guide](https://a11y-guidelines.orange.com/en/web/test/)

---

## Key WCAG Criteria

- **1.1.1 Non-text Content** (A): Badge count has text alternative accessible to assistive technology
- **1.4.1 Use of Color** (A): Status meaning not conveyed by color alone—context provides meaning
- **1.4.3 Contrast (Minimum)** (AA): Count text has 4.5:1 contrast ratio against badge background
- **4.1.2 Name, Role, Value** (A): Badge has accessible name describing count and purpose
- **4.1.3 Status Messages** (AA): Dynamic count updates announced via `aria-live` without focus change

For complete reference: [Orange Accessibility Guidelines - Web Components](https://a11y-guidelines.orange.com/en/web/components-examples/)

---

## Additional Resources

- [Orange Accessibility Guidelines - Textual Content](https://a11y-guidelines.orange.com/en/web/develop/textual-content/)
- [Orange Accessibility Guidelines - Colors and Contrasts](https://a11y-guidelines.orange.com/en/web/design/colors-and-contrasts/)
- [W3C WAI - ARIA Live Regions](https://www.w3.org/WAI/WCAG21/Techniques/aria/ARIA19)
- [Orange Design System - Accessibility & Sustainability](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability)

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Oct 14, 2025 | 1.2.0 | <ul><li>The component now has two states: Enabled and Disabled. <li>Documentation has been updated and published in Zeroeight, with use case examples provided for every state. <li>The colors and background tokens for the functional states of the positive and info statuses have been changed. <li>The minimum required contrast ratio has been corrected from 3:1 to 4.5:1 between content (count) and background for Enable state.</ul>For the "Status neutral" variant: <ul><li>The content token "color-content-on-status-neutral-emphasized" has been replaced by the token "color-content-inverse" <li>The surface token "color-surface-status-neutral-emphasized" has been replaced by the token "color-surface-inverse-high"</ul> | Anton Astafev |
| Jun 16, 2025 | 1.1.0 | <ul><li>"Accent" variant added</ul> | Maxime Tonnerre |
| Mai 9, 2025 | 1.0.0 | <ul><li>Component creation</ul> | Anton Astafev |