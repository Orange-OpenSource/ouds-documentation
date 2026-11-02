**`Enabled`** The default state. The entire card is available for interaction and displays its content normally.

**`Hover`** Indicates that the pointer is positioned over the card.  
Use it to provide visual feedback that the card is interactive.

**`Focus`** Indicates that the card has received keyboard focus. The focus indicator must remain clearly visible around the complete card to support keyboard navigation and accessibility.

**`Pressed`** Provides immediate visual feedback while the user is pressing or activating the card.

⚠️ After activation, the card can follow only one interaction pattern.  
• Action or navigation: the card triggers an action or destination, behaving as a button or link.

**`Loading`** Loading indicates that an action triggered by the card is currently being processed. During this state, the card must not accept additional interactions. By default, the card content is hidden by the action/support/loading overlay, and a Progress indicator is displayed.  
In Figma, designers must set the loading overlay opacity to 100% to fully hide the underlying content.

For specific use cases, designers may customize the slot composition to preserve the existing content and display a Progress indicator over it. Loading should only be applied to the card performing an action. When multiple cards are waiting for content to load, use the Skeleton state instead.

In the Loading state, the card must provide sufficient space to display the Progress Indicator without clipping.

**`Disabled`** Indicates that the card is temporarily unavailable for interaction.

When a card is disabled, all content within the card must visually reflect the disabled state to maintain a consistent hierarchy and clearly communicate that the entire card is unavailable. Interactive or status elements such as buttons, tags, badges, links, or other components should use their corresponding Disabled state when available. Typography should use the appropriate disabled color tokens, while images and illustrations should use the defined disabled opacity.

The card and its content must not respond to user interaction while disabled.

**`Skeleton`** Represents the card while its content is not yet available.  
Use Skeleton when loading the initial content of a card or when multiple cards are loading at the same time, such as when displaying a list, grid, search results, or a page containing several cards.

Unlike the Loading state, Skeleton represents content that has not yet been loaded, rather than feedback for an action already initiated by the user.