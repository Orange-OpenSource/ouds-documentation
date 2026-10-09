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
