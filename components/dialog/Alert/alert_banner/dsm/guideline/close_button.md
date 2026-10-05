**(for Layout=Start only)**
The close button determines whether users can dismiss the banner.
Use it only when the message can be safely removed after being acknowledged. Functional banners that communicate an active system issue or require user awareness should remain visible until the state changes.

**`False`** The banner does not include a close button and remains visible until the underlying issue is resolved.
Use this option for high-priority system states that users must remain aware of. For example, a No internet connection banner should not be dismissible and should disappear automatically only when connectivity is restored.

**`True`** The banner includes a close button and can be dismissed after the user has read the message.
Use this option for non-critical information that does not require action and can be safely hidden without affecting the user’s understanding of the current system state.