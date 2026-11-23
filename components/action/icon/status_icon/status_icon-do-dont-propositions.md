# Status icon — do & don't propositions

AI-generated propositions that no one has validated yet. They are not part of the documentation ([status_icon.md](status_icon.md)) and are not shown on zeroheight. Once a designer validates one, it moves into the full file.

## When to use

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

## Status — do & don't

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

## Animated — do & don't

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
