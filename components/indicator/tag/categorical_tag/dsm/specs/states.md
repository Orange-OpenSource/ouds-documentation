**`Enabled`** Enabled is the default state.
Use it when the categorical information is available and current.
Because the Categorical tag is non-interactive, Enabled does not introduce hover, pressed or focus behaviour.

**`Loading`** Use Loading while the final categorical information is being retrieved or updated. The loading indicator communicates processing only.
It does not make the Categorical tag interactive.

Use case:
• Displaying status before API data is available. For example, while the system fetches the real value, the tag shows "Loading".
• Data updates or filtering. When a table or list is being updated (applying filters or refreshing data), the tag temporarily shows loading and is then replaced with the actual value.

**`Disabled`** Use Disabled when the represented information is no longer available or applicable. Disabled describes the state of the information, not the availability of an action.

Use case:
• Used when a status is no longer valid (an order is canceled and the tag is no longer meaningful).
• When the tag is part of a status system but currently has no value to display.

⚠️ Do not use Disabled only to reduce visual emphasis.

**`Skeleton`** Use Skeleton while the final Categorical tag content is not yet available.
Replace it with the final label as soon as the content is loaded.

Use case:
• Used to display the structure of the interface while waiting for data.
• Helps avoid abrupt interface changes and provides a smoother experience.