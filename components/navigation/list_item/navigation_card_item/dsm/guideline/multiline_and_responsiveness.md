### Multiline
The Navigation card item supports multiline content. The number of lines is not limited.  
The Label, Extra label, Description, Helper text and supported text content must wrap when there is not enough horizontal space.  
The card expands vertically to display its complete content. Do not use a fixed height or truncate information that users need to understand the destination.

⚠️ Use Top alignment when the Label wraps onto multiple lines or when the card contains a Description, Helper text or Bottom slot.  
The affordance indicator must remain visible and must not overlap, truncate or become visually disconnected from the destination label.

⚠️ Keep the destination Label concise. Multiline content is supported, but excessively long labels make card collections more difficult to scan.

### Max-width vs full-width
The Navigation card item does not have a default maximum width. Its width is defined by its parent container, grid or card-based layout.  
The card’s interactive surface extends across its complete visible width and height. The clickable area must not be limited to the Label or affordance indicator.  
On wide layouts, the text area may use a product-defined maximum width to maintain readability. The card’s background, outline, Hover, Pressed and Focus treatments must still cover the complete navigation target.

The affordance indicator remains positioned at the logical edge of the card:  
• At the logical end for the Next layout.  
• At the logical start for the Previous layout.

Optional Leading and Trailing content must not reduce the text area to an unusable width.

⚠️ Do not apply a text maximum width that makes the relationship between the card’s Label, secondary content and affordance indicator unclear.

### User zoom in/out
The Navigation card item must remain readable, operable and complete when users zoom the interface or increase the text size.

⚠️ Avoid combining too many optional elements. Trailing content with Hug contents may leave too little space for the Label and Description, causing excessive wrapping. Prioritise the text area and remove non-essential content when space is limited.

• The component must adapt without clipping, overlapping or hiding meaningful information.  
• Text must resize with the user’s browser or system settings. Text resizing must not be blocked.  
• The Label, Extra label, Description, Helper text, Trailing text, Badge and Tag must wrap when required.  
• The card must expand vertically according to its content. Do not use a fixed height.  
• The entire visible card must remain one interactive target. Zoom must not reduce the clickable area to the Label or affordance indicator.  
• The affordance indicator must remain visible and must not overlap the text or move onto a separate, unrelated line.  
• Leading and Trailing content must remain aligned with the related text. Use Top alignment when increased text size creates multiline content.  
• Optional decorative content may be simplified on narrow layouts, but meaningful status, destination and supporting information must remain available.  
• Do not truncate essential destination labels, statuses, prices, dates or values to preserve the original desktop layout.  
• Focus, Hover and Pressed treatments must adapt to the expanded card dimensions and continue to cover the complete navigation target.  
• In the Previous layout, the affordance indicator remains at the logical start. Leading content is not supported, including after responsive reflow.  
• In the Next layout, the affordance indicator remains at the logical end. Leading content may be retained when it does not prevent the Label from reflowing correctly.  
• The component must support longer translated content without changing its meaning or losing information.

⚠️ Do not reduce the font size, hide the Description or remove meaningful status information solely to keep the card on one line.