Designing a progress indicator is not only about showing a progress. It is also essential to define what assistive technologies, such as screen readers, should announce to users.

Screen readers should announce the same essential information that sighted users perceive visually: what is happening, how far the process has progressed, and what remains.

**Note** Helper text is not included as part of this component. However, depending on the context in which the progress indicator is used, additional descriptive text may be required at the parent component level to provide users with meaningful context about the current process.

**`Determinate`** The system knows the exact progress value, and the loading indicator is animated. Announce the purpose of the progress indicator first (what the system is doing), followed by the current stage of completion (such as a step number or percentage), and avoid reading long sequences of individual values (for example, 1, 2, 3, 4, 5, 6) by grouping progress into clear and meaningful milestones, ideally in a limited number of steps such as 0 to 10, to reduce cognitive load and improve comprehension for screen reader users.
Recommended Screen Reader Announcement
• “Identity verification, step 1 of 2”
• “Uploading file, 50 percent complete”
• “Progress, 50 percent complete”

**`Indeterminate`** The exact progress is unknown, and the indicator is animated continuously.
Recommended Screen Reader Announcement
• “Connecting to server, please wait”