Alerts can be displayed with or without an action.
The placement of the action depends on the amount of content and the available screen space.
For action elements, we use the Link component with the "Text only" layout. This approach maintains visual consistency and aligns with our design system guidelines.

**🔗 Link style used as a button:** In this context, the link style is purely visual, it does not indicate navigation.
• Use <a> elements for navigation.
• Use <button> elements with the link visual style for in-app actions.

**⚠️ Non-navigational usage:** A link can be used to trigger an action rather than navigation (for example, opening a modal, revealing additional content, or executing a function). This pattern should only be applied when the link appearance is preferred, while ensuring the component remains accessible and its intent is clear.

**`Bottom action`** Used when the action is placed below the main message content. **Recommended for mobile** or narrow layouts, or when the text spans multiple lines. This vertical structure improves clarity and ensures the action remains visible after the message is read.

**`Trailing action`** Used when the action is positioned to the right of the message. Best suited for wider layouts or short, single-line alerts where horizontal alignment keeps content compact and balanced.

**`Without action`** Used when no user action is required. Ideal for informational alerts that simply convey status or feedback without any interaction.