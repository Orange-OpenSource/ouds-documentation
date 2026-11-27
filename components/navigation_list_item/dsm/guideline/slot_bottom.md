The Bottom slot adds a custom content area below the main row content.  
Use it when supporting information cannot be clearly represented by the standard Description or Helper text properties.  
All Bottom slot content remains part of the same navigation target.

**`False`** No additional content is displayed below the main content.

**`True`** A custom content area is displayed below the main content.

It may contain non-interactive supporting content such as:  
• A progress indicator.  
• A compact group of metadata.  
• A visual preview.  
• A status summary.  
• Product-specific supporting information.

⚠️ The Bottom slot must not contain links, buttons or other independently interactive elements.

If the supporting content requires a separate destination or action, place it outside the Navigation list item or use another component architecture.