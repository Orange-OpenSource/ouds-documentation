Description is the optional supplementary text in an Alert Message. Use only when additional detail or guidance is needed beyond the label. It should remain short, clear and scannable, helping the user understand what happened and what they can do next.

* If you can express the message fully in the label, omit body text.
* When body text is included, limit it to one or two short sentences. This aligns with practices from major design systems: for example, the Red Hat design system recommends **1-2 sentences for the message body**. [Red Hat design system](https://ux.redhat.com/elements/alert/guidelines/?utm_source=chatgpt.com)
* **Avoid long text blocks or "long-reads" within alerts** – for detailed explanations, direct users to another view or modal. The ServiceNow "Horizon" system states that an alert message shows two lines by default, and if it exceeds two lines, provide a "Show More" link. [Horizon Design System](https://horizon.servicenow.com/workspace/components/now-alert?utm_source=chatgpt.com)
* Use plain language consistent with Orange's tone: friendly, clear, service-oriented. Avoid jargon or complex sentences. The US Web Design System emphasises "concise, human-readable language; avoid jargon and computer code." [U.S. Web Design System (USWDS)](https://designsystem.digital.gov/components/alert/?utm_source=chatgpt.com)
* Provide next-step guidance if the alert requires user action: e.g., "Try again", "Check your settings", "Contact support". If no action is required, the body text can simply explain the state.

**`False`** Label alone conveys message cleary
Example: "Payment successful."

**`True`** Label plus body text to clarify or guide – e.g., "Connection lost. Please reconnect your device to resume service."
