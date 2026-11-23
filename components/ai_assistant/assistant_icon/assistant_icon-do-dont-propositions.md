# Assistant icon — do & don't propositions

AI-generated propositions that no one has validated yet. They are not part of the documentation ([assistant_icon.md](assistant_icon.md)) and are not shown on zeroheight. Once a designer validates one, it moves into the full file.

## When to use

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

## ⚠️ Interactive icon vs button (icon only) — do & don't

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
