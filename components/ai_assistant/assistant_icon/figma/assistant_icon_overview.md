## Definition

An AI assistant icon is an icon action component used to trigger an interaction with an AI-powered feature, such as conversational assistance, content generation, or contextual suggestions.
It combines standard interactive icon behaviors with AI-specific visual attributes to clearly identify actions enhanced or powered by artificial intelligence.

---

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

## Interactive icon vs button (icon only)

**Although both components provide an icon-based interaction, they serve different purposes and should be selected according to the desired visual emphasis and layout constraints.**

An Assistant button (icon only) includes a dedicated interactive container that can display a visible background, either in its default state or during state transitions such as hover, pressed, or selected. This additional visual layer reinforces the affordance of the component and makes it suitable for primary or clearly identifiable actions.

An Assistant icon, on the other hand, relies solely on the icon itself to communicate interactivity. It does not include any additional background or container. State changes are expressed exclusively through color transitions, resulting in a lighter visual footprint that integrates more naturally within surrounding content.

The two components also differ in their sizing approach. The Assistant button (icon only) is designed around predefined dimensions (48px for the default size and 40px for the small size) to ensure consistent touch targets and alignment across interfaces. In contrast, the Assistant icon is not constrained to specific dimensions and can be used at any size required by the layout.

This flexibility allows an Assistant icon to be positioned closer to text or adjacent elements when a more compact and visually harmonious composition is needed, while still preserving its interactive behavior.

---

## Multiline and responsiveness

**User zoom in/out**
The component's height and width must be flexible, never fixed, in order to automatically adapt its dimensions according to the level of zoom (the icons follow the same rules as the text).
In order to preserve the minimun interactive area during user zoom out, this component have a min-width and a min-height **of 28px**.
