### Layout transformation across breakpoints
The dialog layout may technically change between breakpoints when required by the available screen space and the interaction context.  
For example, a Modal dialog may transform into a Fullscreen dialog on smaller viewports when the content or task requires more space. Similarly, a Modal dialog may transform into a Sidescreen dialog at larger breakpoints when maintaining visibility of the underlying page provides useful context.  
These transformations should preserve the same task, content hierarchy, and interaction logic while adapting the presentation to the available viewport.

&nbsp;

### Sticky action flexibility across breakpoints
The positioning of the action area can change (sticky action=True or False) across breakpoints to adapt to the available screen space and the number of actions displayed.  
This flexibility allows the action layout to adapt to the available space while preserving the same action hierarchy and interaction logic across breakpoints.

&nbsp;

### Action button appearance flexibility
The default action appearance is based on the action's hierarchy: the Primary action uses the Strong appearance, while the Secondary action uses the Default appearance.  
However, the appearance of each action can be adapted to the context. You may select another appearance, such as Negative or Minimal, when the semantic meaning of the action requires it.  
The same appearance may also be used for multiple actions when a clear primary/secondary hierarchy is not relevant. For example, two Default appearance can be used when both options should have equal visual weight and remain neutral.  
The Tertiary action is always implemented as a Link and must not be replaced with a Button. Its role is to provide a lower-emphasis action that remains visually and semantically distinct from the Primary and Secondary actions.

&nbsp;

### Title visibility
The title must always be displayed and must not be hidden.  
The title provides the dialog with a clear accessible name and allows users to immediately understand the purpose of the dialog. It is particularly important for screen reader users, who rely on the dialog's accessible name to understand the context of the content presented to them.  
Even when the message is short, the title should clearly identify the purpose or subject of the dialog.

&nbsp;

### Text max-width
The component grid specifications are identical to those of a standard page design. The maximum text widths therefore follow the same limits as those used when designing any other page.

&nbsp;

### Animation
No opening animation for this component.