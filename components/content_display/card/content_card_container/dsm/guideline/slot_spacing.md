The slot allows designers to customize the content and layout inside the card, including its text, imagery, and independent actions.  
Internal padding and spacing can be adjusted using two types of spacing tokens.

**`Fixed space`** Uses a consistent spacing value across screen references. The spacing remains the same on mobile and desktop.

**`Scaled space`** Uses responsive spacing values that adapt to the screen reference. Spacing may differ between mobile and desktop to preserve the intended layout. Use the appropriate OUDS spacing tokens rather than arbitrary values to maintain consistency across layouts.

⚠️ The card container does not apply internal padding by default. Designers are responsible for defining the content padding and spacing within the slot using the appropriate OUDS spacing tokens.  
When using nested components, their own internal spacing and corner-radius rules must be preserved.