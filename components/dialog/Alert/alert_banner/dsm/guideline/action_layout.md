**(for Layout=Start only)**  
Alerts can be displayed with or without an action.  
The placement of the action depends on the amount of content and the available screen space.  
For action elements, we use the Link component with the “Text only” layout. This approach maintains visual consistency and aligns with our design system guidelines.

🔗 Link style used as a button: In this context, the link style is purely visual, it does not indicate navigation.  
• Use <a> elements for navigation.  
• Use <button> elements with the link visual style for in-app actions.

⚠️ Non-navigational usage: A link can be used to trigger an action rather than navigation (for example, opening a modal, revealing additional content, or executing a function). This pattern should only be applied when the link appearance is preferred, while ensuring the component remains accessible and its intent is clear.

**`None`** Used when the banner communicates a system state but no user action is required.  
Suitable for messages that only inform users about the current state, such as a temporary service limitation or a restored connection.

**`Trailing`** Used when the action is positioned at the end of the message.  
Recommended for wide layouts, short messages, and short CTAs that can remain on a single line. This layout keeps the banner compact and makes the action immediately visible.  
Avoid the trailing layout when the message or CTA wraps onto several lines, as this may reduce readability and create an unbalanced layout.

**`Bottom`** Used when the action is positioned below the main message. The bottom layout gives the message and action enough room to wrap independently. It improves readability and prevents the CTA from competing with the main content for horizontal space.

**Recommended for:**  
• mobile and narrow layouts;  
• messages that span multiple lines;  
• long or descriptive CTAs;  
• translated content that may require more horizontal space.