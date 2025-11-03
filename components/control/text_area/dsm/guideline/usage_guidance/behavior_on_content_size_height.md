### Behavior on content size (height)

• **Default display** By default, the height of the input text container is set to 72px, which allows 3 lines of text to be displayed without expanding the component. This height helps distinguish the field from other text inputs, prevents discouraging users with an overly large field, and keeps the layout compact at the start of a form.

• **Auto-resize (automatic expansion)** Above 3 lines of text, the field automatically increases in height as the user types their comment.

• **Vertical scrollbar** If expansion is disabled or the maximum height is reached at 240px, corresponding to about 10 lines of text, an internal scrollbar appears allowing the user to scroll through the overflowing text. This choice prevents breaking the layout but has the drawback, on mobile, of creating a scroll within a scroll (text area scroll inside a page scroll).

**⚠️ No manual resize (by the user)** On both desktop and mobile, we have chosen to disable manual resizing to avoid behaviors inconsistent with the design system.