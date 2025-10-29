### States

**`Enabled`** The component is interactive and ready for use. Users can type in the input or use the increment/decrement buttons.

**`Hover`** The visual appearance of the input field changes when the user hovers their mouse over it, indicating interactivity.

**`Focus`** The input field is currently selected and active, ready to receive keyboard input. A visible focus indicator (such as a border or outline) makes it clear which element is active.

**`Loading`** The component displays a loading indicator while data is being fetched or processed (e.g., updating inventory or verifying constraints in real time). Users cannot interact with the input until the loading process is complete.

**`Read only`** The input displays a value that the user cannot modify. This is useful when the quantity is set by the system or determined by external factors. Users can view the value but cannot interact with the increment, decrement, or input field.

**`Disabled`** The input is not currently available for interaction, often due to contextual constraints (e.g., an item is out of stock, or the maximum allowable quantity has been reached). The component appears grayed out and does not respond to user actions.

**`Skeleton`** The component displays a placeholder animation (skeleton screen) while waiting for content to load. This provides a visual cue that data is being fetched and helps reduce perceived wait time.