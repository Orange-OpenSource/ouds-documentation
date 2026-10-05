**`Close button`** The Close button allows users to dismiss the modal without completing the primary action.

The Close button may be hidden when the modal has a clear, visible alternative way to dismiss it, such as a single Cancel action or another explicit dismissal control. It may also be omitted when the modal represents a mandatory step in a controlled flow where dismissal is intentionally unavailable.

Avoid hiding the Close button when users may reasonably expect to dismiss the dialog without committing to an action. The modal must always provide an accessible and discoverable way to exit unless the flow intentionally prevents dismissal.

**`Previous`** The Previous option displays a navigation link above the title, aligned to the leading edge of the modal. It is intended for multi-step flows where users can navigate back to a previous step without dismissing the entire modal. It is not recommended to include both a subtitle and a “previous” link.

**`Subtitle`** The Subtitle option displays supporting text above the title. Use it to provide additional context or clarify the purpose of the modal when the title alone is not sufficient. It is not recommended to include both a subtitle and a “previous” link.

**`Title icon`** The Title icon displays an icon to the right of the title. It can be used either as a decorative element or to communicate a functional status, such as success, deletion, error, warning, or information.
Functional status icons may be static or animated using motion design when animation helps communicate a change of state or reinforces the meaning of the status.

**`Description`** The Description option displays supporting text below the title.
It provides additional context, instructions, or information required to understand the purpose or outcome of the modal.
The description may be omitted when the title alone provides sufficient context and the message is short and immediately understandable.

**`Slot`** The Slot provides a flexible container where you can insert custom templates, components, or other content within the modal.
Use the Slot when the standard modal content structure does not adequately support the specific use case. Content inserted into the Slot must follow the Design System's spacing and responsive guidelines.

**`Scroll bar`** Decorative element used to indicate a vertical scroll.

**`Action`** The Action option controls whether the modal displays one or more action elements. Use it when the user needs to perform an action, make a decision, or confirm the outcome of the dialog.

Actions may be omitted when the modal is purely informative and no specific user action is required. In this case, the Close button or, when appropriate, clicking outside the modal in the backdrop area can be used to dismiss the dialog.

When no action is required, ensure that the available dismissal mechanism is sufficient and clearly discoverable. For dialogs containing important information or where accidental dismissal should be avoided, a Close button should be preferred over backdrop dismissal.