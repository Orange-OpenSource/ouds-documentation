### ⚠️ Multiple visible toasts
Displaying several toasts at the same time is not recommended. A stack can interrupt the user, obscure interface content and make important messages harder to notice.

Maintain an 8 px gap between each toast in the stack.

When a stack is necessary:  
• display a maximum of three toasts  
• order them according to their priority  
• keep any additional notifications in the queue  
• do not display repeated messages of the same type simultaneously  
• ensure that the stack does not cover navigation, focused elements or important controls  
• prefer a single visible toast on mobile whenever possible

A fourth notification must remain in the queue until a visible toast is dismissed or disappears.
