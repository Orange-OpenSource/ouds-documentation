### Behavior for content lines

The text area component adapts its height behavior based on the amount of content entered:

**1. Fixed height < 3 lines**
For inputs with minimal content (up to 3 lines), the text area maintains a fixed height, providing a compact and consistent layout.

**2. Auto-expansion from 4 to 10 lines**
When the content grows beyond 3 lines, the text area automatically expands to accommodate up to 10 lines. This progressive expansion ensures that users can see their input without needing to scroll, maintaining readability and a smooth user experience.

**3. Internal scroll > 10 lines**
Once the content exceeds 10 lines, the text area stops expanding and activates an internal scroll. This prevents the component from occupying excessive vertical space while still allowing users to navigate through their text comfortably.