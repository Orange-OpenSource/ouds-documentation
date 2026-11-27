**`Loading`** Loading indicates that an action triggered by the card is currently being processed. During this state, the card must not accept additional interactions. By default, the card content is hidden by the action/support/loading overlay, and a Progress indicator is displayed.  
In Figma, designers must set the loading overlay opacity to 100% to fully hide the underlying content.

For specific use cases, designers may customize the slot composition to preserve the existing content and display a Progress indicator over it. Loading should only be applied to the card performing an action. When multiple cards are waiting for content to load, use the Skeleton state instead.

In the Loading state, the card must provide sufficient space to display the Progress Indicator without clipping.
