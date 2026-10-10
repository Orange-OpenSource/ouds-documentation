**`Enabled`** Enabled is the default state.  
The accordion card can be expanded or collapsed. The complete trigger area acts as a single control for changing the Expanded state.

**`Hover`** Hover provides visual feedback when a pointer is positioned over the accordion trigger. Apply the Hover treatment consistently to the trigger area. Hover must not move content, change the card dimensions or reveal information intended to appear only after expansion.

**`Focus`** Focus indicates that the accordion trigger is currently selected for keyboard interaction. Display one clear Focus treatment around the complete trigger area. When the card contains interactive elements inside its Expanded content, those elements receive their own Focus state independently from the accordion trigger.

**`Pressed`** Pressed is a temporary state displayed while the accordion trigger is being activated. Apply the Pressed treatment to the complete trigger area. Pressed must not resize the card or move surrounding content.

**`Disabled`** Use Disabled when the accordion section is temporarily unavailable or cannot currently be expanded. A Disabled trigger must not respond to activation.

**`Skeleton`** Use Skeleton while the card's trigger content is loading and the final information is not yet available. A Skeleton card acts as a placeholder and must not expand or collapse.