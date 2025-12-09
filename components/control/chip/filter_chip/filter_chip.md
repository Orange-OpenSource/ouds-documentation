# Guideline

## Intro 👈🤖

A filter chip is a compact, toggleable element that enables users to refine displayed content by selecting or deselecting filter criteria.

---

## Definition

A filter chip is a compact UI element used in a design system to represent a filter option that can be selected or deselected by the user. Filter chips allow users to refine content or data by applying one or more filters in a visually accessible and interactive way.

Purpose: Allows users to filter content by selecting or deselecting specific categories or attributes.
Behavior: Can be toggled on/off to refine displayed results. Selected chips remain visually distinct to indicate active filters.

---

## Best for 👈🤔

✅ Filtering product catalogs by category, brand, size, or color attributes

✅ Refining search results with multiple concurrent filter criteria

✅ Organizing content by tags or keywords in content management interfaces

✅ Selecting date ranges or time periods for data visualization dashboards

✅ Toggling quick filters in email or messaging applications

✅ Narrowing options in restaurant menus or food delivery apps

✅ Filtering map markers by location type or amenity in navigation apps

✅ Selecting multiple categories in news or media content feeds

✅ Applying status filters in task management or project tracking tools

✅ Refining job listings by location, salary range, or experience level

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Container | Provides the interactive boundary with rounded pill shape and border styling | N |
| 2 | Label text | Displays the filter category or option name | Y |
| 3 | Leading icon (tick) | Indicates selected state when filter is active | Y |
| 4 | Trailing icon | Provides additional visual context or category identification | Y |
| 5 | Border | Differentiates selected (thick, accent color) from unselected (thin, neutral) states | N |
| 6 | Focus ring | Triple-layered border indicating keyboard focus for accessibility | N |
| 7 | Interactive area | Minimum 48px height touch target for accessibility compliance | N |

---

## Selected

**`True`** Visually distinct to indicate an active filter.
Changes in color and includes a tick mark to signify selection.

**`False`** Maintains a neutral appearance, indicating an available filter option.

---

## selected_do_&_dont 👈🤔

✅ **Do:** Use a clear visual indicator like a checkmark or filled background to show selected state  
❌ **Don't:** Rely solely on subtle color changes that may not be perceivable by all users

✅ **Do:** Maintain consistent selected styling across all filter chips in a group  
❌ **Don't:** Mix different selection indicator styles within the same filter set

✅ **Do:** Ensure selected chips have sufficient color contrast (4.5:1 minimum) against the background  
❌ **Don't:** Use colors that only differ in hue without adequate luminance contrast

✅ **Do:** Provide immediate visual feedback when a chip transitions between selected and unselected states  
❌ **Don't:** Delay selection feedback or require additional confirmation for simple filter toggles

✅ **Do:** Consider pre-selecting sensible defaults when appropriate to reduce user effort  
❌ **Don't:** Pre-select all filters as this defeats the purpose of filtering content

---

## Layouts

**`Text + icon`** Combines text with an icon to enhance clarity and recognition.
Ideal when a visual cue helps reinforce the filter's meaning.

**`Text only`** Displays only text, offering a clean and minimalistic look.
Best suited for category-based filters that do not require additional visual elements.

**`Icon only`** Uses only an icon, making it a compact option for limited space.
Works well with universally recognized symbols, such as a heart for favorites or a checkmark for selection.

---

## layouts_do_&_dont 👈🤔

✅ **Do:** Use text-only layouts when filter labels are self-explanatory and space is available  
❌ **Don't:** Force icon-only layouts when the meaning isn't universally understood

✅ **Do:** Combine text with icons when visual reinforcement improves scannability  
❌ **Don't:** Add decorative icons that don't contribute to comprehension

✅ **Do:** Reserve icon-only layouts for universally recognized symbols like favorites or status indicators  
❌ **Don't:** Use ambiguous or custom icons without text labels in icon-only mode

✅ **Do:** Keep text labels concise—ideally one to two words maximum  
❌ **Don't:** Include verbs like "Select" or "Filter" within chip labels

✅ **Do:** Maintain consistent layout type within a single filter group  
❌ **Don't:** Mix text-only and icon-only chips arbitrarily within the same filter set

---

# Specs

## States

**`Enabled`** The chip is active and available for interaction.
It is displayed in its standard style without additional effects.

**`Hover`** The appearance of the chip changes when the cursor hovers over it.
This includes a color change for the border and the chip's content.

**`Pressed`** The active state when the chip is being pressed.
Accompanied by a color change in the content and border.

**`Disabled`** The chip is unavailable for interaction.
It is visually represented with a muted color change in the content and border (reduced brightness and contrast).

**`Focus`** The state when the chip receives focus (e.g., during keyboard navigation).
It features a triple contrasting border to indicate the active element.

**`Skeleton`** Displays a placeholder chip while the content is loading.
It appears as a semi-transparent gray block without content.

---

## Layout and spacing

🚧 Content to be added

---

# Accessibility 👈🤖

## Accessibility intro

Filter chips must meet WCAG 2.2 Level AA requirements for keyboard operability, focus visibility, and state communication to assistive technologies. For comprehensive accessibility guidance, see the [Orange Unified Design System Accessibility Overview](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability).

---

## Accessibility Challenges

Filter chips present unique accessibility challenges due to their dual nature as both toggleable controls and visual status indicators. Users must be able to perceive the selected/unselected state, operate the chip via keyboard, and receive clear feedback when the filter state changes.

### Key Challenges

- Communicating toggle state (selected/unselected) to screen readers
- Ensuring sufficient color contrast between selected and unselected states
- Providing visible focus indication with triple-border design complexity
- Managing focus order within horizontally scrollable chip groups

### Critical Success Factors

1. Use `aria-pressed` attribute to communicate toggle state (WCAG 4.1.2)
2. Maintain minimum 48px touch target for motor accessibility (WCAG 2.5.5)
3. Ensure focus indicator contrast ratio of 3:1 minimum (WCAG 2.4.7)
4. Provide keyboard activation via `Space` or `Enter` keys (WCAG 2.1.1)

---

## Design Requirements

### Structure & Labels

- [ ] **Semantic button element**: Use `<button>` with `aria-pressed` attribute ([Orange guidelines](https://a11y-guidelines.orange.com/en/web/develop/custom-components/))
- [ ] **Accessible name**: Provide visible label text or `aria-label` for icon-only variants
- [ ] **Group labeling**: Wrap chip groups with `role="group"` and `aria-label` describing the filter category

### Visual Design

- [ ] **Color contrast**: Maintain 4.5:1 contrast for text, 3:1 for graphical elements ([Color contrast](https://a11y-guidelines.orange.com/en/web/design/colors-and-contrasts/))
- [ ] **Focus visibility**: Display triple-border focus ring with 3:1 contrast against adjacent colors
- [ ] **Touch target**: Ensure minimum 48×48px interactive area for all chip variants

### Content

- [ ] **Label clarity**: ❌ "Filter: Category" / ✅ "Category" ([Writing guidelines](https://a11y-guidelines.orange.com/en/web/design/textual-content/))
- [ ] **State announcement**: Ensure selected state is conveyed through both visual and programmatic means

---

## Testing Checklist

### Screen Reader Testing

- [ ] Test with NVDA (Windows), JAWS (Windows), VoiceOver (macOS/iOS), TalkBack (Android)
- [ ] Verify chip announces: name, role (button), and pressed state (true/false)

### Keyboard Testing

- [ ] `Tab` navigates to chip group, `Arrow` keys navigate between chips, `Space`/`Enter` toggles selection
- [ ] Verify focus ring visible with sufficient contrast on all chip states

Resources: [Orange Accessibility Testing Guide](https://a11y-guidelines.orange.com/en/web/test/)

---

## Key WCAG Criteria

- **2.1.1 Keyboard** (A): All chip functionality operable via keyboard without timing requirements
- **2.4.7 Focus Visible** (AA): Triple-border focus indicator clearly visible with ≥3:1 contrast
- **4.1.2 Name, Role, Value** (A): Button role with `aria-pressed` communicates toggle state to assistive technology
- **1.4.3 Contrast (Minimum)** (AA): Text and icon content maintains 4.5:1 contrast ratio in all states
- **2.5.5 Target Size** (AAA): Interactive area meets 48px minimum for enhanced motor accessibility

For complete reference: [Orange Accessibility Guidelines - Interactive Components](https://a11y-guidelines.orange.com/en/web/components-examples/)

---

## Additional Resources

- [Orange Accessibility Guidelines - Custom Components](https://a11y-guidelines.orange.com/en/web/develop/custom-components/)
- [W3C WAI-ARIA Authoring Practices - Button Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/button/)
- [Material Design - Chip Accessibility](https://m3.material.io/components/chips/accessibility)
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