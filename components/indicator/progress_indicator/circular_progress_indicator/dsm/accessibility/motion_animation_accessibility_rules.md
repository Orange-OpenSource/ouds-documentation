In terms of animation, there are accessibility criteria to consider: “Animation from Interactions” and “Pause, Stop, Hide.”  
These two main criteria address different issues:

### Pause, Stop, Hide - WCAG 2.2.2
This concerns moving, blinking, scrolling, or automatically updating content.  
The question to ask is: does the animation start automatically and meet the criterion’s conditions?  
When a relevant animation lasts more than 5 seconds, users must be able to pause, stop, or hide it.  
The two criteria should therefore be evaluated independently.

### Reduced Motion (Animation from Interactions) - WCAG 2.3.3
This primarily concerns motion-based animations triggered by user interaction.  
The question to ask is: is the movement essential to the functionality or to the information being conveyed?  
If not, the animation should be removed, reduced, or replaced when the user has enabled Reduced Motion.

ℹ️ The reduced motion preference can be configured by the user at the operating system level and is available to websites through the CSS prefers-reduced-motion media feature.

Concrete application to the Progress Indicator:

### Pause, Stop, Hide
When an animated loader starts automatically and remains active for more than 5 seconds, the criterion must be taken into account.  
Two approaches can be considered:  
• Use a static indicator directly (such as an hourglass icon), accompanied, where possible, by descriptive text such as “Loading…”.  
• Use the animated loader for a maximum of 5 seconds, then replace it with a static indicator accompanied, where possible, by descriptive text.

### Reduced Motion
Loader animation is generally not essential to conveying the information that loading is in progress.  
When Reduced Motion is enabled, the animated loader should therefore be replaced with a static loading indicator (such as an hourglass icon, for example) and, when relevant, with a text alternative such as “Loading…”.  
The loading state must remain understandable without relying on animation.

In both cases, the loading status must remain understandable and, when relevant, be exposed to assistive technologies (e.g. through a vocalized label).
