Controls whether additional text is displayed with the progress indicator.
Helper text can provide context about the process or show the current progress value.
• Helper text should be short, specific.
• For indeterminate progress, use action-oriented labels with progressive verbs, such as Verifying identity or Connecting to server.
• Do not display numbers or percentages when the completion time is unknown.
• An ellipsis (…) may be added when the process is expected to complete within one or two seconds.
• For determinate progress, display the current completion status using a percentage (40% or 40% complete) or, when relevant, a step indicator (Step 3 of 5).
• If the process takes longer than expected, update the message to reassure users, for example Still verifying your identityor This may take a few minutes.
• In the French version, a non-breaking space must always be inserted between the number and the percent sign (40 %).

**Helper text**
**`True`** Displays helper text alongside the progress indicator.
**`False`** No helper text is displayed.

**Percentage (Determinate states only)**
**`True`** Shows the current value (e.g. “0%”). Used with determinate progress only.
**`False`** Text explains what is happening (e.g. “Uploading files”)

**Percentage + Description (Determinate states only)** Shows the current value (e.g. “0%”). Used with determinate progress only.
**`True`** Displays both the percentage and a short description.
**`False`** Displays the percentage only.

**Space before % (Determinate states only)** Controls whether a space is inserted between the number and the percent sign.
**`True`** Displays a space before the percent sign (e.g. 40 %)
Languages such as English, Spanish, and Italian typically do not use a space before the percent sign.
**`False`** Displays the percent sign immediately after the number (e.g. 40%) Use this property according to the typographic conventions of the language used in the interface.
Languages such as French, Russian, German, Polish, and many other European languages require a space before the percent sign.
