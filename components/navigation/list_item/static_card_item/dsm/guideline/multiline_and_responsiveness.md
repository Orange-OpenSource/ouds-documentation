**Multiline**
The Static card item supports multiline content. The number of lines is not limited.
The Label, Extra label, Description, Helper text and supported text content must wrap when there is not enough horizontal space.
The item expands vertically to display its complete content. Do not use a fixed height or truncate information that users need to understand the destination.

⚠️ Use Top alignment when the Label wraps onto multiple lines or when the item contains a Description, Helper text or Bottom slot. The navigation indicator must remain visible and must not overlap, truncate or become visually disconnected from the destination label.
⚠️ Keep the destination Label concise. Multiline content is supported, but excessively long labels make navigation lists more difficult to scan.

**Max-width vs full-width**
The Static card item does not have a default maximum width. Its width is defined by its parent container or navigation layout.
The item’s interactive surface extends across its complete visible width. The clickable area must not be limited to the Label or navigation indicator.
On wide layouts, the text area may use a product-defined maximum width to maintain readability. The item’s background, divider, hover, pressed and focus treatments must still cover the complete navigation target.

The navigation indicator remains positioned at the logical edge of the item:
• At the logical end for the Next layout.
• At the logical start for the Previous layout.

Optional Leading and Trailing content must not reduce the text area to an unusable width.
⚠️ Do not apply a text maximum width that creates a large visual gap between the Label and related Trailing content. The relationship between all parts of the item must remain clear.

**User zoom in/out**
The card item must remain readable, operable and complete when users zoom the interface or increase the text size.
The component must adapt without clipping, overlapping or hiding meaningful information.

⚠️ Avoid combining too many optional elements. Trailing content with Hug contents may leave too little space for the Label and Description, causing excessive wrapping. Prioritise the text area and remove non-essential content when space is limited.

• Text must resize with the user’s browser or system settings. Text resizing must not be blocked.
• The Label, Extra label, Description, Helper text, Trailing text, Badge and Tag must wrap when required.
• The item must expand vertically according to its content. Do not use a fixed height.
• The entire visible item must remain one interactive target. Zoom must not reduce the clickable area to the Label or navigation indicator.
• The navigation indicator must remain visible and must not overlap the text or move onto a separate unrelated line.
• Leading and Trailing content must remain aligned with the related text. Use Top alignment when increased text size creates multiline content.
• Optional decorative content may be simplified on narrow layouts, but meaningful status, destination and supporting information must remain available.
• Do not truncate essential destination labels, statuses, prices, dates or values to preserve the original desktop layout.
• Focus, hover and pressed treatments must adapt to the expanded item dimensions and continue to cover the complete navigation target.
• In the Previous layout, the navigation indicator remains at the logical start. Leading content is not supported, including after responsive reflow.
• In the Next layout, the navigation indicator remains at the logical end. Leading content may be retained when it does not prevent the Label from reflowing correctly.
• The component must support longer translated content without changing its meaning or losing information.

⚠️ Do not reduce the font size, hide the Description or remove meaningful status information solely to keep the item on one line.