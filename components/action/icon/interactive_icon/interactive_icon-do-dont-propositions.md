# Interactive icon — do & don't propositions

AI-generated propositions that no one has validated yet. They are not part of the documentation ([interactive_icon.md](interactive_icon.md)) and are not shown on zeroheight. Once a designer validates one, it moves into the full file.

## When to use

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

## Interactive icon vs Button (icon only) — do & don't

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
