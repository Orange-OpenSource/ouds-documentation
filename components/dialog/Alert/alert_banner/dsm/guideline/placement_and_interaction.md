### Mobile reference design
• Placement: Directly below the top app bar or page header and above the related page content.  
• Width: Full available screen width.  
• Layout: Use the Start layout to keep the icon, message and optional action aligned with the screen margins.  
• Behaviour: The banner is part of the page layout and pushes the content down. It scrolls with the page and must not cover navigation or interactive elements.  
• Use the Bottom action layout when the message or action requires multiple lines.

### Tablet reference design
• Placement: Directly below the main navigation or page header.  
• Width: Full available viewport or parent-container width.  
• Layout: Use the Start layout by default. Align the inner content with the tablet grid.  
• Behaviour: The banner pushes the page content down and scrolls with the page. It is not fixed or sticky by default.  
• Use the Center layout only for short, focused messages that fit comfortably on one line.

### Desktop reference design
• Placement: Directly below the global header or primary navigation and above the main page content.  
• Width: The banner background spans the full viewport or product-container width.  
• Layout: The Center layout is recommended for web when the banner contains a short message and an optional single action.  
• Behaviour: The banner remains part of the document flow, pushes content down and scrolls with the page.  
• Use the Start layout for longer messages, descriptions, close buttons or more complex actions.

### Desktop Large reference design
• Placement: Directly below the global header or navigation.  
• Layout: Use the Center layout for short global messages. Keep the inner content centred and constrained by a maximum text width.  
• Behaviour: The banner scrolls with the page and must not remain fixed over the content by default.

Two width behaviours are supported:

### Edge to edge
• The banner background spans the full viewport width.  
• The inner content remains aligned with the page grid and uses a maximum text width. It must not stretch across the entire screen.

### Maximum width
• The complete banner has a maximum width of 1920 px and remains centred in the viewport.  
• When the viewport is wider than 1920 px, equal margins appear on both sides. The banner must not continue expanding beyond this width.  
• Use this behaviour when the rest of the product already follows a centred (header content), maximum-width layout.