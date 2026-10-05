**(for Layout=Start only)**
Description is the optional supplementary text in an Alert Banner. Use only when additional detail or guidance is needed beyond the label. It should remain short, clear and scannable, helping the user understand what happened and what they can do next.

• If you can express the message fully in the label, omit body text.
• When body text is included, limit it to one or two short sentences. This aligns with practices from major design systems: for example, the Red Hat design system recommends 1-2 sentences for the message body. Red Hat design system
• Avoid long text blocks or “long-reads” within alerts — for detailed explanations, direct users to another view or modal. The ServiceNow “Horizon” system states that an alert message shows two lines by default, and if it exceeds two lines, provide a “Show More” link. Horizon Design System
• Use plain language consistent with Orange’s tone: friendly, clear, service-oriented. Avoid jargon or complex sentences. The US Web Design System emphasises “concise, human-readable language; avoid jargon and computer code.” U.S. Web Design System (USWDS)
• Provide next-step guidance if the alert requires user action: e.g., “Try again”, “Check your settings”, “Contact support”. If no action is required, the body text can simply explain the state.

**`False`** The banner displays the label only.
Use this option for short, self-explanatory messages that do not require additional context.

**`True`** The banner displays a label and a short description.
Use this option when users need more context about the issue, its impact, or the next step.