**Keyboard Navigation**
Tab – Move focus between Chips.
Space / Enter – Activate a Chip (select a filter).
Backspace / Delete – Remove a focused Chip (if dismissible).
Arrow Keys – Navigate through Chips in a group.

**Accessibility aria**
Use aria-selected for selected Chips.
Add aria-label for the close button (Remove {chip content}).
Selectable Chips should be announced as radio button or checkbox for screen readers.

**Visible Focus**
When navigating via keyboard (Tab key), chip must display a visible focus style.

**Microcopy Guidelines**
Chip text should be concise and precise.
The ideal length is one word, max width: 20 characters or 1 to 3 words.
Text should not wrap or be truncated.

**Layout and Arrangement**
Wrapping: Chips are often arranged using a Wrap widget, allowing them to flow within a container and wrap to the next line when needed.
Spacing: Proper spacing between chips and between lines of chips ensures a clean and uncluttered layout.

**Interaction**
Avoid placing more than two rows of Chips to prevent overwhelming users.
Do not use Chips for navigation; use buttons instead.

**Responsiveness**
When the screen resolution changes or the device's scaling settings are adjusted, text-based Chips will adapt by increasing or decreasing in size, while icon-only Chips remain the same size.

**Color Contrast (Applicable for Enabled, Hover, and Focus States)**
Proper contrast ensures accessibility, especially for visually impaired users. Chips should meet WCAG 2.1 AA standards:
* Text Contrast: Minimum 4.5:1 against the background.
* Icon Contrast: At least 3:1 for visibility.

**Screen Reader Accessibility**
For Chips, designers must provide a clear and understandable description for screen readers to ensure accessibility for users who rely on assistive technologies. This is especially important for icon-only Chips.
Additionally, Chips with text should include extra descriptions when necessary to help users understand the context.
By following these principles, designers ensure that icon-only Chips remain accessible and provide a seamless user experience for all, including those who use VoiceOver, TalkBack, and other screen readers.

**Screen Reader Accessibility in Chip Groups**
For Chip groups, it is important to first define the group container with a context explanation for screen readers before assigning labels to each individual Chip. This helps users of assistive technologies, such as VoiceOver and TalkBack, correctly perceive the Chips as a unified set.
