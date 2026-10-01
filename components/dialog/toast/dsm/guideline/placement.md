**Mobile reference design**
• Constraints: Left & right + Bottom
• Spacing: 8 px from both screen edges and 8 px above the bottom navigation or another persistent element.
• Use this position for feedback directly related to a recent action, especially when the action happened near the bottom of the screen.
• For the sm reference, the toast width follows the grid: it spans 10 of 12 columns, instead of using fixed 8 px side margins like 2xs and xs.

⚠️ The toast must not cover important content or controls. If a floating button, navigation bar, or sticky element is already in the same area, place the toast above it or use another position.
⚠️ On mobile reference, the toast takes almost the full screen width and does not follow the grid, unlike on other screen references.

**Tablet reference design**
Maximum width:
md 8 of 12 grid columns
lg 6 of 12 grid columns

**Top center**
• Constraints: Center + Top
• Spacing: 16 px from the top of the viewport.
Align the toast with the four central grid columns.
• Use this position as the default for narrow web layouts, tablets, forms, and pages with a centered content column.
It keeps the message visually connected to the main task without making it feel like a separate system notification.

**Bottom center**
• Constraints: Center + Bottom
• Spacing: 24 px from the bottom of the viewport.
Align the toast with the four central grid columns.
• Use this position when the message is directly related to an action performed near the bottom of the page. It is suitable for brief action feedback, such as confirming that a comment was added or an item was moved.

**Desktop/Desktop Large reference design**
Maximum width: 4 of 12 grid columns

**Top center**
• Constraints: Center + Top
• Spacing: 16 px from the top of the viewport.
Align the toast with the four central grid columns.
• Use this position for centered layouts, forms, checkout flows, or focused tasks with a clear central content area.
Use it as a  default desktop position.

**Top right**
• Constraints: Right + Top
• Spacing: 16 px from the top.
Align the toast with the four rightmost grid columns. Its right edge must align with the last grid column.
• Use this as the default desktop position for system feedback, save confirmations, uploads, and background process updates.

**Bottom center**
• Constraints: Center + Bottom
• Spacing: 32 px from the bottom of the viewport.
Align the toast with the four central grid columns.
• Use this position when the message is directly related to an action performed near the bottom of the page. It is suitable for brief action feedback, such as confirming that a comment was added or an item was moved.

**Bottom right**
• Constraints: Right + Bottom
• Spacing: 32 px from the bottom of the viewport.
• Align the toast with the four rightmost grid columns. Its right edge must follow the grid boundary and keep the responsive layout margin from the viewport edge. Use this position when the top-right area is occupied or when the product already uses a consistent bottom-right notification pattern.

⚠️ Avoid it when this area contains a chat widget, help button, floating action button, or sticky panel.