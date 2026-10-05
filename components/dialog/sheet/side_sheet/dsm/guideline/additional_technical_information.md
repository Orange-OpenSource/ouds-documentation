**Layout transformation across breakpoints**
The dialog layout may technically change between breakpoints when required by the available screen space and the interaction context.
For example, a Modal dialog may transform into a Fullscreen dialog on smaller viewports when the content or task requires more space. Similarly, a Modal dialog may transform into a Sidescreen dialog at larger breakpoints when maintaining visibility of the underlying page provides useful context.
These transformations should preserve the same task, content hierarchy, and interaction logic while adapting the presentation to the available viewport.

**Placement across breakpoints**
Although it is technically possible, the Side sheet placement should generally remain consistent across breakpoints. A Side sheet configured with a Start placement should remain anchored to the Start edge of the viewport across mobile, tablet, and desktop, and the same applies to the End placement.
Changing the placement between breakpoints should only be considered when required by a specific responsive layout or interaction pattern. In such cases, the change should be intentional and supported by a clear UX rationale rather than being used solely to accommodate available screen space.

**Sticky action flexibility across breakpoints**
The positioning of the action area can change (sticky action=True or False) across breakpoints to adapt to the available screen space and the number of actions displayed.
This flexibility allows the action layout to adapt to the available space while preserving the same action hierarchy and interaction logic across breakpoints.

**Action button appearance flexibility**
The default action appearance is based on the action's hierarchy: the Primary action uses the Strong appearance, while the Secondary action uses the Default appearance.
However, the appearance of each action can be adapted to the context. You may select another appearance, such as Negative or Minimal, when the semantic meaning of the action requires it.
The same appearance may also be used for multiple actions when a clear primary/secondary hierarchy is not relevant. For example, two Default appearance can be used when both options should have equal visual weight and remain neutral.
The Tertiary action is always implemented as a Link and must not be replaced with a Button. Its role is to provide a lower-emphasis action that remains visually and semantically distinct from the Primary and Secondary actions.

**Title visibility**
The title must always be displayed and must not be hidden.
The title provides the dialog with a clear accessible name and allows users to immediately understand the purpose of the dialog. It is particularly important for screen reader users, who rely on the dialog's accessible name to understand the context of the content presented to them.
Even when the message is short, the title should clearly identify the purpose or subject of the dialog.

**Text max-width**
There is no maximum width limit for text in this component.

**Static backdrop**
The Static backdrop parameter is optional and may be enabled or disabled depending on the use case.
When the backdrop is set to static, clicking outside the dialog does not close it. This behavior is appropriate when accidental dismissal could result in data loss, interrupt an important process, or cause the user to lose progress.
When the backdrop is not static, clicking outside the dialog may dismiss it when the interaction is considered safe to cancel.

**Animation**
When enabled, the Side sheet uses a slide-left or slide-right entrance animation rather than appearing with an immediate cut.
The Side sheet slides in from the Start or End edge of the viewport, depending on its placement, when it opens. It slides back toward the same edge when it closes. This provides a clear visual transition that helps users understand where the dialog originates from and returns to, establishing a stronger sense of spatial continuity.
Animation should respect the user's reduced-motion preferences. When reduced motion is enabled, the transition should be removed.