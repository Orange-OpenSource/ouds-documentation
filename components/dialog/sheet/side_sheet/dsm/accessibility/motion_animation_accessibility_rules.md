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

Concrete application to the Sheet:

&nbsp;

### Pause, Stop, Hide
Sheet animations are triggered by a user action and do not generally fall within the scope of this criterion.  
However, if a sheet contains moving, blinking, scrolling, or automatically updating content, that content must be evaluated separately.

&nbsp;

### Reduced Motion
The appearance and closing animation of a sheet are not essential to its functionality or to understanding its content.  
When Reduced Motion is enabled, the animated transition should therefore be removed or replaced with an instantaneous transition.  
Default: animated appearance and closing  
Reduced Motion: instantaneous appearance and closing