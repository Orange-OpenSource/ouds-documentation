### Leading actions / Trailing actions
The "Bottom actions" section consists of two independent groups. The group at the beginning ("Leading actions") contains, by default, icon buttons for additional customizable options, as well as a component slot. The group at the end ("Trailing actions") contains the "send" action button, which is not customizable and must never be hidden.

&nbsp;

### Leading and trailing groups
The Bottom actions instance contains leading and trailing action groups. Each group can be shown or hidden independently.

&nbsp;

### Action 1 / Action 2 / Action 3
Show or hide each primary action independently. The default options provided can be customized on a per-project basis.

&nbsp;

### Slot
A dedicated slot is provided within the "Bottom actions" area to accommodate custom content. This is distinct from the content slot associated with the input field.  
This slot is disabled by default. It is not a "content-slot" property located at the root of the chat input component. Any custom content inserted into this slot will appear between the action groups.

&nbsp;

### Trail action
The final "send" action button cannot be customized and must never be hidden, for accessibility reasons.

&nbsp;

### Individual trailing actions
The final "send" action button cannot be customized and must never be hidden, in order to meet accessibility requirements.

Configuration shown here is made through the nested Bottom actions instance. Keep the sending action identifiable and remove actions that have no useful function in the conversation.