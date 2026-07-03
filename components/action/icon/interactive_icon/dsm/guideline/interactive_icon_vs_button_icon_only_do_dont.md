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