# Guideline

## Intro 👈🤖

An AI assistant icon triggers an AI-powered action using only an icon — no container — keeping a light visual footprint within surrounding content.

---

## Definition

An AI assistant icon is an icon action component used to trigger an interaction with an AI-powered feature, such as conversational assistance, content generation, or contextual suggestions.
It combines standard interactive icon behaviors with AI-specific visual attributes to clearly identify actions enhanced or powered by artificial intelligence.

---

## Best for 👈🤔

✅ Inline AI triggers placed directly next to text or form fields

✅ Compact toolbars where an icon-only AI action saves space

✅ Lightweight "ask AI" affordances inside content cards or rows

✅ Triggering AI suggestions without adding a visible button container

✅ Dense interfaces where a button's touch target would feel heavy

✅ Adjacent-to-content actions needing a harmonious visual footprint

✅ Repeated AI actions in lists or tables where buttons would add noise

✅ Custom-sized AI affordances that must scale with the surrounding layout

✅ Secondary AI entry points that shouldn't compete with primary buttons

✅ Icon-driven AI actions where the meaning is already clear from context

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | AI icon | "Sparkle" glyph signalling an AI-powered action | N |
| 2 | Interactive area | Invisible hit target around the icon (min 28px) for pointer/touch | N |
| 3 | Color treatment | State feedback expressed through icon color transitions (no background) | N |
| 4 | Focus ring | Visible outline indicating keyboard focus for accessibility | N |
| 5 | Loading indicator | Spinner shown in place of the icon during the Loading state | Y |
| 6 | Skeleton placeholder | Neutral shape shown before the icon has fully loaded | Y |

---

## Interactive icon vs button (icon only)

**Although both components provide an icon-based interaction, they serve different purposes and should be selected according to the desired visual emphasis and layout constraints.**

An Assistant button (icon only) includes a dedicated interactive container that can display a visible background, either in its default state or during state transitions such as hover, pressed, or selected. This additional visual layer reinforces the affordance of the component and makes it suitable for primary or clearly identifiable actions.

An Assistant icon, on the other hand, relies solely on the icon itself to communicate interactivity. It does not include any additional background or container. State changes are expressed exclusively through color transitions, resulting in a lighter visual footprint that integrates more naturally within surrounding content.

The two components also differ in their sizing approach. The Assistant button (icon only) is designed around predefined dimensions (48px for the default size and 40px for the small size) to ensure consistent touch targets and alignment across interfaces. In contrast, the Assistant icon is not constrained to specific dimensions and can be used at any size required by the layout.

This flexibility allows an Assistant icon to be positioned closer to text or adjacent elements when a more compact and visually harmonious composition is needed, while still preserving its interactive behavior.

---

## interactive_icon_vs_button_icon_only_do_&_dont 👈🤔

✅ **Do:** Use the Assistant icon for lightweight, inline actions meant to blend into surrounding content.  
❌ **Don't:** Use it for primary actions that need a clear tappable container — choose Assistant button (icon only) instead.

✅ **Do:** Choose the Assistant button (icon only) when you need a consistent touch target (48px default / 40px small).  
❌ **Don't:** Stretch the Assistant icon into a primary call-to-action with an implied button affordance.

✅ **Do:** Rely on color transitions alone for the Assistant icon's state feedback.  
❌ **Don't:** Add a background or container to an Assistant icon — that is what the button variant is for.

✅ **Do:** Size the Assistant icon freely so it sits harmoniously next to text or adjacent elements.  
❌ **Don't:** Place it where a button-sized hit area is expected without preserving the 28px minimum interactive area.

✅ **Do:** Provide an accessible name via `aria-label` since there is no visible text label.  
❌ **Don't:** Ship an icon-only AI trigger with no text alternative for screen readers.

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

The AI assistant icon must meet WCAG 2.2 Level AA standards, ensuring everyone can trigger AI-powered actions regardless of ability. For comprehensive accessibility guidance, see the [Orange Unified Design System Accessibility Overview](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability).

---

## Accessibility Challenges

The AI assistant icon is especially challenging because it has no visible label and no button container: the sparkle icon is the only cue, state is conveyed by color alone, and the small, container-less hit area must still be reachable and operable for everyone.

### Key Challenges

- Providing an accessible name when there is no visible text label
- Conveying interactive state without a background — color transitions only
- Keeping an adequate interactive target despite the container-less, custom size
- Announcing the Loading state so users know the AI is processing their request

### Critical Success Factors

1. Use a native `<button>` element wrapping the icon for keyboard and screen-reader support
2. Give every Assistant icon a descriptive accessible name via `aria-label`
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

- [ ] **Descriptive name**: ❌ "icon" / ✅ "Ask the AI assistant" ([Content guidance](https://a11y-guidelines.orange.com/en/web/design/textual-content/))
- [ ] **Decorative duplication**: If a visible label already exists nearby, don't repeat it redundantly in the accessible name

---

## Testing Checklist

### Screen Reader Testing

- [ ] Test with NVDA (Windows), JAWS (Windows), VoiceOver (macOS/iOS), TalkBack (Android)
- [ ] Verify button role announced, accessible name read, and Loading state communicated

### Keyboard Testing

- [ ] Tab to the icon (focus visible), activate with Enter/Space, confirm the AI action triggers
- [ ] Verify focus remains managed during and after the Loading state

### Loading State Testing

- [ ] Confirm the Loading state is announced and the icon is not prematurely re-triggerable

Resources: [Orange Accessibility Testing Guide](https://a11y-guidelines.orange.com/en/web/testing/)

---

## Key WCAG Criteria

- **2.1.1 Keyboard** (A): All AI assistant icon functionality operable via keyboard without timing
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
