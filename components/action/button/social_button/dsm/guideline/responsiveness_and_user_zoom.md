### Responsiveness
The Social button is an icon-only component and does not support multiline content. Its width and height remain proportional to preserve the button shape and the correct alignment of the social network icon. The component should not stretch to fill the available width. When several Social buttons are displayed together, the surrounding layout should allow them to wrap onto another line when there is not enough horizontal space, rather than reducing or compressing their size.

### User zoom in/out
• The component’s height and width must be flexible, never fixed, in order to automatically adapt its dimensions according to the level of zoom.  
• In order to preserve the minimum interactive area during user zoom out, this component have a min-width and a min-height of 48px.  
• Even if, the component has a max-height or a max-width for resizing control purposes, technically, during user zoom in, these limitations are not fixed but must be scalable in order to adapt to the user’s zoom level.  
• During user zoom, visual elements such as the icon or loader scale with the component. However, the defined padding and spacing values remain unchanged.