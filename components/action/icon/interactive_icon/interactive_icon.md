# Guideline

## Intro 👈🤖

An interactive icon triggers an action using only an icon — no container — keeping a light visual footprint that integrates naturally with surrounding content.

---

## Definition

An Interactive Icon is an icon component designed to trigger a user interaction (e.g., open, close, toggle a state). It includes defined interactive states and can be used independently or within other components such as buttons, inputs, or menus.

---

## Best for 👈🤔

✅ Inline actions placed directly next to text or form fields

✅ Compact toolbars where an icon-only action saves space

✅ Toggling a state (open/close, show/hide, expand/collapse)

✅ Lightweight actions inside content cards, rows, or list items

✅ Embedding an action within another component (input, menu, chip)

✅ Dense interfaces where a button's touch target would feel heavy

✅ Repeated actions in tables or lists where buttons would add noise

✅ Custom-sized affordances that must scale with the surrounding layout

✅ Secondary actions that shouldn't compete with primary buttons

✅ Icon-driven actions where the meaning is already clear from context

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Icon | The glyph communicating the action | N |
| 2 | Interactive area | Invisible hit target around the icon (min 28px) for pointer/touch | N |
| 3 | Color treatment | State feedback expressed through icon color transitions (no background) | N |
| 4 | Focus ring | Visible outline indicating keyboard focus for accessibility | N |
| 5 | Loading indicator | Spinner shown in place of the icon during the Loading state | Y |
| 6 | Skeleton placeholder | Neutral shape shown before the icon has fully loaded | Y |

---

## Interactive icon vs Button (icon only)

**Although both components provide an icon-based interaction, they serve different purposes and should be selected according to the desired visual emphasis and layout constraints.**

An Button (icon only) includes a dedicated interactive container that can display a visible background, either in its default state or during state transitions such as hover, pressed, or selected. This additional visual layer reinforces the affordance of the component and makes it suitable for primary or clearly identifiable actions.

An Interactive icon, on the other hand, relies solely on the icon itself to communicate interactivity. It does not include any additional background or container. State changes are expressed exclusively through color transitions, resulting in a lighter visual footprint that integrates more naturally within surrounding content.

The two components also differ in their sizing approach. The Button (icon only) is designed around predefined dimensions (48px for the default size and 40px for the small size) to ensure consistent touch targets and alignment across interfaces. In contrast, the Interactive icon is not constrained to specific dimensions and can be used at any size required by the layout.

This flexibility allows an Interactive icon to be positioned closer to text or adjacent elements when a more compact and visually harmonious composition is needed, while still preserving its interactive behavior.

---

## interactive_icon_vs_button_icon_only_do_&_dont 👈🤔

✅ **Do:** Use the interactive icon for lightweight, inline actions meant to blend into surrounding content.  
❌ **Don't:** Use it for primary actions that need a clear tappable container — choose Button (icon only) instead.

✅ **Do:** Choose Button (icon only) when you need a consistent touch target (48px default / 40px small).  
❌ **Don't:** Stretch the interactive icon into a primary call-to-action with an implied button affordance.

✅ **Do:** Rely on color transitions alone for the interactive icon's state feedback.  
❌ **Don't:** Add a background or container to an interactive icon — that is what the button variant is for.

✅ **Do:** Size the interactive icon freely so it sits harmoniously next to text or adjacent elements.  
❌ **Don't:** Place it where a button-sized hit area is expected without preserving the 28px minimum interactive area.

✅ **Do:** Provide an accessible name via `aria-label` since there is no visible text label.  
❌ **Don't:** Ship an icon-only action with no text alternative for screen readers.

---

## Multiline and responsiveness

**User zoom in/out**
The component's height and width must be flexible, never fixed, in order to automatically adapt its dimensions according to the level of zoom (the icons follow the same rules as the text).
In order to preserve the minimun interactive area during user zoom out, this component have a min-width and a min-height **of 28px**.

---

# Specs

## States

**`Enabled`** The status of the icon before a user has interacted with it, or other content affects it.

**`Hover`** When a user places a pointing device over an icon, but has not yet taken action on it.

**`Focus`** When a user selects an icon via keyboard or voice command, but has not yet taken action on it.
Mirrors the "Hover" state but includes an additional border.

**`Pressed`** An intermediate state that communicates a user has taken action on an icon, and that it is in the process of navigating to a destination, triggering logic, or transmitting data.

**`Loading`** An icon is fetching data from another internal or external resource.
Uses the "Loading indicator" component.

**`Disabled`** Used to indicate an icon that cannot be selected.

**`Skeleton`** Improves the perceived loading time by providing a visual cue of where icon will appear once fully loaded.
Uses the "Skeleton" component, variant "Security marge=False".

---

## Layout and spacing

🚧 Content to be added

---

# Accessibility 👈🤖

## Accessibility intro

The interactive icon must meet WCAG 2.2 Level AA. With no visible label and no container, it must expose an accessible name, convey state without relying on color alone, and keep an operable target. For comprehensive guidance, see the [Orange Unified Design System Accessibility Overview](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability).

---

## Accessibility Challenges

Because the interactive icon has no visible label and no button container, the glyph is the only cue, state is conveyed by color, and the small, container-less hit area must still be reachable and operable for everyone.

### Key Challenges

- Providing an accessible name when there is no visible text label
- Conveying interactive state without a background — color transitions only
- Keeping an adequate interactive target despite the container-less, custom size
- Announcing the Loading state so users know the action is processing

### Critical Success Factors

1. Use a native `<button>` element wrapping the icon for keyboard and screen-reader support
2. Give every interactive icon a descriptive accessible name via `aria-label`
3. Preserve a minimum 28px interactive area (larger where touch is the primary input)
4. Provide a visible focus indicator with ≥3:1 contrast against adjacent colors

---

## Design Requirements

### Structure & Labels

- [ ] **Semantic markup**: Wrap the icon in a native `<button>` for automatic keyboard and screen-reader support
- [ ] **Accessible name**: Always provide a descriptive `aria-label` ([Label guidance](https://a11y-guidelines.orange.com/en/web/develop/textual-content/#make-sure-the-user-can-use-native-browser-options))
- [ ] **State communication**: Expose the Loading state with `aria-busy="true"` and announce completion

### Visual Design

- [ ] **Focus visibility**: Display a focus ring with ≥3:1 contrast against adjacent colors ([Focus guidance](https://a11y-guidelines.orange.com/en/web/design/navigation-focus/))
- [ ] **Color independence**: State is shown by color only — pair it with focus and the icon so meaning isn't color-dependent
- [ ] **Interactive area**: Maintain at least a 28px interactive target; enlarge it for touch-first contexts

### Content

- [ ] **Descriptive name**: ❌ "icon" / ✅ "Close dialog" ([Content guidance](https://a11y-guidelines.orange.com/en/web/design/textual-content/))
- [ ] **No duplication**: If a visible label already exists nearby, don't repeat it redundantly in the accessible name

---

## Testing Checklist

### Screen Reader Testing

- [ ] Test with NVDA (Windows), JAWS (Windows), VoiceOver (macOS/iOS), TalkBack (Android)
- [ ] Verify button role announced, accessible name read, and Loading state communicated

### Keyboard Testing

- [ ] Tab to the icon (focus visible), activate with Enter/Space, confirm the action triggers
- [ ] Verify focus remains managed during and after the Loading state

### Loading State Testing

- [ ] Confirm the Loading state is announced and the icon is not prematurely re-triggerable

Resources: [Orange Accessibility Testing Guide](https://a11y-guidelines.orange.com/en/web/testing/)

---

## Key WCAG Criteria

- **2.1.1 Keyboard** (A): All interactive-icon functionality operable via keyboard without timing
- **2.4.7 Focus Visible** (AA): Visible focus indicator present on the icon when focused
- **4.1.2 Name, Role, Value** (A): Button role, accessible name, and state programmatically exposed
- **1.4.11 Non-text Contrast** (AA): Icon, focus indicator, and interactive states meet ≥3:1 contrast
- **2.5.8 Target Size (Minimum)** (AA): Interactive target meets the minimum size, with spacing where smaller

For complete reference: [Orange Accessibility Guidelines - Components](https://a11y-guidelines.orange.com/en/web/components-examples/)

---

## Additional Resources

- [Orange Accessibility Guidelines - Interactive Components](https://a11y-guidelines.orange.com/en/web/components-examples/)
- [W3C WAI - Button Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/button/)
- [WCAG 2.2 Understanding Target Size (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)
- [Orange Design System - Accessibility & Sustainability](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability)

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Jun 8, 2026 | 1.0.0 | Version 2.6 of the design tokens is required for the development of this update.<ul><li>Component creation</ul> | Maxime Tonnerre |
