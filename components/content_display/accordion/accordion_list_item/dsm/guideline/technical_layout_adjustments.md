Even though the component structure is unique in Figma for easier use by designers, its technical implementation may differ between Web and native environments to respect the layout conventions of each platform.
The trigger and its Expanded content must nevertheless remain visually aligned and clearly perceived as parts of the same accordion section.

**Web (mobile, tablet, and desktop)**
The component is contained within the browser layout and respects its safety margins.
It therefore does not extend into the area reserved for the margin grid.
The component uses internal padding-inline, and its position follows the column structure defined by the surrounding container.
When expanded, the revealed content follows the same horizontal alignment as its associated trigger.

**Native app (Android, iOS, Flutter)**
The component may use the complete screen display area according to the native edge-to-edge layout.
Its internal padding-inline is therefore replaced by the corresponding grid-margin tokens.
The trigger and Expanded content must follow the same grid alignment so that the relationship between them remains visually clear.