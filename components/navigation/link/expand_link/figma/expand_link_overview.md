## Definition

A link expand is a UI element that reveals or hides additional content through a text link. The link expand feature is displayed through a dropdown with selectable values. It is ideal for inline contexts where minimal visual weight is needed, maintaining a clean layout while still providing access to additional information.

---

## Expanded

**`False`** State indicates that the content linked to the expand control is currently hidden. The link should suggest that additional information can be revealed.

**`True`** State indicates that the content has been revealed. The link updates visually to indicate that the section is open and can be collapsed again.

---

## States

**`Enabled`** The default state when the link is available for interaction and displayed with a clear label.

**`Hover`** The state when a user hovers over the link. Provides a visual cue that the element is interactive.

**`Focus`** The state when the link is selected via keyboard or voice commands. Typically shown with an outline or highlight to ensure accessibility.

**`Pressed`** A transient state indicating that the user has clicked the link and the action is being executed.

**`Disabled`** The state when the link is not available for interaction, such as when expanding or collapsing is not possible at the moment.

**`Skeleton`** A placeholder state that indicates where the link will appear once fully loaded. Improves perceived performance by showing upcoming interactivity.

---

## Sizes

**`Default`** This is the default size of the component.
This size is used for the vast majority of applications.

**`Small`** This size can be particularly useful in an information-dense interface or in the construction of a template or component requiring the use of small elements (in an "List item" component, for example).

---

## Density

**`Default`** This is the default density of the component, recommended for most interfaces and primary navigation contexts.
This density wich is used for the vast majority of applications, provides a comfortable touch target that meets accessibility recommendations.

**`Compact`** Reduces the vertical footprint while preserving the same interaction and visual behavior.
Use in dense layouts where space is limited and a smaller touch target is acceptable (desktop or pointer-based contexts).

---

## Specific component: On colored bg

This variant ensures a sufficiently high level of accessibility when the component is used on a background that is "out of control".

**To invert color**
* In light mode: For a black finish
* In dark mode: For a white finish

---

## Multiline and responsiveness

**Multiline**
This component allows multi-line text editing. Although the number of lines is not technically limited, it is recommended not to exceed one line of text.
Nevertheless, if the label spans multiple lines, the chevron icon remains remains vertically centred.

**Max-width vs full-width**
The max-width is applied at the label level and depends on the max-width value assigned to the typographic reference used.
Since the navigation indicator's position always remains close to the last letter of the text label (Reverse=False), it is not possible to use the "Expand link" component in a full-width context. The component cannot adapt to the parent container (or to the screen in a mobile context, for example) and occupy the full available width.
In a full-width context, you should prioritize using the "Accordion list item" component (for "Next" or "Previous" layout).

**User zoom in/out**
The behavior of the text during user zoom in/out must follow a fundamental principle: the text must remain readable, accessible, and must never break the structure or lose information.
- The text must always scale proportionally with user zoom. Text resizing must never be blocked.
- Zooming must never cause text to be truncated or hidden. The component must expand vertically to allow line wrapping.
- The component's height and width must be flexible, never fixed, in order to automatically adapt its dimensions according to the level of zoom.
- In order to preserve the minimun interactive area during user zoom out, this component have:
  - Default size: a min-width and a min-height **of 48px**
  - Small size: a min-width and a min-height **of 44px**
- Even if, the component has a max-height or a max-width for resizing control purposes, technically, during user zoom in, these limitations are not fixed but must be scalable in order to adapt to the user's zoom level.
- As the chevron icon is functional, it must follow the same rules as text.
