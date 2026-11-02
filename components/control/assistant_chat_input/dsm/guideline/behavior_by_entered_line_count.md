### Default display
By default, the height of the input text container is set to 60px, which allows 1 lines of text to be displayed without expanding the component.  
This height helps distinguish the field from other text inputs, prevents discouraging users with an overly large field, and keeps the layout compact at the start of a form.

• **Auto-resize (automatic expansion)**  
Above 1 lines of text, the field automatically increases in height as the user types their comment.  
This behavior is not mandatory. It is possible to enable or disable the component’s expansion depending on the page layout. In a mobile chat-type use case, for example, the height of the text area must remain fixed even if the text entered by the user exceeds 3 lines.

• **Vertical scrollbar**  
If expansion is disabled or the maximum height is reached at 240px, corresponding to about 10 lines of text, an internal scrollbar appears allowing the user to scroll through the overflowing text.  
This choice prevents breaking the layout but has the drawback, on mobile, of creating a scroll within a scroll (text area scroll inside a page scroll).

&nbsp;

### ⚠️ Old web browsers
The automatic expansion of the text area’s height based on the number of lines entered by the user is not a behavior supported by older web browsers. To address this issue, we have planned an alternative behavior for the component, which in this case has a fixed height of 144px (corresponding to about 6 lines of text), whether it is filled in or not. The selection of the appropriate expected behavior for the component is done automatically based on the version of the user’s web browser.