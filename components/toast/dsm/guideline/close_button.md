The close button controls whether users can dismiss the toast manually.  
Its presence does not necessarily determine how long the toast remains visible. A toast may still disappear automatically after an appropriate duration, unless the message is important, actionable, or requires additional reading time.

**`False`** The toast does not include a close button and disappears automatically after a short duration. Use this behavior for short confirmations or status updates that do not require user acknowledgement or interaction. The message should be easy to understand at a glance.

**Use this option for:**  
• brief confirmations  
• simple status updates  
• messages that require no action

**`True`** The toast includes a close button and remains visible until it is dismissed by the user. Use this behavior when the notification contains an action, important contextual information, or when users may need additional time to read it.

**Use this option when:**  
• the toast contains an action  
• the message contains important contextual information  
• the content is multiline or requires more time to read  
• the notification remains visible for an extended period  
• users may want to remove the toast before it disappears automatically

&nbsp;

### Automatic dismissal
Use automatic dismissal for short, non-critical messages that do not require user interaction.

**Examples:**  
• Changes saved  
• Item added to favourites  
• Connection restored

**Do not automatically dismiss a toast when:**  
• it contains an action  
• it communicates an important warning or error  
• the content requires additional reading time  
• the information is not available elsewhere

**⚠️ Note:**  
Actionable toasts should remain visible long enough for users to reach and activate the action. Important messages should remain visible until dismissed or use a persistent component instead.

&nbsp;

### Motion and timing
Toasts may disappear automatically after a short period. The display duration should depend on the amount of content and whether the toast contains an action.

A single-line toast should remain visible for approximately 3 seconds.  
A two-line toast should remain visible for approximately 5 seconds.  
A three-line toast should remain visible for approximately 7 seconds.

The enter and exit transitions should remain short and subtle, usually 1 second.