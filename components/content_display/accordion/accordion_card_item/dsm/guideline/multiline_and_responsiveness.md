**Multiline**
The Accordion card item supports multiline content. The number of lines is not limited.
The Label, Extra label, Description, Trailing text and other supported text content must wrap when there is not enough horizontal space.
The trigger expands vertically to display its complete content. Do not use a fixed height or truncate information that users need to understand the accordion section.

⚠️ Use Top alignment when the Label wraps onto multiple lines or when the card contains a Description or Bottom slot. The Expanding indicator must remain visible and must not overlap, truncate or become visually disconnected from the trigger content.
⚠️ Keep the primary Label concise. Multiline content is supported, but excessively long Labels make accordion card collections more difficult to scan.

**Max-width vs full-width**
The Accordion card item does not have a default maximum width. Its width is defined by its parent container or accordion layout.
The trigger's interactive surface extends across its complete visible width. The clickable area must not be limited to the Label or Expanding indicator.
On wide layouts, the text area may use a product-defined maximum width to maintain readability.
The Background, Divider, Hover, Pressed and Focus treatments must continue to respect the complete accordion trigger.

The Expanding indicator remains positioned according to the Reverse property:
• At the logical end when Reverse is False.
• At the logical start when Reverse is True.

Optional Leading and Trailing content must not reduce the text area to an unusable width.

⚠️ Do not apply a text maximum width that creates a large visual gap between the Label, related Trailing content and Expanding indicator. The relationship between all parts of the trigger must remain clear.

**User zoom in/out**
The Accordion card item must remain readable, operable and complete when users zoom the interface or increase the text size.

The component must adapt without clipping, overlapping or hiding meaningful information.

⚠️ Avoid combining too many optional elements. Trailing content with Hug contents may leave too little space for the Label and Description, causing excessive wrapping. Prioritise the main text area and simplify non-essential content when space is limited.

• Text must resize with the user's browser or system settings. Text resizing must not be blocked.
• The Label, Extra label, Description, Trailing text, Badge, Tag and Expanded text must wrap when required.
• The trigger must expand vertically according to its content. Do not use a fixed height.
• The complete visible trigger must remain one interactive target.
• The Expanding indicator must remain visible and must not overlap the text or move onto a separate unrelated line.
• Leading and Trailing content must remain aligned with the related text. Use Top alignment when increased text size creates multiline content.
• Optional decorative content may be simplified on narrow layouts, but meaningful statuses and supporting information must remain available.
• Do not truncate essential Labels, statuses, prices, dates or values to preserve the original desktop layout.
• Hover, Focus and Pressed treatments must adapt to the increased trigger dimensions and continue to cover the complete interactive area.
• The Expanding indicator must remain at the logical start or end according to the Reverse property after responsive reflow.
• When expanded, the revealed content must reflow independently without changing the relationship between the trigger and its content.
• The component must support longer translated content without changing its meaning or losing information.

⚠️ Do not reduce the font size, hide the Description or remove meaningful status information solely to keep the trigger on one line.