Toast can be displayed with or without an action.  
The placement of the action depends on the amount of content and the available screen space.  
For action elements, we use the Link component with the “Text only” layout. This approach maintains visual consistency and aligns with our design system guidelines.

🔗 Link style used as a button: In this context, the link style is purely visual, it does not indicate navigation.  
• Use <a> elements for navigation.  
• Use <button> elements with the link visual style for in-app actions.

⚠️ Non-navigational usage: A link can be used to trigger an action rather than navigation (for example, opening a modal, revealing additional content, or executing a function). This pattern should only be applied when the link appearance is preferred, while ensuring the component remains accessible and its intent is clear.
