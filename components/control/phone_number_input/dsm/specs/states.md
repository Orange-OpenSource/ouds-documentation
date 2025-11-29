**`Enabled`** The default state when the user can interact with the text input. The field is ready to accept input when the user clicks or taps on it.

**`Hover`** Triggered when the user hovers the cursor over the input. This state provides visual feedback, signaling that the field can be interacted with.

**`Focus`** Activated when the user clicks or taps into the input, indicating that the field is currently selected and ready for input. This state is critical for accessibility, as it shows exactly where the user's focus is within the form.

**`Loading`** The component displays a loading indicator to inform the user that a process is underway, such as validating the input. The input remains disabled during this time.

**`Read only`** The input contains data but is not editable. This state is useful for displaying pre-filled data that the user shouldn't alter, like information pulled from a database or data confirmed in a previous step.

**`Disabled`** The input is inactive and cannot be interacted with. This state indicates that the field is currently unavailable, such as in cases where a required previous action has not been completed.

**`Skeleton`** A placeholder state to indicate that content is loading or being fetched. Useful in maintaining the layout structure while the actual data is being retrieved, providing a smooth user experience during initial page loads.