**Default behaviour**
• Display only one toast at a time.
• When several notifications are triggered, place them in a queue. The currently visible toast must complete its exit transition before the next toast enters. Entrance and exit animations must not overlap.
• This sequential behaviour reduces visual interruption, prevents content from being obscured and makes each message easier to identify.

**⚠️ Multiple visible toasts**
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