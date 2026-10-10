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

Concrete application to the Toast:

&nbsp;

### Pause, Stop, Hide
A toast that appears automatically and remains visible for more than 5 seconds may fall within the scope of this criterion, depending on its behavior.  
If the toast contains moving, blinking, scrolling, or automatically updating content that meets the criterion's conditions, users must be able to pause, stop, or hide it.  
For automatically disappearing toasts, it is recommended to provide sufficient time for users to perceive and read the message. If the toast remains visible for more than 5 seconds and its content meets the criterion's conditions, an appropriate mechanism to pause, stop, or hide the content must be provided.

&nbsp;

### Reduced Motion
The animated appearance and closing of a toast are not essential to conveying the notification itself.  
When Reduced Motion is enabled, the animated transition should therefore be removed or replaced with an instantaneous transition.  
The notification itself must remain perceivable and understandable without relying on animation.  
Default: animated appearance and closing  
Reduced Motion: instantaneous appearance and closing