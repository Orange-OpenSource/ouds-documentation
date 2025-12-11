# Guideline

## Intro 👈🤖

A compact status indicator that uses color-coded icons to communicate system states, notifications, or categorization at a glance.

---

## Definition

The Badge is a small UI element used to highlight status, notifications, or categorization within an interface. It is often displayed as a label or indicator with a distinct background color and text.

**Usage:**
• Support badges with icons to visually reinforce meaning.

---

## Best for 👈🤔

✅ Indicating system status (success, warning, error, info) alongside other UI elements

✅ Providing non-interactive visual feedback on process completion or validation states

✅ Displaying functional alerts that require immediate user attention

✅ Communicating categorical information through semantic color coding

✅ Enhancing navigation items with status context without adding text labels

✅ Marking items in lists or cards that require attention or have specific states

✅ Showing availability or activity status in compact spaces

✅ Supplementing icons or avatars with contextual status information

✅ Indicating feature discovery or new content availability

✅ Providing secondary status information in dashboards and data tables

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Container | Circular background with status-specific color that houses the icon | N |
| 2 | Icon | Functional symbol that reinforces the semantic meaning of the status | N |
| 3 | Background color | Semantic color indicating status type (neutral, accent, positive, info, warning, negative) | N |
| 4 | Icon color | Contrasting color ensuring 4.5:1 minimum contrast ratio with background | N |

---

## State

**`Enabled`** The active state of a badge. Includes all possible visual statuses that represent the current state of the system or element (e.g., success, warning, error, information, etc.). Used when the badge should attract attention and convey meaningful information.

**`Disabled`** The inactive state of a badge. Used to indicate that the user isn't allowed to interact with an element, or when the status is unavailable. It appears less prominent and serves as a secondary indication.
Badges with content keep the Enabled content but change their visual appearance.

---

## state_do_&_dont 👈🤔

✅ **Do:** Use the enabled state when the badge conveys actionable or current status information that users need to see
❌ **Don't:** Use the disabled state as the default—reserve it for genuinely unavailable or inactive contexts

✅ **Do:** Ensure disabled badges maintain sufficient contrast to remain visible while appearing subdued
❌ **Don't:** Hide important status information by using the disabled state when the status is still relevant

✅ **Do:** Pair the badge state with the state of the parent component it accompanies (e.g., disabled button = disabled badge)
❌ **Don't:** Show an enabled badge on a disabled component, creating visual inconsistency

✅ **Do:** Use consistent visual treatment across all disabled badge variants to maintain predictability
❌ **Don't:** Apply different disabled styles to different status types, as this creates confusion

✅ **Do:** Consider whether the badge should be visible at all when disabled—remove it if it adds no value
❌ **Don't:** Keep disabled badges visible when they provide no useful information to the user

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

✅ **Do:** Use semantic colors consistently—green for positive outcomes, red for errors, yellow for warnings, blue for information
❌ **Don't:** Use semantic colors arbitrarily or swap their meanings across different contexts

✅ **Do:** Pair functional status badges (positive, warning, negative, info) with their designated functional icons
❌ **Don't:** Mix non-functional icons with functional status colors, as this breaks semantic meaning

✅ **Do:** Reserve the negative status for errors, restrictions, and truly critical information requiring immediate attention
❌ **Don't:** Overuse negative status badges for minor issues, which dilutes their impact

✅ **Do:** Use neutral status for general-purpose labeling where no specific semantic meaning is needed
❌ **Don't:** Use neutral status when a more specific semantic status would better communicate the meaning

✅ **Do:** Use accent status sparingly to highlight discovery or promotional content that stands out from standard statuses
❌ **Don't:** Use accent status as a substitute for positive status—they serve different purposes

---

## Size

**`Medium`** The default size, providing a balance between visibility and space efficiency, suitable for most use cases.

**`Large`** A prominent badge for drawing more attention, often used in dashboards or highlighted sections.

---

## size_do_&_dont 👈🤔

✅ **Do:** Use medium size as the default for most contexts, as it balances visibility with space efficiency
❌ **Don't:** Default to large size everywhere, which creates visual clutter and reduces the component's impact

✅ **Do:** Use large size when the badge needs to draw more attention in prominent locations like dashboards or feature highlights
❌ **Don't:** Use large badges in compact spaces like table cells or inline with small text

✅ **Do:** Maintain consistent sizing within the same context or component group
❌ **Don't:** Mix medium and large badges within the same list or table without clear hierarchy justification

✅ **Do:** Consider the surrounding element sizes when choosing badge size—match visual weight appropriately
❌ **Don't:** Place a large badge next to small icons or text where it overwhelms the primary content

✅ **Do:** Use size to establish visual hierarchy when multiple badges appear in the same view
❌ **Don't:** Rely solely on size differences to convey importance—combine with status colors and positioning

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

Badge Icon components must meet WCAG 2.2 Level AA standards, with particular attention to non-text contrast and status communication. For comprehensive accessibility guidance, see the [Orange Unified Design System Accessibility Overview](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability).

---

## Accessibility Challenges

Icon-only badges present unique accessibility challenges because they rely heavily on visual cues—color and iconography—to communicate status. Users with color vision deficiencies, cognitive impairments, or those using assistive technologies may not perceive the intended meaning without proper implementation.

### Key Challenges

- Color alone cannot convey status meaning—icons must be recognizable and labeled
- Small badge sizes make icons difficult to perceive for users with low vision
- Non-interactive badges must still communicate their purpose to screen readers
- Functional icons must maintain semantic consistency across all status types

### Critical Success Factors

1. Ensure 4.5:1 minimum contrast ratio between icon and background (WCAG 1.4.3)
2. Provide accessible names via `aria-label` when badges lack visible text
3. Use `aria-hidden="true"` when context is provided by surrounding elements
4. Pair icons with visible text labels whenever space permits

---

## Design Requirements

### Structure & Labels

- [ ] **Accessible name**: Provide `aria-label` describing status and meaning when no visible text exists
- [ ] **Semantic icons**: Use recognizable icons that reinforce status meaning (checkmark for positive, exclamation for warning)
- [ ] **Context association**: Position badges adjacent to the elements they describe

### Visual Design

- [ ] **Icon contrast**: Maintain 4.5:1 contrast ratio between icon and badge background ([Orange contrast guidelines](https://a11y-guidelines.orange.com/en/web/design/colors-and-contrasts/))
- [ ] **Badge contrast**: Ensure 3:1 contrast between badge background and page background
- [ ] **Size sufficiency**: Use minimum 16px badge size (medium) for icon visibility

### Content

- [ ] **Multi-cue communication**: ❌ Color only / ✅ Color + icon + text label ([Use of color](https://a11y-guidelines.orange.com/en/web/design/colors-and-contrasts/))
- [ ] **Consistent meaning**: Use same icon-color pairings across the interface

---

## Testing Checklist

### Screen Reader Testing

- [ ] Test with NVDA (Windows), JAWS (Windows), VoiceOver (macOS/iOS), TalkBack (Android)
- [ ] Verify badge status and meaning are announced, or properly hidden when context exists nearby

### Keyboard Testing

- [ ] Confirm badges are non-interactive and do not receive focus
- [ ] Verify focus moves past badges to interactive elements

### Visual Testing

- [ ] Verify badge meaning is clear when viewed in grayscale (not relying on color alone)

Resources: [Orange Accessibility Testing Guide](https://a11y-guidelines.orange.com/en/web/testing/)

---

## Key WCAG Criteria

- **1.4.1 Use of Color** (A): Status not conveyed by color alone—icons reinforce meaning
- **1.4.3 Contrast (Minimum)** (AA): Icon-to-background contrast ratio of 4.5:1 minimum
- **1.4.11 Non-text Contrast** (AA): Badge background has 3:1 contrast against surrounding area
- **4.1.2 Name, Role, Value** (A): Badges have accessible names when not described by context
- **4.1.3 Status Messages** (AA): Dynamic status changes announced via ARIA live regions when needed

For complete reference: [Orange Accessibility Guidelines - Components](https://a11y-guidelines.orange.com/en/web/components-examples/)

---

## Additional Resources

- [Orange Accessibility Guidelines - Colors and Contrasts](https://a11y-guidelines.orange.com/en/web/design/colors-and-contrasts/)
- [Carbon Design System - Status Indicator Pattern](https://carbondesignsystem.com/patterns/status-indicator-pattern/)
- [W3C WCAG 2.2 - Understanding Non-text Contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html)
- [Adobe Spectrum - Badge Accessibility](https://react-spectrum.adobe.com/react-spectrum/Badge.html)

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Oct 14, 2025 | 1.2.0 | <ul><li>The component now has two states: Enabled and Disabled. <li>Documentation has been updated and published in Zeroeight, with use case examples provided for every state. <li>The colors and background tokens for the functional states of the positive and info statuses have been changed. <li>The minimum required contrast ratio has been corrected from 3:1 to 4.5:1 between content (icon) and background for Enable state. <li>Functional badges (Positive, Warning, Negative, Info) differ from non-functional ones: they can only use functional icons, while non-functional badges are not supported. <li>For the "Status neutral" variant: <ul><li>The content token "color-content-on-status-neutral-emphasized" has been replaced by the token "color-content-inverse" <li>The surface token "color-surface-status-neutral-emphasized" has been replaced by the token "color-surface-inverse-high" </ul></ul> | Anton Astafev |
| Jun 16, 2025 | 1.1.0 | <ul><li>"Accent" variant added</ul> | Maxime Tonnerre |
| Mai 9, 2025 | 1.0.0 | <ul><li>Component creation</ul> | Anton Astafev |
