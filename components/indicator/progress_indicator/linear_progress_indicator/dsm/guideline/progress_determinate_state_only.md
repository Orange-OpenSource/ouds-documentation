Controls whether the progress indicator uses motion to show activity.
Animation helps communicate that the system is actively processing.

The animated property is only available for the Determinate variant.
In the Indeterminate variant, animated = false is not supported and is therefore not exposed as a component option. Indeterminate progress indicators are specifically designed to communicate ongoing activity through motion.

**`True`** The progress indicator is static and does not move. Used to show a fixed state without suggesting ongoing activity.
• Showing a fixed value (e.g. 50%, 100%)
• Reducing motion (accessibility or low distraction)

**`False`** The progress indicator moves to show that a process is ongoing. Used to indicate active system work, especially when progress is changing or unknown (0% → 100%).
• The system is processing and needs to show activity
• It is important to reassure users that the system is not stuck