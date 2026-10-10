The content layout defines how the banner’s icon, message, and action are positioned within the available screen width.  
Choose the layout according to the viewport size and the relationship between the banner and the page grid.

**`Start`** The banner content follows the reference screen grid, with the icon, message, and action aligned to the page margins.  
Recommended for mobile, tablet, and small desktop screens, where the available width is limited and the banner should use the space efficiently.  
Use this layout when the banner needs to remain visually connected to the surrounding interface and aligned with the rest of the page content.

**`Center`** The banner content is grouped and centred within the available width. Recommended for wide desktop screens, where keeping the message and action in a compact central area improves readability and prevents elements from becoming visually disconnected.

Use this layout for short, focused messages with an optional single action. For longer content, multiple text levels, dismissible banners, or more flexible action positioning, use the Edge-to-edge layout.

The Center layout has a simplified structure:  
• It does not support a close button.  
• Content alignment is always centred.  
• Unlike Edge-to-edge, it does not provide Top and Center alignment options.  
• It does not include an Action layout setting. The action can only be shown or hidden.  
• It does not support an additional description. Only the main label can be displayed.

⚠️ Layout: For the Center layout, set a suitable maximum content width for each breakpoint. The text and action must never touch or overflow the banner edges.