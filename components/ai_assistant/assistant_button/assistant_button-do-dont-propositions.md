# Assistant button — do & don't propositions

AI-generated propositions that no one has validated yet. They are not part of the documentation ([assistant_button.md](assistant_button.md)) and are not shown on zeroheight. Once a designer validates one, it moves into the full file.

## When to use

✅ Triggering a conversational AI assistant or chat experience from any screen

✅ Generating content such as text, summaries, or replies on demand

✅ Requesting AI-powered suggestions within a form or input field

✅ Launching contextual help powered by artificial intelligence

✅ Rephrasing, translating, or improving user-written text

✅ Summarizing a long document, thread, or article in a single tap

✅ Offering an "ask AI" entry point inside toolbars or content cards

✅ Compact icon-only AI triggers where horizontal space is limited

✅ Pairing an AI action with a related input (for example, an Assistant input)

✅ Initiating AI analysis of data, images, or a user selection

## Layouts — do & don't

✅ **Do:** Use the "Text + icon" layout when the AI action must be clearly discoverable and explicit.  
❌ **Don't:** Rely on "Icon only" for primary or unfamiliar AI actions where users need a textual cue.

✅ **Do:** Reserve "Icon only" for compact, space-constrained contexts where the action is already understood.  
❌ **Don't:** Place a standalone "Icon only" AI button without surrounding context that clarifies its purpose.

✅ **Do:** Always keep the AI (sparkle) icon present so the action stays recognisably AI-powered.  
❌ **Don't:** Swap the AI icon for an unrelated glyph that hides the intelligent nature of the action.

✅ **Do:** Provide an accessible name via `aria-label` for every "Icon only" AI button.  
❌ **Don't:** Ship an "Icon only" button with no text alternative for screen readers.

✅ **Do:** Keep labels short, action-led, and descriptive of the AI outcome ("Ask AI", "Summarize").  
❌ **Don't:** Use vague labels like "Go" or "Click here" that don't describe the AI action.

## Sizes — do & don't

✅ **Do:** Use the Default size for the vast majority of applications and standalone AI actions.  
❌ **Don't:** Default to the Small size for primary AI actions that should remain easy to notice and tap.

✅ **Do:** Use the Small size in information-dense interfaces or when paired with small elements (e.g., Assistant input).  
❌ **Don't:** Mix Default and Small sizes arbitrarily within the same group of related controls.

✅ **Do:** Preserve the minimum 48px interactive area even when the visual size is reduced.  
❌ **Don't:** Shrink the button below the minimum touch target, harming usability on touch devices.

✅ **Do:** Match the button size to the density and hierarchy of its surrounding layout.  
❌ **Don't:** Choose the Small size purely for aesthetic compactness at the expense of legibility.

✅ **Do:** Keep size choices consistent for buttons that share the same role across the product.  
❌ **Don't:** Vary sizes for identical AI actions on different screens, creating an inconsistent rhythm.

## Rounded corner — do & don't

✅ **Do:** Apply the rounded-corner setting consistently across the entire product or service.  
❌ **Don't:** Mix Rounded corner=True and Rounded corner=False buttons within the same product/service.

✅ **Do:** Use square corners (False) for standard, business-oriented, utility-driven journeys.  
❌ **Don't:** Switch to rounded corners ad-hoc without a clear brand or experience rationale.

✅ **Do:** Use rounded corners (True) for softer, more emotional, immersive, or tactile contexts.  
❌ **Don't:** Enable rounded corners on brand themes where the option is unavailable (Sosh, Wireframe).

✅ **Do:** Treat the rounded-corner choice as a transversal, product-level design decision.  
❌ **Don't:** Expose the per-button rounded-corner toggle as a routine, case-by-case styling option.

✅ **Do:** Align the button's corner style with other interactive elements in the same interface.  
❌ **Don't:** Pair rounded AI buttons with square standard buttons, creating visual inconsistency.
