**`Enabled`** Enabled is the default state. The item is available for navigation.  
The entire item acts as a single link target.

**`Hover`** Hover provides visual feedback when a pointer is positioned over the item. Hover must not move content, change the item’s dimensions or reveal information required to understand the destination.

**`Focus`** Focus indicates that the entire navigation item is currently selected for keyboard interaction. Display one clear focus indicator around the complete navigation target.

**`Pressed`** Pressed is a temporary state displayed while the item is being activated. Apply the pressed treatment to the entire navigation target.

**`Disabled`** Use Disabled when the destination is temporarily unavailable or cannot currently be accessed. A Disabled navigation item must not respond to pointer or keyboard activation and must not be included in the keyboard focus order.

**`Skeleton`** Use Skeleton while the navigation item’s content or destination is loading and is not yet available. A Skeleton item is a placeholder and must not behave as a link or receive keyboard focus.