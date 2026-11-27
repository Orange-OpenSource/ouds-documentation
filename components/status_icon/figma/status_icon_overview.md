## Definition

A Status Icon is a visual component used to communicate the functional state of a system or message, such as Success, Info, Warning, or Error. It provides quick, at-a-glance feedback using standardized colors and symbols to ensure consistent meaning across the product. A Status Icon is typically non-interactive and is used in contexts such as alerts, form validation, notifications, or system messages.

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

## Animated

**`True`** The Status Icon includes a subtle animation to reinforce the status change or draw attention to the state. The animation remains minimal and purposeful, supporting clarity without distraction.

**`False`** The Status Icon is displayed in a static state, without motion. It provides immediate visual feedback using color and symbol only.

---

## Multiline and responsiveness

**User zoom in/out**
The component's height and width must be flexible, never fixed, in order to automatically adapt its dimensions according to the level of zoom (the icons follow the same rules as the text).
In order to preserve the minimun interactive area during user zoom out, this component have a min-width and a min-height **of 28px**.

---

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
