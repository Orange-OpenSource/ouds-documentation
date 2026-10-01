• A higher-priority toast is displayed before a lower-priority toast.
• When several notifications have the same priority, display them in the order in which they were triggered. This is a first in, first out queue.
• Before displaying a queued toast, verify that its information is still relevant. Do not display outdated confirmations or messages that have already been replaced by a newer system state.

**Stack behaviour**
The highest-priority toast remains closest to the placement edge.
• For top positions, the stack grows downwards.
• For bottom positions, the stack grows upwards.
• A fourth toast remains in the queue until space becomes available.

| Priority | Toast type | Auto-dismiss | Behaviour |
|---|---|---|---|
| 1 | Actionable Negative | No | Takes priority over every other toast. A visible lower-priority toast may be interrupted and returned to the queue if it is still relevant. |
| 2 | Negative | No by default | Appears before Warning, Positive, Info and Neutral notifications. Messages of the same priority follow the queue order. |
| 3 | Actionable Warning | No | Appears before non-actionable warnings and all lower-priority statuses. |
| 4 | Warning | No by default | Appears before Positive, Info and Neutral notifications. Auto-dismiss may only be used when the information is available elsewhere. |
| 5 | Actionable Positive | No | Remains visible until the user performs the action or dismisses the toast. |
| 6 | Actionable Info | No | Remains visible until the user performs the action or dismisses the toast. |
| 7 | Actionable Neutral | No | Remains visible until the user performs the action or dismisses the toast. |
| 8 | Positive | Optional | Waits behind actionable, Negative and Warning notifications. Combine repeated confirmations whenever possible. |
| 9 | Info | Optional | Waits behind higher-priority notifications. Do not interrupt an important or actionable toast. |
| 10 | Neutral | Optional | Uses the lowest queue priority. It may be discarded when the information is no longer relevant. |