In terms of animation, there are accessibility criteria to consider: “Animation from Interactions” and “Pause, Stop, Hide.”  
These two main criteria address different issues:

&nbsp;

### Pause, Stop, Hide - WCAG 2.2.2
This concerns moving, blinking, scrolling, or automatically updating content.  
The question to ask is: does the animation start automatically and meet the criterion’s conditions?  
When a relevant animation lasts more than 5 seconds, users must be able to pause, stop, or hide it.  
The two criteria should therefore be evaluated independently.

&nbsp;

### Reduced Motion (Animation from Interactions) - WCAG 2.3.3
This primarily concerns motion-based animations triggered by user interaction.  
The question to ask is: is the movement essential to the functionality or to the information being conveyed?  
If not, the animation should be removed, reduced, or replaced when the user has enabled Reduced Motion.

ℹ️ The reduced motion preference can be configured by the user at the operating system level and is available to websites through the CSS prefers-reduced-motion media feature.

Concrete application to the List item → Illustrations or animated images (leading or trailing container):

&nbsp;

### Pause, Stop, Hide
For an animation that starts automatically and lasts more than 5 seconds, users must be able to pause, stop, or hide the animation when it is presented alongside other content.  
When the animation is short, lasting 5 seconds or less, no pause, stop, or hide control is required.

&nbsp;

### Reduced Motion
If Reduced Motion is enabled, any decorative or not essential animation that is not necessary to understand the content must be removed or replaced with a static representation.  
If an animation conveys essential information, that same information must remain available through a non-animated alternative.