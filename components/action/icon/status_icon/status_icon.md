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

# Accessibility

## Motion & Animation accessibility rules

In terms of animation, there are accessibility criteria to consider: “Animation from Interactions” and “Pause, Stop, Hide.”
These two main criteria address different issues:

**Pause, Stop, Hide - WCAG 2.2.2**
This concerns moving, blinking, scrolling, or automatically updating content.
The question to ask is: does the animation start automatically and meet the criterion’s conditions?
When a relevant animation lasts more than 5 seconds, users must be able to pause, stop, or hide it.
The two criteria should therefore be evaluated independently.

**Reduced Motion (Animation from Interactions) - WCAG 2.3.3**
This primarily concerns motion-based animations triggered by user interaction.
The question to ask is: is the movement essential to the functionality or to the information being conveyed?
If not, the animation should be removed, reduced, or replaced when the user has enabled Reduced Motion.

ℹ️ The reduced motion preference can be configured by the user at the operating system level and is available to websites through the CSS prefers-reduced-motion media feature.

Concrete application to the Status icon:

**Pause, Stop, Hide**
If the icon animation starts automatically and repeats for more than 5 seconds, it must be possible to pause, stop, or hide it, unless a WCAG exception applies.
Whenever possible, it is recommended to use a short, non-repeating animation rather than maintaining a looping animation.

**Reduced Motion**
Animation applied to a functional icon is generally not essential to understanding the information being conveyed.
When Reduced Motion is enabled, the animation should be removed or replaced with a static representation of the corresponding state.
If the animation conveys essential information, that information must remain available through a non-animated representation.

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Jun 8, 2026 | 1.0.0 | Version 2.6 of the design tokens is required for the development of this update.<ul><li>Component creation</ul> | Maxime Tonnerre |
