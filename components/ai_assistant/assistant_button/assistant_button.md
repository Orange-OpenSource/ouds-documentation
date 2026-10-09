# Guideline

## Intro 👈🤖

An AI assistant button triggers an interaction with an AI-powered feature, marked by a distinctive icon that clearly signals its intelligent capability.

---

## Definition

An AI assistant button is an action component used to trigger an interaction with an AI-powered feature, such as conversational assistance, content generation, or contextual suggestions.
It combines standard button behaviors with AI-specific visual attributes to clearly identify actions enhanced or powered by artificial intelligence.

---

## Best for 👈🤔

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

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Container | Houses all button elements and defines the interactive hit area | N |
| 2 | AI icon | "Sparkle" glyph that signals the action is powered by artificial intelligence | N |
| 3 | Label | Action-led text describing the AI assistant action | Y |
| 4 | Background | Visual surface providing hierarchy and state feedback | N |
| 5 | Border | Defines button boundaries; varies with state and rounded corner | Y |
| 6 | Focus ring | Visible outline indicating keyboard focus for accessibility | N |
| 7 | Loading indicator | Spinner shown in place of content during the Loading state | Y |

---

## Layouts

**`Text + icon`** Displays an "sparkle" icon alongside a label to clearly communicate the AI assistant action. Recommended when clarity, discoverability, and explicit communication are priorities.

**`Icon only`** Displays only the AI assistant icon for a more compact and minimal interface. Recommended when the context already makes the action understandable or when space is limited. It is rarely standalone (usually part of a group of elements).

---

## layouts_do_&_dont 👈🤔

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

---

## Sizes

**`Default`** This is the default size of the component.
This size is used for the vast majority of applications.

**`Small`** This size can be particularly useful in an information-dense interface or in the construction of a template or component requiring the use of small elements (in an "Assistant input" component, for example).

---

## sizes_do_&_dont 👈🤔

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

---

## Rounded corner

Even though in Figma this rendering option is available and editable from the properties of each button component, the configuration of this rendering option is actually transversal across the entire product/service in which the component is used. It is therefore impossible to have one button component set to Rounded corner=True and another set to Rounded corner=False within the same product/service.

**`False`**
The square rendering corresponds to Orange's historical style. It conveys the brand's sense of seriousness, robustness and utility-driven. It remains the default style for our digital interface components.

**`True`**
The rounded rendering offers flexibility without sacrificing the attribution to the brand. It helps anchoring the service in a reality where the visual codes of the mobile area tends to rub off on all interfaces. Use rounded corners for a softer, more approachable, friendly and tactile feel.

**Brand theme availability**
This option is technically not available for all brand themes. Here's the list of rounded corners availability by brand theme:

| Brand theme | Availability |
|---|---|
| Orange | ✅ Available |
| Orange Compact | ✅ Available |
| Sosh | ❌ Unavailable |
| Wireframe | ❌ Unavailable |

---

## rounded_corner_do_&_dont 👈🤔

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

---

## Multiline and responsiveness

**Multiline**
This component allows multi-line text editing. Although the number of lines is not technically limited, it is recommended not to exceed one line of text.
In its "Text + icon" variant, if the label spans multiple lines, the label remains horizontally centred and the icon remains vertically centred.

**Max-width vs full-width**
For greater flexibility, this component doesn't have a default max-width. To avoid exceeding a width that would degrade readability and the perception of a compact interactive element, we recommend applying **a max-width of around 360px.**
The component can also naturally wrap within the parent container (or the screen in a mobile use context for exemple) and use the full available width.
Please note that this behavior is not the default rule; it may be preferred if the template allows it (to improve user comfort or for better page structure/hierarchy).

**User zoom in/out**
The behavior of the text during user zoom in/out must follow a fundamental principle: the text must remain readable, accessible, and must never break the structure or lose information.
* The text must always scale proportionally with user zoom. Text resizing must never be blocked.
* Zooming must never cause text to be truncated or hidden. The component must expand vertically to allow line wrapping.
* The component's height and width must be flexible, never fixed, in order to automatically adapt its dimensions according to the level of zoom.
* In order to preserve the minimun interactive area during user zoom out, this component have a min-width and a min-height **of 48px**.
* Even if, the component has a max-height or a max-width for resizing control purposes, technically, during user zoom in, these limitations are not fixed but must be scalable in order to adapt to the user's zoom level.
* In its "Text + icon" variant, user zoom in/out doesn't affect the size of the icons; they remain fixed in size (decorative use).
* As the text is missing, in its "Icon only" variant, the icons follow the same rules as the text.

---

# Specs

## States

**`Enabled`** The status of the button before a user has interacted with it, or other content affects it.

**`Hover`** When a user places a pointing device over a button, but has not yet taken action on it.

**`Focus`** When a user selects a button via keyboard or voice command, but has not yet taken action on it.
Mirrors the "Hover" state but includes an additional border.

**`Pressed`** An intermediate state that communicates a user has taken action on a button, and that it is in the process of navigating to a destination, triggering logic, or transmitting data.

**`Loading`** A button is fetching data from another internal or external resource.
Uses the "Loading indicator" component.

**`Disabled`** Used to indicate a button that cannot be selected.

**`Skeleton`** Improves the perceived loading time by providing a visual cue of where button will appear once fully loaded.
Uses the "Skeleton" component, variant "Security marge=False".

---

## Layout and spacing

🚧 Content to be added

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Jun 8, 2026 | 1.0.0 | Version 2.6 of the design tokens is required for the development of this update.<ul><li>Component creation</ul> | Maxime Tonnerre |
