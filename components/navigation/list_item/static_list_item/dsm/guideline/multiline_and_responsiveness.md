### Multiline
• The Static list item supports multiline content without a predefined line limit.  
• The Label, Extra label, Description, Helper text and other supported text content must wrap when there is not enough horizontal space.  
• The item expands vertically to display its complete content. Do not use a fixed height or truncate essential information.  
• ⚠️ Use Top alignment when the Label wraps onto multiple lines or when the item contains a Description, Helper text or Bottom slot.  
• Leading and Trailing content must remain visually associated with the related text and must not overlap or obscure it.  
• Keep labels concise to maintain readability and make list items easier to scan.

&nbsp;

### Max-width vs full-width
The Static list item does not have a default maximum width. Its width is defined by the parent container or layout.  
On wide layouts, a product-defined maximum width may be applied to the text area to maintain readability.  
Optional Leading and Trailing content must not reduce the available text area to an unusable width.  
⚠️ Avoid excessive horizontal spacing between the Label and related Trailing content. Their visual relationship must remain clear.  
The item is non-interactive and must not behave as a navigation or action target.

&nbsp;

### User zoom in/out
The Static list item must remain readable and complete when users zoom the interface or increase the text size.  
The layout must adapt without clipping, overlapping or hiding meaningful information.  
• Text must resize with the user's browser or system settings. Text resizing must never be blocked.  
• The Label, Extra label, Description, Helper text and other supported text content must wrap when required.  
• The item must expand vertically according to its content. Do not use a fixed height.  
• Leading and Trailing content must remain aligned with the related text. Use Top alignment when increased text size creates multiline content.  
• Optional decorative content may be simplified on narrow layouts, but meaningful statuses, values and supporting information must remain available.  
• Do not truncate essential labels, statuses, prices, dates or values to preserve the original desktop layout.  
• The item must support longer translated content without losing information.  
⚠️ Do not reduce the font size, hide the Description or remove meaningful information solely to keep the item on one line.
