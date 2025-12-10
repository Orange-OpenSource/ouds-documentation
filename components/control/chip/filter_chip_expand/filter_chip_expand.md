# Guideline

## Intro 👈🤖

An expand filter chip combines selection filtering with a dropdown menu to apply filters from predefined options.

---

## Definition

An Expand filter chip is a compact UI component that combines the functionality of a filter chip with a dropdown menu. It allows users to apply a filter from a predefined list of options without leaving the current context. When activated, it reveals a dropdown containing selectable values, and the chip updates to reflect the selected filter. This component is useful for filters with multiple or dynamic options, offering both clarity and space efficiency in the interface.

---

## Best for 👈🤔

✅ Grouping multiple filter options under a single category label

✅ Space-constrained interfaces where inline filter lists would be too wide

✅ Dynamic filter values that change based on data or context

✅ Multi-select filtering where users can choose several options within one category

✅ Filter experiences requiring a counter badge to show active selection count

✅ Mobile and responsive layouts where dropdown menus optimize touch targets

✅ Contextual filtering that needs to remain visible while options are reviewed

✅ Faceted search interfaces with hierarchical or grouped filter options

✅ Data tables or lists requiring quick, non-disruptive filter application

✅ Product catalogs with attribute-based filtering like size, color, or price range

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Container | Pill-shaped wrapper providing interactive area and visual boundary | N |
| 2 | Label text | Displays the filter category name or selected value | N |
| 3 | Tick icon | Indicates selected state when filter is active | Y |
| 4 | Counter badge | Shows number of selected options within the filter category | Y |
| 5 | Chevron icon | Indicates expandable dropdown; points up when expanded, down when collapsed | N |
| 6 | Focus ring | Triple-border focus indicator for keyboard navigation accessibility | N |

---

## Selection Status

**`Selected`** Visually differentiated to show an active filter. The chip changes color and displays a tick and counter to indicate it has been selected.

**`Unselected`** Maintains a neutral appearance, indicating an available filter option.

---

## selection_status_do_&_dont 👈🤔

✅ **Do:** Use a prominent visual change like border color or weight to distinguish selected from unselected states  
❌ **Don't:** Rely solely on color to communicate selection status without additional indicators

✅ **Do:** Display a checkmark or tick icon alongside the label to reinforce the selected state  
❌ **Don't:** Use ambiguous icons that could be confused with other actions like delete or close

✅ **Do:** Include a counter badge when multiple options are selected within one filter category  
❌ **Don't:** Show counters for single-select filters where only one option can be active

✅ **Do:** Ensure selected chips are immediately distinguishable at a glance in filter groups  
❌ **Don't:** Make the visual difference so subtle that users miss which filters are currently applied

✅ **Do:** Allow users to quickly clear selections by interacting with the chip or a dedicated clear action  
❌ **Don't:** Force users to re-open the dropdown and manually deselect each option individually

---

## Expanded

The "Expanded" state allows the filter chip to be dynamically edited via a dropdown component.

**`True`** When a Filter chip is in the "Expanded" state, it:
 - Displays a contextual dropdown containing a menu or controls to modify the associated filter values.
 - Remains visually attached to the source chip (often below or overlapping).
 - Allows the user to select multiple options or apply a new value.
The component can remain in the "Expanded" state until a user action (click or key press) closes it. Chevron icon points up.

**`False`** The "Collapsed" state is the default or "resting" state of the filter chip, in which it simply displays a filter value, without any visible complex interaction. Chevron icon points down.

---

## expanded_do_&_dont 👈🤔

✅ **Do:** Position the dropdown directly below or adjacent to the chip maintaining visual connection  
❌ **Don't:** Display the dropdown far from the chip causing users to lose context of which filter they're editing

✅ **Do:** Use the chevron icon direction to clearly indicate expanded (up) versus collapsed (down) state  
❌ **Don't:** Use the same chevron direction for both states or omit the directional indicator entirely

✅ **Do:** Keep the dropdown open while users make multiple selections in multiselect scenarios  
❌ **Don't:** Close the dropdown after each selection forcing users to repeatedly reopen it

✅ **Do:** Allow closing the dropdown via clicking outside, pressing Escape, or clicking the chip again  
❌ **Don't:** Require a specific close button as the only way to dismiss the dropdown

✅ **Do:** Maintain focus management so keyboard users can navigate between chip and dropdown seamlessly  
❌ **Don't:** Trap focus in the dropdown or lose focus position when the dropdown closes

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

The Expand Filter Chip must meet WCAG 2.2 Level AA standards to ensure all users can effectively filter content regardless of ability. For comprehensive accessibility guidance, see the [Orange Unified Design System Accessibility Overview](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability).

---

## Accessibility Challenges

The Expand Filter Chip presents unique accessibility challenges because it combines interactive button behavior with a dropdown popup. The component must communicate its dual nature (filter indicator and expandable control), announce state changes clearly, and maintain proper focus management when the dropdown opens and closes.

### Key Challenges

- Communicating the expandable nature and current selection status to screen readers
- Managing focus between the chip and the dropdown popup without disorienting users
- Ensuring the chevron icon direction change is perceivable by all users
- Providing keyboard access to all dropdown options while maintaining logical tab order

### Critical Success Factors

1. Use `role="combobox"` with proper `aria-expanded` and `aria-haspopup="listbox"` attributes
2. Announce selection count and expanded state changes via live regions or ARIA attributes
3. Implement complete keyboard navigation following WAI-ARIA combobox pattern
4. Maintain visible focus indicators with ≥3:1 contrast ratio throughout all interactions

---

## Design Requirements

### Structure & Labels

- [ ] **Accessible name**: Provide descriptive label via visible text or `aria-label` ([Orange label guidelines](https://a11y-guidelines.orange.com/en/web/develop/textual-content/))
- [ ] **Role announcement**: Use `role="combobox"` with `aria-haspopup="listbox"` for proper semantics
- [ ] **State communication**: Set `aria-expanded` to "true" or "false" reflecting dropdown visibility

### Visual Design

- [ ] **Focus indicator**: Triple-border focus ring with ≥3:1 contrast against background ([Focus guidelines](https://a11y-guidelines.orange.com/en/web/design/colors-and-contrasts/))
- [ ] **State distinction**: Selected vs unselected states distinguishable without relying on color alone
- [ ] **Touch target**: Minimum 48×48px interactive area for mobile accessibility

### Content

- [ ] **Label clarity**: ❌ "Filter 1" / ✅ "Size" or "Price range" ([Content guidelines](https://a11y-guidelines.orange.com/en/web/develop/textual-content/))
- [ ] **Counter announcement**: Badge count included in accessible name (e.g., "Size, 3 selected")

---

## Testing Checklist

### Screen Reader Testing

- [ ] Test with NVDA (Windows), JAWS (Windows), VoiceOver (macOS/iOS), TalkBack (Android)
- [ ] Verify role, expanded state, selection count, and dropdown options are announced correctly

### Keyboard Testing

- [ ] Tab to chip, Enter/Space opens dropdown, Arrow keys navigate options, Escape closes
- [ ] Focus returns to chip after dropdown closes; focus ring visible throughout

### Interaction Testing

- [ ] Selection changes update chip label, counter badge, and are announced to assistive technology

Resources: [Orange Accessibility Testing Guide](https://a11y-guidelines.orange.com/en/web/test/)

---

## Key WCAG Criteria

- **1.4.11 Non-text Contrast** (AA): Focus indicators and state changes meet ≥3:1 contrast ratio
- **2.1.1 Keyboard** (A): All chip and dropdown functionality operable via keyboard alone
- **2.4.7 Focus Visible** (AA): Visible focus indicator displayed on chip and dropdown options
- **4.1.2 Name, Role, Value** (A): Combobox role with proper ARIA attributes communicates state
- **4.1.3 Status Messages** (AA): Selection changes announced without moving focus

For complete reference: [Orange Accessibility Guidelines - WCAG Criteria](https://a11y-guidelines.orange.com/en/web/wcag/)

---

## Additional Resources

- [Orange Accessibility Guidelines - Form Components](https://a11y-guidelines.orange.com/en/web/components-examples/)
- [WAI-ARIA Combobox Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/)
- [WCAG 2.2 Understanding Focus Visible](https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html)
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