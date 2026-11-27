**1 (single action)**  
A single action button is centered horizontally within the modal on mobile, tablet, and desktop. The action button can use either “fill” (especially on mobile devices) or “hug” behavior in Auto Layout.  
Use this configuration when there is one clear action available to the user.

**2 (primary and secondary actions)**  
Two actions are provided: a Primary action and a Secondary action.  
On mobile, the actions can either be stacked vertically or aligned horizontally. In both cases, each component can use either “fill” or “hug” behavior in Auto Layout.  
On tablet and desktop, the actions are positioned horizontally and aligned to the trailing edge of the modal. Each actions are configured to “hug” behaviour in Auto Layout.  
The Primary action should represent the preferred or most important outcome, while the Secondary action provides an alternative or less prominent option.

**3 (primary, secondary, and tertiary actions)**  
Three actions are provided: a Primary action, a Secondary action, and a Tertiary action presented as a link.  
On mobile, all three actions can either be stacked vertically or aligned horizontally. In both cases, each component can use either “fill” or “hug” behavior in Auto Layout.  
On tablet and desktop, the Primary and Secondary actions are positioned on the trailing edge of the modal, while the Tertiary action is positioned on the leading edge and aligned with the modal content. Each actions are configured to “hug” behaviour in Auto Layout.

**ℹ️ Note (Mobile layout=True):**  
On mobile (grid: 2xs, xs, sm), the “alignment” variant (available from 2 actions onwards) allows you to configure the actions to be positioned either vertically or horizontally.  
In both cases, each component can use either “fill” or “hug” behavior in Auto Layout.  
This “alignment” variant is available whether “Sticky action” is set to True or False.

**ℹ️ Note (Mobile layout=False):**  
On tablet or desktop, the “alignment” variant is not available.  
The Auto Layout setting for the action components is configured to “hug”. This setting cannot be changed.  
• For 1 action: the element is centered in the modal.  
• For 2 actions: the elements are aligned to the right of the modal.  
• For 3 actions: 1 element is aligned to the left and the other 2 are aligned to the right.

&nbsp;

### ⚠️ Accessibility (action order)
The visual order of actions must not change their semantic or interaction order.  
For screen reader and keyboard users, the implementation must preserve the following priority order:  
Primary → Secondary → Tertiary

On tablet or desktop, the visual order may be:  
Tertiary → Secondary → Primary

The DOM and accessibility tree should therefore expose the actions in priority order, even when CSS or layout positioning visually places the Tertiary action on the left. Do not rely on visual order alone to determine the reading or focus order.  
This ensures that assistive technology users encounter actions in the same logical order as users interacting with the mobile layout.