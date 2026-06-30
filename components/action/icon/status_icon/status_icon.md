# Guideline

## Intro 👈🤖

A status icon communicates a system or message state — success, info, warning, or error — using standardized colors and symbols for consistent, at-a-glance meaning.

---

## Definition

A Status Icon is a visual component used to communicate the functional state of a system or message, such as Success, Info, Warning, or Error. It provides quick, at-a-glance feedback using standardized colors and symbols to ensure consistent meaning across the product. A Status Icon is typically non-interactive and is used in contexts such as alerts, form validation, notifications, or system messages.

---

## Best for 👈🤔

✅ Status and feedback inside alerts and inline messages

✅ Form-field validation (success, error, warning)

✅ Notifications and toasts conveying a result

✅ System and connection status indicators

✅ Confirming a completed action with a positive icon

✅ Flagging blocking errors that need user attention

✅ Surfacing non-blocking cautions with a warning icon

✅ Neutral informational updates with an info icon

✅ Reinforcing a status change with the optional animation

✅ Anywhere a standardized, at-a-glance status cue is needed

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Status symbol | Standardized icon expressing the status meaning (never customized) | N |
| 2 | Status color | Semantic color token per status (positive/info/warning/negative) | N |
| 3 | Symbol + color pairing | Pairs a distinct symbol with color so meaning isn't color-only | N |
| 4 | Interactive area | Flexible size with a minimum 28px footprint | N |
| 5 | Animation | Optional subtle motion reinforcing the status change | Y |

---

## Status

⚠️ Note:
Icons must never be replaced or customized. Each type has a dedicated, standardized icon that expresses its meaning clearly.

**`Positive`** Confirms that an action was completed successfully.
Uses a green color and the standard success icon.

**`Info`** Provides neutral information or updates about the system or account status. Uses blue for neutrality and clarity.

**`Warning`** Draws attention to potential issues or upcoming changes.
Uses yellow to signal caution while remaining non-blocking.

**`Negative`** Indicates a failure, error, or blocking issue that needs user attention.
Uses red color and must include the standardized error icon.

---

## status_do_&_dont 👈🤔

✅ **Do:** Use the standardized icon and semantic color for each status.  
❌ **Don't:** Replace or customize the icon — the standardized symbol carries the meaning.

✅ **Do:** Pair color with its distinct symbol so meaning isn't conveyed by color alone.  
❌ **Don't:** Rely on color only — color-blind users may miss the status.

✅ **Do:** Reserve Negative for genuine failures or blocking errors that need attention.  
❌ **Don't:** Overuse Negative for non-blocking cautions — use Warning instead.

✅ **Do:** Use Info for neutral updates and Positive only for confirmed success.  
❌ **Don't:** Mix status meanings (e.g. a green icon for a warning).

✅ **Do:** Keep status meaning consistent everywhere the same state appears.  
❌ **Don't:** Use different icons or colors for the same status across the product.

---

## Animated

**`True`** The Status Icon includes a subtle animation to reinforce the status change or draw attention to the state. The animation remains minimal and purposeful, supporting clarity without distraction.

**`False`** The Status Icon is displayed in a static state, without motion. It provides immediate visual feedback using color and symbol only.

---

## animated_do_&_dont 👈🤔

✅ **Do:** Use animation sparingly to reinforce a meaningful status change.  
❌ **Don't:** Animate every status icon — constant motion becomes distracting.

✅ **Do:** Keep the animation subtle, minimal, and purposeful.  
❌ **Don't:** Use long or looping motion that competes with surrounding content.

✅ **Do:** Use the static (False) icon when motion adds no clarity.  
❌ **Don't:** Rely on animation alone to convey the status — color and symbol must still carry it.

✅ **Do:** Respect users' reduced-motion preferences and fall back to the static state.  
❌ **Don't:** Force animation when `prefers-reduced-motion` is set.

✅ **Do:** Ensure the icon's meaning is fully readable at the animation's start and end.  
❌ **Don't:** Hide essential meaning inside a transient animation frame.

---

## Multiline and responsiveness

**User zoom in/out**
The component's height and width must be flexible, never fixed, in order to automatically adapt its dimensions according to the level of zoom (the icons follow the same rules as the text).
In order to preserve the minimun interactive area during user zoom out, this component have a min-width and a min-height **of 28px**.

---

# Specs

## States

🚧 Not applicable — the status icon is typically non-interactive and has no interactive states. Its variants are expressed through the Status and Animated properties.

---

## Layout and spacing

🚧 Content to be added

---

# Accessibility 👈🤖

## Accessibility intro

Status icons must meet WCAG 2.2 Level AA. Because they convey meaning, the status must be available to assistive technology and never communicated by color alone. For comprehensive guidance, see the [Orange Unified Design System Accessibility Overview](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability).

---

## Accessibility Challenges

A status icon carries meaning visually, so that meaning must also reach screen-reader users and not depend on color perception. Decorative duplicates must be hidden, and any animation must respect reduced-motion preferences.

### Key Challenges

- Conveying status meaning to assistive tech, not by color or shape alone
- Avoiding duplicate announcements when adjacent text already states the status
- Meeting non-text contrast for the icon against its background
- Respecting `prefers-reduced-motion` for the animated variant

### Critical Success Factors

1. Provide a text alternative for the status (or expose it via the surrounding message)
2. Hide the icon from assistive tech (`aria-hidden`) when adjacent text already conveys the status
3. Don't rely on color alone — pair it with the standardized symbol
4. Honor reduced-motion settings; the static state must convey the same meaning

---

## Design Requirements

### Structure & Labels

- [ ] **Text alternative**: Give the icon an accessible name, or ensure nearby text states the status ([Images guidance](https://a11y-guidelines.orange.com/en/web/develop/images/))
- [ ] **No double-speak**: Mark the icon `aria-hidden` when the status is already in adjacent text
- [ ] **Live updates**: For dynamic status, announce changes via an appropriate live region

### Visual Design

- [ ] **Not color-only**: Pair semantic color with the standardized symbol ([Color guidance](https://a11y-guidelines.orange.com/en/web/design/color-and-contrast/))
- [ ] **Non-text contrast**: Meet ≥3:1 for the icon against its background
- [ ] **Reduced motion**: Provide a static fallback for the animated variant

### Content

- [ ] **Consistent meaning**: ❌ Green for a warning / ✅ Standard color+symbol per status ([Content guidance](https://a11y-guidelines.orange.com/en/web/design/textual-content/))
- [ ] **No customization**: Never substitute a non-standard icon for a status

---

## Testing Checklist

### Screen Reader Testing

- [ ] Verify the status is announced (via the icon's name or adjacent text), without duplication
- [ ] Confirm decorative status icons are hidden when text already conveys the status

### Color & Contrast Testing

- [ ] Check the icon's non-text contrast (≥3:1) and confirm meaning survives without color

### Motion Testing

- [ ] With `prefers-reduced-motion`, confirm the animated variant falls back to static

Resources: [Orange Accessibility Testing Guide](https://a11y-guidelines.orange.com/en/web/testing/)

---

## Key WCAG Criteria

- **1.4.1 Use of Color** (A): Status not conveyed by color alone; symbol reinforces meaning
- **1.1.1 Non-text Content** (A): Status icon has a text alternative or is correctly hidden
- **1.4.11 Non-text Contrast** (AA): Icon meets ≥3:1 contrast against its background
- **2.3.3 Animation from Interactions** (AAA): Respect reduced-motion for the animated variant
- **4.1.3 Status Messages** (AA): Dynamic status changes are announced without moving focus

For complete reference: [Orange Accessibility Guidelines - Components](https://a11y-guidelines.orange.com/en/web/components-examples/)

---

## Additional Resources

- [Orange Accessibility Guidelines - Images](https://a11y-guidelines.orange.com/en/web/develop/images/)
- [W3C WAI - Use of Color](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html)
- [WCAG 2.2 Understanding Status Messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html)
- [Orange Design System - Accessibility & Sustainability](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability)

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Jun 8, 2026 | 1.0.0 | Version 2.6 of the design tokens is required for the development of this update.<ul><li>Component creation</ul> | Maxime Tonnerre |
