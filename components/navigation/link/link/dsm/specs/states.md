**`Enabled`** The status of the link before a user has interacted with it, or other content affects it.
Depending on the layout, the underline may or may not appear in this state.
In cases without an underline, the orange chevron icon or a Solaris icon signals interactivity.

**`Hover`** When a user places a pointing device over a link, but has not yet taken action on it.
The underline appears, with UI codes consistent across all components.

**`Pressed`** An intermediate state that communicates a user has taken action on a link, and that it is in the process of navigating to a destination, triggering logic, or transmitting data.
The underline appears, with UI codes consistent across all components.

**`Disabled`** Used to indicate a link that cannot be selected.
Depending on the layout, the underline may or may not appear in this state.

**`Focus`** When a user selects a link via keyboard or voice command, but has not yet taken action on it.
Mirrors the "Hover" state but includes an additional border.

**`Skeleton`** Improves the perceived loading time by providing a visual cue of where link will appear once fully loaded.
Uses the "Skeleton" component, variant "Security marge=False".