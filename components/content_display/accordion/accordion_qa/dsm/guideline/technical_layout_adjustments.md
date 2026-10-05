Even though the component has a single structure in Figma for easier use by designers, its technical implementation may differ between Web and native environments to respect the layout conventions of each platform.
The Q&A trigger and its Expanded answer must remain visually aligned and clearly perceived as parts of the same question-and-answer item.

**Web (mobile, tablet, and desktop)**
The Q&A component is contained within the browser layout and follows the available container or grid width. Internal horizontal spacing follows the corresponding Web spacing tokens.

When expanded, the answer grows vertically below the trigger without changing the horizontal position of the Q&A item. The question and answer must remain aligned within the same content area.

**Native app (Android, iOS, Flutter)**
The Q&A component follows the screen and grid-margin conventions defined by the native product. Its horizontal spacing uses the corresponding native grid-margin tokens. When expanded, the answer grows vertically while maintaining the same relationship with its trigger.