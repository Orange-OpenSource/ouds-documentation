Controls whether the progress indicator uses motion to communicate progress.

The Animated property is available only for the Determinate variant. Indeterminate progress indicators always rely on animation and therefore do not expose this property.

**`True`** The progress indicator uses animation to communicate changes in progress. Use when progress updates over time and motion helps users understand that the process is actively advancing.
• **Start animation** Controls how the progress indicator appears when it is first displayed.
  • **`True`** The progress indicator animates from 0% to the current progress value when the component enters the screen. Use when introducing a new process and providing a smooth visual transition (for example, 0% → 50%).
  • **`False`** The progress indicator immediately displays the current progress value without an introductory animation. Use when the progress value is already known or when restoring an existing process (for example, 50%).

**`False`** The progress indicator remains static and does not animate. Use when the component represents a fixed progress value rather than an actively changing process.