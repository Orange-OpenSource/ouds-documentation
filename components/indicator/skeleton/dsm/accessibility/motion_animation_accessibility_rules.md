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

Concrete application to the Skeleton:

**Pause, Stop, Hide**
When a skeleton uses an automatic shimmer animation, it is recommended to keep the animation short and avoid looping it indefinitely when this is not necessary.
If the automatic animation meets the criterion's conditions, users must be able to pause, stop, or hide it.
A recommended alternative is to play a single short animation, then keep the skeleton blocks in a static state until the content has loaded.

**Reduced Motion**
Skeleton animation is not essential to conveying the information that content is currently loading.
When Reduced Motion is enabled, the skeleton animation should therefore be removed. The skeleton blocks should remain visible in a static state until the content has loaded.
