## Future update! The version 1.7.0 is currently being designed; it will be released in an upcoming release.



---

## Definition

A switch is a UI element that toggles between two states, typically "On" and "Off," and is used to enable or disable features, options, or settings. The switch, that lacks an additional icon asset or text label, provides greater flexibility when creating other components that require a switch.

---

## State

**`Enabled`** The status of the switch before a user has interacted with it, or other content affects it.

**`Hover`** When a user places a pointing device over a switch, but has not yet taken action on it.

**`Focus`** When a user selects a switch via keyboard or voice command, but has not yet taken action on it.
Mirrors the "Hover" state but includes an additional border.

**`Pressed`** A temporary interaction state displayed while the user presses the Switch to change its current On/Off state.

**`Read only`** The switch is displayed in a specific state (true or false), but the user cannot modify it.

**`Disabled`** Used to indicate an option that cannot be selected.

**`Skeleton`** Improves the perceived loading time by providing a visual cue of where switch will appear once fully loaded.
Uses the "Skeleton" component, variant “Security marge=True”.

---

## Selected

Typically, a switch has two main states: Selected and Unselected.

**`False`** The switch is off, the option or feature is disabled.
Used as the default state before activation.

**`True`** The switch is on, the option or feature is enabled.
Indicates that the setting or action is currently active.

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

Concrete application to the Switch:

**Pause, Stop, Hide**
The animation of a switch is triggered by a user action and therefore does not generally fall within the scope of this criterion.
If the state change triggers additional animation or automatically moving content that meets the conditions of the criterion, that content must be evaluated separately.

**Reduced Motion**
The animation applied when a switch changes state is generally not essential to its functionality or to understanding its state.
When Reduced Motion is enabled, the animation should therefore be removed or replaced with an instantaneous transition.
The state of the switch must remain clearly identifiable without relying on animation.
Default: animated state change
Reduced Motion: instantaneous state change
