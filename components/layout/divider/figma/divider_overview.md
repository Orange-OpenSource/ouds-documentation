## Definition

A divider is a UI element that structures content by visually separating different areas. The divider enhances readability and organises content without creating a stronger visual hierarchy, such as a heading or container.

---

## Orientation

**`Horizontal`** Separates stacked vertical sections. Example use case: Between main content and a footer.

**`Vertical`** Separates horizontally aligned elements. Example use case: Between two columns in a layout.

---

## Authorized colors

• color-border-default  
• color-border-muted  
• color-border-emphasized  
• color-border-brand-primary (secondary/tertiary)  
• color-border-on-brand-primary (secondary/tertiary)  
• color-always-black  
• color-always-white  
• color-always-on-black  
• color-always-on-white

---

## Behaviour and interactions

• Semantics and Structure
Use the <hr> (Horizontal Rule) tag when the separator has semantic meaning, i.e., when it represents a topic change or a significant transition in the content.
Use a styled <div> if the divider is purely decorative, ensuring it is hidden from assistive technologies (e.g., aria-hidden="true").

• Compatibility with Assistive Technologies
If <hr> is used, provide a textual alternative if necessary via aria-label or aria-labelledby to specify its role (e.g., <hr aria-label="End of introduction section">).
If the divider is decorative, ensure it is not perceived as content by screen readers (role="presentation" or aria-hidden="true").

• Size and Spacing
A divider that is too thin may be invisible on some screens, so favor a thickness of at least 1px to 2px.
Maintain sufficient margin around the divider to prevent visual clutter and improve readability (e.g., margin: 16px 0;).

• Keyboard Accessibility and Interactions
A divider should not be focusable (tabindex="-1") unless it has an interactive role (which is rare).
If the divider is part of an interactive component (e.g., dropdown menu, accordion panel), ensure it does not interfere with keyboard navigation.
