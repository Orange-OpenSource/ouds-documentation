Select the type of progress indicator based on whether progress can be measured and how long the user is expected to wait.
• Instant (< 200ms)
Do not display any indicator.
• Short (200ms – 5s)
Use an indeterminate indicator when progress cannot be measured.
• Long (> 5s)
Use a determinate indicator when progress can be measured and communicated (with progress description).

**`Determinate`** Shows the exact progress of a task, usually as a percentage from 0% to 100%. Provides clear and measurable feedback, helping users understand how long the task will take and reducing uncertainty. Use determinate indicators whenever possible. Avoid indeterminate when progress can be measured.
• The progress value is known (e.g. file upload, installation, data sync)
• The system can estimate completion time or percentage

**`Indeterminate`** Shows that a process is active without indicating exact progress. Used when the system cannot determine how long the task will take. Communicates that the system is working, even without precise data, and prevents users from thinking the interface is frozen. For long loading times (over 5 seconds), additional context must be provided. This helps inform users about the system state, reduces uncertainty, and prevents the interface from being perceived as unresponsive. User feedback and understanding of the system state (WCAG 2.2.2, 4.1.2).
• The duration is unknown or depends on external factors (e.g. waiting for server response)
• Progress cannot be reliably calculated

**Transitions** An indeterminate progress indicator may transition into a determinate state once sufficient information becomes available to calculate and communicate progress.