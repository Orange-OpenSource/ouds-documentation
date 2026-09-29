**`Enabled`** Enabled is the default state. The card is available for navigation.
The entire visible card acts as a single link target.

**`Hover`** Hover provides visual feedback when a pointer is positioned over the card.
Apply the Hover treatment to the complete card surface. It must not move content, change the card’s dimensions or reveal information required to understand the destination.

**`Focus`** Focus indicates that the complete navigation card is currently selected for keyboard interaction.
Display one clear focus indicator around the complete card target.

**`Pressed`** Pressed is a temporary state displayed while the card is being activated. Apply the Pressed treatment to the complete card surface.

**`Disabled`** Use Disabled when the destination is temporarily unavailable or cannot currently be accessed. A Disabled Navigation card item must not respond to pointer or keyboard activation and must not be included in the keyboard focus order.

**`Skeleton`** Use Skeleton while the card’s content or destination is loading and is not yet available. A Skeleton card is a placeholder and must not behave as a link or receive keyboard focus.