### User zoom in/out
The component's height and width must be flexible, never fixed, in order to automatically adapt its dimensions according to the level of zoom (the icons follow the same rules as the text).  
In order to preserve the minimun interactive area during user zoom out, this component have a min-width and a min-height **of 28px**.

&nbsp;

### Responsive behavior of the outer border
The outer border (surrounding the “sparkles” icon) is not implemented in the same way between the design component (Figma) and the technical component.  
  • On the design side, the outer border is a vector shape, and its size scales according to the size of the component.  
  • On the technical side, the thickness of this border is calculated dynamically (there is no vector shape within the component). The calculation is based on the following:  
An inner circle of 22px  
An outer circle of 24px  
The border thickness is therefore 1px  
Thus: (1/24) * 100 = 4.16666666%
